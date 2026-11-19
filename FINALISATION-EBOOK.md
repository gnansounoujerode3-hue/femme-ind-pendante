# Finalisation — Terre de fête

## Réalisé

- Direction graphique validée conservée : couverture photographique, crème, vert et terre cuite, Crimson Pro et Instrument Sans.
- Mise en page des **100 recettes**, numérotées sans doublon.
- **100 pages photo**, chacune située immédiatement avant sa fiche recette.
- Sommaire cliquable, signets PDF et dix ouvertures de chapitre.
- Introduction, vocabulaire, mesures, hygiène, menus, liste de courses, rétroplanning et dépannage.
- Crédits des aperçus photographiques, texte sélectionnable et polices embarquées.
- PDF de travail : **228 pages**.

## Point bloquant : les photographies

**Ce n’est pas une version prête à vendre.** Quatorze aperçus de travail sont intégrés pour les recettes 2, 4, 11, 18, 20, 22, 24, 25, 39, 44, 52, 68, 85 et 88. Les **86 autres pages photo** portent la mention « Photographie réelle à intégrer ». Tous les aperçus doivent encore être remplacés par des originaux de définition adaptée et validés pour l’édition finale.

Le deuxième lot ajoute dix photographies réelles, avec légendes de variantes et crédits. L’accès direct aux originaux Wikimedia est bloqué dans cet environnement ; les fichiers intégrés restent des miniatures. Voir le [bilan du lot 2](recherche-photos/LOT-2-PHOTOS.md). Le suivi JSON du premier lot est une archive de recherche, pas le bilan actuel du livre.

La couverture reprend une photo réelle provisoire, sans modification de son design. Aucune image IA n’est utilisée dans ce nouveau document. Aucune photographie de substitution trompeuse n’est insérée.

## Contrôles effectués

- 100 fiches et 100 pages photographiques repérées dans le PDF.
- Pour chaque numéro, page recette = page photo + 1.
- Les ingrédients, les étapes et le conseil sont présents sur chacune des 100 fiches.
- Pas de page vide ni de bloc de texte hors de la page dans l’extraction technique.
- 228 pages rendues sous forme de sept planches ; les dix nouvelles pages photo ont été inspectées après intégration. Les fiches longues, la couverture et les crédits avaient été examinés dans la précédente version.
- L’export `--final` est bloqué tant que les 100 recettes n’ont pas une photographie explicitement approuvée et déclarée prête à publier dans le registre.
- Le contrôle automatisé ne certifie ni une conformité PDF/UA ou imprimeur ni la réussite culinaire des recettes. Pas d’essai sur liseuse ou de test d’impression effectué.

## Reproduire

```bash
python -m venv .venv
.venv/bin/pip install -r requirements-editorial.txt
.venv/bin/python tools/construire_ebook_complet.py
.venv/bin/python tools/verifier_ebook_complet.py
```

Pour l’export final, après acquisition, contrôle et validation de toutes les photographies :

```bash
.venv/bin/python tools/construire_ebook_complet.py --final
```

La validation se fait par `status: approved` et `publication_ready: true` sur chaque entrée photographique du registre. Ne jamais attribuer ces valeurs automatiquement à des images non examinées. Les recettes restent non testées dans le cadre de ce projet : une relecture humaine et des essais culinaires sont recommandés avant commercialisation.

## Prochain travail nécessaire

1. Poursuivre la recherche des photographies encore absentes.
2. Obtenir les originaux, examiner la définition et la correspondance exacte du plat et de sa variante.
3. Compléter les crédits et le registre de provenance.
4. Régénérer le livre sans emplacement manquant et contrôler chaque nouvelle page photo.
5. Relire le contenu et tester les recettes, puis préparer le fichier destiné aux clients.
