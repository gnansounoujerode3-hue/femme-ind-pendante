"""Construit l'ebook « Se réveiller, pas subir ».

- chaque fichier de content/ est une section rendue indépendamment
  (les sauts de page sont donc explicites et maîtrisés) ;
- les fichiers nommés pN-*.html sont des ouvertures de partie (fond nuit) ;
- <!--KEY:xx-->   déclare la clé de page, utilisée dans le sommaire
  par le jeton __PAGE_xx__ ;
- <!--BM:n|Titre--> crée un signet PDF de niveau n.
"""
import os
import re

import pymupdf

import paginate as P

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = pymupdf.Archive(os.path.join(HERE, "ttf"))
CSS = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
CSS_DARK = open(os.path.join(HERE, "style-dark.css"), encoding="utf-8").read()

PAGE = pymupdf.paper_rect("a5")
ML, MR, MT, MB = 42, 42, 46, 50
AREA = PAGE + (ML, MT, -MR, -MB)

NAVY = (0.078, 0.141, 0.247)
TERRA = (0.690, 0.322, 0.184)
GOLD = (0.914, 0.643, 0.447)
CREAM = (0.976, 0.953, 0.925)

TMP = os.path.join(HERE, "_tmp.pdf")


def blocks(css):
    """Découpe une feuille CSS en blocs de premier niveau."""
    out, depth, start = [], 0, 0
    for i, ch in enumerate(css):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                out.append(css[start:i + 1].strip())
                start = i + 1
    return out


def story_pages(html, css):
    story = pymupdf.Story(html=html, user_css=css, archive=FONTS)
    writer = pymupdf.DocumentWriter(TMP)
    dev = writer.begin_page(PAGE)
    story.place(AREA)
    story.draw(dev)
    writer.end_page()
    writer.close()
    return pymupdf.open(TMP)


def story_links(html, css):
    """Rendu simple ; les liens internes sont posés après assemblage
    (MuPDF ne résout pas les ancres situées après le lien)."""
    return story_pages(html, css)


def is_dark(name):
    return bool(re.match(r"p\d-\d\d-partie", name))


def render_path(path, source=""):
    name = source or os.path.basename(path)
    dark = is_dark(name)
    raw = open(path, encoding="utf-8").read()
    html = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    css = CSS + ("\n" + CSS_DARK if dark else "")
    pages = P.paginate(html, css, AREA.width, AREA.height, FONTS)
    out = pymupdf.open()
    for pg_html in pages:
        tmp = story_links(pg_html, css)
        for i in range(tmp.page_count):
            page = out.new_page(width=PAGE.width, height=PAGE.height)
            page.draw_rect(page.rect, color=None, fill=NAVY if dark else CREAM)
            page.show_pdf_page(page.rect, tmp, i)
    return out


def _spot_spans(page):
    """Fragments numériques écrits dans la couleur marqueur, en ordre de lecture."""
    out = []
    for b in page.get_text("dict")["blocks"]:
        for line in b.get("lines", []):
            for sp in line["spans"]:
                t = sp["text"].strip()
                if t.isdigit() and hex(sp["color"]) in ("0x14243e", "0xe9a471"):
                    out.append((pymupdf.Rect(sp["bbox"]), t, sp["origin"], sp["size"]))
    out.sort(key=lambda x: (round(x[0].y0, 1), x[0].x0))
    return out


def _make_links(doc, pad=1.4):
    """Rend cliquables les numéros de page du sommaire et des renvois.

    Le numéro imprimé *est* la page (le sommaire est rempli en deux passes),
    donc chaque lien vise simplement la page qu'il affiche : aucun appariement
    fragile à maintenir.
    """
    total = doc.page_count
    hits = 0
    for pno in range(total):
        page = doc[pno]
        for b in page.get_text("dict")["blocks"]:
            for line in b.get("lines", []):
                for sp in line["spans"]:
                    t = sp["text"].strip()
                    if not t.isdigit():
                        continue
                    num = int(t)
                    if not 1 <= num <= total or num > 90:
                        continue
                    rect = pymupdf.Rect(sp["bbox"])
                    if rect.y0 > page.rect.height - 42:
                        continue                      # numéro de pied de page
                    if abs(rect.y1 - (page.rect.height - 30 + 11)) < 6:
                        continue
                    left = page.get_text("text", clip=pymupdf.Rect(
                        0, rect.y0 - 3, rect.x0, rect.y1 + 1))
                    in_column = rect.x1 > page.rect.width - 58
                    if not (in_column or left.rstrip().lower().endswith("page")):
                        continue
                    page.insert_link({
                        "kind": pymupdf.LINK_GOTO,
                        "from": rect + (-pad, -pad, pad, pad),
                        "page": num - 1,
                        "to": pymupdf.Point(ML, MT + 18),
                    })
                    hits += 1
    return hits


