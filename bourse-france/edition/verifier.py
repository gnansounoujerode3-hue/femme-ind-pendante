"""Contrôles hors ligne du kit livré. Ne teste pas l’ouverture actuelle des appels."""
from zipfile import ZipFile
from xml.etree import ElementTree as ET

import pymupdf
from PIL import Image
from docx import Document
from openpyxl import load_workbook

from commun import GUIDE, PANORAMA, DOCX, XLSX, KIT, VENTE, LIENS, RACINE
from livret import read_pages, GROUPS, RACCOURCIS, EXTRAIT, W, H
from panorama import FICHES, ATELIERS, LECTURES

URLS = {v[1] for v in LIENS.values()}


def texte(page):
    return ' '.join(page.get_text().split())


def verifier_cadre(page):
    assert (page.rect.width, page.rect.height) == (W, H)
    words = page.get_text('words', clip=pymupdf.INFINITE_RECT())
    assert words
    for x0, y0, x1, y1, mot, *_ in words:
        assert x0 >= -1 and y0 >= -1 and x1 <= W+1 and y1 <= H+1, (page.number+1, mot, 'hors cadre')
    for lien in page.get_links():
        assert page.rect.contains(lien['from'])
        if 'uri' in lien:
            assert lien['uri'] in URLS and lien['uri'].startswith('https://'), lien
        else:
            assert 0 <= lien['page'] < len(page.parent)
    for champ in page.widgets():
        assert page.rect.contains(champ.rect) and champ.field_label


def internes(page):
    return [l['page'] for l in page.get_links() if 'page' in l]


def verifier_livret(pdf, articles, sommaire, couverture=None, annuaire=False):
    index = {p['key']:i for i,p in enumerate(articles,2)}
    assert len(index) == len(articles) and len(pdf) == 2 + len(articles) + int(annuaire)
    assert [entree[2] for entree in pdf.get_toc()] == list(range(1,len(pdf)+1))
    assert internes(pdf[0]) == ([index[couverture]] if couverture else [])
    assert internes(pdf[1]) == [index[k] for k in sommaire]
    for i, page in enumerate(pdf):
        verifier_cadre(page)
        if 2 <= i < len(articles) + 2:
            article = articles[i-2]
            cibles = [t.split(' | ',1)[0] for typ,t in article['blocks'] if typ=='jump']
            assert sorted(internes(page)) == sorted([1, *[index[k] for k in cibles]]), (article['key'], 'renvoi')
            urls = {l['uri'] for l in page.get_links() if 'uri' in l}
            assert urls == {LIENS[k][1] for k in article['refs']}, (article['key'], 'sources')
        elif i > 1:
            assert internes(page) == [1]  # annuaire : retour au sommaire
    return index


def essai_formulaire(pdf, numero, quantite, case=False):
    """Modifier, sauvegarder puis rouvrir une copie en mémoire, jamais le livrable."""
    page = pdf[numero]
    champs = list(page.widgets())
    assert len({w.field_name for w in champs}) == len(champs) == quantite
    for i, w in enumerate(champs,1):
        assert w.field_type_string == ('CheckBox' if case else 'Text')
        assert w.field_value in (False,'Off',None,'')
        w.field_value = w.on_state() if case else f'Essai Bénin {i}'
        w.update()
    with pymupdf.open(stream=pdf.tobytes(),filetype='pdf') as relu:
        page = relu[numero]
        for i,w in enumerate(page.widgets(),1):
            assert w.field_value == (w.on_state() if case else f'Essai Bénin {i}')


guide = read_pages()
bonus = read_pages('panorama.md')
with pymupdf.open(GUIDE) as pdf:
    ng = len(pdf)
    index = verifier_livret(pdf,guide,['debut',*[item[0] for item in GROUPS+RACCOURCIS]],'debut',True)
    assert index['debut'] == 2 and index['mots']+1 == 6 and index['aiguillage']+1 == 9
    assert all(k in index for k in ('outils','decisions','courriel','compte','benin','depot','correction','scan','joindre','identite','diplomes','releves','formalites','sensibles','langues','competences','studyplan','preadmission','modeword','tableur','faq'))
    assert '1er décembre 2026' in texte(pdf[index['depot']]) and '15 décembre 2026' in texte(pdf[index['correction']])
    assert all(t in texte(pdf[index['tableur']]) for t in ('C7','150000','300 000','20 000'))
    essai_formulaire(pdf,index['debut'],3)
    essai_formulaire(pdf,index['depart'],6,case=True)
    calendrier = ' '.join(texte(pdf[index[k]]).lower() for k in ('mois1','mois2','mois3'))
    assert all(m in calendrier for m in 'septembre octobre novembre décembre janvier février mars avril mai juin juillet août'.split())

