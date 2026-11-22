"""Compose le guide (texte sélectionnable), un extrait et le visuel carré de la boutique."""
import os
import re
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

import pymupdf
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

from commun import ICI, VENTE, LIENS, GUIDE

W, H, M = 390, 844, 22
COL = W-2*M
INK, FOREST, TEAL = '#162C31', '#123F41', '#176563'
FADE, LINE, SOFT, PAPER = '#486266', '#CDDAD4', '#E6F2ED', '#FFFEFA'
SAND, GOLD, SKY, CLAY = '#F6E9D5', '#E6B55D', '#ABCED0', '#D9784C'
WHITE = '#FFFFFF'
FONT_DIR = Path(os.environ.get('DOSSIER_FONTS', '/usr/share/fonts/truetype/dejavu'))
FONTS = {'Sans':'DejaVuSans.ttf', 'SansB':'DejaVuSans-Bold.ttf', 'Serif':'DejaVuSerif.ttf', 'SerifB':'DejaVuSerif-Bold.ttf'}
for name, path in FONTS.items():
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / path)))
pdfmetrics.registerFontFamily('Sans', normal='Sans', bold='SansB')
pdfmetrics.registerFontFamily('Serif', normal='Serif', bold='SerifB')

def fill(c, color): c.setFillColor(HexColor(color))
def stroke(c, color): c.setStrokeColor(HexColor(color))
def rect(c, x, y, w, h, color):
    fill(c, color); c.rect(x,y,w,h,stroke=0,fill=1)
def txt(c,x,y,text,size=11,font='Sans',color=INK,right=False):
    fill(c,color); c.setFont(font,size)
    (c.drawRightString if right else c.drawString)(x,y,text)
def line(c,x1,y1,x2,y2,color=LINE,width=0.7):
    stroke(c,color); c.setLineWidth(width); c.line(x1,y1,x2,y2)
def fr(text):
    text = re.sub(r' (?=[:;?!»€])', '\N{NO-BREAK SPACE}', text).replace('« ', '«\N{NO-BREAK SPACE}')
    return re.sub(r'(?<=\d) (?=\d{3}\b)', '\N{NO-BREAK SPACE}', text)
def markup(text):
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', escape(fr(text)))
def para(text, size=14, leading=None, font='Sans', color=INK, html=False):
    style = ParagraphStyle('ligne', fontName=font, fontSize=size, leading=leading or size*1.35,
                           textColor=HexColor(color), splitLongWords=False, allowWidows=0)
    return Paragraph(text if html else markup(text),style)
def measure(p, width): return p.wrap(width, 5000)[1]
def top(c,p,x,y,w):
    h=measure(p,w); p.drawOn(c,x,y-h); return y-h

def horizon(c,x,y,w,h):
    """Illustration vectorielle originale : un soleil se lève sur des feuilles ouvertes."""
    c.saveState(); c.translate(x,y); c.scale(w/360, h/210)
    clip=c.beginPath(); clip.rect(0,0,360,210); c.clipPath(clip,stroke=0,fill=0)
    rect(c,0,0,360,210,SKY)
    # Cartographic ruling, solar disc and faint concentric arcs.
    for i in range(-2,12): line(c,42*i,-8,42*i+60,218,'#9BBFC0',0.55)
    for i in range(1,7): line(c,0,32*i,360,32*i,'#9BBFC0',0.55)
    aspect=(w/360)/(h/210)
    fill(c,CLAY); c.ellipse(226,142-32*aspect,290,142+32*aspect,stroke=0,fill=1)
    for rad in (41, 48):
        stroke(c,'#8AADB1'); c.setLineWidth(.65); c.arc(258-rad,142-rad*aspect,258+rad,142+rad*aspect,15,122)
    # The two sides of an open notebook meet at the same fold.
    p=c.beginPath(); p.moveTo(-8,127); p.curveTo(53,168,124,152,186,59); p.curveTo(227,123,306,132,368,123); p.lineTo(368,-2); p.lineTo(-8,-2); p.close(); fill(c,SAND); c.drawPath(p,fill=1,stroke=0)
    p=c.beginPath(); p.moveTo(-8,123); p.curveTo(63,155,133,130,186,55); p.curveTo(230,108,308,112,368,106); p.lineTo(368,-2); p.lineTo(-8,-2); p.close(); fill(c,'#E6BC70'); c.drawPath(p,fill=1,stroke=0)
    for i in range(12):
        z=i*7.2; p=c.beginPath(); p.moveTo(-7,116-z*.85); p.curveTo(59,150-z*.85,120,120-z*.7,186,51-z*.45); p.curveTo(239,103-z*.48,299,107-z*.68,370,101-z*.68); stroke(c,'#A86A39'); c.setLineWidth(.65 if i%3 else 1.0); c.drawPath(p)
    p=c.beginPath();p.moveTo(-5,67);p.curveTo(68,93,121,82,186,25);p.curveTo(237,63,300,70,365,61);p.lineTo(365,-5);p.lineTo(-5,-5);p.close();fill(c,TEAL);c.drawPath(p,stroke=0,fill=1)
    for i in range(8):
        z=i*5.8;p=c.beginPath();p.moveTo(-5,63-z);p.curveTo(62,90-z,123,79-z,186,22-z*.62);p.curveTo(235,60-z*.75,302,68-z,365,58-z*.9);stroke(c,'#57918A');c.setLineWidth(.65);c.drawPath(p)
    c.restoreState()

