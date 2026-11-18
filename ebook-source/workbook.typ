#let data = json("ebook_data.json")
#let cfg = data.config
#let wb = data.workbook

#let c_paper    = rgb("#FCFBF8")
#let c_tint     = rgb("#F5F2EC")
#let c_ink      = rgb("#161B19")
#let c_ink2     = rgb("#4B5450")
#let c_muted    = rgb("#78807C")
#let c_accent   = rgb("#103E33")
#let c_ocre     = rgb("#8A5808")
#let c_clay     = rgb("#8E3C1D")
#let c_rule     = rgb("#DDD6CA")
#let c_hair     = rgb("#EAE4DA")

#let checkbox(checked: true, accent: c_accent) = box(
  width: 8.5pt, height: 8.5pt,
  fill: if checked { accent } else { none },
  stroke: 0.7pt + accent,
  baseline: 1.2pt,
  if checked {
    place(center + horizon)[
      #curve(
        stroke: (paint: c_paper, thickness: 1.15pt, cap: "round", join: "round"),
        curve.move((1.5pt, 4.3pt)),
        curve.line((3.4pt, 6.2pt)),
        curve.line((7.0pt, 2.3pt)),
      )
    ]
  }
)

#let wb_masthead(kicker, title) = {
  block(width: 100%, below: 12pt)[
    #text(size: 8.2pt, weight: "semibold", fill: c_accent, tracking: 0.05em)[#kicker]
    #v(4pt)
    #text(font: "Instrument Serif", size: 22.5pt, fill: c_ink)[#title]
    #v(7pt)
    #line(length: 100%, stroke: 0.75pt + c_accent)
  ]
}

#let kv_sheet(rows, col1: 148pt) = table(
  columns: (col1, 1fr),
  stroke: (x, y) => (bottom: 0.35pt + c_hair),
  fill: none,
  inset: (x: 4pt, y: 7.5pt),
  ..rows.map(r => (
    text(size: 8.4pt, weight: "semibold", fill: c_accent)[#r.at(0)],
    text(size: 9.1pt, fill: c_ink)[#r.at(1)],
  )).flatten()
)

#set document(
  title: "Workbook Officiel Jour 2 — Dossier Rempli : " + cfg.ebook_title,
  author: cfg.author_name,
)

#set text(
  font: "Instrument Sans",
  size: 9.3pt,
  fill: c_ink,
  lang: "fr",
  region: "FR",
)
#set par(leading: 0.64em)

#set page(
  paper: "a4",
  fill: c_paper,
  margin: (top: 21mm, bottom: 19mm, left: 17mm, right: 17mm),
  header: context {
    if counter(page).get().first() > 1 {
      box(width: 100%, inset: (bottom: 5pt), stroke: (bottom: 0.35pt + c_rule))[
        #grid(
          columns: (1fr, auto),
          text(size: 7.6pt, fill: c_muted)[Workbook Officiel · Jour 2 · Dossier complété],
          text(size: 7.6pt, weight: "semibold", fill: c_accent)[#cfg.ebook_title]
        )
      ]
    }
  },
  footer: context {
    let pg = counter(page).get().first()
    if pg > 1 {
      box(width: 100%, inset: (top: 5pt), stroke: (top: 0.35pt + c_rule))[
        #grid(
          columns: (1fr, auto),
          text(size: 7.5pt, fill: c_muted)[Méthode appliquée · #cfg.author_name],
          text(size: 8.0pt, weight: "semibold", fill: c_ink)[Page #pg sur 10]
        )
      ]
    }
  },
)

// --- PAGE 1 : COUVERTURE / BIENVENUE ---
#block(width: 100%, below: 14pt)[
  #text(size: 8.2pt, weight: "semibold", fill: c_accent, tracking: 0.05em)[#wb.page1.badge]
  #v(4pt)
  #text(font: "Instrument Serif", size: 24pt, fill: c_ink)[#wb.page1.title]
  #v(5pt)
  #text(size: 10.2pt, style: "italic", fill: c_ink2)[#wb.page1.subtitle]
  #v(8pt)
  #line(length: 100%, stroke: 0.75pt + c_accent)
]

#box(
  width: 100%,
  stroke: (left: 1pt + c_accent),
  inset: (left: 13pt, y: 4pt),
)[
  #text(size: 8.4pt, weight: "bold", fill: c_accent)[Bienvenue (Page 1 du Workbook)]
  #v(4pt)
  #text(size: 9.1pt, fill: c_ink)[#wb.page1.welcome]
]
#v(16pt)

