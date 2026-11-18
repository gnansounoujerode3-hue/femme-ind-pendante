# -*- coding: utf-8 -*-
"""Contenu éditorial structuré de l'ebook et du Workbook Jour 2 rempli.
Rédaction naturelle destinée au lecteur final pour l'ebook, et correspondance
exacte page par page avec le Workbook Jour 2 officiel pour le dossier d'atelier.
"""

BUDGET_GUIDE = [
    {
        "tier": "Petit",
        "label": "Petit budget",
        "range": "Moins de 50 000 FCFA (0 à 80 USD)",
        "desc": (
            "Activités démarrables depuis chez soi avec un smartphone, un savoir-faire "
            "ou un outillage simple. Aucun local commercial requis au départ : idéal pour "
            "tester la demande dès cette semaine."
        ),
    },
    {
        "tier": "Moyen",
        "label": "Budget moyen",
        "range": "50 000 à 300 000 FCFA (80 à 500 USD)",
        "desc": (
            "Demande un premier stock ciblé, un équipement semi-professionnel (moulin, "
            "machine à coudre, kit solaire, congélateur, outillage) ou une petite "
            "enveloppe de mise sur le marché locale."
        ),
    },
    {
        "tier": "Structuré",
        "label": "Budget structuré",
        "range": "300 000 FCFA et plus (500 USD et plus)",
        "desc": (
            "Activités à barrière d'entrée plus élevée (atelier équipé, chambre froide, "
            "véhicule utilitaire, laboratoire ou équipe dédiée) finançables par épargne, "
            "association locale ou partenariat avec la diaspora."
        ),
    },
]

PART_01_INTRO = {
    "num": "01",
    "kicker": "Première partie · Introduction",
    "title": "Pourquoi 2027 est le moment idéal pour lancer un business en Afrique",
    "epigraph": "Comprendre les blocages réels du terrain et s'appuyer sur cinq lames de fond économiques déjà à l'œuvre sur le continent.",
    "lead": (
        "Chaque jour, des milliers de jeunes diplômés, de salariés, de femmes actives et "
        "de membres de la diaspora souhaitent bâtir une source de revenus indépendante. "
        "Pourtant, la majorité reste bloquée avant même de vendre : soit faute d'identifier "
        "une idée adaptée au pouvoir d'achat réel autour d'eux, soit après avoir imité un "
        "commerce déjà saturé sans vérifier la demande."
    ),
    "problem_blocks": [
        (
            "Le vrai frein n'est pas le manque de courage, mais l'absence de filtre",
            "En Afrique francophone, l'énergie entrepreneuriale est immense. Entre des "
            "concepts importés qui supposent une logistique absente et des projets lourds "
            "qui immobilisent des millions de FCFA avant la première vente, beaucoup "
            "s'épuisent avant d'avoir encaissé un seul client."
        ),
        (
            "Cinq vagues économiques qui favorisent les projets agiles",
            "En 2027, démarrer léger avec une offre simple, locale et testée en quelques "
            "jours offre un avantage décisif sur les structures lentes et coûteuses."
        ),
    ],
    "trends_2027": [
        (
            "Paiements mobiles et commerce conversationnel",
            "Du Bénin au Sénégal, de la Côte d'Ivoire au Cameroun, vendre sans boutique "
            "physique grâce à WhatsApp Business, Facebook, TikTok et Mobile Money fait partie des usages quotidiens."
        ),
        (
            "Essor du « Consommons local » transformé",
            "Face au prix des importations, les ménages et la diaspora recherchent des "
            "farines infantiles, jus, épices, soins naturels et textiles locaux présentés proprement."
        ),
        (
            "Outils numériques accessibles sur téléphone",
            "Un prestataire indépendant équipé d'un smartphone produit en deux heures des "
            "visuels, devis, catalogues, supports de formation et contenus qui exigeaient autrefois toute une agence."
        ),
        (
            "Transition énergétique et sobriété",
            "Le coût du réseau pousse commerces, ateliers agricoles et foyers vers les kits "
            "solaires, le froid autonome, le recyclage utile et l'eau potable de proximité."
        ),
        (
            "Externalisation pour PME locales et diaspora",
            "Les petites entreprises préfèrent déléguer comptabilité, prospection, livraison "
            "et accueil client ; la diaspora rémunère volontiers des relais fiables restés au pays."
        ),
    ],
    "profiles": [
        ("Étudiant ou jeune diplômé", "Petit budget (moins de 50 000 FCFA)", "Secteurs 04 (Digital), 05 (Formation), 03 (Social commerce), 12 (Contenu)"),
        ("Salarié cherchant un revenu d'appoint", "Petit à moyen budget", "Secteurs 02 (Livraison week-end), 08 (Immobilier), 16 (Services B2B), 17 (Fintech)"),
        ("Femme active ou mère entrepreneure", "Petit à moyen budget", "Secteurs 01 (Agro-transformation), 06 (Beauté), 07 (Mode), 18 (Enfance)"),
        ("Artisan ou technicien qualifié", "Budget moyen", "Secteurs 10 (Solaire), 15 (Artisanat), 20 (BTP et réparation)"),
        ("Investisseur ou diaspora en partenariat", "Budget structuré", "Secteurs 09 (Logistique), 13 (Tourisme), 14 (Élevage et pisciculture), 01 (Unités)"),
    ],
}

