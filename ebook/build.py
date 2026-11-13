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
        tmp = story_pages(pg_html, css)
        for i in range(tmp.page_count):
            page = out.new_page(width=PAGE.width, height=PAGE.height)
            page.draw_rect(page.rect, color=None, fill=NAVY if dark else CREAM)
            page.show_pdf_page(page.rect, tmp, i)
    return out


# ------------------------------------------------------------------ couverture
def make_cover():
    doc = pymupdf.open()
    page = doc.new_page(width=PAGE.width, height=PAGE.height)
    w, h = PAGE.width, PAGE.height
    page.insert_image(page.rect, pixmap=pymupdf.Pixmap(os.path.join(HERE, "art", "cover.jpg")))
    page.draw_rect(page.rect, color=None, fill=(0.04, 0.07, 0.15), fill_opacity=0.24, overlay=True)
    page.draw_rect(pymupdf.Rect(0, 0, w, 140), color=None, fill=(0.04, 0.07, 0.15),
                   fill_opacity=0.62, overlay=True)
    page.draw_rect(pymupdf.Rect(0, h - 158, w, h), color=None, fill=(0.04, 0.07, 0.15),
                   fill_opacity=0.70, overlay=True)
    page.insert_text(pymupdf.Point(34, 47), "COMPRENDRE  ·  APAISER  ·  PASSER A L'ACTION",
                     fontsize=5.9, fontname="hebo", color=(0.91, 0.78, 0.66))
    page.insert_text(pymupdf.Point(33, 93), "Se réveiller,", fontsize=30, fontname="hebo",
                     color=(1, 1, 1))
    page.insert_text(pymupdf.Point(33, 124), "pas subir", fontsize=30, fontname="hebo",
                     color=(0.96, 0.79, 0.62))
    page.draw_line(pymupdf.Point(34, h - 124), pymupdf.Point(80, h - 124),
                   color=(0.91, 0.78, 0.66), width=1.4)
    page.insert_text(pymupdf.Point(34, h - 105), "La paralysie du sommeil", fontsize=8.4,
                     fontname="hebo", color=(1, 1, 1))
    page.insert_text(pymupdf.Point(34, h - 92), "expliquée, apaisée, maîtrisée",
                     fontsize=8.4, fontname="helv", color=(0.90, 0.85, 0.78))
    page.insert_text(pymupdf.Point(34, h - 58), "21 NUITS POUR REPRENDRE LE CONTROLE",
                     fontsize=5.8, fontname="hebo", color=(0.96, 0.79, 0.62))
    return doc


def footer(page, num, dark):
    w, h = PAGE.width, PAGE.height
    y = h - 30
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
<title>Se réveiller, pas subir — aperçu</title>
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
  <div class="eyebrow">EBOOK · 79 PAGES · A5</div>
  <h1>Se réveiller, pas subir</h1>
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
                    raw = raw.replace("__PAGE_%s__" % k, str(v))
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
            if f.startswith("p"):
                for i in range(frag.page_count):
                    dark.add(n + i + 1)
            n += frag.page_count

    doc = pymupdf.open()
    doc.insert_pdf(make_cover())
    for f in files:
        doc.insert_pdf(cache[f])

    for i in range(1, doc.page_count):
        footer(doc[i], i + 1, (i + 1) in dark)

    doc.set_metadata({
        "title": "Se réveiller, pas subir — la paralysie du sommeil expliquée, apaisée, maîtrisée",
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
    print(f"OK -> {os.path.basename(out)}  ({doc.page_count} pages)")
    if leftovers:
        print("  JETONS NON RÉSOLUS :", leftovers)
    return out


if __name__ == "__main__":
    build()
