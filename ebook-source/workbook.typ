#let data = json("ebook_data.json")
#let cfg = data.config
#let wb = data.workbook

#let c_paper      = rgb("#FAF7F2")
#let c_paper_alt  = rgb("#F2ECE1")
#let c_paper_sage = rgb("#EBF2EE")
#let c_paper_clay = rgb("#F9ECE6")
#let c_ink        = rgb("#12201C")
#let c_ink2       = rgb("#46544F")
#let c_muted      = rgb("#7A857E")
#let c_emerald    = rgb("#0B3B31")
#let c_deep       = rgb("#07241D")
#let c_gold       = rgb("#C5881E")
#let c_gold_hi    = rgb("#E9AF43")
#let c_gold_ink   = rgb("#7A4E04")
#let c_clay       = rgb("#B8532A")
#let c_clay_ink   = rgb("#843212")
#let c_rule       = rgb("#DDD5C7")

#let checkbox(checked: true, accent: c_emerald) = box(
  width: 9pt, height: 9pt, radius: 1.5pt,
  fill: if checked { accent } else { c_paper },
  stroke: 0.8pt + accent,
  baseline: 1.5pt,
  align(center + horizon)[
    #if checked {
      text(font: "Source Sans Pro", size: 7pt, weight: "bold", fill: c_paper)[✓]
    }
  ]
)

#let wb_masthead(kicker, title, page_num) = {
  box(
    width: 100%,
    fill: c_deep,
    radius: 3pt,
    inset: (x: 15pt, y: 12pt),
    stroke: (bottom: 2.2pt + c_gold),
  )[
    #grid(
      columns: (1fr, auto),
      column-gutter: 12pt,
      align: horizon,
      block[
        #text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_gold_hi, tracking: 0.14em)[#upper(kicker)]
        #v(3pt)
        #text(font: "Instrument Serif", size: 20pt, fill: c_paper)[#title]
      ],
      box(
        fill: rgb("#E9AF4322"),
        stroke: 0.7pt + c_gold,
        radius: 2pt,
        inset: (x: 9pt, y: 5pt),
        text(font: "JetBrains Mono", size: 8.5pt, weight: "bold", fill: c_gold_hi)[PAGE #page_num / 10]
      )
    )
  ]
}

#let kv_sheet(rows, col1: 145pt, fill_alt: c_paper_alt) = table(
  columns: (col1, 1fr),
  stroke: (x: 0.45pt + c_rule, y: 0.45pt + c_rule),
  fill: (_, r) => if calc.even(r) { fill_alt } else { c_paper },
  inset: (x: 10pt, y: 7.5pt),
  ..rows.map(r => (
    text(font: "JetBrains Mono", size: 7.6pt, weight: "bold", fill: c_emerald)[#r.at(0)],
    text(size: 9.2pt, fill: c_ink)[#r.at(1)],
  )).flatten()
)

#set document(
  title: "Workbook Officiel Jour 2 — Dossier Rempli : " + cfg.ebook_title,
  author: cfg.author_name,
)

#set text(
  font: ("Instrument Sans", "Source Sans Pro"),
  size: 9.4pt,
  fill: c_ink,
  lang: "fr",
  region: "FR",
)
#set par(leading: 0.62em)

#set page(
  paper: "a4",
  fill: c_paper,
  margin: (top: 19mm, bottom: 18mm, left: 16mm, right: 16mm),
  header: context {
    if counter(page).get().first() > 1 {
      box(width: 100%, inset: (bottom: 4pt), stroke: (bottom: 0.45pt + c_rule))[
        #grid(
          columns: (1fr, auto),
          text(font: "JetBrains Mono", size: 6.8pt, fill: c_muted, tracking: 0.08em)[WORKBOOK OFFICIEL – JOUR 2 · DOSSIER COMPLÉTÉ],
          text(font: ("Instrument Sans", "Source Sans Pro"), size: 7.4pt, weight: "bold", fill: c_emerald)[#cfg.ebook_title]
        )
      ]
    }
  },
  footer: context {
    let pg = counter(page).get().first()
    if pg > 1 {
      box(width: 100%, inset: (top: 4pt), stroke: (top: 0.45pt + c_rule))[
        #grid(
          columns: (1fr, auto),
          text(size: 7.3pt, fill: c_muted)[Méthode exacte appliquée · #cfg.author_name],
          text(font: "JetBrains Mono", size: 7.5pt, weight: "bold", fill: c_emerald)[Page #pg / 10]
        )
      ]
    }
  },
)

