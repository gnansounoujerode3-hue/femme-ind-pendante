"""Génère le guide PDF A4 à partir du contenu et de la mise en page ci-dessous."""
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Paragraph

OUT = Path(__file__).with_name('expertise-comptable-francaise.pdf')
W, H = A4
M = 49
CW = W - 2 * M
INK = '#231C31'
PLUM = '#362747'
VIOLET = '#643B80'
MUTED = '#5F526A'
PAPER = '#FAF7F1'
LILAC = '#EDE3F5'
PEACH = '#F4DACA'
LINE = '#D7CADD'
WHITE = '#FFFFFF'

SOURCES = [
    ('01', 'Obligations comptables en micro-entreprise', 'Service Public Entreprendre', 'https://entreprendre.service-public.gouv.fr/vosdroits/F23266'),
    ('02', 'Obligations comptables d’une société commerciale', 'Service Public Entreprendre', 'https://entreprendre.service-public.gouv.fr/vosdroits/F37169'),
    ('03', 'Mentions obligatoires sur une facture', 'Service Public Entreprendre', 'https://entreprendre.service-public.gouv.fr/vosdroits/F31808'),
    ('04', 'Se mettre en conformité avec la facturation électronique', 'Service Public Entreprendre', 'https://entreprendre.service-public.gouv.fr/vosdroits/F39785'),
    ('05', 'Professionnels qui peuvent aider à gérer une entreprise', 'Service Public Entreprendre', 'https://entreprendre.service-public.gouv.fr/vosdroits/F31447'),
    ('06', 'Honoraires, lettre de mission et accès à l’annuaire', 'Ordre des experts-comptables', 'https://www.experts-comptables.fr/faq'),
    ('07', 'Déclarer le chiffre d’affaires en micro-entreprise', 'Service Public Entreprendre', 'https://entreprendre.service-public.gouv.fr/vosdroits/F23257'),
]
SECTIONS = [
    ('profil', 'Identifier tes obligations'),
    ('routine', 'Installer une routine comptable'),
    ('factures', 'Préparer la facturation électronique'),
    ('cabinet', 'Choisir un cabinet et comparer les offres'),
    ('plan', 'Fiche à remplir : ton premier mois'),
    ('sources', 'Sources officielles'),
]

c = canvas.Canvas(str(OUT), pagesize=A4, invariant=1, lang='fr-FR')
c.setTitle('L’expertise comptable française — Guide pratique')
c.setAuthor('Femme indépendante')
c.setSubject('Guide pratique pour indépendantes et dirigeantes de petites entreprises en France')


def box(x, y, w, h, fill, radius=0):
    c.setFillColor(HexColor(fill))
    if radius:
        c.roundRect(x, H-y-h, w, h, radius, fill=1, stroke=0)
    else:
        c.rect(x, H-y-h, w, h, fill=1, stroke=0)


def rule(x, y, x2, color=LINE, weight=.65):
    c.setStrokeColor(HexColor(color))
    c.setLineWidth(weight)
    c.line(x, H-y, x2, H-y)


def text(s, x, y, size=11, font='Helvetica', color=INK, *, right=False):
    if right:
        x -= stringWidth(s, font, size)
    c.setFont(font, size)
    c.setFillColor(HexColor(color))
    c.drawString(x, H-y, s)


def para(s, x, y, w=CW, size=12, lead=17.5, color=INK):
    p = Paragraph(s, ParagraphStyle('body', fontName='Helvetica', fontSize=size,
                                   leading=lead, textColor=HexColor(color)))
    _, h = p.wrap(w, H)
    assert y+h < H-59, (s, y+h)
    p.drawOn(c, x, H-y-h)
    return y+h


def label(s, x, y, color=VIOLET):
    c.saveState()
    c.setFillColor(HexColor(color))
    t = c.beginText(x, H-y)
    t.setFont('Helvetica-Bold', 9)
    t.setCharSpace(1.35)
    t.textLine(s)
    c.drawText(t)
    c.restoreState()


def header(i, tag, title, intro):
    key, outline = SECTIONS[i-1]
    c.bookmarkPage(key)
    c.addOutlineEntry(outline, key)
    box(0, 0, W, H, PAPER)
    label('FEMME INDÉPENDANTE', M, 48)
    text('GUIDE PRATIQUE  /  FRANCE', W-M, 48, 9, 'Helvetica-Bold', MUTED, right=True)
    rule(M, 64, W-M)
    label(f'{i:02d}  /  {tag}', M, 102)
    text(title, M, 152, 37, 'Times-Bold')
    return para(intro, M, 179, CW-16, 13, 19, MUTED) + 24