#text(font: "Instrument Serif", size: 15.5pt, fill: c_ink)[Fiche d'identité du produit créé]
#v(4pt)
#line(length: 100%, stroke: 0.5pt + c_rule)
#kv_sheet(wb.page1.summary_rows, col1: 148pt)
#v(18pt)

#box(
  width: 100%,
  stroke: (top: 0.6pt + c_rule, bottom: 0.6pt + c_rule),
  inset: (y: 10pt),
)[
  #text(size: 8.6pt, fill: c_ink2)[
    Chaque page de ce dossier correspond page pour page à *WORKBOOK-OFFICIEL-JOUR-2-CREE-TON-PREMIER-PRODUIT-DIGITAL.pdf* (pages 1 à 10), concrétisé dans l'ouvrage *500-Idees-de-Business-a-Lancer-en-Afrique-en-2027.pdf*.
  ]
]
#pagebreak()

// --- PAGE 2 : OBJECTIF ---
#wb_masthead(wb.page2.kicker, wb.page2.title)
#text(size: 9.4pt, fill: c_ink)[#wb.page2.intro]
#v(14pt)

#box(
  width: 100%,
  stroke: (left: 1.1pt + c_accent),
  inset: (left: 13pt, y: 5pt),
)[
  #text(font: "Instrument Serif", size: 15pt, style: "italic", fill: c_ink)[#wb.page2.quote]
]
#v(18pt)

#text(font: "Instrument Serif", size: 15.5pt, fill: c_ink)[Engagement personnel (Complété)]
#v(4pt)
#line(length: 100%, stroke: 0.5pt + c_rule)
#kv_sheet(wb.page2.commitment, col1: 142pt)
#v(18pt)

#box(
  width: 100%,
  stroke: (top: 0.45pt + c_rule),
  inset: (top: 9pt),
)[
  #text(size: 8.6pt, weight: "semibold", fill: c_accent)[Rappel de méthode]
  #v(3pt)
  #text(size: 8.9pt, fill: c_ink2)[
    Oublier la perfection signifie livrer dès aujourd'hui un livre utile, structuré et lisible hors ligne sur smartphone, puis enrichir la version suivante grâce aux retours des dix premiers lecteurs.
  ]
]
#pagebreak()

// --- PAGE 3 : VALIDATION VIN ---
#wb_masthead(wb.page3.kicker, wb.page3.title)
#text(size: 9.3pt, fill: c_ink)[#wb.page3.intro]
#v(14pt)

#grid(
  columns: (1fr, 18pt, 1fr, 18pt, 1fr),
  align: horizon,
  box(width: 100%, stroke: (top: 1.2pt + c_accent, bottom: 0.4pt + c_rule), inset: (y: 8pt), align(center)[
    #text(font: "Instrument Serif", size: 22pt, fill: c_accent)[V] \
    #text(size: 7.8pt, weight: "semibold", fill: c_ink)[Valeur claire]
  ]),
  align(center, text(size: 12pt, weight: "semibold", fill: c_muted)[+]),
  box(width: 100%, stroke: (top: 1.2pt + c_ocre, bottom: 0.4pt + c_rule), inset: (y: 8pt), align(center)[
    #text(font: "Instrument Serif", size: 22pt, fill: c_ocre)[I] \
    #text(size: 7.8pt, weight: "semibold", fill: c_ink)[Intensité #wb.page3.I_score]
  ]),
  align(center, text(size: 12pt, weight: "semibold", fill: c_muted)[+]),
  box(width: 100%, stroke: (top: 1.2pt + c_clay, bottom: 0.4pt + c_rule), inset: (y: 8pt), align(center)[
    #text(font: "Instrument Serif", size: 22pt, fill: c_clay)[N] \
    #text(size: 7.8pt, weight: "semibold", fill: c_ink)[Nombre massif]
  ]),
)
#v(14pt)

#box(width: 100%, stroke: (left: 1pt + c_accent), inset: (left: 12pt, y: 3pt))[
  #text(size: 8.5pt, weight: "bold", fill: c_accent)[V · Problème (Valeur) : quel problème précis veux-tu résoudre ?]
  #v(3pt)
  #text(size: 9pt, fill: c_ink)[#wb.page3.V]
]
#v(10pt)

#box(width: 100%, stroke: (left: 1pt + c_ocre), inset: (left: 12pt, y: 3pt))[
  #text(size: 8.5pt, weight: "bold", fill: c_ocre)[I · Intensité : note #wb.page3.I_score — pourquoi est-il douloureux ?]
  #v(3pt)
  #text(size: 9pt, fill: c_ink)[#wb.page3.I_exp]
]
#v(10pt)

