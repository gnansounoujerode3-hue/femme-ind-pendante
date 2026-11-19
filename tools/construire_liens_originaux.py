"""Publier les liens documentés, en distinguant les pistes des images approuvées."""
from pathlib import Path
import csv
import json
import sys
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from construire_guide import load_recipes


def main():
    recipes = load_recipes()
    registry = json.loads((ROOT / 'assets/food/registry.json').read_text())
    previous = {p['recipe_id']: p for p in registry['images']
                if p.get('image_kind') == 'photograph'
                and p.get('status') != 'rejected' and p.get('original_url')}
    data = json.loads((ROOT / 'recherche-photos/liens-originaux-supplementaires.json').read_text())
    new = {p['recipe_id']: p for p in data['candidates']}
    assert len(new) == len(data['candidates']), 'Recette dupliquée'
    assert not (previous.keys() & new.keys()), 'Source précédente écrasée'
    assert set(previous) | set(new) <= set(range(1, 101))
    unresolved = [r for r in recipes if r['number'] not in previous and r['number'] not in new]
    lines = [
        '# Liens de téléchargement des photographies originales', '',
        '## Bilan actualisé — 18 novembre 2026', '',
        f'- **{len(previous) + len(new)} recettes avec un lien vers un fichier original repéré** : {len(previous)} sources précédentes et **{len(new)} nouvelles pistes**.',
        f'- **{len(unresolved)} recettes restent sans fichier original adapté identifié** ; elles sont listées en fin de document avec un lien de recherche, et non un faux lien de téléchargement.',
        '- Aucun fichier image ni PDF modifié. Les originaux ne sont pas hébergés dans le dépôt.',
        '- « Original » désigne le fichier déposé chez la source, pas une garantie HD : certains fichiers sont petits.',
        '- Les nouvelles pistes ont une existence et des dimensions confirmées dans les métadonnées Wikimedia. Elles ne sont **pas validées visuellement**, ni garanties comme photographies réelles plutôt qu’illustrations. Leur authenticité, leur licence et leur correspondance avec la recette restent à contrôler. **Ne pas les intégrer au livre avant ces contrôles ; aucune image IA n’y est autorisée.**',
        '- Les liens « Ouvrir l’original » des nouvelles pistes passent par la redirection officielle Commons vers le fichier original.', '',
        '## 1. Les 15 sources précédemment documentées', '',
        '| Recette | Original | Dimensions annoncées | Source et crédit |',
        '|---|---|---|---|',
    ]
    for recipe in recipes:
        n = recipe['number']
        if n not in previous:
            continue
        p = previous[n]
        dims = ' × '.join(map(str, p.get('original_dimensions', []))) + ' px'
        lines.append(f"| {n:02}. {recipe['title']} | [Télécharger l’original]({p['original_url']}) | {dims} | [Page source]({p['source_page_url']}) — {p['attribution']} |")
    lines += ['', '## 2. Nouvelles pistes — fichiers originaux à vérifier', '',
              'Ces liens sont des **candidats documentaires**, pas une sélection finale de photos. Une variante avec accompagnement ou ingrédients différents est signalée ; elle ne doit pas être présentée comme le résultat exact de la recette.', '',
              '| Recette | Original | Dimensions annoncées | Source et réserve |',
              '|---|---|---|---|']
    for recipe in recipes:
        n = recipe['number']
        if n not in new:
            continue
        p = new[n]
        dims = ' × '.join(map(str, p['original_dimensions'])) + ' px'
        lines.append(f"| {n:02}. {recipe['title']} | [Ouvrir l’original]({p['original_url']}) | {dims} | [Page source]({p['source_page_url']}) — {p['note']} |")
    lines += ['', '## 3. Recettes encore sans original adapté', '',
              '**Les liens ci-dessous ouvrent une recherche, pas une photographie sélectionnée.** Aucun résultat pertinent n’est revendiqué pour ces lignes. Les résultats hors sujet, ingrédients seuls, préparations en cours et plats manifestement incompatibles ont été écartés.', '',
              '| Recette | Recherche à poursuivre |', '|---|---|']
    for r in unresolved:
        query = r['title'] + ' plat terminé photographie'
        url = 'https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=' + quote(query)
        lines.append(f"| {r['number']:02}. {r['title']} | [Chercher une photographie adaptée]({url}) |")
    lines += ['', '## Conditions d’utilisation', '',
              'Consulter la page source pour l’auteur, la licence et l’historique. Un lien vers une image ne vaut pas autorisation de la réutiliser. Les dimensions sont celles annoncées par la source, pas celles des aperçus déjà présents dans le dépôt.', '',
              'Le livre reste à 14 aperçus intégrés et 86 photographies manquantes ; cette liste de liens ne change pas son état de production.', '']
    (ROOT / 'recherche-photos/LIENS-ORIGINAUX.md').write_text('\n'.join(lines))
    output = ROOT / 'recherche-photos/liens-100-recettes.csv'
    fields = ['numero', 'recette', 'statut', 'original', 'source', 'largeur', 'hauteur', 'note']
    with output.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        for r in recipes:
            n = r['number']
            p = previous.get(n) or new.get(n)
            dims = p.get('original_dimensions', ['', '']) if p else ['', '']
            writer.writerow(dict(numero=n, recette=r['title'],
                statut=('Source précédente — publication finale non validée' if n in previous else 'Nouveau fichier candidat — non examiné visuellement') if p else 'Original adapté non identifié',
                original=p['original_url'] if p else '', source=p['source_page_url'] if p else '',
                largeur=dims[0], hauteur=dims[1],
                note=p.get('note', p.get('editorial_note', '')) if p else 'Recherche à poursuivre ; aucun fichier sélectionné.'))
    print(f'{len(previous)} sources précédentes + {len(new)} nouvelles pistes ; {len(unresolved)} recettes sans original adapté.')


if __name__ == '__main__':
    main()
