# -*- coding: utf-8 -*-
"""Générateur complet des livrables PDF et Markdown éditables pour :
« 500 Idées de Business à Lancer en Afrique en 2027 »
aligné à 100 % sur WORKBOOK-OFFICIEL-JOUR-2-CREE-TON-PREMIER-PRODUIT-DIGITAL.pdf.
"""

import json
import os
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.flowables import Flowable
from reportlab.platypus.tableofcontents import TableOfContents

from ebook_content import (
    BUDGET_GUIDE,
    CONCLUSION_CONTENT,
    PART_01_INTRO,
    PART_02_ERRORS,
    PART_04_VALIDATION,
    PART_05_LAUNCH,
    get_workbook_pages_data,
)
from ideas_500 import get_numbered_sectors

ROOT_DIR = Path(__file__).resolve().parent.parent
SOURCE_DIR = Path(__file__).resolve().parent

OUT_EBOOK_PDF = ROOT_DIR / "500-Idees-de-Business-a-Lancer-en-Afrique-en-2027.pdf"
OUT_WORKBOOK_PDF = ROOT_DIR / "Workbook-Jour-2-Rempli-500-Idees-Business-Afrique-2027.pdf"
OUT_EBOOK_MD = SOURCE_DIR / "ebook-500-idees-business-afrique-2027.md"
OUT_WORKBOOK_MD = SOURCE_DIR / "workbook-jour-2-rempli.md"
COVER_ART_PATH = SOURCE_DIR / "cover_art.png"
CONFIG_PATH = SOURCE_DIR / "author_config.json"

PAGE_W, PAGE_H = A4  # 595.27 x 841.89 pt
MARGIN_L = 46
MARGIN_R = 46
MARGIN_T = 58
MARGIN_B = 48
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R  # 503.27 pt

# Palette éditoriale Afro-Moderniste (assortie à cover_art.png)
C_EMERALD_DARK = colors.HexColor("#082A23")
C_EMERALD = colors.HexColor("#0B3B31")
C_EMERALD_SOFT = colors.HexColor("#135245")
C_GOLD = colors.HexColor("#D4942A")
C_GOLD_BRIGHT = colors.HexColor("#F2B84B")
C_GOLD_BG = colors.HexColor("#FDF6E7")
C_TERRACOTTA = colors.HexColor("#B8532A")
C_TERRACOTTA_BG = colors.HexColor("#FCF0EB")
C_CREAM = colors.HexColor("#F9F6F0")
C_SAGE_BG = colors.HexColor("#EEF5F2")
C_SAGE_BORDER = colors.HexColor("#D1DFD9")
C_CHARCOAL = colors.HexColor("#1B2321")
C_SLATE = colors.HexColor("#4B5854")
C_MUTED = colors.HexColor("#73807B")
C_LINE = colors.HexColor("#DCE4E0")
C_WHITE = colors.white

BUDGET_STYLES = {
    "Petit": {
        "label": "Petit (< 50k FCFA)",
        "short": "Petit budget",
        "accent": C_EMERALD,
        "bg": colors.HexColor("#E6F3EE"),
        "fg": colors.HexColor("#093A2F"),
    },
    "Moyen": {
        "label": "Moyen (50k–300k)",
        "short": "Budget moyen",
        "accent": C_GOLD,
        "bg": colors.HexColor("#FDF3DF"),
        "fg": colors.HexColor("#7D5106"),
    },
    "Structuré": {
        "label": "Structuré (300k+)",
        "short": "Budget structuré",
        "accent": C_TERRACOTTA,
        "bg": colors.HexColor("#FBECE6"),
        "fg": colors.HexColor("#8C3614"),
    },
}


def register_fonts():
    """Enregistre les polices SourceSerifPro et SourceSansPro depuis .venv."""
    site_pkgs = list((ROOT_DIR / ".venv" / "lib").glob("python*/site-packages"))
    if not site_pkgs:
        raise RuntimeError("Impossible de localiser site-packages dans .venv")
    sp = site_pkgs[0]

    sans_dir = sp / "font_source_sans_pro" / "files"
    serif_dir = sp / "font_source_serif_pro" / "files"

    fonts_to_reg = [
        ("Sans", sans_dir / "SourceSansPro-Regular.ttf"),
        ("Sans-Bold", sans_dir / "SourceSansPro-Bold.ttf"),
        ("Sans-Semibold", sans_dir / "SourceSansPro-Semibold.ttf"),
        ("Sans-Italic", sans_dir / "SourceSansPro-It.ttf"),
        ("Sans-BoldItalic", sans_dir / "SourceSansPro-BoldIt.ttf"),
        ("Serif", serif_dir / "SourceSerifPro-Regular.ttf"),
        ("Serif-Semibold", serif_dir / "SourceSerifPro-Semibold.ttf"),
        ("Serif-Bold", serif_dir / "SourceSerifPro-Bold.ttf"),
        ("Serif-Black", serif_dir / "SourceSerifPro-Black.ttf"),
        ("Serif-Italic", serif_dir / "SourceSerifPro-It.ttf"),
        ("Serif-BoldItalic", serif_dir / "SourceSerifPro-BoldIt.ttf"),
    ]
    for name, path in fonts_to_reg:
        if not path.exists():
            raise FileNotFoundError(f"Police manquante : {path}")
        pdfmetrics.registerFont(TTFont(name, str(path)))

    registerFontFamily(
        "Sans",
        normal="Sans",
        bold="Sans-Bold",
        italic="Sans-Italic",
        boldItalic="Sans-BoldItalic",
    )
    registerFontFamily(
        "Serif",
        normal="Serif",
        bold="Serif-Bold",
        italic="Serif-Italic",
        boldItalic="Serif-BoldItalic",
    )


def esc(text):
    """Échappe les caractères spéciaux XML pour ReportLab Paragraph."""
    return escape(str(text))


def build_styles():
    """Construit la feuille de styles typographiques."""
    s = {}
    s["kicker"] = ParagraphStyle(
        "kicker", fontName="Sans-Bold", fontSize=8.5, leading=11,
        textColor=C_GOLD, spaceAfter=3,
    )
    s["h1"] = ParagraphStyle(
        "h1", fontName="Serif-Bold", fontSize=20, leading=25,
        textColor=C_EMERALD_DARK, spaceAfter=8, keepWithNext=True,
    )
    s["h2"] = ParagraphStyle(
        "h2", fontName="Serif-Bold", fontSize=13.5, leading=17.5,
        textColor=C_EMERALD, spaceBefore=9, spaceAfter=5, keepWithNext=True,
    )
    s["h3"] = ParagraphStyle(
        "h3", fontName="Sans-Bold", fontSize=10.5, leading=14,
        textColor=C_EMERALD_DARK, spaceAfter=2, keepWithNext=True,
    )
    s["lead"] = ParagraphStyle(
        "lead", fontName="Sans-Italic", fontSize=10.5, leading=15,
        textColor=C_SLATE, spaceAfter=8,
    )
    s["body"] = ParagraphStyle(
        "body", fontName="Sans", fontSize=9.8, leading=14.2,
        textColor=C_CHARCOAL, spaceAfter=6, alignment=TA_LEFT,
    )
    s["body_sm"] = ParagraphStyle(
        "body_sm", fontName="Sans", fontSize=9.0, leading=12.8,
        textColor=C_CHARCOAL, spaceAfter=4,
    )
    s["body_muted"] = ParagraphStyle(
        "body_muted", fontName="Sans", fontSize=8.6, leading=12,
        textColor=C_SLATE, spaceAfter=3,
    )
    s["quote"] = ParagraphStyle(
        "quote", fontName="Serif-Italic", fontSize=11, leading=15.5,
        textColor=C_EMERALD_DARK,
    )
    s["idea_title"] = ParagraphStyle(
        "idea_title", fontName="Sans-Bold", fontSize=9.8, leading=12.5,
        textColor=C_EMERALD_DARK,
    )
    s["idea_desc"] = ParagraphStyle(
        "idea_desc", fontName="Sans", fontSize=8.7, leading=11.8,
        textColor=C_SLATE,
    )
    s["wb_h1"] = ParagraphStyle(
        "wb_h1", fontName="Serif-Bold", fontSize=18, leading=23,
        textColor=C_EMERALD_DARK, spaceAfter=6,
    )
    s["wb_box_title"] = ParagraphStyle(
        "wb_box_title", fontName="Sans-Bold", fontSize=9.8, leading=13,
        textColor=C_EMERALD_DARK, spaceAfter=3,
    )
    s["wb_body"] = ParagraphStyle(
        "wb_body", fontName="Sans", fontSize=9.5, leading=13.5,
        textColor=C_CHARCOAL, spaceAfter=4,
    )
    s["wb_small"] = ParagraphStyle(
        "wb_small", fontName="Sans", fontSize=8.6, leading=12,
        textColor=C_SLATE, spaceAfter=2,
    )
    s["toc_0"] = ParagraphStyle(
        "toc_0", fontName="Sans-Bold", fontSize=9.5, leading=12.0,
        textColor=C_EMERALD_DARK, leftIndent=0, firstLineIndent=0,
        spaceBefore=3.0, spaceAfter=1.0,
    )
    s["toc_1"] = ParagraphStyle(
        "toc_1", fontName="Sans", fontSize=8.3, leading=10.3,
        textColor=C_SLATE, leftIndent=14, firstLineIndent=0,
        spaceBefore=0.0, spaceAfter=0.4,
    )
    return s