#box(width: 100%, stroke: (left: 1pt + c_clay), inset: (left: 12pt, y: 3pt))[
  #text(size: 8.5pt, weight: "bold", fill: c_clay)[N · Nombre : cas isolé ou marché répandu ?]
  #v(3pt)
  #text(size: 9pt, fill: c_ink)[#wb.page3.N]
]
#v(14pt)

#box(width: 100%, stroke: (top: 0.8pt + c_accent, bottom: 0.8pt + c_accent), inset: (y: 9pt))[
  #text(size: 9.2pt, weight: "semibold", fill: c_accent)[#wb.page3.conclusion]
]
#pagebreak()

// --- PAGE 4 : PROMESSE CLAIRE ---
#wb_masthead(wb.page4.kicker, wb.page4.title)
#text(size: 9.4pt, fill: c_ink)[#wb.page4.intro]
#v(12pt)

#kv_sheet((
  ("1. Pour qui est ton produit ?", wb.page4.q1),
  ("2. Résultat concret promis", wb.page4.q2),
  ("3. Délai promis", wb.page4.q3),
), col1: 155pt)

#v(18pt)
#text(font: "Instrument Serif", size: 15.5pt, fill: c_ink)[Formule du Workbook appliquée]
#v(4pt)
#text(size: 8.4pt, fill: c_muted)[Modèle vierge : #wb.page4.formula_template]
#v(12pt)

#box(
  width: 100%,
  stroke: (left: 1.2pt + c_accent),
  inset: (left: 14pt, y: 6pt),
)[
  #text(font: "Instrument Serif", size: 16.5pt, style: "italic", fill: c_ink)[#wb.page4.formula_filled]
]
#pagebreak()

// --- PAGE 5 : FORMAT PDF ---
#wb_masthead(wb.page5.kicker, wb.page5.title)
#text(font: "Instrument Serif", size: 15.5pt, fill: c_ink)[Pourquoi commencer avec un PDF ?]
#v(7pt)

#for r in wb.page5.reasons_pdf [
  #box(width: 100%, inset: (y: 4.5pt), stroke: (bottom: 0.35pt + c_hair))[
    #checkbox(checked: true, accent: c_accent) #h(7pt) #text(size: 9.1pt, fill: c_ink)[#r]
  ]
]
#v(16pt)

#text(font: "Instrument Serif", size: 15.5pt, fill: c_ink)[Exercice « À toi de jouer ! » (Complété avec transparence)]
#v(4pt)
#line(length: 100%, stroke: 0.5pt + c_rule)
#kv_sheet((
  ("Pourquoi le format PDF", wb.page5.why_chosen),
  ("Nombre de pages prévues", wb.page5.pages_note),
  ("Titre officiel du produit", wb.page5.provisional_title),
), col1: 150pt)
#pagebreak()

// --- PAGE 6 : STRUCTURE EN 5 PARTIES + CONCLUSION ---
#wb_masthead(wb.page6.kicker, wb.page6.title)
#text(size: 9.3pt, fill: c_ink)[Architecture exacte appliquée dans l'ouvrage *« #cfg.ebook_title »* :]
#v(10pt)

#table(
  columns: (36pt, 96pt, 1fr),
  stroke: (x, y) => (bottom: if y == 0 { 0.8pt + c_ink } else { 0.35pt + c_hair }),
  fill: none,
  inset: (x: 5pt, y: 8.5pt),
  table.header(
    text(size: 7.8pt, weight: "bold", fill: c_accent)[N°],
    text(size: 7.8pt, weight: "bold", fill: c_accent)[Partie],
    text(size: 7.8pt, weight: "bold", fill: c_accent)[Contenu synthétique],
  ),
  ..wb.page6.parts.map(p => (
    align(left + top, text(font: "Instrument Serif", size: 15pt, fill: c_accent)[#p.at(0)]),
    text(size: 9.1pt, weight: "bold", fill: c_ink)[#p.at(1)],
    text(size: 8.8pt, fill: c_ink2)[#p.at(2)],
  )).flatten()
)
#pagebreak()

// --- PAGE 7 : IA & CHECKLIST ---
#wb_masthead(wb.page7.kicker, wb.page7.title)

#box(
  width: 100%,
  fill: c_tint,
  stroke: (left: 1pt + c_accent),
  inset: (x: 11pt, y: 8pt),
)[
  #text(size: 8.2pt, weight: "bold", fill: c_accent)[Prompt du Workbook · Modèle et version adaptée]
  #v(4pt)
  #text(size: 8.1pt, style: "italic", fill: c_ink2)[*Modèle :* #wb.page7.prompt_template]
  #v(4pt)
  #text(size: 8.3pt, fill: c_ink)[*Appliqué :* #wb.page7.prompt_applied]
]
#v(10pt)

#text(font: "Instrument Serif", size: 14pt, fill: c_ink)[Comment l'utiliser (6 étapes réalisées)]
#v(4pt)
#for s in wb.page7.how_to_use [
  #text(size: 8.4pt, fill: c_ink2)[#s]
  #v(2pt)
]
#v(9pt)

#text(font: "Instrument Serif", size: 14pt, fill: c_ink)[Checklist de création (7 items du Workbook)]
#v(4pt)
#for item in wb.page7.checklist [
  #box(width: 100%, inset: (y: 3.3pt), stroke: (bottom: 0.35pt + c_hair))[
    #checkbox(checked: true, accent: c_accent) #h(7pt) #text(size: 8.4pt, fill: c_ink)[#item.at(0)]
  ]
]
#v(9pt)