// --- PAGE 1 : COUVERTURE / BIENVENUE ---
#box(
  width: 100%,
  fill: c_deep,
  radius: 3pt,
  inset: (x: 18pt, y: 18pt),
  stroke: (bottom: 2.8pt + c_gold),
)[
  #place(right + top, dx: 4pt, dy: -4pt, text(font: "Instrument Serif", size: 62pt, fill: rgb("#E9AF4326"))[J2])
  #text(font: "JetBrains Mono", size: 7.8pt, weight: "bold", fill: c_gold_hi, tracking: 0.16em)[#wb.page1.badge]
  #v(5pt)
  #text(font: "Instrument Serif", size: 25pt, fill: c_paper)[#wb.page1.title]
  #v(5pt)
  #line(length: 44pt, stroke: 1.2pt + c_gold)
  #v(5pt)
  #text(size: 10.2pt, fill: rgb("#EBE6DC"))[#wb.page1.subtitle]
]
#v(14pt)

#box(
  width: 100%,
  fill: c_paper_sage,
  stroke: (left: 2.5pt + c_emerald, rest: 0.45pt + c_rule),
  inset: 12pt,
)[
  #text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_emerald, tracking: 0.10em)[BIENVENUE — ESPRIT OFFICIEL DU WORKBOOK (PAGE 1)]
  #v(5pt)
  #text(size: 9.2pt, fill: c_ink)[#wb.page1.welcome]
]
#v(12pt)

#text(font: "Instrument Serif", size: 15.5pt, fill: c_deep)[Fiche d'identité du produit créé grâce à ce workbook]
#v(6pt)
#kv_sheet(wb.page1.summary_rows, col1: 150pt)
#v(14pt)

#box(
  width: 100%,
  fill: rgb("#FBF1DC"),
  stroke: (left: 2.5pt + c_gold, rest: 0.45pt + rgb("#E4C98C")),
  inset: 12pt,
)[
  #text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_gold_ink, tracking: 0.10em)[CORRESPONDANCE 1-POUR-1 (PAGES 1 À 10)]
  #v(4pt)
  #text(size: 8.9pt, fill: c_ink)[
    Chaque page de ce dossier correspond exactement à la page homonyme de *WORKBOOK-OFFICIEL-JOUR-2-CREE-TON-PREMIER-PRODUIT-DIGITAL.pdf*. Tous les exercices sont remplis sur mesure pour ton ebook, puis concrétisés dans *500-Idees-de-Business-a-Lancer-en-Afrique-en-2027.pdf*.
  ]
]
#pagebreak()

// --- PAGE 2 : OBJECTIF ---
#wb_masthead(wb.page2.kicker, wb.page2.title, 2)
#v(14pt)
#text(size: 9.6pt, fill: c_ink)[#wb.page2.intro]
#v(12pt)

#box(
  width: 100%,
  fill: rgb("#FBF1DC"),
  stroke: (left: 2.8pt + c_gold, rest: 0.45pt + rgb("#E4C98C")),
  inset: 14pt,
)[
  #text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_gold_ink, tracking: 0.12em)[OBJECTIF CENTRAL DU WORKBOOK]
  #v(4pt)
  #text(font: "Instrument Serif", size: 15pt, style: "italic", fill: c_deep)[#wb.page2.quote]
]
#v(14pt)

#text(font: "Instrument Serif", size: 15.5pt, fill: c_deep)[Ton engagement personnel (Complété)]
#v(6pt)
#kv_sheet(wb.page2.commitment, col1: 135pt, fill_alt: c_paper_sage)
#v(14pt)

#box(
  width: 100%,
  fill: c_paper_alt,
  stroke: (left: 2.5pt + c_emerald, rest: 0.45pt + c_rule),
  inset: 12pt,
)[
  #text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_emerald)[RAPPEL D'ACTION IMMÉDIATE]
  #v(4pt)
  #text(size: 9pt, fill: c_ink2)[
    Oublier la perfection signifie livrer dès aujourd'hui un ebook utile, structuré et lisible hors ligne sur smartphone. Tu pourras ensuite enrichir la version 2.0 avec les retours réels de tes 10 premiers lecteurs.
  ]
]
#pagebreak()