# ---------------------------------------------------------------------------
# FLOWABLES PERSONNALISÉS
# ---------------------------------------------------------------------------

class CoverPageFlowable(Flowable):
    """Couverture plein cadre A4 utilisant cover_art.png + typographie haute lisibilité."""

    def __init__(self, config, mode="ebook"):
        super().__init__()
        self.config = config
        self.mode = mode  # "ebook" ou "workbook"
        self.width = PAGE_W
        self.height = PAGE_H

    def wrap(self, availWidth, availHeight):
        return PAGE_W, PAGE_H

    def draw(self):
        c = self.canv
        c.saveState()

        # Fond émeraude profond par sécurité
        c.setFillColor(C_EMERALD_DARK)
        c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

        # Dessin de cover_art.png en recadrage "cover" plein cadre
        if COVER_ART_PATH.exists():
            im = PILImage.open(COVER_ART_PATH)
            iw, ih = im.size
            target_ratio = PAGE_W / PAGE_H
            img_ratio = iw / ih
            if img_ratio > target_ratio:
                # image plus large -> ajuster hauteur et centrer horizontalement
                draw_h = PAGE_H
                draw_w = PAGE_H * img_ratio
                dx = (PAGE_W - draw_w) / 2.0
                dy = 0
            else:
                draw_w = PAGE_W
                draw_h = PAGE_W / img_ratio
                dx = 0
                dy = (PAGE_H - draw_h) / 2.0
            c.drawImage(ImageReader(str(COVER_ART_PATH)), dx, dy, width=draw_w, height=draw_h)

        # Dégradé doux sans couture en haut et en bas pour garantir un contraste net
        steps = 20
        top_zone_h = 268.0
        step_h = top_zone_h / steps
        for i in range(steps):
            alpha = 0.62 * ((steps - i) / steps) ** 1.35
            c.setFillColorRGB(0.03, 0.14, 0.11, alpha)
            c.rect(0, PAGE_H - (i + 1) * step_h, PAGE_W, step_h + 0.5, fill=1, stroke=0)

        bot_zone_h = 215.0
        b_step_h = bot_zone_h / steps
        for i in range(steps):
            alpha = 0.78 * ((steps - i) / steps) ** 1.25
            c.setFillColorRGB(0.03, 0.14, 0.11, alpha)
            c.rect(0, i * b_step_h, PAGE_W, b_step_h + 0.5, fill=1, stroke=0)

        # Filet doré d'encadrement intérieur
        c.setStrokeColor(C_GOLD)
        c.setLineWidth(1.0)
        c.rect(22, 22, PAGE_W - 44, PAGE_H - 44, fill=0, stroke=1)

        cx = PAGE_W / 2.0

        # Cartouche supérieur
        pill_text = (
            "WORKBOOK OFFICIEL – JOUR 2 • DOSSIER D'APPLICATION"
            if self.mode == "workbook"
            else self.config.get("edition", "ÉDITION 2027 • GUIDE PRATIQUE & CATALOGUE COMPLET").upper()
        )
        pill_w = min(430, max(270, len(pill_text) * 6.2 + 34))
        pill_y = PAGE_H - 64
        c.setFillColor(C_GOLD)
        c.roundRect(cx - pill_w / 2, pill_y, pill_w, 21, 10.5, fill=1, stroke=0)
        c.setFillColor(C_EMERALD_DARK)
        c.setFont("Sans-Bold", 8.6)
        c.drawCentredString(cx, pill_y + 6.8, pill_text)

        if self.mode == "ebook":
            # Grand Titre Ebook
            c.setFillColor(C_WHITE)
            c.setFont("Serif-Black", 30)
            c.drawCentredString(cx, PAGE_H - 106, "500 IDÉES DE BUSINESS")
            c.drawCentredString(cx, PAGE_H - 140, "À LANCER EN AFRIQUE")
            c.setFillColor(C_GOLD_BRIGHT)
            c.setFont("Serif-Black", 32)
            c.drawCentredString(cx, PAGE_H - 176, "EN 2027")

            # Filet séparateur or
            c.setStrokeColor(C_GOLD_BRIGHT)
            c.setLineWidth(1.4)
            c.line(cx - 80, PAGE_H - 190, cx + 80, PAGE_H - 190)

            # Sous-titre wrapped proprement
            sub_style = ParagraphStyle(
                "cov_sub", fontName="Sans", fontSize=11.0, leading=15.0,
                textColor=C_CREAM, alignment=TA_CENTER,
            )
            sub_p = Paragraph(esc(self.config.get("ebook_subtitle", "")), sub_style)
            sw, sh = sub_p.wrap(PAGE_W - 116, 70)
            sub_p.drawOn(c, 58, PAGE_H - 199 - sh)
        else:
            # Titre Workbook Jour 2 Rempli
            c.setFillColor(C_WHITE)
            c.setFont("Serif-Black", 26)
            c.drawCentredString(cx, PAGE_H - 110, "CRÉE TON PREMIER")
            c.drawCentredString(cx, PAGE_H - 142, "PRODUIT DIGITAL")
            c.setFillColor(C_GOLD_BRIGHT)
            c.setFont("Sans-Bold", 12)
            c.drawCentredString(cx, PAGE_H - 170, "CAHIER PRATIQUE COMPLÉTÉ (PAGES 1 À 10)")

            c.setStrokeColor(C_GOLD_BRIGHT)
            c.setLineWidth(1.5)
            c.line(cx - 80, PAGE_H - 186, cx + 80, PAGE_H - 186)

            sub_style = ParagraphStyle(
                "cov_sub_wb", fontName="Sans-Semibold", fontSize=11.2, leading=15.5,
                textColor=C_CREAM, alignment=TA_CENTER,
            )
            sub_p = Paragraph(
                esc(f"Application exacte de la méthode au projet : « {self.config.get('ebook_title', '')} »"),
                sub_style,
            )
            sw, sh = sub_p.wrap(PAGE_W - 110, 80)
            sub_p.drawOn(c, 55, PAGE_H - 198 - sh)

        # Zone inférieure : Encadré Promesse + Auteur
        box_x, box_y, box_w, box_h = 46, 86, PAGE_W - 92, 86
        c.setFillColorRGB(0.05, 0.21, 0.17, 0.90)
        c.setStrokeColor(C_GOLD)
        c.setLineWidth(1.1)
        c.roundRect(box_x, box_y, box_w, box_h, 8, fill=1, stroke=1)

        c.setFillColor(C_GOLD_BRIGHT)
        c.setFont("Sans-Bold", 8.2)
        c.drawCentredString(cx, box_y + box_h - 17, "LA PROMESSE DU GUIDE (FORMULE WORKBOOK JOUR 2)")

        prom_style = ParagraphStyle(
            "cov_prom", fontName="Serif-Italic", fontSize=10.8, leading=14.8,
            textColor=C_WHITE, alignment=TA_CENTER,
        )
        prom_p = Paragraph(esc(f"« {self.config.get('promise_formula', '')} »"), prom_style)
        pw, ph = prom_p.wrap(box_w - 36, box_h - 28)
        prom_p.drawOn(c, box_x + 18, box_y + (box_h - 22 - ph) / 2.0 + 2)

        # Pied de couverture
        c.setFillColor(C_CREAM)
        c.setFont("Sans-Bold", 10)
        c.drawString(46, 46, f"Par {self.config.get('author_name', '[Ton Nom / Ta Marque]')}")
        c.setFillColor(C_GOLD_BRIGHT)
        c.setFont("Sans-Semibold", 9.5)
        right_label = (
            "Méthode 10 étapes • 100 % Appliquée"
            if self.mode == "workbook"
            else "20 Secteurs • 500 Idées • Plan 7 Jours"
        )
        c.drawRightString(PAGE_W - 46, 46, right_label)

        c.restoreState()


class CalloutBox(Flowable):
    """Encadré éditorial à bordure gauche colorée et fond doux."""

    def __init__(self, title, body_paragraphs, width=CONTENT_W, bg=C_SAGE_BG, accent=C_EMERALD, title_color=C_EMERALD_DARK, pad_v=8, gap_p=2.5):
        super().__init__()
        self.title = title
        self.body_paragraphs = body_paragraphs  # list of Paragraph
        self.width = width
        self.bg = bg
        self.accent = accent
        self.title_color = title_color
        self.pad_v = pad_v
        self.gap_p = gap_p
        self._title_p = None
        self._height = 0

    def wrap(self, availWidth, availHeight):
        w = min(self.width, availWidth)
        self.width = w
        inner_w = w - 28
        t_style = ParagraphStyle(
            "co_t", fontName="Sans-Bold", fontSize=9.8, leading=13.0,
            textColor=self.title_color, spaceAfter=2,
        )
        h = self.pad_v
        if self.title:
            self._title_p = Paragraph(esc(self.title), t_style)
            _, th = self._title_p.wrap(inner_w, availHeight)
            h += th + 3
        for p in self.body_paragraphs:
            _, ph = p.wrap(inner_w, availHeight)
            h += ph + self.gap_p
        h += self.pad_v - 1
        self._height = h
        return w, h

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(self.bg)
        c.setStrokeColor(C_SAGE_BORDER)
        c.setLineWidth(0.6)
        c.roundRect(0, 0, self.width, self._height, 5, fill=1, stroke=1)
        c.setFillColor(self.accent)
        c.rect(0, 0, 4, self._height, fill=1, stroke=0)

        y = self._height - self.pad_v
        if self._title_p:
            _, th = self._title_p.wrap(self.width - 28, self._height)
            y -= th
            self._title_p.drawOn(c, 16, y)
            y -= 3
        for p in self.body_paragraphs:
            _, ph = p.wrap(self.width - 28, self._height)
            y -= ph
            p.drawOn(c, 16, y)
            y -= self.gap_p
        c.restoreState()


