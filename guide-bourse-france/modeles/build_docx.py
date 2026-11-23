"""Génère le fichier Word des modèles de documents du candidat.

Usage (depuis la racine du dépôt) :
    python3 guide-bourse-france/modeles/build_docx.py guide-bourse-france/MODELES-DOCUMENTS-CANDIDAT.docx

Dépendance : python-docx (pip install python-docx).
Les éléments entre crochets [ ... ] sont surlignés en jaune : ils doivent être remplacés.
"""
import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_COLOR_INDEX, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Cm, RGBColor

PLACEHOLDER = re.compile(r"(\[[^\]]+\])")

doc = Document()
for s in doc.sections:
    s.top_margin = s.bottom_margin = Cm(2.2)
    s.left_margin = s.right_margin = Cm(2.2)

style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)
style.paragraph_format.space_after = Pt(6)
style.paragraph_format.line_spacing = 1.15


def add_runs(par, text, bold=False, italic=False, size=None):
    """Ajoute du texte ; les [placeholders] sont surlignés en jaune."""
    for part in PLACEHOLDER.split(text):
        if not part:
            continue
        run = par.add_run(part)
        run.bold = bold
        run.italic = italic
        if size:
            run.font.size = Pt(size)
        if PLACEHOLDER.fullmatch(part):
            run.font.highlight_color = WD_COLOR_INDEX.YELLOW
    return par


def p(text="", bold=False, italic=False, size=None, align=None, indent=None):
    par = doc.add_paragraph()
    if indent is not None:
        par.paragraph_format.left_indent = Cm(indent)
    if align == "right":
        par.alignment = 2
    add_runs(par, text, bold=bold, italic=italic, size=size)
    return par


def bullet(text):
    par = doc.add_paragraph(style="List Bullet")
    add_runs(par, text)
    return par


def h1(text):
    doc.add_heading(text, level=1)


def h2(text):
    doc.add_heading(text, level=2)


def note(text):
    par = doc.add_paragraph()
    run = par.add_run(text)
    run.italic = True
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    return par


def page_break():
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def shade(cell, hex_color):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tc_pr.append(shd)


