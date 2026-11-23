"""Génère le PDF d'un guide à partir de chapitres Markdown.

Usage (depuis la racine du dépôt) :
    python3 guide-bourse-france/build_pdf.py SORTIE.pdf [DOSSIER_SOURCE] [TITRE] [SOUS-TITRE]

Guide principal :
    python3 guide-bourse-france/build_pdf.py guide-bourse-france/DECROCHE-TA-BOURSE-FRANCAISE-TOI-MEME.pdf
Bonus :
    python3 guide-bourse-france/build_pdf.py guide-bourse-france/BONUS-COMPARATIF-BOURSES.pdf \\
        guide-bourse-france/bonus "Bonus : comparatif des bourses françaises" "Bourses vérifiées au 22 novembre 2026"

Mise en page :
- couverture à bandeau coloré ;
- sommaire avec numéros de page cliquables ;
- en-tête séparé du texte, pied de page avec numéro ;
- listes à puces et numérotées avec retrait suspendu (les lignes suivantes restent alignées) ;
- tableaux réels, à bordures et en-tête colorée ;
- un saut de page par chapitre ; signets PDF pour chaque chapitre.

Dépendance : fpdf2 (pip install fpdf2). Polices DejaVu requises.
Les liens (Markdown ou URL nues) apparaissent en bleu et sont cliquables.
"""
import glob
import os
import re
import sys

from fpdf import FPDF
from fpdf.fonts import FontFace

HERE = os.path.dirname(os.path.abspath(__file__))
FD = "/usr/share/fonts/truetype/dejavu/"
BLUE = (0, 0, 238)
NAVY = (31, 60, 110)
GREY = (110, 110, 110)
LIGHT = (232, 238, 247)
ML = 22  # marge gauche et droite (mm)
MT = 28  # marge haute (mm) : le texte commence sous l'en-tête

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "guide.pdf")
SRC_DIR = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "chapitres")
TITLE = sys.argv[3] if len(sys.argv) > 3 else "Décroche ta bourse française"
SUBTITLE = sys.argv[4] if len(sys.argv) > 4 else "toi-même, sans payer une agence"
SHORT_TITLE = TITLE if len(TITLE) < 60 else TITLE[:57] + "…"
files = sorted(glob.glob(os.path.join(SRC_DIR, "*.md")))

TOK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)|(https?://[^\s)]+)")
TOC_LINKS = {}


def clean(t):
    t = re.sub(r"\*\*|__|(?<!\w)\*|\*(?!\w)|`", "", t)
    return t.replace("[ ]", "☐")


class Guide(FPDF):
    def header(self):
        if self.page_no() <= 2:
            return
        self.set_font("DV", "", 8)
        self.set_text_color(*GREY)
        self.set_xy(ML, 10)
        self.cell(0, 5, SHORT_TITLE, align="R")
        self.set_draw_color(*GREY)
        self.set_line_width(0.2)
        self.line(ML, 17, self.w - ML, 17)
        self.set_text_color(0, 0, 0)
        self.set_xy(ML, MT)  # le texte reprend sous l'en-tête, à la marge haute

    def footer(self):
        if self.page_no() <= 2:
            return
        self.set_y(-14)
        self.set_font("DV", "", 8)
        self.set_text_color(*GREY)
        self.cell(0, 5, str(self.page_no()), align="C")
        self.set_text_color(0, 0, 0)


pdf = Guide(format="A4")
pdf.set_margins(ML, MT, ML)
pdf.set_auto_page_break(True, 24)
pdf.add_font("DV", "", FD + "DejaVuSans.ttf")
pdf.add_font("DV", "B", FD + "DejaVuSans-Bold.ttf")
pdf.add_font("DVS", "", FD + "DejaVuSerif.ttf")
pdf.add_font("DVS", "B", FD + "DejaVuSerif-Bold.ttf")
TEXT_W = pdf.w - 2 * ML


def inline(text, size, style, font, h, color=None):
    """Écrit du texte à partir de la position courante ; liens bleus et cliquables."""
    segs, pos = [], 0
    for m in TOK.finditer(text):
        if m.start() > pos:
            segs.append((text[pos:m.start()], None))
        if m.group(1):
            segs.append((m.group(1) + " (" + m.group(2) + ")", m.group(2)))
        else:
            segs.append((m.group(3), m.group(3)))
        pos = m.end()
    if pos < len(text):
        segs.append((text[pos:], None))
    for seg, url in segs:
        if url:
            pdf.set_text_color(*BLUE)
            pdf.set_font(font, "U" + style, size)
        else:
            pdf.set_text_color(*(color or (0, 0, 0)))
            pdf.set_font(font, style, size)
        pdf.write(h, seg, link=url or "")
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(font, style, size)


def para(text, size=10.5, style="", font="DV", h=None, after=0, color=None, indent=0):
    """Paragraphe normal, à l'alignement de la marge (avec retrait éventuel)."""
    h = h or size * 0.55
    pdf.set_left_margin(ML + indent)
    pdf.set_x(ML + indent)
    inline(clean(text), size, style, font, h, color)
    pdf.ln(h)
    pdf.set_left_margin(ML)
    if after:
        pdf.ln(after)


def item(marker, text, size=10.5, h=6, indent=6):
    """Élément de liste avec retrait suspendu : le marqueur à gauche, le texte aligné."""
    hang = 8 if len(marker) > 2 else 5
    x0 = ML + indent
    pdf.set_x(x0)
    pdf.set_font("DV", "", size)
    pdf.cell(hang, h, marker)
    pdf.set_left_margin(x0 + hang)
    pdf.set_x(x0 + hang)
    inline(clean(text), size, "", "DV", h)
    pdf.ln(h)
    pdf.set_left_margin(ML)


def rule():
    pdf.ln(2)
    pdf.set_draw_color(*NAVY)
    pdf.set_line_width(0.3)
    pdf.line(ML, pdf.get_y(), pdf.w - ML, pdf.get_y())
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.2)
    pdf.ln(5)


