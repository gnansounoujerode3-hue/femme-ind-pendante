"""Contrôles hors ligne après génération. N’atteste pas que les appels sont encore ouverts."""
from zipfile import ZipFile
from PIL import Image
from docx import Document
from openpyxl import load_workbook
import pymupdf
from commun import GUIDE, DOCX, XLSX, KIT, VENTE, LIENS
from livret import read_pages, GROUPS

pages = read_pages(); valid_urls={v[1] for v in LIENS.values()}
with pymupdf.open(GUIDE) as pdf:
    assert len(pdf)==len(pages)+3 and len(pdf.get_toc())==len(pdf)
    toc_pages={k:i for i,p in enumerate(pages,2) for k in [p['key']]}
    assert [l['page'] for l in pdf[1].get_links()] == [toc_pages[k] for k,_,_ in GROUPS]
    for i,page in enumerate(pdf):
        assert all(w[0]>=-1 and w[1]>=-1 and w[2]<=page.rect.width+1 and w[3]<=page.rect.height+1 for w in page.get_text('words'))
        for l in page.get_links():
            if 'uri' in l:assert l['uri'] in valid_urls
        if 2<=i<len(pdf)-1:
            urls={l.get('uri') for l in page.get_links()};assert all(LIENS[k][1] in urls for k in pages[i-2]['refs'])
    assert '1er décembre' in pdf[toc_pages['benin']].get_text().replace('\xa0',' ')
with pymupdf.open(VENTE/'Extrait-gratuit.pdf') as pdf:
    assert len(pdf)==3 and all(l.get('uri') in valid_urls for page in pdf for l in page.get_links())
with Image.open(VENTE/'Visuel-Chariow.png') as png: assert png.size==(1080,1080)
assert sum(p.text.startswith('GABARIT') for p in Document(DOCX).paragraphs)==8
w=load_workbook(XLSX,data_only=True);assert len(w.sheetnames)==5
ex=w['Exemple budget'];assert [ex[t].value for t in ('G28','H28','G29','G30')]==[450000,250000,350000,70000]
assert w['Budget']['G29'].value in ('',None) and w['Pistes']['J5'].value.year==2027;w.close()
w=load_workbook(XLSX);assert w['Budget']['G29'].data_type=='f' and w['Pièces'].freeze_panes=='B5';w.close()
for arch,paths in [(KIT,[GUIDE,DOCX,XLSX]),(VENTE/'Ressources-Chariow.zip',[VENTE/n for n in ('Fiche-Chariow.md','Visuel-Chariow.png','Extrait-gratuit.pdf')])]:
    with ZipFile(arch) as z:
        assert z.testzip() is None and sorted(z.namelist())==sorted(p.name for p in paths)
        assert all(z.read(p.name)==p.read_bytes() for p in paths)
print('OK : guide, sommaire, liens, mise en page, extrait, image, huit modèles, tableur et archives.')