class PartHeaderFlowable(Flowable):
    """En-tête majeur de Partie (01, 02, 03, 04, 05, Conclusion)."""

    def __init__(self, badge, title, subtitle="", width=CONTENT_W, toc_text=None):
        super().__init__()
        self.badge = badge
        self.title = title
        self.subtitle = subtitle
        self.width = width
        if toc_text:
            self._toc_entry = (0, toc_text)
        self._section_header_text = toc_text or title
        self._title_p = None
        self._sub_p = None
        self._height = 0

    def wrap(self, availWidth, availHeight):
        w = min(self.width, availWidth)
        self.width = w
        t_style = ParagraphStyle(
            "ph_t", fontName="Serif-Bold", fontSize=18, leading=23,
            textColor=C_WHITE,
        )
        s_style = ParagraphStyle(
            "ph_s", fontName="Sans-Italic", fontSize=9.2, leading=13,
            textColor=C_CREAM,
        )
        self._title_p = Paragraph(esc(self.title), t_style)
        _, th = self._title_p.wrap(w - 32, availHeight)
        sh = 0
        if self.subtitle:
            self._sub_p = Paragraph(esc(self.subtitle), s_style)
            _, sh = self._sub_p.wrap(w - 32, availHeight)
            sh += 5
        self._height = 14 + 16 + 6 + th + sh + 14
        return w, self._height

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(C_EMERALD_DARK)
        c.roundRect(0, 0, self.width, self._height, 6, fill=1, stroke=0)
        c.setFillColor(C_GOLD)
        c.rect(0, 0, self.width, 3.5, fill=1, stroke=0)

        y = self._height - 14
        c.setFillColor(C_GOLD_BRIGHT)
        c.setFont("Sans-Bold", 8.5)
        y -= 10
        c.drawString(16, y, self.badge.upper())
        y -= 8

        _, th = self._title_p.wrap(self.width - 32, self._height)
        y -= th
        self._title_p.drawOn(c, 16, y)

        if self._sub_p:
            _, sh = self._sub_p.wrap(self.width - 32, self._height)
            y -= (5 + sh)
            self._sub_p.drawOn(c, 16, y)
        c.restoreState()


class SectorBannerFlowable(Flowable):
    """Bandeau élégant ouvrant chacun des 20 secteurs."""

    def __init__(self, sector, width=CONTENT_W):
        super().__init__()
        self.sector = sector
        self.width = width
        self._toc_entry = (
            1,
            f"Secteur {sector['num']:02d} : {sector['title']} ({sector['start_id']:03d}–{sector['end_id']:03d})",
        )
        self._section_header_text = f"Secteur {sector['num']:02d} — {sector['title']}"
        self._title_p = None
        self._intro_p = None
        self._height = 0

    def wrap(self, availWidth, availHeight):
        w = min(self.width, availWidth)
        self.width = w
        t_style = ParagraphStyle(
            "sb_t", fontName="Serif-Bold", fontSize=14.5, leading=18.5,
            textColor=C_EMERALD_DARK,
        )
        i_style = ParagraphStyle(
            "sb_i", fontName="Sans", fontSize=9.1, leading=13,
            textColor=C_CHARCOAL,
        )
        self._title_p = Paragraph(esc(self.sector["title"]), t_style)
        self._intro_p = Paragraph(esc(self.sector["intro"]), i_style)
        _, th = self._title_p.wrap(w - 28, availHeight)
        _, ih = self._intro_p.wrap(w - 28, availHeight)
        self._height = 10 + 16 + 3 + th + 4 + ih + 18 + 8
        return w, self._height

    def draw(self):
        c = self.canv
        s = self.sector
        c.saveState()

        # Carte d'en-tête de secteur
        c.setFillColor(C_CREAM)
        c.setStrokeColor(C_GOLD)
        c.setLineWidth(1.0)
        c.roundRect(0, 0, self.width, self._height, 6, fill=1, stroke=1)
        c.setFillColor(C_EMERALD)
        c.rect(0, 0, 6, self._height, fill=1, stroke=0)

        # Barre supérieure étiquette secteur + plage numéros
        y = self._height - 20
        c.setFillColor(C_EMERALD)
        c.roundRect(16, y, 92, 16, 3, fill=1, stroke=0)
        c.setFillColor(C_WHITE)
        c.setFont("Sans-Bold", 8.2)
        c.drawCentredString(16 + 46, y + 4.5, f"SECTEUR {s['num']:02d} / 20")

        c.setFillColor(C_TERRACOTTA)
        c.setFont("Sans-Bold", 8.5)
        c.drawRightString(self.width - 14, y + 4.5, f"Idées #{s['start_id']:03d} à #{s['end_id']:03d} • 25 fiches")

        # Titre secteur
        _, th = self._title_p.wrap(self.width - 28, self._height)
        y -= (4 + th)
        self._title_p.drawOn(c, 16, y)

        # Intro secteur
        _, ih = self._intro_p.wrap(self.width - 28, self._height)
        y -= (4 + ih)
        self._intro_p.drawOn(c, 16, y)

        # Compteurs budgets du secteur
        counts = {"Petit": 0, "Moyen": 0, "Structuré": 0}
        for it in s["ideas"]:
            counts[it["budget"]] += 1
        y -= 15
        c.setFillColor(C_MUTED)
        c.setFont("Sans-Semibold", 8.0)
        c.drawString(
            16,
            y,
            f"Répartition budgets :  {counts['Petit']} Petit  •  {counts['Moyen']} Moyen  •  {counts['Structuré']} Structuré",
        )
        c.restoreState()


class IdeaCardFlowable(Flowable):
    """Fiche atomique pour une idée business (#001 à #500), impossible à scinder entre deux pages."""

    def __init__(self, idea, styles, width=CONTENT_W):
        super().__init__()
        self.idea = idea
        self.styles = styles
        self.width = width
        self._title_p = None
        self._desc_p = None
        self._height = 0
        self._badge_w = 98

    def wrap(self, availWidth, availHeight):
        w = min(self.width, availWidth)
        self.width = w
        bstyle = BUDGET_STYLES[self.idea["budget"]]
        self._badge_label = bstyle["label"]
        self._badge_w = max(88, len(self._badge_label) * 4.7 + 16)

        # Largeur disponible pour le titre = largeur totale - colonne numéro (38) - badge droit - marges
        title_w = w - 42 - self._badge_w - 22
        desc_w = w - 42 - 16

        self._title_p = Paragraph(esc(self.idea["title"]), self.styles["idea_title"])
        self._desc_p = Paragraph(esc(self.idea["desc"]), self.styles["idea_desc"])

        _, th = self._title_p.wrap(title_w, availHeight)
        _, dh = self._desc_p.wrap(desc_w, availHeight)

        header_h = max(th, 14)
        self._height = 6.0 + header_h + 2.0 + dh + 6.0
        return w, self._height

    def draw(self):
        c = self.canv
        it = self.idea
        bstyle = BUDGET_STYLES[it["budget"]]
        c.saveState()

        # Fond alterné léger
        bg = C_WHITE if it["id"] % 2 == 1 else colors.HexColor("#F8FAF9")
        c.setFillColor(bg)
        c.setStrokeColor(C_LINE)
        c.setLineWidth(0.55)
        c.roundRect(0, 0, self.width, self._height, 4, fill=1, stroke=1)

        # Liseré gauche couleur budget
        c.setFillColor(bstyle["accent"])
        c.rect(0, 0, 3.2, self._height, fill=1, stroke=0)

        # Numéro #001
        num_box_y = self._height - 20.5
        c.setFillColor(C_SAGE_BG)
        c.roundRect(9, num_box_y, 28, 15, 3, fill=1, stroke=0)
        c.setFillColor(C_EMERALD_DARK)
        c.setFont("Sans-Bold", 8.2)
        c.drawCentredString(9 + 14, num_box_y + 4.3, it["code"])

        # Badge budget haut droit
        bx = self.width - self._badge_w - 8
        by = self._height - 20
        c.setFillColor(bstyle["bg"])
        c.roundRect(bx, by, self._badge_w, 14.5, 7.2, fill=1, stroke=0)
        c.setFillColor(bstyle["fg"])
        c.setFont("Sans-Bold", 7.4)
        c.drawCentredString(bx + self._badge_w / 2.0, by + 4.1, self._badge_label)

        # Titre & Description
        title_w = self.width - 42 - self._badge_w - 22
        desc_w = self.width - 42 - 16
        _, th = self._title_p.wrap(title_w, self._height)
        header_h = max(th, 14)
        title_y = self._height - 6.0 - th
        self._title_p.drawOn(c, 42, title_y)

        _, dh = self._desc_p.wrap(desc_w, self._height)
        desc_y = self._height - 6.0 - header_h - 2.0 - dh
        self._desc_p.drawOn(c, 42, desc_y)

        c.restoreState()


