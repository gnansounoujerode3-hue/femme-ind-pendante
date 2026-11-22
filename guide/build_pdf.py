#!/usr/bin/env python3
"""Build a navigable, print-ready A4 PDF from the chapter 1 Markdown draft."""
from __future__ import annotations

import html
import re
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

import markdown
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Flowable, Frame, KeepTogether, ListFlowable, ListItem,
    NextPageTemplate, PageBreak, PageTemplate, Paragraph, Spacer, Table, TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "chapitre-01-bien-se-preparer.md"
OUTPUT = ROOT / "chapitre-01-bien-se-preparer.pdf"
VERSION_DATE = "22 novembre 2026"
INK = colors.HexColor("#172B3A")
TEAL = colors.HexColor("#176B68")
GOLD = colors.HexColor("#D69B3D")
PAPER = colors.HexColor("#F7F5EF")
MUTED = colors.HexColor("#52616B")
PALE_TEAL = colors.HexColor("#EAF3F1")
PALE_GOLD = colors.HexColor("#FBF3E4")
RULE = colors.HexColor("#D8DEDE")

FONT_DIRS = [
    Path("/usr/share/fonts/truetype/dejavu"),
    Path("/usr/share/fonts/truetype/liberation"),
]


def font_path(filename: str) -> Path:
    for directory in FONT_DIRS:
        candidate = directory / filename
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        f"Font {filename} not found. Install DejaVu Sans or update FONT_DIRS."
    )


pdfmetrics.registerFont(TTFont("DejaVu", str(font_path("DejaVuSans.ttf"))))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", str(font_path("DejaVuSans-Bold.ttf"))))
# The sandbox provides regular and bold DejaVu files; map italic variants to
# their closest installed faces to keep the PDF self-contained and Unicode-safe.
pdfmetrics.registerFont(TTFont("DejaVu-Oblique", str(font_path("DejaVuSans.ttf"))))
pdfmetrics.registerFont(TTFont("DejaVu-BoldOblique", str(font_path("DejaVuSans-Bold.ttf"))))
pdfmetrics.registerFont(TTFont("DejaVuMono", str(font_path("DejaVuSansMono.ttf"))))
pdfmetrics.registerFontFamily(
    "DejaVu", normal="DejaVu", bold="DejaVu-Bold",
    italic="DejaVu-Oblique", boldItalic="DejaVu-BoldOblique",
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    "BodyFR", fontName="DejaVu", fontSize=11, leading=16.2,
    textColor=INK, spaceAfter=7.2, allowWidows=0, allowOrphans=0,
))
styles.add(ParagraphStyle(
    "BodyCompact", parent=styles["BodyFR"], fontSize=9.4, leading=13.2,
    spaceAfter=3,
))
styles.add(ParagraphStyle(
    "H2FR", fontName="DejaVu-Bold", fontSize=16, leading=20,
    textColor=INK, spaceBefore=16, spaceAfter=8, keepWithNext=True,
))
styles.add(ParagraphStyle(
    "H3FR", fontName="DejaVu-Bold", fontSize=11.8, leading=15.5,
    textColor=TEAL, spaceBefore=11, spaceAfter=5, keepWithNext=True,
))
styles.add(ParagraphStyle(
    "TOCTitle", fontName="DejaVu-Bold", fontSize=22, leading=27,
    textColor=INK, spaceAfter=12,
))
styles.add(ParagraphStyle(
    "TOC0", fontName="DejaVu-Bold", fontSize=10, leading=15,
    leftIndent=0, firstLineIndent=0, textColor=INK, spaceBefore=2,
))
styles.add(ParagraphStyle(
    "TOC1", fontName="DejaVu", fontSize=8.7, leading=12,
    leftIndent=13, firstLineIndent=0, textColor=MUTED,
))
styles.add(ParagraphStyle(
    "TableCell", fontName="DejaVu", fontSize=7.5, leading=10,
    textColor=INK, spaceAfter=0,
))
styles.add(ParagraphStyle(
    "TableHeader", fontName="DejaVu-Bold", fontSize=7.5, leading=10,
    textColor=colors.white, spaceAfter=0,
))
styles.add(ParagraphStyle(
    "BulletFR", parent=styles["BodyFR"], leftIndent=0, firstLineIndent=0,
    spaceAfter=4.5,
))


def slug(text: str) -> str:
    plain = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-") or "section"