# ------------------------------------------------------------------ couverture
def make_cover():
    doc = pymupdf.open()
    page = doc.new_page(width=PAGE.width, height=PAGE.height)
    w, h = PAGE.width, PAGE.height
    page.insert_image(page.rect, filename=os.path.join(HERE, "art", "cover-sleep-paralysis.jpg"), keep_proportion=False)
    page.draw_rect(pymupdf.Rect(0, 0, w, 190), color=None,
                   fill=(0.025, 0.035, 0.08), fill_opacity=0.48)
    page.draw_rect(pymupdf.Rect(0, h - 105, w, h), color=None,
                   fill=(0.025, 0.035, 0.08), fill_opacity=0.75)
    page.insert_font(fontname="coverdisplay", fontfile=os.path.join(HERE, "ttf", "playfair-display-latin-700-normal.ttf"))
    page.insert_font(fontname="covertext", fontfile=os.path.join(HERE, "ttf", "inter-latin-600-normal.ttf"))
    page.insert_text((32, 46), "COMPRENDRE  ·  APAISER  ·  AGIR", fontname="covertext",
                     fontsize=7, color=(0.94, 0.73, 0.55))
    page.insert_text((30, 91), "Réveillée,", fontname="coverdisplay", fontsize=31,
                     color=(1, 1, 1))
    page.insert_text((30, 132), "mais prisonnière", fontname="coverdisplay", fontsize=27,
                     color=(1, 0.84, 0.71))
    page.insert_text((32, 160), "COMPRENDRE LA PARALYSIE DU SOMMEIL", fontname="covertext",
                     fontsize=7.8, color=(1, 1, 1))
    page.draw_line((32, h - 78), (76, h - 78), color=(0.91, 0.65, 0.45), width=1.4)
    page.insert_text((32, h - 56), "Se réveiller, pas subir", fontname="coverdisplay",
                     fontsize=14, color=(1, 1, 1))
    page.insert_text((32, h - 35), "UN GUIDE PRATIQUE POUR RETROUVER SES REPÈRES", fontname="covertext",
                     fontsize=6.6, color=(0.95, 0.85, 0.76))
    return doc


def footer(page, num, dark):
    w, h = PAGE.width, PAGE.height
    y = h - 22
    page.draw_line(pymupdf.Point(ML, y), pymupdf.Point(w - MR, y),
                   color=(0.35, 0.39, 0.48) if dark else (0.858, 0.804, 0.741),
                   width=0.5)
    page.insert_text(pymupdf.Point(ML, y + 10.5), "SE RÉVEILLER, PAS SUBIR", fontsize=5.2,
                     fontname="hebo", color=(0.55, 0.55, 0.56) if dark else (0.70, 0.64, 0.57))
    txt = str(num)
    tw = pymupdf.get_text_length(txt, fontname="hebo", fontsize=8)
    page.insert_text(pymupdf.Point(w - MR - tw, y + 11), txt, fontsize=8, fontname="hebo",
                     color=GOLD if dark else NAVY)


