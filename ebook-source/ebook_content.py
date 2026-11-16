# -*- coding: utf-8 -*-
"""Contenu éditorial structuré de l'ebook et du Workbook Jour 2 rempli,
strictement aligné sur WORKBOOK-OFFICIEL-JOUR-2-CREE-TON-PREMIER-PRODUIT-DIGITAL.pdf.
"""

BUDGET_GUIDE = [
    {
        "tier": "Petit",
        "label": "Petit budget",
        "range": "Moins de 50 000 FCFA (environ 0 à 80 $ USD)",
        "desc": (
            "Activités démarrables depuis chez soi avec un smartphone, une compétence "
            "ou un petit kit de base. Zéro local commercial exigé au départ : idéal "
            "pour tester le marché dès cette semaine."
        ),
    },
    {
        "tier": "Moyen",
        "label": "Budget moyen",
        "range": "50 000 à 300 000 FCFA (environ 80 à 500 $ USD)",
        "desc": (
            "Nécessite un premier stock ciblé, un équipement semi-pro (moulin, machine "
            "à coudre, kit solaire, congélateur, outillage) ou une petite enveloppe "
            "de mise en marché locale."
        ),
    },
    {
        "tier": "Structuré",
        "label": "Budget structuré",
        "range": "300 000 FCFA et plus (500 $ USD et +)",
        "desc": (
            "Projets à forte barrière d'entrée (atelier équipé, chambres froides, "
            "véhicule utilitaire, laboratoire agréé ou équipe salariée) accessibles "
            "via épargne, association, tontine business ou co-investissement diaspora."
        ),
    },
]

PART_01_INTRO = {
    "num": "01",
    "kicker": "PARTIE 01 • INTRODUCTION",
    "title": "Pourquoi 2027 est le meilleur moment pour lancer ton business en Afrique",
    "workbook_question": "Réponse à la section 01 du Workbook : Quel est le problème et pourquoi est-il important ?",
    "lead": (
        "Chaque jour, des milliers de jeunes diplômés, de salariés, de femmes actives "
        "et de membres de la diaspora africaine rêvent d'indépendance financière. "
        "Pourtant, la majorité reste bloquée au point de départ pour deux raisons très "
        "simples : soit ils ne savent pas quelle idée rentable choisir face aux réalités "
        "locales, soit ils copient un business saturé et perdent leurs économies faute de méthode."
    ),
    "problem_blocks": [
        (
            "Le vrai blocage n'est pas le manque de courage, mais le manque de filtre",
            "En Afrique francophone, l'envie d'entreprendre est immense. Mais entre les idées "
            "importées d'Europe qui ne collent pas au pouvoir d'achat local et les projets "
            "qui demandent des millions de FCFA avant même le premier client, beaucoup "
            "finissent par abandonner avant d'avoir essayé."
        ),
        (
            "Pourquoi agir maintenant pour 2027 ?",
            "L'année 2027 marque l'accélération de cinq vagues économiques majeures sur le "
            "continent. Ceux qui se positionnent aujourd'hui avec une offre simple, locale "
            "et validée rapidement prendront une longueur d'avance décisive."
        ),
    ],
    "trends_2027": [
        (
            "1. L'explosion des paiements mobiles et du commerce WhatsApp",
            "Du Bénin au Sénégal, de la Côte d'Ivoire au Cameroun, vendre sans boutique "
            "physique via WhatsApp Business, Facebook, TikTok et Mobile Money est devenu la norme."
        ),
        (
            "2. Le virage du « Consommons Local » et de la transformation alimentaire",
            "Face à la hausse des prix des produits importés, les ménages et la diaspora "
            "plébiscitent les farines, jus, épices, cosmétiques et textiles fabriqués localement avec hygiène et bel emballage."
        ),
        (
            "3. L'intelligence artificielle accessible sur simple smartphone",
            "Un indépendant équipé d'IA produit désormais en 2 heures des visuels, scripts, "
            "devis, formations ou contenus clients qui demandaient autrefois une agence entière."
        ),
        (
            "4. L'urgence énergétique et l'économie verte",
            "Le coût élevé du réseau électrique pousse commerces, exploitations agricoles et "
            "ménages vers les kits solaires, le froid solaire, le recyclage et l'eau potable de proximité."
        ),
        (
            "5. L'externalisation de services vers la diaspora et les PME locales",
            "Les PME africaines cherchent à externaliser comptabilité, recrutement, livraison "
            "et relation client ; la diaspora paie volontiers des prestataires fiables restés au pays."
        ),
    ],
    "profiles": [
        ("Étudiant / Jeune diplômé", "Petit budget (< 50 000 FCFA)", "Secteurs 04 (Digital/IA), 05 (EdTech), 03 (Social commerce), 12 (Contenu)"),
        ("Salarié en quête d'un revenu bis", "Petit à Moyen budget", "Secteurs 02 (Livraison weekend), 08 (Immobilier), 16 (B2B), 17 (Fintech)"),
        ("Femme active / Maman entrepreneure", "Petit à Moyen budget", "Secteurs 01 (Agro-transfo), 06 (Beauté), 07 (Mode), 18 (Enfance)"),
        ("Artisan / Technicien qualifié", "Moyen budget", "Secteurs 10 (Solaire), 15 (Artisanat), 20 (BTP & Réparation)"),
        ("Investisseur / Diaspora en partenariat", "Budget Structuré", "Secteurs 09 (Logistique), 13 (Tourisme), 14 (Élevage/Pisciculture), 01 (Unités)"),
    ],
}

