"""Tableau de bord XLSX sans macros : pistes datées, pièces et deux budgets."""
from datetime import datetime
import xlsxwriter
from commun import BONUS, XLSX, LIENS

NOUVEAU, FINI = 'Budget incomplet : complète les paramètres et chaque poste applicable.', 'Budget calculé pour la période choisie.'

def make():
    BONUS.mkdir(exist_ok=True);book=xlsxwriter.Workbook(str(XLSX))
    book.set_properties({'title':'Mon dossier France — Suivi et budget','author':'Mon dossier France','comments':'Édition de novembre 2026 ; vérifier chaque appel avant dépôt.'});book.set_calc_mode('auto')
    def fmt(**kw):return book.add_format({'font_name':'Calibri','font_size':12,'font_color':'#183A3B','valign':'vcenter',**kw})
    title=fmt(bold=True,font_size=19,font_color='white',bg_color='#143E40',indent=1)
    sub=fmt(font_size=11,bg_color='#DAEAE4',text_wrap=True,indent=1)
    head=fmt(bold=True,bg_color='#22716A',font_color='white',text_wrap=True,indent=1)
    body=fmt(text_wrap=True);alt=fmt(text_wrap=True,bg_color='#F2F7F4');label=fmt(bold=True,text_wrap=True)
    entry=fmt(bg_color='#FFF1D8',text_wrap=True);num=fmt(bg_color='#FFF1D8',num_format='#,##0.00');rate=fmt(bg_color='#FFF1D8',num_format='#,##0.000');dt=fmt(bg_color='#FFF1D8',num_format='dd/mm/yyyy')
    dates=fmt(num_format='dd/mm/yyyy',bold=True);link=fmt(font_color='#135C6A',underline=True,text_wrap=True)
    calc=fmt(num_format='#,##0.00',bg_color='#E2F1EA');banner=fmt(bold=True,bg_color='#DBEBE5',text_wrap=True,indent=1)
    total=fmt(bold=True,num_format='#,##0.00',bg_color='#143E40',font_color='white');sumlabel=fmt(bold=True,bg_color='#DBEBE5',indent=1,text_wrap=True)
    hint=fmt(italic=True,font_size=11,text_wrap=True,indent=1);bad=fmt(bg_color='#FBE0D4',font_color='#833A1F');good=fmt(bg_color='#D8EEDB',font_color='#23583D')
    tabs={n:book.add_worksheet(n) for n in ('Mode d’emploi','Pistes','Pièces','Budget','Exemple budget')}
    def setup(s,last,t,st):
        s.hide_gridlines(2);s.set_zoom(90);s.set_default_row(23);s.merge_range(0,0,0,last,t,title);s.set_row(0,40)
        s.merge_range(1,0,1,last,st,sub);s.set_row(1,43);s.set_landscape();s.fit_to_pages(1,0);s.set_margins(.23,.23,.4,.45)
        s.set_footer('&LMon dossier France — Édition novembre 2026&RPage &P / &N');s.set_tab_color('#22716A')
    def dropdown(s,where,options):s.data_validation(where,{'validate':'list','source':options,'error_title':'Valeur non prévue','error_message':'Choisis une option dans la liste.'})
    def display_source(s,r,c,key):s.write_url(r,c,LIENS[key][1],link,string=LIENS[key][0])
    mode=tabs['Mode d’emploi'];setup(mode,3,'Mon dossier France  /  Tableau de bord','Commence ici. Fais une copie du tableur pour chaque rentrée. Tu peux travailler hors ligne ; une connexion est nécessaire pour vérifier les appels.')
    mode.set_column('A:A',24);mode.set_column('B:D',23)
    for row,(tab,desc) in enumerate([('Pistes','Exemples datés pour la rentrée 2027. Ta date de dépôt et la date du porteur sont distinctes. Filtre ou ajoute une ligne ; note l’action suivante et la preuve de dépôt.'),('Pièces','Une ligne par pièce et par programme. Mets à jour la personne responsable et la date promise. N’enregistre pas tes mots de passe ou un numéro de passeport dans ce tableur.'),('Budget','En jaune : à saisir. Indique une période, tes fonds disponibles et tes seules aides confirmées. Zéro = coût réellement nul ; vide = coût inconnu. Les résultats apparaissent quand le budget est complet.'),('Exemple budget','Cas fictif du guide en XOF. Compare l’argent à avancer et ce qui reste au final. Les montants ne sont ni des tarifs ni les prestations d’une bourse réelle.')],3):
        mode.write_url(row,0,f"internal:'{tab}'!A1",link,string=tab+' →');mode.merge_range(row,1,row,3,desc,body);mode.set_row(row,63)
    mode.merge_range('A9:D9','Si la date est dépassée, cherche la nouvelle session. N’ajoute pas un an par défaut.',banner)
    mode.merge_range('A11:D12','Sur mobile : fais défiler vers la droite pour les conditions, le lien officiel et les preuves. Dans « Pistes », les colonnes utiles à l’action viennent en premier. Les couleurs sont des repères ; les statuts sont aussi écrits.',sub)
    mode.merge_range('A14:D16','Les frais officiels éventuels ne sont pas des frais d’agence. Une admission, une bourse et un visa sont trois décisions distinctes. Pour une autre monnaie que le XOF, modifie la devise et le taux dans chaque budget.',body)
    mode.print_area('A1:D16')

    s=tabs['Pistes'];setup(s,12,'Pistes  /  Une ligne par démarche','Exemples de la campagne 2027, pas une liste d’appels toujours ouverts. Date vide = à vérifier, jamais « sans limite ». Ouvre le lien officiel avant toute dépense. Les cellules sont modifiables.')
    hs=['Piste ou session','Prochaine action','Ma limite','Heure / précision','État','Démarche','Qui reçoit le dossier ?','Public / point à vérifier','Financement / frais','Limite du porteur (pas la tienne)','Source officielle →','Mon contrôle le','Preuve / note privée']
    for i,(h,width) in enumerate(zip(hs,[27,39,15,25,18,18,39,53,52,18,35,17,37])):s.set_column(i,i,width);s.write(3,i,h,head)
    s.set_row(3,43);s.freeze_panes(4,1);s.autofilter('A4:M44');s.repeat_rows(3,3)
    rows=[('Eiffel · master Paris-Saclay','Contacter le responsable AVANT la date indiquée.',(2026,11,26),'Date interne ; contacter avant.','Bourse','Responsable du master ; Paris-Saclay présente les dossiers retenus.','Volet master. Ne pas réutiliser cette date pour le doctorat ou une autre école. Vérifier candidature d’admission séparée.','Allocation et prestations sous conditions ; pas de couverture générale des frais de formation.',(2027,1,6),'saclay'),
          ('Émile Boutmy · Bachelor international','Demander la bourse dans le dossier, puis valider.',(2027,1,13),'Voie internationale ; vérifier l’heure.','Bourse','Portail Sciences Po, informations financières.','Bachelor éligible ; situation familiale et fiscale, diplôme et voie d’admission à vérifier.','Exonération des droits, pas de versement pour la vie courante. Frais de dossier à vérifier.',None,'boutmy'),
          ('Émile Boutmy · master','Compléter aussi la rubrique financière avant validation.',(2026,11,29),'23 h 59, Paris (2e commission).','Bourse','Portail d’admission internationale Sciences Po.','Primo-arrivant ; vérifier nationalité, foyer fiscal, master et exclusions.','18 500 € de droits exonérés par an selon la fiche. Demander Boutmy ne dispense pas des frais de dossier.',None,'boutmy'),
          ('Mastercard · Sciences Po · vague 1','Vérifier mon université/passerelle/statut, ma moyenne et lancer les deux dossiers.',(2026,11,23),'Vague 1 ; vérifier l’heure.','Bourse','Plateforme bourse ET dossier d’admission en master à créer en parallèle.','Critères africains et académiques ; licence concernée ; autres exclusions dans la notice.','Scolarité et vie des lauréats ; exonération de candidature si confirmée, pas automatiquement.',None,'carte'),
          ('Mastercard · Sciences Po · vague 2','Choisir UNE vague ; préparer les pièces d’admission sans attendre.',(2026,12,14),'Vague 2 ; vérifier l’heure.','Bourse','Même parcours : plateforme bourse ET portail d’admission.','Le message d’éligibilité précise quand valider le dossier de master.','L’éligibilité et la dispense des frais ne valent pas attribution de la bourse.',None,'carte'),
          ('Erasmus Mundus · Europhotonics','Faire envoyer les deux références et valider le dossier M1.',(2027,2,4),'17 h 00, Paris.','Bourse','Portail du consortium ; un dossier admission + bourse.','Études scientifiques, preuve d’anglais ; premier semestre à Marseille puis mobilité européenne.','Bourse UE sur sélection ; une admission seule ne confirme pas l’allocation.',None,'euro'),
          ('Bénin · Études en France classique','Vérifier le paiement ou la dispense ET la première soumission.',(2026,12,1),'Prolongation publiée, étapes 4 et 5.','Admission','Espace personnel Études en France ; Campus France Bénin.','Résident du Bénin et formation concernée, rentrée 2027. Pas un délai pour toutes les bourses.','70 000 F CFA si dus. Vérifier « Cas particuliers » avant paiement.',None,'bj')]
    for i,row in enumerate(rows,4):
        name,action,day,time,kind,route,public,benefit,host,src=row
        s.write(i,0,name,label);s.write(i,1,action,entry);s.write_datetime(i,2,datetime(*day),dates);s.write(i,3,time,body);s.write(i,4,'À vérifier',entry)
        for col,val in enumerate([kind,route,public,benefit],5):s.write(i,col,val,alt if i%2 else body)
        if host:s.write_datetime(i,9,datetime(*host),dates)
        display_source(s,i,10,src);s.write_blank(i,11,None,dt);s.set_row(i,68)
    for i in range(4+len(rows),44):
        for j in (1,2,4,9,11):s.write_blank(i,j,None,dt if j in (2,9,11) else entry)
    dropdown(s,'E5:E44',['À vérifier','À préparer','En cours','Déposé','Retenu','Non retenu','Écarté','Clos']);dropdown(s,'F5:F44',['Bourse','Admission','Visa']);s.print_area('A1:M12')

    s=tabs['Pièces'];setup(s,7,'Pièces  /  Ce qu’il reste à obtenir','Exemples à adapter : une pièce citée ici n’est pas exigée pour toutes les formations. Copie d’abord la liste de TON appel. Les dates ci-dessous sont tes propres rappels.')
    hs=['Pièce / preuve','Piste','État','Qui s’en charge ?','Format / mode de dépôt','À obtenir avant','Reçu / transmis le','Preuve ou action suivante']
    for i,(h,width) in enumerate(zip(hs,[28,26,19,26,44,18,19,39])):s.set_column(i,i,width);s.write(3,i,h,head)
    s.set_row(3,38);s.freeze_panes(4,1);s.autofilter('A4:H44');s.repeat_rows(3,3)
    pieces=[
        ('Identité / passeport','[Mon programme]','Moi / DEI','Pièce acceptée à ce stade ; passeport pour voyager.','Comparer noms, dates, page photo et validité.'),
        ('Bac : attestation et relevé','Bénin · EEF','Moi / Office du bac','Pièces distinctes ; choisir les actes demandés pour le niveau visé.','Conserver code de suivi et bordereau de retrait.'),
        ('Bulletins du secondaire','Bénin · EEF','Lycée','Années requises selon le niveau visé.','Vérifier que les bulletins après 2019 sont authentifiables sur Educmaster.'),
        ('Relevés universitaires','[Mon programme]','Scolarité','Semestres complets ; recto-verso si le barème est au dos.','Contrôler filière, session et légende des notes.'),
        ('Diplôme / preuve provisoire','[Mon programme]','Scolarité','Attestation de succès ou d’inscription seulement si admise pour cette étape.','Noter la date à laquelle le diplôme final sera exigé.'),
        ('Traduction / copie certifiée','[Si exigée]','Traducteur / guichet reconnu','Reprendre la langue, l’agrément ou le type de copie exacts dans la notice.','Ne pas confondre copie, traduction et légalisation de l’acte.'),
        ('Casier judiciaire B3','[Seulement si prescrit]','Moi / Service public du Bénin','Vérifier émetteur, ancienneté et stade demandé ; sinon Sans objet.','Planifier le B3 béninois en tenant compte de ses trois mois de validité.'),
        ('Fiche médicale','[Seulement si prescrite]','Médecin ou centre admis','Modèle de la campagne, selon la convocation ; sinon Sans objet.','Noter le statut, jamais un diagnostic ni le détail médical dans ce classeur.'),
        ('Test ou attestation de langue','[Mon programme]','Moi / centre habilité','Résultat du test admis ou preuve d’une dispense.','Vérifier langue, score et date de réception des résultats.'),
        ('Stage / certificat de compétence','[Si pertinent et admis]','Structure émettrice','Compétence, dates et preuve vérifiable ; pas de pièce hors consigne.','Comparer les dates et le rôle décrits sur le CV.'),
        ('CV, motivation, Study Plan','[Si demandés]','Moi','Formulaire, fichiers, langue et limites de la notice.','Retirer les crochets et les consignes du modèle Word.'),
        ('Attestation de classement','Eiffel · Paris-Saclay','Scolarité','Attestation officielle, années demandées dans l’appel.','Demander la disponibilité de la pièce.'),
        ('Preuve de licence en cours','Mastercard · Sciences Po','Scolarité','Selon voie : établissement référencé / passerelle / statut HCR.','Vérifier la liste et le justificatif.'),
        ('Recommandation 1 / 2','Europhotonics','Référent 1','Envoi direct, adresse institutionnelle.','Obtenir son accord avant la demande.'),
        ('Recommandation 2 / 2','Europhotonics','Référent 2','Envoi direct ; un référent au moins doit être enseignant connaissant ton parcours.','Vérifier le statut dans le portail.'),
        ('Lettre de préadmission','[Selon appel et étape]','Admissions de l’école','Lettre officielle, conditions et délai d’acceptation.','L’accusé de candidature n’est pas une admission.'),
        ('API après choix définitif','Bénin · EEF classique','Moi / Campus France Bénin','Accord préalable d’inscription signé et tamponné avant le visa.','Suivre les instructions de l’espace local.'),
        ('Accusé de dépôt','[Mon programme]','Moi','PDF ou courriel de confirmation transmis par le portail.','Noter date et identifiant, conserver une copie.')]
    for i,(a,b,who,detail,nxt) in enumerate(pieces,4):
        for j,v in enumerate((a,b,'À vérifier',who,detail,'','',nxt)):
            if v:s.write(i,j,v,entry if j==2 else body)
        s.set_row(i,55)
    for i in range(4,44):
        for j in (5,6):s.write_blank(i,j,None,dt)
    dropdown(s,'C5:C44',['À vérifier','À demander','Demandé','Reçu','À corriger','Transmis','Sans objet']);s.print_area(0,0,3+len(pieces),7)

    def budget(name,demo):
        s=tabs[name];setup(s,9,'Exemple budget  /  Simulation fictive' if demo else 'Budget  /  Ta période, ta monnaie','Exemple pédagogique, pas des tarifs réels.' if demo else 'En jaune : tes données. Utilise une seule période. Un coût inconnu doit rester vide ; mets 0 seulement si le poste ne te coûte rien.')
        for i,width in enumerate([30,14,18,9,19,19,21,21,45,19]):s.set_column(i,i,width)
        for r,text in enumerate(['Période (début et fin)','Monnaie locale (code)','1 EUR en monnaie locale','Fonds disponibles au départ','Aides en espèces à recevoir'],4):s.merge_range(f'A{r}:B{r}',text,label)
        s.merge_range('C4:J4','Du dépôt au premier versement — à dater',entry);s.write('C5','XOF',entry);s.write_number('C6',655.957,rate)
        if demo:s.write_number('C7',100000,num);s.write_number('C8',80000,num)
        else:s.write_blank('C7',None,num);s.write_blank('C8',None,num)
        for r,text in enumerate(['Ex. XOF au Bénin. Si tu changes de monnaie, ajuste aussi le taux ci-dessous.','Taux de conversion (hors frais). Par défaut, 1 euro = 655,957 francs CFA BCEAO.','En monnaie locale : argent mobilisable maintenant. N’y inclus pas de remboursement futur.','En monnaie locale : seulement les aides confirmées pour cette période, non comptées ailleurs. Zéro si aucune.'],5):s.merge_range(f'D{r}:J{r}',text,hint)
        s.merge_range('A10:J10','',banner)
        headers=['Poste de dépense','Monnaie','Prix par unité','Qté','Pris en charge sans avance¹','Remboursé après avance¹','À décaisser (local)','Net après remb. (local)','Devis / preuve écrite / hypothèse','Contrôle']
        for j,t in enumerate(headers):s.write(10,j,t,head)
        s.set_row(10,44);s.freeze_panes(11,1)
        postes=['Frais de procédure (si dus)','Frais de candidature école','Traductions et justificatifs','Test de langue','Visa + prestataire éventuel','Voyage et trajet d’arrivée','Droits et frais de scolarité','Caution à avancer','Logement pour la période','Vie courante et transport local','Assurance / autres frais requis','Frais bancaires / transferts']
        for r in range(12,27):
            mandatory=r-12<len(postes);i=r-1
            if mandatory:s.write(i,0,postes[r-12],body);s.write(i,1,'Locale',entry);s.write_number(i,3,1,num)
            else:
                for j in (0,1,3):s.write_blank(i,j,None,entry)
            val={17:300000,18:400000,20:90000,21:60000}.get(r,0) if demo and mandatory else None
            direct=400000 if demo and r==18 else 0;remb=200000 if demo and r==17 else 0
            for j,amt in ((2,val),(4,direct or None),(5,remb or None)):
                if amt is not None:s.write_number(i,j,amt,num)
                else:s.write_blank(i,j,None,num)
            if demo and r in (17,18,20,21):s.write(i,8,{17:'Hypothèse : remboursement de 200 000 après l’arrivée.',18:'Hypothèse : l’école ne facture pas cette somme au candidat.',20:'Hypothèse : 90 000 de logement.',21:'Hypothèse : 60 000 de vie courante.'}[r],body);s.set_row(i,40)
            # Vérifier le type avant de comparer les montants pour ne pas produire d’erreur lors d’une saisie incomplète.
            check=(f'=IF(A{r}="",IF(COUNTA(B{r}:F{r})=0,"","Sans nom"),IF(OR(B{r}="",C{r}="",D{r}=""),"À chiffrer",'
                   f'IF(OR(AND(B{r}<>"Locale",B{r}<>"EUR"),COUNT(C{r}:D{r})<>2,COUNT(E{r}:F{r})<>COUNTA(E{r}:F{r})),"À corriger",'
                   f'IF(OR(MIN(C{r}:F{r})<0,D{r}<=0,SUM(E{r}:F{r})>C{r}*D{r}),"À corriger","OK"))))')
            status=('OK' if demo else 'À chiffrer') if mandatory else ''
            s.write_formula(f'J{r}',check,body,status)
            for col,minus,cache in [('G',f'SUM(E{r})',None if val is None else val-direct),('H',f'SUM(E{r}:F{r})',None if val is None else val-direct-remb)]:
                form=f'=IF(OR(J{r}<>"OK",NOT(ISNUMBER($C$6)),$C$6<=0),"",ROUND((C{r}*D{r}-{minus})*IF(B{r}="EUR",$C$6,1),2))'
                s.write_formula(f'{col}{r}',form,calc,'' if cache is None else cache)
        dropdown(s,'B12:B26',['Locale','EUR'])
        for zone in ('C12:C26','E12:F26','C7:C8'):s.data_validation(zone,{'validate':'decimal','criteria':'>=','value':0})
        for zone in ('D12:D26','C6'):s.data_validation(zone,{'validate':'decimal','criteria':'>','value':0})
        st=(f'=IF(OR(C4="",C5="",NOT(ISNUMBER(C6)),C6<=0,COUNT(C7:C8)<>2,MIN(C7:C8)<0,'
            f'COUNTIF(J12:J26,"À*")+COUNTIF(J12:J26,"Sans nom")>0,COUNTIF(J12:J26,"OK")=0),"{NOUVEAU}","{FINI}")')
        s.write_formula('A10',st,banner,FINI if demo else NOUVEAU)
        s.conditional_format('J12:J26',{'type':'text','criteria':'containing','value':'À','format':bad});s.conditional_format('J12:J26',{'type':'cell','criteria':'==','value':'"OK"','format':good})
        s.merge_range('A28:F28','Totaux de la période, en monnaie locale',sumlabel)
        for col,val in [('G',450000),('H',250000)]:s.write_formula(f'{col}28',f'=IF($A$10="{FINI}",SUM({col}12:{col}26),"")',total,val if demo else '')
        for r,t,fo,val in [(29,'À trouver avant les versements (si tout est payé d’abord)','G28-$C$7',350000),(30,'À trouver au final, après remboursement et aides','H28-$C$7-$C$8',70000)]:
            s.merge_range(f'A{r}:F{r}',t,sumlabel);s.merge_range(f'G{r}:H{r}','',total);s.write_formula(f'G{r}',f'=IF($A$10="{FINI}",MAX(0,{fo}),"")',total,val if demo else '');s.merge_range(f'I{r}:J{r}','En monnaie locale (C5)',hint);s.set_row(r-1,29)
        s.merge_range('A32:J32','¹ En E et F, saisis un TOTAL pour la ligne, dans la monnaie de B, pas un montant unitaire. Laisser vide = aucune couverture confirmée. Une même somme ne peut pas être directe et remboursée.',sub)
        s.merge_range('A33:J33','Le calcul « avant » suppose que toutes ces dépenses précèdent les entrées. Pour un autre calendrier, fais une copie par période. Une exonération n’est pas de l’argent reçu. Un remboursement de caution ne se compte que si son retour tombe dans la période étudiée.',sub)
        s.set_row(31,34);s.set_row(32,41);s.write_url('A35',LIENS['change'][1],link,string='BCEAO · vérifier le taux EUR/XOF');s.print_area('A1:J35')
    budget('Budget',False);budget('Exemple budget',True);book.close()

if __name__=='__main__':make()
