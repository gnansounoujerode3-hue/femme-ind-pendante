# Terre de fête — copie personnelle illustrée reconstruite

## Télécharger

**[Ouvrir le PDF (240 pages)](EBOOK-100-RECETTES-TERRE-DE-FETE-PERSONNEL.pdf)**

**[Télécharger directement sur GitHub](https://github.com/gnansounoujerode3-hue/femme-ind-pendante/raw/refs/heads/arena/f365f470-femme-ind-pendante/EBOOK-100-RECETTES-TERRE-DE-FETE-PERSONNEL.pdf)**

100 recettes, 100 photographies distinctes, chaque page photo immédiatement avant sa fiche. Design validé conservé, y compris la couverture photographique. La taille et l’empreinte exacte figurent dans le [contrôle des images](reports/edition-personnelle/controle-images.json).

## Pourquoi une reconstruction ?

Le précédent PDF personnel et les 86 nouveaux fichiers image étaient exclus de Git et n’ont pas survécu à la restauration de l’espace de travail. Le lien donné auparavant n’était plus utilisable et le client n’a pas pu télécharger le fichier.

Les recettes, le générateur, les 14 photos historiques et le tableau de sources avaient été conservés. Ils ont servi à reconstruire cette copie ; les 86 photographies supplémentaires ont été recherchées et récupérées à nouveau. Certaines sélections et légendes ont donc changé. Ce n’est pas une restauration à l’identique de l’ancien fichier.

À la demande explicite du client de mettre le PDF sur GitHub, **le PDF reconstruit et les images sélectionnées sont cette fois archivés dans la branche de travail**, avec le manifeste `assets/food/personnel/manifest.json`. Les fichiers de recherche rejetés et les planches intermédiaires restent exclus. Le PDF public de travail n’a pas été remplacé.

## Statut éditorial

- Aucune image générée avec un outil d’IA pour le livre ; sélection visuelle de photographies trouvées sur les sources citées. Ce contrôle ne certifie pas la provenance de chaque fichier tiers.
- Illustrations de variantes, pas des résultats de recettes testées pour le livre. Accompagnements et différences signalés en légende.
- Définition variable, parfois très faible. Copie écran, pas un export haute définition pour impression.
- Crédits et filigranes présents conservés. Images mises à l’échelle proportionnellement, sans retouche générative ; réduction éventuelle à 1 800 pixels et JPEG pour limiter le poids.
- Les droits de republication des nouvelles images **ne sont pas validés** ; leur présence dans cette archive demandée par le client ne leur confère aucune licence libre et ne constitue pas une autorisation de vente.
- Recettes non testées en cuisine dans le cadre de ce projet. Pas de validation imprimeur ou PDF/UA.

[Sources actuelles et dimensions des 100 fichiers](recherche-photos/SOURCES-RECONSTRUCTION.csv). Le tableau `SOURCES-COPIE-PERSONNELLE.csv` est conservé comme historique de la sélection perdue.

## Contrôles de la reconstruction

- 100 fiches, 100 pages photo et 100 fichiers image distincts (SHA-256).
- 100 liens internes valides, une source externe par page photo.
- Polices utilisées incorporées ; aucune page quasi vide ni texte hors page selon le vérificateur.
- Contrôle des 100 photos sur cinq planches, puis des 100 pages photo mises en page sur cinq planches et de la couverture.
- Photos d’ingrédients du thiakry et de poisson cru écartées au profit des plats terminés ; candidats suspects ou hors sujet rejetés.

[Rapport technique](reports/edition-personnelle/validation.json).

## Reconstruction depuis un clone GitHub

```bash
python -m venv .venv
.venv/bin/pip install -r requirements-editorial.txt
.venv/bin/python tools/construire_ebook_complet.py --personal
.venv/bin/python tools/verifier_ebook_complet.py \
  --pdf EBOOK-100-RECETTES-TERRE-DE-FETE-PERSONNEL.pdf \
  --report-dir personnel/rapports --require-photos
```

Le générateur combine les 14 photos locales du registre historique et les 86 entrées du manifeste archivé. Aucun téléchargement réseau n’est nécessaire pour cette reconstruction. `--final` reste protégé : cette copie personnelle ne transforme pas les images tierces en photographies approuvées pour une édition commerciale.