#box(width: 100%, stroke: (top: 0.5pt + c_rule), inset: (top: 7pt))[
  #text(size: 8.3pt, style: "italic", fill: c_ink2)[#wb.page7.important_note]
]
#pagebreak()

// --- PAGE 8 : RÉCAPITULATIF ---
#wb_masthead(wb.page8.kicker, wb.page8.title)
#text(size: 9.4pt, fill: c_ink)[#wb.page8.intro]
#v(12pt)

#table(
  columns: (1fr, 74pt),
  stroke: (x, y) => (bottom: 0.35pt + c_hair),
  fill: none,
  inset: (x: 4pt, y: 9.5pt),
  ..wb.page8.recap_cards.map(c => (
    block[
      #text(size: 9.4pt, weight: "bold", fill: c_ink)[#c.at(0)]
      #v(2pt)
      #text(size: 8.6pt, fill: c_ink2)[#c.at(1)]
    ],
    align(right + horizon)[
      #text(size: 8.4pt, weight: "semibold", fill: c_accent)[#checkbox(checked: true, accent: c_accent) #h(5pt) #c.at(2)]
    ]
  )).flatten()
)
#v(16pt)

#box(width: 100%, stroke: (left: 1pt + c_accent), inset: (left: 13pt, y: 4pt))[
  #text(font: "Instrument Serif", size: 14.5pt, fill: c_ink)[Tu es maintenant un créateur de produits digitaux]
  #v(3pt)
  #text(size: 8.9pt, fill: c_ink2)[L'ouvrage complet *« #cfg.ebook_title »* concrétise les cinq étapes ci-dessus.]
]
#pagebreak()

// --- PAGE 9 : DÉCLARATION OFFICIELLE & POSTS FACEBOOK ---
#wb_masthead(wb.page9.kicker, wb.page9.title)
#text(font: "Instrument Serif", size: 14.5pt, fill: c_ink)[Ton engagement officiel]
#v(4pt)
#line(length: 100%, stroke: 0.5pt + c_rule)
#kv_sheet(wb.page9.declaration, col1: 138pt)
#v(14pt)

#text(font: "Instrument Serif", size: 14.5pt, fill: c_ink)[Partage ta victoire]
#v(2pt)
#text(size: 8.5pt, weight: "semibold", fill: c_clay)[#wb.page9.fb_action]
#v(9pt)

#for p in wb.page9.social_posts [
  #box(
    width: 100%,
    stroke: (left: 0.9pt + c_accent),
    inset: (left: 11pt, y: 3pt),
  )[
    #text(size: 8.3pt, weight: "bold", fill: c_accent)[#p.at(0)]
    #v(2.5pt)
    #text(size: 8.3pt, style: "italic", fill: c_ink)[#p.at(1)]
  ]
  #v(9pt)
]
#pagebreak()

// --- PAGE 10 : PROCHAINS PAS ---
#wb_masthead(wb.page10.kicker, wb.page10.title)

#for st in wb.page10.steps [
  #box(
    width: 100%,
    stroke: (bottom: 0.35pt + c_hair),
    inset: (y: 8pt),
  )[
    #text(size: 9.4pt, weight: "bold", fill: c_ink)[#st.at(0)]
    #v(3pt)
    #text(size: 8.8pt, fill: c_ink2)[#st.at(1)]
  ]
]
#v(12pt)

#box(
  width: 100%,
  stroke: (left: 1pt + c_accent),
  inset: (left: 12pt, y: 4pt),
)[
  #text(size: 8.4pt, style: "italic", fill: c_ink)[#wb.page10.whatsapp_testers]
]
#v(16pt)
#text(font: "Instrument Serif", size: 13.5pt, style: "italic", fill: c_accent)[#wb.page10.closing]
