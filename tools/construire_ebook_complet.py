"""Livre complet au design validé. --final refuse une édition incomplètement illustrée."""
from pathlib import Path
from html import escape
import argparse,json,re,sys
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Flowable, Paragraph,
    Spacer, PageBreak, NextPageTemplate, Table, TableStyle, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from construire_guide import load_recipes
W,H=595.276,841.89
CREAM,GREEN,TERRA,MUTED=[HexColor(x) for x in ('#FAF6ED','#174A3B','#A9472D','#53665B')]
OUT='EBOOK-100-RECETTES-TERRE-DE-FETE-TRAVAIL.pdf'


def main(final=False):
    recipes=load_recipes()
    registry=json.loads((ROOT/'assets/food/registry.json').read_text())
    photos={}
    for item in registry['images']:
        local=item.get('local_path')
        if item.get('image_kind')=='photograph' and item.get('status')!='rejected' and local and (ROOT/local).is_file():
            photos[item['recipe_id']]=item
    ready={n:p for n,p in photos.items() if p['status']=='approved' and p.get('publication_ready') is True}
    if final and any(r['number'] not in ready for r in recipes):
        missing=[str(r['number']) for r in recipes if r['number'] not in ready]
        print('EXPORT FINAL BLOQUÉ : photographies finales manquantes ou non validées pour '+', '.join(missing),file=sys.stderr)
        return 2
    if final: photos=ready
    fonts=ROOT/'.agents/skills/canvas-design/canvas-fonts'
    for name,file in [('Serif','CrimsonPro-Regular.ttf'),('SerifBold','CrimsonPro-Bold.ttf'),('Sans','InstrumentSans-Regular.ttf'),('SansBold','InstrumentSans-Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
    pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='SansBold',italic='Sans',boldItalic='SansBold')
    styles={
        'body':ParagraphStyle('body',fontName='Sans',fontSize=11,leading=15.5,textColor=GREEN,spaceAfter=8),
        'small':ParagraphStyle('small',fontName='Sans',fontSize=9,leading=12.5,textColor=MUTED,spaceAfter=7),
        'label':ParagraphStyle('label',fontName='SansBold',fontSize=9,leading=13,textColor=TERRA,spaceAfter=8,keepWithNext=True),
        'h1':ParagraphStyle('h1',fontName='Serif',fontSize=31,leading=34,textColor=GREEN,spaceAfter=15,keepWithNext=True),
        'h2':ParagraphStyle('h2',fontName='Serif',fontSize=21,leading=25,textColor=GREEN,spaceBefore=13,spaceAfter=10,keepWithNext=True),
        'sub':ParagraphStyle('sub',fontName='SansBold',fontSize=12,leading=17,textColor=GREEN,spaceBefore=10,spaceAfter=9,keepWithNext=True),
        'index':ParagraphStyle('index',fontName='Sans',fontSize=11,leading=16,textColor=GREEN,spaceAfter=7),
    }
    def p(s,style='body'): return Paragraph(s,styles[style])
    def inline(s):return re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',escape(s))
    def paragraph_draw(c,s,x,y,w,style='body'):
        par=p(s,style);_,height=par.wrap(w,1000);par.drawOn(c,x,y-height);return height

    class Cover(Flowable):
        def __init__(self):
            super().__init__();self.width=W;self.height=H
        def draw(self):
            c=self.canv;c.setFillColor(CREAM);c.rect(0,0,W,H,fill=1,stroke=0)
            def t(s,x,top,size,font='Sans',color=GREEN):
                c.setFillColor(color);c.setFont(font,size);c.drawString(x,H-top-size*.78,s)
            t('LE GUIDE ULTIME',44,38,10,'SansBold',TERRA)
            t('100 recettes',41,70,56,'SerifBold')
            t('béninoises & africaines',44,130,33,'Serif')
            t('Noël & le 1er janvier',45,180,19,'Serif')
            c.setStrokeColor(TERRA);c.setLineWidth(.6);c.line(45,H-219,109,H-219)
            t('PAS À PAS, POUR DÉBUTER EN CONFIANCE',45,235,9.5,'SansBold')
            photo=photos[11]
            with Image.open(ROOT/photo['local_path']) as im:
                scale=max(W/im.width,516/im.height)
                sw,sh=W/scale,516/scale;x0,y0=(im.width-sw)/2,(im.height-sh)/2
                crop=im.crop((round(x0),round(y0),round(x0+sw),round(y0+sh)))
                c.drawImage(ImageReader(crop),0,H-789,W,516)
            c.setFillColor(GREEN);c.rect(0,0,W,53,fill=1,stroke=0)
            t('Quantités claires. Gestes expliqués. Le plaisir de recevoir.',31,807,10,'Sans',CREAM)
            c.rect(315,H-789,280,20,fill=1,stroke=0)
            t('Photo : Aimeabibis • CC BY-SA 4.0 • recadrée',325,776,7,'Sans',CREAM)
            c.linkURL(photo['source_page_url'],(315,H-789,W,H-769),relative=0,thickness=0)

    class Picture(Flowable):
        width=505;height=440
        def __init__(self,photo=None):
            super().__init__();self.photo=photo;self.width=505;self.height=440
        def draw(self):
            c=self.canv
            if self.photo:
                with Image.open(ROOT/self.photo['local_path']) as im:
                    scale=min(self.width/im.width,self.height/im.height)
                    w,h=im.width*scale,im.height*scale
                    c.drawImage(ImageReader(im),(self.width-w)/2,(self.height-h)/2,w,h)
            else:
                c.setFillColor(HexColor('#EEEADF'));c.roundRect(0,0,505,440,8,fill=1,stroke=0)
                paragraph_draw(c,'Photographie réelle<br/>à intégrer',40,265,425,'h1')
                paragraph_draw(c,'Emplacement de production — aucune image de substitution.<br/>Cette page doit être complétée avant diffusion au client.',40,155,425,'small')

    def decoration(c,doc):
        c.saveState();c.setFillColor(CREAM);c.rect(0,0,W,H,fill=1,stroke=0)
        c.setFillColor(GREEN);c.setFont('SansBold',8);c.drawString(45,H-34,'TERRE DE FÊTE')
        c.setFont('Sans',8);c.drawRightString(W-45,H-34,'100 RECETTES • ÉDITION DÉBUTANT')
        c.setStrokeColor(TERRA);c.setLineWidth(.5);c.line(45,H-49,W-45,H-49);c.line(45,45,W-45,45)
        c.setFillColor(MUTED);c.setFont('Sans',7.5)
        c.drawString(45,29,'VERSION DE TRAVAIL • PHOTOGRAPHIES À COMPLÉTER' if not final else '100 RECETTES BÉNINOISES & AFRICAINES')
        c.setFont('SansBold',9);c.drawRightString(W-45,28,str(doc.page).zfill(2));c.restoreState()

    class Book(BaseDocTemplate):
        def afterFlowable(self,flowable):
            key=getattr(flowable,'nav_key',None)
            if key:
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(flowable.getPlainText(),key,0,False)
    output=ROOT/('EBOOK-100-RECETTES-TERRE-DE-FETE.pdf' if final else OUT)
    doc=Book(str(output),pagesize=(W,H),title='100 recettes béninoises & africaines — Terre de fête',
             author='Atelier éditorial culinaire',subject='Mise en page intégrale — photographies réelles uniquement',pageCompression=1)
    doc.addPageTemplates([
        PageTemplate(id='cover',frames=[Frame(0,0,W,H,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)]),
        PageTemplate(id='body',frames=[Frame(45,58,505,H-128,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=decoration)
    ])
    story=[Cover(),NextPageTemplate('body'),PageBreak()]
    def heading(text,key):
        item=p(escape(text),'h1');item.nav_key=key;story.append(item)
    def markdown(text):
        for raw in text.splitlines():
            line=raw.strip()
            if not line or line=='---' or line.startswith('# '):continue
            if line.startswith('### '):story.append(p(inline(line[4:]),'sub'))
            elif line.startswith('## '):story.append(p(inline(line[3:]),'h2'))
            elif line.startswith('- '):story.append(p('• '+inline(line[2:])))
            else:story.append(p(inline(line)))
    heading('Avant publication','etat')
    story.extend([p('MISE EN PAGE COMPLÈTE — VERSION DE TRAVAIL','label'),
        p('Le design de la couverture et des fiches reprend la maquette validée. Ce volume contient les 100 recettes, leurs emplacements photographiques, les conseils pour débutants et les annexes.'),
        p(f'<b>{len(photos)} aperçus photographiques disponibles sur 100 ; {100-len(photos)} emplacements restent à compléter.</b> Les aperçus sont en basse définition et ne sont pas validés pour une publication finale.'),
        p('Les pages sans photographie portent explicitement la mention « à intégrer ». Ce document n’est pas un e-book final prêt à vendre. Aucune image générée par IA n’est utilisée.'),
        p('Les photographies existantes illustrent des variantes des plats : elles ne montrent pas des recettes testées pour ce livre. Les accompagnements visibles ne sont pas forcément inclus dans la fiche.'),
        p('Recettes rédigées pour ce projet, non testées en cuisine dans le cadre de sa réalisation. Faire relire et tester avant commercialisation.'),
        p('Pour exporter la version finale, le générateur exige une photographie validée pour chacune des 100 recettes. Il ne transforme pas les emplacements vides en illustrations fictives.'),PageBreak()])
    heading('Les 100 recettes','sommaire')
    story.append(p('Touchez un titre pour ouvrir la fiche correspondante.','small'))
    chapter=''
    for r in recipes:
        if chapter!=r['chapter']:
            chapter=r['chapter'];story.append(p(escape(chapter),'h2'))
        story.append(p(f'<link href="#recette-{r["number"]}" color="#174A3B">{r["number"]:02}. {escape(r["title"])}</link>','index'))
    story.append(PageBreak());heading('Cuisiner en confiance','debuter')
    markdown((ROOT/'guide-introduction.md').read_text())
    story.append(PageBreak())
    chapter=''
    for r in recipes:
        num=r['number']
        if chapter!=r['chapter']:
            chapter=r['chapter'];heading(chapter,f'chapitre-{num}')
            story.extend([Spacer(1,30),p('Des gestes simples, des repères clairs.','h2'),
                p('Commencez par lire la recette entière. Préparez les ingrédients, vérifiez les temps d’attente et choisissez votre accompagnement.'),
                p('Une page est réservée au plat terminé avant chaque recette. Les emplacements sans photo sont signalés sans ambiguïté.','small'),PageBreak()])
        label=p(f'RECETTE {num:02} • LE PLAT EN IMAGE','label');story.append(label)
        heading(r['title'],f'photo-{num}')
        photo=photos.get(num)
        story.extend([Picture(photo),Spacer(1,16)])
        if photo:
            story.append(p('Photographie illustrative d’une variante du plat. Aperçu de travail en basse définition.','small'))
            if photo.get('caption'):
                story.append(p(escape(photo['caption']),'small'))
            story.append(p(escape(photo['attribution'])+'. Mise à l’échelle sans recadrage sur cette page.','small'))
            story.append(p(f'<link href="{escape(photo["source_page_url"],quote=True)}">Page source</link> · <link href="{escape(photo["license_url"],quote=True)}">Licence</link>','small'))
        else:story.append(p('PHOTOGRAPHIE MANQUANTE — NE PAS PUBLIER CETTE PAGE EN L’ÉTAT','label'))
        story.extend([p('La recette commence à la page suivante.','small'),PageBreak()])
        story.append(p(f'RECETTE {num:02}','label'));heading(r['title'],f'recette-{num}')
        story.append(p(escape(r['origin']),'small'))
        meta=Table([[p('<b>POUR</b>','small'),p('<b>PRÉPARATION + CUISSON</b>','small')],
                    [p(escape(r['portions'])),p(escape(r['duration']))]],colWidths=[245,260])
        meta.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),HexColor('#EAECDD')),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LEFTPADDING',(0,0),(-1,-1),12)]))
        story.extend([meta,Spacer(1,10),p('<b>Attente à prévoir :</b> '+escape(r['wait'])),Spacer(1,9)])
        ingredients=[p('Les ingrédients','h2')]+[p(escape(x)) for x in r['ingredients'].split(' ; ')]
        steps=[p('À vous de jouer','h2')]+[p(f'<font color="#A9472D"><b>{i:02}.</b></font> '+escape(s)) for i,s in enumerate(r['steps'],1)]
        columns=Table([[ingredients,steps]],colWidths=[184,321])
        columns.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(0,0),22),('RIGHTPADDING',(1,0),(1,0),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
        story.append(columns)
        tip=Table([[p('<b>LE PETIT CONSEIL</b><br/>'+escape(r['tip']))]],colWidths=[505])
        tip.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),HexColor('#EEE5D6')),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
        story.extend([Spacer(1,15),tip,PageBreak()])
    heading('Menus & organisation','annexes')
    markdown((ROOT/'guide-annexes.md').read_text())
    story.extend([PageBreak()]);heading('Crédits photographiques','credits')
    story.append(p('Les photos ci-dessous sont des aperçus présents dans cette version de travail. Leurs licences ne s’étendent pas automatiquement au texte du livre. Les pages photo indiquent leur source.'))
    for num,photo in sorted(photos.items()):
        story.extend([p(f'{num}. {escape(recipes[num-1]["title"])}','sub'),p(escape(photo['attribution'])),
            p(f'<link href="{escape(photo["source_page_url"],quote=True)}">{escape(photo["source_page_url"])}</link>','small'),
            p(f'<link href="{escape(photo["license_url"],quote=True)}">{escape(photo["license_url"])}</link>','small')])
    story.append(p('La couverture reprend la photographie d’amiwo par Aimeabibis, recadrée. Les aperçus intérieurs sont mis à l’échelle sans retouche générative.','small'))
    doc.build(story)
    report=dict(file=output.name,recipes=100,photo_slots=100,preview_photos=len(photos),missing_photos=100-len(photos),publication_ready=False if not final else True,
                notes=['Couverture et direction artistique validées','Photos manquantes signalées, aucune image IA','Recettes non testées en cuisine','Validation visuelle et technique requise'])
    folder=ROOT/'reports/ebook-complet';folder.mkdir(exist_ok=True,parents=True)
    (folder/'etat-production.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(output)
    return 0

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--final',action='store_true')
    sys.exit(main(parser.parse_args().final))