PART_02_ERRORS = {
    "num": "02",
    "kicker": "Deuxième partie · Erreurs à éviter",
    "title": "Les sept erreurs qui coûtent le plus cher aux nouveaux projets",
    "epigraph": "Avant d'engager ton énergie ou ton épargne, évite ces pièges observés sur le terrain et adopte d'emblée l'alternative économe.",
    "intro": (
        "La plupart des échecs précoces ne viennent pas d'un manque d'ardeur au travail, "
        "mais de décisions prises dans les deux premières semaines. Voici les sept écueils "
        "les plus fréquents et le réflexe pragmatique qui les neutralise."
    ),
    "errors": [
        (
            "Lancer sur un coup de cœur sans vérifier le besoin",
            "Tu produis un bel article ou ouvres un service dont personne ne ressent l'urgence autour de toi.",
            "Applique le test terrain en trois critères (Valeur, Intensité, Nombre) auprès de cinq clients potentiels avant tout achat de stock."
        ),
        (
            "Copier le voisin à l'identique",
            "Lorsque trois étals vendent la même chose au même carrefour, il ne reste qu'à casser les prix, et chacun travaille à perte.",
            "Différencie au moins un axe concret : emballage soigné, livraison à domicile, horaire tardif, abonnement ou clientèle précise."
        ),
        (
            "Immobiliser l'essentiel du capital dans un local",
            "Caution, loyer d'avance, enseigne et mobilier assèchent ta trésorerie bien avant l'arrivée du dixième client.",
            "Démarre depuis chez toi, sur précommande, en point relais partagé ou avec un kiosque léger."
        ),
        (
            "Confondre la caisse du business et les dépenses personnelles",
            "Tu as le sentiment de bien vendre, puis impossible de renouveler le stock parce que l'argent a servi aux imprévus familiaux.",
            "Sépare dès le premier jour deux comptes Mobile Money distincts et verse-toi une part fixe définie à l'avance."
        ),
        (
            "Accorder du crédit aux proches sans cadre écrit",
            "Ton fonds de roulement reste bloqué chez des connaissances difficiles à relancer, et tu abîmes à la fois ta trésorerie et le lien.",
            "Travaille au comptant ou demande un acompte de 50 % à la commande, avec confirmation claire avant la livraison."
        ),
        (
            "Fixer ses tarifs sans compter les frais invisibles",
            "Transport, pertes, emballages, données mobiles, frais de retrait et temps passé grignotent la marge sans que tu t'en aperçoives.",
            "Additionne tous les coûts directs, ajoute 15 % pour les aléas puis ta marge nette avant d'annoncer un prix."
        ),
        (
            "Attendre une version parfaite avant d'exister",
            "Pendant des mois passés à peaufiner un logo ou des statuts, un concurrent plus simple et plus rapide prend les premiers clients.",
            "Mets sur le marché une première offre sobre dès cette semaine, encaisse tes dix premières ventes, puis améliore en version 2."
        ),
    ],
}