with pymupdf.open(PANORAMA) as pdf:
    nb = len(pdf)
    index = verifier_livret(pdf,bonus,[a[0] for a in [*LECTURES,*FICHES,*ATELIERS]])
    assert len({f[1] for f in FICHES}) == 10
    for k,pays,_,_ in FICHES:
        page = pdf[index[k]]
        assert all(t in texte(page) for t in (pays.upper(),'Qui paie quoi','Où déposer')), pays
        assert any('uri' in l for l in page.get_links())
    essai_formulaire(pdf,index['decision'],9)

with pymupdf.open(VENTE/'Extrait-gratuit.pdf') as pdf:
    ne = len(pdf)
    assert ne == len(EXTRAIT)+1 and internes(pdf[0]) == [1]
    for page in pdf:
        verifier_cadre(page)
    for i,k in enumerate(EXTRAIT,1):
        article = next(p for p in guide if p['key']==k)
        assert article['title'] in texte(pdf[i]) and not internes(pdf[i])
        assert {l['uri'] for l in pdf[i].get_links()} == {LIENS[ref][1] for ref in article['refs']}
    essai_formulaire(pdf,1,3)
with Image.open(VENTE/'Visuel-Chariow.png') as png:
    assert png.size == (1080,1080)
    png.verify()

modeles = [p.text for p in Document(DOCX).paragraphs]
assert sum(t.startswith('GABARIT') for t in modeles) == 8
assert all(any(chaine in t for t in modeles) for chaine in ('Study Plan','préadmission','Copier','Coller','ferme puis rouvre'))
ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
with ZipFile(DOCX) as z:
    xml = ET.fromstring(z.read('word/document.xml'))
    ancres = [e.get('{%s}anchor'%ns['w']) for e in xml.findall('.//w:hyperlink',ns)]
    signets = [e.get('{%s}name'%ns['w']) for e in xml.findall('.//w:bookmarkStart',ns)]
    assert ancres == signets == [f'Modele_{i:02d}' for i in range(1,9)]

w = load_workbook(XLSX,data_only=True)
assert w.sheetnames == ['Mode d’emploi','Pistes','Pièces','Budget','Exemple budget']
ex = w['Exemple budget']
assert [ex[t].value for t in ('C7','C8','G28','H28','G29','G30')] == [100000,80000,450000,250000,350000,70000]
assert [max(0,ex['G28'].value-150000),max(0,ex['H28'].value-150000-ex['C8'].value)] == [300000,20000]
assert all(w['Budget'][c].value in ('',None) for c in ('C4','C7','G29','G30'))
assert w['Pistes']['J5'].value.year == 2027
assert sum(w['Pistes'].cell(r,1).value is not None for r in range(5,45)) == 7
assert sum(w['Pièces'].cell(r,1).value is not None for r in range(5,45)) == 18
for cellule,lieu in [('A5',"'Exemple budget'!C7"),('A9',"'Pistes'!A5"),('A10',"'Pièces'!A5"),('A13',"'Budget'!C4")]:
    assert w.worksheets[0][cellule].hyperlink.location == lieu
w.close()
w = load_workbook(XLSX)
assert all(w[feuille][c].data_type == 'f' for feuille in ('Budget','Exemple budget') for c in ('A10','G28','H28','G29','G30'))
assert w['Pièces'].freeze_panes == 'B5'
w.close()

fiche = (VENTE/'Fiche-Chariow.md').read_text(encoding='utf-8')
lisez = (RACINE/'README.md').read_text(encoding='utf-8')
for t in (f'{ng} pages',f'{nb} pages',f'{ne} pages','5 000 FCFA'):
    assert t in fiche and t in lisez,t
assert all(t in fiche for t in ('Acheter maintenant','huit modèles','cinq onglets','clos'))
for arch,paths in [(KIT,[GUIDE,PANORAMA,DOCX,XLSX]),(VENTE/'Ressources-Chariow.zip',[VENTE/n for n in ('Fiche-Chariow.md','Visuel-Chariow.png','Extrait-gratuit.pdf')])]:
    with ZipFile(arch) as z:
        assert z.testzip() is None and sorted(z.namelist()) == sorted(p.name for p in paths)
        assert all(z.read(p.name) == p.read_bytes() for p in paths)
print(f'OK : guide {ng} p. (3 réponses + 6 coches), Top 10 {nb} p. (10 pays, 9 champs), extrait {ne} p., navigation, sources, visuel, 8 modèles Word, 5 feuilles Excel et deux archives.')
