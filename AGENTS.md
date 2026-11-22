# Atelier d’édition · Mon dossier France

Pour une tâche sur le livre ou ses bonus, utiliser les Agent Skills installés **dans ce dépôt**, sous `.agents/skills/`. Ils sont des modes opératoires, pas des services distants. Si le client ne les charge pas automatiquement, ouvrir le `SKILL.md` approprié. Le répertoire `.claude/skills` pointe vers la même installation. Ne charger que les fiches utiles à la tâche.

| Demande | Skill à ouvrir |
| --- | --- |
| Vérifier une condition, une date, un coût ou une campagne | [verification-bourses](.agents/skills/verification-bourses/SKILL.md) |
| Rendre les démarches compréhensibles dès la première lecture | [redaction-debutants](.agents/skills/redaction-debutants/SKILL.md) |
| Composer la couverture, les pages, les sommaires ou simuler la lecture sur téléphone | [maquette-livre-mobile](.agents/skills/maquette-livre-mobile/SKILL.md) |
| Proposer une autre direction de couleurs/polices, **si demandé** | [theme-factory](.agents/skills/theme-factory/SKILL.md), puis `maquette-livre-mobile` pour l’appliquer au livre |
| Rendre et inspecter un PDF plutôt que juger le seul texte extrait | [pdf](.agents/skills/pdf/SKILL.md) + l’épreuve locale |
| Vérifier PDF, modèles Word, budget Excel, extrait et ZIP | [controle-kit](.agents/skills/controle-kit/SKILL.md) |

**Ordre pour une nouvelle édition :** vérifier les faits → rédiger → composer → examiner les épreuves → contrôler les fichiers livrés. Pour une simple retouche graphique, inutile de relancer une enquête complète ; en revanche ne pas modifier les faits au passage.

**Conventions locales pour les skills génériques :** conserver `bourse-france/edition/`, les chemins finaux du kit et les conventions typographiques françaises (accents et espaces insécables). Utiliser la pile Python déjà prévue, ReportLab et le rendu PyMuPDF de `.agents/studio.py` ; pas besoin d’installer Poppler avec `sudo`, de créer `output/pdf/` ou de remplacer les polices par défaut. Les épreuves restent dans `.cache/epreuves/`, pas dans les ZIP. Le catalogue des thèmes et les licences sont des outils d’auteur, pas des bonus acheteur.

Partir des [commandes et exemples](ATELIER-EDITION.md). Pour un audit ou un essai sans livraison, `studio.py tester` lit le kit et `studio.py tester --brouillon` le refabrique **dans une copie temporaire**. Une installation de skills ne demande ni réédition, ni mise en vente, ni accès aux comptes du candidat.
