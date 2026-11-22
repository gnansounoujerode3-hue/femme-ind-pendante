# Les outils de mise en page de *Mon dossier France*

Un **skill** est une fiche de travail que l’assistant peut suivre. Ici, six fiches sont installées avec le projet. **Tu n’as rien à installer sur ton téléphone pour lire le livre.** Les skills servent à la personne qui le prépare ; ils ne changent pas à eux seuls la couverture, le texte ou les fichiers en vente.

## Que demander en premier ?

Tu peux copier ce message :

> Utilise `maquette-livre-mobile`. Montre-moi la couverture, le sommaire et la page qui explique comment envoyer le dossier, à la largeur d’un petit téléphone. Dis-moi où l’œil doit aller en premier et ce qui risque d’être trop petit. Ne modifie pas le livre pour l’instant.

| Je veux… | Fiche installée | Ce que j’obtiens |
| --- | --- | --- |
| Des pages faciles à lire | [maquette-livre-mobile](.agents/skills/maquette-livre-mobile/SKILL.md) | Une grille pour la couverture, les démarches, les fiches et les budgets. Une **épreuve** (image d’une vraie page) à 360 ou 390 pixels de large. |
| Choisir d’autres couleurs et polices | [theme-factory](.agents/skills/theme-factory/SKILL.md) | [Un catalogue de dix thèmes](.agents/skills/theme-factory/theme-showcase.pdf). On choisit une direction avant de refaire la maquette. |
| Vérifier l’aspect du PDF | [pdf](.agents/skills/pdf/SKILL.md) | Une méthode pour repérer du texte coupé, des caractères manquants ou des éléments mal alignés sur les pages rendues. |
| Expliquer une démarche à quelqu’un qui débute | [redaction-debutants](.agents/skills/redaction-debutants/SKILL.md) | Des gestes dans l’ordre, un exemple, une preuve de réussite et une solution si ça bloque. |
| Savoir si une bourse est vraiment ouverte | [verification-bourses](.agents/skills/verification-bourses/SKILL.md) | Une feuille de vérification avec les liens officiels à lire. Elle sépare la date du candidat de celle de l’école, et l’aide confirmée d’une simple demande. **Les dates ne se mettent pas à jour toutes seules.** |
| Vérifier ce qui sera livré | [controle-kit](.agents/skills/controle-kit/SKILL.md) | Des contrôles sur les PDF, leurs liens et champs, les modèles Word, les exemples Excel et le contenu des deux ZIP. |

Deux autres demandes utiles :

- « Utilise `verification-bourses` sur Eiffel à Paris-Saclay. Quelle date concerne l’étudiant ? Laquelle concerne l’école ? Montre la source de chaque réponse. Si la prochaine rentrée n’est pas annoncée, écris “à confirmer”. »
- « Utilise `redaction-debutants` pour expliquer la différence entre payer et envoyer le dossier. Propose le texte, puis teste sa mise en page **en brouillon**, sans remplacer l’édition actuelle. »

## Où sont-ils installés ?

L’installation est **locale au projet** : les fiches `SKILL.md` et leurs ressources sont dans [`.agents/skills/`](.agents/skills/). Elles suivent le dépôt et n’ont pas besoin de boutique de plugins ni de compte externe. Pour un client qui utilise `.claude/skills/`, un lien mène au même dossier. Si ton outil ne découvre pas les skills ou ne suit pas les liens symboliques, donne-lui le chemin de la fiche : par exemple **« Lis `.agents/skills/maquette-livre-mobile/SKILL.md` et applique-la »**. [AGENTS.md](AGENTS.md) associe chaque tâche à sa fiche. Cela ne crée pas de bouton dans Arena et ne modifie pas les autres projets.

## Pour la personne qui fabrique le livre

Depuis la racine du dépôt, `python .agents/studio.py liste` affiche les noms installés. Pour les commandes d’édition, utiliser l’environnement Python du [projet](bourse-france/README.md#pour-mettre-à-jour-lédition). S’il n’existe pas encore, sur Linux/macOS avec Python 3.11+ :

```sh
python -m venv .venv
.venv/bin/python -m pip install -r bourse-france/edition/requirements.txt
```

Les générateurs attendent DejaVu Sans et Serif, normales et grasses. Si elles ne sont pas au chemin Linux prévu, définir `DOSSIER_FONTS` vers leur dossier. Sur Windows, remplacer `.venv/bin/python` par `.venv\Scripts\python.exe`.

```sh
# 1. Voir les pages disponibles puis rendre les pages choisies.
.venv/bin/python .agents/studio.py epreuve france --liste
.venv/bin/python .agents/studio.py epreuve france couverture sommaire depot --largeur 360

# 2. Retrouver les sources citées pour une fiche. Aucune visite web automatique.
.venv/bin/python .agents/studio.py sources france saclay

# 3. Tester les fichiers existants, puis la fabrication depuis les sources sans les écraser.
.venv/bin/python .agents/studio.py tester
.venv/bin/python .agents/studio.py tester --brouillon
```

Les épreuves affichent leur chemin sous `.cache/epreuves/`. Ouvrir `planche.png` pour comparer les pages, puis `page-XX.png` pour lire à taille réelle. Les liens et formulaires se testent dans le **PDF**, pas dans ces images. L’option `--brouillon` fonctionne aussi avec `epreuve` : elle montre les modifications en cours du manuscrit sans écrire sur le PDF livré. Aucune de ces commandes ne publie le kit.

## Provenance et mises à jour

Quatre skills sont écrits pour ce livre. Les deux autres ont été installés en entier, sans modification, depuis des versions précises :

- [PDF — OpenAI Skills, révision `49f948f`](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/pdf) · [licence Apache 2.0 conservée](.agents/skills/pdf/LICENSE.txt).
- [Theme Factory — Anthropic Skills, révision `e4bb5d9`](https://github.com/anthropics/skills/tree/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/theme-factory) · [licence Apache 2.0 conservée](.agents/skills/theme-factory/LICENSE.txt).

[Le registre des origines](.agents/origines.json) indique la révision et l’empreinte SHA-256 de chaque fichier importé. `tester` compare les fichiers locaux à ce registre, sans internet. Pour actualiser un skill tiers, relire les changements et la licence à la nouvelle révision, remplacer seulement son dossier, mettre à jour le registre et les liens de provenance, puis refaire les contrôles. Aucune installation globale ni mise à jour automatique.
