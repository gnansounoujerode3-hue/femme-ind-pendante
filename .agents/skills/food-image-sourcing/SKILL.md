---
name: food-image-sourcing
description: Rechercher, comparer et documenter des images culinaires fidèles aux recettes, avec vérification des licences, de la résolution et de la provenance.
---

# Iconographie culinaire et droits

Skill local créé pour le projet. Il ne fournit ni banque d’images, ni accès payant, ni garantie juridique.

## Recherche
1. Lire la recette, sa variante, ses ingrédients et son dressage attendu avant de chercher une photo.
2. Rechercher le nom local et des variantes linguistiques : « amiwo poulet Bénin », « atassi rice beans Benin », « ablo steamed rice cakes », « Senegal chicken yassa ». Ne pas assimiler automatiquement deux plats proches.
3. Utiliser image_search ou les outils web disponibles dans la session. Sinon indiquer la limitation réseau et demander des photos fournies par l’utilisateur, ou proposer une illustration générée. Ne pas scraper un domaine inaccessible.
4. Consulter la page d’origine de chaque image, pas seulement la miniature ou le résultat de recherche. Les moteurs, Pinterest et les réseaux sociaux ne sont pas des sources de licence.
5. Favoriser : photos originales avec autorisation documentée ; photos commandées ; domaine public vérifié ; licences permettant explicitement l’usage prévu. Wikimedia Commons a des licences variables par fichier ; Unsplash et Pexels ont aussi leurs propres conditions à relire. « Gratuit à télécharger » ne signifie pas « réutilisable commercialement ».

## Validation du candidat
- Identifier le plat, l’accompagnement et la variante : un riz rouge générique n’illustre pas automatiquement l’amiwo.
- Comparer ingrédients visibles et préparation. Rejeter une photo avec ingrédients incompatibles ou présentation trompeuse.
- Vérifier netteté, lumière, absence de filigrane, résolution et espace pour recadrer.
- Calculer la résolution utile : pixels requis = largeur imprimée en pouces × résolution cible. À 300 ppp, 15 cm de large demandent environ 1772 pixels ; une couverture A4 pleine page demande davantage, plus le fond perdu.
- Préférer cohérence de lumière et vaisselle, sans uniformiser artificiellement les cultures représentées.

## Droits obligatoires
Avant toute intégration, enregistrer dans `assets/food/registry.json` : identifiant recette, chemin local, URL de la page source, URL du fichier si connue, auteur, licence exacte, URL ou preuve de licence, date de vérification, attribution, autorisation commerciale, droit de modification, modifications réalisées et statut.

Statuts : `pending` tant que non vérifié ; `approved` uniquement après vérification complète ; `rejected` si incompatible. Ne pas approuver automatiquement à partir du nom d’un site. Une licence NC ne convient pas à une vente ; une licence ND peut empêcher certains usages modifiés. Vérifier les obligations BY et SA au cas par cas, ainsi que les autres droits applicables. En cas de doute, ne pas utiliser.

Conserver une preuve datée des conditions lorsque permis, sans stocker de données sensibles ni d’images non autorisées dans Git. Générer les crédits depuis ce registre, et non de mémoire.

## Images générées
Demander l’accord si le choix entre photographie et illustration est important. Utiliser generate_image seulement si disponible ; suivre ses règles de présentation. Décrire précisément les ingrédients, le plat, le contenant et les textures. Étiqueter l’image comme illustration générée, jamais comme photo de la recette testée. Vérifier visuellement les défauts et le respect culturel. Les conditions du service restent à contrôler pour l’usage commercial. Les scripts seuls ne donnent aucun accès à ce service.

## Priorisation
Commencer par la couverture et une image par chapitre, puis les recettes prioritaires. Une absence de photo honnête vaut mieux qu’une photo de mauvais plat. Ne pas promettre « 100 photos libres de droits » avant acquisition et vérification effectives.
