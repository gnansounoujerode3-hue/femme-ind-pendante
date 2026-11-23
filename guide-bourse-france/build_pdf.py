"""Génère le PDF d'un guide à partir de chapitres Markdown.

Usage (depuis la racine du dépôt) :
    python3 guide-bourse-france/build_pdf.py SORTIE.pdf [DOSSIER_SOURCE] [TITRE] [SOUS-TITRE]

Par défaut : chapitres/ -> guide principal. Pour le bonus :
    python3 guide-bourse-france/build_pdf.py guide-bourse-france/BONUS-COMPARATIF-BOURSES.pdf \\
        guide-bourse-france/bonus "Bonus : comparatif des bourses françaises" "Bourses vérifiées au 22 novembre 2026"

Mise en page :
- couverture à bandeau coloré ;
- sommaire avec numéros de page cliquables ;
- en-tête (titre court) et numéro de page à partir du sommaire ;
- un saut de page par chapitre ;
- signets PDF (volet de navigation) pour chaque chapitre.

Dépendance : fpdf2 (pip install fpdf2). Polices DejaVu requises.
Les liens (Markdown ou URL nues) apparaissent en bleu et sont cliquables.
"""
import glob
import os
import re
import sys

from fpdf import FPDF

HERE = os.path.dirname(os.path.abspath(__file__))
FD = "/usr/share/fonts/truetype/dejavu/"
BLUE = (0, 0, 238)
NAVY = (31, 60, 110)
GREY = (110, 110, 110)

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "guide.pdf")
SRC_DIR = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "chapitres")
TITLE = sys.argv[3] if len(sys.argv) > 3 else "Décroche ta bourse française"
SUBTITLE = sys.argv[4] if len(sys.argv) > 4 else "toi-même, sans payer une agence"
SHORT_TITLE = TITLE if len(TITLE) < 45 else TITLE[:42] + "…"
files = sorted(glob.glob(os.path.join(SRC_DIR, "*.md")))

TOK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)|(https?://[^\s)]+)")


def clean(t):
    t = re.sub(r"\*\*|__|(?<!\w)\*|\*(?!\w)|`", "", t)
    return t.replace("[ ]", "☐")


class Guide(FPDF):
    def header(self):
        if self.page_no() <= 2:
            return
        self.set_font("DV", "", 8)
        self.set_text_color(*GREY)
        self.set_y(12)
        self.cell(0, 5, SHORT_TITLE, align="R")
        self.set_draw_color(*GREY)
        self.line(22, 18.5, self.w - 22, 18.5)
        self.set_text_color(0, 0, 0)

    def footer(self):
        if self.page_no() <= 2:
            return
        self.set_y(-14)
        self.set_font("DV", "", 8)
        self.set_text_color(*GREY)
        self.cell(0, 5, str(self.page_no()), align="C")
        self.set_text_color(0, 0, 0)


pdf = Guide(format="A4")
pdf.set_margins(22, 24, 22)
pdf.set_auto_page_break(True, 22)
pdf.add_font("DV", "", FD + "DejaVuSans.ttf")
pdf.add_font("DV", "B", FD + "DejaVuSans-Bold.ttf")
pdf.add_font("DVS", "", FD + "DejaVuSerif.ttf")
pdf.add_font("DVS", "B", FD + "DejaVuSerif-Bold.ttf")
W = pdf.w - 44


def write(text, size=10.5, style="", font="DV", indent=0, h=None, after=0, color=None):
    """Écrit un paragraphe ; les liens sont bleus, soulignés et cliquables."""
    h = h or size * 0.55
    text = clean(text)
    pdf.set_x(22 + indent)
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
    pdf.ln(h)
    if after:
        pdf.ln(after)


def rule():
    pdf.ln(2)
    pdf.set_draw_color(*NAVY)
    pdf.line(22, pdf.get_y(), pdf.w - 22, pdf.get_y())
    pdf.set_draw_color(0, 0, 0)
    pdf.ln(5)


def cover():
    pdf.add_page()
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, pdf.w, 110, "F")
    pdf.set_y(40)
    write(TITLE, 26, "B", "DVS", h=13, color=(255, 255, 255))
    write(SUBTITLE, 18, "", "DVS", h=10, color=(255, 255, 255))
    pdf.set_y(130)
    write("Guide pratique complet pour les candidats béninois", 13, "B", after=4)
    write("Procédure Campus France Bénin, bourse d'excellence Eiffel, dossier, entretien, visa, départ", 10.5, after=60)
    write("Version de référence : 22 novembre 2026", 10, after=2)
    write("Vérifie toujours les dates, montants et liens sur les sites officiels avant d'agir.", 10)


TOC_LINKS = {}


def toc_page():
    pdf.add_page()
    pdf.insert_toc_placeholder(render_toc, pages=1)


def render_toc(pdf_, outline):
    pdf_.set_font("DVS", "B", 18)
    pdf_.set_x(22)
    pdf_.cell(0, 10, "Sommaire", new_x="LMARGIN", new_y="NEXT")
    pdf_.ln(4)
    for item in outline:
        if item.level != 0:
            continue
        pdf_.set_font("DV", "", 10.5)
        pdf_.set_text_color(*BLUE)
        pdf_.set_x(22)
        label = item.name
        pdf_.cell(W - 12, 7, label, link=TOC_LINKS.get(item.name, ""), new_x="RIGHT", new_y="TOP")
        pdf_.set_text_color(0, 0, 0)
        pdf_.cell(12, 7, str(item.page_number), align="R", new_x="LMARGIN", new_y="NEXT")


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
            for r_i, r in enumerate(rows):
                write(" | ".join(r), 9, "B" if r_i == 0 else "", indent=2, after=1)
            pdf.ln(3)
            continue
        if l.startswith("# "):
            write(l[2:], 20, "B", "DVS", h=11, after=4, color=NAVY)
        elif l.startswith("## "):
            pdf.ln(3)
            write(l[3:], 13.5, "B", "DVS", h=8, after=2, color=NAVY)
        elif l.startswith("### "):
            pdf.ln(2)
            write(l[4:], 11.5, "B", h=7, after=1)
        elif l.strip() == "---":
            rule()
        elif l.startswith("> "):
            write(l[2:], 10, "", "DVS", indent=8, h=6)
        elif re.match(r"^\s*- \[[ x]\] ", l):
            write("☐  " + re.sub(r"^\s*- \[[ x]\] ", "", l), 10.5, indent=6, h=6)
        elif re.match(r"^\s*- ", l):
            write("•  " + re.sub(r"^\s*- ", "", l), 10.5, indent=6, h=6)
        elif re.match(r"^\s*\d+\. ", l):
            write(l.strip(), 10.5, indent=6, h=6)
        elif l.strip() == "":
            pdf.ln(2.5)
        else:
            write(l, 10.5, h=6)
        i += 1


cover()
toc_page()
for f in files:
    chapter(f)

pdf.output(OUT)
print("pages", pdf.page_no(), "chapitres", len(files))