def cover(c,extrait=False):
    rect(c,0,0,W,H,FOREST)
    for n,clr in enumerate([SAND,GOLD,CLAY]): rect(c,M+n*8,H-54,5,19-n*3,clr)
    txt(c,M+36,H-48,'CARNET DE CANDIDATURE',10,'SansB',SAND)
    txt(c,W-M,H-48,'2027',11,'Serif',SAND,True)
    line(c,M,H-70,W-M,H-70,'#547674')
    txt(c,M,H-120,'ÉTUDES SUPÉRIEURES',10,'SansB','#B9DAD3')
    txt(c,M-2,H-186,'Mon dossier',43,'Serif',PAPER)
    txt(c,M-3,H-254,'France',73,'SerifB',PAPER)
    txt(c,M,H-296,'Trouver une bourse et',20,'Sans',SAND)
    txt(c,M,H-325,'candidater sans agence',20,'SansB',SAND)
    horizon(c,0,127,W,309)
    rect(c,0,0,W,127,'#103638');rect(c,M,105,45,3,CLAY)
    txt(c,M,78,'AFRIQUE FRANCOPHONE',12,'SansB',PAPER)
    txt(c,M,56,'Avec un parcours pratique depuis le Bénin',12,'Sans','#CFDFD7')
    txt(c,M,24,'EXTRAIT GRATUIT' if extrait else 'GUIDE INDÉPENDANT',9,'SansB',SAND)
    txt(c,W-M,24,'ÉDITION  /  NOVEMBRE 2026',9,'Sans',SAND,True)

def vignette():
    # Render as a true 1080×1080 PNG; no third-party logos or photo rights.
    from io import BytesIO
    b=BytesIO(); c=canvas.Canvas(b,pagesize=(540,540),invariant=1)
    rect(c,0,0,540,540,FOREST); txt(c,32,500,'GUIDE PRATIQUE   /   AFRIQUE FRANCOPHONE',13,'SansB',SAND)
    line(c,32,482,508,482,'#68908B');txt(c,29,423,'Mon dossier',50,'Serif',PAPER);txt(c,29,343,'France',83,'SerifB',PAPER)
    txt(c,33,302,'Trouver une bourse et candidater sans agence',19,'Sans',SAND)
    horizon(c,0,62,540,211)
    txt(c,32,25,'GUIDE + MODÈLES + TABLEUR',13,'SansB',PAPER);txt(c,508,25,'RENTRÉE 2027',12,'SansB',SAND,True)
    c.showPage();c.save();d=pymupdf.open(stream=b.getvalue(),filetype='pdf');d[0].get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False).save(VENTE/'Visuel-Chariow.png');d.close()

def read_pages():
    result=[]
    for line_ in (ICI/'guide.md').read_text(encoding='utf-8').splitlines():
        s=line_.strip()
        if not s: continue
        if s.startswith('# '):
            key,tag,title=s[2:].split(' | ',2);result.append(dict(key=key,tag=tag,title=title,blocks=[],refs=[])); continue
        if s.startswith('@ '):
            result[-1]['refs'].extend(s[2:].split()); continue
        prefix=s[:2]
        kind,text=({'##':('h',s[3:]), '> ':('lead',s[2:]), '- ':('item',s[2:]), '! ':('note',s[2:])}.get(prefix,('p',s)))
        result[-1]['blocks'].append((kind,text))
    return result

