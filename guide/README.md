# Guide — génération du PDF

Le PDF est généré à partir de `chapitre-01-bien-se-preparer.md` par `build_pdf.py`.

## Générer ou actualiser

Depuis la racine du dépôt :

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r guide/requirements.txt
.venv/bin/python guide/build_pdf.py
```

Le script écrit `guide/chapitre-01-bien-se-preparer.pdf`. Il nécessite une police DejaVu Sans installée sous `/usr/share/fonts/truetype/dejavu` (ou un ajustement des chemins dans le script).

## Choix de production

- Format A4, couverture graphique originale sans image de banque ni logo.
- Corps de texte en 11 pt, styles de titres, tableaux adaptés aux fiches de travail et contraste élevé.
- Table des matières cliquable, signets de navigation PDF et liens internes.
- Polices Unicode intégrées, métadonnées de document, pied de page avec version/date et pagination hors couverture.
- Poids maîtrisé ; la version actuelle reste très inférieure à 20 Mo.

Le PDF est un **brouillon éditorial**. Les entretiens de validation ont été laissés de côté à la demande de l’utilisateur. Ce fichier n’est pas une version finale, n’a pas encore fait l’objet d’une validation des informations propres aux démarches officielles, et ne constitue pas un PDF balisé PDF/UA. Vérifier les sources et tester la lecture avec les publics concernés avant diffusion.