def table(rows):
    """Tableau réel : en-tête colorée et grasse, bordures fines, retour à la ligne dans les cellules."""
    ncol = len(rows[0])
    widths = tuple(TEXT_W / ncol for _ in range(ncol))
    pdf.ln(2)
    pdf.set_font("DV", "", 9)
    pdf.set_fill_color(255, 255, 255)  # le corps du tableau reste blanc
    pdf.set_text_color(0, 0, 0)
    pdf.set_draw_color(150, 160, 175)
    with pdf.table(col_widths=widths, first_row_as_headings=True, line_height=5, padding=1.5,
                   text_align="LEFT", borders_layout="ALL", width=TEXT_W,
                   headings_style=FontFace(emphasis="B", fill_color=LIGHT)) as t:
        for r in rows:
            row = t.row()
            for c in r:
                row.cell(clean(c))
    pdf.set_draw_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)
    pdf.ln(4)


COVER_IMG = os.path.join(HERE, "couverture", "couverture-finale.png")
COVER_FORMAT = (210, 315)  # format de l'image de couverture (2:3), sans la déformer


def cover():
    # Couverture image (uniquement pour le guide principal, pas pour le bonus)
    if os.path.exists(COVER_IMG) and SRC_DIR == os.path.join(HERE, "chapitres"):
        pdf.add_page(format=COVER_FORMAT)
        pdf.image(COVER_IMG, x=0, y=0, w=COVER_FORMAT[0], h=COVER_FORMAT[1])
        return
    pdf.add_page()
    pdf.set_fill_color(*NAVY)  # bandeau de couverture uniquement
    pdf.rect(0, 0, pdf.w, 110, "F")
    pdf.set_left_margin(ML)
    pdf.set_y(40)
    para(TITLE, 26, "B", "DVS", h=13, color=(255, 255, 255))
    para(SUBTITLE, 18, "", "DVS", h=10, color=(255, 255, 255))
    pdf.set_y(130)
    para("Guide pratique complet pour les candidats béninois", 13, "B", after=4)
    para("Procédure Campus France Bénin, bourse d'excellence Eiffel, dossier, entretien, visa, départ",
         10.5, after=60)
    para("Version de référence : 22 novembre 2026", 10, after=2)
    para("Vérifie toujours les dates, montants et liens sur les sites officiels avant d'agir.", 10)


def toc_page():
    pdf.add_page()
    pdf.insert_toc_placeholder(render_toc, pages=1)


def render_toc(pdf_, outline):
    pdf_.set_left_margin(ML)
    pdf_.set_font("DVS", "B", 18)
    pdf_.set_text_color(*NAVY)
    pdf_.set_x(ML)
    pdf_.cell(0, 10, "Sommaire", new_x="LMARGIN", new_y="NEXT")
    pdf_.set_text_color(0, 0, 0)
    pdf_.ln(4)
    for item_ in outline:
        if item_.level != 0:
            continue
        pdf_.set_font("DV", "", 10.5)
        pdf_.set_text_color(*BLUE)
        pdf_.set_x(ML)
        pdf_.cell(TEXT_W - 12, 7, item_.name, link=TOC_LINKS.get(item_.name, ""), new_x="RIGHT", new_y="TOP")
        pdf_.set_text_color(0, 0, 0)
        pdf_.cell(12, 7, str(item_.page_number), align="R", new_x="LMARGIN", new_y="NEXT")


def chapter(path):
    pdf.add_page()
    lines = open(path, encoding="utf-8").read().split("\n")
    first = next((l for l in lines if l.startswith("# ")), os.path.basename(path))
    name = clean(first[2:]).strip()
    pdf.start_section(name, level=0)
    TOC_LINKS[name] = pdf.add_link(page=pdf.page_no(), y=0)
    i = 0
    while i < len(lines):
        l = lines[i].rstrip()
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-| ]+\|$", lines[i].strip()):
                    rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            if rows:
                table(rows)
            continue
        if l.startswith("# "):
            para(l[2:], 20, "B", "DVS", h=11, after=4, color=NAVY)
        elif l.startswith("## "):
            pdf.ln(3)
            para(l[3:], 13.5, "B", "DVS", h=8, after=2, color=NAVY)
        elif l.startswith("### "):
            pdf.ln(2)
            para(l[4:], 11.5, "B", h=7, after=1)
        elif l.strip() == "---":
            rule()
        elif l.startswith("> "):
            para(l[2:], 10, "", "DVS", h=6, indent=8)
        elif re.match(r"^\s*- \[[ x]\] ", l):
            item("☐", re.sub(r"^\s*- \[[ x]\] ", "", l))
        elif re.match(r"^\s*- ", l):
            item("•", re.sub(r"^\s*- ", "", l))
        elif re.match(r"^\s*\d+\. ", l):
            m = re.match(r"^\s*(\d+)\. (.*)", l)
            item(m.group(1) + ".", m.group(2))
        elif l.strip() == "":
            pdf.ln(2.5)
        else:
            para(l, 10.5, h=6)
        i += 1


cover()
toc_page()
for f in files:
    chapter(f)

pdf.output(OUT)
print("pages", pdf.page_no(), "chapitres", len(files))
