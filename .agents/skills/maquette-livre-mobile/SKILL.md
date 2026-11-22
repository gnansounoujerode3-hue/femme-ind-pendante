---
name: maquette-livre-mobile
description: "Composer ou améliorer la mise en page d’un guide de bourses en français : couverture, typographie, grille, fiches, navigation tactile, contraste et épreuves sur téléphone. À utiliser pour une maquette, une page trop dense, un sommaire ou un visuel de boutique."
---

# Composer pour la personne qui lit sur son téléphone

**Résultat attendu :** une page où le lecteur repère la question, sa prochaine action et la preuve à garder. Une belle couverture ne compense pas une date de dépôt illisible. Respecter le périmètre demandé : pour un diagnostic, ne pas modifier le livre ; pour une proposition, travailler sur une épreuve.

## 1. Observer avant de dessiner

- Identifier le support : guide France, Top 10, extrait ou vignette. Ouvrir `bourse-france/edition/livret.py` (charte et composition) et, pour le bonus, `panorama.py`. Modifier le manuscrit pour le **contenu**, le générateur pour une **règle graphique**. Ne pas retoucher un PDF final page par page.
- Rendre au moins une page dense et une page interactive. À la racine :

```sh
.venv/bin/python .agents/studio.py epreuve france couverture sommaire debut depot depart --largeur 360
```

Ouvrir `planche.png` pour voir le rythme, puis les **PNG individuels** du dossier indiqué pour juger le texte à taille réelle. `epreuve top10 --liste` affiche les pages disponibles du bonus. Les images sont des épreuves : elles ne remplacent pas les PDF cliquables.

## 2. Choisir un patron, pas une décoration

| Page | Ce que l’œil doit trouver, de haut en bas |
| --- | --- |
| Couverture | Titre lisible en miniature → à qui sert le livre et pour quelle rentrée → où commencer. Une illustration originale ; aucun faux logo d’État, diplôme ou sceau officiel. Pour la vignette de vente seulement, vérifier aussi le prix au format carré. |
| Fiche bourse | Nom et niveau → **campagne + état en toutes lettres** → qui peut demander → ce qui est payé ou reste à avancer → qui dépose et où → lien officiel. Ne jamais utiliser le même badge pour « admission ouverte » et « bourse accordée ». |
| Démarche | Une question en titre → ce qu’il faut avoir sous la main → étapes numérotées → résultat visible → « si ça bloque ». Mettre le numéro près du geste qu’il repère. |
| Calcul ou exercice | Situation fictive et monnaie → données → une opération par ligne → somme nécessaire **avant** puis **après** versement. Placer chaque étiquette juste au-dessus de son champ. |

Pour essayer une composition dans le manuscrit, voir les [deux patrons prêts à adapter](references/patrons.md) : une démarche Eiffel et un billet remboursé. Ne les ajouter à l’édition livrée que si cela apporte un usage nouveau.

## 3. Régler la hiérarchie

- Partir de la grille existante : **390 × 844 points, une colonne, marges de 22 points**. Conserver la paire Serif pour les titres / Sans pour le texte, les alignements communs et la zone indépendante des sources. Deux niveaux de titres suffisent à la plupart des pages.
- Commencer le texte courant vers 14–15 points avec de l’air entre les étapes ; le moteur actuel teste le corps jusqu’à 12,6 points. Si le dernier bloc touche les sources ou si l’œil se perd, **scinder la tâche** ou enlever une répétition avant d’envisager une réduction. Ne pas gagner de place au détriment d’un critère ou d’un délai.
- Respecter les espaces insécables des montants et la ponctuation française. Vérifier `É`, `œ`, `€`, les accents et les milliers. Les liens doivent se distinguer même sans couleur. Réserver les aplats aux décisions ou aux alertes, pas à chaque paragraphe.
- Pour une **nouvelle identité demandée**, utiliser `theme-factory` pour proposer des thèmes, attendre le choix, puis traduire la palette en rôles : texte, fond, accent, lien, avertissement. Ne pas remplacer la charte actuelle par défaut. Un nom de police dans un thème n’autorise pas sa redistribution ; utiliser des polices disponibles et autorisées.

## 4. Accepter ou reprendre l’épreuve

Après un changement des sources de mise en page, lancer la même commande avec `--brouillon` : le livre est refabriqué dans une copie temporaire. Comparer **la même page à la même largeur**. Le script calcule le contraste de quatre paires de texte de la charte (repère 4,5:1) ; ce n’est pas un audit de tous les pixels ni une certification d’accessibilité.

Vérifier le vrai PDF : lire le titre sans zoom, suivre « Je débute », revenir au sommaire, remplir un champ, enregistrer puis rouvrir. Vérifier aussi l’extrait : aucun renvoi ne doit mener à une page absente. Terminer par `controle-kit`. Rendre un avis exploitable : **page → défaut observé → correction → résultat après contrôle**. Ne pas annoncer un essai sur un appareil physique si seule une simulation en pixels a été faite.