PART_04_VALIDATION = {
    "num": "04",
    "kicker": "Quatrième partie · Validation en 48 heures",
    "title": "Valider ton Top 3 en 48 heures avant de dépenser le moindre franc",
    "epigraph": "Une méthode simple pour confronter tes trois meilleures pistes à de vrais acheteurs avant d'acheter du matériel ou du stock.",
    "intro": (
        "Une fois trois à cinq pistes repérées dans le répertoire, résiste à l'envie de "
        "produire tout de suite. Consacre quarante-huit heures et zéro franc de fabrication "
        "à mesurer la demande réelle grâce aux trois filtres VIN et à cinq conversations."
    ),
    "vin_reminders": [
        ("Valeur · Le problème précis", "En une phrase : quelle contrainte ou envie précise le client accepte-t-il de payer pour résoudre dès cette semaine ?"),
        ("Intensité · L'urgence ressentie (/10)", "Le besoin est-il pressant ou accessoire ? Vise au moins 7 sur 10 : si l'acheteur peut attendre six mois, il différera sa dépense."),
        ("Nombre · Le volume solvable", "Combien de personnes prêtes à payer rencontrent ce problème chaque semaine dans ton quartier, ta ville ou ton réseau ?"),
    ],
    "steps_48h": [
        ("Heures 0 à 4 · Retenir trois finalistes", "Sélectionne une piste à petit budget démarrable aussitôt, une piste appuyée sur ton réseau actuel et ton choix prioritaire."),
        ("Heures 4 à 18 · Noter sur 30 points", "Évalue chaque piste de 1 à 5 sur les six critères ci-dessous. Écarte sans hésiter tout projet en dessous de 20 sur 30."),
        ("Heures 18 à 36 · Mener cinq vrais échanges", "Appelle ou rencontre cinq clients potentiels. Évite « Aimerais-tu ce produit ? », demande plutôt : « Combien as-tu dépensé pour cela le mois dernier, et commandes-tu si je te livre vendredi à tel prix ? »."),
        ("Heures 36 à 48 · Obtenir un engagement daté", "Une idée est validée lorsque deux personnes sur cinq au moins réservent, précommandent ou versent un premier acompte."),
    ],
    "scoring_criteria": [
        ("1. Besoin urgent et vérifié", "Des clients cherchent déjà une réponse et dépensent de l'argent pour l'obtenir."),
        ("2. Capital disponible tout de suite", "Tu réunis le budget nécessaire sans recourir à un endettement risqué."),
        ("3. Savoir-faire accessible en moins de 7 jours", "Tu maîtrises déjà le geste, ou tu peux te former ou t'associer rapidement."),
        ("4. Cycle de vente court (moins de 7 jours)", "Tu produis, livres et encaisses au cours de la même semaine."),
        ("5. Marge nette saine (30 % et plus)", "Une fois transport, emballage et frais déduits, un bénéfice clair subsiste."),
        ("6. Répétition d'achat ou recommandation", "Un même client revient régulièrement ou t'adresse des contacts proches."),
    ],
    "example_box_title": "Cas d'application · Idée #002 : Chips de banane plantain aromatisées",
    "example_box_lines": [
        "Filtre VIN : besoin d'un en-cas croquant et propre au bureau ou à l'école (Valeur), envie quotidienne immédiate notée 8/10 (Intensité) auprès de milliers de salariés, étudiants et supérettes (Nombre).",
        "Note sur 30 : besoin (5/5), petit budget inférieur à 50 000 FCFA (5/5), prise en main rapide (5/5), vente en 24 heures (5/5), marge supérieure à 40 % (4/5), réachat hebdomadaire (5/5), soit 29/30.",
        "Test en 48 heures : deux lots préparés en cuisine puis proposés à dix collègues et deux épiceries de quartier. Huit sachets réglés comptant et une commande hebdomadaire confirmée avant même d'investir dans du matériel.",
    ],
}

