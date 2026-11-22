"""Composer la proposition Eiffel, isolée du guide et des deux ZIP."""
from io import BytesIO
from pathlib import Path
import sys

import pymupdf
from PIL import Image
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parents[1] / 'edition'))
from commun import LIENS
from livret import (W, H, M, COL, FOREST, TEAL, INK, FADE, PAPER, SAND, SOFT,
                    LINE, GOLD, CLAY, rect, line, txt, fill, fr, para, top)

PDF = ICI / 'Eiffel-master-Paris-Saclay.pdf'
IMAGE = ICI / 'Eiffel-master-mobile.png'
CATALOGUE = 'https://www.universite-paris-saclay.fr/formation/deuxieme-cycle'
LIEN_LOCAL = LIENS['saclay'][1]
LIEN_NATIONAL = LIENS['eiffel'][1]


def enveloppe(c):
    """Petit dessin vectoriel de correspondance, sans logo d’établissement."""
    c.saveState()
    c.translate(W-M-47, H-86)
    c.rotate(7)
    rect(c, 3, -2, 42, 27, '#2D5555')
    rect(c, 0, 0, 42, 26, SAND)
    line(c, 1, 1, 17, 14, TEAL, .85)
    line(c, 41, 1, 25, 14, TEAL, .85)
    volet = c.beginPath()
    volet.moveTo(0, 26); volet.lineTo(21, 10); volet.lineTo(42, 26); volet.close()
    fill(c, GOLD); c.drawPath(volet, fill=1, stroke=0)
    for x, y, longueur in [(-13, 18, 8), (-17, 12, 11), (-9, 6, 5)]:
        line(c, x, y, x+longueur, y, '#A8C8BB', 1.2)
    c.restoreState()


def composer_page(c):
    # Les positions ci-dessous descendent à partir du haut de la page.
    def texte(x, y, s, corps, police='Sans', couleur=INK, droite=False):
        txt(c, x, H-y, fr(s), corps, police, couleur, droite)

    def bloc(y, s, corps=14.2, interligne=18.4, *, x=M, largeur=COL, couleur=INK):
        return H-top(c, para(s, corps, interligne, color=couleur), x, H-y, largeur)

    def fond(x, y, largeur, hauteur, couleur):
        rect(c, x, H-y-hauteur, largeur, hauteur, couleur)

    def titre_etape(y, numero, titre):
        # Le numéro et les mots donnent le sens même sans couleur.
        fond(M, y-15.5, 23, 20, SOFT)
        texte(M+4.5, y-1, numero, 10, 'SansB', TEAL)
        texte(M+33, y, titre, 18, 'SerifB', FOREST)

    def lien(x, y, largeur, hauteur, libelle, url, *, bouton=False):
        corps = 13.4 if bouton else 11.6
        marge = 12 if bouton else 0
        w = stringWidth(libelle, 'SansB', corps)
        if w+2*marge+17 > largeur:
            raise ValueError(f'Libellé trop long : {libelle}')
        if bouton:
            fond(x, y, largeur, hauteur, SOFT)
        base = y+hauteur/2+corps*.34
        texte(x+marge, base, libelle, corps, 'SansB', TEAL)
        line(c, x+marge, H-base-2, x+marge+w, H-base-2, TEAL, .65)
        # Flèche dessinée plutôt qu’un caractère qui dépend de la police du lecteur.
        ax = x+largeur-marge-8 if bouton else x+w+6
        ay = H-base+1
        line(c, ax, ay, ax+6, ay+6, TEAL, 1.1)
        line(c, ax+1, ay+6, ax+6, ay+6, TEAL, 1.1)
        line(c, ax+6, ay+6, ax+6, ay+1, TEAL, 1.1)
        c.linkURL(url, (x, H-y-hauteur, x+largeur, H-y), relative=0, thickness=0)

    fond(0, 0, W, H, PAPER)
    fond(0, 0, W, 250, FOREST)
    for i, couleur in enumerate((SAND, GOLD, CLAY)):
        fond(M+i*5.7, 20+i*1.6, 3.6, 11-i*1.6, couleur)
    texte(M+24, 29.5, 'MON DOSSIER FRANCE', 10.2, 'SansB', PAPER)
    texte(W-M, 29.5, 'RENTRÉE 2027–2028', 10, 'SansB', SAND, True)
    line(c, M, H-42, W-M, H-42, '#527878')
    texte(M-1, 90, 'Bourse Eiffel', 34.5, 'SerifB', PAPER)
    enveloppe(c)
    texte(M, 116, 'Master à l’Université Paris-Saclay', 15.6, 'Sans', SAND)
    line(c, M, H-135, W-M, H-135, '#527878')

    texte(M, 158, 'TON PREMIER GESTE', 10.8, 'SansB', GOLD)
    texte(M, 189, 'Avant le 26 novembre 2026', 21.8, 'SerifB', PAPER)
    fin = bloc(201, 'Écris à la **personne responsable** du master que tu as choisi.',
               16.1, 20.3, couleur=PAPER)
    assert fin < 247, 'Le premier geste dépasse du bandeau.'
    fond(M, 247, 42, 3, GOLD)

    titre_etape(283, '01', 'Trouve ses coordonnées')
    x, largeur = M+33, COL-33
    y = bloc(295, 'Choisis ton master dans le catalogue. Sur sa fiche, touche le lien sous le nom de la personne responsable.',
             x=x, largeur=largeur)
    hauteur_cible = 48  # Environ 44 pixels de haut à 360 pixels de large.
    lien(x, y+8, largeur, hauteur_cible, 'Ouvrir le catalogue des masters', CATALOGUE, bouton=True)

    y += 8+hauteur_cible+27
    titre_etape(y, '02', 'Prépare ton message')
    y = bloc(y+11, 'Précise ton niveau d’études, ton université (nom et pays), tes notes, ton classement, tes stages ou emplois et ton projet.',
             x=x, largeur=largeur)
    y += 12
    texte(x+11, y+10, 'UNE QUESTION À AJOUTER', 10, 'SansB', TEAL)
    fin = bloc(y+16, '« Je vise le master [nom]. Quelles pièces dois-je vous envoyer pour la bourse Eiffel ? »',
               13.7, 17.6, x=x+11, largeur=largeur-11)
    fond(x, y, 2.3, fin-y, CLAY)

    y = fin+18
    fond(M, y, COL, 1, LINE)
    texte(M, y+24, 'ENSUITE, C’EST L’UNIVERSITÉ QUI AGIT', 10.6, 'SansB', TEAL)
    fin = bloc(y+32, 'Si Paris-Saclay retient ton dossier, **l’université** l’envoie à Campus France. Elle a jusqu’au **6 janvier 2027 inclus**. Ce délai est le sien, pas le tien.')
    fin = bloc(fin+7, 'Garde la réponse du master. La demande de bourse ne remplace pas ta demande d’admission.',
               13.6, 17.6, couleur=FADE)

    # Zone stable ; pas de renvoi au sommaire d’un livre absent de ce PDF autonome.
    sources_y = 755
    assert fin <= sources_y-8, f'Texte trop proche des sources : {fin:.1f}'
    fond(M, sources_y, COL, 1, LINE)
    texte(M, sources_y+15.5, 'SOURCES  /  VÉRIFIER LES DEUX DATES', 9.8, 'SansB', TEAL)
    lien(M, sources_y+19, 163, hauteur_cible, 'Appel de Paris-Saclay', LIEN_LOCAL)
    lien(M+176, sources_y+19, COL-176, hauteur_cible, 'Calendrier national', LIEN_NATIONAL)
    texte(M, 832, 'MAQUETTE  /  GUIDE INDÉPENDANT', 9, 'SansB', FADE)
    texte(W-M, 832, '01 / 01', 9.6, 'SansB', FADE, True)


