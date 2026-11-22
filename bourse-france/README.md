# Mon dossier France — Trouver une bourse et candidater sans agence

Produit numérique en français pour les candidats d’Afrique francophone, avec un parcours pratique depuis le Bénin. Édition de novembre 2026, rentrée 2027. Produit indépendant, pas un service de dépôt. Aucun fichier n’a été mis en vente automatiquement.

## Pour l’acheteur

[Kit complet à livrer](Kit-Mon-dossier-France.zip) : trois fichiers à extraire dans un même dossier. On peut aussi les proposer séparément pour éviter la décompression sur téléphone.

1. [Guide de 27 pages](Mon-dossier-France.pdf) — sommaire et sources cliquables ; pour commencer, choisir sa piste page 3.
2. [Atelier Word](bonus/Atelier-dossier.docx) — huit gabarits à personnaliser ; ne jamais envoyer l’atelier entier à un jury.
3. [Suivi et budget](bonus/Suivi-et-budget.xlsx) — cinq onglets. Ouvrir dans un tableur qui recalcule les formules, puis faire une copie de travail. L’exemple chiffré est fictif ; le budget personnel est vierge.

## Pour la boutique, à conserver séparément

[Ressources de vente](vente/Ressources-Chariow.zip) : [texte de la fiche et proposition de prix](vente/Fiche-Chariow.md), [vignette 1080 × 1080](vente/Visuel-Chariow.png), [extrait public de 3 pages](vente/Extrait-gratuit.pdf). Le ZIP vendeur n’est pas le fichier à remettre aux acheteurs.

## Actualisation

Relire les [sources officielles](edition/sources.json) chez le financeur, l’établissement porteur et l’espace local **avant de relancer les ventes**. La page HTML actualisée de Campus France Bénin (étapes 4 et 5) signale une prolongation que son calendrier PDF initial ne reprend pas. Les exemples de dates, de frais et d’exonérations sont localisés ; ne pas simplement changer le millésime.

Le [manuscrit du guide](edition/guide.md) est séparé de la mise en page. Les modèles Word sont dans `edition/atelier.py`, les exemples du classeur et les formules dans `edition/tableur.py`. Penser aussi au texte de vente et au nombre de pages si l’édition change.

Pour régénérer depuis la racine du dépôt (Python 3.11+, polices DejaVu Sans et Serif, normales et grasses) :

```sh
python -m venv .venv
.venv/bin/pip install -r bourse-france/edition/requirements.txt
.venv/bin/python bourse-france/edition/fabriquer.py
.venv/bin/python bourse-france/edition/verifier.py
```

Le chemin des polices peut être défini avec `DOSSIER_FONTS`. La génération ne télécharge pas les sources et ne publie rien en ligne.
