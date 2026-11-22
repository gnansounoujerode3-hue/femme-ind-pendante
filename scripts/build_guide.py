#!/usr/bin/env python3
"""
Générateur PDF haute qualité pour :
« Guide Ultime : Décroche ta Bourse Française Toi-Même, Sans Payer une Agence »
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, NextPageTemplate,
    Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, Flowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from PIL import Image as PILImage

# --- Chemins ---
REPO_ROOT = "/home/user/femme-ind-pendante"
OUTPUT_PDF = os.path.join(REPO_ROOT, "Guide-Ultime-Decroche-Ta-Bourse-Francaise-Sans-Agence.pdf")
COVER_ART = os.path.join(REPO_ROOT, "assets", "cover-art.png")

ROBOTO_DIR = "/tmp/venv/lib/python3.11/site-packages/font_roboto/files"
SERIF_DIR = "/tmp/venv/lib/python3.11/site-packages/font_source_serif_pro/files"
DEJAVU_TTF = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DEJAVU_BOLD_TTF = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# --- Enregistrement des polices ---
pdfmetrics.registerFont(TTFont("Roboto", os.path.join(ROBOTO_DIR, "Roboto-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Roboto-Medium", os.path.join(ROBOTO_DIR, "Roboto-Medium.ttf")))
pdfmetrics.registerFont(TTFont("Roboto-Bold", os.path.join(ROBOTO_DIR, "Roboto-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Roboto-Italic", os.path.join(ROBOTO_DIR, "Roboto-Italic.ttf")))
pdfmetrics.registerFont(TTFont("Roboto-BoldItalic", os.path.join(ROBOTO_DIR, "Roboto-BoldItalic.ttf")))
registerFontFamily(
    "Roboto",
    normal="Roboto",
    bold="Roboto-Bold",
    italic="Roboto-Italic",
    boldItalic="Roboto-BoldItalic",
)

pdfmetrics.registerFont(TTFont("Serif", os.path.join(SERIF_DIR, "SourceSerifPro-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Serif-Semibold", os.path.join(SERIF_DIR, "SourceSerifPro-Semibold.ttf")))
pdfmetrics.registerFont(TTFont("Serif-Bold", os.path.join(SERIF_DIR, "SourceSerifPro-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Serif-Italic", os.path.join(SERIF_DIR, "SourceSerifPro-It.ttf")))
pdfmetrics.registerFont(TTFont("Serif-BoldItalic", os.path.join(SERIF_DIR, "SourceSerifPro-BoldIt.ttf")))
registerFontFamily(
    "Serif",
    normal="Serif",
    bold="Serif-Bold",
    italic="Serif-Italic",
    boldItalic="Serif-BoldItalic",
)

# DejaVu pour les symboles Unicode nets (✓, ☐, →, ▪)
pdfmetrics.registerFont(TTFont("Sym", DEJAVU_TTF))
pdfmetrics.registerFont(TTFont("Sym-Bold", DEJAVU_BOLD_TTF))

# --- Palette éditoriale parisienne ---
NAVY = colors.HexColor("#132238")
NAVY_SOFT = colors.HexColor("#1E3454")
GOLD = colors.HexColor("#C59B43")
IVORY = colors.HexColor("#FAF7F2")
PAPER = colors.HexColor("#FFFFFF")
SLATE = colors.HexColor("#2B3440")
MUTED = colors.HexColor("#667085")
BORDER = colors.HexColor("#E4DFD5")
BURGUNDY = colors.HexColor("#9E3333")
BURGUNDY_BG = colors.HexColor("#FDF3F3")
FOREST = colors.HexColor("#1B664C")
FOREST_BG = colors.HexColor("#F0F8F5")
BLUE_TINT = colors.HexColor("#F2F5FA")

PAGE_W, PAGE_H = A4
MARGIN_X = 48
MARGIN_TOP = 54
MARGIN_BOTTOM = 48
CONTENT_W = PAGE_W - 2 * MARGIN_X

# --- Styles typographiques ---
S = {
    "kicker": ParagraphStyle(
        "kicker", fontName="Roboto-Bold", fontSize=8.5, leading=11,
        textColor=GOLD, spaceAfter=4, letterSpacing=1.1
    ),
    "h1": ParagraphStyle(
        "h1", fontName="Serif-Bold", fontSize=20.5, leading=25,
        textColor=NAVY, spaceAfter=6
    ),
    "h2": ParagraphStyle(
        "h2", fontName="Serif-Bold", fontSize=13, leading=17,
        textColor=NAVY, spaceBefore=10, spaceAfter=4.5
    ),
    "body": ParagraphStyle(
        "body", fontName="Roboto", fontSize=9.5, leading=14.2,
        textColor=SLATE, spaceAfter=5.5, alignment=TA_LEFT
    ),
    "body_small": ParagraphStyle(
        "body_small", fontName="Roboto", fontSize=8.8, leading=13,
        textColor=SLATE, spaceAfter=4
    ),
    "lead": ParagraphStyle(
        "lead", fontName="Serif-Italic", fontSize=10.8, leading=15.5,
        textColor=NAVY_SOFT, spaceAfter=8
    ),
    "bullet": ParagraphStyle(
        "bullet", fontName="Roboto", fontSize=9.2, leading=13.5,
        textColor=SLATE, leftIndent=18, firstLineIndent=-14, spaceAfter=4
    ),
    "caption": ParagraphStyle(
        "caption", fontName="Roboto", fontSize=8, leading=11,
        textColor=MUTED
    ),
    "th": ParagraphStyle(
        "th", fontName="Roboto-Bold", fontSize=8.2, leading=11,
        textColor=PAPER
    ),
    "td": ParagraphStyle(
        "td", fontName="Roboto", fontSize=8.1, leading=11.3,
        textColor=SLATE
    ),
    "td_bold": ParagraphStyle(
        "td_bold", fontName="Roboto-Bold", fontSize=8.1, leading=11.3,
        textColor=NAVY
    ),
    "card_title": ParagraphStyle(
        "card_title", fontName="Roboto-Bold", fontSize=9.6, leading=13,
        textColor=NAVY, spaceAfter=3
    ),
    "card_body": ParagraphStyle(
        "card_body", fontName="Roboto", fontSize=8.8, leading=13,
        textColor=SLATE, spaceAfter=2.5
    ),
    "toc_num": ParagraphStyle(
        "toc_num", fontName="Serif-Bold", fontSize=12, leading=15,
        textColor=GOLD
    ),
    "toc_title": ParagraphStyle(
        "toc_title", fontName="Roboto-Bold", fontSize=10, leading=14,
        textColor=NAVY
    ),
    "toc_sub": ParagraphStyle(
        "toc_sub", fontName="Roboto", fontSize=8.5, leading=12,
        textColor=MUTED
    ),
    "toc_page": ParagraphStyle(
        "toc_page", fontName="Roboto-Bold", fontSize=9.5, leading=14,
        textColor=NAVY_SOFT, alignment=TA_RIGHT
    ),
}


# --- Flowables personnalisés ---
class GoldRule(Flowable):
    def __init__(self, width=50, thickness=2.2, color=GOLD, space_after=8):
        super().__init__()
        self.rule_width = width
        self.thickness = thickness
        self.color = color
        self.space_after = space_after
        self.width = width
        self.height = thickness + space_after

    def draw(self):
        self.canv.saveState()
        self.canv.setFillColor(self.color)
        self.canv.roundRect(0, self.space_after, self.rule_width, self.thickness, 1, stroke=0, fill=1)
        self.canv.restoreState()


class SectionHeader(Flowable):
    """En-tête de chapitre éditorial numéroté avec filet doré."""
    def __init__(self, number, kicker, title, subtitle=None):
        super().__init__()
        self.number = number
        self.kicker = kicker
        self.title = title
        self.subtitle = subtitle
        self._p_kicker = Paragraph(kicker.upper(), S["kicker"])
        self._p_title = Paragraph(title, S["h1"])
        self._p_sub = Paragraph(subtitle, S["lead"]) if subtitle else None

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        text_w = availWidth - 46
        _, h_k = self._p_kicker.wrap(text_w, availHeight)
        _, h_t = self._p_title.wrap(text_w, availHeight)
        h_s = 0
        if self._p_sub:
            _, h_s = self._p_sub.wrap(availWidth, availHeight)
            h_s += 3
        self._h_k = h_k
        self._h_t = h_t
        self._h_s = h_s
        self._top_h = max(36, h_k + h_t + 2)
        self.height = self._top_h + 9 + h_s + 3
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.saveState()
        badge_y = self.height - 35
        c.setFillColor(NAVY)
        c.roundRect(0, badge_y, 34, 34, 5, stroke=0, fill=1)
        c.setFillColor(GOLD)
        c.setFont("Serif-Bold", 15)
        c.drawCentredString(17, badge_y + 11, self.number)

        y_k = self.height - self._h_k - 1
        self._p_kicker.drawOn(c, 46, y_k)
        y_t = y_k - self._h_t - 1
        self._p_title.drawOn(c, 46, y_t)

        line_y = self.height - self._top_h - 3
        c.setFillColor(GOLD)
        c.rect(0, line_y, 52, 2.2, stroke=0, fill=1)
        c.setFillColor(BORDER)
        c.rect(56, line_y + 0.7, self.width - 56, 0.8, stroke=0, fill=1)

        if self._p_sub:
            self._p_sub.drawOn(c, 0, line_y - self._h_s + 2)
        c.restoreState()


def make_callout(title, paragraphs, bg=IVORY, accent=GOLD, title_color=NAVY, pad_v=8, space_after=7):
    inner = []
    if title:
        st = ParagraphStyle("ct", parent=S["card_title"], textColor=title_color)
        inner.append(Paragraph(title, st))
    for p in paragraphs:
        if isinstance(p, str):
            inner.append(Paragraph(p, S["card_body"]))
        else:
            inner.append(p)
    t = Table([[inner]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 3.5, accent),
        ("BOX", (0, 0), (-1, -1), 0.5, BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), pad_v),
        ("BOTTOMPADDING", (0, 0), (-1, -1), pad_v),
        ("LEFTPADDING", (0, 0), (-1, -1), 13),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    return KeepTogether([t, Spacer(1, space_after)])


def make_stat_strip(items):
    col_w = (CONTENT_W - 14) / len(items)
    cells = []
    for big, label, sub in items:
        p_big = Paragraph(
            big,
            ParagraphStyle("sb", fontName="Serif-Bold", fontSize=18, leading=21, textColor=GOLD, alignment=TA_CENTER)
        )
        p_lbl = Paragraph(
            label,
            ParagraphStyle("sl", fontName="Roboto-Bold", fontSize=8.8, leading=11.5, textColor=NAVY, alignment=TA_CENTER, spaceBefore=2)
        )
        p_sub = Paragraph(
            sub,
            ParagraphStyle("ss", fontName="Roboto", fontSize=7.8, leading=10.5, textColor=MUTED, alignment=TA_CENTER, spaceBefore=2)
        )
        cells.append([p_big, p_lbl, p_sub])

    row = []
    widths = []
    for idx, cell in enumerate(cells):
        row.append(cell)
        widths.append(col_w)
        if idx < len(cells) - 1:
            row.append("")
            widths.append(7)

    t = Table([row], colWidths=widths)
    styles = [
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    for idx in range(len(cells)):
        c_idx = idx * 2
        styles.append(("BACKGROUND", (c_idx, 0), (c_idx, 0), IVORY))
        styles.append(("BOX", (c_idx, 0), (c_idx, 0), 0.7, BORDER))
        styles.append(("LINEABOVE", (c_idx, 0), (c_idx, 0), 2.5, NAVY))
    t.setStyle(TableStyle(styles))
    return KeepTogether([t, Spacer(1, 10)])


def make_styled_table(headers, rows, col_widths, font_size=8.1, pad_v=5.2):
    th_style = ParagraphStyle("th_dyn", parent=S["th"], fontSize=font_size, leading=font_size + 3)
    td_style = ParagraphStyle("td_dyn", parent=S["td"], fontSize=font_size, leading=font_size + 3.1)
    td_b_style = ParagraphStyle("tdb_dyn", parent=S["td_bold"], fontSize=font_size, leading=font_size + 3.1)

    data = [[Paragraph(h, th_style) for h in headers]]
    for r in rows:
        row_cells = []
        for idx, val in enumerate(r):
            if idx == 0:
                row_cells.append(Paragraph(val, td_b_style))
            else:
                row_cells.append(Paragraph(val, td_style))
        data.append(row_cells)

    t = Table(data, colWidths=col_widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), PAPER),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, BORDER),
        ("TOPPADDING", (0, 0), (-1, 0), 6.5),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6.5),
        ("TOPPADDING", (0, 1), (-1, -1), pad_v),
        ("BOTTOMPADDING", (0, 1), (-1, -1), pad_v),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    for i in range(1, len(data)):
        style.append(("BACKGROUND", (0, i), (-1, i), IVORY if i % 2 == 0 else PAPER))
    t.setStyle(TableStyle(style))
    return t


def sym_span(symbol, color_hex="#1B664C", size=None):
    sz = f' size="{size}"' if size else ""
    return f'<font name="Sym-Bold" color="{color_hex}"{sz}>{symbol}</font>'


def bullet(text, symbol="01", color_hex="#C59B43", use_sym_font=False):
    if use_sym_font:
        prefix = sym_span(symbol, color_hex)
    else:
        prefix = f'<font name="Roboto-Bold" color="{color_hex}">{symbol}</font>'
    return Paragraph(f'{prefix}&nbsp;&nbsp;{text}', S["bullet"])


def checkbox_item(text):
    return Paragraph(
        f'{sym_span("☐", "#1B664C", size=10)}&nbsp;&nbsp;{text}',
        ParagraphStyle("chk", parent=S["bullet"], leftIndent=16, firstLineIndent=-14, spaceAfter=5)
    )


# --- Dessin de la Couverture (Page 1) ---
def draw_cover_page(canvas, doc):
    c = canvas
    c.saveState()

    c.setFillColor(NAVY)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    img_x = 46
    img_y = 355
    img_w = PAGE_W - 92
    img_h = 415

    c.setStrokeColor(GOLD)
    c.setLineWidth(0.9)
    c.rect(24, 24, PAGE_W - 48, PAGE_H - 48, stroke=1, fill=0)

    c.setFillColor(GOLD)
    c.setFont("Roboto-Bold", 8.4)
    c.drawString(46, PAGE_H - 46, "ÉDITION 2026 – 2027   •   MÉTHODE 100 % AUTONOME & OFFICIELLE")
    c.setFillColor(colors.HexColor("#B8C5D6"))
    c.setFont("Roboto-Medium", 8.4)
    c.drawRightString(PAGE_W - 46, PAGE_H - 46, "AFRIQUE FRANCOPHONE  •  FRANCE")

    c.setStrokeColor(colors.HexColor("#2B4162"))
    c.setLineWidth(0.6)
    c.line(46, PAGE_H - 55, PAGE_W - 46, PAGE_H - 55)

    if os.path.exists(COVER_ART):
        im = PILImage.open(COVER_ART)
        iw, ih = im.size
        target_ratio = img_w / img_h
        src_ratio = iw / ih
        if src_ratio > target_ratio:
            new_w = int(ih * target_ratio)
            left = (iw - new_w) // 2
            cropped = im.crop((left, 0, left + new_w, ih))
        else:
            new_h = int(iw / target_ratio)
            top = int((ih - new_h) * 0.18)
            cropped = im.crop((0, top, iw, top + new_h))
        tmp_crop = "/tmp/cover_art_cropped.jpg"
        cropped.convert("RGB").save(tmp_crop, quality=94)

        c.setStrokeColor(GOLD)
        c.setLineWidth(1.5)
        c.rect(img_x - 3, img_y - 3, img_w + 6, img_h + 6, stroke=1, fill=0)
        c.drawImage(tmp_crop, img_x, img_y, width=img_w, height=img_h, preserveAspectRatio=False)

        c.setFillColor(NAVY)
        c.rect(img_x, img_y, 206, 28, stroke=0, fill=1)
        c.setFillColor(GOLD)
        c.rect(img_x, img_y, 4, 28, stroke=0, fill=1)
        c.setFont("Roboto-Bold", 8.5)
        c.setFillColor(PAPER)
        c.drawString(img_x + 14, img_y + 10, "GUIDE PRATIQUE COMPLET  •  12 PAGES")

    c.setFillColor(GOLD)
    c.setFont("Roboto-Bold", 10.5)
    c.drawString(46, 322, "GUIDE ULTIME POUR")

    c.setFillColor(GOLD)
    c.rect(46, 311, 56, 2.5, stroke=0, fill=1)

    title_style = ParagraphStyle(
        "cover_title",
        fontName="Serif-Bold",
        fontSize=27.5,
        leading=33,
        textColor=PAPER,
    )
    p_title = Paragraph("Décroche ta Bourse Française Toi-Même, Sans Payer une Agence", title_style)
    _, th = p_title.wrap(PAGE_W - 92, 160)
    p_title.drawOn(c, 46, 302 - th)

    sub_style = ParagraphStyle(
        "cover_sub",
        fontName="Roboto",
        fontSize=10.8,
        leading=16,
        textColor=colors.HexColor("#D2DCE8"),
    )
    p_sub = Paragraph(
        "La feuille de route étape par étape pour repérer les bourses 2026–2027 ouvertes aux étudiants d'Afrique francophone, bâtir un dossier irrésistible et réussir Campus France en toute autonomie.",
        sub_style
    )
    _, sh = p_sub.wrap(PAGE_W - 92, 90)
    p_sub.drawOn(c, 46, 288 - th - sh)

    footer_y = 48
    c.setStrokeColor(colors.HexColor("#2B4162"))
    c.setLineWidth(0.8)
    c.line(46, footer_y + 38, PAGE_W - 46, footer_y + 38)

    cols = [
        ("10+ BOURSES PHARES", "Eiffel, BGF, Paris-Saclay, Erasmus…"),
        ("MODÈLES INCLUS", "Lettre, email université & checklist"),
        ("0 FCFA D'AGENCE", "Portails 100 % officiels & gratuits"),
    ]
    col_step = (PAGE_W - 92) / 3
    for i, (h, sub) in enumerate(cols):
        cx = 46 + i * col_step
        c.setFillColor(GOLD)
        c.setFont("Roboto-Bold", 8.2)
        c.drawString(cx, footer_y + 20, h)
        c.setFillColor(colors.HexColor("#B8C5D6"))
        c.setFont("Roboto", 7.8)
        c.drawString(cx, footer_y + 7, sub)

    c.restoreState()


def draw_interior_page(canvas, doc):
    c = canvas
    c.saveState()

    c.setStrokeColor(BORDER)
    c.setLineWidth(0.6)
    c.line(MARGIN_X, PAGE_H - 36, PAGE_W - MARGIN_X, PAGE_H - 36)

    c.setFillColor(GOLD)
    c.rect(MARGIN_X, PAGE_H - 36.6, 24, 1.5, stroke=0, fill=1)

    c.setFillColor(MUTED)
    c.setFont("Roboto-Medium", 7.6)
    c.drawString(MARGIN_X, PAGE_H - 30, "GUIDE ULTIME  •  DÉCROCHE TA BOURSE FRANÇAISE TOI-MÊME")
    c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 30, "ÉDITION 2026–2027")

    c.setStrokeColor(BORDER)
    c.setLineWidth(0.6)
    c.line(MARGIN_X, 34, PAGE_W - MARGIN_X, 34)

    c.setFillColor(MUTED)
    c.setFont("Roboto", 7.6)
    c.drawString(MARGIN_X, 21, "Méthode 100 % officielle & autonome — Sans intermédiaire ni agence")

    pg = doc.page
    c.setFillColor(NAVY)
    c.roundRect(PAGE_W - MARGIN_X - 24, 17, 24, 14, 3, stroke=0, fill=1)
    c.setFillColor(PAPER)
    c.setFont("Roboto-Bold", 8)
    c.drawCentredString(PAGE_W - MARGIN_X - 12, 21, str(pg))

    c.restoreState()


def build_story():
    story = []

    # Page 1 : Couverture
    story.append(NextPageTemplate("interior"))
    story.append(Spacer(1, 10))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2 : SOMMAIRE & PROMESSE DU GUIDE
    # =========================================================================
    story.append(Paragraph("BIENVENUE DANS TON GUIDE PRATIQUE", S["kicker"]))
    story.append(Paragraph("Sommaire & Promesse", S["h1"]))
    story.append(GoldRule(56, 2.4, GOLD, 10))

    story.append(make_callout(
        "La promesse de ce guide",
        [
            "<b>Comment identifier les meilleures bourses françaises, monter un dossier solide et réussir ta procédure Campus France en toute autonomie — sans jamais payer une agence intermédiaire.</b>",
            "Ce guide a été conçu spécialement pour les étudiantes et étudiants d'Afrique francophone (Licence, Master, Doctorat) qui veulent reprendre le contrôle total de leur avenir académique grâce à une méthode claire, structurée et 100 % basée sur les portails officiels."
        ],
        bg=IVORY, accent=GOLD, title_color=NAVY
    ))

    story.append(make_stat_strip([
        ("0 FCFA", "Honoraires d'agence", "Tu gardes ton budget pour les vrais frais officiels"),
        ("700+", "Bourses recensées", "Disponibles gratuitement sur Campus Bourses"),
        ("5 Étapes", "Méthode claire", "Du ciblage jusqu'au visa étudiant"),
    ]))

    story.append(Paragraph("Ce que tu vas découvrir page après page", S["h2"]))

    toc_entries = [
        ("01", "Introduction : Pourquoi tu n'as pas besoin d'une agence",
         "La vérité sur les intermédiaires, ce qu'ils ne peuvent pas faire et ton vrai avantage.", "3"),
        ("02", "Les 7 erreurs fatales qui éliminent 80 % des candidats",
         "Les pièges de calendrier, de dossier et d'arnaques à éviter absolument.", "4"),
        ("03", "Étape 1 : Cartographier & cibler les meilleures bourses 2026–2027",
         "Tableau comparatif des 10 bourses phares, Campus Bourses et calendrier officiel.", "5–6"),
        ("04", "Étape 2 : Bâtir un dossier de candidature irrésistible",
         "Pièces maîtresses, méthode C-P-I, modèle de lettre et email aux universités.", "7–8"),
        ("05", "Étape 3 : Réussir Campus France, l'entretien et le visa",
         "Études en France (DAP / Hors-DAP), 8 questions d'entretien et dossier France-Visas.", "9–10"),
        ("06", "Boîte à outils : Portails officiels & tableau de suivi",
         "Annuaire des sites 100 % gratuits et ton tableau prêt à remplir.", "11"),
        ("07", "Conclusion : Ton plan d'action sur 30 jours & checklist finale",
         "Feuille de route semaine par semaine pour passer à l'action dès aujourd'hui.", "12"),
    ]

    toc_rows = []
    for num, title, sub, pg in toc_entries:
        toc_rows.append([
            Paragraph(num, S["toc_num"]),
            [Paragraph(title, S["toc_title"]), Paragraph(sub, S["toc_sub"])],
            Paragraph(f"p. {pg}", S["toc_page"]),
        ])

    toc_table = Table(toc_rows, colWidths=[32, CONTENT_W - 76, 44])
    toc_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 7.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(toc_table)
    story.append(Spacer(1, 10))

    story.append(make_callout(
        "Comment utiliser ce guide efficacement ?",
        [
            "Ne te contente pas de le lire d'une traite. Prends un cahier dédié (ou un dossier Google Drive nommé <i>« Bourse France 2027 »</i>), surligne les bourses qui correspondent à ton niveau et coche chaque étape au fur et à mesure. <b>Ton objectif n'est pas la perfection : c'est d'envoyer des dossiers propres, cohérents et avant les dates limites.</b>"
        ],
        bg=BLUE_TINT, accent=NAVY, title_color=NAVY
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 3 : PARTIE 01 — INTRODUCTION
    # =========================================================================
    story.append(SectionHeader(
        "01", "Introduction",
        "Pourquoi tu n'as PAS besoin de payer une agence",
        "Chaque année, des milliers d'étudiants francophones dépensent entre 300 000 et 2 000 000 FCFA pour des démarches entièrement publiques, gratuites et accessibles en ligne."
    ))

    story.append(Paragraph(
        "Si tu rêves d'étudier en France avec une bourse, tu as sûrement vu passer des publicités sur Facebook, TikTok ou WhatsApp promettant : <i>« Bourse garantie à 100 % », « Admission + Visa clé en main »</i>. La tentation de payer un intermédiaire est compréhensible : la procédure semble complexe et la peur de se tromper paralyse.",
        S["body"]
    ))
    story.append(Paragraph(
        "Pourtant, la réalité du système français est limpide : <b>aucune agence privée au monde ne possède de passe-droit auprès de Campus France, des universités publiques, du ministère des Affaires étrangères ou du consulat.</b> Tout se déroule sur des plateformes officielles ouvertes directement aux candidats.",
        S["body"]
    ))

    story.append(Paragraph("Ce qu'une agence fait vraiment… et ce qu'elle ne peut PAS faire", S["h2"]))

    comp_rows = [
        ["Accès aux offres de bourses",
         "Consulte les mêmes sites publics que toi (Campus Bourses, sites des universités).",
         "Tu accèdes gratuitement aux 700+ bourses en 15 minutes."],
        ["Dossier Études en France",
         "Crée un compte avec ton email (parfois le sien !) et téléverse tes propres PDF.",
         "Tu gardes tes identifiants et contrôles chaque pièce déposée."],
        ["Lettre de motivation",
         "Utilise souvent un modèle standard recyclé pour des dizaines de candidats.",
         "Tu rédiges un projet authentique, cohérent avec ton parcours."],
        ["Entretien & Jury de bourse",
         "Ne peut pas entrer dans la salle d'entretien à ta place.",
         "Ayant monté ton dossier, tu réponds avec aisance et crédibilité."],
        ["Décision bourse et visa",
         "Aucun pouvoir sur les jurys ni sur le consulat français.",
         "Mêmes chances officielles — sans perdre 500 000+ FCFA."],
    ]
    story.append(make_styled_table(
        ["Étape", "Ce que fait une agence payante", "Ce que TU fais toi-même"],
        comp_rows,
        [110, 196, CONTENT_W - 306],
        font_size=8.0,
        pad_v=4.4
    ))
    story.append(Spacer(1, 5))

    story.append(Paragraph("Tes 3 vrais avantages quand tu postules toi-même", S["h2"]))
    story.append(bullet("<b>Tu maîtrises ton projet sur le bout des doigts :</b> lors de l'entretien Campus France, les conseillers repèrent en deux minutes un dossier monté par un tiers. Quand tu as choisi toi-même tes formations, tu connais les matières et tu inspires confiance.", "01"))
    story.append(bullet("<b>Tu protèges ton budget pour l'essentiel :</b> les vrais coûts se limitent aux frais officiels (test de langue si requis, frais Campus France, légalisations, visa si non exonéré). Tout le reste doit servir à ton installation, pas à un intermédiaire.", "02"))
    story.append(bullet("<b>Tu évites les erreurs catastrophiques :</b> doublons de comptes Études en France, fausses attestations d'hébergement ou relevés « arrangés » — les pratiques douteuses de certaines agences provoquent des refus de visa immédiats.", "03"))

    story.append(Spacer(1, 4))
    story.append(make_callout(
        "À retenir avant de continuer",
        [
            "<i>« Obtenir une bourse française n'est pas une question de piston : c'est une question de méthode, d'anticipation et de cohérence. Si tu sais lire un email, remplir un formulaire en ligne et raconter ton parcours avec sincérité, tu es 100 % capable de réussir seul(e). »</i>"
        ],
        bg=IVORY, accent=GOLD, title_color=NAVY, pad_v=7, space_after=0
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4 : PARTIE 02 — LES 7 ERREURS FATALES
    # =========================================================================
    story.append(SectionHeader(
        "02", "Erreurs à éviter",
        "Les 7 erreurs fatales qui éliminent 80 % des candidats",
        "Avant même d'envoyer une seule candidature, assure-toi d'éviter ces pièges classiques qui font échouer même d'excellents étudiants."
    ))

    erreurs = [
        ("1. Confier ses identifiants (email et compte Campus France) à quelqu'un d'autre",
         "Certaines agences créent le dossier avec leur propre adresse email pour te garder dépendant(e) et réclamer de l'argent à chaque étape. <b>Règle d'or :</b> ton adresse email professionnelle (prenom.nom@…) et ton mot de passe Études en France t'appartiennent exclusivement."),
        ("2. Commencer ses démarches 3 mois avant la rentrée",
         "Pour une rentrée en septembre, les grandes bourses ouvrent entre <b>octobre et janvier de l'année précédente</b> (9 à 12 mois avant le départ !). Commencer en mai, c'est arriver après la fermeture des bourses Eiffel, Paris-Saclay, Erasmus Mundus et Campus France."),
        ("3. Croire qu'on postule soi-même à la Bourse Eiffel sur Campus France",
         "C'est le piège n°1 ! Un étudiant <b>ne peut pas</b> déposer directement sa candidature Eiffel auprès de Campus France. Ce sont uniquement les <b>établissements français</b> qui présélectionnent leurs candidats (souvent dès novembre) puis soumettent le dossier début janvier."),
        ("4. Envoyer une lettre de motivation générique (ou copiée-collée depuis une IA)",
         "Les jurys lisent des centaines de lettres identiques commençant par <i>« C'est avec un immense intérêt… »</i>. Pire : plusieurs programmes (dont certaines bourses d'ambassades) éliminent les textes visiblement générés par IA sans personnalisation. L'IA peut t'aider à structurer, jamais à inventer ta vie."),
        ("5. Choisir des formations sans lien logique avec son parcours",
         "Postuler en Master Finance avec une Licence en Lettres Modernes sans justification solide déclenche un refus quasi automatique. Le jury cherche une <b>continuité académique</b> et un projet professionnel réaliste."),
        ("6. Ne viser qu'une seule bourse très sélective (et ignorer les bourses d'universités)",
         "Tout le monde connaît la Bourse Eiffel, mais peu d'étudiants connaissent les bourses internes d'excellence (Paris-Saclay, SMARTS-UP, TIGER, IdEx Grenoble, ENS, BGF Ambassade). Diversifier tes candidatures multiplie tes chances par 5."),
        ("7. Confondre admission universitaire, bourse et visa étudiant",
         "Être admis dans une université ne donne pas automatiquement une bourse, et une bourse partielle (ex. 5 000 €/an) ne suffit pas toujours à elle seule pour le justificatif de ressources du visa. Tu dois articuler les trois volets dès le départ."),
    ]

    for title, desc in erreurs:
        box = Table(
            [[Paragraph(f'<b>{title}</b><br/><font size="8.6" color="#2B3440">{desc}</font>',
                        ParagraphStyle("err", fontName="Roboto", fontSize=9.0, leading=12.8, textColor=BURGUNDY))]],
            colWidths=[CONTENT_W]
        )
        box.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), BURGUNDY_BG),
            ("LINEBEFORE", (0, 0), (0, -1), 3, BURGUNDY),
            ("TOPPADDING", (0, 0), (-1, -1), 5.5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5.5),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ]))
        story.append(KeepTogether([box, Spacer(1, 5)]))

    story.append(Spacer(1, 3))
    story.append(make_callout(
        "5 signaux d'alerte d'une arnaque ou fausse agence",
        [
            "• On te promet une <b>« bourse garantie à 100 % »</b> ou un <b>« visa garanti »</b> moyennant paiement.<br/>"
            "• On te demande de payer via Mobile Money sur un numéro personnel pour <i>« débloquer »</i> une bourse gratuite.<br/>"
            "• On te propose de <i>« fabriquer »</i> un relevé de notes, un relevé bancaire ou une attestation d'hébergement.<br/>"
            "• On refuse de te donner les liens officiels (.gouv.fr / .campusfrance.org) ou tes propres identifiants.<br/>"
            "• On crée une fausse urgence (<i>« paie avant minuit sinon ta place est perdue »</i>)."
        ],
        bg=IVORY, accent=NAVY, title_color=NAVY, pad_v=7.5, space_after=0
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 5 : PARTIE 03 (1/2) — CARTOGRAPHIER LES MEILLEURES BOURSES 2026-2027
    # =========================================================================
    story.append(SectionHeader(
        "03", "Étape 1 — Ciblage stratégique",
        "Cartographier les meilleures bourses françaises (2026–2027)",
        "Il n'existe pas UNE seule bourse pour la France, mais plus de 700 programmes. Voici comment repérer rapidement ceux faits pour ton profil."
    ))

    story.append(Paragraph("Le réflexe n°1 : maîtriser le catalogue officiel Campus Bourses", S["h2"]))
    story.append(Paragraph(
        "Avant de chercher sur les réseaux sociaux, rends-toi sur <b>campusbourses.campusfrance.org</b>. C'est l'annuaire officiel et 100 % gratuit de l'agence Campus France. Il centralise les financements du gouvernement français, des ambassades, des universités, des régions et des fondations. En 15 minutes, applique trois filtres : <b>1) Ta nationalité</b>, <b>2) Ton niveau visé (Licence, Master, Doctorat)</b>, <b>3) Ton domaine d'études</b>.",
        S["body"]
    ))

    story.append(Paragraph("Tableau comparatif des 10 bourses phares pour étudiants africains (2026–2027)", S["h2"]))

    bourses_rows = [
        ["France Excellence Eiffel",
         "Master (≤29 ans)<br/>Doctorat (≤35 ans)",
         "1 200 €/mois (Master)<br/>2 000 €/mois (Doct.) + vol, santé",
         "Via l'établissement français (interne nov. / dépôt janv.)"],
        ["BGF / France Excellence (Ambassades)",
         "Licence, Master, Doctorat (selon pays)",
         "Couverture partielle à totale + statut boursier",
         "Appels locaux SCAC & Campus France de ton pays"],
        ["Mastercard Foundation – Sciences Po",
         "Master (Politiques publ., Aff. int., Éco…)",
         "Prise en charge complète (scolarité + vie + suivi)",
         "Candidature directe Sciences Po (automne/hiver)"],
        ["Bourse Émile Boutmy – Sciences Po",
         "Bachelor & Master (hors UE)",
         "Exonération partielle à totale / jusqu'à 18 500 €/an",
         "À cocher directement dans le dossier Sciences Po"],
        ["Paris-Saclay International Master",
         "Master 1 & Master 2",
         "10 000 €/an + jusqu'à 900 € voyage/visa",
         "Présélection par le responsable de Master après admission"],
        ["Erasmus Mundus Joint Masters",
         "Master (mobilité dans 2+ pays d'Europe)",
         "Jusqu'à 1 400 €/mois + frais de scolarité couverts",
         "Portail de chaque consortium (octobre à janvier)"],
        ["ENS-PSL & ENS de Lyon (Ampère)",
         "L3 / Master (Sciences & Lettres)",
         "~1 000 €/mois + accès logement campus",
         "Concours/dossier direct ENS (hiver : nov.–janv.)"],
        ["SMARTS-UP – Univ. Paris Cité",
         "Master (excellence internationale)",
         "10 000 € pour l'année universitaire",
         "Candidature dédiée selon calendrier Paris Cité"],
        ["TIGER – Aix-Marseille Université",
         "Master (parcours labellisés)",
         "Jusqu'à 10 000 € + accompagnement logement",
         "Dépôt sur le portail AMU lors de la candidature Master"],
        ["IdEx / Graduate School – UGA Grenoble",
         "Master & Ingénieur",
         "5 500 € à 14 500 € (selon parcours 1 ou 2 ans)",
         "Sélection académique lors de la candidature UGA"],
    ]

    story.append(make_styled_table(
        ["Programme de bourse", "Niveau & Cible", "Financement indicatif", "Comment postuler"],
        bourses_rows,
        [118, 95, 137, CONTENT_W - 350],
        font_size=7.6,
        pad_v=4.8
    ))
    story.append(Spacer(1, 5))
    story.append(Paragraph(
        "<i>Note : Les montants et dates limites sont actualisés sur la base des campagnes 2026–2027 (Campus France & établissements). Vérifie toujours la page officielle du programme au moment de déposer ton dossier.</i>",
        S["caption"]
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 6 : PARTIE 03 (2/2) — STRATÉGIE PORTEFEUILLE & CALENDRIER 2026-2027
    # =========================================================================
    story.append(Paragraph("ÉTAPE 1 (SUITE) — STRATÉGIE & TIMING", S["kicker"]))
    story.append(Paragraph("La stratégie du « Portefeuille de 5 Candidatures »", S["h1"]))
    story.append(GoldRule(50, 2.2, GOLD, 8))

    story.append(Paragraph(
        "Ne mets jamais tous tes œufs dans le même panier. Les candidats qui décrochent un financement combinent intelligemment prestige et accessibilité. Construis dès cette semaine ton <b>portefeuille équilibré de 5 cibles</b> :",
        S["body"]
    ))

    port_rows = [
        ["1 Bourse Prestige", "Eiffel, Erasmus Mundus ou Mastercard Sciences Po", "Très sélective, financement intégral"],
        ["2 Bourses d'Université", "Paris-Saclay, TIGER (AMU), SMARTS-UP, IdEx UGA, ENS…", "Excellentes chances avec un bon dossier L3/M1"],
        ["1 Bourse Ambassade / Coopération", "BGF France Excellence (Ambassade de France / SCAC) ou AUF", "Adaptée aux priorités de ton pays d'origine"],
        ["1 Plan B malin (Exonération)", "Université publique française offrant l'exonération des frais différenciés", "Frais réduits au tarif national (~175 €–250 €/an)"],
    ]
    story.append(make_styled_table(
        ["Catégorie", "Exemples concrets", "Pourquoi l'inclure"],
        port_rows,
        [125, 200, CONTENT_W - 325],
        font_size=8.2
    ))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Calendrier maître 2026–2027 (pour une rentrée en septembre 2027)", S["h2"]))
    story.append(Paragraph(
        "Le secret des lauréats tient en un mot : <b>l'anticipation</b>. Voici la chronologie officielle à afficher au mur de ta chambre :",
        S["body"]
    ))

    cal_rows = [
        ["Sept. – Oct. 2026", "Préparation & Ouverture",
         "Ouverture de la plateforme <b>Études en France (1er octobre)</b>. Sélection de tes 5 bourses, préparation du CV, demande des lettres de recommandation et inscription au TCF/DELF si non dispensé(e)."],
        ["Novembre 2026", "Dates internes Eiffel & Grandes Écoles",
         "Envoi de ta demande de présélection <b>Bourse Eiffel</b> aux services des Relations Internationales des universités cibles (beaucoup clôturent mi-novembre à fin novembre !). Ouverture Erasmus Mundus & Sciences Po."],
        ["Décembre 2026", "Clôture DAP (Licence 1)",
         "<b>15 décembre 2026 : date limite nationale DAP</b> (Licence 1 et écoles d'architecture) sur Études en France. Poursuite des dépôts Hors-DAP (L2, L3, Master) selon le calendrier de ton pays."],
        ["Janvier 2027", "Dépôt Eiffel & Bourses d'excellence",
         "Dépôt des dossiers Eiffel par les établissements auprès de Campus France (<b>6 janvier 2027</b>). Clôture de nombreux programmes Erasmus Mundus, ENS et bourses d'universités."],
        ["Fév. – Mars 2027", "Entretiens & Bourses Ambassades",
         "Passage de l'<b>entretien pédagogique Campus France</b> (souvent jusqu'à mi-mars). Ouverture de plusieurs appels BGF des Ambassades de France et bourses de régions/fondations."],
        ["Avril – Mai 2027", "Résultats & Choix final",
         "Résultats <b>Bourse Eiffel (semaine du 12 avril 2027)</b>. Réponses des universités (au plus tard <b>30 avril</b> pour la DAP) et choix définitif de ta formation (<b>31 mai</b>)."],
        ["Juin – Août 2027", "Visa, Logement CROUS & Départ",
         "Validation finale Campus France, demande de visa étudiant sur <b>france-visas.gouv.fr</b> avec ton attestation de bourse, réservation logement CROUS et préparation du vol !"],
    ]
    story.append(make_styled_table(
        ["Période", "Cap clé", "Actions précises à mener"],
        cal_rows,
        [88, 118, CONTENT_W - 206],
        font_size=7.9
    ))
    story.append(Spacer(1, 8))

    story.append(make_callout(
        "Astuce qui fait la différence : vérifie le calendrier de TON Espace Campus France",
        [
            "Si les dates nationales DAP (1er octobre / 15 décembre / 30 avril / 31 mai) sont communes, les dates <b>Hors-DAP (L2, L3, Master)</b> et les dates d'entretien varient selon chaque pays (Bénin, Sénégal, Côte d'Ivoire, Togo, Cameroun, Mali, Burkina Faso, Gabon, etc.). Consulte toujours la page officielle <b>[tonpays].campusfrance.org</b>."
        ],
        bg=FOREST_BG, accent=FOREST, title_color=FOREST
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 7 : PARTIE 04 (1/2) — BÂTIR UN DOSSIER IRRÉSISTIBLE
    # =========================================================================
    story.append(SectionHeader(
        "04", "Étape 2 — Dossier gagnant",
        "Bâtir un dossier de candidature irrésistible",
        "Un dossier boursier ne gagne pas parce qu'il est épais : il gagne parce qu'il est propre, lisible, honnête et raconte une trajectoire évidente."
    ))

    story.append(Paragraph("1. Le kit complet de tes pièces maîtresses (à scanner en PDF nets)", S["h2"]))
    story.append(Paragraph(
        "Crée un dossier numérique ordonné avec des fichiers nommés proprement (exemple : <i>01_Releves_L1_L2_L3_NOM_Prenom.pdf</i>). Évite les photos floues prises au téléphone sur un lit : utilise une application de scan propre (Adobe Scan, CamScanner en mode document sans filigrane).",
        S["body"]
    ))

    pieces_left = [
        "<b>Identité :</b> Passeport en cours de validité (ou CNI au début, passeport obligatoire pour le visa).",
        "<b>Parcours scolaire & universitaire :</b> Baccalauréat + relevés de notes de toutes les années post-bac + attestations de réussite/diplômes.",
        "<b>Classement (atout bourse !) :</b> Demande une attestation de rang si tu es dans le top 10–20 % de ta promotion.",
    ]
    pieces_right = [
        "<b>CV académique (1 page max) :</b> Sobre, structuré, sans photo fantaisiste, mettant en avant tes résultats, stages et engagements.",
        "<b>2 Lettres de recommandation :</b> Signées sur papier à en-tête universitaire (avec email professionnel du professeur).",
        "<b>Langue :</b> TCF / DELF B2 / DALF C1 — ou justificatif officiel de dispense (vérifie les règles de ton pays francophone).",
    ]

    p_tbl = Table(
        [[
            [bullet(x, "✓", "#1B664C", use_sym_font=True) for x in pieces_left],
            [bullet(x, "✓", "#1B664C", use_sym_font=True) for x in pieces_right],
        ]],
        colWidths=[CONTENT_W / 2 - 4, CONTENT_W / 2 - 4]
    )
    p_tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, -1), IVORY),
        ("BOX", (0, 0), (-1, -1), 0.6, BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(KeepTogether([p_tbl, Spacer(1, 10)]))

    story.append(Paragraph("2. La méthode « C-P-I » pour une lettre de motivation qui convainc le jury", S["h2"]))
    story.append(Paragraph(
        "Un jury de bourse ne finance pas un rêve vague (<i>« j'aime la France »</i>) : il investit dans un <b>futur diplômé à fort impact</b>. Structure chaque lettre de motivation (1 page, 4 paragraphes) selon la formule <b>C-P-I</b> :",
        S["body"]
    ))

    arrow = sym_span("→", "#C59B43")
    cpi_rows = [
        [f"C — Cohérence<br/><font name='Roboto' color='#667085'>Parcours {arrow} Formation</font>",
         "Relie tes études passées et tes résultats à la formation visée. Cite <b>2 à 3 modules précis</b> du programme de l'université (prouve que tu as lu la maquette !)."],
        ["P — Projet Professionnel<br/><font name='Roboto' color='#667085'>Vision à 3–5 ans</font>",
         "Explique le métier précis que tu vises après le diplôme et le besoin concret auquel tu réponds dans ton pays ou sur le continent africain."],
        ["I — Impact & Singularité<br/><font name='Roboto' color='#667085'>Pourquoi TOI ?</font>",
         "Mets en avant une preuve concrète : mémoire, projet étudiant, stage, engagement associatif ou prix. Explique pourquoi la bourse est un levier décisif."],
    ]
    story.append(make_styled_table(
        ["Pilier C-P-I", "Ce que le jury veut lire absolument"],
        cpi_rows,
        [142, CONTENT_W - 142],
        font_size=8.3
    ))
    story.append(Spacer(1, 9))

    story.append(make_callout(
        "Comment obtenir 2 lettres de recommandation percutantes (sans courir après tes profs)",
        [
            "Sollicite tes enseignants <b>au moins 4 semaines avant la date limite</b>. Ne leur dis pas simplement <i>« écrivez-moi une lettre »</i> : envoie-leur un petit dossier clair contenant <b>(1)</b> ton CV, <b>(2)</b> le nom exact de la bourse et du Master visé, <b>(3)</b> tes notes dans leur cours et 2 souvenirs concrets de projets réalisés avec eux, et <b>(4)</b> la date limite. Plus tu leur facilites la tâche, plus la lettre sera précise et élogieuse !"
        ],
        bg=BLUE_TINT, accent=NAVY, title_color=NAVY
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 8 : PARTIE 04 (2/2) — MODÈLES PRÊTS À ADAPTER
    # =========================================================================
    story.append(Paragraph("ÉTAPE 2 (SUITE) — MODÈLES PRÊTS À UTILISER", S["kicker"]))
    story.append(Paragraph("Tes 2 scripts prêts à adapter dès aujourd'hui", S["h1"]))
    story.append(GoldRule(50, 2.2, GOLD, 8))

    story.append(Paragraph("Modèle A — Plan de lettre de motivation gagnante (4 paragraphes)", S["h2"]))

    letter_text = [
        "<b>[Paragraphe 1 — Accroche & Objectif clair]</b><br/>"
        "Actuellement étudiant(e) en [Licence 3 / Master 1] de [Ta filière] à [Ton université, Pays] avec une moyenne de [X/20] (classé(e) [rang si bon]), je soumets ma candidature au [Nom exact du Master] de [Université française] ainsi qu'à la bourse [Nom de la bourse].",
        "<b>[Paragraphe 2 — Cohérence & Pourquoi CE programme]</b><br/>"
        "Au cours de ma formation, j'ai développé des bases solides en [Compétence 1] et [Compétence 2], concrétisées par [mon mémoire / mon stage chez X sur le sujet Y]. Votre programme se distingue par ses enseignements en [Module précis 1] et [Module précis 2], dirigés par [laboratoire / équipe], qui répondent exactement aux compétences techniques qu'il me manque aujourd'hui.",
        "<b>[Paragraphe 3 — Projet professionnel & Impact]</b><br/>"
        "À l'issue de ce diplôme, mon ambition est d'exercer comme [Métier précis] afin de contribuer à [problématique concrète dans ton pays / en Afrique, ex. transition énergétique, santé publique, finance inclusive, transformation numérique]. Mon engagement au sein de [association / projet] m'a déjà appris à mener des initiatives collectives orientées résultats.",
        "<b>[Paragraphe 4 — Financement & Conclusion sobre]</b><br/>"
        "L'obtention de la bourse [Nom] me permettrait de me consacrer pleinement à l'excellence académique sans contrainte matérielle. Je reste à votre entière disposition pour tout entretien et vous prie d'agréer, Madame, Monsieur, l'expression de ma considération distinguée."
    ]
    story.append(make_callout("Trame à personnaliser (1 page max — 350 à 450 mots)", letter_text, bg=IVORY, accent=GOLD, title_color=NAVY))

    story.append(Paragraph("Modèle B — Email à envoyer à une université française (Bourse Eiffel / Excellence)", S["h2"]))
    story.append(Paragraph(
        "Rappel crucial : pour la <b>Bourse Eiffel</b> et plusieurs bourses internes, c'est l'université qui te présélectionne. Envoie cet email dès <b>octobre–novembre</b> au responsable du Master et au service des Relations Internationales :",
        S["body"]
    ))

    email_text = [
        "<b>Objet :</b> Candidature Bourse France Excellence Eiffel 2027 – [Nom du Master] – [Ton NOM Prénom]",
        "Madame, Monsieur,<br/><br/>"
        "Titulaire (ou en cours d'obtention) d'une [Licence / Master 1] en [Discipline] à [Université, Pays] avec une moyenne de [X/20] (mention [Très Bien / Bien]), je souhaite intégrer le <b>[Nom exact du Master]</b> de votre établissement à la rentrée de septembre 2027.<br/><br/>"
        "Particulièrement intéressé(e) par [mentionner 1 spécificité du Master], je souhaiterais solliciter le soutien de votre établissement pour présenter ma candidature au programme <b>France Excellence Eiffel</b> (ou à votre bourse d'excellence interne).<br/><br/>"
        "Pourriez-vous m'indiquer la procédure et la date limite interne pour soumettre mon dossier de présélection ? Vous trouverez ci-joint mon CV ainsi que mes derniers relevés de notes pour une première appréciation de mon profil.<br/><br/>"
        "En vous remerciant vivement pour votre attention, je vous prie d'agréer, Madame, Monsieur, mes respectueuses salutations.<br/>"
        "<b>[Prénom NOM]</b> — [Téléphone avec indicatif] — [Email pro] — [Pays]"
    ]
    story.append(make_callout("Email prêt à copier-adapter (joindre CV + relevés en 1 PDF)", email_text, bg=BLUE_TINT, accent=NAVY, title_color=NAVY))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 9 : PARTIE 05 (1/2) — CAMPUS FRANCE & ENTRETIEN PÉDAGOGIQUE
    # =========================================================================
    story.append(SectionHeader(
        "05", "Étape 3 — Procédure officielle",
        "Réussir Campus France (« Études en France ») et l'entretien",
        "La procédure Études en France concerne la majorité des pays d'Afrique francophone. Voici comment la piloter proprement du premier clic jusqu'à l'accord préalable."
    ))

    story.append(Paragraph("1. Les 5 étapes sur la plateforme Études en France", S["h2"]))
    story.append(bullet("<b>Étape A — Crée un compte unique :</b> rends-toi sur <b>pastel.diplomatie.gouv.fr</b> (ou via le site Campus France de ton pays). Si tu as déjà eu un compte lors d'une campagne précédente, réutilise-le : <b>ne crée jamais de doublon</b>.", "01"))
    story.append(bullet("<b>Étape B — Choisis la bonne voie :</b> <b>DAP</b> (Demande d'Admission Préalable) pour la Licence 1 et les écoles d'architecture (jusqu'à <b>3 vœux</b>, clôture le 15 décembre) ; <b>Hors-DAP</b> pour la Licence 2, Licence 3, Master et BUT (jusqu'à <b>7 vœux</b>).", "02"))
    story.append(bullet("<b>Étape C — Remplis ton panier de formations avec stratégie :</b> panache tes vœux entre universités de grandes métropoles (très demandées) et excellentes universités de villes moyennes (Rennes, Nantes, Grenoble, Strasbourg, Bordeaux, Toulouse, Lille, Montpellier…), où les taux d'admission et le coût de la vie sont souvent plus favorables.", "03"))
    story.append(bullet("<b>Étape D — Soumets et paie les frais officiels :</b> les frais de procédure Campus France se paient <b>exclusivement</b> via la banque ou le guichet officiel indiqué par ton Espace Campus France (jamais sur le compte privé d'une agence).", "04"))
    story.append(bullet("<b>Étape E — Passe l'entretien pédagogique :</b> une fois ton dossier vérifié, tu reçois une convocation pour un échange de 15 à 25 minutes avec un conseiller Campus France.", "05"))

    story.append(Paragraph("2. Les 8 questions classiques de l'entretien Campus France (et comment briller)", S["h2"]))

    q_rows = [
        ["1. Présentez-vous et expliquez votre parcours.",
         "Réponse structurée en 90 secondes : études actuelles, point fort académique, stage/projet marquant et objectif du jour."],
        ["2. Pourquoi choisir la France plutôt qu'un autre pays ?",
         "Parle de qualité académique, de reconnaissance internationale du diplôme, de francophonie et d'un point précis de ta discipline en France."],
        ["3. Pourquoi ces universités et connaissez-vous le contenu des cours ?",
         "Cite 2 matières exactes de chaque formation de ton panier et le lien avec ton projet. Ne dis jamais « j'ai choisi au hasard »."],
        ["4. Quel est votre projet professionnel après le diplôme ?",
         "Donne un poste précis, un secteur et un horizon (3 à 5 ans) en montrant l'utilité de ta formation pour ton pays ou l'Afrique."],
        ["5. Comment comptez-vous financer vos études ?",
         "Explique calmement : bourses auxquelles tu postules (noms précis) + plan B réaliste (soutien familial / garant) si bourse en attente."],
        ["6. Que ferez-vous si vous n'êtes pas admis(e) cette année ?",
         "Montre ta maturité : poursuivre ton cursus localement, renforcer ton expérience (stage/langues) et recandidater avec un dossier encore plus fort."],
        ["7. Pourquoi avez-vous une mauvaise note / une année blanche ?",
         "Ne mens jamais. Assume brièvement, explique la cause factuelle et montre comment tu as rebondi ensuite."],
        ["8. Où comptez-vous vous loger en France ?",
         "Cite les démarches réelles : demande de résidence CROUS (prioritaire pour les boursiers du gouvernement français), résidences étudiantes ou garant."],
    ]
    story.append(make_styled_table(
        ["Question fréquente du conseiller", "Ta stratégie de réponse gagnante"],
        q_rows,
        [185, CONTENT_W - 185],
        font_size=7.9
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 10 : PARTIE 05 (2/2) — DU SUCCÈS D'ADMISSION AU VISA ÉTUDIANT
    # =========================================================================
    story.append(Paragraph("ÉTAPE 3 (SUITE) — ADMISSION, BOURSE & VISA", S["kicker"]))
    story.append(Paragraph("Finaliser ton admission, activer ta bourse et obtenir ton visa", S["h1"]))
    story.append(GoldRule(50, 2.2, GOLD, 8))

    story.append(Paragraph(
        "Félicitations : tu as reçu une ou plusieurs acceptations universitaires et/ou une lettre d'attribution de bourse ! Il reste la dernière ligne droite : transformer ton admission en <b>visa long séjour valant titre de séjour (VLS-TS Étudiant)</b> sans aucune erreur de dernière minute.",
        S["body"]
    ))

    story.append(Paragraph("1. Ce que change ton statut de boursier pour le visa", S["h2"]))

    visa_rows = [
        ["Bourse complète<br/><font name='Roboto' color='#667085'>Eiffel, BGF, Erasmus Mundus, Mastercard…</font>",
         "<b>Énorme avantage :</b> ton attestation officielle de bourse sert directement de justificatif de ressources financières (seuil légal couvert). Pour les boursiers du gouvernement français (BGF/Eiffel), tu bénéficies aussi de l'exonération des frais d'inscription nationaux dans les établissements publics, de la priorité logement CROUS et souvent de l'exonération des frais de visa !"],
        ["Bourse partielle<br/><font name='Roboto' color='#667085'>Ex. 5 000 € à 10 000 €/an d'une université</font>",
         "L'attestation de bourse est comptabilisée dans tes ressources, mais si son montant mensuel est inférieur au seuil exigé par le consulat, tu dois simplement fournir un <b>complément de ressources</b> (attestation de virement irrévocable / AVI bancaire officielle ou prise en charge d'un garant solvable)."],
        ["Admission sans bourse<br/><font name='Roboto' color='#667085'>Plan B exonération</font>",
         "Si tu pars via ton plan B, vérifie les politiques d'exonération partielle/totale de ton université et prépare le justificatif de ressources exigé sur france-visas.gouv.fr (toujours vérifier le montant actualisé au moment du dépôt)."],
    ]
    story.append(make_styled_table(
        ["Ta situation financière", "Impact concret sur le dossier Visa"],
        visa_rows,
        [145, CONTENT_W - 145],
        font_size=8.2
    ))
    story.append(Spacer(1, 10))

    story.append(Paragraph("2. La procédure officielle France-Visas en 4 temps", S["h2"]))
    story.append(bullet("<b>Valide ton choix définitif sur Études en France :</b> sélectionne ton université finale dans les délais (ex. avant le 31 mai pour la DAP) afin d'obtenir ton <b>attestation d'accord préalable d'inscription (EEF)</b>.", "01"))
    story.append(bullet("<b>Crée ton dossier sur france-visas.gouv.fr :</b> remplis le formulaire en ligne de visa long séjour étudiant (VLS-TS) en vérifiant que chaque nom, numéro de passeport et date correspond au millimètre près à tes justificatifs.", "02"))
    story.append(bullet("<b>Réunis les 5 piliers du dossier visa :</b> passeport valide, attestation d'accord préalable Campus France + lettre d'admission, attestation officielle de bourse (et complément si bourse partielle), justificatif d'hébergement pour les 3 premiers mois (CROUS, résidence, attestation d'accueil ou réservation hôtelière conforme), et photos d'identité aux normes.", "03"))
    story.append(bullet("<b>Prends rendez-vous au centre officiel (TLScontact / VFS Global / Consulat) :</b> ne paie jamais un « rabatteur » de rendez-vous. Dépose ton dossier complet dès juin–juillet pour éviter l'engorgement d'août !", "04"))

    story.append(Spacer(1, 6))
    story.append(make_callout(
        "Rappel vital : ne touche JAMAIS aux faux documents",
        [
            "Les consulats français vérifient systématiquement les attestations bancaires, les réservations d'hébergement et les attestations de bourse. Un seul document falsifié entraîne un refus immédiat pour fraude et compromet tous tes futurs projets en espace Schengen. <b>La transparence totale est ta meilleure protection.</b>"
        ],
        bg=BURGUNDY_BG, accent=BURGUNDY, title_color=BURGUNDY
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 11 : BOÎTE À OUTILS — PORTAILS OFFICIELS & TABLEAU DE SUIVI
    # =========================================================================
    story.append(SectionHeader(
        "06", "Boîte à outils",
        "Portails 100 % officiels & tableau de suivi de tes candidatures",
        "Garde cette page en favori : chaque lien ci-dessous est gratuit, officiel et vérifié."
    ))

    story.append(Paragraph("Annuaire des 8 portails indispensables (0 FCFA d'accès)", S["h2"]))

    portals_rows = [
        ["Campus France (Portail général)", "campusfrance.org", "Guides études, fiches pays, règlement Bourse Eiffel et actualités officielles."],
        ["Campus Bourses (Annuaire)", "campusbourses.campusfrance.org", "Moteur de recherche officiel de 700+ bourses filtrables par pays, niveau et filière."],
        ["Plateforme Études en France", "pastel.diplomatie.gouv.fr", "Dépôt officiel des vœux universitaires (DAP / Hors-DAP) et suivi Campus France."],
        ["Espace Campus France local", "[tonpays].campusfrance.org", "Calendrier exact de ton pays (ex. benin, senegal, cotedivoire, togo, cameroun…)."],
        ["France-Visas", "france-visas.gouv.fr", "Portail officiel unique pour préparer et déposer ta demande de visa étudiant."],
        ["Erasmus Mundus (UE)", "erasmus-plus.ec.europa.eu", "Catalogue officiel des Masters conjoints européens entièrement financés."],
        ["CROUS (Logement étudiant)", "messervices.etudiant.gouv.fr", "Portail officiel des résidences universitaires et services de vie étudiante."],
        ["Ambassade de France / SCAC", "Site de l'Ambassade de ton pays", "Appels à candidatures annuels des Bourses du Gouvernement Français (BGF)."],
    ]
    story.append(make_styled_table(
        ["Plateforme", "Adresse officielle", "À quoi elle sert"],
        portals_rows,
        [130, 145, CONTENT_W - 275],
        font_size=7.9
    ))

    story.append(Spacer(1, 10))
    story.append(Paragraph("Mon tableau de suivi des candidatures (à imprimer ou recopier)", S["h2"]))
    story.append(Paragraph(
        "Note ici tes 5 bourses et formations cibles pour ne rater aucune date limite :",
        S["body_small"]
    ))

    box_sym = sym_span("☐", "#132238", size=9)
    pieces_chk = f"{box_sym} CV &nbsp;&nbsp;{box_sym} LM &nbsp;&nbsp;{box_sym} Reco"
    tracker_headers = ["#", "Bourse / Université ciblée", "Date limite", "Pièces prêtes", "Statut (Envoyé / Résultat)"]
    tracker_rows = [
        ["1", "Ex. Eiffel – Master … (Univ. …)", "… / … / 2026", pieces_chk, ""],
        ["2", "", "", pieces_chk, ""],
        ["3", "", "", pieces_chk, ""],
        ["4", "", "", pieces_chk, ""],
        ["5", "", "", pieces_chk, ""],
    ]
    t_track = make_styled_table(
        tracker_headers, tracker_rows,
        [22, 166, 74, 122, CONTENT_W - 384],
        font_size=7.9
    )
    t_track.setStyle(TableStyle([
        ("TOPPADDING", (0, 1), (-1, -1), 11),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 11),
    ]))
    story.append(t_track)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 12 : CONCLUSION — PLAN D'ACTION 30 JOURS & CHECKLIST FINALE
    # =========================================================================
    story.append(SectionHeader(
        "07", "Conclusion & Passage à l'action",
        "Ton plan d'action sur 30 jours pour décrocher ta bourse",
        "La différence entre ceux qui rêvent d'étudier en France et ceux qui montent dans l'avion, c'est un premier pas concret fait cette semaine."
    ))

    plan_rows = [
        ["Semaine 1<br/><font name='Roboto' color='#C59B43'>Clarification & Ciblage</font>",
         "Crée ton dossier numérique <i>« Bourse France 2027 »</i> et ton email pro. Passe 1 heure sur <b>Campus Bourses</b> et choisis ton portefeuille de <b>5 bourses + 5 à 7 formations</b>. Note toutes les dates limites."],
        ["Semaine 2<br/><font name='Roboto' color='#C59B43'>Pièces & Contacts</font>",
         "Scanne proprement tous tes relevés et diplômes. Sollicite <b>2 professeurs</b> pour tes lettres de recommandation. Envoie tes emails de prise de contact aux universités (présélection Eiffel / bourses internes)."],
        ["Semaine 3<br/><font name='Roboto' color='#C59B43'>Rédaction & Dépôt</font>",
         "Rédige ton CV académique (1 page) et personnalise tes lettres de motivation selon la <b>méthode C-P-I</b>. Crée et remplis ton dossier sur <b>Études en France</b>. Fais relire chaque document par une personne attentive."],
        ["Semaine 4<br/><font name='Roboto' color='#C59B43'>Soumission & Oral</font>",
         "Soumets tes dossiers <b>au moins 5 jours avant chaque date limite</b> (pour éviter tout bug de serveur). Prépare tes réponses aux 8 questions d'entretien Campus France à voix haute, chronomètre en main."],
    ]
    story.append(make_styled_table(
        ["Semaine", "Tes actions concrètes"],
        plan_rows,
        [118, CONTENT_W - 118],
        font_size=8.3
    ))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Checklist finale avant de cliquer sur « Soumettre »", S["h2"]))

    checks_l = [
        "Mon adresse email et mon compte Études en France m'appartiennent à 100 %.",
        "Tous mes fichiers PDF sont nets, droits et nommés clairement.",
        "Chaque lettre cite le nom exact de l'université et 2 modules précis.",
        "J'ai vérifié l'orthographe et fait relire mon dossier par un proche.",
    ]
    checks_r = [
        "J'ai ciblé au moins 3 à 5 bourses différentes (pas seulement Eiffel).",
        "Mes 2 lettres de recommandation sont signées et datées.",
        "J'ai noté toutes les dates limites (internes + Campus France).",
        "Je n'ai payé aucun intermédiaire ni fourni aucun faux document.",
    ]

    chk_tbl = Table(
        [[
            [checkbox_item(x) for x in checks_l],
            [checkbox_item(x) for x in checks_r],
        ]],
        colWidths=[CONTENT_W / 2 - 4, CONTENT_W / 2 - 4]
    )
    chk_tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, -1), FOREST_BG),
        ("BOX", (0, 0), (-1, -1), 0.7, FOREST),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(KeepTogether([chk_tbl, Spacer(1, 12)]))

    final_box = Table(
        [[
            Paragraph(
                '<font color="#C59B43"><b>TON AVENIR NE SE SOUS-TRAITE PAS</b></font><br/><br/>'
                '<font color="#FFFFFF">Tu as désormais entre les mains la même information que les meilleures agences — avec quelque chose qu\'aucune agence n\'aura jamais : <b>ta détermination, ton histoire et ta voix</b>. Commence dès aujourd\'hui par la Semaine 1. Dans quelques mois, tu regarderas en arrière avec une immense fierté en disant : <i>« Je l\'ai décrochée moi-même. »</i></font><br/><br/>'
                '<font color="#D2DCE8" size="8.4">Mon engagement — Je démarre le : ____ / ____ / 202___ &nbsp;|&nbsp; Ma bourse prioritaire : _____________________</font>',
                ParagraphStyle("fin", fontName="Roboto", fontSize=9.4, leading=14.2, textColor=PAPER)
            )
        ]],
        colWidths=[CONTENT_W]
    )
    final_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LINEABOVE", (0, 0), (-1, 0), 3, GOLD),
        ("TOPPADDING", (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
    ]))
    story.append(KeepTogether([final_box]))

    return story


def build_pdf():
    doc = BaseDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        title="Guide Ultime : Décroche ta Bourse Française Toi-Même, Sans Payer une Agence",
        author="Guide Pratique — Édition 2026-2027",
        subject="Méthode autonome pour obtenir une bourse d'études en France depuis l'Afrique francophone",
    )

    cover_frame = Frame(0, 0, PAGE_W, PAGE_H, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="cover")
    interior_frame = Frame(
        MARGIN_X, MARGIN_BOTTOM,
        CONTENT_W, PAGE_H - MARGIN_TOP - MARGIN_BOTTOM,
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        id="interior"
    )

    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=draw_cover_page),
        PageTemplate(id="interior", frames=[interior_frame], onPage=draw_interior_page),
    ])

    story = build_story()
    doc.build(story)
    print(f"PDF généré avec succès : {OUTPUT_PDF}")


if __name__ == "__main__":
    build_pdf()