PART_02_ERRORS = {
    "num": "02",
    "kicker": "PARTIE 02 • ERREURS À ÉVITER",
    "title": "Les 7 erreurs fatales qui tuent 80 % des nouveaux business en Afrique",
    "workbook_question": "Réponse à la section 02 du Workbook : Quelles sont les erreurs fréquentes que les gens font ?",
    "intro": (
        "Avant même de choisir ton idée parmi les 500 de ce catalogue, protège ton énergie "
        "et ton capital. Ces 7 erreurs reviennent dans presque tous les échecs évitables "
        "observés sur le terrain."
    ),
    "errors": [
        (
            "Erreur 1 : Lancer sur un « coup de cœur » sans vérifier la douleur client",
            "Conséquence : Tu fabriques un beau produit ou ouvres un service dont personne n'a besoin en urgence.",
            "Réflexe 2027 : Applique la méthode VIN (Valeur, Intensité, Nombre) et parle à 5 vrais clients avant d'acheter du stock."
        ),
        (
            "Erreur 2 : Copier le voisin exactement à l'identique",
            "Conséquence : Quand trois boutiques vendent le même produit au même carrefour, la seule arme restante est de casser les prix — et tout le monde perd.",
            "Réflexe 2027 : Change au moins un angle fort : qualité d'emballage, livraison à domicile, horaire tardif, abonnement ou cible précise."
        ),
        (
            "Erreur 3 : Immobiliser 80 % de son capital dans le décor ou un local",
            "Conséquence : Loyer, caution, enseigne et meubles engloutissent ta trésorerie avant que tu n'aies encaissé ton 10e client.",
            "Réflexe 2027 : Démarre depuis chez toi, sur commande, en kiosque mobile ou en partenariat avec un point déjà existant."
        ),
        (
            "Erreur 4 : Mélanger la caisse du business et les dépenses personnelles",
            "Conséquence : Tu as l'impression de bien vendre, mais impossible de renouveler le stock le mois suivant parce que l'argent a payé loyer, cérémonies et imprévus familiaux.",
            "Réflexe 2027 : Deux portefeuilles / comptes Mobile Money strictement séparés dès le Jour 1, et verse-toi un salaire fixe ou un pourcentage clair."
        ),
        (
            "Erreur 5 : Vendre à crédit « aux connaissances » sans règles écrites",
            "Conséquence : Ton fonds de roulement reste bloqué chez des clients qui disparaissent quand il faut payer, et tu perds à la fois l'argent et la relation.",
            "Réflexe 2027 : Paiement comptant ou acompte minimum de 50 % à la commande, relance automatique par WhatsApp avant livraison."
        ),
        (
            "Erreur 6 : Fixer ses prix sans calculer les coûts cachés",
            "Conséquence : Tu oublies les frais de transport, pertes/invendus, emballages, données internet, frais de retrait Mobile Money et ton propre temps : tu travailles à perte.",
            "Réflexe 2027 : Additionne TOUS les coûts directs, ajoute 15 % d'imprévus puis ta marge nette avant d'annoncer ton tarif."
        ),
        (
            "Erreur 7 : Attendre la perfection absolue avant de se lancer",
            "Conséquence : Pendant que tu peaufines ton logo, tes statuts ou ton site pendant 6 mois, un concurrent imparfait mais rapide prend déjà le marché.",
            "Réflexe 2027 : Comme le rappelle le Workbook Jour 2, oublie la perfection. Sors une version simple, encaisse tes 10 premiers clients et améliore en V2.0."
        ),
    ],
}

