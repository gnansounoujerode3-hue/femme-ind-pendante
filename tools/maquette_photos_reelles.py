"""Prototype : photos réelles uniquement, une page photo avant chaque recette sélectionnée."""
from pathlib import Path
from html import escape
import sys,json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from construire_guide import load_recipes
W,H=595.276,841.89
BG,GREEN,TERRA,MUTED=[HexColor(x) for x in ('#FAF6ED','#174A3B','#A9472D','#53665B')]
fonts=ROOT/'.agents/skills/canvas-design/canvas-fonts'
for name,file in [('Serif','CrimsonPro-Regular.ttf'),('SerifBold','CrimsonPro-Bold.ttf'),('Sans','InstrumentSans-Regular.ttf'),('SansBold','InstrumentSans-Bold.ttf')]:
 pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='SansBold',italic='Sans',boldItalic='SansBold')
selected=[11,22,4]
recipes={r['number']:r for r in load_recipes()}
registry=json.loads((ROOT/'assets/food/registry.json').read_text())
photos={p['recipe_id']:p for p in registry['images'] if p.get('image_kind')=='photograph'}
out=ROOT/'MAQUETTE-PHOTOS-REELLES.pdf'
c=canvas.Canvas(str(out),pagesize=(W,H))
c.setTitle('Terre de fête — photographie avant la recette — prototype')
c.setSubject('Trois recettes avec photographies réelles. Aucune image générée par IA.')

def text(s,x,y,size=11,font='Sans',color=GREEN):
 c.setFillColor(color);c.setFont(font,size);c.drawString(x,H-y-size*.8,s)
def para(s,x,y,w,size=11,font='Sans',color=GREEN):
 p=Paragraph(s,ParagraphStyle('body',fontName=font,fontSize=size,leading=size*1.42,textColor=color))
 _,h=p.wrap(w,1000)
 assert y+h<790,(s[:40],y,h)
 p.drawOn(c,x,H-y-h)
 return y+h

def line(y):
 c.setStrokeColor(TERRA);c.setLineWidth(.5);c.line(45,H-y,W-45,H-y)
def page(n,label):
 c.setFillColor(BG);c.rect(0,0,W,H,fill=1,stroke=0)
 text('TERRE DE FÊTE',45,27,8,'SansBold');text(label,320,27,8,color=MUTED)
 line(50);line(797)
 text('PHOTOGRAPHIES RÉELLES • MAQUETTE DE TRAVAIL',45,810,7.5,color=MUTED)
 text(str(n).zfill(2),530,808,9,'SansBold')
 c.bookmarkPage(f'p{n}')

# Couverture : reprendre exactement la composition initiale ; remplacer uniquement l’image.
c.setFillColor(BG);c.rect(0,0,W,H,fill=1,stroke=0)
c.bookmarkPage('p1')
def cover_text(s,x,y,size=11,font='Sans',color=GREEN):
 c.setFillColor(color);c.setFont(font,size);c.drawString(x,H-y-size*.78,s)
cover_text('LE GUIDE ULTIME',44,38,10,'SansBold',TERRA)
cover_text('100 recettes',41,70,56,'SerifBold')
cover_text('béninoises & africaines',44,130,33,'Serif')
cover_text('Noël & le 1er janvier',45,180,19,'Serif')
c.setStrokeColor(TERRA);c.setLineWidth(.6);c.line(45,H-219,109,H-219)
cover_text('PAS À PAS, POUR DÉBUTER EN CONFIANCE',45,235,9.5,'SansBold')
cover_photo=photos[11]
assert cover_photo['image_kind']=='photograph'
with Image.open(ROOT/cover_photo['local_path']) as im:
 # Même cadre que la première couverture ; recadrage proportionnel, sans étirement.
 scale=max(W/im.width,516/im.height)
 sw,sh=W/scale,516/scale
 x0,y0=(im.width-sw)/2,(im.height-sh)/2
 cropped=im.crop((round(x0),round(y0),round(x0+sw),round(y0+sh)))
 c.drawImage(ImageReader(cropped),0,H-273-516,W,516)
