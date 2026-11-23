"""Génère le PDF du guide à partir des chapitres Markdown.

Usage (depuis la racine du dépôt) :
    python3 guide-bourse-france/build_pdf.py SORTIE.pdf [DOSSIER_SOURCE] [TITRE] [SOUS-TITRE]

Par défaut : chapitres/ -> guide principal. Pour le bonus :
    python3 guide-bourse-france/build_pdf.py guide-bourse-france/BONUS-COMPARATIF-BOURSES.pdf \
        guide-bourse-france/bonus "Bonus : comparatif des bourses françaises" "Bourses vérifiées au 22 novembre 2026"

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
SRC_DIR = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "chapitres")
TITLE = sys.argv[3] if len(sys.argv) > 3 else "Décroche ta bourse française"
SUBTITLE = sys.argv[4] if len(sys.argv) > 4 else "toi-même, sans payer une agence"
files = sorted(glob.glob(os.path.join(SRC_DIR, "*.md")))

pdf = FPDF(format="A4")
pdf.set_margins(22, 22, 22)
pdf.set_auto_page_break(True, 22)
pdf.add_font("DV", "", FD + "DejaVuSans.ttf")
pdf.add_font("DV", "B", FD + "DejaVuSans-Bold.ttf")
pdf.add_font("DVS", "", FD + "DejaVuSerif.ttf")
pdf.add_font("DVS", "B", FD + "DejaVuSerif-Bold.ttf")
W = pdf.w - 44

TOK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)|(https?://[^\s)]+)")


def clean(t):
    t = re.sub(r"\*\*|__|(?<!\w)\*|\*(?!\w)|`", "", t)
    return t.replace("[ ]", "☐")


def write(text, size=10.5, style="", font="DV", indent=0, h=None, after=0):
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
            pdf.set_text_color(0, 0, 0)
            pdf.set_font(font, style, size)
        pdf.write(h, seg, link=url or "")
    pdf.set_text_color(0, 0, 0)
    pdf.set_font(font, style, size)
    pdf.ln(h)
    if after:
        pdf.ln(after)


def rule():
    pdf.ln(2)
    pdf.line(22, pdf.get_y(), pdf.w - 22, pdf.get_y())
    pdf.ln(5)


# Page de titre
pdf.add_page()
pdf.ln(60)
write(TITLE, 26, "B", "DVS", h=13)
write(SUBTITLE, 20, "", "DVS", h=11, after=10)
write("Guide pratique complet pour les candidats béninois", 12, after=4)
write("Procédure Campus France Bénin, bourse d'excellence Eiffel, dossier, entretien, visa, départ", 10.5, after=40)
write("Version de référence : 22 novembre 2026", 10, after=2)
write("Vérifie toujours les dates, montants et liens sur les sites officiels avant d'agir.", 10)

# Sommaire
pdf.add_page()
write("Sommaire", 18, "B", "DVS", h=10, after=6)
for f in files:
    first = open(f, encoding="utf-8").readline().strip().lstrip("# ").strip()
    write(first, 10.5, indent=4, after=1)

# Chapitres : un saut de page par chapitre
for f in files:
    pdf.add_page()
    lines = open(f, encoding="utf-8").read().split("\n")
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
            write(l[2:], 20, "B", "DVS", h=11, after=4)
        elif l.startswith("## "):
            pdf.ln(3)
            write(l[3:], 13.5, "B", "DVS", h=8, after=2)
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

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "guide.pdf")
pdf.output(out)
print("pages", pdf.page_no(), "chapitres", len(files))