# ------------------------------------------------------------------ assemblage
VIEWER = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Réveillée, mais prisonnière — aperçu</title>
<style>
  :root {{ --navy:#14243F; --terra:#B0522F; --cream:#F9F2EA; }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; background:#0C1523; color:#EFE7DC;
         font-family: ui-sans-serif, system-ui, -apple-system, sans-serif; }}
  header {{ padding:34px 22px 20px; max-width:760px; margin:0 auto; }}
  .eyebrow {{ font-size:11px; letter-spacing:2.4px; color:#E9A472; font-weight:700; }}
  h1 {{ font-family: Georgia, 'Times New Roman', serif; font-size:34px; line-height:1.1;
       margin:10px 0 8px; color:#fff; }}
  .sub {{ color:#B9AFA1; font-size:15px; line-height:1.55; margin:0 0 14px; }}
  .dl {{ display:inline-block; background:var(--terra); color:#fff; text-decoration:none;
        padding:11px 18px; border-radius:2px; font-size:13px; font-weight:600;
        letter-spacing:.6px; }}
  main {{ max-width:1060px; margin:0 auto; padding:8px 16px 60px;
         display:grid; grid-template-columns:repeat(auto-fill,minmax(180px,1fr)); gap:14px; }}
  figure {{ margin:0; background:var(--cream); box-shadow:0 6px 18px rgba(0,0,0,.35); }}
  figure img {{ display:block; width:100%; height:auto; }}
  figcaption {{ font-size:10px; color:#6E6153; padding:5px 6px; text-align:right;
                font-variant-numeric:tabular-nums; background:var(--cream); }}
  .note {{ max-width:760px; margin:0 auto; padding:0 22px 40px; color:#7E8A9B; font-size:12.5px; line-height:1.6; }}
</style></head><body>
<header>
  <div class="eyebrow">EBOOK · {n} PAGES · A5</div>
  <h1>Réveillée, mais prisonnière</h1>
  <p class="sub">La paralysie du sommeil expliquée, apaisée, maîtrisée —
  avec un programme de 21 nuits, une fiche d'urgence et un journal de bord.</p>
  <a class="dl" href="SE-REVEILLER-PAS-SUBIR-paralysie-du-sommeil.pdf">Télécharger le PDF</a>
</header>
<main>
{cards}
</main>
<p class="note">Ceci est un aperçu des {n} pages. Le fichier PDF complet contient le sommaire
cliquable, les signets de navigation et les polices intégrées — c'est lui qu'il faut
envoyer à tes lecteurs ou imprimer.</p>
</body></html>
"""


def write_viewer(doc, path):
    import base64
    cards = []
    for i in range(doc.page_count):
        pix = doc[i].get_pixmap(dpi=64, colorspace=pymupdf.csGRAY)
        data = base64.b64encode(pix.tobytes("jpeg", jpg_quality=72)).decode()
        cards.append(
            '<figure><img loading="lazy" src="data:image/jpeg;base64,%s" '
            'alt="page %d"/><figcaption>%02d</figcaption></figure>' % (data, i + 1, i + 1)
        )
    open(path, "w", encoding="utf-8").write(
        VIEWER.format(cards="\n".join(cards), n=doc.page_count))
    print("aperçu ->", path)


def build():
    files = sorted(f for f in os.listdir(os.path.join(HERE, "content")) if f.endswith(".html"))
    keys = {}
    for f in files:
        raw = open(os.path.join(HERE, "content", f), encoding="utf-8").read()
        m = re.search(r"<!--KEY:([a-z0-9_]+)-->", raw)
        keys[f] = m.group(1) if m else None


    def make(pagemap):
        cache = {}
        for f in files:
            key = keys[f]
            raw = open(os.path.join(HERE, "content", f), encoding="utf-8").read()
            if key:
                for k, v in pagemap.items():
                    n = str(v)
                    slots = []
                    for token in ("__PAGE_%s__" % k, "__TOC_%s__" % k.upper()):
                        slots += [(m.start(), m.end(), k)
                                  for m in re.finditer(re.escape(token), raw)]
                    for start, end, key in reversed(sorted(slots)):
                        raw = raw[:start] + n + raw[end:]
            tmpdir = os.path.join(HERE, "_tmp")
            os.makedirs(tmpdir, exist_ok=True)
            path = os.path.join(tmpdir, f)
            open(path, "w", encoding="utf-8").write(raw)
            cache[f] = render_path(path, source=f)
        return cache

    nums, dark = {}, set()
    # passe 1 (placeholders visibles) puis passe 2 avec les vrais numéros
    for _ in range(2):
        cache = make(nums)
        nums, dark = {}, set()
        n = 1
        for f in files:
            frag = cache[f]
            if keys[f]:
                nums[keys[f]] = n + 1
            if is_dark(f):          # seules les ouvertures de partie sont sur fond nuit
                for i in range(frag.page_count):
                    dark.add(n + i + 1)
            n += frag.page_count

    doc = pymupdf.open()
    doc.insert_pdf(make_cover())

    # liens internes : les marqueurs [[|cle|]] sont posés juste après le numéro
    for f in files:
        doc.insert_pdf(cache[f])

    nlinks = _make_links(doc)
    for i in range(1, doc.page_count):
        footer(doc[i], i + 1, (i + 1) in dark)

    doc.set_metadata({
        "title": "Réveillée, mais prisonnière — comprendre la paralysie du sommeil",
        "author": "Collection Femme Indépendante",
        "subject": "Guide pratique et programme de 21 nuits contre la paralysie du sommeil",
        "keywords": "paralysie du sommeil, sommeil, anxiété, angoisse nocturne, Afrique francophone, minzi-minzi, insomnie",
    })

    bms = []
    for f in files:
        raw = open(os.path.join(HERE, "content", f), encoding="utf-8").read()
        for m in re.finditer(r"<!--BM:(\d)\|(.*?)-->", raw):
            bms.append([int(m.group(1)), m.group(2), nums.get(keys[f], 2)])
    if bms:
        doc.set_toc(bms)

    # maquette légère pour la prévisualisation web
    html_out = os.path.join(HERE, "..", "index.html")
    write_viewer(doc, html_out)

    out = os.path.join(HERE, "..", "SE-REVEILLER-PAS-SUBIR-paralysie-du-sommeil.pdf")
    doc.save(out, garbage=4, deflate=True)
    # contrôle des jetons non résolus
    leftovers = set()
    for i in range(doc.page_count):
        leftovers |= set(re.findall(r"__PAGE_[A-Za-z0-9_]+__", doc[i].get_text()))
    print(f"OK -> {os.path.basename(out)}  ({doc.page_count} pages, {nlinks} liens)")
    if leftovers:
        print("  JETONS NON RÉSOLUS :", leftovers)
    return out


if __name__ == "__main__":
    build()