def produire():
    memoire = BytesIO()
    c = canvas.Canvas(memoire, pagesize=(W, H), invariant=1, pageCompression=1, lang='fr')
    c.setTitle('Bourse Eiffel · Master à Paris-Saclay — Maquette mobile')
    c.setAuthor('Mon dossier France · guide indépendant')
    composer_page(c)
    c.showPage(); c.save()
    donnees = memoire.getvalue()
    with pymupdf.open(stream=donnees, filetype='pdf') as doc:
        page = doc[0]
        assert len(doc) == 1 and tuple(page.rect) == (0, 0, W, H)
        liens = page.get_links()
        assert len(liens) == 3 and {l['uri'] for l in liens} == {CATALOGUE, LIEN_LOCAL, LIEN_NATIONAL}
        assert all(page.rect.contains(l['from']) and l['from'].height * 360/W >= 44 for l in liens)
        mots = page.get_text('words', clip=pymupdf.INFINITE_RECT())
        assert all(page.rect.contains(pymupdf.Rect(mot[:4])) for mot in mots)
        entete = ' '.join(page.get_text(clip=pymupdf.Rect(0, 0, W, 250)).split())
        assert 'Avant le 26 novembre 2026' in entete and 'personne responsable du master' in entete
        assert '6 janvier 2027' not in entete and '6 janvier 2027' in ' '.join(page.get_text().split())
        pix = page.get_pixmap(matrix=pymupdf.Matrix(2,2), alpha=False)
        mobile = Image.frombytes('RGB', (pix.width,pix.height), pix.samples)
        mobile = mobile.resize((360,round(360*H/W)), Image.Resampling.LANCZOS)
    PDF.write_bytes(donnees)
    mobile.save(IMAGE, optimize=True)
    print(f'{PDF.name} : 1 page, 3 liens ; {IMAGE.name} : {mobile.width} × {mobile.height} px.')


if __name__ == '__main__':
    produire()