# ---------------------------------------------------------------------------
# DOCUMENT TEMPLATE AVEC EN-TÊTES / PIEDS DE PAGE ET TOC MULTI-PASSES
# ---------------------------------------------------------------------------

class BrandedDocTemplate(BaseDocTemplate):
    """Template gérant couverture sans marge, en-têtes dynamiques et multiBuild."""

    def __init__(self, filename, doc_title, right_footer_prefix="Édition 2027 • Afrique Francophone", **kwargs):
        super().__init__(filename, pagesize=A4, **kwargs)
        self.doc_title = doc_title
        self.right_footer_prefix = right_footer_prefix
        self.active_section = doc_title

        cover_frame = Frame(0, 0, PAGE_W, PAGE_H, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="cover_frame")
        content_frame = Frame(
            MARGIN_L, MARGIN_B, CONTENT_W, PAGE_H - MARGIN_T - MARGIN_B,
            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="content_frame",
        )

        self.addPageTemplates([
            PageTemplate(id="cover", frames=[cover_frame], onPage=self._draw_cover_bg),
            PageTemplate(id="content", frames=[content_frame], onPageEnd=self._draw_content_chrome),
        ])

    def handle_documentBegin(self):
        super().handle_documentBegin()
        self.active_section = self.doc_title

    def _draw_cover_bg(self, canvas, doc):
        pass

    def _draw_content_chrome(self, canvas, doc):
        canvas.saveState()
        # En-tête discret
        y_top = PAGE_H - 34
        canvas.setFillColor(C_MUTED)
        canvas.setFont("Sans-Semibold", 7.8)
        canvas.drawString(MARGIN_L, y_top, self.doc_title)
        sec_txt = self.active_section[:62] + ("…" if len(self.active_section) > 62 else "")
        canvas.setFillColor(C_EMERALD)
        canvas.drawRightString(PAGE_W - MARGIN_R, y_top, sec_txt)

        canvas.setStrokeColor(C_LINE)
        canvas.setLineWidth(0.6)
        canvas.line(MARGIN_L, y_top - 6, PAGE_W - MARGIN_R, y_top - 6)

        # Pied de page
        y_bot = 28
        canvas.line(MARGIN_L, y_bot + 10, PAGE_W - MARGIN_R, y_bot + 10)
        canvas.setFillColor(C_MUTED)
        canvas.setFont("Sans", 7.8)
        canvas.drawString(MARGIN_L, y_bot, self.right_footer_prefix)
        canvas.setFillColor(C_EMERALD_DARK)
        canvas.setFont("Sans-Bold", 8.2)
        canvas.drawRightString(PAGE_W - MARGIN_R, y_bot, f"Page {doc.page}")
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if hasattr(flowable, "_section_header_text"):
            self.active_section = flowable._section_header_text
        if hasattr(flowable, "_toc_entry"):
            level, text = flowable._toc_entry
            self.notify("TOCEntry", (level, text, self.page))


class BookmarkableHeading(Flowable):
    """Marqueur invisible ou léger pour enregistrer un titre dans le Sommaire."""

    def __init__(self, text, level=0, section_label=None):
        super().__init__()
        self._toc_entry = (level, text)
        self._section_header_text = section_label or text
        self.width = 0
        self.height = 0

    def wrap(self, availWidth, availHeight):
        return 0, 0

    def draw(self):
        pass


# ---------------------------------------------------------------------------
# CONSTRUCTION DU WORKBOOK JOUR 2 REMPLI (10 PAGES EXACTES)
# ---------------------------------------------------------------------------

def wb_page_header(kicker, title, page_num, styles):
    """Bandeau supérieur uniforme pour chaque page 2..10 du Workbook rempli."""
    k_p = Paragraph(f"<font name='Sans-Bold' size='8.5' color='#F2B84B'>{esc(kicker)}</font>",
                    ParagraphStyle("wbk", leading=11, spaceAfter=3))
    t_p = Paragraph(f"<font name='Serif-Bold' size='16' color='#FFFFFF'>{esc(title)}</font>",
                    ParagraphStyle("wbt", leading=20))
    p_p = Paragraph(f"<font name='Sans-Bold' size='10.5' color='#F2B84B'>PAGE {page_num}/10</font>",
                    ParagraphStyle("wbp", alignment=TA_RIGHT, leading=14))
    tbl = Table([[ [k_p, t_p], p_p ]], colWidths=[CONTENT_W - 96, 96])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), C_EMERALD_DARK),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 11),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
        ("LINEBELOW", (0, 0), (-1, -1), 2.5, C_GOLD),
    ]))
    return tbl


def kv_table(rows, styles, col_left=155, bg=C_CREAM):
    data = []
    for k, v in rows:
        data.append([
            Paragraph(f"<b>{esc(k)}</b>", styles["wb_small"]),
            Paragraph(esc(v), styles["wb_body"]),
        ])
    tbl = Table(data, colWidths=[col_left, CONTENT_W - col_left])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.7, C_SAGE_BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, C_LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return tbl


