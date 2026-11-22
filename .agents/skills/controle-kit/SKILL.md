---
name: controle-kit
description: "Contrôler un kit de bourses avant livraison ou vente : PDF et formulaires, liens, Word modifiable, calculs du budget Excel, extrait et archives acheteur/vendeur. À utiliser après une révision, une nouvelle mise en page ou pour tester le kit sans l’écraser."
---

# Vérifier ce que recevra réellement le lecteur

**Livrer un état :** validé / à corriger / non testé, avec fichier, page ou cellule. Un contrôle technique réussi ne prouve ni que la bourse est ouverte aujourd’hui ni qu’un lecteur novice comprend le texte.

### 1. Choisir le bon type d’essai

À la racine, avec l’environnement Python du projet :

```sh
# Vérifie les skills, puis les fichiers réellement présents. Ne les remplace pas.
.venv/bin/python .agents/studio.py tester
# Vérifie que les sources permettent aussi de tout refaire dans une copie temporaire.
.venv/bin/python .agents/studio.py tester --brouillon
```

Ces commandes utilisent `bourse-france/edition/verifier.py`. Pour une épreuve visuelle après modification des sources, utiliser `epreuve … --brouillon` dans `maquette-livre-mobile`. Ne lancer `bourse-france/edition/fabriquer.py` sur le dossier réel que si la mise à jour des livrables est demandée ; ensuite recontrôler **ces** fichiers.

### 2. Compléter les contrôles automatiques par un essai d’usage

| Objet | Geste de contrôle et signe de réussite |
| --- | --- |
| PDF France | Depuis la couverture, toucher « Je débute », écrire quelques mots, enregistrer une copie et la rouvrir. Tester le retour au sommaire, un lien de bourse et les cases du dernier contrôle. Les caractères accentués restent lisibles. |
| Top 10 et extrait | Retrouver une campagne close et l’explication de son état sans se fier à la couleur. Tester une fiche de décision. Dans l’extrait, aucun lien interne vers un chapitre absent. Ne pas confondre URL bien formée et page officielle effectivement consultée. |
| Word | Depuis l’index, ouvrir un modèle, copier uniquement la partie utile dans un document vierge, remplacer les crochets puis rouvrir la copie. Le modèle d’origine reste utilisable. Faire l’essai sur des noms fictifs. |
| Excel | Dans **une copie** de « Exemple budget », remplacer les 100 000 F en C7 par 150 000 F. Les montants à trouver aux lignes 29/30 passent de 350 000 / 70 000 F à **300 000 / 20 000 F** dans l’exercice actuel. Tester dans un tableur qui recalcule : des valeurs en cache ne prouvent pas le recalcul. Ne jamais enregistrer cet essai par-dessus le classeur acheteur. |
| Vente | Comparer titre, prix (5 000 FCFA dans cette édition), nombre de pages et contenu annoncé aux fichiers. Ouvrir le ZIP acheteur : deux PDF, un DOCX, un XLSX. Le ZIP vendeur ne contient que fiche, visuel et extrait. Aucun skill, police de travail, donnée personnelle ou image d’épreuve dans ces archives. |

### 3. Décider

Bloquer la livraison en cas de montant faux, lien interne cassé, pièce obligatoire illisible, ancienne date donnée comme actuelle, formulaire qui perd les réponses sans solution indiquée ou archive intervertie. Après correction, retester la page **et** ce qui y renvoie. Distinguer les essais réalisés dans un lecteur ou tableur des tests en mémoire. Une certification PDF/UA, un test sur téléphone physique ou une vérification en ligne ne doivent pas être revendiqués sans avoir été réalisés.