PART_04_VALIDATION = {
    "num": "04",
    "kicker": "PARTIE 04 • ÉTAPE 2",
    "title": "Valide ton Top 3 en 48 heures avant de dépenser 1\u00A0FCFA",
    "workbook_question": "Réponse à la section 04 du Workbook : Deuxième action concrète — Filtrer et prouver la demande réelle.",
    "intro": (
        "Tu viens de repérer 3 à 5 idées prometteuses dans les 500 fiches de la Partie 03 ? "
        "Ne te lance pas encore à l'aveugle. En moins de 48 heures et avec zéro dépense "
        "de production, tu vas soumettre ton Top 3 au filtre implacable de la méthode VIN "
        "et du terrain."
    ),
    "vin_reminders": [
        ("V — Valeur (Problème précis)", "En une phrase : quelle douleur ou envie précise ton client paie-t-il pour résoudre ? (Ex. : gagner du temps, manger sain, augmenter ses ventes, réparer vite)."),
        ("I — Intensité (/10)", "Le problème est-il urgent ou secondaire ? Vise au moins 7/10 : si le client peut attendre 6 mois sans agir, il reportera son achat."),
        ("N — Nombre (Volume solvable)", "Combien de clients capables de payer vivent ce problème dans ton quartier, ta ville ou ta communauté en ligne chaque semaine ?"),
    ],
    "steps_48h": [
        ("Heure 0 à 4 : Sélectionne 3 idées finalistes", "Une idée en « Petit budget » (démarrage immédiat), une qui exploite tes contacts actuels, et ton coup de cœur rentable."),
        ("Heure 4 à 18 : Remplis la grille de score ci-dessous", "Note chaque idée de 1 à 5 sur 6 critères concrets (/30). Élimine immédiatement toute idée en dessous de 20/30."),
        ("Heure 18 à 36 : Le test des 5 vraies conversations", "Appelle ou rencontre 5 personnes correspondant à ta cible. Ne demande pas « Est-ce que tu aimes mon idée ? » (tout le monde dit oui par politesse), demande : « Combien as-tu dépensé pour ce besoin le mois dernier ? Et si je te livre tel résultat vendredi pour X FCFA, tu commandes ? »."),
        ("Heure 36 à 48 : Preuve par l'engagement", "Une idée est officiellement validée lorsque au moins 2 personnes sur 5 acceptent de précommander, verser un petit acompte ou réserver un créneau daté."),
    ],
    "scoring_criteria": [
        ("1. Besoin urgent et prouvé (méthode VIN)", "Les clients cherchent déjà une solution et dépensent de l'argent pour cela."),
        ("2. Budget de départ accessible tout de suite", "Tu disposes déjà du capital nécessaire sans t'endetter dangereusement."),
        ("3. Compétence ou apprentissage rapide (< 7 jours)", "Tu sais faire, ou tu peux t'associer / te former en quelques jours."),
        ("4. Cycle de vente court (< 7 jours)", "Tu peux produire, livrer et encaisser dans la même semaine."),
        ("5. Marge nette saine (>= 30 %)", "Après transport, emballage et frais Mobile Money, il te reste un vrai bénéfice."),
        ("6. Récurrence possible", "Le même client peut racheter chaque semaine, chaque mois ou recommander 3 proches."),
    ],
    "example_box_title": "Exemple concret rempli : Idée #002 — Chips de banane plantain aromatisées",
    "example_box_lines": [
        "• Méthode VIN : V = Offrir un snack croquant, propre et bien emballé pour les pauses bureau/écoles • I = 8/10 (demande quotidienne immédiate) • N = Massif (bureaux, supérettes, campus, feux tricolores).",
        "• Score sur 30 : Besoin (5/5) + Budget < 50k FCFA (5/5) + Apprentissage rapide (5/5) + Cycle de vente 24h (5/5) + Marge > 40 % (4/5) + Réachat hebdo (5/5) = 29 / 30 → Feu vert immédiat !",
        "• Test 48h réussi : 2 lots tests préparés le soir, proposés le lendemain à 10 collègues et 2 supérettes de quartier → 8 sachets vendus comptant + 1 commande hebdomadaire confirmée avant d'acheter la friteuse pro.",
    ],
}