def table(headers, rows=3, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, htxt in enumerate(headers):
        cell = t.rows[0].cells[i]
        cell.text = ""
        add_runs(cell.paragraphs[0], htxt, bold=True, size=9.5)
        shade(cell, "E8EEF7")
    for _ in range(rows):
        cells = t.add_row().cells
        for c in cells:
            c.text = ""
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return t


def letter_block(lines):
    for line in lines:
        p(line)


# ---------------------------------------------------------------- Couverture
p("Décroche ta bourse française toi-même", bold=True, size=22)
p("Modèles de documents à rédiger pour le candidat", size=14)
p("Version de référence : 22 novembre 2026", italic=True, size=10)
doc.add_paragraph()
note("Compagnon du guide « Décroche ta bourse française toi-même ». Les modèles sont des points de départ. "
     "Chaque élément entre crochets surligné en jaune doit être remplacé par tes propres informations. "
     "N'envoie jamais un modèle tel quel : un jury repère immédiatement un texte générique.")
page_break()

# ---------------------------------------------------------------- Sommaire
h1("Sommaire des modèles")
for line in [
    "1. Lettre de motivation",
    "2. Projet d'études",
    "3. Projet professionnel",
    "4. Curriculum vitae",
    "5. Demande de lettre de recommandation",
    "6. Lettre explicative (interruption, redoublement, changement de filière)",
    "7. Demande d'attestation de rang dans la promotion",
    "8. Mail à un établissement pour la bourse Eiffel",
    "9. Réponse à une demande de correction de Campus France",
    "10. Relance d'un établissement sans réponse",
    "11. Remerciement après l'entretien",
    "12. Remerciement au recommandeur",
    "13. Préparation de l'entretien Campus France",
    "14. Budget mensuel",
    "15. Tableau de suivi des candidatures",
    "16. Tableau de suivi des bourses",
    "17. Note de suivi hebdomadaire",
]:
    p(line, indent=0.5)
page_break()

# ---------------------------------------------------------------- 1 Lettre de motivation
h1("1. Lettre de motivation")
note("Structure : accroche, parcours, formation visée, projet, conclusion. Une page et demie, 500 à 800 mots, en français "
     "(sauf indication contraire de la formation). Chaque affirmation doit être prouvable par une pièce du dossier.")
h2("Modèle à compléter")
letter_block([
    "[Ville], le [date]",
    "",
    "Madame, Monsieur,",
    "",
    "[Accroche : un fait précis, par exemple : « Lors de mon stage à [structure], j'ai constaté que [problème]. "
    "C'est ce constat qui m'a conduit(e) vers [domaine]. »]",
    "",
    "Après l'obtention de mon [diplôme] en [discipline] à [établissement], en [année], j'ai choisi de [action]. "
    "[Un ou deux éléments de parcours qui montrent une progression, avec un résultat chiffré si tu peux le prouver.] "
    "Ces expériences m'ont appris [compétence précise] et m'ont donné envie d'approfondir [thème].",
    "",
    "Je souhaite intégrer le [nom du master] à [établissement]. Le programme [cite un cours, un module, un laboratoire "
    "ou un enseignant précis] correspond à ce que je cherche : [explication du lien avec ton projet].",
    "",
    "À mon retour au Bénin, je souhaite [projet précis : poste, structure, problème à résoudre]. "
    "[Une phrase qui montre que tu as réfléchi à la façon dont tu appliqueras ces compétences.]",
    "",
    "Je vous remercie de l'attention portée à ma candidature et reste à votre disposition pour un entretien.",
    "",
    "Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.",
    "",
    "[Prénom et nom]",
])
h2("Vérification avant envoi")
for line in [
    "La lettre est adaptée à la formation visée (nom exact, établissement exact).",
    "Chaque affirmation peut être prouvée par le dossier.",
    "Le projet professionnel est précis, et non générique.",
    "Aucune faute d'orthographe ni de grammaire ; lecture à voix haute faite.",
    "Lettre datée et signée.",
]:
    bullet(line)
page_break()

# ---------------------------------------------------------------- 2 Projet d'études
h1("2. Projet d'études")
note("Réponds à cinq questions : le problème, pourquoi moi, pourquoi cette formation, pourquoi la France, que feras-tu après. "
     "Deux pages maximum sauf indication contraire du formulaire.")
h2("Plan à suivre")
table(["Partie", "Ce que tu écris", "Longueur indicative"], rows=5, widths=[4, 10, 3])
h2("Modèle à compléter")
letter_block([
    "Contexte. [Décris la situation concrète qui t'a conduit à ce projet : un problème observé, une expérience, des chiffres.]",
    "",
    "Mon parcours. [Diplôme actuel, établissement, moyenne ou résultats marquants, expériences utiles.]",
    "",
    "Ce que je veux apprendre. La formation [nom] à [établissement] me permettrait d'acquérir [compétences précises]. "
    "Le module [nom] et le laboratoire [nom] répondent à [besoin précis].",
    "",
    "Pourquoi la France. [Éléments précis : recherche, méthode, réseau, accès à des données ou à des terrains.]",
    "",
    "Mon projet après la formation. [Type de structure, poste ou projet, zone géographique, échéance.]",
])
page_break()

# ---------------------------------------------------------------- 3 Projet professionnel
h1("3. Projet professionnel")
note("Le projet professionnel fait l'objet d'une notation spécifique pour la bourse Eiffel. Lis la grille officielle "
     "de notation (master ou doctorat) sur le site de Campus France avant de rédiger.")
h2("Questions à répondre par écrit")
table(["Question", "Ta réponse"], rows=6, widths=[7, 10])
h2("Modèle de synthèse")
letter_block([
    "Problème. [Le problème précis que je veux résoudre, dans quel secteur et quelle zone.]",
    "Compétence. [La compétence que je dois acquérir, et pourquoi cette formation la donne.]",
    "Action. [Ce que je ferai concrètement à mon retour : structure, fonction, premier projet.]",
    "Horizon. [Ce que je pense faire dans trois ans, puis dans dix ans.]",
    "Preuve. [Démarches déjà faites : échanges avec des professionnels, lectures, stages, projets.]",
])
page_break()

# ---------------------------------------------------------------- 4 CV
h1("4. Curriculum vitae")
note("Une page, en français, format Europass si possible. Chaque expérience doit contenir une action et un résultat. "
     "Chaque information doit pouvoir être vérifiée.")
p("[PRÉNOM NOM]", bold=True, size=14)
p("[Adresse, ville, pays] · [téléphone] · [e-mail] · Nationalité : [nationalité]")
h2("Formation")
p("[Année] — [Diplôme] en [discipline], [établissement], [ville]. Mention : [mention].")
p("[Année] — Baccalauréat série [série], [lycée], [ville]. Mention : [mention].")
h2("Expériences")
p("[Mois Année] – [Mois Année] — [Poste ou stage], [structure], [ville]", bold=True)
bullet("[Verbe d'action + tâche + résultat]")
bullet("[Verbe d'action + tâche + résultat]")
p("[Mois Année] – [Mois Année] — [Poste ou bénévolat], [structure], [ville]", bold=True)
bullet("[Verbe d'action + tâche + résultat]")
h2("Compétences")
bullet("Informatique : [outils, logiciels, langages]")
bullet("Langues : Français ([niveau], [preuve, date]) ; Anglais ([niveau], [preuve, date])")
bullet("Techniques : [compétences propres à ta discipline]")
h2("Engagements")
bullet("[Année] — [Association ou club], [rôle], [action principale]")
h2("Centres d'intérêt")
bullet("[Deux ou trois activités, en une ligne]")
page_break()

# ---------------------------------------------------------------- 5 Recommandation
h1("5. Demande de lettre de recommandation")
note("Demande-la au moins quatre à six semaines avant la date limite interne. Donne au recommandeur ton CV, ta lettre, "
     "ton projet et trois à cinq faits précis que vous avez vécus ensemble.")
letter_block([
    "Objet : Demande de lettre de recommandation pour une candidature en master",
    "",
    "Bonjour [Titre] [Nom],",
    "",
    "Je suis [prénom nom], étudiant(e) en [discipline] à [établissement]. J'ai suivi votre [cours, encadrement ou mission] "
    "en [année], et votre accompagnement a beaucoup compté dans mon parcours.",
    "",
    "Je prépare une candidature au master [nom] à [établissement en France], dont la date limite est le [date]. "
    "Je serais très reconnaissant(e) si vous acceptiez de rédiger une lettre de recommandation me concernant. "
    "Je peux vous transmettre mon CV, ma lettre de motivation et mon projet d'études.",
    "",
    "La lettre doit être envoyée [mode d'envoi] avant le [date interne]. Je reste à votre disposition pour toute information.",
    "",
    "Merci d'avance pour votre temps et votre soutien.",
    "",
    "[Prénom nom] — [téléphone] — [e-mail]",
])
h2("Éléments à transmettre au recommandeur")
table(["Élément", "Fourni (oui/non)"], rows=5, widths=[12, 5])
page_break()

# ---------------------------------------------------------------- 6 Lettre explicative
h1("6. Lettre explicative")
note("À utiliser si ton dossier comporte une interruption, un redoublement, un changement de filière ou un écart de notes. "
     "Reste factuel, bref et sans justification excessive. Une seule page.")
letter_block([
    "[Ville], le [date]",
    "",
    "Objet : Explication sur mon parcours académique — dossier [numéro BJ ou référence]",
    "",
    "Madame, Monsieur,",
    "",
    "Dans le cadre de ma candidature, je souhaite apporter une précision sur mon parcours. "
    "[Fait précis : année concernée, nature de l'interruption, du redoublement ou du changement de filière.]",
    "",
    "[Ce qui s'est passé, en deux ou trois phrases factuelles.]",
    "",
    "Pendant cette période, j'ai [ce que tu as appris ou réalisé : formation, stage, travail, projet].",
    "",
    "Depuis [date], j'ai repris mon parcours avec [résultat ou situation actuelle], comme le montrent les pièces jointes "
    "[liste des pièces].",
    "",
    "Je reste à votre disposition pour toute précision.",
    "",
    "Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.",
    "",
    "[Prénom nom]",
])
page_break()

# ---------------------------------------------------------------- 7 Attestation de rang
h1("7. Demande d'attestation de rang dans la promotion")
letter_block([
    "Objet : Demande d'attestation de rang dans la promotion",
    "",
    "Madame, Monsieur,",
    "",
    "Je suis [prénom nom], étudiant(e) en [filière], promotion [année], matricule [numéro].",
    "",
    "Dans le cadre d'une candidature à une formation à l'étranger, je vous serais reconnaissant(e) de bien vouloir me délivrer "
    "une attestation de rang dans la promotion pour les années [années concernées], ou, à défaut, une attestation équivalente "
    "précisant le mode de classement.",
    "",
    "Je reste à votre disposition pour fournir tout justificatif complémentaire. Je vous remercie d'avance pour votre aide.",
    "",
    "[Prénom nom] — [téléphone] — [e-mail]",
])
page_break()

# ---------------------------------------------------------------- 8 Mail Eiffel
h1("8. Mail à un établissement pour la bourse Eiffel")
letter_block([
    "Objet : Demande d'information sur la candidature à la bourse Eiffel — session 2027",
    "",
    "Madame, Monsieur,",
    "",
    "Je suis [prénom nom], [titulaire d'une licence en discipline à établissement d'origine, ou étudiant(e) en année de ...]. "
    "Je souhaite candidater à la formation [intitulé exact] au sein de votre établissement, et je m'intéresse à la bourse "
    "France Excellence Eiffel pour la session 2027.",
    "",
    "Pourriez-vous m'indiquer :",
    "1. votre date limite interne de réception des candidatures Eiffel ;",
    "2. la liste exacte des pièces que vous attendez de ma part ;",
    "3. le nom et les coordonnées de la personne qui instruit les dossiers Eiffel ;",
    "4. le calendrier de vos échanges avec les candidats.",
    "",
    "Je reste à votre disposition et vous remercie de l'attention portée à ma demande.",
    "",
    "Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées.",
    "",
    "[Prénom nom] — [téléphone] — [e-mail]",
])
page_break()

# ---------------------------------------------------------------- 9 Réponse correction
h1("9. Réponse à une demande de correction de Campus France")
letter_block([
    "Objet : Réponse à la demande de correction — dossier [numéro BJ]",
    "",
    "Bonjour,",
    "",
    "En réponse à votre demande du [date], veuillez trouver ci-joint [liste des documents corrigés ou complétés].",
    "",
    "[Si nécessaire : Pour la pièce [nom], je ne peux pas la fournir car [raison précise], et je joins à la place [justificatif].]",
    "",
    "Je reste à votre disposition pour toute précision.",
    "",
    "[Prénom nom] — Numéro BJ : [BJXX-XXXXX]",
])
note("Nomme chaque fichier joint de façon claire, par exemple : releve_licence_2024_corrige.pdf.")
page_break()

# ---------------------------------------------------------------- 10 Relance
h1("10. Relance d'un établissement sans réponse")
letter_block([
    "Objet : Relance — candidature [formation] — dossier [numéro]",
    "",
    "Madame, Monsieur,",
    "",
    "Je me permets de revenir vers vous au sujet de ma candidature en [formation], déposée le [date] sous le numéro [numéro]. "
    "Je n'ai pas encore reçu de réponse et je souhaite connaître l'état d'avancement de mon dossier.",
    "",
    "Je reste à votre disposition pour tout document complémentaire.",
    "",
    "Merci d'avance. [Prénom nom]",
])
page_break()

# ---------------------------------------------------------------- 11 Remerciement entretien
h1("11. Remerciement après l'entretien")
letter_block([
    "Objet : Remerciements — entretien du [date]",
    "",
    "Bonjour [Titre] [Nom],",
    "",
    "Je vous remercie pour l'entretien que vous m'avez accordé le [date]. Vos conseils sur [point précis] m'ont été très utiles, "
    "et je vais les appliquer dans la suite de mon dossier.",
    "",
    "Je reste à votre disposition pour toute information complémentaire.",
    "",
    "Bien cordialement,",
    "",
    "[Prénom nom]",
])
page_break()

# ---------------------------------------------------------------- 12 Remerciement recommandeur
h1("12. Remerciement au recommandeur")
letter_block([
    "Objet : Merci pour votre lettre de recommandation",
    "",
    "Bonjour [Titre] [Nom],",
    "",
    "Je tiens à vous remercier d'avoir accepté de rédiger une lettre de recommandation pour ma candidature en [formation]. "
    "Votre soutien compte beaucoup pour moi.",
    "",
    "Je vous tiendrai informé(e) de la suite de ma candidature.",
    "",
    "Bien respectueusement,",
    "",
    "[Prénom nom]",
])
page_break()

# ---------------------------------------------------------------- 13 Entretien
h1("13. Préparation de l'entretien Campus France")
note("Remplis une réponse écrite pour chaque question, en suivant la structure : réponse, preuve, ouverture. "
     "Puis entraîne-toi à la dire à voix haute. Ne récite pas un texte appris par cœur.")
h2("Ta présentation (3 à 5 minutes)")
table(["Partie", "Ce que je dis"], rows=3, widths=[5, 12])
h2("Questions types")
table(["Question", "Ma réponse (réponse, preuve, ouverture)"], rows=12, widths=[6, 11])
h2("Questions à poser au conseiller")
for _ in range(3):
    bullet("[Question]")
page_break()

# ---------------------------------------------------------------- 14 Budget
h1("14. Budget mensuel")
note("Remplis ce tableau avec les montants vérifiés sur les sites officiels. Le montant de référence du visa se confirme "
     "sur France-Visas au moment du dépôt. Ne te fie pas aux montants publiés sur les blogs.")
t = table(["Poste", "Montant mensuel estimé", "Source de l'information"], rows=7, widths=[6, 4.5, 6.5])
for i, label in enumerate(["Logement", "Nourriture", "Transports", "Assurance santé",
                           "Téléphone et internet", "Fournitures et livres", "Loisirs et imprévus (10 %)"], start=1):
    t.rows[i].cells[0].text = label
t.add_row().cells[0].text = "Total mensuel"
h2("Coûts ponctuels")
table(["Poste", "Montant", "Date prévue"], rows=6, widths=[8, 4, 5])
page_break()

# ---------------------------------------------------------------- 15 Suivi candidatures
h1("15. Tableau de suivi des candidatures")
table(["Établissement", "Formation", "Date de dépôt", "Statut", "Pièces demandées", "Date de réponse"], rows=8,
      widths=[3.2, 3.2, 2.4, 2.4, 3.2, 2.6])
page_break()

# ---------------------------------------------------------------- 16 Suivi bourses
h1("16. Tableau de suivi des bourses")
note("Une ligne par programme. Mets à jour chaque semaine.")
table(["Programme", "Niveau", "Date limite", "Passe par un établissement ?", "Montant", "Pièces demandées", "Statut"],
      rows=8, widths=[3, 2.2, 2.2, 2.6, 2, 2.6, 1.8])
page_break()

# ---------------------------------------------------------------- 17 Note hebdo
h1("17. Note de suivi hebdomadaire")
note("Prends dix minutes chaque dimanche pour remplir cette note.")
table(["Date", "Démarche réalisée", "Interlocuteur", "Résultat", "Prochaine action", "Échéance"], rows=6,
      widths=[2, 4, 3, 3, 3, 2])

out = sys.argv[1] if len(sys.argv) > 1 else "MODELES-DOCUMENTS-CANDIDAT.docx"
doc.save(out)
print("écrit :", out)