// --- PAGE 3 : VALIDATION VIN ---
#wb_masthead(wb.page3.kicker, wb.page3.title, 3)
#v(12pt)
#text(size: 9.3pt, fill: c_ink)[#wb.page3.intro]
#v(12pt)

// Diagramme VIN vectoriel horizontal
#grid(
  columns: (1fr, 18pt, 1fr, 18pt, 1fr),
  align: horizon,
  box(width: 100%, fill: c_paper_sage, stroke: 0.6pt + c_emerald, radius: 2pt, inset: 8pt, align(center)[
    #text(font: "Instrument Serif", size: 22pt, fill: c_emerald)[V] \
    #text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_emerald)[VALEUR CLAIRE]
  ]),
  align(center, text(font: "JetBrains Mono", size: 11pt, weight: "bold", fill: c_gold)[+]),
  box(width: 100%, fill: rgb("#FBF1DC"), stroke: 0.6pt + c_gold, radius: 2pt, inset: 8pt, align(center)[
    #text(font: "Instrument Serif", size: 22pt, fill: c_gold_ink)[I] \
    #text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_gold_ink)[INTENSITÉ #wb.page3.I_score]
  ]),
  align(center, text(font: "JetBrains Mono", size: 11pt, weight: "bold", fill: c_gold)[+]),
  box(width: 100%, fill: c_paper_clay, stroke: 0.6pt + c_clay, radius: 2pt, inset: 8pt, align(center)[
    #text(font: "Instrument Serif", size: 22pt, fill: c_clay_ink)[N] \
    #text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_clay_ink)[NOMBRE MASSIF]
  ]),
)
#v(12pt)

#box(width: 100%, fill: c_paper_sage, stroke: (left: 2.5pt + c_emerald), inset: 11pt)[
  #text(font: "JetBrains Mono", size: 7.4pt, weight: "bold", fill: c_emerald)[V – PROBLÈME (VALEUR) : QUEL PROBLÈME PRÉCIS VEUX-TU RÉSOUDRE ?]
  #v(4pt)
  #text(size: 9pt, fill: c_ink)[#wb.page3.V]
]
#v(9pt)

#box(width: 100%, fill: rgb("#FBF1DC"), stroke: (left: 2.5pt + c_gold), inset: 11pt)[
  #text(font: "JetBrains Mono", size: 7.4pt, weight: "bold", fill: c_gold_ink)[I – INTENSITÉ : NOTE #wb.page3.I_score — POURQUOI EST-IL DOULOUREUX ?]
  #v(4pt)
  #text(size: 9pt, fill: c_ink)[#wb.page3.I_exp]
]
#v(9pt)

#box(width: 100%, fill: c_paper_clay, stroke: (left: 2.5pt + c_clay), inset: 11pt)[
  #text(font: "JetBrains Mono", size: 7.4pt, weight: "bold", fill: c_clay_ink)[N – NOMBRE : CAS ISOLÉ OU MARCHÉ RÉPANDU ?]
  #v(4pt)
  #text(size: 9pt, fill: c_ink)[#wb.page3.N]
]
#v(11pt)

#box(width: 100%, fill: c_deep, radius: 2pt, inset: 11pt)[
  #text(font: "JetBrains Mono", size: 8pt, weight: "bold", fill: c_gold_hi)[VERDICT : ]
  #text(size: 9.2pt, weight: "bold", fill: c_paper)[#wb.page3.conclusion]
]
#pagebreak()

// --- PAGE 4 : PROMESSE CLAIRE ---
#wb_masthead(wb.page4.kicker, wb.page4.title, 4)
#v(12pt)
#text(size: 9.4pt, fill: c_ink)[#wb.page4.intro]
#v(12pt)

#kv_sheet((
  ("1. Pour qui est ton produit ?", wb.page4.q1),
  ("2. Résultat concret promis", wb.page4.q2),
  ("3. Délai promis", wb.page4.q3),
), col1: 155pt, fill_alt: c_paper_sage)

#v(16pt)
#text(font: "Instrument Serif", size: 15.5pt, fill: c_deep)[Formule exacte du Workbook appliquée]
#v(4pt)
#text(font: "JetBrains Mono", size: 7.8pt, fill: c_muted)[Modèle vierge : #wb.page4.formula_template]
#v(10pt)

