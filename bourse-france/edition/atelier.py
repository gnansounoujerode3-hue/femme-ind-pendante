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
        return t
    def begin(i,desc):
        d.add_page_break()
        titre=p(f'GABARIT   /   {i:02d}', 'Surtitre')
        start=OxmlElement('w:bookmarkStart');start.set(qn('w:id'),str(i));start.set(qn('w:name'),f'Modele_{i:02d}')
        end=OxmlElement('w:bookmarkEnd');end.set(qn('w:id'),str(i))
        titre.runs[0]._r.addprevious(start);titre._p.append(end)
        p(TITRES[i-1],'Titre pratique');note(desc)
    p('LES OUTILS   /   RENTRÉE 2027','Surtitre');p('Atelier de candidature','Titre pratique')
    p('Ce fichier est ton brouillon. Un modèle, aussi appelé « gabarit », te propose des cases et des questions. Il ne dit pas ce que tu as fait à ta place. Tu n’as pas huit documents à envoyer.')
    h2('Que demande l’école ? Choisis une seule ligne.')
    index=table([['Si tu as besoin de…','Touche le modèle…'],['Résumer tes études, même sans emploi','01 · CV'],['Dire pourquoi tu veux cette place','02 · Lettre de motivation'],['Expliquer comment tu vas étudier','03 · Plan d’études (Study Plan)'],['Présenter une question de recherche','04 · Projet de thèse'],['Poser une question à l’école ou demander une préadmission','05 · Premier contact'],['Demander à un professeur son avis sur ton travail','06 · Demande de recommandation'],['Reprendre contact après un premier message','07 · Relance'],['T’entraîner pour un rendez-vous','08 · Entretien']])
    for i,row in enumerate(index.rows[1:],1):
        # Le numéro reste lisible si le lecteur Word ne suit pas les liens internes.
        pp=row.cells[1].paragraphs[0];r=pp.runs[0];r.underline=True;r.font.color.rgb=RGBColor.from_string('176563')
        lien=OxmlElement('w:hyperlink');lien.set(qn('w:anchor'),f'Modele_{i:02d}');lien.append(r._r);pp._p.append(lien)
    note('Si l’école te donne son propre formulaire, réponds dans celui de l’école. Première fois ? Fais le petit essai à la page suivante. Ne joins pas ce cahier entier et ne signe jamais à la place de la personne qui te recommande.')
    d.add_page_break();p('MON PREMIER ESSAI   /   AUCUN ENVOI','Surtitre');p('Transformer un modèle en mon CV','Titre pratique')
    h2('1. Ouvre et copie')
    p('Ouvre Atelier-dossier.docx dans Word ou une application qui peut le modifier. Si tu ne peux pas écrire, tu es peut-être dans un simple aperçu. Cherche « Ouvrir avec » ou « Modifier ». Garde cet original pour pouvoir recommencer.')
    p('Va au modèle 01. Sélectionne le texte à partir de [PRÉNOM NOM], sans le titre du modèle ni ses consignes. Sur téléphone, garde le doigt sur un mot puis déplace les deux poignées pour élargir la sélection. Choisis « Copier ». Ouvre un document vide, puis « Coller ». Les boutons dépendent de ton appareil.')
    h2('2. Remplace : un exemple avant et après')
    p('Avant : « [Action que j’ai réalisée] avec [outil / méthode] pour [objectif]. »')
    p('Après, pour Nadia, étudiante imaginaire : « Pendant quatre matinées, j’ai noté dans un tableau les temps d’attente à deux arrêts de bus. » Elle peut montrer le tableau. Tes mots à toi doivent raconter un travail que tu connais, même un simple exercice de cours.')
    p('Écris ton nom à la place de [PRÉNOM NOM]. Remplace tous les autres crochets. Tu n’as pas fait de stage ? Retire la rubrique vide ou décris un vrai projet de classe dans la rubrique appropriée.')
    h2('3. Enregistre et rouvre')
    p('Donne au nouveau fichier un nom comme CV_NOM.docx. Si la notice demande un PDF, utilise « Exporter en PDF » ou l’option équivalente. Changer les lettres du nom du fichier ne change pas son format.')
    note('Test : ferme puis rouvre le nouveau fichier. Il ne reste ni crochet, ni consigne, ni autre modèle ? Tu peux expliquer chaque ligne ? Le CV est prêt à être relu. Ne le joins que sur le site demandé. Sans application compatible, commence ces réponses dans un cahier.')
    begin(1,'Un CV résume ce que tu as étudié et fait. Copie à partir de [PRÉNOM NOM], remplace les crochets puis retire les rubriques vides. Une page suffit si tout y tient et si l’école le permet.')
    p('[PRÉNOM NOM]','Titre pratique');p('[Ville, pays]  •  [E-mail personnel consulté]  •  [Téléphone avec indicatif, si utile]')
    h2('Objectif');p('Candidature à [intitulé exact, niveau, rentrée] — [spécialité / question qui motive mon choix].')
    h2('Formation');p('[Mois/année – mois/année ou « en cours »]  |  [Diplôme et mention]');p('[Établissement, ville, pays] — [cours ou mémoire pertinent]. [Résultat vérifiable si demandé ; ne pas inventer un classement.]')
    h2('Projet ou expérience');p('[Dates]  |  [Fonction réelle ou nom du projet], [structure]');p('• [Action que j’ai réalisée] avec [outil / méthode] pour [objectif].');p('• [Résultat ou livrable précis]. [En équipe : préciser ma contribution.]')
    h2('Engagement ou activité');p('[Période] — [Rôle] : [action et effet observé, sans exagération].')
    h2('Compétences et langues');p('[Outil] : utilisé pour [travail concret].  •  [Langue] : [niveau réel ; certification, score et date, si disponible].')
    begin(2,'Écris pour une seule formation : un fait vécu, un cours qui te manque, un usage après les études. Si le site demande une réponse dans une case, écris-y le texte au lieu de joindre une lettre. Respecte les règles de l’école sur l’IA.')
    p('[Ville], le [date]\nÀ l’attention de [jury / service indiqué]');p('Objet : candidature à [programme et, si demandé, bourse], rentrée [année]');p('Madame, Monsieur,')
    p('À [lieu / date], j’ai rencontré [situation concrète]. Dans le cadre de [cours / stage / engagement], ma responsabilité était de [action exacte]. [Résultat que je peux expliquer ; difficulté ou limite rencontrée.]')
    p('Cette expérience m’a amené(e) à me poser la question suivante : [question]. J’ai déjà appris à [acquis], mais il me manque [compétence précise]. Dans votre programme, [enseignement, atelier ou méthode dont j’ai vérifié l’existence] me permettrait de [usage concret].')
    p('Après la formation, mon premier objectif serait de [activité réaliste], auprès de [public ou secteur]. [Si le jury le demande : dépense que l’aide rendrait possible, durée et raison ; distinguer faits et projet.]')
    p('Je vous remercie de l’attention portée à ma candidature.\n[Signature / Prénom Nom]')
    note('Relecture : si tu changes le nom de l’école, quel passage devient faux ? Si la réponse est « aucun », reprends le paragraphe sur la formation.')
    begin(3,'Study Plan veut dire « plan d’études ». Prends la liste des vrais cours. Pour chaque période, note ce que tu veux apprendre et le travail qui le montrera. Suis le format de l’école.')
    p('[Titre précis du projet]  |  [Diplôme visé, établissement, rentrée]','Surtitre')
    h2('1. Ma question de départ');p('[Situation observée et raison de m’y intéresser. Fait vérifiable de mon parcours qui me permet de poser cette question.]')
    h2('2. Ce que je vais apprendre');p('[Compétence à acquérir] pour pouvoir [tâche professionnelle]. [Nom du cours ou de l’activité tel qu’il apparaît sur le site de la formation.]')
    h2('3. Comment je compte m’y prendre');table([['Étape','Travail réalisable','Trace attendue'],['[Semestre / période]','[Cours et entraînement précis]','[Exercice / compte rendu]'],['[Semestre / période]','[Projet, stage espéré ou mémoire]','[Livrable réaliste]']])
    h2('4. Après le diplôme');p('[Premier usage du savoir acquis, public concerné, résultat raisonnable. Ne pas annoncer comme acquis un poste ou un partenariat espéré.]')
    h2('Question de faisabilité');p('[Que ferai-je si l’accès aux données / au stage / au terrain n’est pas obtenu ?]')
    begin(4,'Réservé à la thèse : pose une question, puis dis comment tu pourrais y répondre. Apporte cette note à la personne qui pourrait diriger ta recherche. Si son école donne une autre liste, suis-la.')
    h2('[Titre provisoire]');p('Question : [que cherches-tu à comprendre, sur quel terrain ou quels documents, et à quelle période ?].')
    h2('État des travaux');p('[Deux ou trois références réellement lues ; pour chacune, résultat utile et question encore ouverte. Vérifier les références exactes.]')
    h2('Méthode et faisabilité');p('[Données ou corpus accessibles, méthode envisagée, autorisations requises, limites et solution de repli. Ne pas confondre accès espéré et accès autorisé.]')
    h2('Accueil et encadrement');p('[Laboratoire, équipe et correspondance avec ses axes réels]. [Personnes contactées, accord écrit ou discussion en cours]. [Cotutelle ou codirection seulement si applicable.]')
    h2('Calendrier et financement');table([['Période et lieu','Travail prévu','Financement : confirmé / à obtenir'],['[Mois, pays]','[Recherche / collecte]','[Source, durée, justificatif]'],['[Mois, pays]','[Analyse / rédaction]','[Mois non couverts, démarche prévue]']])
    p('Question à poser : [attente du laboratoire, voie de candidature ou règle financière encore incertaine].')
    begin(5,'Choisis UN message : le premier pour poser une question sur Eiffel, la variante pour demander une lettre à l’école. N’envoie pas les deux ensemble. Prends l’adresse sur le site de la formation.')
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
    begin(7,'Une relance est un deuxième message sur la même question. Avant de l’envoyer, vérifie le délai de réponse annoncé, ton compte et les courriels indésirables. Si possible, réponds à ton premier message pour garder le contexte.')
    p('Objet : suivi de [objet du premier message] — [identifiant de dossier si utile]');p('Bonjour [titre / service],')
    p('Je me permets de revenir vers vous au sujet de [question unique], transmise le [date]. Je candidate à [intitulé et session] et la date indiquée dans la notice est le [date, fuseau].')
    p('J’ai vérifié [portail ou rubrique] et j’y vois [statut exact]. Pourriez-vous m’indiquer [action attendue : confirmer la réception / préciser la pièce manquante / m’orienter vers le bon service] ?')
    p('Merci pour votre aide.\n[Prénom Nom, référence si demandée]')
    h2('Variante : confirmation de présentation Eiffel');p('« Pour éviter une double présentation, pourriez-vous me confirmer si mon dossier a été retenu et déposé par votre établissement pour la session [année] ? »')
    note('Ne renvoie pas de documents sensibles en pièces jointes sans demande du destinataire officiel. Une absence de réponse n’est ni un accord ni un refus.')
    begin(8,'Une page de notes pour répéter. N’apprends pas un texte mot à mot. À adapter selon qu’il s’agit d’un entretien pédagogique, d’admission ou de bourse.')
    p('Convocation : [organisme, date, heure, fuseau, langue, lieu ou lien]')
    table([['Question','Mes mots-clés (deux lignes maximum)'],['Pourquoi ce programme ?','[Cours précis + compétence qui me manque]'],['Qu’ai-je fait moi-même ?','[Situation, action personnelle, résultat, limite]'],['Pourquoi cette bourse ?','[Dépense précise, montant documenté, ce qui reste]'],['Quel projet ensuite ?','[Premier usage concret, pour qui et avec quelle méthode]'],['Et en cas de refus ?','[Plan réaliste sans financer le séjour par une somme hypothétique]']])
    h2('Ma répétition');p('Fait que je dois encore vérifier : [source et action].\nQuestion posée par la personne qui m’écoute : [question].\nRéponse trop vague à reprendre : [phrase].')
    h2('Avant le rendez-vous');p('□ Convocation relue     □ Dossier soumis relu     □ Originaux demandés prêts\n□ Test audio si entretien en ligne     □ Budget revu, aides acquises et en attente distinguées')
    BONUS.mkdir(exist_ok=True);d.save(DOCX)

if __name__=='__main__':make()
