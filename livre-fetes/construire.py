"""Construit le guide des fêtes à partir de livre.md. Nécessite PyMuPDF."""
from pathlib import Path
import html
import re
import sys
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'ebook'))
import build as base
import paginate

SOURCE = Path(__file__).with_name('livre.md')
OUTPUT = ROOT / 'MES-FETES-MON-BUDGET-MA-LIBERTE.pdf'


def render(raw, compact=False):
    css = base.CSS + ("\nbody { font-size: 8.6pt; line-height: 1.5; } p { margin-bottom: 5pt; }" if compact else "")
    pages = paginate.paginate(raw, css, base.AREA.width, base.AREA.height, base.FONTS)
    doc = pymupdf.open()
    for page_html in pages:
        tmp = base.story_pages(page_html, css)
        page = doc.new_page(width=base.PAGE.width, height=base.PAGE.height)
        page.draw_rect(page.rect, color=None, fill=base.CREAM)
        page.show_pdf_page(page.rect, tmp, 0)
        tmp.close()
    return doc


def cover():
    doc = pymupdf.open()
    p = doc.new_page(width=base.PAGE.width, height=base.PAGE.height)
    w, h = p.rect.width, p.rect.height
    p.insert_image(p.rect, filename=str(ROOT / 'ebook/art/fetes-autonomie.jpg'), keep_proportion=False)
    p.draw_rect((0, 0, w, 218), color=None, fill=(0.04, 0.09, 0.10), fill_opacity=.77)
    p.draw_rect((0, h-105, w, h), color=None, fill=(0.04, 0.09, 0.10), fill_opacity=.83)
    p.insert_font(fontname='titlefont', fontfile=str(ROOT/'ebook/ttf/playfair-display-latin-700-normal.ttf'))
    p.insert_font(fontname='textfont', fontfile=str(ROOT/'ebook/ttf/inter-latin-600-normal.ttf'))
    for y, line in ((65,'Mes fêtes,'), (103,'mon budget,'), (141,'ma liberté')):
        p.insert_text((30,y), line, fontname='titlefont', fontsize=28, color=(1,.96,.9))
    p.insert_text((31,177), 'PRÉPARER LES FÊTES SANS DÉPENDRE', fontname='textfont', fontsize=8, color=(1,.82,.65))
    p.insert_text((31,191), "FINANCIÈREMENT D’UN HOMME", fontname='textfont', fontsize=8, color=(1,.82,.65))
    p.insert_text((31,h-57), 'UN GUIDE PRATIQUE POUR CHOISIR', fontname='textfont', fontsize=7.3, color=(1,1,1))
    p.insert_text((31,h-42), 'ET CÉLÉBRER À TA MESURE', fontname='textfont', fontsize=7.3, color=(1,1,1))
    return doc


def main():
    source = SOURCE.read_text(encoding='utf-8')
    chunks = re.split(r'(?m)^# ', source)[2:]
    sections = []
    for chunk in chunks:
        title, body = chunk.split('\n', 1)
        blocks = [p.strip() for p in re.split(r'\n\s*\n', body) if p.strip()]
        content = '<div class="ch-open"><div class="ch-title">' + html.escape(title) + '</div><div class="rule"></div></div>'
        content += ''.join('<p>' + html.escape(p) + '</p>' for p in blocks)
        sections.append((title, render(content, compact=title.startswith("5."))))
    # The introduction belongs to the initial title block in the Markdown.
    intro_text = source.split('## Introduction : reprendre la main, sans se juger\n',1)[1].split('\n# 1.',1)[0]
    intro = '<div class="ch-open"><div class="ch-title">Introduction : reprendre la main, sans se juger</div><div class="rule"></div></div>'
    intro += ''.join('<p>'+html.escape(x.strip())+'</p>' for x in re.split(r'\n\s*\n',intro_text) if x.strip())
    sections.insert(0, ('Introduction', render(intro)))
    # Reserve a single contents page and calculate physical PDF page numbers.
    cursor = 3
    starts = []
    for title, frag in sections:
        starts.append(cursor)
        cursor += len(frag)
    toc_html = '<h1>Sommaire</h1><p>Un parcours pratique pour préparer les fêtes et protéger ton budget.</p><table class="toc">'
    for (title, _), number in zip(sections, starts):
        toc_html += '<tr><td>'+html.escape(title)+'</td><td class="toc-pg">'+str(number)+'</td></tr>'
    toc_html += '</table>'
    toc = render(toc_html)
    if len(toc) != 1:
        raise RuntimeError('Le sommaire ne tient plus sur une page.')
    doc = cover()
    doc.insert_pdf(toc)
    for _, frag in sections: doc.insert_pdf(frag)
    for i in range(1, len(doc)):
        page = doc[i]; w,h=page.rect.width,page.rect.height
        page.draw_line((42,h-22),(w-42,h-22),color=(.85,.80,.74),width=.5)
        page.insert_text((42,h-11.5),'MES FÊTES, MON BUDGET, MA LIBERTÉ',fontsize=5.2,fontname='hebo',color=(.60,.53,.47))
        page.insert_text((w-55,h-11),str(i+1),fontsize=8,fontname='hebo',color=base.NAVY)
    toc_page = doc[1]
    for (title, _), number in zip(sections, starts):
        hits = toc_page.search_for(title)
        if len(hits) != 1: raise RuntimeError('Entrée introuvable ou ambiguë : '+title)
        toc_page.insert_link({'kind':pymupdf.LINK_GOTO, 'from':hits[0], 'page':number-1, 'to':pymupdf.Point(42,46)})
    doc.set_toc([[1,title,number] for (title,_),number in zip(sections,starts)])
    doc.set_metadata({'title':'Mes fêtes, mon budget, ma liberté', 'subject':'Guide pratique pour préparer les fêtes et renforcer son autonomie financière'})
    doc.save(str(OUTPUT), garbage=4, deflate=True)
    print(f'{OUTPUT.name} : {len(doc)} pages, {len(sections)} liens')

if __name__ == '__main__': main()