#box(
  width: 100%,
  fill: rgb("#FBF1DC"),
  stroke: (left: 3pt + c_gold, rest: 0.6pt + rgb("#E4C98C")),
  inset: 16pt,
)[
  #text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_gold_ink, tracking: 0.12em)[PROMESSE RETENUE SUR LA COUVERTURE & POUR LA VENTE]
  #v(5pt)
  #text(font: "Instrument Serif", size: 16pt, style: "italic", fill: c_deep)[#wb.page4.formula_filled]
]
#pagebreak()

// --- PAGE 5 : FORMAT PDF ---
#wb_masthead(wb.page5.kicker, wb.page5.title, 5)
#v(12pt)
#text(font: "Instrument Serif", size: 15.5pt, fill: c_deep)[Pourquoi commencer avec un PDF ? (Critères du Workbook)]
#v(7pt)

#for r in wb.page5.reasons_pdf [
  #box(width: 100%, inset: (y: 4pt), stroke: (bottom: 0.4pt + c_rule))[
    #checkbox(checked: true, accent: c_emerald) #h(7pt) #text(size: 9.2pt, fill: c_ink)[#r]
  ]
]
#v(14pt)

#text(font: "Instrument Serif", size: 15.5pt, fill: c_deep)[Exercice « À toi de jouer ! » (Complété avec transparence)]
#v(6pt)
#kv_sheet((
  ("Pourquoi le format PDF", wb.page5.why_chosen),
  ("Nombre de pages prévues", wb.page5.pages_note),
  ("Titre officiel du produit", wb.page5.provisional_title),
), col1: 150pt, fill_alt: c_paper_alt)
#pagebreak()

// --- PAGE 6 : STRUCTURE EN 5 PARTIES + CONCLUSION ---
#wb_masthead(wb.page6.kicker, wb.page6.title, 6)
#v(12pt)
#text(size: 9.3pt, fill: c_ink)[Architecture exacte appliquée dans *500-Idees-de-Business-a-Lancer-en-Afrique-en-2027.pdf* :]
#v(10pt)

#table(
  columns: (38pt, 95pt, 1fr),
  stroke: (x: 0.45pt + c_rule, y: 0.45pt + c_rule),
  fill: (_, r) => if calc.even(r) { c_paper_sage } else { c_paper_alt },
  inset: (x: 9pt, y: 8.5pt),
  ..wb.page6.parts.map(p => (
    align(center + top, text(font: "Instrument Serif", size: 15pt, fill: c_emerald)[#p.at(0)]),
    text(size: 9.2pt, weight: "bold", fill: c_deep)[#p.at(1)],
    text(size: 8.9pt, fill: c_ink2)[#p.at(2)],
  )).flatten()
)
#pagebreak()

// --- PAGE 7 : IA & CHECKLIST ---
#wb_masthead(wb.page7.kicker, wb.page7.title, 7)
#v(10pt)

#box(
  width: 100%,
  fill: c_paper_sage,
  stroke: (left: 2.5pt + c_emerald, rest: 0.45pt + c_rule),
  inset: 10pt,
)[
  #text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_emerald)[PROMPT EXACT DU WORKBOOK → VERSION APPLIQUÉE]
  #v(4pt)
  #text(size: 8.2pt, style: "italic", fill: c_ink2)[*Modèle :* #wb.page7.prompt_template]
  #v(4pt)
  #text(size: 8.4pt, fill: c_ink)[*Appliqué :* #wb.page7.prompt_applied]
]
#v(9pt)

#text(font: "Instrument Serif", size: 13.5pt, fill: c_deep)[Comment l'utiliser (6 étapes réalisées)]
#v(3pt)
#for s in wb.page7.how_to_use [
  #text(size: 8.4pt, fill: c_ink)[#s]
  #v(2pt)
]
#v(7pt)

#text(font: "Instrument Serif", size: 13.5pt, fill: c_deep)[Checklist de création (7 items du Workbook)]
#v(4pt)
#box(width: 100%, fill: c_paper_alt, stroke: 0.5pt + c_rule, inset: (x: 10pt, y: 5pt))[
  #for item in wb.page7.checklist [
    #box(width: 100%, inset: (y: 3pt), stroke: (bottom: 0.35pt + c_rule))[
      #checkbox(checked: true, accent: c_emerald) #h(7pt) #text(size: 8.4pt, fill: c_ink)[#item.at(0)]
    ]
  ]
]
#v(8pt)

