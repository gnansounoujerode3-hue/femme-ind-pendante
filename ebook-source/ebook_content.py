# -*- coding: utf-8 -*-
"""Contenu éditorial structuré de l'ebook et du Workbook Jour 2 rempli.
Angle éditorial : lancer un business rentable en Afrique pour bien finir l'année,
sans attendre janvier ni immobiliser un gros capital.
"""

BUDGET_GUIDE = [
    {
        "tier": "Petit",
        "label": "Petit budget",
        "range": "Moins de 50 000 FCFA (0 à 80 USD)",
        "desc": (
            "Activités démarrables depuis chez soi avec un smartphone, un savoir-faire "
            "ou un outillage simple. Aucun local commercial requis au départ : idéal pour "
            "capter la demande de fin d'année dès cette semaine."
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
    "title": "Pourquoi la fin d'année est le meilleur moment pour lancer un business en Afrique",
    "epigraph": "Ne pas attendre janvier pour se lancer : profiter des dernières semaines de l'année où l'argent, les commandes et la diaspora circulent le plus vite.",
    "lead": (
        "Chaque mois de novembre, beaucoup se répètent la même phrase : « L'année est "
        "presque terminée, je commencerai en janvier. » C'est une erreur coûteuse. En "
        "Afrique francophone, les six à huit dernières semaines de l'année concentrent la "
        "plus forte circulation d'argent des douze mois : achats familiaux, cérémonies, "
        "primes, colis diaspora et clôture de budgets d'entreprises."
    ),
    "problem_blocks": [
        (
            "Le vrai frein n'est pas le manque de temps, mais l'absence de filtre",
            "Repousser à janvier fait rater le pic commercial le plus généreux de l'année. "
            "À l'inverse, ceux qui s'appuient sur des concepts trop lourds immobilisent leurs "
            "économies avant d'avoir encaissé un seul client. L'enjeu est de choisir une "
            "offre simple, vendable immédiatement."
        ),
        (
            "Cinq dynamiques de fin d'année favorables aux projets légers",
            "Démarrer léger en novembre ou décembre permet de tester une idée sur une vraie "
            "demande urgente, d'encaisser avant le 31 décembre et d'aborder la nouvelle année "
            "avec une clientèle déjà fidélisée."
        ),
    ],
    "trends_fin_annee": [
        (
            "Pic d'achats festifs et commerce sur WhatsApp",
            "Des repas de groupe aux tenues et coffrets cadeaux, les ménages commandent par "
            "WhatsApp Business, TikTok et Facebook avec règlement rapide par Mobile Money."
        ),
        (
            "Demande record autour du « Consommons local » et des colis diaspora",
            "Réceptions de fin d'année, visites familiales et retours de la diaspora dopent les "
            "ventes de jus naturels, épices, pâtisseries, soins locaux, textiles et artisanat."
        ),
        (
            "Commerçants débordés en quête de renfort digital express",
            "Les boutiques ont besoin dès cette semaine de visuels promo, catalogues WhatsApp, "
            "vidéos courtes et suivi de messages pour ne rater aucune commande des fêtes."
        ),
        (
            "Besoins urgents en fraîcheur, énergie, transport et nettoyage",
            "Réunions de famille, galas et congés multiplient la demande en glaçons, froid "
            "autonome, livraisons ponctuelles, lavage auto, ménage et location de matériel."
        ),
        (
            "Clôtures d'exercice des PME et résolutions déjà en préparation",
            "Entreprises et particuliers délèguent leurs inventaires, paniers d'entreprise, "
            "comptes de fin d'année et carnets d'objectifs pour repartir du bon pied."
        ),
    ],
    "profiles": [
        ("Étudiant ou jeune diplômé", "Petit budget (moins de 50 000 FCFA)", "Secteurs 04 (Digital), 05 (Formation), 03 (Social commerce), 12 (Contenu)"),
        ("Salarié cherchant un revenu d'appoint avant les fêtes", "Petit à moyen budget", "Secteurs 02 (Livraison week-end), 08 (Immobilier), 16 (Services B2B), 17 (Fintech)"),
        ("Femme active ou mère entrepreneure", "Petit à moyen budget", "Secteurs 01 (Agro-transformation), 06 (Beauté), 07 (Mode), 18 (Enfance)"),
        ("Artisan ou technicien qualifié", "Budget moyen", "Secteurs 10 (Solaire), 15 (Artisanat), 20 (BTP et réparation)"),
        ("Investisseur ou diaspora en séjour de fin d'année", "Budget structuré", "Secteurs 09 (Logistique), 13 (Tourisme), 14 (Élevage et pisciculture), 01 (Unités)"),
    ],
}

PART_02_ERRORS = {
    "num": "02",
    "kicker": "Deuxième partie · Erreurs à éviter",
    "title": "Les sept erreurs qui font perdre de l'argent en fin d'année",
    "epigraph": "Avant d'engager ton épargne ou tes primes de fin d'année, évite ces pièges fréquents et adopte d'emblée l'alternative économe.",
    "intro": (
        "En fin d'année, l'envie d'aller vite pousse parfois à dépenser son capital dans "
        "le mauvais ordre. Voici les sept erreurs les plus coûteuses observées sur le terrain "
        "et le réflexe sobre qui protège ta trésorerie."
    ),
    "errors": [
        (
            "Lancer sur un coup de cœur sans vérifier le besoin",
            "Tu achètes un beau stock de fin d'année dont personne ne ressent l'urgence autour de toi.",
            "Applique le test terrain en trois critères (Valeur, Intensité, Nombre) auprès de cinq clients potentiels avant tout achat de stock."
        ),
        (
            "Copier le voisin à l'identique",
            "Lorsque trois vendeurs proposent exactement les mêmes coffrets ou plats au même endroit, il ne reste qu'à brader les marges.",
            "Différencie au moins un axe concret : emballage cadeau soigné, livraison le soir, paiement en deux tranches ou clientèle précise."
        ),
        (
            "Immobiliser l'essentiel du capital dans un local",
            "Caution, loyer d'avance, enseigne et mobilier avalent ton épargne avant même d'avoir profité de la saison des achats.",
            "Démarre depuis chez toi, sur précommande, en point relais partagé ou en boutique éphémère sur les week-ends forts."
        ),
        (
            "Confondre les ventes de décembre avec de l'argent de poche",
            "L'euphorie des fêtes pousse à puiser dans la caisse pour les cadeaux et sorties familiales ; en janvier, plus de fonds de roulement.",
            "Sépare dès le premier jour deux comptes Mobile Money distincts et applique la règle des trois enveloppes sur chaque encaissement."
        ),
        (
            "Accorder du crédit aux proches pendant les fêtes",
            "Les achats « je te paie en janvier » bloquent ta trésorerie au pire moment et fragilisent les relations dès la rentrée.",
            "Travaille au comptant ou exige un acompte de 50 % à la commande, solde réglé à la remise."
        ),
        (
            "Fixer ses tarifs sans compter les frais invisibles",
            "Transport de dernière minute, emballages, pertes, données mobiles et frais de retrait grignotent toute ta marge.",
            "Additionne tous les coûts directs, ajoute 15 % pour les aléas puis ta marge nette avant d'afficher un tarif."
        ),
        (
            "Attendre le 1er janvier ou une version parfaite avant d'exister",
            "Reporter le lancement à l'an prochain par peur d'un logo imparfait te fait manquer les semaines les plus acheteuses de l'année.",
            "Mets sur le marché une première offre sobre dès cette semaine, encaisse tes premières ventes avant le 31 décembre, puis améliore en version 2."
        ),
    ],
}

PART_04_VALIDATION = {
    "num": "04",
    "kicker": "Quatrième partie · Validation en 48 heures",
    "title": "Valider ton Top 3 en 48 heures avant de dépenser le moindre franc",
    "epigraph": "Une méthode express pour confronter tes trois meilleures pistes à de vrais acheteurs dès cette semaine, sans acheter de stock à l'aveugle.",
    "intro": (
        "Une fois trois à cinq pistes repérées dans le répertoire, résiste à l'envie de "
        "produire tout de suite. Consacre quarante-huit heures et zéro franc d'investissement "
        "à vérifier l'appétit réel de ton entourage grâce aux trois filtres VIN."
    ),
    "vin_reminders": [
        ("Valeur · Le problème précis", "En une phrase : quelle envie ou contrainte immédiate le client accepte-t-il de payer pour résoudre dès cette semaine ?"),
        ("Intensité · L'urgence ressentie (/10)", "Le besoin est-il pressant avant la fin de l'année ? Vise au moins 7 sur 10 : si le prospect peut attendre trois mois, il n'achètera pas aujourd'hui."),
        ("Nombre · Le volume solvable", "Combien de personnes prêtes à payer rencontrent ce besoin chaque semaine dans ton quartier, ton bureau, ton église ou ton groupe WhatsApp ?"),
    ],
    "steps_48h": [
        ("Heures 0 à 4 · Retenir trois finalistes", "Sélectionne une piste à petit budget vendable cette semaine, une piste portée par le pic de fin d'année et ton choix de cœur."),
        ("Heures 4 à 18 · Noter sur 30 points", "Évalue chaque piste de 1 à 5 sur les six critères ci-dessous. Écarte sans hésiter tout projet en dessous de 20 sur 30."),
        ("Heures 18 à 36 · Mener cinq vrais échanges", "Appelle ou rencontre cinq acheteurs probables. Évite « Aimerais-tu ce produit ? », demande plutôt : « Si je te livre ce format vendredi à tel prix, est-ce que je te note une commande ? »."),
        ("Heures 36 à 48 · Obtenir un engagement daté", "Une idée est validée lorsque deux personnes sur cinq au moins réservent, précommandent ou versent un premier acompte."),
    ],
    "scoring_criteria": [
        ("1. Besoin urgent et vérifié", "Des clients achètent déjà une solution proche en cette fin d'année."),
        ("2. Capital disponible tout de suite", "Tu réunis le budget nécessaire sans recourir à un endettement risqué."),
        ("3. Savoir-faire accessible en moins de 7 jours", "Tu maîtrises déjà le geste, ou tu peux te former ou t'associer immédiatement."),
        ("4. Cycle de vente court (moins de 7 jours)", "Tu produis, livres et encaisses au cours de la même semaine."),
        ("5. Marge nette saine (30 % et plus)", "Une fois transport, emballage et frais déduits, un bénéfice clair subsiste."),
        ("6. Répétition d'achat après les fêtes", "Le produit reste utile ou recommandable au-delà du 31 décembre."),
    ],
    "example_box_title": "Cas d'application · Idée #002 : Chips de banane plantain aromatisées",
    "example_box_lines": [
        "Filtre VIN : besoin d'un en-cas croquant et présentable pour bureaux, réceptions et paniers de fin d'année (Valeur), demande immédiate notée 8/10 (Intensité) auprès des collègues, familles et supérettes (Nombre).",
        "Note sur 30 : besoin (5/5), petit budget inférieur à 50 000 FCFA (5/5), fabrication maîtrisée en 24h (5/5), encaissement immédiat (5/5), marge supérieure à 40 % (4/5), réachat régulier en semaine comme en janvier (5/5), soit 29/30.",
        "Test en 48 heures : deux lots préparés en cuisine puis proposés à dix collègues et deux épiceries de quartier. Huit sachets réglés comptant et deux précommandes de coffrets apéro confirmées avant même d'acheter une friteuse pro.",
    ],
}

PART_05_LAUNCH = {
    "num": "05",
    "kicker": "Cinquième partie · Plan d'action en 7 jours",
    "title": "Lancer ton activité en sept jours et encaisser avant la fin de l'année",
    "epigraph": "Une feuille de route jour par jour pour passer de l'idée choisie aux premiers encaissements sans site complexe ni local coûteux.",
    "intro": (
        "Une fois l'idée la mieux notée validée, l'objectif n'est plus d'attendre une nouvelle "
        "année mais de réaliser tes premières ventes concrètes en une semaine. Suis ces sept "
        "étapes dans l'ordre."
    ),
    "days": [
        ("Jour 1", "Clarifier une offre simple et son prix", "Définis une formule découverte ou un pack de fin d'année lisible, vérifie tes coûts complets et rédige ta promesse en une phrase."),
        ("Jour 2", "Préparer le minimum présentable", "Réalise trois photos nettes à la lumière du jour (ou une fiche PDF propre), puis règle ton profil WhatsApp Business et ton compte Mobile Money."),
        ("Jour 3", "Lister trente acheteurs probables", "Note dix connaissances directes, dix contacts professionnels ou de quartier et dix groupes locaux où l'on prépare déjà les achats de fin d'année."),
        ("Jour 4", "Envoyer les trente premiers messages", "Adresse le premier message ci-contre à vingt contacts ciblés et publie un statut WhatsApp avec une offre valable pour les cinq premiers clients."),
        ("Jour 5", "Encaisser et livrer avec soin", "Demande un acompte ou un règlement à la commande, livre à l'heure convenue avec une présentation propre et un mot soigné."),
        ("Jour 6", "Recueillir les premiers retours", "Demande un court avis écrit ou vocal à tes premiers acheteurs et propose un avantage simple à ceux qui te recommandent auprès de leurs proches."),
        ("Jour 7", "Sécuriser le cash pour traverser les fêtes", "Répartis tes recettes selon la règle des trois enveloppes afin que les dépenses de décembre ne mangent jamais ton capital de janvier."),
    ],
    "scripts": [
        (
            "Message WhatsApp pour le premier cercle",
            "« Bonjour [Prénom], j'espère que tu termines bien l'année. Je lance cette semaine [nom de ton service ou produit] pour aider [cible] à [résultat concret] en [délai], sans [principal frein]. Pour mes cinq premières commandes avant [Jour/Date], je propose l'offre à [Prix] au lieu de [Prix habituel]. Est-ce utile pour toi ou quelqu'un autour de toi ? »"
        ),
        (
            "Publication Facebook ou statut WhatsApp",
            "« Besoin de [résultat concret] à [Ville/Quartier] avant la fin de l'année sans [difficulté courante] ? Nous ouvrons cette semaine [Nom de l'offre] avec [deux avantages précis et délai de livraison]. Offre de lancement limitée aux dix premières commandes de la semaine. Écrivez INFOS en commentaire ou envoyez un message WhatsApp au [Numéro]. »"
        ),
        (
            "Réponse sereine à l'objection sur le prix",
            "« Je comprends tout à fait. Ce tarif inclut justement [élément de qualité, garantie ou livraison comprise] pour t'éviter tout souci de dernière minute. Si tu préfères tester plus léger cette semaine, nous avons aussi la formule Essentiel à [Prix d'entrée]. Souhaites-tu démarrer avec celle-ci ? »"
        ),
    ],
    "pricing_formula": [
        "1. Additionne tous les coûts directs : matière première, emballage soigné, livraison, énergie et frais Mobile Money.",
        "2. Ajoute une juste rétribution pour ton temps de travail ainsi qu'une marge de 10 à 15 % pour les pertes ou imprévus.",
        "3. Applique ta marge nette cible (au moins 30 % sur un produit physique, 50 % ou plus sur une prestation de service) afin de fixer ton prix plancher.",
    ],
    "envelopes": [
        ("Enveloppe 1 · 50 % Capital & Stock", "Reste bloquée sur ton compte business pour renouveler la marchandise et entrer en janvier avec de la trésorerie."),
        ("Enveloppe 2 · 30 % Charges et réserve", "Couvre transport, crédit internet, emballages, communication et coussin de sécurité pour les semaines plus calmes."),
        ("Enveloppe 3 · 20 % Rémunération personnelle", "Constitue ta vraie paie pour tes achats personnels et fêtes : ne touche jamais aux deux premières enveloppes."),
    ],
}

CONCLUSION_CONTENT = {
    "kicker": "Conclusion · Passage à l'action",
    "title": "N'attends pas janvier, agis dans les quarante-huit heures",
    "epigraph": "Un bilan d'année réussi ne se décide pas le 1er janvier, il commence par une première action mesurable dès cette semaine.",
    "message": (
        "Tu disposes désormais de cinq cents pistes concrètes adaptées aux marchés africains, "
        "d'une grille lucide pour préserver ton argent pendant la période la plus animée de "
        "l'année, d'un test en quarante-huit heures et d'un plan d'exécution sur sept jours. "
        "Ceux qui finissent l'année avec un business actif sont simplement ceux qui lancent "
        "avant tout le monde."
    ),
    "mantra": "« Mieux vaut encaisser tes cinq premiers clients imparfaits avant le 31 décembre que rédiger un plan parfait qui dort jusqu'en mars. »",
    "action_sheet": [
        "Secteur retenu (01 à 20) :",
        "Idée sélectionnée (numéro et intitulé) :",
        "Budget réaliste disponible dès aujourd'hui (FCFA) :",
        "Promesse en une phrase (Pour qui, quel résultat, en quel délai) :",
        "Cinq premiers prospects à contacter demain matin :",
        "Premier encaissement visé avant le 31 décembre (montant et date) :",
    ],
    "next_steps_reader": [
        "1. Dans les deux prochaines heures, arrête ton choix sur une seule idée parmi tes finalistes, en privilégiant celle que tu peux vendre dès cette semaine.",
        "2. Dans les quarante-huit heures, mène cinq entretiens de terrain et propose une première offre test à dix personnes de ton entourage.",
        "3. Avant la fin de la semaine, encaisse tes premières commandes et protège ton fonds de roulement grâce aux trois enveloppes.",
    ],
}


def get_workbook_pages_data(config, ebook_pages=None):
    """Retourne les données exactes pour les 10 pages du Workbook Jour 2 rempli."""
    author = config.get("author_name", "[Ton Nom / Ta Marque]")
    date_str = config.get("date_creation", "16 novembre 2026")
    title = config.get(
        "ebook_title",
        "500 Idées de Business à Lancer en Afrique pour Bien Finir l'Année",
    )
    promise = config.get(
        "promise_formula",
        "Comment choisir, valider et lancer ton business rentable en Afrique pour bien finir l'année en 7 jours sans gros capital ni attendre janvier.",
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
                "en bout à ton ebook sur les 500 idées de business pour bien finir l'année en Afrique."
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
                "En fin d'année, des milliers de jeunes, salariés, femmes actives et membres de la "
                "diaspora veulent générer un revenu avant le 31 décembre au lieu d'attendre janvier, "
                "mais manquent d'idées ciblées adaptées à leur budget et d'une méthode pour tester vite."
            ),
            "I_score": "9 / 10",
            "I_exp": (
                "Les dépenses de fin d'année, la hausse du coût de la vie et le besoin d'entrer "
                "dans la nouvelle année avec de la trésorerie créent une urgence immédiate. Beaucoup "
                "dilapident leurs économies en décembre faute d'activité rentable lancée à temps."
            ),
            "N": (
                "Marché massif et saisonnier à très forte réactivité : des millions de francophones en "
                "Afrique de l'Ouest et Centrale (Bénin, Côte d'Ivoire, Sénégal, Togo, Cameroun, Burkina "
                "Faso, Mali, RDC, Guinée, Gabon...) et dans la diaspora veulent agir avant la clôture de l'année."
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
            "q1": "Les futurs entrepreneurs africains francophones (étudiants, salariés, femmes actives, commerçants et diaspora) qui refusent d'attendre janvier pour se lancer.",
            "q2": "Choisir une activité adaptée à son budget réel (Petit, Moyen ou Structuré), la valider en 48 heures sur le terrain et réaliser ses premières ventes avant la fin de l'année.",
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
                ("01", "Introduction", "Pourquoi lancer avant le 31 décembre plutôt qu'attendre janvier, les 5 dynamiques de fin d'année et le guide des trois budgets."),
                ("02", "Erreurs à éviter", "Les 7 erreurs fatales de fin d'année (immobiliser son cash, vendre à crédit, confondre caisse et fêtes, attendre janvier)."),
                ("03", "Étape 1", "Sélectionner son idée : répertoire complet des 500 idées classées en 20 secteurs porteurs en Afrique (25 idées/secteur avec budget Petit, Moyen ou Structuré)."),
                ("04", "Étape 2", "Valider son Top 3 en 48 heures avant d'investir 1\u00A0FCFA grâce à la grille de notation /30, la méthode VIN et le test des 5 vraies conversations."),
                ("05", "Étape 3", "Lancer son business en 7 jours : feuille de route J1 à J7, 3 scripts WhatsApp/Facebook de fin d'année, calcul du prix juste et règle des 3 enveloppes."),
                ("End", "Conclusion", "Engagement daté sur 48h avant le 31 décembre, passage à l'action immédiat, puis page auteur personnalisable et prise de contact."),
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
                "sur [500 idées de business rentables à lancer en Afrique pour bien finir l'année, réparties "
                "en 20 secteurs et 3 niveaux de budget, avec validation en 48h et plan de lancement en 7 jours] "
                "destiné à [des entrepreneurs africains francophones et membres de la diaspora voulant "
                "encaisser avant la fin de l'année sans gros capital]. Le guide doit être clair, simple, "
                "pratique et structuré en étapes. Inclure une introduction motivante, les 7 erreurs à éviter, "
                "3 étapes détaillées (Choisir, Valider, Lancer) et une conclusion actionnable. »"
            ),
            "how_to_use": [
                "1. Prompt copié et adapté avec l'angle précis « bien finir l'année » en Afrique",
                "2. Structuration en 20 secteurs × 25 fiches uniques (500 idées sans doublon)",
                "3. Adaptation locale : montants en FCFA et USD, Mobile Money, pic de fin d'année",
                "4. Relecture linguistique complète et suppression de toute formulation artificielle",
                "5. Mise en page de livre soignée avec couverture illustrée, sommaire et folios",
                "6. Export en PDF final vérifié et conservation des sources éditables pour personnalisation",
            ],
            "checklist": [
                ("J'ai généré la base de contenu avec l'IA", True),
                ("J'ai relu et corrigé (500 idées uniques vérifiées, français naturel)", True),
                ("J'ai simplifié le langage (phrases directes, sans jargon inutile)", True),
                ("J'ai personnalisé avec l'angle fin d'année en Afrique francophone", True),
                ("J'ai mis en page dans un vrai gabarit éditorial de livre (couverture + sommaire)", True),
                ("J'ai enregistré en format PDF (500-Idees-de-Business-a-Lancer-en-Afrique-pour-Bien-Finir-l-Annee.pdf)", True),
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
                ("2. Tu as défini ta promesse", "Formule claire pour lancer en 7 jours avant la fin de l'année", "Accompli"),
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
                    f"« J'ai créé mon premier produit digital ! [Photo de couverture] Après avoir appliqué étape par étape la méthode VIN, défini ma promesse et structuré les 5 parties, voici enfin mon ebook : \"{title}\". Pas besoin d'attendre janvier pour agir. Merci à la communauté pour l'élan ! »"
                ),
                (
                    "Modèle 2 · Publication valeur & urgence fin d'année",
                    "« Pourquoi attendre janvier alors que la fin d'année concentre la plus forte demande de l'année ? J'ai réuni 500 idées concrètes réparties en 20 secteurs africains (du petit budget < 50 000 FCFA aux projets structurés) + une méthode en 48h pour encaisser avant le 31 décembre. Commente \"SOMMAIRE\" si tu veux le découvrir ! »"
                ),
                (
                    "Modèle 3 · Lancement et précommande",
                    f"« OFFRE DE FIN D'ANNÉE : Mon nouveau guide \"{title}\" est disponible en PDF instantané sur téléphone. En bonus : les 7 erreurs à éviter pendant les fêtes et le plan exact des 7 premiers jours avec scripts WhatsApp. Écris-moi en privé ou sur WhatsApp pour recevoir ton exemplaire dès aujourd'hui. »"
                ),
            ],
        },
        "page10": {
            "kicker": "Prochains pas · Page 10",
            "title": "Et maintenant ? Tes prochains pas",
            "steps": [
                (
                    "1. Lance ton produit auprès de dix proches dès cette semaine",
                    "Partage dès aujourd'hui le PDF (ou les dix premières pages en extrait gratuit) à dix personnes ciblées pour récolter leurs vrais retours en quarante-huit heures."
                ),
                (
                    "2. Améliore-le en version 2.0",
                    "Note quelles idées suscitent le plus de questions. Pour l'édition suivante, ajoute des fiches chiffrées détaillées sur les vingt idées favorites de tes premiers lecteurs."
                ),
                (
                    "3. Crée le suivant avec la même méthode",
                    "Suites naturelles faciles à décliner ensuite : « 50 Business à lancer avec moins de 25 000 FCFA », « Modèles de gestion de caisse sur WhatsApp » ou « Plan d'action de rentrée janvier »."
                ),
            ],
            "whatsapp_testers": (
                "Message WhatsApp prêt à envoyer à tes 10 premiers testeurs :\n"
                f"« Salut [Prénom] ! Je viens de finaliser mon tout premier ebook pratique : \"{title}\" (20 secteurs + méthode pour valider en 48h et encaisser avant la fin de l'année). Comme ton avis compte beaucoup pour moi, je t'envoie le PDF en avant-première. Tu peux me dire d'ici 48h : 1) quelle idée t'a le plus marqué, et 2) ce que tu aimerais voir approfondi dans la version 2.0 ? Un grand merci d'avance ! »"
            ),
            "closing": "Le succès n'est pas une destination, c'est un voyage. Bonne continuation dans la communauté des créateurs de produits digitaux !",
        },
    }
