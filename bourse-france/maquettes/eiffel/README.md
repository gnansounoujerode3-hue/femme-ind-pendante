# Épreuve mobile · Eiffel en master à Paris-Saclay

[Ouvrir la fiche PDF](Eiffel-master-Paris-Saclay.pdf?raw=true) · [Voir le rendu à 360 px de large](Eiffel-master-mobile.png)

Proposition pour la page 11 (« Deux dates : laquelle est la tienne ? ») de *Mon dossier France*. La première chose à repérer est le geste du candidat ; la date de l’établissement vient après. Cette page autonome n’est incluse ni dans le guide ni dans les archives de vente.

**Repères vérifiés pour la rentrée 2027–2028** (lecture du 18 novembre 2026) :

- [Université Paris-Saclay, « Niveau Master / Comment candidater »](https://www.universite-paris-saclay.fr/admission/bourses-et-aides-financieres/bourses-france-excellence-eiffel) : la consigne de prise de contact dit **avant le 26 novembre 2026**, sans heure. Elle vise la personne responsable de la formation choisie ; le lien se trouve sous son nom sur la fiche accessible depuis le [catalogue des masters](https://www.universite-paris-saclay.fr/formation/deuxieme-cycle). La procédure d’admission au master reste distincte.
- [Campus France, « Calendrier session 2027 »](https://www.campusfrance.org/fr/le-programme-de-bourses-france-excellence-eiffel) : **6 janvier 2027 inclus** pour le dépôt par les établissements, pas pour une candidature étudiante directe. Relire les deux appels avant diffusion ou changement de rentrée.

Pour refaire **uniquement** le PDF et son image, depuis la racine avec les dépendances de `bourse-france/edition/requirements.txt` :

```sh
.venv/bin/python bourse-france/maquettes/eiffel/composer.py
```

Le script contrôle la page, le texte du bandeau et les destinations et tailles des trois zones tactiles. L’image est un rendu du PDF, pas un essai sur un téléphone physique.