def inline_markup(node: ET.Element) -> str:
    """Convert safe Markdown HTML inline nodes to ReportLab Paragraph markup."""
    parts: list[str] = []
    if node.text:
        parts.append(html.escape(node.text, quote=False))
    for child in list(node):
        tag = child.tag.lower().split("}")[-1]
        body = inline_markup(child)
        if tag in ("strong", "b"):
            body = f"<b>{body}</b>"
        elif tag in ("em", "i"):
            body = f"<i>{body}</i>"
        elif tag == "code":
            body = f'<font name="DejaVuMono" size="8.5">{body}</font>'
        elif tag == "a":
            href = html.escape(child.attrib.get("href", ""), quote=True)
            body = f'<link href="{href}" color="#176B68">{body}</link>' if href else body
        elif tag == "br":
            body += "<br/>"
        elif tag in ("sub", "sup"):
            body = f"<{tag}>{body}</{tag}>"
        parts.append(body)
        if child.tail:
            parts.append(html.escape(child.tail, quote=False))
    return "".join(parts)


class TocHeading(Paragraph):
    def __init__(self, text: str, style: ParagraphStyle, level: int, key: str,
                 include_in_toc: bool = True):
        super().__init__(text, style)
        self.toc_level = level
        self.toc_text = re.sub(r"<[^>]+>", "", text)
        self.toc_key = key
        self.include_in_toc = include_in_toc


class BookDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str):
        page_w, page_h = A4
        super().__init__(
            filename, pagesize=A4, title="Chapitre 1 — Bien se préparer",
            author="Mon dossier d’études à l’étranger",
            subject="Guide pratique de préparation aux études en France",
            creator="Générateur éditorial local — ReportLab",
            leftMargin=19 * mm, rightMargin=19 * mm,
            topMargin=22 * mm, bottomMargin=19 * mm,
        )
        cover_frame = Frame(0, 0, page_w, page_h, id="cover", leftPadding=0,
                            rightPadding=0, topPadding=0, bottomPadding=0)
        body_frame = Frame(self.leftMargin, self.bottomMargin,
                           page_w-self.leftMargin-self.rightMargin,
                           page_h-self.topMargin-self.bottomMargin,
                           id="body", leftPadding=0, rightPadding=0,
                           topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="Cover", frames=[cover_frame], onPage=self.draw_cover),
            PageTemplate(id="Body", frames=[body_frame], onPage=self.draw_body),
        ])

    @staticmethod
    def draw_cover(canvas, doc):
        w, h = A4
        canvas.saveState()
        canvas.setFillColor(PAPER)
        canvas.rect(0, 0, w, h, stroke=0, fill=1)
        canvas.setFillColor(INK)
        canvas.rect(0, h-82*mm, w, 82*mm, stroke=0, fill=1)
        canvas.setFillColor(TEAL)
        canvas.rect(0, h-85*mm, w, 3*mm, stroke=0, fill=1)
        # Original, lightweight geometric motif; no stock imagery or logos.
        canvas.setStrokeColor(colors.Color(1, 1, 1, alpha=0.17))
        canvas.setLineWidth(1.2)
        for idx in range(5):
            canvas.circle(w-17*mm-idx*12*mm, h-21*mm, (idx+1)*11*mm,
                          stroke=1, fill=0)
        canvas.setFillColor(GOLD)
        canvas.circle(27*mm, 55*mm, 3*mm, stroke=0, fill=1)
        canvas.setFillColor(TEAL)
        canvas.circle(39*mm, 55*mm, 3*mm, stroke=0, fill=1)
        canvas.setFillColor(GOLD)
        canvas.circle(51*mm, 55*mm, 3*mm, stroke=0, fill=1)
        canvas.setFillColor(MUTED)
        canvas.setFont("DejaVu", 8)
        canvas.drawString(20*mm, 18*mm, "VERSION DE TRAVAIL · 22 NOVEMBRE 2026")
        canvas.restoreState()

    @staticmethod
    def draw_body(canvas, doc):
        if doc.page == 1:
            return
        w, h = A4
        canvas.saveState()
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.55)
        canvas.line(19*mm, h-14*mm, w-19*mm, h-14*mm)
        canvas.setFont("DejaVu-Bold", 7.2)
        canvas.setFillColor(TEAL)
        canvas.drawString(19*mm, h-11*mm, "MON DOSSIER D’ÉTUDES À L’ÉTRANGER")
        canvas.setFont("DejaVu", 7.2)
        canvas.setFillColor(MUTED)
        canvas.drawRightString(w-19*mm, h-11*mm, "CHAPITRE 1 · VERSION DE TRAVAIL")
        canvas.line(19*mm, 13*mm, w-19*mm, 13*mm)
        canvas.setFont("DejaVu", 7.2)
        canvas.drawString(19*mm, 8.5*mm, "Version du 22 novembre 2026 · Informations à vérifier selon votre situation")
        canvas.drawRightString(w-19*mm, 8.5*mm, str(doc.page-1))
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, TocHeading):
            self.canv.bookmarkPage(flowable.toc_key)
            self.canv.addOutlineEntry(flowable.toc_text, flowable.toc_key,
                                      level=flowable.toc_level, closed=False)
            if flowable.include_in_toc:
                # Pagination excludes the unnumbered cover, matching the printed footer.
                self.notify("TOCEntry", (flowable.toc_level, flowable.toc_text,
                                         self.page - 1, flowable.toc_key))