def footer(i, refs=()):
    if refs:
        label('SOURCES', M, 759)
        for j, n in enumerate(refs):
            x = M+71+j*35
            text(f'[{n}]', x, 759, 10, 'Helvetica-Bold', VIOLET)
            c.linkRect('', 'ref'+n, (x-2, H-765, x+27, H-746), relative=0, thickness=0)
    rule(M, 778, W-M)
    text('L’EXPERTISE COMPTABLE FRANÇAISE', M, 802, 8, 'Helvetica-Bold', MUTED)
    text(f'{i+1:02d} / 07', W-M, 802, 9, 'Helvetica-Bold', VIOLET, right=True)
    c.showPage()


def card(y, tag, title, body, fill=LILAC):
    box(M, y, CW, 109, fill, 10)
    label(tag, M+16, y+23)
    text(title, M+16, y+45, 17, 'Times-Bold')
    assert para(body, M+16, y+54, CW-32, 11.5, 15.5) <= y+103
    return y+120


def item(y, n, title, body):
    text(n, M, y+15, 11, 'Helvetica-Bold', VIOLET)
    text(title, M+35, y+16, 17, 'Times-Bold')
    end = para(body, M+35, y+27, CW-35, 11.5, 16)
    rule(M, end+10, W-M)
    return end+23


def highlight(y, title, body, fill=LILAC):
    p = Paragraph(body, ParagraphStyle('measure', fontName='Helvetica', fontSize=11.5, leading=16))
    _, h = p.wrap(CW-36, H)
    box(M, y, CW, h+50, fill, 9)
    text(title, M+18, y+23, 14, 'Helvetica-Bold')
    para(body, M+18, y+33, CW-36, 11.5, 16)
    return y+h+64


def cover():
    c.bookmarkPage('cover')
    c.addOutlineEntry('Couverture', 'cover')
    box(0, 0, W, H, PAPER)
    box(0, 0, W, 455, PLUM)
    label('FEMME INDÉPENDANTE', M, 52, PEACH)
    rule(M, 69, W-M, '#786786')
    label('GUIDE PRATIQUE  /  ÉDITION NOVEMBRE 2026', M, 116, '#EADCF1')
    text('L’expertise', M, 192, 61, 'Times-Bold', WHITE)
    text('comptable', M, 256, 61, 'Times-Bold', WHITE)
    text('française', M, 320, 61, 'Times-Italic', PEACH)
    para('Tes obligations, ta routine et les bons réflexes<br/>pour travailler avec un cabinet.', M, 359, 348, 15, 21, WHITE)

    # Illustration vectorielle : un petit registre avec ses lignes pointées.
    box(429, 279, 107, 119, '#50405D', 13)
    box(413, 265, 107, 119, PEACH, 13)
    label('SUIVI', 429, 292)
    for y in (308, 328, 348):
        c.setStrokeColor(HexColor(VIOLET))
        c.setLineWidth(1.2)
        path = c.beginPath()
        path.moveTo(430, H-y)
        path.lineTo(434, H-y-4)
        path.lineTo(440, H-y+4)
        c.drawPath(path)
        rule(450, y, 503, '#9B757C', 1)

    label('LE SOMMAIRE', M, 503)
    for i, (key, name) in enumerate(SECTIONS, 1):
        y = 535 + (i-1)*36
        text(f'{i:02d}', M, y, 10, 'Helvetica-Bold', VIOLET)
        text(name, M+31, y, 13)
        text(f'{i+1:02d}', W-M, y, 10, 'Helvetica-Bold', MUTED, right=True)
        rule(M, y+11, W-M)
        c.linkRect('', key, (M, H-y-10, W-M, H-y+18), relative=0, thickness=0)
    text('Pour les indépendantes et dirigeantes de petites entreprises établies en France.',
         M, 781, 10, 'Helvetica', MUTED)
    c.showPage()


cover()

y = header(1, 'TES OBLIGATIONS', 'Repère ton régime',
           'Commence par noter trois informations : ta forme juridique, ton régime fiscal et ta situation au regard de la TVA. L’une ne suffit pas à déduire les deux autres.')