PART_05_LAUNCH = {
    "num": "05",
    "kicker": "PARTIE 05 • ÉTAPE 3",
    "title": "Plan d'action en 7 jours pour lancer et encaisser tes premiers clients",
    "workbook_question": "Réponse à la section 05 du Workbook : Troisième action concrète — Passer de l'idée validée au premier encaissement.",
    "intro": (
        "Ton idée n°1 est validée. Voici la feuille de route exacte sur 7 jours pour "
        "transformer cette décision en premières ventes réelles — sans site web coûteux, "
        "sans bureau et sans attendre des mois."
    ),
    "days": [
        ("Jour 1", "Verrouille ton offre et ton prix", "Définis 1 offre d'entrée simple (format découverte + offre standard), calcule tes coûts complets et rédige ta promesse en 1 phrase claire."),
        ("Jour 2", "Prépare ton « minimum vendable »", "Crée 3 photos propres à la lumière du jour (ou une fiche PDF/Canva claire), configure ton profil WhatsApp Business (catalogue + numéro Mobile Money prêt)."),
        ("Jour 3", "Liste tes 30 premiers acheteurs probables", "Note 10 connaissances directes, 10 contacts professionnels/quartier et 10 groupes Facebook/WhatsApp pertinents où ta cible se trouve déjà."),
        ("Jour 4", "Lance l'offensive directe (30 messages)", "Envoie le Script 1 personnalisé aux 20 premiers contacts et publie 1 statut WhatsApp + 1 post Facebook avec une offre de lancement limitée aux 5 premiers."),
        ("Jour 5", "Convertis, encaisse et livre impeccablement", "Encaisse un acompte ou paiement à la commande, livre avec 10 minutes d'avance ou un petit mot d'attention qui crée la surprise positive."),
        ("Jour 6", "Récolte les preuves et active le bouche-à-oreille", "Demande un court avis vocal ou écrit WhatsApp à tes premiers clients + propose « 1 recommandation = 1 petit bonus offert »."),
        ("Jour 7", "Fais ton bilan cash et prépare la semaine 2", "Applique la règle des 3 enveloppes sur tes encaissements, note ce qui a le mieux marché et double l'action sur le canal le plus rentable."),
    ],
    "scripts": [
        (
            "Script 1 — Message WhatsApp cercle proche / réseau tiède",
            "« Bonjour [Prénom], j'espère que tu vas bien ! Je lance cette semaine [nom de ton service/produit] pour aider [cible] à [bénéfice concret] en [délai], sans [principal blocage]. Pour mes 5 premiers clients de lancement d'ici samedi, je propose le pack à [Prix] au lieu de [Prix normal]. Est-ce que ça t'intéresse, ou connais-tu quelqu'un autour de toi qui en a besoin en ce moment ? »"
        ),
        (
            "Script 2 — Post Facebook / Statut WhatsApp à fort impact",
            "« Vous cherchez [résultat concret] à [Ville/Quartier] sans [galère habituelle] ? Dès cette semaine, nous lançons [Nom de l'offre] : [2 avantages simples + délai de livraison]. Offre de lancement valable jusqu'à dimanche pour les 10 premières commandes. Écrivez « INFOS » en commentaire ou envoyez un message direct sur WhatsApp au [Numéro] pour réserver votre place. »"
        ),
        (
            "Script 3 — Répondre à l'objection « C'est un peu cher »",
            "« Je comprends tout à fait ! C'est justement pour éviter les mauvaises surprises que ce tarif inclut [élément de qualité/garantie/service inclus]. Pour démarrer plus léger aujourd'hui, on peut commencer par notre formule Essentiel à [Prix réduit / petit format] afin que tu testes la qualité par toi-même dès cette semaine. On part sur celle-ci ? »"
        ),
    ],
    "pricing_formula": [
        "1. Additionne tous tes coûts directs (matière première, emballage, livraison, électricité/gaz, frais Mobile Money).",
        "2. Ajoute la valeur de ton temps (même modeste au début) + 10 à 15 % pour les imprévus et pertes.",
        "3. Ajoute ta marge bénéficiaire cible (minimum 30 % sur les produits, 50 %+ sur les services) pour obtenir ton Prix Plancher.",
    ],
    "envelopes": [
        ("Enveloppe 1 — 50 % Réinvestissement & Stock", "Reste intouchable dans le compte pro pour racheter les matières premières, améliorer l'emballage et faire grandir l'activité."),
        ("Enveloppe 2 — 30 % Charges, Réserve & Imprévus", "Couvre transport, crédit internet, marketing, impôts/formalisation et coussin de sécurité en cas de semaine creuse."),
        ("Enveloppe 3 — 20 % Rémunération du Fondateur", "Ton salaire clair et officiel. C'est uniquement cette enveloppe qui finance tes dépenses personnelles : jamais la caisse brute !"),
    ],
}