PART_05_LAUNCH = {
    "num": "05",
    "kicker": "Cinquième partie · Plan d'action en 7 jours",
    "title": "Lancer ton activité en sept jours et encaisser tes premières ventes",
    "epigraph": "Une progression jour par jour pour passer de l'idée validée au premier encaissement sans site complexe ni local coûteux.",
    "intro": (
        "Une fois l'idée la mieux notée validée, l'objectif n'est plus de planifier mais "
        "d'obtenir tes premières ventes réelles en une semaine. Suis ces sept étapes "
        "dans l'ordre."
    ),
    "days": [
        ("Jour 1", "Clarifier une offre simple et son prix", "Définis une formule découverte claire et un format standard, vérifie tes coûts complets et rédige ta promesse en une phrase."),
        ("Jour 2", "Préparer le minimum présentable", "Réalise trois photos nettes à la lumière du jour (ou une fiche PDF lisible), puis règle ton profil WhatsApp Business et ton compte Mobile Money."),
        ("Jour 3", "Lister trente acheteurs probables", "Note dix connaissances directes, dix contacts professionnels ou de quartier et dix groupes locaux où se trouve déjà ta clientèle."),
        ("Jour 4", "Envoyer les trente premiers messages", "Adresse le premier message ci-contre à vingt contacts ciblés et publie un statut WhatsApp accompagné d'une offre limitée aux cinq premiers clients."),
        ("Jour 5", "Encaisser et livrer avec soin", "Demande un acompte ou un règlement à la commande, livre à l'heure convenue avec une présentation propre et un mot personnalisé."),
        ("Jour 6", "Recueillir les premiers retours", "Demande un court avis écrit ou vocal à tes premiers acheteurs et propose un avantage simple à ceux qui te recommandent un proche."),
        ("Jour 7", "Faire les comptes et préparer la semaine suivante", "Répartis tes recettes selon la règle des trois enveloppes, relève le canal le plus efficace et concentre tes efforts dessus."),
    ],
    "scripts": [
        (
            "Message WhatsApp pour le premier cercle",
            "« Bonjour [Prénom], j'espère que tu vas bien. Je lance cette semaine [nom de ton service ou produit] pour aider [cible] à [résultat concret] en [délai], sans [principal frein]. Pour mes cinq premiers clients d'ici samedi, je propose l'offre à [Prix] au lieu de [Prix habituel]. Est-ce utile pour toi ou pour quelqu'un autour de toi en ce moment ? »"
        ),
        (
            "Publication Facebook ou statut WhatsApp",
            "« Vous cherchez [résultat concret] à [Ville/Quartier] sans [difficulté courante] ? Nous ouvrons cette semaine [Nom de l'offre] avec [deux avantages précis et délai de livraison]. Offre d'ouverture valable jusqu'à dimanche pour les dix premières demandes. Écrivez INFOS en commentaire ou envoyez un message WhatsApp au [Numéro]. »"
        ),
        (
            "Réponse sereine à l'objection sur le prix",
            "« Je comprends tout à fait. Ce tarif inclut justement [élément de qualité, garantie ou livraison comprise] pour éviter toute mauvaise surprise. Si tu préfères démarrer plus léger cette semaine, nous avons aussi la formule Essentiel à [Prix d'entrée] pour que tu testes par toi-même. Souhaites-tu essayer celle-ci ? »"
        ),
    ],
    "pricing_formula": [
        "1. Additionne tous les coûts directs : matière première, emballage, livraison, énergie et frais Mobile Money.",
        "2. Ajoute une juste rétribution pour ton temps de travail ainsi qu'une marge de 10 à 15 % pour les pertes ou imprévus.",
        "3. Applique ta marge nette cible (au moins 30 % sur un produit physique, 50 % ou plus sur une prestation de service) afin de fixer ton prix plancher.",
    ],
    "envelopes": [
        ("Enveloppe 1 · 50 % Réinvestissement", "Reste sur le compte professionnel pour reconstituer le stock, soigner le conditionnement et faire croître l'outil de travail."),
        ("Enveloppe 2 · 30 % Charges et réserve", "Couvre transport, crédit internet, communication, démarches légales et coussin de sécurité pour les semaines plus calmes."),
        ("Enveloppe 3 · 20 % Rémunération personnelle", "Constitue ta paie officielle. Seule cette enveloppe règle tes dépenses privées, jamais le chiffre d'affaires brut."),
    ],
}