c.setFillColor(GREEN);c.rect(0,0,W,53,fill=1,stroke=0)
cover_text('Quantités claires. Gestes expliqués. Le plaisir de recevoir.',31,807,10,'Sans',BG)
# Attribution discrète, dans la zone où figurait le crédit de l’ancienne illustration.
c.setFillColor(GREEN);c.rect(315,H-789,280,20,fill=1,stroke=0)
cover_text('Photo : Aimeabibis • CC BY-SA 4.0 • recadrée',325,776,7,'Sans',BG)
c.linkURL(cover_photo['source_page_url'],(315,H-789,W,H-769),relative=0,thickness=0)
c.showPage()
page(2,'DANS CET EXTRAIT')
text('D’abord les yeux,',43,100,38,'Serif')
text('ensuite les gestes.',43,145,38,'Serif')
para('Chaque plat s’ouvre sur une photographie réelle, puis une page rassemble les ingrédients et la marche à suivre.',45,218,490,12)
y=310
for i,num in enumerate(selected):
 r=recipes[num];photo_page=3+2*i
 text(f'{num:02}',45,y,20,'SerifBold',TERRA)
 text(r['title'],100,y,20,'Serif')
 text(f'Photographie p. {photo_page}  /  Recette p. {photo_page+1}',100,y+34,10,color=MUTED)
 c.linkRect('',f'p{photo_page}',(44,H-y-60,550,H-y+5),thickness=0)
 line(y+74);y+=110
para('Les photos montrent des variantes familiales. Le poulet et les accompagnements visibles ne font pas automatiquement partie des quantités de chaque fiche.',45,689,490,10,color=MUTED)
para('Les recettes demeurent non testées en cuisine dans le cadre de ce projet.',45,754,490,9,color=MUTED)
c.showPage()
for index,num in enumerate(selected):
 r=recipes[num];p=photos[num];n=3+2*index
 assert p['image_kind']=='photograph'
 path=(ROOT/p['local_path']).resolve()
 assert path.parent==ROOT/'assets/food/previews'
 page(n,'LE PLAT EN IMAGE')
 text(f'RECETTE {num:02}',45,83,9,'SansBold',TERRA)
 para(escape(r['title']),43,110,510,33,'Serif')
 with Image.open(path) as im:
  ratio=min(505/im.width,445/im.height)
  w,h=im.width*ratio,im.height*ratio
  c.drawImage(ImageReader(im),45+(505-w)/2,H-220-h,w,h)
 caption='Amiwo accompagné de poulet.' if num==11 else ('Poulet yassa et riz servi à part.' if num==22 else 'Kelewele, présentation en tranches.')
 para(escape(caption)+' Photo illustrative d’une variante du plat.',45,683,505,10)
 credit=f'{escape(p["author"])} — {escape(p["license"])}. Image mise à l’échelle, sans retouche.'
 para(credit,45,715,505,8.5,color=MUTED)
 para(f'<link href="{escape(p["source_page_url"],quote=True)}" color="#174A3B">Source photographique</link> · <link href="{escape(p["license_url"],quote=True)}" color="#174A3B">Conditions de réutilisation</link>',45,744,505,8.5)
 text(f'LA RECETTE À LA PAGE SUIVANTE  →  {n+1}',45,773,8.5,'SansBold',TERRA)
 c.showPage()
 page(n+1,'LES INGRÉDIENTS & LES GESTES')
 text(f'RECETTE {num:02}',45,80,9,'SansBold',TERRA)
 para(escape(r['title']),43,105,505,31,'Serif')
 para(escape(r['origin']),45,155,505,9.5,color=MUTED)
 c.setFillColor(HexColor('#EAECDD'));c.rect(45,H-254,505,64,fill=1,stroke=0)
 text('POUR',58,202,8,'SansBold',TERRA);text(r['portions'],58,222,10,'SansBold')
 text('PRÉPARATION + CUISSON',260,202,8,'SansBold',TERRA);text(r['duration'],260,222,10)
 para('<b>Attente à prévoir :</b> '+escape(r['wait']),45,273,505,10)
 text('Les ingrédients',45,320,20,'Serif');text('À vous de jouer',242,320,20,'Serif')
 y=363
 for ing in r['ingredients'].split(' ; '):
  y=para(escape(ing),45,y,161,11)+9
 sy=363
 for step,description in enumerate(r['steps'],1):
  text(f'{step:02}',241,sy,12,'SerifBold',TERRA)
  sy=para(escape(description),270,sy,278,11)+14
 top=max(670,max(y,sy)+12)
 assert top<710,(num,top)
 text('LE PETIT CONSEIL',45,top,8.5,'SansBold',TERRA)
 para(escape(r['tip']),45,top+22,505,10)
 c.showPage()
c.save()
print(out)