CONCLUSION_CONTENT = {
    "kicker": "CONCLUSION • PROCHAIN PAS",
    "title": "Oublie la perfection, passe à l'action dès les 48 prochaines heures",
    "workbook_question": "Réponse à la section Conclusion du Workbook : Quel est le prochain pas pour le lecteur ?",
    "message": (
        "Tu as maintenant entre les mains 500 idées concrètes adaptées aux réalités africaines "
        "de 2027, la grille pour éviter les pièges qui coûtent cher, la méthode VIN pour "
        "valider en 48 heures et le plan exact sur 7 jours pour encaisser tes premiers clients. "
        "Mais la différence entre un lecteur qui rêve et un entrepreneur qui encaisse tient "
        "en une seule chose : l'action immédiate."
    ),
    "mantra": "« Ton premier jour de vente ne sera pas parfait, et c'est normal. L'important est de lancer une version simple, d'encaisser ton premier client réel et d'améliorer en version 2.0. »",
    "action_sheet": [
        "Mon secteur retenu (01 à 20) : ________________________________________________",
        "Mon idée choisie (#___) : _____________________________________________________",
        "Mon budget de départ réaliste : _______________________ FCFA",
        "Ma promesse en 1 phrase (Comment ___ en ___ sans ___) : _______________________",
        "Mes 5 premiers prospects à contacter demain matin : ___________________________",
        "Date de mon premier encaissement cible : ______________________________________",
    ],
    "next_steps_reader": [
        "1. Dans les 2 prochaines heures : choisis 1 seule idée parmi tes 3 finalistes (commence par celle que tu peux tester au moindre coût).",
        "2. Dans les 48 prochaines heures : réalise les 5 conversations terrain et publie ta première offre test auprès de 10 proches.",
        "3. À J+7 : récolte les avis de tes premiers acheteurs et passe directement à ta version 2.0 améliorée.",
    ],
}

