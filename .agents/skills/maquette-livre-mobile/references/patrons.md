# Deux patrons à essayer dans une copie du manuscrit

Ce sont des exemples de **composition**, pas de nouveaux appels. Le moteur du livre lit une ligne `#` comme une nouvelle page ; un `!` dessine un encadré, un `~` crée un renvoi interne et un `@` place les sources dans la zone du bas. Choisir un exemple, adapter les faits et vérifier les références avant toute intégration. Ne pas empiler les deux patrons sur une même page.

## 1. Démarche : séparer le geste du candidat de celui de l’école

```text
# essai-eiffel | Atelier / Comprendre la démarche | Qui envoie le dossier Eiffel ?
> Tu peux demander à une école d’étudier ton dossier. Cela ne veut pas encore dire que l’école l’a présenté au jury Eiffel.
1. Ouvre la page du master que tu vises. Cherche qui est responsable de la formation et comment le contacter.
2. Lis la date de sélection de cette école pour la bonne rentrée. Dans ton agenda, note ton action : « contacter le master », pas « envoyer au jury national ».
3. Demande à l’école de confirmer si elle te présente. Fais aussi la démarche demandée pour entrer dans le master.
! Preuve à garder | La réponse écrite de l’école. Une preuve de présentation n’est pas une lettre d’attribution de bourse.
~ saclay | Comprendre les deux dates avec l’exemple de Paris-Saclay
@ eiffel saclay
```

**Pourquoi cet ordre ?** Le titre pose la question du lecteur. Les numéros repèrent ses gestes. Le seul encadré évite l’erreur importante. Les liens officiels restent en bas, séparés de la prochaine page du livre. Une date actuelle, si on l’ajoute, doit venir de la campagne effectivement relue.

## 2. Budget : faire lire deux moments, pas un tableau trop large

```text
# essai-billet | Atelier / Exemple inventé en francs CFA | Un billet remboursé est-il gratuit au départ ?
> Simulation, pas un tarif réel. Le billet coûte 100 000 F. L’étudiante a 60 000 F en main. Une lettre lui promet un remboursement de 30 000 F après le voyage.
## Le jour de l’achat
Elle doit payer 100 000 F. Il lui manque 100 000 − 60 000 = **40 000 F** pour acheter le billet.
## Après le remboursement
La dépense nette sera de 100 000 − 30 000 = **70 000 F**. Avec les 60 000 F dont elle disposait, il reste donc 10 000 F non couverts au final.
! Ce qui change la décision | Elle ne peut pas partir avec seulement 10 000 F de plus aujourd’hui : le remboursement arrivera plus tard.
~ exemple | Refaire le calcul du guide avec le logement et l’allocation
```

**Contrôle de la maquette :** peut-on montrer du doigt la somme manquante **au départ** sans la confondre avec la dépense nette ? Au besoin, raccourcir le titre ou diviser l’exercice, pas les chiffres. Remplacer les clés `essai-*` par des clés uniques lors d’une intégration réelle ; vérifier les renvois, le sommaire et les décomptes avec `controle-kit`.