def build_workbook_pdf(config, styles, ebook_pages=None):
    """Génère le Workbook Jour 2 rempli en exactement 10 pages."""
    wb = get_workbook_pages_data(config, ebook_pages=ebook_pages)
    doc = BrandedDocTemplate(
        str(OUT_WORKBOOK_PDF),
        doc_title="Workbook Officiel Jour 2 – Dossier Rempli",
        right_footer_prefix="Méthode exacte appliquée • 500 Idées de Business en Afrique 2027",
    )
    story = []

    # --- PAGE 1 : COUVERTURE / BIENVENUE ---
    # On intègre une page de couverture + fiche bienvenue directement sur la Page 1 pour garder le 1-pour-1 (10 pages exactes)
    story.append(NextPageTemplate("content"))
    p1 = wb["page1"]
    hero = Table(
        [[Paragraph(
            f"<font name='Sans-Bold' size='9' color='#F2B84B'>{esc(p1['badge'])}</font><br/>"
            f"<font name='Serif-Black' size='21' color='#FFFFFF'>{esc(p1['title'])}</font><br/>"
            f"<font name='Sans-Semibold' size='10.5' color='#F9F6F0'>{esc(p1['subtitle'])}</font>",
            ParagraphStyle("p1h", leading=24),
        )]],
        colWidths=[CONTENT_W],
    )
    hero.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), C_EMERALD_DARK),
        ("LEFTPADDING", (0, 0), (-1, -1), 18),
        ("RIGHTPADDING", (0, 0), (-1, -1), 18),
        ("TOPPADDING", (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
        ("LINEBELOW", (0, 0), (-1, -1), 3, C_GOLD),
    ]))
    story.append(hero)
    story.append(Spacer(1, 14))
    story.append(CalloutBox(
        "Bienvenue — Esprit officiel du Workbook (Page 1)",
        [Paragraph(esc(p1["welcome"]), styles["wb_body"])],
        bg=C_SAGE_BG, accent=C_EMERALD,
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Fiche d'identité du produit créé grâce à ce workbook", styles["h2"]))
    story.append(kv_table(p1["summary_rows"], styles, col_left=160, bg=C_CREAM))
    story.append(Spacer(1, 14))
    story.append(CalloutBox(
        "Comment utiliser ce dossier complété (Pages 1 à 10)",
        [Paragraph(
            esc(
                "Chaque page de ce document correspond page pour page au document "
                "WORKBOOK-OFFICIEL-JOUR-2-CREE-TON-PREMIER-PRODUIT-DIGITAL.pdf. "
                "Les exercices y sont remplis sur mesure pour ton ebook « 500 Idées de Business "
                "à Lancer en Afrique en 2027 », puis matérialisés intégralement dans le PDF final."
            ),
            styles["wb_body"],
        )],
        bg=C_GOLD_BG, accent=C_GOLD, title_color=colors.HexColor("#7D5106"),
    ))
    story.append(PageBreak())

    # --- PAGE 2 : OBJECTIF & ENGAGEMENT ---
    p2 = wb["page2"]
    story.append(wb_page_header(p2["kicker"], p2["title"], 2, styles))
    story.append(Spacer(1, 14))
    story.append(Paragraph(esc(p2["intro"]), styles["wb_body"]))
    story.append(Spacer(1, 10))
    story.append(CalloutBox(
        "Objectif central",
        [Paragraph(esc(p2["quote"]), styles["quote"])],
        bg=C_GOLD_BG, accent=C_GOLD,
    ))
    story.append(Spacer(1, 16))
    story.append(Paragraph("Ton engagement personnel (Complété)", styles["h2"]))
    story.append(kv_table(p2["commitment"], styles, col_left=140, bg=C_SAGE_BG))
    story.append(Spacer(1, 14))
    story.append(CalloutBox(
        "Rappel d'action immédiate",
        [Paragraph(
            esc(
                "Oublier la perfection signifie livrer dès aujourd'hui un ebook utile, structuré "
                "et prêt à être lu sur smartphone. Tu pourras ensuite enrichir la version 2.0 "
                "avec les retours concrets de tes 10 premiers lecteurs."
            ),
            styles["wb_body"],
        )],
        bg=C_CREAM, accent=C_EMERALD,
    ))
    story.append(PageBreak())

    # --- PAGE 3 : VALIDATION EXPRESS (MÉTHODE VIN) ---
    p3 = wb["page3"]
    story.append(wb_page_header(p3["kicker"], p3["title"], 3, styles))
    story.append(Spacer(1, 12))
    story.append(Paragraph(esc(p3["intro"]), styles["wb_body"]))
    story.append(Spacer(1, 8))
    story.append(CalloutBox(
        "V – PROBLÈME (Valeur) : Quel problème précis veux-tu résoudre ?",
        [Paragraph(esc(p3["V"]), styles["wb_body"])],
        bg=C_SAGE_BG, accent=C_EMERALD,
    ))
    story.append(Spacer(1, 10))
    story.append(CalloutBox(
        f"I – INTENSITÉ : Note {p3['I_score']} — Pourquoi ce problème est douloureux ?",
        [Paragraph(esc(p3["I_exp"]), styles["wb_body"])],
        bg=C_GOLD_BG, accent=C_GOLD, title_color=colors.HexColor("#7D5106"),
    ))
    story.append(Spacer(1, 10))
    story.append(CalloutBox(
        "N – NOMBRE : Est-ce un cas isolé ou un marché répandu ?",
        [Paragraph(esc(p3["N"]), styles["wb_body"])],
        bg=C_TERRACOTTA_BG, accent=C_TERRACOTTA, title_color=colors.HexColor("#8C3614"),
    ))
    story.append(Spacer(1, 12))
    story.append(CalloutBox(
        "Verdict Méthode VIN",
        [Paragraph(f"<b>{esc(p3['conclusion'])}</b>", styles["wb_body"])],
        bg=C_CREAM, accent=C_EMERALD_DARK,
    ))
    story.append(PageBreak())

    # --- PAGE 4 : PROMESSE CLAIRE ---
    p4 = wb["page4"]
    story.append(wb_page_header(p4["kicker"], p4["title"], 4, styles))
    story.append(Spacer(1, 12))
    story.append(Paragraph(esc(p4["intro"]), styles["wb_body"]))
    story.append(Spacer(1, 8))
    story.append(kv_table([
        ("1. Pour qui est ton produit ?", p4["q1"]),
        ("2. Résultat concret promis", p4["q2"]),
        ("3. Délai promis", p4["q3"]),
    ], styles, col_left=165, bg=C_SAGE_BG))
    story.append(Spacer(1, 16))
    story.append(Paragraph("Formule de ta promesse (Modèle exact du Workbook)", styles["h2"]))
    story.append(Paragraph(f"<i>Modèle vierge : {esc(p4['formula_template'])}</i>", styles["body_muted"]))
    story.append(Spacer(1, 6))
    story.append(CalloutBox(
        "Promesse finale retenue pour la couverture et la vente",
        [Paragraph(esc(p4["formula_filled"]), styles["quote"])],
        bg=C_GOLD_BG, accent=C_GOLD, title_color=colors.HexColor("#7D5106"),
    ))
    story.append(PageBreak())

    # --- PAGE 5 : FORMAT PDF ---
    p5 = wb["page5"]
    story.append(wb_page_header(p5["kicker"], p5["title"], 5, styles))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Pourquoi commencer avec un PDF ? (Critères du Workbook)", styles["h2"]))
    for r in p5["reasons_pdf"]:
        story.append(Paragraph(f"✓  {esc(r)}", styles["wb_body"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Exercice « À toi de jouer ! » (Complété avec transparence)", styles["h2"]))
    story.append(kv_table([
        ("Pourquoi je choisis le format PDF", p5["why_chosen"]),
        ("Nombre de pages prévues", p5["pages_note"]),
        ("Titre officiel du produit", p5["provisional_title"]),
    ], styles, col_left=165, bg=C_CREAM))
    story.append(PageBreak())

    # --- PAGE 6 : STRUCTURE EN 5 PARTIES + CONCLUSION ---
    p6 = wb["page6"]
    story.append(wb_page_header(p6["kicker"], p6["title"], 6, styles))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Plan exact appliqué à l'ebook « 500 Idées de Business à Lancer en Afrique en 2027 » :",
        styles["wb_body"],
    ))
    story.append(Spacer(1, 6))
    part_rows = []
    for num, label, desc in p6["parts"]:
        part_rows.append([
            Paragraph(f"<b>{esc(num)}</b>", ParagraphStyle("p6n", fontName="Sans-Bold", fontSize=10, textColor=C_EMERALD, alignment=TA_CENTER)),
            Paragraph(f"<b>{esc(label)}</b>", styles["wb_small"]),
            Paragraph(esc(desc), styles["wb_small"]),
        ])
    ptbl = Table(part_rows, colWidths=[42, 108, CONTENT_W - 150])
    ptbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), C_WHITE),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [C_SAGE_BG, C_CREAM]),
        ("BOX", (0, 0), (-1, -1), 0.7, C_SAGE_BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, C_LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story.append(ptbl)
    story.append(PageBreak())

    # --- PAGE 7 : IA & CHECKLIST ---
    p7 = wb["page7"]
    story.append(wb_page_header(p7["kicker"], p7["title"], 7, styles))
    story.append(Spacer(1, 8))
    story.append(CalloutBox(
        "Prompt exact du Workbook → Version appliquée à ton projet",
        [
            Paragraph(f"<b>Modèle :</b> <i>{esc(p7['prompt_template'])}</i>", styles["wb_small"]),
            Paragraph(f"<b>Appliqué :</b> {esc(p7['prompt_applied'])}", styles["wb_small"]),
        ],
        bg=C_SAGE_BG, accent=C_EMERALD,
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph("Comment l'utiliser (6 étapes réalisées)", styles["h3"]))
    for step in p7["how_to_use"]:
        story.append(Paragraph(esc(step), styles["wb_small"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Checklist de création (7 items du Workbook)", styles["h3"]))
    chk_rows = [[
        Paragraph(f"<font color='#0B3B31'><b>☑</b></font>  {esc(label)}", styles["wb_small"])
    ] for label, _ in p7["checklist"]]
    ctbl = Table(chk_rows, colWidths=[CONTENT_W])
    ctbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), C_CREAM),
        ("BOX", (0, 0), (-1, -1), 0.6, C_SAGE_BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, C_LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ]))
    story.append(ctbl)
    story.append(Spacer(1, 7))
    story.append(CalloutBox(
        "Important — Personnalisation",
        [Paragraph(esc(p7["important_note"]), styles["wb_small"])],
        bg=C_GOLD_BG, accent=C_GOLD, title_color=colors.HexColor("#7D5106"),
    ))
    story.append(PageBreak())

    # --- PAGE 8 : RÉCAPITULATIF ---
    p8 = wb["page8"]
    story.append(wb_page_header(p8["kicker"], p8["title"], 8, styles))
    story.append(Spacer(1, 12))
    story.append(Paragraph(esc(p8["intro"]), styles["wb_body"]))
    story.append(Spacer(1, 10))
    rec_rows = []
    for title_r, desc_r, status_r in p8["recap_cards"]:
        rec_rows.append([
            Paragraph(f"<b>{esc(title_r)}</b><br/><font color='#4B5854'>{esc(desc_r)}</font>", styles["wb_body"]),
            Paragraph(f"<font color='#0B3B31'><b>✓ {esc(status_r)}</b></font>",
                      ParagraphStyle("st", fontName="Sans-Bold", fontSize=9.5, alignment=TA_CENTER)),
        ])
    rtbl = Table(rec_rows, colWidths=[CONTENT_W - 95, 95])
    rtbl.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [C_SAGE_BG, C_WHITE]),
        ("BOX", (0, 0), (-1, -1), 0.7, C_SAGE_BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, C_LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    story.append(rtbl)
    story.append(Spacer(1, 14))
    story.append(CalloutBox(
        "Tu es maintenant un créateur de produits digitaux",
        [Paragraph(
            esc("Ton fichier complet « 500-Idees-de-Business-a-Lancer-en-Afrique-en-2027.pdf » concrétise les 5 étapes ci-dessus."),
            styles["wb_body"],
        )],
        bg=C_GOLD_BG, accent=C_GOLD, title_color=colors.HexColor("#7D5106"),
    ))
    story.append(PageBreak())

    # --- PAGE 9 : DÉCLARATION OFFICIELLE & POSTS FACEBOOK ---
    p9 = wb["page9"]
    story.append(wb_page_header(p9["kicker"], p9["title"], 9, styles))
    story.append(Spacer(1, 8))
    story.append(Paragraph("Ton engagement officiel", styles["h3"]))
    story.append(kv_table(p9["declaration"], styles, col_left=140, bg=C_SAGE_BG))
    story.append(Spacer(1, 9))
    story.append(Paragraph(f"Partage ta victoire ! — {esc(p9['fb_action'])}", styles["h3"]))
    for post_title, post_text in p9["social_posts"]:
        story.append(CalloutBox(
            post_title,
            [Paragraph(esc(post_text), styles["wb_small"])],
            bg=C_CREAM, accent=C_GOLD,
        ))
        story.append(Spacer(1, 6))
    story.append(PageBreak())

    # --- PAGE 10 : PROCHAINS PAS ---
    p10 = wb["page10"]
    story.append(wb_page_header(p10["kicker"], p10["title"], 10, styles))
    story.append(Spacer(1, 10))
    for st_title, st_body in p10["steps"]:
        story.append(CalloutBox(
            st_title,
            [Paragraph(esc(st_body), styles["wb_body"])],
            bg=C_SAGE_BG, accent=C_EMERALD,
        ))
        story.append(Spacer(1, 8))
    story.append(CalloutBox(
        "Modèle de message WhatsApp pour tes 10 premiers testeurs",
        [Paragraph(esc(p10["whatsapp_testers"]).replace("\n", "<br/>"), styles["wb_small"])],
        bg=C_GOLD_BG, accent=C_GOLD, title_color=colors.HexColor("#7D5106"),
    ))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"<i>{esc(p10['closing'])}</i>", styles["lead"]))

    doc.build(story)


