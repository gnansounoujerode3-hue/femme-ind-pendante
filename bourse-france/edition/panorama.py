"""Le bonus autonome : un index tactile, dix fiches sourcées et des exercices."""
from math import cos, sin, pi
from reportlab.pdfgen import canvas
from commun import BONUS, PANORAMA
from livret import (W, H, M, COL, INK, FOREST, TEAL, PAPER, SOFT, SAND, GOLD, CLAY,
                    FADE, rect, line, txt, fill, stroke, top, para, header, footer,
                    read_pages, page_body)

# L’ordre des liens suit celui des pages du bonus.
LECTURES = [('orientation', 'Quel est mon niveau ?'), ('lecture', 'Les mots en anglais')]
FICHES = [
    ('suisse', 'Suisse', 'ESOP · ETH Zurich', 'Ouvert'),
    ('paysbas', 'Pays-Bas', 'NL-High Potential · Maastricht', 'Ouvert'),
    ('rwanda', 'Rwanda', 'Mastercard · CMU-Africa', 'Admission ouverte'),
    ('belgique', 'Belgique', 'ICP Connect · UHasselt', 'Ouvert'),
    ('turquie', 'Turquie', 'Türkiye Scholarships', 'À confirmer'),
    ('royaumeuni', 'Royaume-Uni', 'Chevening', 'Clos'),
    ('allemagne', 'Allemagne', 'DAAD · Helmut-Schmidt', 'Clos'),
    ('canada', 'Canada', 'McCall MacBain · McGill', 'Clos'),
    ('japon', 'Japon', 'MEXT · voie ambassade', 'Clos'),
    ('chine', 'Chine', 'Schwarzman · Tsinghua', 'Clos · rentrée 2028 à suivre'),
]
ATELIERS = [('comparer','Comparer deux profils'), ('avance','Calculer une avance'),
            ('veille','Suivre un appel fermé'), ('decision','Ma fiche de décision')]


def couverture(c):
    nuit, azur = '#193C50', '#42677A'
    rect(c, 0, 0, W, H, nuit)
    txt(c,M,H-46,'MON DOSSIER FRANCE',10,'SansB',SAND)
    txt(c,W-M,H-46,'HORS-SÉRIE  /  01',9,'SansB',SAND,True)
    line(c,M,H-63,W-M,H-63,azur)
    txt(c,M,H-112,'LE TOP 10',16,'SansB',GOLD)
    txt(c,M-2,H-174,'Bourses',48,'SerifB',PAPER)
    txt(c,M-2,H-236,'complètes',48,'SerifB',PAPER)
    top(c,para('Dix pays où financer tes études, en partant du Bénin.',20,27,'Sans',SAND),M,H-266,COL)
    # Rose des dix directions, illustration vectorielle originale ; pas une carte.
    x, y, r = W/2, 330, 117
    for radius in (r, r*.76, r*.49):
        stroke(c,azur); c.setLineWidth(.8); c.circle(x,y,radius,stroke=1,fill=0)
    for i in range(10):
        a=pi/2-2*pi*i/10
        line(c,x+(r*.5)*cos(a),y+(r*.5)*sin(a),x+(r-5)*cos(a),y+(r-5)*sin(a),azur,.8)
        fill(c, GOLD if i%2==0 else CLAY); c.circle(x+r*cos(a),y+r*sin(a),3.2,stroke=0,fill=1)
    txt(c,x-39,y-22,'10',54,'Serif',PAPER)
    rect(c,0,0,W,148,SAND);rect(c,M,120,39,3,CLAY)
    txt(c,M,91,'SCOLARITÉ  +  VIE SUR PLACE',13,'SansB',FOREST)
    top(c,para('Ce qui est payé, ce qui reste à avancer et où déposer ton dossier.',13.5,18,'Sans',INK),M,76,COL)
    txt(c,M,20,'FICHES INDÉPENDANTES',8.8,'SansB',TEAL)
    txt(c,W-M,20,'NOVEMBRE 2026',9,'SansB',TEAL,True)


def sommaire(c, numbers, total):
    header(c,'Top 10 / Sommaire interactif')
    y=top(c,para('Choisis ta destination',25,30,'SerifB'),M,H-69,COL)-12
    y=top(c,para('En novembre 2026, certaines campagnes sont déjà closes. Touche un pays pour vérifier sa rentrée, ses règles et son site. Tu débutes ? Commence par ces deux pages.',13.5,18),M,y,COL)-12
    for i,(key,label) in enumerate(LECTURES):
        x=M+i*(COL/2+2); rect(c,x,y-30,COL/2-3,30,SOFT)
        txt(c,x+6,y-20,f'{numbers[key]}  {label}',11.2,'SansB',TEAL)
        c.linkRect(label,key,(x,y-30,x+COL/2-3,y),relative=0,thickness=0)
    y-=42
    for i,(key,pays,nom,etat) in enumerate(FICHES,1):
        txt(c,M,y-13,f'{i:02d}',10,'SansB',TEAL)
        txt(c,M+28,y-13,pays,14,'SansB',INK)
        txt(c,M+28,y-29,nom,11,'Sans',FADE)
        txt(c,W-M,y-13,etat,10.2,'SansB',FOREST,True)
        line(c,M,y-38,W-M,y-38)
        c.linkRect(f'{pays} : {nom}',key,(M,y-38,W-M,y+3),relative=0,thickness=0)
        y-=43
    y-=10; txt(c,M,y,'POUR PASSER À L’ACTION',9,'SansB',TEAL); y-=9
    for i,(key,label) in enumerate(ATELIERS):
        x=M+(i%2)*(COL/2+2); row_y=y-(i//2)*30
        rect(c,x,row_y-25,COL/2-3,25,SAND)
        txt(c,x+5,row_y-16,f'{numbers[key]}  {label}',10.6,'SansB',FOREST)
        c.linkRect(label,key,(x,row_y-25,x+COL/2-3,row_y),relative=0,thickness=0)
    assert y-60>45, 'Index du Top 10 trop long'
    footer(c,2,total,index_label='BONUS  /  10 PAYS')


def make():
    pages=read_pages('panorama.md')
    numbers={p['key']:i for i,p in enumerate(pages,3)}
    assert list(numbers)==[*[key for key,_ in LECTURES],*[f[0] for f in FICHES],*[a[0] for a in ATELIERS]]
    total=len(pages)+2
    BONUS.mkdir(exist_ok=True)
    c=canvas.Canvas(str(PANORAMA),pagesize=(W,H),pageCompression=1,invariant=1,lang='fr')
    c.setTitle('Top 10 des bourses complètes — Dix pays, depuis le Bénin')
    c.setAuthor('Mon dossier France · édition indépendante')
    c.setSubject('Scolarité, vie sur place, calendrier et reste à avancer')
    c.bookmarkPage('couverture'); c.addOutlineEntry('Top 10 des bourses complètes','couverture'); couverture(c); c.showPage()
    c.bookmarkPage('sommaire'); c.addOutlineEntry('Choisis ta destination','sommaire'); sommaire(c,numbers,total); c.showPage()
    pays={f[0]:f[1] for f in FICHES}
    for p in pages:
        k=p['key']; c.bookmarkPage(k)
        label=(pays[k]+' — ' if k in pays else '')+p['title']
        c.addOutlineEntry(label,k); base=page_body(c,p,numbers[k],total,numbers)
        print('Top 10 /',k,base); c.showPage()
    c.save()
    print(f'Bonus international : {len(FICHES)} pays, {total} pages.')

if __name__=='__main__':
    make()
