# Se réveiller, pas subir

Ebook complet sur la paralysie du sommeil, réalisé à partir du
`WORKBOOK-OFFICIEL-JOUR-2-CREE-TON-PREMIER-PRODUIT-DIGITAL.pdf`
(méthode VIN → promesse → format → structure en 5 parties → contenu → checklists).

## Le livrable

| Fichier | Contenu |
|---|---|
| `SE-REVEILLER-PAS-SUBIR-paralysie-du-sommeil.pdf` | **Le produit fini** : 79 pages, format A5, couverture illustrée, sommaire paginé, signets, 5 parties, programme de 21 nuits, fiche d'urgence, journal de bord. |
| `index.html` | Aperçu de toutes les pages dans le navigateur + lien de téléchargement. |
| `WORKBOOK-JOUR-2-COMPLETE-paralysie-du-sommeil.md` | Le workbook du Jour 2 rempli (VIN, promesse, format, structure, prompts, checklist). |

## Structure du livre

1. **Avant de commencer** — « Ce n'est pas une attaque, c'est un décalage »
2. **Partie I — Comprendre** : le verrou de 90 secondes, les déclencheurs, les 3 personnages de la nuit
3. **Partie II — Survivre** : la méthode S.A.F.E. pendant l'épisode, les 20 minutes d'après-crise
4. **Partie III — Croire** : le minzi-minzi, le djinn et l'ombre ; ce que la prière fait vraiment
5. **Partie IV — Agir** : le programme des 21 nuits, une page par nuit
6. **Partie V — Tenir** : fiche d'urgence, journal de bord, quand consulter, déclaration

## Reconstruire le PDF

```bash
pip install pymupdf pillow fonttools brotli
cd ebook
python build.py       # régénère le PDF et index.html
```

Le texte est dans `ebook/content/` : un fichier HTML par section, nommé pour
l'ordre d'assemblage. La maquette est dans `ebook/style.css`.

- `pN-00-partie.html` → ouverture de partie (fond bleu nuit)
- `00-toc.html` → sommaire, dont les numéros de page se remplissent seuls
- `<!--KEY:xx-->` → déclare une clé, insérée ailleurs via `__PAGE_xx__`
- `<!--BM:n|Titre-->` → signet PDF de niveau n
