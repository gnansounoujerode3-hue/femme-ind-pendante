---
name: ebook-quality
description: Contrôler la qualité d’un livre de recettes PDF ou EPUB avant livraison, y compris texte, images, liens, métadonnées et limites d’accessibilité.
---

# Contrôle avant publication

Skill local créé pour le projet.

## Vérifications automatiques
Exécuter `.venv/bin/python tools/audit_ebook.py` après génération. Lire les résultats : aucune vérification automatique ne garantit une recette réussie, une licence valide ou une belle composition.

Contrôler : 100 identifiants uniques ; titres et sections obligatoires ; PDF ouvrable ; présence des titres ; absence de pages vides ; polices incorporées ; liens internes ; dimensions des pages. Pour les images, utiliser Pillow pour contrôler pixels et format ; calculer la résolution à leur taille réelle d’utilisation. Consulter le registre de provenance et ses statuts.

## Contrôle visuel obligatoire
Avec PyMuPDF, rendre des pages en PNG à 120–160 ppp, puis les ouvrir avec read_file si disponible. Voir couverture, sommaire, ouverture de chapitre, recette la plus longue, page avec photo, index et dernière page. Parcourir aussi les miniatures de toutes les pages.

Vérifier : aucun chevauchement, texte coupé, titre isolé, crédit minuscule ou image étirée ; marges constantes ; contraste lisible ; alignements et numéros corrects. Tester les liens dans un lecteur PDF. Lire à 100 % sur écran et tester sur mobile ; ne pas déduire la lisibilité d’un simple zoom dans une grande page.

## PDF numérique
Conserver le texte sélectionnable. Fournir titre, langue lorsque possible, sommaire navigable et polices incorporées. Ne pas aplatir le livre en images. Pour un véritable PDF accessible, balisage et ordre de lecture demandent un travail dédié ; ne pas annoncer PDF/UA sans validation spécialisée.

## EPUB si demandé
Utiliser EbookLib pour construire un EPUB redistribuable : sections sémantiques, ordre logique, langue française, navigation, texte alternatif pertinent, crédits, images optimisées et styles simples. Ne pas convertir chaque page PDF en image. Valider avec EPUBCheck si disponible ; sinon annoncer que cette validation n’a pas été faite. Tester dans au moins un vrai lecteur. Installer EbookLib ne génère pas automatiquement un EPUB et ne remplace pas EPUBCheck.

## Bon à livrer
- Recettes non testées signalées ; adaptations annoncées.
- Images utilisées autorisées et créditées, ou illustrations générées signalées.
- Fichiers source et dépendances conservés.
- Audit technique et inspection visuelle effectués avec limites explicites.
- Une version impression exige le cahier des charges de l’imprimeur.