def get_workbook_pages_data(config, ebook_pages=None):
    """Retourne les données exactes pour les 10 pages du Workbook Jour 2 rempli."""
    author = config.get("author_name", "[Ton Nom / Ta Marque]")
    date_str = config.get("date_creation", "16 novembre 2026")
    title = config.get("ebook_title", "500 Idées de Business à Lancer en Afrique en 2027")
    promise = config.get(
        "promise_formula",
        "Comment choisir, valider et lancer ton business rentable en Afrique en 2027 en 7 jours sans gros capital ni peur de te tromper."
    )
    pages_txt = f"{ebook_pages} pages" if ebook_pages else "environ 60 pages"
    return {
        "author": author,
        "date": date_str,
        "title": title,
        "promise": promise,
        "page1": {
            "badge": "WORKBOOK OFFICIEL – JOUR 2",
            "title": "CRÉE TON PREMIER PRODUIT DIGITAL",
            "subtitle": f"Dossier d'application complété pour le projet : « {title} »",
            "welcome": (
                "Bienvenue dans ton guide pratique pour transformer ton idée en un véritable produit "
                "digital. Ce workbook est conçu spécialement pour toi, entrepreneur africain francophone, "
                "qui souhaites passer à l'action dès aujourd'hui. Pas besoin d'être expert en technologie "
                "ou d'avoir des années d'expérience. Ce qui compte, c'est ta volonté d'avancer et de créer "
                "quelque chose de concret qui aide les autres. Dans les pages suivantes, la méthode exacte "
                "du Workbook Jour 2 (valider → structurer → créer étape par étape) est appliquée de bout "
                "en bout à ton ebook sur les 500 idées de business en Afrique en 2027."
            ),
            "summary_rows": [
                ("Produit créé", title),
                ("Cible prioritaire", "Entrepreneurs & porteurs de projets en Afrique francophone + diaspora"),
                ("Format retenu", "PDF professionnel prêt à diffuser + sources éditables"),
                ("Créateur / Marque", author),
                ("Date de réalisation", date_str),
            ],
        },
        "page2": {
            "kicker": "PAGE 2 • OBJECTIF",
            "title": "À la fin de ce workbook, tu as un produit",
            "intro": (
                "Oublie la perfection. Ton premier produit ne sera pas parfait, et c'est normal. "
                "Ce qui importe aujourd'hui, c'est de passer à l'action et de créer quelque chose "
                "de réel que tu pourras améliorer avec le temps. Chaque page contient des exercices "
                "concrets appliqués ici directement à ton ebook."
            ),
            "quote": "→ À la fin, tu pourras écrire : « J'ai créé mon premier produit digital. »",
            "commitment": [
                ("Nom / Marque", author),
                ("Date", date_str),
                ("Signature / Statut", f"Validé — Engagement tenu pour « {title} »"),
            ],
        },
        "page3": {
            "kicker": "PAGE 3 • VALIDATION",
            "title": "Validation Express de ton Idée (Méthode VIN)",
            "intro": (
                "Avant de créer ton produit, assure-toi que ton idée répond à un vrai besoin. "
                "VIN signifie Valeur, Intensité et Nombre. Si ces trois éléments sont élevés, "
                "ton idée est validée et tu peux avancer en toute confiance."
            ),
            "V": (
                "Des milliers de jeunes, salariés, femmes actives et membres de la diaspora en "
                "Afrique francophone veulent entreprendre en 2027, mais restent bloqués par manque "
                "d'idées concrètes adaptées au terrain, à leur petit budget et sans méthode simple "
                "pour valider avant d'investir."
            ),
            "I_score": "9 / 10",
            "I_exp": (
                "Le chômage, la hausse du coût de la vie et le besoin d'indépendance financière rendent "
                "la création d'une source de revenus urgente. Beaucoup perdent leurs maigres économies "
                "dans des business mal ciblés faute de filtre et de plan de démarrage."
            ),
            "N": (
                "Marché massif et très répandu : des millions de francophones en Afrique de l'Ouest "
                "et Centrale (Bénin, Côte d'Ivoire, Sénégal, Togo, Cameroun, Burkina Faso, Mali, RDC, "
                "Guinée, Gabon...) et dans la diaspora cherchent ce type de feuille de route chaque mois."
            ),
            "conclusion": "Mini-conclusion : V (problème réel) + I (9/10) + N (marché massif) sont élevés → Idée 100 % validée !",
        },
        "page4": {
            "kicker": "PAGE 4 • PROMESSE",
            "title": "Transformation de ton Idée en Promesse Claire",
            "intro": (
                "Ton produit doit offrir une transformation concrète à tes lecteurs. Plus ta promesse "
                "est précise (pour qui, quel résultat, en combien de temps), plus elle est convaincante."
            ),
            "q1": "Les futurs entrepreneurs africains francophones (étudiants, salariés, femmes actives, commerçants et diaspora) cherchant un business rentable et réaliste pour 2027.",
            "q2": "Choisir une activité adaptée à son budget réel (Petit, Moyen ou Structuré), la valider en 48 heures sur le terrain et lancer les premières ventes concrètes.",
            "q3": "En 7 jours (48 heures de filtrage et validation terrain + 5 jours de lancement commercial).",
            "formula_template": "« Comment _________________ en _________________ sans _________________. »",
            "formula_filled": f"« {promise} »",
        },
        "page5": {
            "kicker": "PAGE 5 • FORMAT",
            "title": "Choisis ton Format (Simple et Rapide)",
            "reasons_pdf": [
                "Facile à créer et mettre à jour avec des outils accessibles",
                "Compatible avec tous les appareils (téléphones Android/iPhone, tablettes, PC)",
                "Professionnel et crédible pour vendre sur WhatsApp, Chariow, Selar ou Maketou",
                "Rapide à produire pour passer à l'action sans blocage technique",
                "Parfait pour tester ton idée et encaisser avant de créer des vidéos",
            ],
            "why_chosen": (
                "Le PDF s'ouvre instantanément sur smartphone même avec une connexion faible, "
                "se livre automatiquement par WhatsApp ou Mobile Money, se lit hors ligne et "
                "offre une vraie valeur perçue de livre de référence."
            ),
            "pages_note": (
                "Recommandation de base du workbook : 5 à 15 pages pour un premier mini-guide. "
                f"Pour honorer la promesse réelle de « 500 idées détaillées », l'édition finale publiée "
                f"compte exactement {pages_txt} structurées en 20 secteurs, accompagnée d'un extrait gratuit "
                "idéal de 10 pages (Couverture + Parties 01, 02 et début Secteur 01) conforme au format court."
            ),
            "provisional_title": title,
        },
        "page6": {
            "kicker": "PAGE 6 • STRUCTURE",
            "title": "Structure Ton Produit en 5 Parties + Conclusion",
            "parts": [
                ("01", "Introduction", "Le problème du manque de filtre entrepreneurial en Afrique et pourquoi les 5 vagues économiques de 2027 créent une opportunité historique (+ guide des budgets)."),
                ("02", "Erreurs à éviter", "Les 7 erreurs fatales qui ruinent les débutants (copier sans se différencier, tout mettre dans le local, mélanger les caisses, vendre à crédit, attendre la perfection)."),
                ("03", "Étape 1", "Sélectionner son idée : catalogue complet des 500 idées classées en 20 secteurs porteurs Afrique 2027 (25 idées/secteur avec budget Petit, Moyen ou Structuré)."),
                ("04", "Étape 2", "Valider son Top 3 en 48 heures avant d'investir 1\u00A0FCFA grâce à la grille de notation /30, la méthode VIN et le test des 5 vraies conversations."),
                ("05", "Étape 3", "Lancer son business en 7 jours : feuille de route jour par jour (J1 à J7), 3 scripts WhatsApp/Facebook, calcul du prix juste et règle des 3 enveloppes."),
                ("End", "Conclusion", "Engagement écrit du lecteur sur 48h, passage à l'action imparfait mais immédiat, puis page auteur personnalisable et prise de contact."),
            ],
        },
        "page7": {
            "kicker": "PAGE 7 • IA & CHECKLIST",
            "title": "Utilise l'IA pour Générer Ton Contenu Rapidement",
            "prompt_template": (
                "Agis comme un expert pédagogique. Crée un guide structuré sur [sujet] destiné "
                "à [type de personne]. Le guide doit être clair, simple, pratique et structuré en "
                "étapes. Inclure une introduction motivante, 3 à 5 étapes détaillées et une conclusion actionnable."
            ),
            "prompt_applied": (
                "« Agis comme un expert pédagogique et analyste marché africain. Crée un guide structuré "
                "sur [500 idées de business rentables à lancer en Afrique en 2027, réparties en 20 secteurs "
                "et 3 niveaux de budget, avec validation en 48h et plan de lancement en 7 jours] destiné "
                "à [des entrepreneurs africains francophones et membres de la diaspora voulant démarrer "
                "vite sans gros capital]. Le guide doit être clair, simple, pratique et structuré en "
                "étapes. Inclure une introduction motivante, les 7 erreurs à éviter, 3 étapes détaillées "
                "(Choisir, Valider, Lancer) et une conclusion actionnable. »"
            ),
            "how_to_use": [
                "1. Prompt copié et adapté avec le sujet précis et la cible Afrique 2027",
                "2. Génération structurée en 20 secteurs × 25 fiches uniques (500 idées sans doublon)",
                "3. Adaptation locale : montants en FCFA & USD, Mobile Money, réalités terrain 2027",
                "4. Révision linguistique et cohérence éditoriale complète",
                "5. Mise en page professionnelle avec couverture originale et typographie dédiée",
                "6. Export en PDF final vérifié + fichiers sources éditables pour personnalisation",
            ],
            "checklist": [
                ("J'ai généré le contenu avec l'IA", True),
                ("J'ai relu et corrigé (500 idées uniques vérifiées, français soigné)", True),
                ("J'ai simplifié le langage (phrases courtes, actionnables)", True),
                ("J'ai personnalisé avec mes exemples (réalités Afrique francophone 2027)", True),
                ("J'ai mis en page dans un gabarit éditorial soigné (couverture + sommaire)", True),
                ("J'ai enregistré en format PDF (500-Idees-de-Business-a-Lancer-en-Afrique-en-2027.pdf)", True),
                ("J'ai testé l'ouverture du fichier (inspection visuelle de contrôle)", True),
            ],
            "important_note": (
                "Important : Personnalise ebook-source/author_config.json avec ton vrai nom, ton "
                "histoire (3-4 lignes) et ton numéro WhatsApp, puis relance le script pour obtenir "
                "ta version signée à 100 % !"
            ),
        },
        "page8": {
            "kicker": "PAGE 8 • RÉCAPITULATIF",
            "title": "Félicitations ! Tu es presque au bout",
            "intro": (
                "Beaucoup parlent de créer un produit digital, mais peu passent réellement à l'action. "
                "Voici le bilan exact des 5 étapes du Workbook Jour 2 validées pour ton ebook :"
            ),
            "recap_cards": [
                ("1. Tu as validé ton idée", "Méthode VIN appliquée (Valeur claire, Intensité 9/10, Nombre massif)", "VALIDÉ"),
                ("2. Tu as défini ta promesse", "Formule claire en 7 jours sans gros capital ni peur de se tromper", "VALIDÉ"),
                ("3. Tu as choisi ton format", "PDF haute lisibilité mobile + sources Markdown & JSON éditables", "VALIDÉ"),
                ("4. Tu as structuré ton contenu", "5 parties exactes (Intro, Erreurs, 500 Idées, Validation, Lancement) + Conclusion", "VALIDÉ"),
                ("5. Tu as créé et mis en page", "Ebook complet produit, vérifié et prêt à diffuser dès aujourd'hui", "VALIDÉ"),
            ],
        },
        "page9": {
            "kicker": "PAGE 9 • DÉCLARATION OFFICIELLE",
            "title": "Je confirme avoir créé mon premier produit digital",
            "declaration": [
                ("Nom / Marque", author),
                ("Signature", "____________________________________ (À parapher après personnalisation)"),
                ("Date", date_str),
                ("Titre de mon produit", title),
            ],
            "fb_action": "Action immédiate : Publie dans le groupe Facebook avec une capture de la couverture de ton ebook !",
            "social_posts": [
                (
                    "Modèle 1 — Victoire communautaire (Workbook Jour 2)",
                    "« J'ai créé mon premier produit digital ! [Photo de couverture] Après avoir appliqué étape par étape la méthode VIN, défini ma promesse et structuré les 5 parties, voici enfin mon ebook : \"500 Idées de Business à Lancer en Afrique en 2027\". Pas besoin d'attendre la perfection pour passer à l'action. Merci à la communauté pour l'élan ! »"
                ),
                (
                    "Modèle 2 — Publication valeur & autorité",
                    "« Tu veux entreprendre en 2027 mais tu te demandes par quel business commencer avec ton budget actuel ? J'ai réuni 500 idées concrètes réparties en 20 secteurs africains (du petit budget < 50 000 FCFA aux projets structurés) + une méthode en 48h pour tester avant d'investir. Commente \"2027\" si tu veux découvrir le sommaire ! »"
                ),
                (
                    "Modèle 3 — Appel à l'action lancement / précommande",
                    "« OFFRE DE LANCEMENT : Mon nouveau guide \"500 Idées de Business à Lancer en Afrique en 2027\" est disponible en PDF instantané sur téléphone. En bonus : les 7 erreurs à éviter et le plan exact des 7 premiers jours avec scripts WhatsApp. Écris-moi en privé ou sur WhatsApp pour recevoir ton exemplaire dès aujourd'hui. »"
                ),
            ],
        },
        "page10": {
            "kicker": "PAGE 10 • PROCHAINS PAS",
            "title": "Et maintenant ? Tes prochains pas",
            "steps": [
                (
                    "1. Lance ton produit (10 personnes de ton entourage)",
                    "Partage dès aujourd'hui le PDF (ou les 10 premières pages en extrait gratuit) à 10 personnes ciblées pour récolter leurs vrais retours en 48 heures."
                ),
                (
                    "2. Améliore-le (Version 2.0)",
                    "Note quelles idées ont reçu le plus de questions. Pour la V2.0, ajoute par exemple des fiches chiffrées détaillées sur les 20 idées favorites de tes premiers lecteurs."
                ),
                (
                    "3. Crée le suivant avec la même méthode",
                    "Produits dérivés faciles à lancer ensuite : (a) « 50 Business à lancer avec moins de 25 000 FCFA », (b) « Modèles de business plan simplifiés sur WhatsApp & Excel », (c) « Pack scripts de vente Afrique 2027 »."
                ),
            ],
            "whatsapp_testers": (
                "Message WhatsApp prêt à envoyer à tes 10 premiers testeurs :\n"
                "« Salut [Prénom] ! Je viens de finaliser mon tout premier ebook pratique : \"500 Idées de Business à Lancer en Afrique en 2027\" (20 secteurs + méthode pour valider en 48h et lancer en 7 jours). Comme ton avis compte beaucoup pour moi, je t'envoie le PDF en avant-première. Tu peux me dire d'ici 48h : 1) quelle idée t'a le plus marqué, et 2) ce que tu aimerais voir approfondi dans la version 2.0 ? Un grand merci d'avance ! »"
            ),
            "closing": "Le succès n'est pas une destination, c'est un voyage. Bonne continuation dans la communauté des créateurs de produits digitaux !",
        },
    }