CONCLUSION_CONTENT = {
    "kicker": "Conclusion · Passage à l'action",
    "title": "Oublie la perfection, agis dans les quarante-huit heures",
    "epigraph": "Un livre de business ne change rien tant qu'il reste fermé : tout se joue dans les deux prochaines journées.",
    "message": (
        "Tu disposes désormais de cinq cents pistes adaptées aux marchés africains de 2027, "
        "d'une grille claire pour éviter les erreurs coûteuses, d'une méthode de validation en "
        "quarante-huit heures et d'une feuille de route sur sept jours. Ce qui sépare un projet "
        "qui reste dans un carnet d'une activité qui encaisse tient à la rapidité de ton premier pas."
    ),
    "mantra": "« Ton premier jour de vente ne sera pas parfait, et c'est normal. Lance une version simple, encaisse ton premier client réel, puis améliore en version 2.0. »",
    "action_sheet": [
        "Secteur retenu (01 à 20) :",
        "Idée sélectionnée (numéro et intitulé) :",
        "Budget réaliste disponible au départ (FCFA) :",
        "Promesse en une phrase (Pour qui, quel résultat, en quel délai) :",
        "Cinq premiers prospects à contacter demain matin :",
        "Date visée pour le premier encaissement :",
    ],
    "next_steps_reader": [
        "1. Dans les deux prochaines heures, arrête ton choix sur une seule idée parmi tes finalistes, en privilégiant celle qui demande le moindre capital initial.",
        "2. Dans les quarante-huit heures, mène cinq entretiens de terrain et propose une première offre test à dix personnes de ton entourage.",
        "3. Au bout de sept jours, rassemble les remarques de tes premiers clients et ajuste ton offre pour passer en version améliorée.",
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
    pages_txt = f"{ebook_pages} pages" if ebook_pages else "environ 50 pages"
    return {
        "author": author,
        "date": date_str,
        "title": title,
        "promise": promise,
        "page1": {
            "badge": "Workbook Officiel · Jour 2",
            "title": "Crée ton premier produit digital",
            "subtitle": f"Dossier d'application complété pour l'ouvrage « {title} »",
            "welcome": (
                "Bienvenue dans ton guide pratique pour transformer ton idée en un véritable produit "
                "digital. Ce workbook est conçu spécialement pour toi, entrepreneur africain francophone, "
                "qui souhaites passer à l'action dès aujourd'hui. Pas besoin d'être expert en technologie "
                "ou d'avoir des années d'expérience. Ce qui compte, c'est ta volonté d'avancer et de créer "
                "quelque chose de concret qui aide les autres. Dans les pages suivantes, la méthode exacte "
                "du Workbook Jour 2 (valider, structurer, créer étape par étape) est appliquée de bout "
                "en bout à ton ebook sur les 500 idées de business en Afrique en 2027."
            ),
            "summary_rows": [
                ("Produit créé", title),
                ("Cible prioritaire", "Entrepreneurs et porteurs de projets en Afrique francophone et diaspora"),
                ("Format retenu", "Livre PDF prêt à diffuser et sources éditables"),
                ("Auteur ou marque", author),
                ("Date de réalisation", date_str),
            ],
        },
        "page2": {
            "kicker": "Objectif · Page 2",
            "title": "À la fin de ce workbook, tu as un produit",
            "intro": (
                "Oublie la perfection. Ton premier produit ne sera pas parfait, et c'est normal. "
                "Ce qui importe aujourd'hui, c'est de passer à l'action et de créer quelque chose "
                "de réel que tu pourras améliorer avec le temps. Chaque page contient des exercices "
                "concrets appliqués ici directement à ton ebook."
            ),
            "quote": "À la fin, tu pourras écrire : « J'ai créé mon premier produit digital. »",
            "commitment": [
                ("Nom / Marque", author),
                ("Date", date_str),
                ("Statut de l'engagement", f"Validé pour « {title} »"),
            ],
        },
        "page3": {
            "kicker": "Validation · Page 3",
            "title": "Validation express de ton idée (Méthode VIN)",
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
            "conclusion": "Verdict : Valeur (problème réel) + Intensité (9/10) + Nombre (marché massif) sont élevés, l'idée est validée.",
        },
        "page4": {
            "kicker": "Promesse · Page 4",
            "title": "Transformation de ton idée en promesse claire",
            "intro": (
                "Ton produit doit offrir une transformation concrète à tes lecteurs. Plus ta promesse "
                "est précise (pour qui, quel résultat, en combien de temps), plus elle est convaincante."
            ),
            "q1": "Les futurs entrepreneurs africains francophones (étudiants, salariés, femmes actives, commerçants et diaspora) cherchant un business rentable et réaliste pour 2027.",
            "q2": "Choisir une activité adaptée à son budget réel (Petit, Moyen ou Structuré), la valider en 48 heures sur le terrain et lancer les premières ventes concrètes.",
            "q3": "En 7 jours (48 heures de filtrage et validation terrain, puis 5 jours de lancement commercial).",
            "formula_template": "« Comment _________________ en _________________ sans _________________. »",
            "formula_filled": f"« {promise} »",
        },
        "page5": {
            "kicker": "Format · Page 5",
            "title": "Choisis ton format (simple et rapide)",
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
                "de 10 pages (Couverture, Introduction, Erreurs et début du Secteur 01) conforme au format court."
            ),
            "provisional_title": title,
        },
        "page6": {
            "kicker": "Structure · Page 6",
            "title": "Structure ton produit en 5 parties + Conclusion",
            "parts": [
                ("01", "Introduction", "Le problème du manque de filtre entrepreneurial en Afrique et pourquoi les cinq dynamiques de 2027 créent une opportunité claire (+ guide des budgets)."),
                ("02", "Erreurs à éviter", "Les 7 erreurs fatales qui fragilisent les débutants (copier sans se différencier, tout mettre dans le local, mélanger les caisses, vendre à crédit, attendre la perfection)."),
                ("03", "Étape 1", "Sélectionner son idée : répertoire complet des 500 idées classées en 20 secteurs porteurs Afrique 2027 (25 idées/secteur avec budget Petit, Moyen ou Structuré)."),
                ("04", "Étape 2", "Valider son Top 3 en 48 heures avant d'investir 1\u00A0FCFA grâce à la grille de notation /30, la méthode VIN et le test des 5 vraies conversations."),
                ("05", "Étape 3", "Lancer son business en 7 jours : feuille de route jour par jour (J1 à J7), 3 scripts WhatsApp/Facebook, calcul du prix juste et règle des 3 enveloppes."),
                ("End", "Conclusion", "Engagement écrit du lecteur sur 48h, passage à l'action imparfait mais immédiat, puis page auteur personnalisable et prise de contact."),
            ],
        },
        "page7": {
            "kicker": "Rédaction & Checklist · Page 7",
            "title": "Utilise l'IA pour générer ton contenu rapidement",
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
                "1. Prompt copié et adapté avec le sujet précis et le lectorat Afrique 2027",
                "2. Structuration en 20 secteurs × 25 fiches uniques (500 idées sans doublon)",
                "3. Adaptation locale : montants en FCFA et USD, Mobile Money, réalités terrain 2027",
                "4. Relecture linguistique complète et suppression de toute formulation artificielle",
                "5. Mise en page de livre soignée avec couverture illustrée, sommaire et folios",
                "6. Export en PDF final vérifié et conservation des sources éditables pour personnalisation",
            ],
            "checklist": [
                ("J'ai généré la base de contenu avec l'IA", True),
                ("J'ai relu et corrigé (500 idées uniques vérifiées, français naturel)", True),
                ("J'ai simplifié le langage (phrases directes, sans jargon inutile)", True),
                ("J'ai personnalisé avec des exemples locaux (réalités Afrique francophone 2027)", True),
                ("J'ai mis en page dans un vrai gabarit éditorial de livre (couverture + sommaire)", True),
                ("J'ai enregistré en format PDF (500-Idees-de-Business-a-Lancer-en-Afrique-en-2027.pdf)", True),
                ("J'ai vérifié l'ouverture et le rendu visuel de chaque page", True),
            ],
            "important_note": (
                "Personnalisation avant diffusion : remplace le nom provisoire, la courte biographie "
                "et tes coordonnées de contact par les tiens afin de signer pleinement ton ouvrage."
            ),
        },
        "page8": {
            "kicker": "Récapitulatif · Page 8",
            "title": "Félicitations ! Tu es presque au bout",
            "intro": (
                "Beaucoup parlent de créer un produit digital, mais peu passent réellement à l'action. "
                "Voici le bilan exact des 5 étapes du Workbook Jour 2 validées pour ton ebook :"
            ),
            "recap_cards": [
                ("1. Tu as validé ton idée", "Méthode VIN appliquée (Valeur claire, Intensité 9/10, Nombre massif)", "Accompli"),
                ("2. Tu as défini ta promesse", "Formule claire en 7 jours sans gros capital ni peur de se tromper", "Accompli"),
                ("3. Tu as choisi ton format", "PDF haute lisibilité mobile et fichiers sources éditables", "Accompli"),
                ("4. Tu as structuré ton contenu", "5 parties exactes (Intro, Erreurs, 500 Idées, Validation, Lancement) et Conclusion", "Accompli"),
                ("5. Tu as créé et mis en page", "Ebook complet produit, relu, composé en gabarit d'édition et prêt à diffuser", "Accompli"),
            ],
        },
        "page9": {
            "kicker": "Déclaration officielle · Page 9",
            "title": "Je confirme avoir créé mon premier produit digital",
            "declaration": [
                ("Nom / Marque", author),
                ("Signature", "À parapher après personnalisation"),
                ("Date", date_str),
                ("Titre de mon produit", title),
            ],
            "fb_action": "Action immédiate : publie dans le groupe Facebook avec une capture de la couverture de ton ebook.",
            "social_posts": [
                (
                    "Modèle 1 · Victoire communautaire (Workbook Jour 2)",
                    "« J'ai créé mon premier produit digital ! [Photo de couverture] Après avoir appliqué étape par étape la méthode VIN, défini ma promesse et structuré les 5 parties, voici enfin mon ebook : \"500 Idées de Business à Lancer en Afrique en 2027\". Pas besoin d'attendre la perfection pour passer à l'action. Merci à la communauté pour l'élan ! »"
                ),
                (
                    "Modèle 2 · Publication valeur & autorité",
                    "« Tu veux entreprendre en 2027 mais tu te demandes par quel business commencer avec ton budget actuel ? J'ai réuni 500 idées concrètes réparties en 20 secteurs africains (du petit budget < 50 000 FCFA aux projets structurés) + une méthode en 48h pour tester avant d'investir. Commente \"2027\" si tu veux découvrir le sommaire ! »"
                ),
                (
                    "Modèle 3 · Lancement et précommande",
                    "« OFFRE DE LANCEMENT : Mon nouveau guide \"500 Idées de Business à Lancer en Afrique en 2027\" est disponible en PDF instantané sur téléphone. En bonus : les 7 erreurs à éviter et le plan exact des 7 premiers jours avec scripts WhatsApp. Écris-moi en privé ou sur WhatsApp pour recevoir ton exemplaire dès aujourd'hui. »"
                ),
            ],
        },
        "page10": {
            "kicker": "Prochains pas · Page 10",
            "title": "Et maintenant ? Tes prochains pas",
            "steps": [
                (
                    "1. Lance ton produit auprès de dix proches",
                    "Partage dès aujourd'hui le PDF (ou les dix premières pages en extrait gratuit) à dix personnes ciblées pour récolter leurs vrais retours en quarante-huit heures."
                ),
                (
                    "2. Améliore-le en version 2.0",
                    "Note quelles idées suscitent le plus de questions. Pour la version suivante, ajoute des fiches chiffrées détaillées sur les vingt idées favorites de tes premiers lecteurs."
                ),
                (
                    "3. Crée le suivant avec la même méthode",
                    "Suites naturelles faciles à décliner ensuite : « 50 Business à lancer avec moins de 25 000 FCFA », « Modèles de budget sur WhatsApp et tableur » ou « Scripts de vente Afrique 2027 »."
                ),
            ],
            "whatsapp_testers": (
                "Message WhatsApp prêt à envoyer à tes 10 premiers testeurs :\n"
                "« Salut [Prénom] ! Je viens de finaliser mon tout premier ebook pratique : \"500 Idées de Business à Lancer en Afrique en 2027\" (20 secteurs + méthode pour valider en 48h et lancer en 7 jours). Comme ton avis compte beaucoup pour moi, je t'envoie le PDF en avant-première. Tu peux me dire d'ici 48h : 1) quelle idée t'a le plus marqué, et 2) ce que tu aimerais voir approfondi dans la version 2.0 ? Un grand merci d'avance ! »"
            ),
            "closing": "Le succès n'est pas une destination, c'est un voyage. Bonne continuation dans la communauté des créateurs de produits digitaux !",
        },
    }
