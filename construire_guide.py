"""Génère le guide éditable et son PDF. Dépendance : reportlab."""
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parent
STEM = 'LE-GUIDE-ULTIME-100-RECETTES-BENINOISES-AFRICAINES'

def load_recipes():
    result, chapter = [], ''
    for line in (ROOT / 'recettes-africaines-source.txt').read_text().splitlines():
        if not line.strip():
            continue
        if line.startswith('# '):
            chapter = line[2:].split('|', 1)[1].strip()
            continue
        parts = line.split('|')
        assert len(parts) == 9, (parts[0], len(parts))
        number, title, origin, portions, duration, wait, ingredients, steps, tip = parts
        result.append(dict(number=int(number), title=title, origin=origin, portions=portions,
                           duration=duration, wait=wait, ingredients=ingredients,
                           steps=steps.split(' / '), tip=tip, chapter=chapter))
    assert [r['number'] for r in result] == list(range(1, 101))
    assert all(len(r['steps']) == 4 for r in result)
    return result

def make_markdown(recipes):
    sections = [(ROOT / 'guide-introduction.md').read_text(), '\n## Index des 100 recettes\n']
    for r in recipes:
        sections.append(f"- [{r['number']}. {r['title']}](#recette-{r['number']})")
    chapter = ''
    for r in recipes:
        if chapter != r['chapter']:
            chapter = r['chapter']
            sections.append(f'\n---\n\n## {chapter}\n')
        sections.append(f"\n<a id=\"recette-{r['number']}\"></a>\n\n### {r['number']}. {r['title']}\n\n"
                        f"*{r['origin']}*\n\n**Quantité :** {r['portions']}  \n"
                        f"**Préparation et cuisson :** {r['duration']}  \n**Attente à prévoir :** {r['wait']}\n\n"
                        f"**Ingrédients**\n\n{r['ingredients']}\n\n**Pas à pas**\n")
        sections.extend(f'{i}. {step}' for i, step in enumerate(r['steps'], 1))
        sections.append(f"\n**Conseil débutant :** {r['tip']}\n")
    sections.append('\n---\n\n' + (ROOT / 'guide-annexes.md').read_text())
    (ROOT / f'{STEM}.md').write_text('\n'.join(sections))

