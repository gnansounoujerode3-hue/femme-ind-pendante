"""Pagination automatique : découpe le HTML en blocs de premier niveau,
puis remplit des pages entières sans jamais couper un bloc."""
import re

import pymupdf

VOID = {"br", "hr", "img", "col", "meta", "link", "input"}


def split_blocks(html):
    """Retourne la liste des blocs de premier niveau (chaînes HTML)."""
    blocks = []
    depth = 0
    start = None
    for m in re.finditer(r"<(/?)([a-zA-Z0-9]+)([^>]*?)(/?)>", html):
        tag = m.group(2).lower()
        closing = m.group(1) == "/"
        selfclose = m.group(4) == "/" or tag in VOID
        if not closing and not selfclose:
            if depth == 0:
                start = m.start()
            depth += 1
        elif closing:
            depth -= 1
            if depth == 0 and start is not None:
                blocks.append(html[start:m.end()])
                start = None
    return blocks


def measure(html, css, width, archive):
    st = pymupdf.Story(html=html, user_css=css, archive=archive)
    res = st.fit_height(width, height_min=1, height_max=8000)
    return res.rect.height


def paginate(html, css, width, height, archive, gap=0.0):
    blocks = split_blocks(html)
    heights = []
    for b in blocks:
        try:
            heights.append(measure(b, css, width, archive))
        except Exception:
            heights.append(height)  # bloc non mesurable : page seule
    pages, cur, curh = [], [], 0.0
    for b, hgt in zip(blocks, heights):
        add = hgt + (gap if cur else 0)
        if cur and curh + add > height:
            pages.append(cur)
            cur, curh = [b], hgt
        else:
            cur.append(b)
            curh += add
    if cur:
        pages.append(cur)
    return ["\n".join(p) for p in pages]


def is_short(html, css, width, height, archive, ratio=0.72):
    """Vrai si le contenu ne remplit pas la page (évite les pages orphelines)."""
    return measure(html, css, width, archive) < height * ratio