y = card(y, 'PROFIL 01', 'Micro-entreprise',
         'Tiens un livre des recettes encaissées et, selon ton activité (vente de marchandises ou hébergement notamment), un registre des achats. Déclare le chiffre d’affaires encaissé à l’Urssaf chaque mois ou trimestre, même s’il est nul.')
y = card(y, 'PROFIL 02', 'Entreprise individuelle hors micro',
         'Vérifie les obligations propres à ton régime fiscal. Le réel en BIC (bénéfices industriels et commerciaux) et la déclaration contrôlée en BNC (bénéfices non commerciaux) n’impliquent pas les mêmes registres ni les mêmes déclarations.', WHITE)
y = card(y, 'PROFIL 03', 'Société commerciale : SASU, EURL, SAS, SARL…',
         'En règle générale, tiens une comptabilité, établis les comptes annuels et organise leur approbation et leur dépôt selon les règles applicables à ta société. Des simplifications existent selon le régime et la taille.')
highlight(y+4, 'Faut-il une experte ou un expert-comptable ?',
          'Non, tu peux tenir ta comptabilité en interne. Si tu en confies la tenue à un prestataire, vérifie son inscription à l’Ordre. Le commissaire aux comptes exerce une autre mission : certifier les comptes lorsqu’il est nommé.', PEACH)
footer(1, ('01', '02', '05', '06', '07'))

y = header(2, 'TA ROUTINE', 'Suis tes encaissements',
           'Bloque un créneau chaque semaine. Le but : savoir ce qui est facturé, ce qui est encaissé et quelles échéances approchent.')
y = item(y, '01', 'Facture et classe',
         'Attribue aux factures un numéro unique dans une séquence chronologique et continue. Vérifie les mentions selon ta situation : identité des parties, prestation, prix, TVA ou mention d’exonération applicable et conditions de règlement.')
y = item(y, '02', 'Rapproche tes paiements des justificatifs',
         'Compare relevés et pièces : factures, avoirs, notes et justificatifs d’achat. Note les impayés et la date de relance. En micro, note dans ton livre la date, l’origine, le montant, le mode de règlement et la référence du justificatif de chaque recette, sauf exceptions prévues.')
y = item(y, '03', 'Vérifie les échéances et archive',
         'Mets au calendrier Urssaf, TVA si applicable et obligations annuelles selon ton régime. Prévois le montant des charges à venir. Conserve les pièces comptables et les registres concernés pendant dix ans selon les règles applicables.')
y = highlight(y+3, 'Exemple : une facture n’est pas un encaissement',
              'Une graphiste en micro, en franchise de TVA, facture <b>600 € le 28 janvier</b> et reçoit le virement <b>le 4 février</b>. Elle inscrit les 600 € dans son livre au 4 février. Si elle déclare mensuellement, cette somme relève de février, pas de janvier.')
footer(2, ('01', '02', '03', '07'))

y = header(3, 'LA RÉFORME', 'Facturation électronique',
           'Si ton entreprise est établie en France et assujettie à la TVA, la réforme te concerne aussi en franchise en base de TVA.')
y = card(y, 'DEPUIS LE 1ER SEPTEMBRE 2026', 'Réception des factures',
         'Ton entreprise doit pouvoir recevoir les factures électroniques de ses fournisseurs via une plateforme agréée, même si elle ne facture pas elle-même la TVA.')
y = card(y, 'À PARTIR DU 1ER SEPTEMBRE 2027', 'Émission et transmission de données',
         'Les PME et micro-entreprises émettent leurs factures électroniques pour les opérations concernées entre assujettis établis en France. Pour certaines ventes à des particuliers ou à l’étranger, elles transmettent des données (e-reporting).', WHITE)
y = item(y+3, '→', 'Ce que tu peux vérifier dès maintenant',
         'Choisis une plateforme sur la liste officielle, ou vérifie que ton outil de facturation est relié à l’une d’elles. Identifie tes clients : professionnels en France, particuliers, clients à l’étranger. Vérifie aussi qui enverra les données si tu travailles avec un cabinet.')
highlight(y+2, 'Un PDF envoyé par courriel ne suffit pas',
          'La facture électronique au sens de la réforme contient des données structurées et transite par une plateforme agréée.', PEACH)
footer(3, ('04',))