def make_pdf(recipes):
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, HRFlowable
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.colors import HexColor, white
    from reportlab.lib.enums import TA_CENTER
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.pagesizes import A4
    fontdir = Path('/usr/share/fonts/truetype/dejavu')
    pdfmetrics.registerFont(TTFont('Guide', str(fontdir / 'DejaVuSans.ttf')))
    pdfmetrics.registerFont(TTFont('GuideBold', str(fontdir / 'DejaVuSans-Bold.ttf')))
    pdfmetrics.registerFontFamily('Guide', normal='Guide', bold='GuideBold', italic='Guide', boldItalic='GuideBold')
    green, gold = HexColor('#174A3B'), HexColor('#B46F2B')
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='BodyGuide', fontName='Guide', fontSize=9, leading=13.4, spaceAfter=7, textColor=HexColor('#263B35')))
    styles.add(ParagraphStyle(name='ChapterGuide', parent=styles['BodyGuide'], fontName='GuideBold', fontSize=17, leading=22, textColor=green, spaceBefore=12, spaceAfter=14, keepWithNext=True))
    styles.add(ParagraphStyle(name='SubGuide', parent=styles['BodyGuide'], fontName='GuideBold', fontSize=11.5, leading=16, textColor=green, spaceBefore=9, spaceAfter=8, keepWithNext=True))
    styles.add(ParagraphStyle(name='RecipeGuide', parent=styles['SubGuide'], fontSize=13, leading=17))
    styles.add(ParagraphStyle(name='MetaGuide', parent=styles['BodyGuide'], fontSize=8, leading=11, textColor=gold))
    styles.add(ParagraphStyle(name='IndexGuide', parent=styles['BodyGuide'], fontSize=9, leading=13, spaceAfter=4))
    styles.add(ParagraphStyle(name='CoverGuide', fontName='GuideBold', fontSize=30, leading=39, textColor=green, alignment=TA_CENTER, spaceAfter=24))
    styles.add(ParagraphStyle(name='CoverSub', parent=styles['BodyGuide'], fontSize=14, leading=22, alignment=TA_CENTER))
    body = []
    def p(text, style='BodyGuide'):
        return Paragraph(text, styles[style])
    def inline(text):
        text = escape(text)
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
        return text
    def markdown(text):
        for line in text.splitlines():
            if not line.strip() or line == '---':
                continue
            if line.startswith('# '):
                continue
            if line.startswith('### '):
                body.append(p(inline(line[4:]), 'SubGuide'))
            elif line.startswith('## '):
                body.append(p(inline(line[3:]), 'ChapterGuide'))
            elif line.startswith('- '):
                body.append(p('• ' + inline(line[2:])))
            else:
                body.append(p(inline(line)))
    body += [Spacer(1, 90), p('LE GUIDE ULTIME', 'CoverSub'), Spacer(1, 15),
             p('100 RECETTES<br/>BÉNINOISES<br/>&amp; AFRICAINES', 'CoverGuide'),
             p('À préparer pour Noël<br/>et le 1er janvier', 'CoverSub'), Spacer(1, 30),
             HRFlowable(width='45%', thickness=2, color=gold, hAlign='CENTER'), Spacer(1, 26),
             p('ÉDITION DÉBUTANT', 'CoverSub'),
             p('Quantités • Étapes numérotées • Conseils de cuisson<br/>Menus • Liste de courses • Organisation', 'CoverSub'),
             Spacer(1, 40), p('Des recettes familiales, des adaptations annoncées<br/>et le plaisir de recevoir.', 'CoverSub'), PageBreak()]
    markdown((ROOT / 'guide-introduction.md').read_text())
    body.append(PageBreak())
    body.append(p('Index des 100 recettes', 'ChapterGuide'))
    chapter = ''
    for r in recipes:
        if r['chapter'] != chapter:
            chapter = r['chapter']
            body.append(p(escape(chapter), 'SubGuide'))
        body.append(p(f'<link href="#recette-{r["number"]}" color="#174A3B">{r["number"]}. {escape(r["title"])}</link>', 'IndexGuide'))
    body.append(PageBreak())
    for idx, r in enumerate(recipes):
        if idx % 10 == 0:
            body.append(p(escape(r['chapter']), 'ChapterGuide'))
        header = f'<a name="recette-{r["number"]}"/>{r["number"]}. {escape(r["title"])}'
        card = [p(header, 'RecipeGuide'), p(escape(r['origin']), 'MetaGuide'),
                p(f'<b>{escape(r["portions"])}</b> · Préparation et cuisson : {escape(r["duration"])}<br/>Attente à prévoir : {escape(r["wait"])}', 'MetaGuide'),
                p('<b>INGRÉDIENTS</b><br/>' + escape(r['ingredients'])),
                p('<b>PAS À PAS</b>')]
        for i, step in enumerate(r['steps'], 1):
            card.append(p(f'<b>{i}.</b> {escape(step)}'))
        card.append(p('<b>Conseil débutant.</b> ' + escape(r['tip'])))
        body.append(KeepTogether(card))
        if idx % 2 == 1:
            body.append(PageBreak())
        else:
            body.extend([Spacer(1, 9), HRFlowable(width='100%', thickness=.5, color=gold), Spacer(1, 8)])
    markdown((ROOT / 'guide-annexes.md').read_text())
    def footer(canvas, doc):
        if doc.page == 1:
            return
        canvas.saveState()
        canvas.setStrokeColor(gold)
        canvas.line(42, 35, A4[0]-42, 35)
        canvas.setFont('Guide', 7)
        canvas.setFillColor(green)
        canvas.drawString(42, 23, '100 RECETTES BÉNINOISES & AFRICAINES • ÉDITION DÉBUTANT')
        canvas.drawRightString(A4[0]-42, 23, str(doc.page))
        canvas.restoreState()
    doc = SimpleDocTemplate(str(ROOT / f'{STEM}.pdf'), pagesize=A4, rightMargin=42, leftMargin=42,
                            topMargin=36, bottomMargin=47, title='Le Guide Ultime des 100 Recettes Béninoises & Africaines',
                            author='Guide culinaire — édition débutant', pageCompression=1)
    doc.build(body, onFirstPage=footer, onLaterPages=footer)

if __name__ == '__main__':
    recipes = load_recipes()
    make_markdown(recipes)
    make_pdf(recipes)
    print(f'100 recettes vérifiées. Fichiers générés : {STEM}.md et .pdf')
