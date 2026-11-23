"""Ajoute le titre sur les visuels de couverture et produit une page A4 par style.

Usage (depuis la racine du dépôt) :
    /tmp/pdfenv/bin/python guide-bourse-france/couverture/build_covers.py
"""
import os
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
A4 = pymupdf.paper_rect("a4")  # 595 x 842 pt
NAVY = (31 / 255, 60 / 255, 110 / 255)
GOLD = (201 / 255, 162 / 255, 39 / 255)
WHITE = (1, 1, 1)


def cover_clip(path):
    """Zone de l'image à garder pour remplir le format A4 sans l'étirer (centrée)."""
    img = pymupdf.open(path)
    img = pymupdf.open("pdf", img.convert_to_pdf())  # une image convertie en PDF, pour le recadrage
    r = img[0].rect
    target = A4.width / A4.height
    w, h = r.width, r.height
    if w / h > target:
        nw = h * target
        x0 = (w - nw) / 2
        clip = pymupdf.Rect(x0, 0, x0 + nw, h)
    else:
        nh = w / target
        y0 = (h - nh) / 2
        clip = pymupdf.Rect(0, y0, w, y0 + nh)
    return img, clip


def make(path_in, path_out, style):
    doc = pymupdf.open()
    page = doc.new_page(width=A4.width, height=A4.height)
    img, clip = cover_clip(path_in)
    page.show_pdf_page(A4, img, 0, clip=clip)
    if style == "photo":
        # Bandeau sombre en bas pour la lisibilité du titre
        page.draw_rect(pymupdf.Rect(0, 470, A4.width, A4.height), color=None,
                       fill=NAVY, fill_opacity=0.82)
        title_color, sub_color = WHITE, GOLD
        top = 520
    else:
        # Style minimaliste : titre en bas sur fond clair
        page.draw_rect(pymupdf.Rect(0, 0, A4.width, A4.height), color=None,
                       fill=(0.98, 0.97, 0.95), fill_opacity=0.0)
        title_color, sub_color = NAVY, GOLD
        top = 90
    page.insert_textbox(pymupdf.Rect(48, top, A4.width - 48, top + 160),
                        "Décroche ta bourse française",
                        fontname="hebo", fontsize=34, color=title_color, align=0)
    page.insert_textbox(pymupdf.Rect(48, top + 120, A4.width - 48, top + 180),
                        "toi-même, sans payer une agence",
                        fontname="helv", fontsize=18, color=sub_color, align=0)
    page.insert_textbox(pymupdf.Rect(48, A4.height - 110, A4.width - 48, A4.height - 60),
                        "Guide pratique pour les candidats béninois\nCampus France Bénin · bourse Eiffel · dossier · visa",
                        fontname="helv", fontsize=10, color=title_color, align=0)
    doc.save(path_out)
    pix = page.get_pixmap(dpi=90)
    pix.save(path_out.replace(".pdf", ".png"))
    doc.close()


make(os.path.join(HERE, "style-1-photo.jpg"), os.path.join(HERE, "cover-photo.pdf"), "photo")
make(os.path.join(HERE, "style-4-minimal.jpg"), os.path.join(HERE, "cover-minimal.pdf"), "minimal")
print("ok")