y = header(4, 'TON CABINET', 'Choisis ton cabinet',
           'Une consultation ponctuelle peut suffire pour une question de régime ou de TVA. Un suivi régulier peut être utile si tu embauches, passes en société ou vends à l’étranger.')
y = item(y, '01', 'Vérifie l’inscription et l’expérience',
         'Consulte l’annuaire de l’Ordre des experts-comptables. Demande si le cabinet accompagne déjà des entreprises de ton secteur, de ta taille et avec ton régime fiscal.')
y = item(y, '02', 'Compare les offres à périmètre égal',
         'Demande qui tient ou révise la comptabilité, prépare les comptes, déclare la TVA, gère la paie ou t’aide sur la facturation électronique. Compare le coût annuel, les frais de logiciel ou de démarrage, et le tarif des demandes ponctuelles.')
y = item(y, '03', 'Lis la lettre de mission avant de signer',
         'Vérifie les prestations incluses et exclues, les documents que tu dois fournir, les délais, les honoraires, leur révision et les conditions de résiliation. Demande comment récupérer tes pièces et tes données si tu changes de cabinet.')
highlight(y+3, 'À préparer pour le premier rendez-vous',
          'Ton SIREN si tu es déjà immatriculée, ton régime si tu le connais, ton chiffre d’affaires estimé, le volume de factures, le type de clientèle et tes deux questions prioritaires. Demande un canal sécurisé avant d’envoyer des pièces sensibles.')
footer(4, ('05', '06'))

y = header(5, 'FICHE D’ACTION', 'Ton premier mois',
           'Imprime cette page ou reporte-la dans ton agenda. Si une case reste floue, transforme-la en question pour ton premier rendez-vous.')
for fields in [
    (('Forme juridique', 0), ('Régime fiscal', 1)),
    (('Situation TVA', 0), ('Prochaine échéance + date', 1)),
]:
    for title, j in fields:
        x = M+j*(CW/2+8)
        label(title.upper(), x, y+10)
        rule(x, y+39, x+CW/2-8, MUTED)
    y += 61
for week, task in [
    ('S1', 'Je vérifie mon régime, mes registres et mes échéances.'),
    ('S2', 'Je rassemble mes pièces et je vérifie ma numérotation.'),
    ('S3', 'Je rapproche mes encaissements et je vérifie ma plateforme.'),
    ('S4', 'Je décide : gestion interne, rendez-vous ponctuel ou suivi régulier.'),
]:
    c.setStrokeColor(HexColor(VIOLET))
    c.setLineWidth(1)
    c.roundRect(M, H-y-19, 14, 14, 2, fill=0, stroke=1)
    text(week, M+25, y+16, 10, 'Helvetica-Bold', VIOLET)
    para(task, M+53, y+3, CW-53, 11.5, 16)
    rule(M, y+29, W-M)
    y += 44
for heading in ('MA QUESTION PRIORITAIRE', 'MA PROCHAINE ACTION ET SA DATE'):
    label(heading, M, y+13)
    rule(M, y+41, W-M, MUTED)
    rule(M, y+64, W-M, MUTED)
    y += 82
footer(5)

y = header(6, 'À GARDER SOUS LA MAIN', 'Sources officielles',
           'Ces liens sont cliquables. Consulte la version en vigueur avant une déclaration, un choix de régime ou une signature.')
for n, title, org, url in SOURCES:
    c.bookmarkHorizontalAbsolute('ref'+n, H-y+10)
    text(n, M, y+16, 10, 'Helvetica-Bold', VIOLET)
    text(title, M+33, y+16, 16, 'Times-Bold')
    text(org, M+33, y+35, 10, 'Helvetica', MUTED)
    text('Ouvrir', W-M, y+35, 10, 'Helvetica-Bold', VIOLET, right=True)
    c.linkURL(url, (M, H-y-42, W-M, H-y+2), relative=0, thickness=0)
    rule(M, y+46, W-M)
    y += 57
highlight(y+2, 'Le périmètre du guide',
          'Repères généraux pour une petite activité établie en France, vérifiés le 19 novembre 2026. Si ton entreprise est établie hors de France, le fait d’avoir des clients français ne suffit pas à te placer sous les mêmes règles. Fais vérifier ton cas : ce guide ne remplace pas un conseil personnalisé.', PEACH)
footer(6)

c.save()