GROUPS=[('niveau','Choisir ta piste','Niveau d’études, admission, financement, visa.'),('eiffel','Comparer quatre financements','Eiffel, Boutmy, Mastercard et Erasmus Mundus.'),('voie','Candidater depuis ton pays','Choix du portail ; exemple de la procédure au Bénin.'),('pieces','Construire ton dossier','Pièces, CV, motivation, projet et recommandations.'),('budget','Déposer et suivre','Budget, délais, entretien et réponse à une offre.'),('depart','Vérifier avant de partir','Dernière liste de contrôle et liens officiels.')]

def footer(c,n,total,extrait=False):
    line(c,M,38,W-M,38)
    txt(c,M,19,'EXTRAIT   /   MON DOSSIER FRANCE' if extrait else ('RENTRÉE 2027' if n==2 else '←  SOMMAIRE'),9.5,'SansB',TEAL)
    if not extrait and n!=2:c.linkRect('Sommaire','sommaire',(M-4,10,M+104,36),relative=0,thickness=0)
    txt(c,W-M,18,f'{n:02d}   /   {total:02d}',10,'SansB',FADE,True)

def header(c,tag):
    rect(c,0,0,W,H,PAPER);rect(c,M,H-39,15,4,CLAY)
    txt(c,M+23,H-40,tag.upper(),9,'SansB',TEAL)
    line(c,M,H-53,W-M,H-53)

def toc(c,numbers,total):
    header(c,'Mode d’emploi')
    y=top(c,para('Par où commencer ?',28,33,'SerifB'),M,H-70,COL)-14
    y=top(c,para('Tu n’as pas besoin de lire ce guide dans l’ordre. Touche la rubrique qui débloque ta prochaine démarche.',14.7,20.3),M,y,COL)-19
    for i,(key,title,desc) in enumerate(GROUPS,1):
        y1=y; rect(c,M,y-25,29,25,SOFT);txt(c,M+6,y-18,str(i).zfill(2),10.4,'SansB',TEAL)
        txt(c,M+40,y-15,title,14.9,'SansB',INK)
        b=top(c,para(desc,12.6,17,'Sans',FADE),M+40,y-23,COL-85)
        txt(c,W-M,b+3,str(numbers[key]).zfill(2)+' →',11,'SansB',TEAL,True)
        y=b-12;line(c,M,y,W-M,y);c.linkRect(title,key,(M,y,W-M,y1),relative=0,thickness=0);y-=12
    y-=2
    top(c,para('**Avec le guide :** un atelier Word à personnaliser et un tableur pour comparer les appels, suivre tes pièces et calculer ton budget. Les liens soulignés dans le PDF ouvrent les sources officielles.',12.7,17.6,'Sans',FOREST),M,y,COL)
    footer(c,2,total)

def source_par(keys):
    labels=[]
    for key in keys:
        name,url=LIENS[key];labels.append(f'<link href={quoteattr(url)} color="{TEAL}"><u>{escape(name)}</u></link>')
    return para('  •  '.join(labels),10.4,15.3,html=True)

def blocks(page,base):
    """(kind, paragraph, usable width, space before, space after, callout label)."""
    out=[]
    for typ,text in page['blocks']:
        label='';w=COL
        if typ=='lead':p=para(text,base+.65,base*1.39,'Sans',FOREST);pre,post=0,11
        elif typ=='h':p=para(text,base+1.0,base*1.30,'SansB',TEAL);pre,post=3,3.5
        elif typ=='note':
            label,value=text.split(' | ',1);p=para(value,base-.35,base*1.33);w-=22;pre,post=4,6
        elif typ=='item':p=para(text,base,base*1.34);w-=15;pre,post=0,5.5
        else:p=para(text,base,base*1.34);pre,post=0,6
        out.append((typ,p,w,pre,post,label))
    return out

