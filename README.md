# Femme indépendante — créations interactives

Ce dépôt réunit deux ressources autonomes en français pour aider les femmes à créer plus d’autonomie et de choix au quotidien.

## Guide « Mon argent, ma liberté »

Un guide d’indépendance financière au féminin, conçu depuis le Bénin, pour les femmes d’Afrique et de sa diaspora. Les fêtes sont le cas pratique de départ ; le sujet principal est l’autonomie durable : état des lieux, gestion et accès à son argent, budget et réserve, développement des revenus, activité viable, épargne et investissement prudent, pouvoir financier dans le couple, protections et plan de 90 jours.

- **Page de présentation et version web lisible :** `ebook/index.html`
- **PDF prêt à lire ou imprimer :** `ebook/Mon-argent-ma-liberte.pdf`
- **Télécharger le PDF depuis la page :** bouton « Télécharger le PDF » (fichier de 24 pages avec signets de navigation)
- Les exercices du carnet sont enregistrés localement dans le navigateur ; aucune donnée n’est envoyée.
- Illustrations originales, motifs géométriques inspirés de l’art textile ouest-africain, palette indigo / or / corail / teal, polices auto-hébergées.
- Le contenu donne des repères généraux, et invite à vérifier auprès de sources locales les règles financières, juridiques et professionnelles applicables.

## Workbook interactif — Jour 2

Le workbook permet de valider une idée de produit digital, d’écrire sa promesse et de préparer sa structure. Il comprend dix sections, la sauvegarde automatique, une progression, des signatures, des réponses guidées et l’export PDF ou JSON.

- **Page web :** `index.html`
- **Sections :** `accueil`, `objectif`, `validation`, `promesse`, `format`, `structure`, `ia`, `felicitations`, `declaration`, `prochaines-etapes`.
- Les réponses et signatures restent dans le stockage local du navigateur.

## Lancer le projet

Node.js 18 ou plus récent suffit, sans dépendances npm :

```bash
npm start
```

Puis ouvrir `http://localhost:4173/` pour le workbook, ou `http://localhost:4173/ebook/` pour le guide d’indépendance financière.

```bash
npm run check
```

Le guide propose des informations générales d’éducation financière ; il ne remplace pas un conseil financier, juridique ou professionnel adapté au pays et à la situation de la lectrice.
