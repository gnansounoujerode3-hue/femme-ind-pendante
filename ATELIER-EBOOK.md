# Atelier e-book culinaire — installation

## Ce qui est installé

Sept skills locaux sont disponibles dans `.agents/skills/`, avec un routage dans `AGENTS.md`. Il s’agit de consignes, de références, de ressources graphiques et, pour certains, de scripts ; ce ne sont pas des extensions globales de la plateforme. Aucun classement objectif ne permet de garantir qu’ils seraient « les meilleurs » : cette sélection couvre les besoins de ce livre sans multiplier les modules inutiles.

### Trois ressources publiques importées

Source : https://github.com/anthropics/skills

Révision épinglée : `e4bb5d960d87126ff3b3a8af1a104b7db67560ba`.

| Skill | Fonction |
|---|---|
| `pdf` | Génération, lecture et manipulation de PDF ; références et exemples de traitement. |
| `canvas-design` | Composition graphique, direction artistique, ressources typographiques et couverture. |
| `theme-factory` | Palettes et associations typographiques pour une identité visuelle cohérente. |

Les fichiers de licence et les licences des polices fournis par la source sont conservés. Vérifier leurs conditions avant redistribution. Les empreintes de tous les fichiers importés sont consignées dans `.agents/upstream/manifest.json`. Aucun script tiers n’a été exécuté pour installer ces skills : ils ont été copiés depuis une archive épinglée.

### Quatre skills spécifiques créés pour votre projet

| Skill | Fonction |
|---|---|
| `cookbook-layout` | Gabarits de recettes, lisibilité, grille, marges, couverture et protocole d’inspection. |
| `food-image-sourcing` | Recherche d’images fidèles aux plats africains, sélection, résolution, licences et crédits. |
| `recipe-editor` | Quantités, cohérence ingrédients/étapes, explications pour débutants et sécurité alimentaire. |
| `ebook-quality` | Contrôles PDF, inspection visuelle, préparation EPUB et critères de livraison. |

Ces quatre guides sont des créations locales, pas des plugins externes certifiés.

## Outils Python installés et vérifiés

- **ReportLab** : construction PDF.
- **pypdf** : lecture et vérification du texte PDF.
- **Pillow** : vérification et traitement des fichiers image.
- **PyMuPDF** : rendu des pages PDF pour contrôle visuel.
- **EbookLib** : bibliothèque disponible pour une future version EPUB.

Les versions sont figées dans `requirements-editorial.txt`. L’environnement `.venv` est local et ignoré par Git ; il peut être recréé.

## Reproduire l’installation

```bash
python tools/install_editorial_skills.py
python -m venv .venv
.venv/bin/pip install -r requirements-editorial.txt
.venv/bin/python tools/audit_ebook.py
```

Le premier script retélécharge les trois skills publics à la même révision et remplace leurs copies locales. Il ne modifie pas les quatre skills spécifiques.

## Photos : capacités et limites réelles

Le skill d’iconographie indique comment employer les outils de recherche d’images disponibles dans la conversation, mais **il ne crée pas d’accès réseau ou d’abonnement**. Dans cet environnement, les connexions sortantes depuis le terminal sont limitées aux domaines autorisés ; certaines banques photo ne peuvent pas être téléchargées directement par script. Les outils web et image de la session, s’ils sont accessibles, ont leur propre fonctionnement.

Une image trouvée doit être vérifiée sur sa page d’origine. Un moteur de recherche n’accorde pas le droit de l’utiliser. Le registre `assets/food/registry.json` est prêt, mais **vide** : aucune photo n’a été acquise, approuvée ou intégrée pendant cette installation. Les illustrations générées doivent être signalées comme telles et ne doivent pas être présentées comme les photos de recettes testées.

## Résultat du contrôle effectué

Commande : `.venv/bin/python tools/audit_ebook.py`.

- Présence des sept skills et intégrité des trois imports publics contrôlées.
- Numérotation 1–100 et sections des recettes contrôlées.
- PDF actuel de 62 pages ouvert et titres des 100 recettes retrouvés.
- Avertissements conservés : aucune photo acquise ; le contrôle automatique ne remplace ni une inspection graphique ni des essais culinaires.

Rapport : `reports/audit-editorial.json`.

## Ce qui n’a pas été fait dans cette installation

- Pas de nouvelle mise en page ni de remplacement du PDF existant.
- Pas d’achat d’images, de téléchargement de photos ou de garantie de licence.
- Pas de génération d’EPUB ; EbookLib est prêt, mais EPUBCheck n’est pas installé.
- Pas de certification PDF/UA, de validation imprimeur ou de test culinaire.
- Pas d’activation de Notion, Supabase ou Vercel : ces applications ne sont pas nécessaires ici.

## Suite recommandée

1. Choisir une direction artistique et produire une couverture plus quatre ou cinq pages pilotes.
2. Vérifier ce prototype avant d’appliquer le gabarit aux 100 recettes.
3. Constituer une première sélection d’images : couverture et dix ouvertures de chapitre ; valider fidélité culinaire et droits.
4. Ajouter progressivement des photos de recettes avec crédits et textes alternatifs.
5. Exporter le PDF, inspecter les pages, tester les liens, puis préparer un EPUB si souhaité.
6. Faire tester les recettes et réaliser une relecture humaine avant commercialisation.
