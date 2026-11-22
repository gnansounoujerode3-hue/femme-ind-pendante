# Mon dossier France — Trouver une bourse et candidater sans agence

Édition **première candidature**, novembre 2026, pour préparer la rentrée 2027. Le parcours principal part du **Bénin** vers la **France**. Le Top 10 présente dix autres pays. Prix prévu en boutique : **5 000 FCFA** pour les quatre fichiers, pas pour une candidature, une bourse ou un visa. Aucun suivi individuel n’est inclus.

## Si c’est ta première demande, commence ici

1. **[Ouvre le guide France (PDF)](Mon-dossier-France.pdf?raw=true).** Si tu lis sur un téléphone, tu peux commencer avec ce seul fichier. Sur la couverture, touche **« Je débute »**, ou tourne jusqu’à la **page 3**.
2. **Réponds à trois questions :** quel diplôme prépares-tu ou as-tu déjà ? Qu’aimerais-tu étudier, et quand ? Pour quelle dépense cherches-tu une aide ? Écris dans les cases ou dans un cahier. Rien n’est envoyé à une école.
3. **Choisis une seule suite.** Un mot te bloque ? Le petit dictionnaire est page 6. Tu sais déjà quelles études tu vises ? La page 9 t’aide à choisir une aide à regarder. Le bouton « Sommaire » au bas des pages te ramène au menu.

## Télécharger tout le kit

**[Télécharger les quatre fichiers ensemble (ZIP)](Kit-Mon-dossier-France.zip?raw=true)**. Un ZIP est un fichier qui en contient plusieurs. Ouvre « Fichiers » ou « Téléchargements », touche le ZIP et choisis « Extraire » ou « Décompresser » si l’option apparaît. Sur ordinateur, le clic droit peut proposer « Extraire tout ». Si un dossier de même nom se crée, ouvre-le. **Si l’extraction ne marche pas, utilise les quatre liens séparés ci-dessous.**

| Fichier | À quoi sert-il ? |
| --- | --- |
| [Mon dossier France · PDF de 56 pages](Mon-dossier-France.pdf?raw=true) | Quatre aides françaises ou avec séjour en France, compte Études en France, paiement et preuve d’envoi, pièces et écrits, budget, calendrier, entretien, liste à cocher et questions fréquentes. |
| [Top 10 international · PDF de 18 pages](bonus/Top-10-bourses-internationales.pdf?raw=true) | Dix pays, dix programmes. Une page pour choisir son niveau, une pour comprendre les mots anglais. Lis l’état de la campagne, les conditions et l’argent à avancer avant de décider. Remplis la dernière page pour une seule piste. |
| [Atelier de candidature · Word](bonus/Atelier-dossier.docx?raw=true) | Huit modèles. Un premier essai explique comment sélectionner **un** modèle, remplacer les crochets, enregistrer un document séparé et le rouvrir avant de l’envoyer. |
| [Suivi et budget · Excel](bonus/Suivi-et-budget.xlsx?raw=true) | Cinq feuilles, sept exemples de démarches, dix-huit exemples de pièces. Commence par « Mode d’emploi » : dans une copie, change une somme de l’exemple, vérifie le résultat, puis utilise la feuille « Budget » pour tes vrais chiffres. |

Les deux PDF sont en français et à texte sélectionnable. **Après le téléchargement, pas besoin d’internet pour les lire.** Une connexion est nécessaire pour consulter les organismes et déposer un vrai dossier. Si le navigateur ne garde pas tes réponses, télécharge le PDF et ouvre une copie dans un lecteur avec formulaires, ou réponds dans un cahier. Pour écrire sur un modèle, utilise Word ou une application compatible. Pour modifier le budget, utilise Excel ou un autre tableur qui recalcule les formules.

## Pour la personne qui vend le kit

**[Télécharger les ressources Chariow](vente/Ressources-Chariow.zip?raw=true)** : [description et message WhatsApp](vente/Fiche-Chariow.md), [visuel 1080 × 1080](vente/Visuel-Chariow.png), [extrait gratuit de 4 pages](vente/Extrait-gratuit.pdf?raw=true). L’extrait contient la couverture, le premier exercice, les relevés par niveau et le calcul du billet. **Ne pas livrer cette archive à la place du kit acheteur.** Rien n’a été publié automatiquement en boutique. Le dépôt est public : les fichiers ne sont pas réservés aux acheteurs.

## Pour mettre à jour l’édition

- Contrôler les [sources officielles](edition/sources.json) avant toute nouvelle mise en vente. Pour le Bénin, le **1er décembre 2026** concerne le paiement si dû **et le premier envoi** ; le **15 décembre** concerne le dernier envoi après correction. Lire les pages actualisées, pas seulement le premier calendrier PDF. Une campagne close ne se rouvre pas en ajoutant un an aux dates.
- Modifier le [texte France](edition/guide.md) et le [texte international](edition/panorama.md). Les lignes `1.`, `2.`… sont des étapes, `?` des champs à remplir, `□` des cases à cocher, `~` des renvois vers une autre page et `@` des références dans `sources.json`. Les numéros des renvois sont calculés à la fabrication. Aligner l’index et les statuts du Top 10 dans `edition/panorama.py`, la fiche boutique, l’extrait et les décomptes de pages ci-dessus.
- Les modèles Word se trouvent dans `edition/atelier.py` ; les exemples, les cellules et les formules du classeur dans `edition/tableur.py`. Quand une cellule d’exercice change, vérifier aussi les numéros et les résultats annoncés dans le guide.

Pour régénérer et vérifier depuis la racine (Python 3.11+, polices DejaVu Sans et Serif, normales et grasses) :

```sh
python -m venv .venv
.venv/bin/pip install -r bourse-france/edition/requirements.txt
.venv/bin/python bourse-france/edition/fabriquer.py
.venv/bin/python bourse-france/edition/verifier.py
```

Le chemin des polices peut être défini avec `DOSSIER_FONTS`. La génération et les contrôles sont hors ligne : ils vérifient les fichiers livrés, pas l’ouverture actuelle des appels, et ne publient rien en ligne.
