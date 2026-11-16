# Philosophie Éditoriale & Système Design : « Savane Solaire & Papier Ivoire »

Conçu à partir des meilleurs standards éditoriaux installés dans `.agents/skills/` (`canvas-design`, `top-design`, `web-typography`, `editorial`, `terracotta`, `paper`, `refined`, `editorial-package`, `hallmark` et `pdf`), propulsé par le moteur typographique **Typst 0.15**.

## 1. Mouvement Esthétique : « Monocle Afro-Moderniste »

Un livre pratique d'entrepreneuriat africain ne doit ni ressembler à un rapport administratif généré, ni à un fichier Word empilé de cadres gris. Il doit porter la présence tactile d'un beau livre imprimé **Taschen / Monocle / Stripe Press** : papier ivoire chaud, encre vert-forêt profonde, titres sculpturaux à fort contraste d'échelle, filets architecturaux fins et respiration spatiale maîtrisée.

## 2. Système Typographique (3 Rôles Disciplinés)

1. **Display & Titres Monumentaux** — `Instrument Serif` (*Regular & Italic*) : lettrines de chapitres, numéros de parties (`01`–`05`), couverture, titres de secteurs et citations d'accroche. Contraste d'échelle > 6:1 sur les ouvertures.
2. **Corps de Texte & Fiches Catalogue** — `Instrument Sans` (*Regular, Bold, Italic, BoldItalic*, avec repli `Source Sans Pro`) : dessinée pour s'accorder avec `Instrument Serif` (harmonie de fonderie), optimisée pour une mesure de 48 à 55 caractères par colonne en grille suisse à 2 colonnes.
3. **Indices Techniques & Télémétrie** — `JetBrains Mono` (*Regular & Bold*) : codes `#001` à `#500`, étiquettes `SECTEUR 01 / 20`, badges budgets `PETIT` / `MOYEN` / `STRUCTURÉ`, chronologie `J1`–`J7` et grille `VIN`.

## 3. Palette Tactile (Zéro `#000000` ni `#FFFFFF` stérile)

| Rôle | Token | Hex | Usage |
|---|---|---|---|
| Papier principal | `paper` | `#FAF7F2` | Fond chaud ivoire sur toutes les pages intérieures |
| Papier secondaire | `paper-alt` | `#F2ECE1` | Encadrés éditoriaux, colophon, lignes paires |
| Papier sauge | `paper-sage` | `#EBF2EE` | Blocs action & validation terrain |
| Encre primaire | `ink` | `#12201C` | Texte principal haute lisibilité |
| Encre secondaire | `ink-2` | `#46544F` | Descriptions et sous-titres |
| Émeraude profonde | `emerald` / `deep` | `#0B3B31` / `#07241D` | Ouvertures de chapitres, couverture, titres majeurs |
| Or solaire | `gold` / `gold-hi` | `#C5881E` / `#E9AF43` | Filets, accents de promesse, numéros clés |
| Terre cuite | `terracotta` | `#B8532A` | Alertes erreurs, budgets structurés, repères terrain |
| Filets | `rule` | `#DDD5C7` | Lignes de séparation éditoriales 0.45pt |

## 4. Règles d'Artisanat Anti-Slop

- **Zéro carte répétitive dans une carte** : le catalogue des 500 idées adopte une grille éditoriale suisse à **2 colonnes séparées par de fins filets typographiques** (aucune bordure lourde répétitive).
- **Atomicité absolue** : aucune fiche idée, aucun bandeau de chapitre, aucune table d'erreur ne peut être coupé entre deux pages.
- **Navigation active** : le Sommaire utilise des liens internes PDF cliquables et des numéros de pages calculés nativement par Typst.
- **Cohérence 1-pour-1** : les 10 pages du Workbook Jour 2 rempli et les 5 parties + Conclusion de l'ebook partagent exactement le même langage visuel et les données dynamiques de `ebook-source/author_config.json`.
