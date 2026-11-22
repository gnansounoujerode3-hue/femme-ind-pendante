"""Atelier éditable. Les gabarits restent distincts des exemples rédigés du livret."""
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from commun import BONUS, DOCX

TITRES=['CV de candidature','Lettre de motivation','Mon Study Plan : projet d’études','Note d’intention pour une thèse','Contacter une formation','Demande de recommandation','Relance après un premier contact','Préparation de l’entretien']

def make():
    d=Document();sec=d.sections[0];sec.page_height=Cm(29.7);sec.page_width=Cm(21)
    sec.left_margin=sec.right_margin=Cm(2.15);sec.top_margin=Cm(2.2);sec.bottom_margin=Cm(2)
    sec.header_distance=Cm(1);sec.footer_distance=Cm(1)
    props=d.core_properties;props.title='Mon dossier France — Atelier de candidature';props.author='Mon dossier France';props.subject='Huit modèles à personnaliser avant tout dépôt'
    normal=d.styles['Normal'];normal.font.name='Calibri';normal.font.size=Pt(12);normal.font.color.rgb=RGBColor.from_string('203B3D');normal.paragraph_format.space_after=Pt(6)
    normal.paragraph_format.line_spacing=1.14
    lang=OxmlElement('w:lang');lang.set(qn('w:val'),'fr-FR');normal.element.get_or_add_rPr().append(lang)
    for name,size,color,bold,space in [('Surtitre',10,'226965',True,5),('Consigne',11,'48656A',False,13),('Intertitre',13,'176563',True,3),('Titre pratique',26,'123F41',True,9),('Discret',9,'48656A',False,3)]:
        s=d.styles.add_style(name,WD_STYLE_TYPE.PARAGRAPH);s.base_style=normal;s.font.size=Pt(size);s.font.bold=bold;s.font.color.rgb=RGBColor.from_string(color);s.paragraph_format.space_after=Pt(space)
        if name in ('Titre pratique','Intertitre','Surtitre'):s.paragraph_format.keep_with_next=True
    h=sec.header.paragraphs[0];h.style='Discret';h.text='MON DOSSIER FRANCE     /     ATELIER PERSONNEL';h.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    f=sec.footer.paragraphs[0];f.style='Discret';f.add_run('DOCUMENT DE TRAVAIL  •  EXTRAIRE LE MODÈLE AVANT ENVOI                                    ')
    field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');f._p.append(field)
    def p(text,sty=None):return d.add_paragraph(text,style=sty)
    def h2(text):p(text,'Intertitre')
    def note(text):p(text,'Consigne')
    def table(rows):
        t=d.add_table(rows=0,cols=len(rows[0]));t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.style='Light Shading Accent 1'
        for i,arr in enumerate(rows):
            cells=t.add_row().cells
            for j,txt in enumerate(arr):
                cell=cells[j];cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
                shade=OxmlElement('w:shd');shade.set(qn('w:fill'),'164844' if i==0 else ('ECF4EF' if i%2 else 'FFFFFF'));cell._tc.get_or_add_tcPr().append(shade)
                pp=cell.paragraphs[0];pp.paragraph_format.space_before=Pt(4);pp.paragraph_format.space_after=Pt(4)
                r=pp.add_run(txt);r.bold=i==0;r.font.size=Pt(10.5);r.font.color.rgb=RGBColor.from_string('FFFFFF' if i==0 else '203B3D')
        p('','Discret')
    def begin(i,desc):
        d.add_page_break();p(f'GABARIT   /   {i:02d}', 'Surtitre');p(TITRES[i-1],'Titre pratique');note(desc)
    p('LES OUTILS   /   RENTRÉE 2027','Surtitre');p('Atelier de candidature','Titre pratique')
    p('Huit modèles pour préparer ton propre dossier, pas huit pièces à joindre systématiquement. Le formulaire officiel et ses consignes de langue et de longueur passent toujours en premier.')
    h2('Comment t’en servir sur téléphone ou ordinateur')
    p('1. Fais une copie de cet atelier. Choisis seulement le gabarit dont tu as besoin.');p('2. Copie son contenu dans un document vierge ou dans ton brouillon d’e-mail. Remplace chaque passage entre crochets, adapte le ton et supprime ce qui ne te concerne pas.');p('3. Avant envoi, retire titre du gabarit, consignes, crochets et en-tête. Vérifie les faits, le destinataire et le nom du fichier. Exporte en PDF seulement si la notice le demande.')
    table([['N°','Gabarits','Usage'],['01–02','CV • Lettre','Présenter ton parcours et tes raisons.'],['03–04','Projet d’études • Note de thèse','Définir la compétence ou la question de recherche.'],['05–07','Prise de contact • Recommandation • Relance','Écrire au bon service avec une question précise.'],['08','Fiche d’entretien','Répéter sans apprendre un discours par cœur.']])
    note('Ne transmets pas cet atelier en entier. Il ne remplace ni les formulaires officiels ni une recommandation rédigée par son véritable auteur.')
    begin(1,'Commence à ton nom. Garde une page si elle suffit ; respecte la longueur exigée par le programme. Retire les rubriques vides.')
    p('[PRÉNOM NOM]','Titre pratique');p('[Ville, pays]  •  [E-mail personnel consulté]  •  [Téléphone avec indicatif, si utile]')
    h2('Objectif');p('Candidature à [intitulé exact, niveau, rentrée] — [spécialité / question qui motive mon choix].')
    h2('Formation');p('[Mois/année – mois/année ou « en cours »]  |  [Diplôme et mention]');p('[Établissement, ville, pays] — [cours ou mémoire pertinent]. [Résultat vérifiable si demandé ; ne pas inventer un classement.]')
    h2('Projet ou expérience');p('[Dates]  |  [Fonction réelle ou nom du projet], [structure]');p('• [Action que j’ai réalisée] avec [outil / méthode] pour [objectif].');p('• [Résultat ou livrable précis]. [En équipe : préciser ma contribution.]')
    h2('Engagement ou activité');p('[Période] — [Rôle] : [action et effet observé, sans exagération].')
    h2('Compétences et langues');p('[Outil] : utilisé pour [travail concret].  •  [Langue] : [niveau réel ; certification, score et date, si disponible].')
    begin(2,'Si l’école pose des questions précises, réponds directement à ces questions au lieu de joindre une lettre séparée. Respecte ses règles d’usage de l’IA.')
    p('[Ville], le [date]\nÀ l’attention de [jury / service indiqué]');p('Objet : candidature à [programme et, si demandé, bourse], rentrée [année]');p('Madame, Monsieur,')
    p('À [lieu / date], j’ai rencontré [situation concrète]. Dans le cadre de [cours / stage / engagement], ma responsabilité était de [action exacte]. [Résultat que je peux expliquer ; difficulté ou limite rencontrée.]')
    p('Cette expérience m’a amené(e) à me poser la question suivante : [question]. J’ai déjà appris à [acquis], mais il me manque [compétence précise]. Dans votre programme, [enseignement, atelier ou méthode dont j’ai vérifié l’existence] me permettrait de [usage concret].')
    p('Après la formation, mon premier objectif serait de [activité réaliste], auprès de [public ou secteur]. [Si le jury le demande : dépense que l’aide rendrait possible, durée et raison ; distinguer faits et projet.]')
    p('Je vous remercie de l’attention portée à ma candidature.\n[Signature / Prénom Nom]')
    note('Relecture : si tu changes le nom de l’école, quel passage devient faux ? Si la réponse est « aucun », reprends le paragraphe sur la formation.')
    begin(3,'Plan de travail pour une note de projet de master. Ajuste-le si l’établissement fournit son propre modèle.')
    p('[Titre précis du projet]  |  [Diplôme visé, établissement, rentrée]','Surtitre')
    h2('1. Ma question de départ');p('[Situation observée et raison de m’y intéresser. Fait vérifiable de mon parcours qui me permet de poser cette question.]')
    h2('2. Ce que je vais apprendre');p('[Compétence à acquérir] pour pouvoir [tâche professionnelle]. [Unité d’enseignement ou activité du programme vérifiée sur sa maquette.]')
    h2('3. Comment je compte m’y prendre');table([['Étape','Travail réalisable','Trace attendue'],['[Semestre / période]','[Cours et entraînement précis]','[Exercice / compte rendu]'],['[Semestre / période]','[Projet, stage espéré ou mémoire]','[Livrable réaliste]']])
    h2('4. Après le diplôme');p('[Premier usage du savoir acquis, public concerné, résultat raisonnable. Ne pas annoncer comme acquis un poste ou un partenariat espéré.]')
    h2('Question de faisabilité');p('[Que ferai-je si l’accès aux données / au stage / au terrain n’est pas obtenu ?]')
    begin(4,'À utiliser avant un échange avec un encadrant. Une école doctorale peut demander une autre structure, bibliographie comprise.')
    h2('[Titre provisoire]');p('Question : [une question délimitée par un objet, un lieu ou un corpus, et une période].')
    h2('État des travaux');p('[Deux ou trois références réellement lues ; pour chacune, résultat utile et question encore ouverte. Vérifier les références exactes.]')
    h2('Méthode et faisabilité');p('[Données ou corpus accessibles, méthode envisagée, autorisations requises, limites et solution de repli. Ne pas confondre accès espéré et accès autorisé.]')
    h2('Accueil et encadrement');p('[Laboratoire, équipe et correspondance avec ses axes réels]. [Personnes contactées, accord écrit ou discussion en cours]. [Cotutelle ou codirection seulement si applicable.]')
    h2('Calendrier et financement');table([['Période et lieu','Travail prévu','Financement : confirmé / à obtenir'],['[Mois, pays]','[Recherche / collecte]','[Source, durée, justificatif]'],['[Mois, pays]','[Analyse / rédaction]','[Mois non couverts, démarche prévue]']])
    p('Question à poser : [attente du laboratoire, voie de candidature ou règle financière encore incertaine].')
    begin(5,'Pour vérifier une présélection Eiffel ou clarifier une consigne non publiée. Lis d’abord la page de la formation. N’envoie pas le même message à des dizaines de responsables.')
    p('À : [adresse professionnelle indiquée par la formation]\nObjet : [Intitulé du master] — présélection Eiffel [session]');p('Madame / Monsieur [nom],')
    p('Je prépare / j’ai obtenu [diplôme, établissement et pays]. Mon travail sur [projet précis] m’a conduit(e) à envisager votre [nom exact du parcours], notamment pour [enseignement vérifié ou axe de recherche].')
    p('J’ai consulté [titre de l’appel et lien officiel]. Pourriez-vous me confirmer [une question non résolue : date interne, justificatif accepté, personne à contacter ou mode de dépôt] ? Je souhaite aussi m’assurer de suivre séparément la bonne procédure d’admission à la formation.')
    p('[Si demandé : je joins mon CV et les pièces indiquées dans l’appel.]\nMerci pour votre aide.\n[Prénom Nom, établissement, pays et e-mail]')
    h2('Variante : demander une lettre de préadmission')
    p('Objet : [Master / rentrée] — justificatif d’admission pour [bourse]. « Ma candidature n° […] est [statut exact]. La notice du financeur demande [intitulé de la pièce] avant le [date]. Votre service peut-il délivrer ce document à mon stade ? Si l’offre est conditionnelle, pourriez-vous préciser les conditions et le délai pour les lever ? Merci. »')
    note('Adresse la demande aux admissions ; seul le service compétent délivre la lettre. Un e-mail de premier contact ne vaut ni dépôt, ni admission, ni nomination à Eiffel.')
    begin(6,'Demande l’accord d’une personne qui a vu ton travail. Il s’agit d’un message de demande, jamais d’une lettre à signer à sa place.')
    p('Objet : recommandation pour [programme] — échéance [date et fuseau]');p('Bonjour [titre et nom],')
    p('Vous avez encadré mon [TD / mémoire / stage] sur [sujet] en [période]. J’y ai notamment [tâche permettant de me resituer]. Je souhaite candidater à [formation et établissement] pour y apprendre [objectif].')
    p('Seriez-vous disponible pour recommander ma candidature avant le [date, heure, fuseau] ? Le programme demande [langue, format ou formulaire]. [Si envoi direct : après votre accord, le portail vous écrira à votre adresse institutionnelle et vous seul(e) transmettrez la recommandation.]')
    p('Je peux vous envoyer mon CV, le descriptif du programme et [travail corrigé ou livrable]. Si ce délai ne vous convient pas, je comprends tout à fait.')
    p('Merci de votre réponse.\n[Prénom Nom, promotion, e-mail]')
    h2('Notes privées');p('Accord reçu le : [date]     •     Adresse confirmée : [adresse institutionnelle]\nLien reçu : [oui / à vérifier]     •     Statut sur le portail : [statut]')
    begin(7,'Une relance courte suffit généralement. Respecte le délai de réponse annoncé et vérifie d’abord le statut et les indésirables.')
    p('Objet : suivi de [objet du premier message] — [identifiant de dossier si utile]');p('Bonjour [titre / service],')
    p('Je me permets de revenir vers vous au sujet de [question unique], transmise le [date]. Je candidate à [intitulé et session] et la date indiquée dans la notice est le [date, fuseau].')
    p('J’ai vérifié [portail ou rubrique] et j’y vois [statut exact]. Pourriez-vous m’indiquer [action attendue : confirmer la réception / préciser la pièce manquante / m’orienter vers le bon service] ?')
    p('Merci pour votre aide.\n[Prénom Nom, référence si demandée]')
    h2('Variante : confirmation de présentation Eiffel');p('« Pour éviter une double présentation, pourriez-vous me confirmer si mon dossier a été retenu et déposé par votre établissement pour la session [année] ? »')
    note('Ne renvoie pas de documents sensibles en pièces jointes sans demande du destinataire officiel. Une absence de réponse n’est ni un accord ni un refus.')
    begin(8,'Une page de notes pour répéter. N’apprends pas un texte mot à mot. À adapter selon qu’il s’agit d’un entretien pédagogique, d’admission ou de bourse.')
    p('Convocation : [organisme, date, heure, fuseau, langue, lieu ou lien]')
    table([['Question','Mes mots-clés (deux lignes maximum)'],['Pourquoi ce programme ?','[Cours précis + compétence qui me manque]'],['Qu’ai-je fait moi-même ?','[Situation, action personnelle, résultat, limite]'],['Pourquoi cette bourse ?','[Dépense précise, montant documenté, ce qui reste]'],['Quel projet ensuite ?','[Premier usage concret, pour qui et avec quelle méthode]'],['Et en cas de refus ?','[Plan réaliste sans financer le séjour par une somme hypothétique]']])
    h2('Ma répétition');p('Fait que je dois encore vérifier : [source et action].\nQuestion posée par mon binôme : [question].\nRéponse trop vague à reprendre : [phrase].')
    h2('Avant le rendez-vous');p('□ Convocation relue     □ Dossier soumis relu     □ Originaux demandés prêts\n□ Test audio si entretien en ligne     □ Budget revu, aides acquises et en attente distinguées')
    BONUS.mkdir(exist_ok=True);d.save(DOCX)

if __name__=='__main__':make()
