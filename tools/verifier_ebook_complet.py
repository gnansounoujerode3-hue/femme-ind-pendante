"""Vérifications reproductibles du PDF intégral, sans prétendre valider sa qualité culinaire."""
from pathlib import Path
import argparse,json,re,sys
import pymupdf
ROOT=Path(__file__).resolve().parents[1]

def main(path=None, report_dir=None, require_photos=False):
    path=Path(path) if path else ROOT/'EBOOK-100-RECETTES-TERRE-DE-FETE-TRAVAIL.pdf'
    doc=pymupdf.open(path)
    photo_pages,recipe_pages={},{}
    empty,outside,issues=[],[],[]
    internal_links=0
    for index,page in enumerate(doc):
        text=page.get_text()
        if len(text.strip())<80:empty.append(index+1)
        match=re.search(r'RECETTE (\d+)([^\n]*)',text)
        if match:
            number=int(match.group(1))
            target=photo_pages if 'LE PLAT EN IMAGE' in text else recipe_pages
            if number in target:issues.append(f'Numéro dupliqué : {number}')
            target[number]=index+1
            if target is recipe_pages:
                for label in ('Les ingrédients','À vous de jouer','LE PETIT CONSEIL','01.','02.','03.','04.'):
                    if label not in text:issues.append(f'Section absente, fiche {number} : {label}')
        for block in page.get_text('blocks'):
            if block[0]<-1 or block[1]<-1 or block[2]>page.rect.width+1 or block[3]>page.rect.height+1:
                outside.append(index+1)
        for link in page.get_links():
            if link['kind']==pymupdf.LINK_GOTO:
                internal_links+=1
                if not 0<=link.get('page',-1)<len(doc):issues.append(f'Lien interne invalide p.{index+1}')
    if sorted(photo_pages)!=list(range(1,101)):issues.append('100 pages photo non retrouvées')
    if sorted(recipe_pages)!=list(range(1,101)):issues.append('100 fiches non retrouvées')
    for number,page in photo_pages.items():
        if recipe_pages.get(number)!=page+1:issues.append(f'Ordre photo/recette incorrect : {number}')
    if empty:issues.append(f'Pages quasi vides : {empty}')
    if outside:issues.append(f'Texte hors page : {outside}')
    actual_photos=sum(bool(doc[page-1].get_images()) for page in photo_pages.values())
    if require_photos and actual_photos!=100:
        issues.append(f'100 photos exigées, {actual_photos} trouvées')
    for number,page in photo_pages.items():
        if doc[page-1].get_images() and not any(link.get('uri','').startswith('https://') or link.get('uri','').startswith('http://') for link in doc[page-1].get_links()):
            issues.append(f'Lien source absent, photo {number}')
    # ReportLab déclare parfois Helvetica sans l’utiliser : contrôler les polices réellement dessinées.
    used_fonts={span['font'] for page in doc for block in page.get_text('dict')['blocks']
                if 'lines' in block for line in block['lines'] for span in line['spans']}
    resources={font[3].split('+')[-1]:font[0] for page in doc for font in page.get_fonts()}
    embedded=all(name in resources and bool(doc.extract_font(resources[name])[3]) for name in used_fonts)
    if not embedded:issues.append('Police non incorporée')
    if internal_links<100:issues.append('Moins de 100 liens internes')
    result=dict(file=path.name,pages=len(doc),recipe_count=len(recipe_pages),photo_slot_count=len(photo_pages),
                actual_preview_photos=actual_photos,missing_photos=100-actual_photos,
                internal_links=internal_links,all_fonts_embedded=embedded,empty_pages=empty,
                text_out_of_bounds=outside,errors=issues,publication_ready=False,
                visual_review='Maquette initiale inspectée ; nouvelles photos examinées sur planches puis pages mises en page contrôlées séparément.',
                limits=[f'{100-actual_photos} photographies manquantes',f'{actual_photos} aperçus basse définition non validés pour publication finale','Recettes non testées en cuisine','Pas de validation imprimeur ou PDF/UA'])
    folder=Path(report_dir) if report_dir else ROOT/'reports/ebook-complet'
    folder.mkdir(exist_ok=True,parents=True)
    (folder/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 1 if issues else 0

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--pdf')
    parser.add_argument('--report-dir')
    parser.add_argument('--require-photos',action='store_true')
    args=parser.parse_args()
    sys.exit(main(args.pdf,args.report_dir,args.require_photos))