def page_body(c,page,n,total,extrait=False):
    header(c,page['tag']);footer(c,n,total,extrait)
    headerp=para(page['title'],26.2,30.1,'SerifB',INK)
    y=top(c,headerp,M,H-62,COL)-11
    sp=source_par(page['refs']) if page['refs'] else None
    # Sources go in a separate, stable area, never over the text.
    src_top=49+(measure(sp,COL) + 18 if sp else 0)
    if sp:
        line(c,M,src_top+1,W-M,src_top+1);txt(c,M,src_top-11,'SOURCES  /  TOUCHER POUR OUVRIR',8,'SansB',FADE)
        top(c,sp,M,src_top-17,COL)
    last=src_top+8
    for tick in range(148,125,-1):
        base=tick/10
        stack=blocks(page,base);req=sum(a+b+measure(p,w)+(26 if k=='note' else 0) for k,p,w,a,b,_ in stack)
        if req <= y-last:break
    else:raise ValueError(f"Trop de texte : {page['key']} ({req:.1f} > {y-last:.1f})")
    for k,p,w,before,after,label in stack:
        y-=before;h=measure(p,w)
        if k=='note':
            rect(c,M,y-h-26,COL,h+26,SOFT);rect(c,M,y-h-26,2.3,h+26,TEAL)
            txt(c,M+11,y-13,label.upper(),9,'SansB',TEAL);top(c,p,M+11,y-19,w);y-=h+26
        elif k=='item':
            fill(c,CLAY);c.circle(M+3.2,y-base*.58,2.45,stroke=0,fill=1);y=top(c,p,M+15,y,w)
        else:y=top(c,p,M,y,w)
        y-=after
    assert y>=last-.1
    return base

def directory(c,n,total):
    header(c,'06 / À garder sous la main');footer(c,n,total)
    y=top(c,para('Ton carnet d’adresses',27,32,'SerifB'),M,H-70,COL)-12
    y=top(c,para('Un lien a changé ? Repars du domaine de l’organisme et recherche l’intitulé du programme et la rentrée. Ne suis pas un lien de paiement reçu en réponse privée.',14.2,19),M,y,COL)-18
    sections=[('Chercher un financement', ['catalogue','mundus','espaces']),('Retrouver les quatre pistes', ['eiffel','saclay','boutmy','carte','euro']),('Vérifier les modalités locales', ['eef','bj','exon','cotonou']),('Préparer le séjour', ['visa','assistant'])]
    for name,keys in sections:
        h=para(name,15,19,'SansB',FOREST);y=top(c,h,M,y,COL)-5
        for key in keys:
            lbl,url=LIENS[key];t=para(f'<link href={quoteattr(url)} color="{TEAL}"><u>{escape(lbl)}</u></link>',12.4,16.6,html=True);y=top(c,t,M+11,y,COL-11)-2
        y-=8
    top(c,para('**Repères vérifiés : novembre 2026.** Les appels cités concernent la rentrée 2027. Pour une rentrée ultérieure, recherche un nouvel appel : ne décale pas simplement les dates d’un an.',12.7,17.5,'Sans',FADE),M,y,COL)

def make():
    pages=read_pages();numbers={p['key']:i for i,p in enumerate(pages,3)};total=len(pages)+3
    assert len(numbers)==len(pages)
    VENTE.mkdir(exist_ok=True)
    c=canvas.Canvas(str(GUIDE),pagesize=(W,H),pageCompression=1,invariant=1,lang='fr')
    c.setTitle('Mon dossier France — Trouver une bourse et candidater sans agence');c.setAuthor('Mon dossier France · guide indépendant');c.setSubject('Afrique francophone • Rentrée 2027')
    c.bookmarkPage('couverture');c.addOutlineEntry('Mon dossier France','couverture');cover(c);c.showPage()
    c.bookmarkPage('sommaire');c.addOutlineEntry('Sommaire','sommaire');toc(c,numbers,total);c.showPage()
    for page in pages:
        k=page['key'];c.bookmarkPage(k);c.addOutlineEntry(page['title'],k,0 if k in {s[0] for s in GROUPS} else 1,closed=True)
        base=page_body(c,page,numbers[k],total);print(k,base);c.showPage()
    c.bookmarkPage('liens');c.addOutlineEntry('Ton carnet d’adresses','liens',1);directory(c,total,total);c.showPage();c.save()
    # An excerpt is rendered separately so no broken links point to missing book pages.
    c=canvas.Canvas(str(VENTE/'Extrait-gratuit.pdf'),pagesize=(W,H),pageCompression=1,invariant=1,lang='fr')
    c.setTitle('Mon dossier France — Extrait gratuit');c.setAuthor('Mon dossier France · guide indépendant');cover(c,True);c.showPage()
    for i,k in enumerate(('saclay','exemple'),2):
        page_body(c,next(p for p in pages if p['key']==k),i,3,True);c.showPage()
    c.save();vignette();print(f'{total} pages, extrait 3 pages, visuel 1080×1080')

if __name__=='__main__':make()
