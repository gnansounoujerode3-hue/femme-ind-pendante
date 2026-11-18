"""Consigne uniquement les sources effectivement consultées dans cette session."""
from pathlib import Path
import sys, json, shutil
from urllib.parse import quote
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from construire_guide import load_recipes
DATE='2026-11-18'
BASE='https://commons.wikimedia.org/wiki/'
# id, source observée, statut de la correspondance — une catégorie n'est pas une licence.
SOURCES=[
(1,'File:Pastels.jpg','Beignets au poisson ; vérifier dressage, farce et fichier original.'),
(2,'File:Akara_balls.jpg','Bonne famille de plat ; vérifier texture et photographie en grand.'),
(3,'Category:Alloco','Choisir une photo du plantain seul, sans accompagnements non prévus.'),
(4,'File:Kelewele,_a_Ghanaian_snack.jpg','Photo réelle vue : bananes en tranches, plus foncées que notre présentation en dés ; qualité éditoriale à revoir.'),
(11,'File:Amiwô_accompagné_de_la_viande_de_poulet.jpg','Photo réelle vue : amiwo accompagné de poulet ; légender cet accompagnement, non inclus dans la fiche 11 seule.'),
(12,'https://fr.wikipedia.org/wiki/Atassi','Article repéré ; rechercher la page du fichier et sa licence. Pas encore de fichier sélectionné.'),
(13,'File:Waagashi.jpg','Fromage comme ingrédient, pas wagassi en sauce tomate : ne pas utiliser comme résultat final.'),
(18,'File:Ablo.jpg','La source décrit des ablos de maïs ; notre adaptation contient du riz et du maïs. À signaler comme variante.'),
(19,'Category:Akassa','Page de désambiguïsation repérée ; ouvrir la catégorie du plat. Aucun fichier choisi.'),
(22,'File:Yassapoulet.JPG','Photo réelle vue : poulet aux oignons et riz à côté ; présentation familiale, qualité éditoriale à revoir.'),
(24,'File:Kedjenou.JPG','Source décrit un kedjenou de poulet ; vérifier la photo et sa résolution finale.'),
(25,'File:Poulet_DG.JPG','Candidate du bon plat ; licence et correspondance détaillée à contrôler.'),
(31,'Category:Maafe','Plusieurs variantes ; choisir un mafé de bœuf, pas de poisson.'),
(33,'Category:Suya','Choisir bœuf en brochettes, sans confondre morceaux grillés et abats.'),
(39,'Category:Bobotie','Choisir le plat terminé avec couverture aux œufs, pas la farce crue.'),
(44,'File:Thieboudienne.JPG','Fichier du plat repéré ; comparer légumes et couleur avec notre adaptation.'),
(52,'File:Jollof_rice.jpg','Fichier de riz jollof repéré ; vérifier les garnitures visibles.'),
(53,'Category:Waakye','Attention : notre version sans feuilles de sorgho est moins colorée. Ne pas présenter un résultat identique garanti.'),
(61,'Category:Red_red','Écarter les versions avec poisson ou poulet pour notre recette végétale.'),
(63,'Category:Moin_moin','Écarter les pièces avec poisson ou œuf visibles, absents de notre version.'),
(67,'Category:Chakalaka','Choisir légumes terminés ; vérifier que les haricots sont cohérents.'),
(81,'File:Du_dêguê.jpg','La source décrit lait caillé et semoule de mil, pas exactement notre yaourt vanillé : variante à légender.'),
(82,'Category:Chakery','La coco doit correspondre à la variante ; aucune photo exacte sélectionnée.'),
(84,'Category:Nourriture_terrestre_LSP','Une photo de pause au yovo doko a été repérée ; risque de scène de groupe, chercher un gros plan du plat.'),
(85,'Category:Mandazi','Choisir des pièces triangulaires finies et vérifier variante coco.'),
(86,'Category:Chin_chin','Ne pas sélectionner le fichier Unfried chin chin, qui montre un produit cru.'),
(88,'File:Malva_Pudding.jpg','Fichier du dessert terminé repéré ; droits et dressage à vérifier.'),
(91,'Category:Bissap','Choisir un verre de boisson rouge terminée, pas les fleurs sèches ni une bouteille de sirop.'),
(95,'File:Baobab_juice_-_final_straining_with_sieve.jpg','Photo d’étape de filtration, non du service final : impropre à la page résultat, chercher mieux.')
]
VERIFIED={
4:dict(author='Maame1Yaa',license='CC0 1.0',license_url='https://creativecommons.org/publicdomain/zero/1.0/',width=2160,height=3840,original='https://upload.wikimedia.org/wikipedia/commons/a/ac/Kelewele%2C_a_Ghanaian_snack.jpg',preview='image-search/kelewele-a-ghanaian-snack-maame1yaa-1.jpg'),
11:dict(author='Aimeabibis',license='CC BY-SA 4.0',license_url='https://creativecommons.org/licenses/by-sa/4.0/',width=4608,height=3456,original='https://upload.wikimedia.org/wikipedia/commons/2/28/Amiw%C3%B4_accompagn%C3%A9_de_la_viande_de_poulet.jpg',preview='image-search/amiw-accompagn-de-la-viande-de-poulet-1.jpg'),
18:dict(author='Rayman3640',license='CC BY-SA 3.0 (parmi les licences proposées)',license_url='https://creativecommons.org/licenses/by-sa/3.0/',width=3072,height=2304,original='https://upload.wikimedia.org/wikipedia/commons/7/70/Ablo.jpg',preview='image-search/ablo-wikimedia-commons-2.jpg'),
22:dict(author='KVDP',license='Domaine public, cession par l’auteur',license_url='https://commons.wikimedia.org/wiki/File:Yassapoulet.JPG#Licensing',width=2816,height=2112,original='https://upload.wikimedia.org/wikipedia/commons/f/fc/Yassapoulet.JPG',preview='image-search/yassapoulet-jpg-1.jpg'),
81:dict(author='BeraDigle',license='CC BY-SA 4.0',license_url='https://creativecommons.org/licenses/by-sa/4.0/',width=3024,height=4032,original='https://upload.wikimedia.org/wikipedia/commons/d/d5/Du_d%C3%AAgu%C3%AA.jpg',preview=None)
}

