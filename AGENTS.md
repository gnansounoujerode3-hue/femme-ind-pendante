# Atelier éditorial — livres de recettes

Les skills de ce dépôt sont des ressources de travail locales, pas des extensions globales d’Arena. Leur installation ne modifie pas les outils disponibles sur la plateforme. Respecter en priorité les instructions de la session et la demande de l’utilisateur.

## Routage
- Mise en page de livre : `.agents/skills/cookbook-layout/SKILL.md`.
- Couverture, composition et choix typographiques : `.agents/skills/canvas-design/SKILL.md` et `.agents/skills/theme-factory/SKILL.md`.
- PDF : `.agents/skills/pdf/SKILL.md`.
- Recherche de photographies et droits : `.agents/skills/food-image-sourcing/SKILL.md`.
- Rédaction et cohérence des recettes : `.agents/skills/recipe-editor/SKILL.md`.
- Contrôles avant livraison, PDF/EPUB : `.agents/skills/ebook-quality/SKILL.md`.

## Publication GitHub
- Demande permanente du client : à chaque étape terminée qui modifie le projet, mettre à jour GitHub sur la branche de travail actuelle, sans attendre une nouvelle demande.
- Vérifier le statut, sélectionner les fichiers pertinents, créer un commit et pousser uniquement la branche actuelle. Ne pas publier d’images IA, de secrets ou de fichiers temporaires non validés. Ne pas fusionner vers main sans demande explicite.
- En cas d’échec du push, le signaler ; ne pas prétendre que la publication a réussi.

## Règles du projet
- Le client a validé la maquette à couverture photographique. Appliquer cette direction au livre complet ; ne pas rouvrir la validation du design sans besoin.
- Générateur intégral : `tools/construire_ebook_complet.py`. Le PDF historique `EBOOK-100-RECETTES-TERRE-DE-FETE-TRAVAIL.pdf` n’a que 14 aperçus et 86 photos absentes. La copie séparée `EBOOK-100-RECETTES-TERRE-DE-FETE-PERSONNEL.pdf` se reconstruit avec `--personal` : 240 pages, 100 photos, manifeste persistant `assets/food/personnel/manifest.json`. PDF et sélection archivés sur GitHub à la demande explicite du client après perte de la copie ignorée par Git. Ne présenter aucun de ces documents comme une édition commerciale approuvée : droits des nouvelles images non vérifiés, définition variable et recettes non testées. Voir `EDITION-PERSONNELLE.md`.
- Couverture : **conserver le design de la première maquette** (bloc crème, mêmes titres et polices, grande image en bas, bandeau vert). Remplacer uniquement l’image IA par une vraie photographie ; ne pas refaire la composition sans demande explicite.
- Décision explicite du client : **aucune image générée par IA**, y compris la couverture. L’ancienne maquette illustrée est obsolète et ne doit pas être présentée comme la version approuvée.
- Pour la prochaine édition : **une page de photographie réelle du plat terminé immédiatement avant chaque recette**. Les images de préparation ou d’ingrédients seuls ne conviennent pas à cette page.
- Les photos trouvées en ligne illustrent une variante ; ne pas les présenter comme le résultat exact d’une recette testée pour ce livre.
- Suivi de recherche : `recherche-photos/suivi-100-recettes.json`. Ne pas confondre piste, licence consultée, original obtenu et photo approuvée.
- Conserver les recettes sources et les scripts de génération, pas seulement le PDF final.
- Ne pas présenter une adaptation comme une recette traditionnelle authentifiée, ni une recette non testée comme testée.
- Ne jamais affirmer qu’une image est libre de droits sans vérification de sa licence et de sa provenance.
- Utiliser les outils de recherche d’images réellement accessibles dans la session ; ne pas inventer un moteur de recherche, une API ou un abonnement.
- Les scripts tiers installés sont des exemples à lire avant exécution ; aucune installation de skill ne donne le droit d’exécuter aveuglément leur contenu.
- Après une modification visuelle, rendre et inspecter des pages : le contrôle du texte seul ne prouve pas la qualité graphique.

## Commandes
- Installation reproductible : `python tools/install_editorial_skills.py`.
- Dépendances : `python -m venv .venv` puis `.venv/bin/pip install -r requirements-editorial.txt`.
- Guide actuel : `.venv/bin/python construire_guide.py`.
- Audit : `.venv/bin/python tools/audit_ebook.py`.

Voir `ATELIER-EBOOK.md` pour les capacités installées et leurs limites.
