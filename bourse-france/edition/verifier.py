"""Contrôles hors ligne des fichiers livrés, pas de l’ouverture actuelle des appels."""
from zipfile import ZipFile
from PIL import Image
from docx import Document
from openpyxl import load_workbook
import pymupdf
from commun import GUIDE, PANORAMA, DOCX, XLSX, KIT, VENTE, LIENS
from livret import read_pages, GROUPS, RACCOURCIS, W, H
from panorama import FICHES, ATELIERS

URLS = {v[1] for v in LIENS.values()}

def texte(page):
    return ' '.join(page.get_text().split())


def verifier_pages(pdf, articles, raccourcis, annuaire=False):
    """Texte visible, signets, index cliquable, retours et références des manuscrits."""
    assert len(pdf) == 2 + len(articles) + int(annuaire)
    assert [entree[2] for entree in pdf.get_toc()] == list(range(1,len(pdf)+1))
    indices = {p['key']:i for i,p in enumerate(articles,2)}
    assert [l['page'] for l in pdf[1].get_links()] == [indices[k] for k in raccourcis]
    for i,page in enumerate(pdf):
        assert (page.rect.width,page.rect.height)==(W,H)
        words=page.get_text('words'); assert words
        assert all(x0>=-1 and y0>=-1 and x1<=W+1 and y1<=H+1 for x0,y0,x1,y1,*_ in words), (i,'texte hors cadre')
        for l in page.get_links():
            assert page.rect.contains(l['from']), (i,'lien hors cadre')
            if 'uri' in l:
                assert l['uri'] in URLS and l['uri'].startswith('https://')
            else:
                assert 0 <= l['page'] < len(pdf)
                if i>1: assert l['page']==1  # retour au sommaire, même pour l’annuaire
        if i>=2:
            assert any(l.get('page')==1 for l in page.get_links())
        if 2<=i<2+len(articles):
            p=articles[i-2]; urls={l.get('uri') for l in page.get_links() if 'uri' in l}
            assert urls=={LIENS[k][1] for k in p['refs']}, (p['key'],'sources manquantes')
    return indices


guide=read_pages(); panorama=read_pages('panorama.md')
with pymupdf.open(GUIDE) as pdf:
    index=verifier_pages(pdf,guide,[item[0] for item in GROUPS+RACCOURCIS],annuaire=True)
    assert len(pdf)==40 and '1er décembre' in texte(pdf[index['benin']])
    assert all(k in index for k in ['identite','diplomes','releves','formalites','sensibles','langues','competences','studyplan','preadmission','depart','faq'])
    page=pdf[index['depart']]; cases=list(page.widgets()); assert len(cases)==6
    for case in cases:
        assert case.field_type_string=='CheckBox' and case.field_value in (False,'Off',None)
        case.field_value=case.on_state(); case.update()
    with pymupdf.open(stream=pdf.tobytes(),filetype='pdf') as essai:
        relu=essai[index['depart']]; assert all(w.field_value==w.on_state() for w in relu.widgets())
    calendrier=' '.join(texte(pdf[index[k]]).lower() for k in ('mois1','mois2','mois3'))
    assert all(mois in calendrier for mois in 'septembre octobre novembre décembre janvier février mars avril mai juin juillet août'.split())

with pymupdf.open(PANORAMA) as pdf:
    index=verifier_pages(pdf,panorama,['orientation',*[f[0] for f in FICHES],*[a[0] for a in ATELIERS]])
    assert len(pdf)==17 and len({f[1] for f in FICHES})==10
    for k,pays,_,_ in FICHES:
        page=pdf[index[k]]; contenu=texte(page)
        assert pays.upper() in contenu and 'Qui paie quoi' in contenu and 'Où déposer' in contenu
        assert any(l.get('uri') for l in page.get_links()), (pays,'aucune source officielle')
    # Saisie, sauvegarde et relecture en mémoire uniquement ; le livrable reste vierge.
    page=pdf[-1]; champs=list(page.widgets()); assert len(champs)==9
    assert len({w.field_name for w in champs})==len(champs)
    for i,w in enumerate(champs):
        assert w.field_type_string=='Text' and not w.field_value and page.rect.contains(w.rect)
        w.field_value=f'Essai Bénin {i+1}'; w.update()
    with pymupdf.open(stream=pdf.tobytes(),filetype='pdf') as essai:
        relu=essai[-1]; assert [w.field_value for w in relu.widgets()]==[f'Essai Bénin {i+1}' for i in range(9)]

with pymupdf.open(VENTE/'Extrait-gratuit.pdf') as pdf:
    assert len(pdf)==3 and 'Quels bulletins' in texte(pdf[1]) and '350 000' in texte(pdf[2])
    assert all(l.get('uri') in URLS for page in pdf for l in page.get_links())
with Image.open(VENTE/'Visuel-Chariow.png') as png:
    assert png.size==(1080,1080); png.verify()
modeles=[p.text for p in Document(DOCX).paragraphs]
assert sum(t.startswith('GABARIT') for t in modeles)==8
assert any('Study Plan' in t for t in modeles) and any('préadmission' in t for t in modeles)

w=load_workbook(XLSX,data_only=True); assert len(w.sheetnames)==5
ex=w['Exemple budget']; assert [ex[t].value for t in ('G28','H28','G29','G30')]==[450000,250000,350000,70000]
assert w['Budget']['G29'].value in ('',None) and w['Pistes']['J5'].value.year==2027
assert sum(w['Pistes'].cell(r,1).value is not None for r in range(5,45))==7
assert sum(w['Pièces'].cell(r,1).value is not None for r in range(5,45))==18
w.close()
w=load_workbook(XLSX); assert w['Budget']['G29'].data_type=='f' and w['Pièces'].freeze_panes=='B5'; w.close()

fiche=(VENTE/'Fiche-Chariow.md').read_text(encoding='utf-8')
assert all(t in fiche for t in ('40 pages','17 pages','5 000 FCFA','Acheter maintenant','huit modèles','cinq onglets'))
for arch,paths in [(KIT,[GUIDE,PANORAMA,DOCX,XLSX]),(VENTE/'Ressources-Chariow.zip',[VENTE/n for n in ('Fiche-Chariow.md','Visuel-Chariow.png','Extrait-gratuit.pdf')])]:
    with ZipFile(arch) as z:
        assert z.testzip() is None and sorted(z.namelist())==sorted(p.name for p in paths)
        assert all(z.read(p.name)==p.read_bytes() for p in paths)
print('OK : guide (40 p.), Top 10 (10 pays, 17 p., 9 champs testés), navigation et sources, extrait, image, 8 gabarits, tableur et deux ZIP.')