#box(width: 100%, fill: rgb("#FBF1DC"), stroke: (left: 2.2pt + c_gold), inset: 9pt)[
  #text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_gold_ink)[IMPORTANT — PERSONNALISATION]
  #v(2pt)
  #text(size: 8.2pt, fill: c_ink)[#wb.page7.important_note]
]
#pagebreak()

// --- PAGE 8 : RÉCAPITULATIF ---
#wb_masthead(wb.page8.kicker, wb.page8.title, 8)
#v(12pt)
#text(size: 9.4pt, fill: c_ink)[#wb.page8.intro]
#v(12pt)

#table(
  columns: (1fr, 78pt),
  stroke: (x: 0.45pt + c_rule, y: 0.45pt + c_rule),
  fill: (_, r) => if calc.even(r) { c_paper_sage } else { c_paper },
  inset: (x: 11pt, y: 9.5pt),
  ..wb.page8.recap_cards.map(c => (
    block[
      #text(size: 9.5pt, weight: "bold", fill: c_deep)[#c.at(0)]
      #v(2pt)
      #text(size: 8.6pt, fill: c_ink2)[#c.at(1)]
    ],
    align(center + horizon)[
      #box(fill: c_emerald, radius: 2pt, inset: (x: 7pt, y: 3pt))[
        #text(font: "JetBrains Mono", size: 7.4pt, weight: "bold", fill: c_paper)[#c.at(2)]
      ]
    ]
  )).flatten()
)
#v(14pt)

#box(width: 100%, fill: rgb("#FBF1DC"), stroke: (left: 2.5pt + c_gold), inset: 12pt)[
  #text(font: "Instrument Serif", size: 14pt, fill: c_deep)[Tu es maintenant un créateur de produits digitaux]
  #v(3pt)
  #text(size: 8.9pt, fill: c_ink2)[Ton fichier complet *500-Idees-de-Business-a-Lancer-en-Afrique-en-2027.pdf* concrétise les 5 étapes ci-dessus.]
]
#pagebreak()

// --- PAGE 9 : DÉCLARATION OFFICIELLE & POSTS FACEBOOK ---
#wb_masthead(wb.page9.kicker, wb.page9.title, 9)
#v(10pt)
#text(font: "Instrument Serif", size: 14pt, fill: c_deep)[Ton engagement officiel]
#v(5pt)
#kv_sheet(wb.page9.declaration, col1: 135pt, fill_alt: c_paper_sage)
#v(11pt)

#text(font: "Instrument Serif", size: 14pt, fill: c_deep)[Partage ta victoire !]
#v(2pt)
#text(size: 8.5pt, weight: "bold", fill: c_clay_ink)[#wb.page9.fb_action]
#v(7pt)

#for p in wb.page9.social_posts [
  #box(
    width: 100%,
    fill: c_paper_alt,
    stroke: (left: 2.2pt + c_gold, rest: 0.45pt + c_rule),
    inset: (x: 11pt, y: 8pt),
  )[
    #text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_gold_ink)[#p.at(0)]
    #v(3pt)
    #text(size: 8.2pt, style: "italic", fill: c_ink)[#p.at(1)]
  ]
  #v(6pt)
]
#pagebreak()

// --- PAGE 10 : PROCHAINS PAS ---
#wb_masthead(wb.page10.kicker, wb.page10.title, 10)
#v(12pt)

#for st in wb.page10.steps [
  #box(
    width: 100%,
    fill: c_paper_sage,
    stroke: (left: 2.5pt + c_emerald, rest: 0.45pt + c_rule),
    inset: 11pt,
  )[
    #text(size: 9.4pt, weight: "bold", fill: c_deep)[#st.at(0)]
    #v(3pt)
    #text(size: 8.7pt, fill: c_ink2)[#st.at(1)]
  ]
  #v(8pt)
]

#box(
  width: 100%,
  fill: rgb("#FBF1DC"),
  stroke: (left: 2.5pt + c_gold, rest: 0.45pt + rgb("#E4C98C")),
  inset: 11pt,
)[
  #text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_gold_ink)[MESSAGE WHATSAPP PRÊT POUR TES 10 PREMIERS TESTEURS]
  #v(4pt)
  #text(size: 8.4pt, style: "italic", fill: c_ink)[#wb.page10.whatsapp_testers]
]
#v(12pt)
#text(font: "Instrument Serif", size: 13pt, style: "italic", fill: c_emerald)[#wb.page10.closing]
