# Mon dossier France — Trouver une bourse et candidater sans agence

Édition indépendante de novembre 2026 pour la rentrée 2027. Le parcours principal concerne un candidat qui réside **au Bénin** et souhaite étudier en **France**. Le bonus international est un ouvrage distinct. Prix du kit : **5 000 FCFA**. Aucun service de dépôt ou de suivi individuel n’est inclus ; rien n’a été publié automatiquement en boutique.

## Fichiers acheteur

**[Télécharger le kit complet](Kit-Mon-dossier-France.zip)**. Extraire les quatre fichiers. Ils peuvent aussi être proposés séparément sur téléphone :

| Fichier | Par où commencer ? |
| --- | --- |
| [Guide France · 40 pages (PDF)](Mon-dossier-France.pdf) | Sommaire page 2. Quatre financements, démarches béninoises pièce par pièce, écrits, plan mensuel, entretien, checklist, FAQ et sources. |
| [Top 10 · 10 bourses complètes dans 10 pays · 17 pages (PDF)](bonus/Top-10-bourses-internationales.pdf) | Le sommaire indique quelles campagnes sont ouvertes, à confirmer ou closes à l’édition. Chaque fiche distingue les dépenses couvertes et les avances. Enregistrer une copie par piste pour remplir les champs de la dernière page ; sur un lecteur sans formulaires, imprimer ou répondre dans une note. |
| [Atelier de candidature (Word)](bonus/Atelier-dossier.docx) | Huit gabarits modifiables : CV, motivation, Study Plan, projet de thèse, contacts (dont préadmission), recommandation, relance, entretien. Extraire le modèle voulu, pas de dossier type à envoyer tel quel. |
| [Suivi et budget (Excel)](bonus/Suivi-et-budget.xlsx) | Cinq onglets, sept exemples de démarches françaises, dix-huit exemples de pièces ou preuves, budget personnel et simulation. Ouvrir une copie dans un tableur qui recalcule les formules. |

Les PDF sont en français, à texte sélectionnable et à sommaire cliquable, lisibles hors ligne sur téléphone ou ordinateur. Une connexion est nécessaire pour consulter les sources officielles. Le prix des fichiers ne couvre aucun frais de candidature.

## Fichiers pour la vente

**[Ressources Chariow](vente/Ressources-Chariow.zip)** : [fiche produit et bouton d’achat à configurer](vente/Fiche-Chariow.md), [vignette 1080 × 1080](vente/Visuel-Chariow.png), [extrait gratuit de 3 pages](vente/Extrait-gratuit.pdf). Le ZIP vendeur ne doit pas être livré comme kit acheteur. Le dépôt étant public, ces fichiers n’offrent aucune exclusivité d’accès au produit payant.

## Actualiser une campagne

- Contrôler les [sources officielles](edition/sources.json) avant de relancer les ventes. Pour le Bénin, distinguer le **1er décembre** (paiement si dû et première soumission) du **15 décembre 2026** (dernière soumission après correction) : lire les pages HTML actualisées, pas seulement le premier calendrier PDF.
- Modifier le [manuscrit France](edition/guide.md) et le [manuscrit international](edition/panorama.md). Dans le second, relire chaque année nationalité/résidence, niveau, financement, durée, versements, voie d’admission et date de la bourse. Une offre passée n’est pas une nouvelle session. Mettre à jour aussi les statuts affichés dans l’index de `edition/panorama.py`.
- Les modèles Word sont dans `edition/atelier.py` ; les exemples du classeur et les formules sont dans `edition/tableur.py`. Aligner la fiche boutique, l’extrait et le visuel sur ce qui est réellement livré. Pas de chiffres de ventes ni d’avis d’autres vendeurs.

Pour régénérer et vérifier depuis la racine (Python 3.11+, polices DejaVu Sans et Serif, normales et grasses) :

```sh
python -m venv .venv
.venv/bin/pip install -r bourse-france/edition/requirements.txt
.venv/bin/python bourse-france/edition/fabriquer.py
.venv/bin/python bourse-france/edition/verifier.py
```

Le chemin des polices peut être défini avec `DOSSIER_FONTS`. La génération et le contrôle sont hors ligne : ils testent les fichiers, pas la disponibilité actuelle des bourses, et ne publient rien en ligne.