class Cover(Flowable):
    def __init__(self):
        super().__init__()
        self.width = A4[0]
        self.height = A4[1]

    def wrap(self, availWidth, availHeight):
        return A4

    def draw(self):
        c = self.canv
        w, h = A4
        c.saveState()
        c.setFillColor(GOLD)
        c.roundRect(20*mm, h-34*mm, 46*mm, 8*mm, 2*mm, stroke=0, fill=1)
        c.setFillColor(INK)
        c.setFont("DejaVu-Bold", 8)
        c.drawCentredString(43*mm, h-31.3*mm, "CHAPITRE 01")
        c.setFillColor(colors.white)
        c.setFont("DejaVu", 9)
        c.drawString(20*mm, h-49*mm, "MON DOSSIER D’ÉTUDES À L’ÉTRANGER")
        c.setFont("DejaVu-Bold", 29)
        c.drawString(20*mm, h-65*mm, "Bien se")
        c.drawString(20*mm, h-78*mm, "préparer")
        c.setFillColor(INK)
        c.setFont("DejaVu-Bold", 20)
        c.drawString(20*mm, h-112*mm, "Clarifier votre projet.")
        c.setFont("DejaVu", 11)
        c.setFillColor(MUTED)
        c.drawString(20*mm, h-122*mm, "Repérer les étapes, les questions et les appuis")
        c.drawString(20*mm, h-129*mm, "à vérifier avant de vous lancer.")
        c.setFillColor(TEAL)
        c.roundRect(20*mm, h-159*mm, 170*mm, 16*mm, 2*mm, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont("DejaVu-Bold", 9)
        c.drawString(26*mm, h-149*mm, "GUIDE PRATIQUE · PROJET BÉNIN → FRANCE")
        c.setFillColor(MUTED)
        c.setFont("DejaVu", 8.5)
        c.drawString(20*mm, h-177*mm, "Pour les lycéens, étudiants et familles qui préparent")
        c.drawString(20*mm, h-184*mm, "un projet d’études en France.")
        c.setFillColor(GOLD)
        c.setFont("DejaVu-Bold", 8)
        c.drawString(20*mm, h-207*mm, "BROUILLON ÉDITORIAL — NON VALIDÉ PAR DES ENTRETIENS")
        c.setStrokeColor(RULE)
        c.line(20*mm, 32*mm, w-20*mm, 32*mm)
        c.setFillColor(MUTED)
        c.setFont("DejaVu", 8)
        c.drawString(20*mm, 24*mm, "Aucune promesse d’admission, de bourse ou de visa.")
        c.restoreState()


def markdown_blocks(source: str):
    rendered = markdown.markdown(source, extensions=["tables", "sane_lists"])
    root = ET.fromstring(f"<root>{rendered}</root>")
    story = []
    h2_index = 0
    for node in list(root):
        tag = node.tag.lower().split("}")[-1]
        if tag == "h1":
            continue  # The cover carries the chapter title.
        if tag == "h2":
            text = inline_markup(node)
            h2_index += 1
            heading_text = ''.join(node.itertext()).strip()
            # Keep the contents page concise; detailed subheadings remain in PDF bookmarks.
            include_in_toc = bool(re.match(r"^[1-5]\.", heading_text))
            story.append(TocHeading(text, styles["H2FR"], 0,
                                    f"section-{h2_index}-{slug(heading_text)}",
                                    include_in_toc=include_in_toc))
        elif tag == "h3":
            text = inline_markup(node)
            story.append(TocHeading(text, styles["H3FR"], 1,
                                    f"subsection-{slug(''.join(node.itertext()))}",
                                    include_in_toc=False))
        elif tag == "p":
            para = Paragraph(inline_markup(node), styles["BodyFR"])
            if len(list(node)) == 0 and (node.text or "").strip().startswith("**À propos de cette version :**"):
                story.append(callout(para, PALE_GOLD, GOLD))
            elif len(list(node)) == 0 and (node.text or "").strip().startswith("**À retenir :**"):
                story.append(callout(para, PALE_TEAL, TEAL))
            else:
                story.append(para)
        elif tag == "blockquote":
            paras = [Paragraph(inline_markup(p), styles["BodyCompact"])
                     for p in node if p.tag.lower().split("}")[-1] == "p"]
            if paras:
                story.append(callout(paras, PALE_GOLD, GOLD))
        elif tag in ("ul", "ol"):
            items = []
            for li in node.findall("li"):
                content = inline_markup(li).strip()
                items.append(ListItem(Paragraph(content, styles["BodyFR"]),
                                      leftIndent=10, bulletColor=TEAL))
            story.append(ListFlowable(
                items, bulletType="bullet" if tag == "ul" else "1",
                bulletChar="•" if tag == "ul" else None,
                start="1" if tag == "ol" else None,
                leftIndent=18, bulletFontName="DejaVu",
                bulletFontSize=8, bulletColor=TEAL, spaceAfter=7,
            ))
        elif tag == "table":
            rows = []
            for row in node.findall(".//tr"):
                cells = []
                for cell in list(row):
                    ctag = cell.tag.lower().split("}")[-1]
                    if ctag in ("th", "td"):
                        style = styles["TableHeader"] if ctag == "th" else styles["TableCell"]
                        cells.append(Paragraph(inline_markup(cell), style))
                if cells:
                    rows.append(cells)
            if rows:
                story.append(make_table(rows))
        elif tag == "hr":
            story.append(Hairline())
        elif tag == "pre":
            story.append(Paragraph(inline_markup(node), styles["BodyCompact"]))
        story.append(Spacer(1, 1.2))
    return story


def callout(content, background, accent):
    cells = content if isinstance(content, list) else [content]
    table = Table([[cells]], colWidths=[A4[0]-38*mm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("BOX", (0, 0), (-1, -1), 0.4, background),
        ("LINEBEFORE", (0, 0), (0, -1), 3, accent),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return KeepTogether([table, Spacer(1, 7)])


class Hairline(Flowable):
    def __init__(self):
        super().__init__()
        self.height = 10

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return self.width, self.height

    def draw(self):
        self.canv.setStrokeColor(RULE)
        self.canv.setLineWidth(0.7)
        self.canv.line(0, self.height/2, self.width, self.height/2)


def make_table(rows):
    columns = max(len(row) for row in rows)
    available = A4[0] - 38*mm
    maxlens = []
    for col in range(columns):
        lengths = []
        for row in rows:
            if col >= len(row):
                continue
            cell = row[col]
            text = cell.getPlainText() if hasattr(cell, "getPlainText") else str(cell)
            lengths.append(len(text))
        maxlens.append(max(lengths, default=5))
    weights = [max(0.8, min(10, length ** 0.5)) for length in maxlens]
    min_width = 24 if columns >= 4 else 36
    remain = available - min_width*columns
    total = sum(weights) or 1
    widths = [min_width + remain*weight/total for weight in weights]
    normalized = []
    for row in rows:
        normalized.append(row + [Paragraph("", styles["TableCell"])]*(columns-len(row)))
    tbl = Table(normalized, colWidths=widths, repeatRows=1, hAlign="LEFT", splitByRow=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PAPER]),
        ("GRID", (0, 0), (-1, -1), 0.35, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return KeepTogether([tbl, Spacer(1, 7)])


def build():
    source = SOURCE.read_text(encoding="utf-8")
    doc = BookDocTemplate(str(OUTPUT))
    toc = TableOfContents()
    toc.levelStyles = [styles["TOC0"], styles["TOC1"]]
    toc.dotsMinLevel = 0
    story = [Cover(), NextPageTemplate("Body"), PageBreak(),
             Paragraph("Dans ce chapitre", styles["TOCTitle"]),
             Paragraph("Les repères et exercices de ce chapitre", styles["BodyCompact"]),
             Spacer(1, 5), toc, PageBreak()]
    story.extend(markdown_blocks(source))
    doc.multiBuild(story)
    print(f"Created {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    build()