# ---------------------------------------------------------------------------
# CONSTRUCTION DE L'EBOOK COMPLET (500 IDÉES)
# ---------------------------------------------------------------------------

def build_ebook_pdf(config, sectors, styles):
    """Génère le PDF complet de l'ebook structuré selon la Page 6 du Workbook."""
    doc = BrandedDocTemplate(
        str(OUT_EBOOK_PDF),
        doc_title=config.get("ebook_title", "500 Idées de Business à Lancer en Afrique en 2027"),
        right_footer_prefix="Édition 2027 • Afrique Francophone • Guide Pratique",
    )

    story = []

    # --- PAGE 1 : COUVERTURE ---
    story.append(CoverPageFlowable(config, mode="ebook"))
    story.append(NextPageTemplate("content"))
    story.append(PageBreak())

    # --- PAGE 2 : PAGE DE GARDE, PROMESSE & MODE D'EMPLOI DES BUDGETS ---
    story.append(BookmarkableHeading("Page de garde, Promesse & Guide des Budgets", level=0, section_label="Mode d'emploi & Budgets"))
    story.append(Paragraph("AVANT-PROPOS ÉDITORIAL • ÉDITION 2027", styles["kicker"]))
    story.append(Paragraph(esc(config.get("ebook_title", "")), styles["h1"]))
    story.append(Paragraph(esc(config.get("ebook_subtitle", "")), styles["lead"]))
    story.append(Spacer(1, 6))

    story.append(CalloutBox(
        "La promesse de ce livre",
        [Paragraph(esc(f"« {config.get('promise_formula', '')} »"), styles["quote"])],
        bg=C_GOLD_BG, accent=C_GOLD, title_color=colors.HexColor("#7D5106"),
    ))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Comment lire les 3 niveaux de budget de cet ebook ?", styles["h2"]))
    story.append(Paragraph(
        "Chaque idée parmi les 500 fiches est classée selon le niveau d'investissement réaliste "
        "nécessaire pour démarrer une première version test en Afrique francophone en 2027 :",
        styles["body"],
    ))
    story.append(Spacer(1, 4))

    b_rows = []
    for bg_item in BUDGET_GUIDE:
        st = BUDGET_STYLES[bg_item["tier"]]
        b_rows.append([
            Paragraph(
                f"<font color='{st['fg'].hexval()}'><b>{esc(bg_item['label'])}</b></font><br/>"
                f"<font size='8.2' color='#4B5854'>{esc(bg_item['range'])}</font>",
                styles["body_sm"],
            ),
            Paragraph(esc(bg_item["desc"]), styles["body_sm"]),
        ])
    btbl = Table(b_rows, colWidths=[165, CONTENT_W - 165])
    btbl.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [C_SAGE_BG, C_GOLD_BG, C_TERRACOTTA_BG]),
        ("BOX", (0, 0), (-1, -1), 0.7, C_SAGE_BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, C_LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(btbl)
    story.append(Spacer(1, 14))

    story.append(CalloutBox(
        "Architecture fidèle au Workbook Officiel Jour 2",
        [Paragraph(
            esc(
                "Ce guide suit rigoureusement la structure en 5 parties + Conclusion du Workbook Officiel Jour 2 : "
                "01 Introduction • 02 Les 7 erreurs à éviter • 03 Étape 1 (Choisir parmi 500 idées en 20 secteurs) • "
                "04 Étape 2 (Valider son Top 3 en 48h avec la méthode VIN) • 05 Étape 3 (Plan de lancement 7 jours) • Conclusion. "
                "Astuce diffusion : les 10 premières pages de cet ebook constituent un extrait gratuit idéal à offrir pour attirer tes premiers lecteurs !"
            ),
            styles["body_sm"],
        )],
        bg=C_CREAM, accent=C_EMERALD,
    ))
    story.append(Spacer(1, 16))
    story.append(Paragraph(
        f"<b>Auteur / Éditeur :</b> {esc(config.get('author_name', ''))}  •  "
        f"<b>Date :</b> {esc(config.get('date_creation', ''))}  •  "
        f"<b>Contact :</b> {esc(config.get('contact_whatsapp', ''))}",
        styles["body_muted"],
    ))
    story.append(PageBreak())

    # --- SOMMAIRE DYNAMIQUE ---
    story.append(BookmarkableHeading("Sommaire détaillé", level=0, section_label="Sommaire"))
    story.append(Paragraph("PLAN DU GUIDE • 5 PARTIES + 20 SECTEURS", styles["kicker"]))
    story.append(Paragraph("Sommaire détaillé", styles["h1"]))
    story.append(Spacer(1, 6))

    toc = TableOfContents()
    toc.dotsMinLevel = 0
    toc.levelStyles = [styles["toc_0"], styles["toc_1"]]
    story.append(toc)
    story.append(PageBreak())

    # --- PARTIE 01 : INTRODUCTION ---
    story.append(PartHeaderFlowable(
        PART_01_INTRO["kicker"], PART_01_INTRO["title"],
        PART_01_INTRO["workbook_question"],
        toc_text="Partie 01 — Introduction : Pourquoi entreprendre en Afrique en 2027",
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph(esc(PART_01_INTRO["lead"]), styles["lead"]))

    for btitle, bbody in PART_01_INTRO["problem_blocks"]:
        story.append(Paragraph(esc(btitle), styles["h2"]))
        story.append(Paragraph(esc(bbody), styles["body"]))

    story.append(Paragraph("Les 5 méga-tendances qui créent les gagnants de 2027", styles["h2"]))
    for ttitle, tbody in PART_01_INTRO["trends_2027"]:
        story.append(CalloutBox(
            ttitle,
            [Paragraph(esc(tbody), styles["body_sm"])],
            bg=C_SAGE_BG, accent=C_EMERALD,
        ))
        story.append(Spacer(1, 6))

    story.append(Paragraph("Par quel secteur commencer selon ton profil ?", styles["h2"]))
    prof_rows = [[
        Paragraph("<b>Ton profil</b>", styles["body_sm"]),
        Paragraph("<b>Budget réaliste</b>", styles["body_sm"]),
        Paragraph("<b>Secteurs recommandés en priorité</b>", styles["body_sm"]),
    ]]
    for p_name, p_bud, p_sec in PART_01_INTRO["profiles"]:
        prof_rows.append([
            Paragraph(f"<b>{esc(p_name)}</b>", styles["body_sm"]),
            Paragraph(esc(p_bud), styles["body_sm"]),
            Paragraph(esc(p_sec), styles["body_sm"]),
        ])
    pr_tbl = Table(prof_rows, colWidths=[145, 115, CONTENT_W - 260])
    pr_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), C_GOLD_BG),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [C_WHITE, C_CREAM]),
        ("BOX", (0, 0), (-1, -1), 0.7, C_SAGE_BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, C_LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(pr_tbl)
    story.append(Spacer(1, 14))
    story.append(CalloutBox(
        "Comment combiner ce guide avec ton Workbook Jour 2",
        [Paragraph(
            esc(
                "1. Repère 3 idées dans tes secteurs prioritaires ci-dessus (Partie 03).  "
                "2. Applique la méthode VIN et le score sur 30 (Partie 04) pour élire ton idée n°1 en 48 heures.  "
                "3. Exécute le plan d'action Jour 1 à Jour 7 (Partie 05) et signe ta fiche d'engagement en Conclusion."
            ),
            styles["body_sm"],
        )],
        bg=C_SAGE_BG, accent=C_EMERALD,
    ))
    story.append(PageBreak())

    # --- PARTIE 02 : LES 7 ERREURS À ÉVITER ---
    story.append(PartHeaderFlowable(
        PART_02_ERRORS["kicker"], PART_02_ERRORS["title"],
        PART_02_ERRORS["workbook_question"],
        toc_text="Partie 02 — Les 7 erreurs fatales à éviter",
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph(esc(PART_02_ERRORS["intro"]), styles["body_sm"]))
    story.append(Spacer(1, 4))

    err_style = ParagraphStyle(
        "err_s", fontName="Sans", fontSize=8.4, leading=11.4,
        textColor=C_CHARCOAL, spaceAfter=0,
    )
    for err_title, err_cons, err_fix in PART_02_ERRORS["errors"]:
        story.append(KeepTogether([
            CalloutBox(
                err_title,
                [
                    Paragraph(f"<font color='#8C3614'><b>{esc(err_cons)}</b></font>", err_style),
                    Paragraph(f"<font color='#0B3B31'><b>{esc(err_fix)}</b></font>", err_style),
                ],
                bg=C_CREAM, accent=C_TERRACOTTA, title_color=colors.HexColor("#8C3614"),
                pad_v=5.5, gap_p=1.5,
            ),
            Spacer(1, 4.5),
        ]))
    story.append(PageBreak())

    # --- PARTIE 03 : ÉTAPE 1 — LES 500 IDÉES EN 20 SECTEURS ---
    story.append(PartHeaderFlowable(
        "PARTIE 03 • ÉTAPE 1",
        "Choisis ton idée parmi 500 opportunités rentables en 20 secteurs",
        "Réponse à la section 03 du Workbook : Première action concrète — Explorer et présélectionner ton Top 3.",
        toc_text="Partie 03 — Étape 1 : Les 500 Idées de Business (20 Secteurs)",
    ))
    story.append(Spacer(1, 10))
    story.append(CalloutBox(
        "Mode d'emploi rapide pour ne pas te perdre dans les 500 idées",
        [Paragraph(
            esc(
                "Ne cherche pas à lire les 500 fiches comme un roman. Parcours d'abord le Sommaire "
                "pour cibler les 3 ou 4 secteurs qui correspondent à ton budget et à ton environnement. "
                "Note 5 idées qui te parlent dès la lecture, puis emmène tes 3 favorites vers la Partie 04 "
                "(Validation Express en 48 heures)."
            ),
            styles["body_sm"],
        )],
        bg=C_GOLD_BG, accent=C_GOLD, title_color=colors.HexColor("#7D5106"),
    ))
    story.append(Spacer(1, 12))

    for idx_s, sector in enumerate(sectors):
        banner = SectorBannerFlowable(sector)
        first_card = IdeaCardFlowable(sector["ideas"][0], styles)
        # Empêche le bandeau secteur de rester seul en bas de page
        story.append(KeepTogether([banner, Spacer(1, 6), first_card, Spacer(1, 3.6)]))
        for idea in sector["ideas"][1:]:
            story.append(IdeaCardFlowable(idea, styles))
            story.append(Spacer(1, 3.6))
        if idx_s < len(sectors) - 1:
            story.append(PageBreak())

    story.append(PageBreak())

    # --- PARTIE 04 : ÉTAPE 2 — VALIDATION EXPRESS 48H ---
    story.append(PartHeaderFlowable(
        PART_04_VALIDATION["kicker"], PART_04_VALIDATION["title"],
        PART_04_VALIDATION["workbook_question"],
        toc_text="Partie 04 — Étape 2 : Valider ton Top 3 en 48 heures (Méthode VIN)",
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph(esc(PART_04_VALIDATION["intro"]), styles["lead"]))

    story.append(Paragraph("Rappel express de la Méthode VIN (issue du Workbook Jour 2)", styles["h2"]))
    for vt, vd in PART_04_VALIDATION["vin_reminders"]:
        story.append(CalloutBox(vt, [Paragraph(esc(vd), styles["body_sm"])], bg=C_SAGE_BG, accent=C_EMERALD))
        story.append(Spacer(1, 6))

    story.append(Paragraph("Le protocole terrain en 48 heures chrono", styles["h2"]))
    for st_t, st_d in PART_04_VALIDATION["steps_48h"]:
        story.append(Paragraph(f"<b>• {esc(st_t)} :</b> {esc(st_d)}", styles["body"]))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Grille de notation comparée de tes 3 idées finalistes (/30)", styles["h2"]))
    grid_rows = [[
        Paragraph("<b>Critère (note de 1 à 5)</b>", styles["body_sm"]),
        Paragraph("<b>Idée A</b>", ParagraphStyle("gc", fontName="Sans-Bold", fontSize=8.8, alignment=TA_CENTER)),
        Paragraph("<b>Idée B</b>", ParagraphStyle("gc", fontName="Sans-Bold", fontSize=8.8, alignment=TA_CENTER)),
        Paragraph("<b>Idée C</b>", ParagraphStyle("gc", fontName="Sans-Bold", fontSize=8.8, alignment=TA_CENTER)),
    ]]
    for c_title, c_desc in PART_04_VALIDATION["scoring_criteria"]:
        grid_rows.append([
            Paragraph(f"<b>{esc(c_title)}</b><br/><font color='#4B5854'>{esc(c_desc)}</font>", styles["body_sm"]),
            Paragraph("___ / 5", ParagraphStyle("gc2", alignment=TA_CENTER, fontSize=9)),
            Paragraph("___ / 5", ParagraphStyle("gc2", alignment=TA_CENTER, fontSize=9)),
            Paragraph("___ / 5", ParagraphStyle("gc2", alignment=TA_CENTER, fontSize=9)),
        ])
    grid_rows.append([
        Paragraph("<b>TOTAL FINAL (/30) — Garde l'idée >= 20/30</b>", styles["body_sm"]),
        Paragraph("<b>___ / 30</b>", ParagraphStyle("gc3", fontName="Sans-Bold", alignment=TA_CENTER, fontSize=9.2)),
        Paragraph("<b>___ / 30</b>", ParagraphStyle("gc3", fontName="Sans-Bold", alignment=TA_CENTER, fontSize=9.2)),
        Paragraph("<b>___ / 30</b>", ParagraphStyle("gc3", fontName="Sans-Bold", alignment=TA_CENTER, fontSize=9.2)),
    ])
    gtbl = Table(grid_rows, colWidths=[CONTENT_W - 180, 60, 60, 60], repeatRows=1)
    gtbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), C_GOLD_BG),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [C_WHITE, C_CREAM]),
        ("BACKGROUND", (0, -1), (-1, -1), C_SAGE_BG),
        ("BOX", (0, 0), (-1, -1), 0.7, C_SAGE_BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, C_LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(gtbl)
    story.append(Spacer(1, 12))
    story.append(CalloutBox(
        PART_04_VALIDATION["example_box_title"],
        [Paragraph(esc(line), styles["body_sm"]) for line in PART_04_VALIDATION["example_box_lines"]],
        bg=C_GOLD_BG, accent=C_GOLD, title_color=colors.HexColor("#7D5106"),
    ))
    story.append(PageBreak())

    # --- PARTIE 05 : ÉTAPE 3 — PLAN DE LANCEMENT 7 JOURS ---
    story.append(PartHeaderFlowable(
        PART_05_LAUNCH["kicker"], PART_05_LAUNCH["title"],
        PART_05_LAUNCH["workbook_question"],
        toc_text="Partie 05 — Étape 3 : Plan d'action 7 jours, Scripts & Trésorerie",
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph(esc(PART_05_LAUNCH["intro"]), styles["lead"]))

    story.append(Paragraph("Feuille de route jour par jour (Jour 1 à Jour 7)", styles["h2"]))
    d_rows = []
    for d_num, d_title, d_desc in PART_05_LAUNCH["days"]:
        d_rows.append([
            Paragraph(f"<b>{esc(d_num)}</b>", ParagraphStyle("dn", fontName="Sans-Bold", fontSize=9.2, textColor=C_EMERALD, alignment=TA_CENTER)),
            Paragraph(f"<b>{esc(d_title)}</b><br/><font color='#4B5854'>{esc(d_desc)}</font>", styles["body_sm"]),
        ])
    dtbl = Table(d_rows, colWidths=[64, CONTENT_W - 64])
    dtbl.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [C_SAGE_BG, C_WHITE]),
        ("BOX", (0, 0), (-1, -1), 0.7, C_SAGE_BORDER),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, C_LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(dtbl)
    story.append(Spacer(1, 10))

    story.append(Paragraph("3 Scripts commerciaux prêts à copier-coller", styles["h2"]))
    for sc_t, sc_b in PART_05_LAUNCH["scripts"]:
        story.append(KeepTogether([
            CalloutBox(sc_t, [Paragraph(esc(sc_b), styles["body_sm"])], bg=C_CREAM, accent=C_GOLD),
            Spacer(1, 6),
        ]))

    story.append(Paragraph("Fixer ton prix juste & Règle des 3 Enveloppes", styles["h2"]))
    for pf in PART_05_LAUNCH["pricing_formula"]:
        story.append(Paragraph(esc(pf), styles["body_sm"]))
    story.append(Spacer(1, 6))
    for env_t, env_d in PART_05_LAUNCH["envelopes"]:
        story.append(KeepTogether([
            CalloutBox(env_t, [Paragraph(esc(env_d), styles["body_sm"])], bg=C_SAGE_BG, accent=C_EMERALD),
            Spacer(1, 5),
        ]))
    story.append(PageBreak())

    # --- CONCLUSION & PAGE AUTEUR ---
    story.append(PartHeaderFlowable(
        CONCLUSION_CONTENT["kicker"], CONCLUSION_CONTENT["title"],
        CONCLUSION_CONTENT["workbook_question"],
        toc_text="Conclusion — Prochain pas, Engagement 48h & À propos de l'auteur",
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph(esc(CONCLUSION_CONTENT["message"]), styles["body"]))
    story.append(Spacer(1, 6))
    story.append(CalloutBox(
        "Mantra du Workbook Jour 2",
        [Paragraph(esc(CONCLUSION_CONTENT["mantra"]), styles["quote"])],
        bg=C_GOLD_BG, accent=C_GOLD, title_color=colors.HexColor("#7D5106"),
    ))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Tes 3 prochains pas dès la fermeture de ce livre", styles["h2"]))
    for ns in CONCLUSION_CONTENT["next_steps_reader"]:
        story.append(Paragraph(esc(ns), styles["body"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Ma Fiche d'Engagement Terrain (À remplir maintenant)", styles["h2"]))
    sheet_rows = [[Paragraph(f"☐  {esc(line)}", styles["body_sm"])] for line in CONCLUSION_CONTENT["action_sheet"]]
    stbl = Table(sheet_rows, colWidths=[CONTENT_W])
    stbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), C_CREAM),
        ("BOX", (0, 0), (-1, -1), 0.8, C_GOLD),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, C_LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story.append(stbl)
    story.append(Spacer(1, 16))

    story.append(CalloutBox(
        f"À propos de l'auteur : {config.get('author_name', '[Ton Nom / Ta Marque]')}",
        [
            Paragraph(f"<b>{esc(config.get('author_role', ''))}</b>", styles["body_sm"]),
            Paragraph(esc(config.get("author_bio", "")), styles["body_sm"]),
            Paragraph(
                f"<b>WhatsApp :</b> {esc(config.get('contact_whatsapp', ''))}  •  "
                f"<b>Réseaux :</b> {esc(config.get('contact_social', ''))}  •  "
                f"<b>Email :</b> {esc(config.get('contact_email', ''))}",
                styles["body_muted"],
            ),
        ],
        bg=C_SAGE_BG, accent=C_EMERALD_DARK,
    ))

    doc.multiBuild(story)
    return doc.page


# ---------------------------------------------------------------------------
# EXPORTS MARKDOWN ÉDITABLES
# ---------------------------------------------------------------------------

def write_markdown_exports(config, sectors, ebook_pages=None):
    """Écrit les versions Markdown complètes pour personnalisation libre dans Notion/Docs/Word."""
    wb = get_workbook_pages_data(config, ebook_pages=ebook_pages)
    wb_lines = [
        f"# Workbook Officiel Jour 2 — Dossier Rempli : {config['ebook_title']}",
        "",
        f"> Auteur : **{wb['author']}** | Date : **{wb['date']}**",
        "",
        "## Page 1 — Bienvenue",
        wb["page1"]["welcome"],
        "",
    ]
    for k, v in wb["page1"]["summary_rows"]:
        wb_lines.append(f"- **{k}** : {v}")
    wb_lines += [
        "",
        "## Page 2 — Objectif & Engagement personnel",
        wb["page2"]["intro"],
        f"\n> {wb['page2']['quote']}\n",
    ]
    for k, v in wb["page2"]["commitment"]:
        wb_lines.append(f"- **{k}** : {v}")
    wb_lines += [
        "",
        "## Page 3 — Validation Express (Méthode VIN)",
        f"- **V – Problème (Valeur)** : {wb['page3']['V']}",
        f"- **I – Intensité** : {wb['page3']['I_score']} — {wb['page3']['I_exp']}",
        f"- **N – Nombre** : {wb['page3']['N']}",
        f"- **{wb['page3']['conclusion']}**",
        "",
        "## Page 4 — Promesse Claire",
        f"- **1. Pour qui ?** {wb['page4']['q1']}",
        f"- **2. Résultat concret :** {wb['page4']['q2']}",
        f"- **3. Délai :** {wb['page4']['q3']}",
        f"- **Formule complétée :** {wb['page4']['formula_filled']}",
        "",
        "## Page 5 — Format PDF",
        f"- **Pourquoi le PDF :** {wb['page5']['why_chosen']}",
        f"- **Pagination :** {wb['page5']['pages_note']}",
        f"- **Titre :** {wb['page5']['provisional_title']}",
        "",
        "## Page 6 — Structure en 5 Parties + Conclusion",
    ]
    for num, lbl, desc in wb["page6"]["parts"]:
        wb_lines.append(f"- **{num} — {lbl}** : {desc}")
    wb_lines += [
        "",
        "## Page 7 — IA & Checklist",
        f"**Prompt appliqué :** {wb['page7']['prompt_applied']}",
        "",
        "**Checklist de création :**",
    ]
    for lbl, _ in wb["page7"]["checklist"]:
        wb_lines.append(f"- [x] {lbl}")
    wb_lines += [
        "",
        "## Page 8 — Récapitulatif",
    ]
    for t_r, d_r, s_r in wb["page8"]["recap_cards"]:
        wb_lines.append(f"- **{t_r}** ({s_r}) : {d_r}")
    wb_lines += [
        "",
        "## Page 9 — Déclaration officielle & Posts Facebook",
    ]
    for k, v in wb["page9"]["declaration"]:
        wb_lines.append(f"- **{k}** : {v}")
    wb_lines.append("")
    for pt, pb in wb["page9"]["social_posts"]:
        wb_lines.append(f"### {pt}\n{pb}\n")
    wb_lines += [
        "## Page 10 — Prochains pas",
    ]
    for st_t, st_b in wb["page10"]["steps"]:
        wb_lines.append(f"- **{st_t}** : {st_b}")
    wb_lines.append(f"\n```\n{wb['page10']['whatsapp_testers']}\n```")
    OUT_WORKBOOK_MD.write_text("\n".join(wb_lines), encoding="utf-8")

    eb_lines = [
        f"# {config['ebook_title']}",
        f"*{config['ebook_subtitle']}*",
        "",
        f"**Promesse :** {config['promise_formula']}",
        "",
        f"**Auteur :** {config['author_name']} | **Date :** {config['date_creation']}",
        "",
        "---",
        "",
        f"## Partie 01 — {PART_01_INTRO['title']}",
        PART_01_INTRO["lead"],
        "",
    ]
    for bt, bb in PART_01_INTRO["problem_blocks"]:
        eb_lines.append(f"### {bt}\n{bb}\n")
    for tt, tb in PART_01_INTRO["trends_2027"]:
        eb_lines.append(f"- **{tt}** : {tb}")
    eb_lines += ["", f"## Partie 02 — {PART_02_ERRORS['title']}", PART_02_ERRORS["intro"], ""]
    for et, ec, ef in PART_02_ERRORS["errors"]:
        eb_lines.append(f"### {et}\n- {ec}\n- {ef}\n")
    eb_lines += ["", "## Partie 03 — Étape 1 : Les 500 Idées de Business en 20 Secteurs", ""]
    for s in sectors:
        eb_lines.append(f"### Secteur {s['num']:02d} : {s['title']} (#{s['start_id']:03d}–#{s['end_id']:03d})")
        eb_lines.append(s["intro"])
        eb_lines.append("")
        for it in s["ideas"]:
            eb_lines.append(f"- **#{it['code']} — {it['title']}** *[{it['budget']}]* : {it['desc']}")
        eb_lines.append("")
    eb_lines += ["", f"## Partie 04 — {PART_04_VALIDATION['title']}", PART_04_VALIDATION["intro"], ""]
    for vt, vd in PART_04_VALIDATION["vin_reminders"]:
        eb_lines.append(f"- **{vt}** : {vd}")
    eb_lines += ["", f"## Partie 05 — {PART_05_LAUNCH['title']}", PART_05_LAUNCH["intro"], ""]
    for dn, dt, dd in PART_05_LAUNCH["days"]:
        eb_lines.append(f"- **{dn} — {dt}** : {dd}")
    eb_lines.append("")
    for st, sb in PART_05_LAUNCH["scripts"]:
        eb_lines.append(f"### {st}\n{sb}\n")
    eb_lines += [
        "",
        f"## Conclusion — {CONCLUSION_CONTENT['title']}",
        CONCLUSION_CONTENT["message"],
        "",
        f"> {CONCLUSION_CONTENT['mantra']}",
    ]
    OUT_EBOOK_MD.write_text("\n".join(eb_lines), encoding="utf-8")


def main():
    import pymupdf

    register_fonts()
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    sectors = get_numbered_sectors()
    styles = build_styles()

    print("1/3 Génération de l'Ebook complet 500 idées...")
    build_ebook_pdf(config, sectors, styles)
    with pymupdf.open(str(OUT_EBOOK_PDF)) as eb_doc:
        ebook_pages = len(eb_doc)
    print(f"    -> {OUT_EBOOK_PDF} ({ebook_pages} pages)")

    print("2/3 Génération du Workbook Jour 2 rempli (10 pages exactes)...")
    build_workbook_pdf(config, styles, ebook_pages=ebook_pages)
    with pymupdf.open(str(OUT_WORKBOOK_PDF)) as wb_doc:
        wb_pages = len(wb_doc)
    print(f"    -> {OUT_WORKBOOK_PDF} ({wb_pages} pages)")

    print("3/3 Export des sources Markdown éditables...")
    write_markdown_exports(config, sectors, ebook_pages=ebook_pages)
    print(f"    -> {OUT_WORKBOOK_MD}")
    print(f"    -> {OUT_EBOOK_MD}")
    print("Terminé avec succès !")


if __name__ == "__main__":
    main()
