# Copie personnelle illustrée — Terre de fête

## Fichier remis dans la conversation

`EBOOK-100-RECETTES-TERRE-DE-FETE-PERSONNEL.pdf` : **240 pages, 100 photographies illustratives, 100 recettes**, environ **18,6 Mo**.

- Les 100 pages photo précèdent immédiatement leur fiche recette.
- Couverture et design validés conservés.
- Ajout de 86 images aux 14 aperçus précédents, dans une copie séparée.
- Photos sélectionnées visuellement ; aucune génération d’image par IA utilisée. Résultats hors sujet et images suspectes écartés.
- Différences de composition, de cuisson et accompagnements explicités sous les nouvelles images : il ne s’agit pas de résultats exacts de recettes testées pour ce livre.
- Images de définition variable. Les dimensions **réellement acquises**, et non les dimensions annoncées des originaux distants, figurent dans le [tableau des sources](recherche-photos/SOURCES-COPIE-PERSONNELLE.csv).
- Mise à l’échelle proportionnelle sans recadrage intérieur ; crédits et marques présents dans les images conservés. Compression JPEG et réduction éventuelle à 1 800 pixels par côté pour alléger la lecture écran, sans agrandissement artificiel des fichiers.

## Séparation entre copie personnelle et dépôt public

La demande porte sur un usage personnel. Les droits de republication des nouvelles images ne sont pas validés : le **PDF personnel, son registre local et les images tierces ne sont pas ajoutés au dépôt GitHub public**. Ils sont disponibles dans l’espace de travail et le PDF a vocation à être remis dans la conversation.

GitHub contient le générateur, le tableau de sources et les rapports techniques, mais pas cette copie personnelle. Le PDF public de travail garde son statut antérieur (14 aperçus, 86 images absentes) ; il n’est pas remplacé silencieusement par la copie personnelle. Le registre public n’est pas marqué « approuvé ».

## Contrôles

- 100 fiches complètes et 100 pages photo repérées.
- Une page photo immédiatement avant chaque fiche ; 100 images distinctes selon leurs empreintes de fichiers.
- 100 liens internes valides ; lien source présent sur chacune des 100 pages photo.
- Polices utilisées incorporées ; pas de page quasi vide ni de texte hors des limites.
- 100 pages photo examinées sur cinq planches ; remplacement d’une photo de pintade non terminée et d’un résultat « shiro » montrant des ingrédients. Photo du wagassi récupérée dans une meilleure définition.
- Export personnel optimisé d’environ 18,6 Mo, après remplacement d’un premier export non optimisé de 296 Mo.
- Le mode `--personal` ne permet pas de contourner le contrôle de l’édition finale : `--personal --final` est refusé.
- [Rapport technique](reports/edition-personnelle/validation.json) et [contrôle des images](reports/edition-personnelle/controle-images.json).

## Reproduction locale

Les images et le manifeste local sont nécessaires : ils ne sont volontairement pas publiés sur GitHub. Dans cet espace de travail :

```bash
.venv/bin/python tools/construire_ebook_complet.py --personal
.venv/bin/python tools/verifier_ebook_complet.py \
  --pdf EBOOK-100-RECETTES-TERRE-DE-FETE-PERSONNEL.pdf \
  --report-dir personnel/rapports --require-photos
```

Le générateur lit les aperçus existants du registre public, puis `personnel/manifest.json`. L’option `--manifest chemin/registre.json` permet de préciser un autre manifeste local, uniquement avec `--personal`.

Chaque entrée de `images` contient `recipe_id`, `local_path`, `source_page_url`, `attribution`, `caption`, `status: personal_only` et `image_kind: photograph`. Un numéro dupliqué, invalide ou une image absente entraîne une erreur. Ce manifeste sert uniquement à une copie personnelle et ne vaut pas validation pour la vente ou la diffusion.