def main():
    records={}
    for n,source,note in SOURCES:
        url=source if source.startswith('https:') else BASE+quote(source,safe=':_(),')
        records[n]=dict(source_page_url=url,note=note)
    registry_path=ROOT/'assets/food/registry.json'
    registry=json.loads(registry_path.read_text())
    for entry in registry['images']:
        if entry.get('id')=='table-festive-ia-01':
            entry['status']='rejected'
            entry['usage']='Exclue par demande explicite : aucune image générée par IA autorisée dans les prochaines éditions.'
    registry['images']=[e for e in registry['images'] if not str(e.get('id','')).startswith('photo-recherche-')]
    rows=[]
    for recipe in load_recipes():
        n=recipe['number']
        row=dict(recipe_id=n,title=recipe['title'],search_query=f"{recipe['title']} photographie réelle plat terminé licence commerciale",status='not_searched',source_page_url=None,note='Recherche à effectuer ; aucune photo trouvée n’est revendiquée.')
        if n in records:
            row.update(records[n]);row['status']='source_identified'
        if n in VERIFIED:
            d=VERIFIED[n]
            row.update({k:v for k,v in d.items() if k!='preview'})
            row['status']='license_read_visual_pending'
            row['local_preview']=None
            if d['preview'] and (ROOT/d['preview']).exists():
                dest=ROOT/f'assets/food/previews/recette-{n:03}.jpg'
                dest.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(ROOT/d['preview'],dest)
                row['local_preview']=str(dest.relative_to(ROOT))
            registry['images'].append(dict(id=f'photo-recherche-{n:03}',recipe_id=n,
                local_path=row['local_preview'],source_page_url=row['source_page_url'],original_url=d['original'],
                author=d['author'],license=d['license'],license_evidence=row['source_page_url']+'#Licensing',
                license_url=d['license_url'],verified_on=DATE,attribution=f"{d['author']} — {d['license']} — Wikimedia Commons",
                commercial_use=True,modifications_allowed=True,modifications='Aucune retouche ; miniature du moteur de recherche pour revue uniquement si disponible.',
                status='pending',image_kind='photograph',usage='Candidate de recherche seulement ; télécharger et contrôler l’original avant mise en page.',
                original_dimensions=[d['width'],d['height']],editorial_note=row['note']))
        rows.append(row)
    registry['description']='Photographies uniquement pour les futures éditions. Illustration IA exclue. Cinq pages de licence consultées, aucune photo approuvée pour publication finale.'
    registry_path.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
    out=ROOT/'recherche-photos';out.mkdir(exist_ok=True)
    (out/'suivi-100-recettes.json').write_text(json.dumps(dict(date=DATE,policy='Photographies réelles uniquement. Une page photo avant chaque recette.',recipes=rows),ensure_ascii=False,indent=2)+'\n')
    lines=['# Recherche de photographies réelles — premier lot',
           '\n## État réel du travail\n',
           f'- **100 recettes suivies ; {len(SOURCES)} pistes de sources repérées.** Une piste peut être une catégorie, un ingrédient ou une photo à écarter : ce ne sont pas 29 photos sélectionnées.',
           '- **5 pages de fichier et leurs licences consultées**, 4 miniatures récupérées pour examen. Les originaux haute définition ne sont pas encore téléchargés.',
           '- **0 photo approuvée pour le livre final** : adéquation exacte, qualité, cadrage et crédits définitifs restent à valider.',
           f'- **{100-len(SOURCES)} recettes restent sans recherche effectuée** dans ce lot. Aucun résultat n’est inventé pour compléter la liste.',
           '- Aucune nouvelle image IA produite. L’ancienne illustration est exclue des prochaines éditions ; l’ancienne maquette reste un historique obsolète, pas le futur livre.',
           '\n## Cinq candidates avec licence consultée\n',
           'Les licences CC BY-SA permettent la réutilisation sous obligations, notamment attribution et partage des adaptations de l’image sous licence identique ou compatible. Cela ne dispense pas de vérifier les autres droits éventuels. Les images illustrent une variante du plat, pas une recette testée pour ce livre.\n']
    for row in rows:
        n=row['recipe_id']
        if n not in VERIFIED:continue
        lines.extend([f"### {n}. {row['title']}",f"- [Page source et conditions]({row['source_page_url']})",f"- Auteur : **{row['author']}**. Licence affichée : **{row['license']}**.",f"- [Original à télécharger]({row['original']}) : {row['width']} × {row['height']} pixels.",f"- Contrôle éditorial : {row['note']}"])
        if row['local_preview']:
            lines.append(f"- [Miniature de travail](../{row['local_preview']}) — non destinée à la pleine page.")
        lines.append('')
    lines.extend(['## Suivi des 100 recettes\n','| N° | Recette | Avancement et source | Point de vigilance |','|---:|---|---|---|'])
    for row in rows:
        status={'not_searched':'À rechercher','source_identified':'Piste, non validée','license_read_visual_pending':'Licence lue, sélection en attente'}[row['status']]
        if row['source_page_url']:status=f"[{status}]({row['source_page_url']})"
        lines.append(f"| {row['recipe_id']} | {row['title']} | {status} | {row['note']} |")
    lines.extend(['\n## Avant publication\n','1. Trouver une photographie du résultat terminé, pas d’une étape ou d’un ingrédient seul.',
                  '2. Vérifier qu’elle représente la variante décrite, sans ingrédients supplémentaires trompeurs.',
                  '3. Télécharger l’original haute définition et l’examiner en grand ; ne pas agrandir artificiellement une miniature.',
                  '4. Archiver source, auteur, licence et modifications, puis préparer les crédits.',
                  '5. Mettre la grande photo et sa légende sur une page distincte, immédiatement avant la recette.',
                  '6. N’acheter aucune image sans accord. Ne pas utiliser les photos de blogs sans permission ou licence explicite.'])
    (out/'SELECTION-PHOTOS-REELLES.md').write_text('\n'.join(lines)+'\n')
    print(f'{len(rows)} recettes suivies ; {len(SOURCES)} pistes ; {len(VERIFIED)} licences lues.')

if __name__=='__main__':main()
