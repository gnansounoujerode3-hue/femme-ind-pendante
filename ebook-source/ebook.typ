#let data = json("ebook_data.json")
#let cfg = data.config
#let sectors = data.sectors

// Palette « Savane Solaire & Papier Ivoire »
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
#let c_sage_rule  = rgb("#C7D7CF")

#let set_sec(name) = [#metadata(name)<sec-marker>]

#let checkbox(checked: false, accent: c_emerald) = box(
  width: 8.5pt, height: 8.5pt, radius: 1.5pt,
  fill: if checked { accent } else { c_paper },
  stroke: 0.8pt + accent,
  baseline: 1.2pt,
  align(center + horizon)[
    #if checked {
      text(font: "Source Sans Pro", size: 6.5pt, weight: "bold", fill: c_paper)[✓]
    }
  ]
)

#let pill_budget(tier) = {
  let bg = if tier == "Petit" { c_paper_sage } else if tier == "Moyen" { rgb("#FBF1DC") } else { c_paper_clay }
  let fg = if tier == "Petit" { c_emerald } else if tier == "Moyen" { c_gold_ink } else { c_clay_ink }
  let bd = if tier == "Petit" { rgb("#B7D3C7") } else if tier == "Moyen" { rgb("#E4C98C") } else { rgb("#E3B4A1") }
  let lbl = if tier == "Petit" { "PETIT <50K" } else if tier == "Moyen" { "MOYEN 50-300K" } else { "STRUCTURÉ 300K+" }
  box(
    fill: bg, stroke: 0.45pt + bd, radius: 2pt,
    inset: (x: 4.5pt, y: 2pt),
    text(font: "JetBrains Mono", size: 6.3pt, weight: "bold", fill: fg, tracking: 0.04em)[#lbl]
  )
}

#let chapter_opener(num, kicker, title, question, lbl_name) = {
  set_sec(kicker)
  [#metadata(kicker)#label(lbl_name)]
  box(
    width: 100%,
    fill: c_deep,
    radius: 3pt,
    inset: (x: 16pt, y: 12pt),
    stroke: (bottom: 2.2pt + c_gold),
  )[
    #place(
      right + horizon,
      dx: 4pt,
      text(font: "Instrument Serif", size: 62pt, fill: rgb("#E9AF4330"))[#num]
    )
    #block(width: 84%)[
      #text(font: "JetBrains Mono", size: 7.3pt, weight: "bold", fill: c_gold_hi, tracking: 0.14em)[#upper(kicker)]
      #v(3pt)
      #text(font: "Instrument Serif", size: 21.5pt, fill: c_paper, weight: "regular")[#title]
      #v(4pt)
      #line(length: 34pt, stroke: 1.1pt + c_gold)
      #v(4pt)
      #text(font: ("Instrument Sans", "Source Sans Pro"), size: 8.4pt, style: "italic", fill: rgb("#DCE6E1"))[#question]
    ]
  ]
}

#let section_subhead(kicker, title) = {
  v(7pt)
  block(breakable: false, sticky: true)[
    #text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_gold_ink, tracking: 0.12em)[#upper(kicker)]
    #v(2pt)
    #text(font: "Instrument Serif", size: 15.5pt, fill: c_emerald)[#title]
    #v(2pt)
    #line(length: 100%, stroke: 0.5pt + c_rule)
  ]
  v(4pt)
}

#set document(
  title: cfg.ebook_title,
  author: cfg.author_name,
)

#set text(
  font: ("Instrument Sans", "Source Sans Pro"),
  size: 9.4pt,
  fill: c_ink,
  lang: "fr",
  region: "FR",
)

#set par(leading: 0.62em, justify: false)

// ============================================================================
// PAGE 1 : COUVERTURE TASCHEN / MONOCLE FULL-BLEED
// ============================================================================
#page(
  paper: "a4",
  margin: 0mm,
  fill: c_deep,
  header: none,
  footer: none,
)[
  // Artwork plein cadre
  #place(top + left, image("cover_art.png", width: 210mm, height: 297mm, fit: "cover"))

  // Dégradé doux supérieur & inférieur pour contraste typographique maximal
  #place(top + left, rect(
    width: 210mm, height: 118mm,
    fill: gradient.linear(
      rgb("#061E18F5"), rgb("#061E18DC"), rgb("#061E1885"), rgb("#061E1800"),
      angle: 90deg,
    )
  ))
  #place(bottom + left, rect(
    width: 210mm, height: 90mm,
    fill: gradient.linear(
      rgb("#061E1800"), rgb("#061E18B5"), rgb("#061E18EE"), rgb("#061E18F6"),
      angle: 90deg,
    )
  ))

  // Cadre architectural doré fin
  #place(top + left, dx: 9mm, dy: 9mm, rect(
    width: 192mm, height: 279mm,
    stroke: 0.6pt + rgb("#C5881E99"),
    fill: none,
  ))

  // Masthead supérieur (zéro pill criard — pure typographie éditoriale)
  #place(top + left, dx: 17mm, dy: 16mm, box(width: 176mm)[
    #grid(
      columns: (1fr, 1fr),
      align(left)[
        #text(font: "JetBrains Mono", size: 7.4pt, weight: "bold", fill: c_gold_hi, tracking: 0.16em)[ÉDITION 2027 · COLLECTION AFRIQUE]
      ],
      align(right)[
        #text(font: "JetBrains Mono", size: 7.4pt, fill: rgb("#DCE5E0"), tracking: 0.14em)[GUIDE PRATIQUE & CATALOGUE]
      ]
    )
    #v(5pt)
    #line(length: 100%, stroke: 0.5pt + rgb("#C5881E77"))
  ])

  // Bloc Titre Sculptural à fort contraste d'échelle (Instrument Serif)
  #place(top + left, dx: 17mm, dy: 27mm, box(width: 176mm)[
    #grid(
      columns: (auto, 1fr),
      column-gutter: 12pt,
      align: bottom,
      box(
        inset: (right: 11pt, top: 2pt, bottom: 2pt),
        stroke: (right: 1.4pt + c_gold),
      )[
        #text(font: "Instrument Serif", size: 70pt, fill: c_gold_hi, tracking: -0.02em)[500]
      ],
      block(inset: (bottom: 4pt))[
        #text(font: "Instrument Serif", size: 28pt, fill: c_paper, tracking: -0.01em)[Idées de Business]
        #v(-4pt)
        #text(font: "Instrument Serif", size: 28pt, fill: c_paper, tracking: -0.01em)[à lancer en Afrique]
      ]
    )
    #v(6pt)
    #text(font: "JetBrains Mono", size: 10.5pt, weight: "bold", fill: c_gold_hi, tracking: 0.22em)[HORIZON 2027]
    #v(7pt)
    #text(font: ("Instrument Sans", "Source Sans Pro"), size: 10pt, fill: rgb("#F6F2EA"))[
      #cfg.ebook_subtitle
    ]
  ])

  // Zone Basse : Promesse du Workbook + Colophon Auteur
  #place(bottom + left, dx: 17mm, dy: -16mm, box(width: 176mm)[
    #box(
      width: 100%,
      fill: rgb("#07241DD6"),
      stroke: (left: 2.2pt + c_gold, rest: 0.5pt + rgb("#C5881E66")),
      radius: 2.5pt,
      inset: (x: 14pt, y: 11pt),
    )[
      #text(font: "JetBrains Mono", size: 6.8pt, weight: "bold", fill: c_gold_hi, tracking: 0.14em)[PROMESSE DU GUIDE · MÉTHODE WORKBOOK JOUR 2]
      #v(4pt)
      #text(font: "Instrument Serif", size: 13.5pt, style: "italic", fill: c_paper)[
        « #cfg.promise_formula »
      ]
    ]
    #v(11pt)
    #line(length: 100%, stroke: 0.45pt + rgb("#C5881E66"))
    #v(6pt)
    #grid(
      columns: (1fr, auto),
      align(left)[
        #text(font: ("Instrument Sans", "Source Sans Pro"), size: 9.2pt, weight: "bold", fill: c_paper)[Par #cfg.author_name]
      ],
      align(right)[
        #text(font: "JetBrains Mono", size: 7.4pt, fill: c_gold_hi, tracking: 0.08em)[20 SECTEURS · 500 FICHES · PLAN 7 JOURS]
      ]
    )
  ])
]

// ============================================================================
// CONFIGURATION DES PAGES INTÉRIEURES (PAPIER IVOIRE & FOLIOS ÉDITORIAUX)
// ============================================================================
#set page(
  paper: "a4",
  fill: c_paper,
  margin: (top: 20mm, bottom: 18mm, left: 15mm, right: 15mm),
  header: context {
    let pg = here().page()
    let markers = query(selector(<sec-marker>)).filter(m => m.location().page() <= pg)
    let sec = if markers.len() > 0 { markers.last().value } else { "Avant-propos" }
    box(width: 100%, inset: (bottom: 4pt), stroke: (bottom: 0.45pt + c_rule))[
      #grid(
        columns: (auto, 1fr),
        column-gutter: 12pt,
        align(left)[
          #text(font: "JetBrains Mono", size: 6.7pt, fill: c_muted, tracking: 0.05em)[500 IDÉES DE BUSINESS · AFRIQUE 2027]
        ],
        align(right)[
          #text(font: ("Instrument Sans", "Source Sans Pro"), size: 7.4pt, weight: "bold", fill: c_emerald)[#sec]
        ]
      )
    ]
  },
  footer: context {
    let pg = counter(page).get().first()
    box(width: 100%, inset: (top: 4pt), stroke: (top: 0.45pt + c_rule))[
      #grid(
        columns: (1fr, auto),
        align(left)[
          #text(font: ("Instrument Sans", "Source Sans Pro"), size: 7.3pt, fill: c_muted)[Édition 2027 · Afrique Francophone · Guide Pratique & Catalogue]
        ],
        align(right)[
          #text(font: "JetBrains Mono", size: 7.5pt, weight: "bold", fill: c_emerald)[#pg]
        ]
      )
    ]
  },
)

// ============================================================================
// PAGE 2 : FAUX-TITRE, COLOPHON & MATRICE DES 3 BUDGETS
// ============================================================================
#set_sec("Avant-propos · Mode d'emploi & Budgets")
#metadata("garde") <p-garde>

#text(font: "JetBrains Mono", size: 7.4pt, weight: "bold", fill: c_gold_ink, tracking: 0.14em)[AVANT-PROPOS ÉDITORIAL · ÉDITION 2027]
#v(4pt)
#text(font: "Instrument Serif", size: 28pt, fill: c_deep)[#cfg.ebook_title]
#v(4pt)
#text(font: ("Instrument Sans", "Source Sans Pro"), size: 10.5pt, style: "italic", fill: c_ink2)[#cfg.ebook_subtitle]
#v(8pt)
#line(length: 40pt, stroke: 1.4pt + c_clay)
#v(12pt)

// Pull-quote monumentale
#box(
  width: 100%,
  fill: c_paper_alt,
  stroke: (left: 2.5pt + c_gold),
  inset: (x: 16pt, y: 11pt),
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 10pt,
    align: top,
    text(font: "Instrument Serif", size: 32pt, fill: c_gold, weight: "regular")[«],
    block[
      #text(font: "JetBrains Mono", size: 6.8pt, weight: "bold", fill: c_gold_ink, tracking: 0.12em)[LA PROMESSE DE CE LIVRE]
      #v(3pt)
      #text(font: "Instrument Serif", size: 14pt, style: "italic", fill: c_deep)[
        #cfg.promise_formula
      ]
    ]
  )
]

#section_subhead("CLÉ DE LECTURE", "Les 3 niveaux de budget utilisés dans ce catalogue")
#text(size: 9.2pt, fill: c_ink2)[
  Chaque idée parmi les 500 fiches indique le capital réaliste requis pour lancer une première version testable dès cette semaine en Afrique francophone :
]
#v(7pt)

#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 8pt,
  ..data.budget_guide.enumerate().map(((idx, b)) => {
    let accent = if idx == 0 { c_emerald } else if idx == 1 { c_gold } else { c_clay }
    let tint = if idx == 0 { c_paper_sage } else if idx == 1 { rgb("#FBF1DC") } else { c_paper_clay }
    grid.cell(
      fill: tint,
      stroke: (top: 2.2pt + accent, rest: 0.45pt + c_rule),
      inset: 9.5pt,
    )[
      #text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: accent, tracking: 0.08em)[NIVEAU 0#(idx + 1)]
      #v(3pt)
      #text(font: "Instrument Serif", size: 14pt, fill: c_deep)[#b.label]
      #v(2pt)
      #text(font: "JetBrains Mono", size: 7.1pt, weight: "bold", fill: c_ink)[#b.range]
      #v(4pt)
      #line(length: 100%, stroke: 0.4pt + c_rule)
      #v(4pt)
      #text(size: 8.0pt, fill: c_ink2)[#b.desc]
    ]
  })
)

#v(14pt)
#box(
  width: 100%,
  fill: c_paper_alt,
  stroke: 0.5pt + c_rule,
  radius: 2pt,
  inset: 12pt,
)[
  #text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_emerald, tracking: 0.12em)[ARCHITECTURE WORKBOOK OFFICIEL JOUR 2]
  #v(4pt)
  #text(size: 8.6pt, fill: c_ink)[
    Ce livre applique rigoureusement le plan en *5 parties + Conclusion* : *01 Introduction* · *02 Les 7 erreurs à éviter* · *03 Étape 1 (500 idées en 20 secteurs)* · *04 Étape 2 (Validation Express 48h par méthode VIN)* · *05 Étape 3 (Plan de lancement 7 jours)* · *Conclusion & engagement terrain*.
  ]
  #v(5pt)
  #text(size: 8.2pt, style: "italic", fill: c_ink2)[
    Astuce diffusion : les 10 premières pages de ce livre forment un extrait gratuit autonome idéal pour attirer tes premiers lecteurs.
  ]
]

#v(1fr)
#line(length: 100%, stroke: 0.5pt + c_rule)
#v(5pt)
#grid(
  columns: (1fr, auto),
  text(size: 8pt, fill: c_ink2)[*Éditeur / Auteur :* #cfg.author_name · *Date :* #cfg.date_creation],
  text(font: "JetBrains Mono", size: 7.5pt, fill: c_emerald)[#cfg.contact_whatsapp]
)

#pagebreak()

// ============================================================================
// PAGE 3 : SOMMAIRE ARCHITECTURAL CLICABLE (1 PAGE COMPLÈTE)
// ============================================================================
#set_sec("Sommaire architectural")
#metadata("sommaire") <p-sommaire>

#text(font: "JetBrains Mono", size: 7.0pt, weight: "bold", fill: c_gold_ink, tracking: 0.14em)[NAVIGATION COMPLÈTE DU GUIDE]
#v(1pt)
#text(font: "Instrument Serif", size: 22.5pt, fill: c_deep)[Sommaire architectural]
#v(3pt)
#line(length: 100%, stroke: 1.2pt + c_emerald)
#v(5pt)

#let toc_part_row(num, title, target_lbl) = context {
  let pg = counter(page).at(target_lbl).first()
  link(target_lbl)[
    #box(width: 100%, inset: (y: 3.0pt), stroke: (bottom: 0.45pt + c_rule))[
      #grid(
        columns: (24pt, 1fr, auto, auto),
        column-gutter: 6pt,
        align: horizon,
        text(font: "JetBrains Mono", size: 8.2pt, weight: "bold", fill: c_gold_ink)[#num],
        text(font: "Instrument Serif", size: 11.4pt, fill: c_deep)[#title],
        box(width: 34pt, align(right, line(length: 100%, stroke: (paint: c_rule, thickness: 0.6pt, dash: "dotted")))),
        box(fill: c_paper_sage, radius: 2pt, inset: (x: 4.5pt, y: 1pt),
          text(font: "JetBrains Mono", size: 7.6pt, weight: "bold", fill: c_emerald)[p. #pg]
        )
      )
    ]
  ]
}

#toc_part_row("00", "Mode d'emploi & Matrice des 3 budgets", <p-garde>)
#toc_part_row("01", "Introduction — Pourquoi entreprendre en Afrique en 2027", <p-01>)
#toc_part_row("02", "Erreurs à éviter — Les 7 pièges qui tuent 80 % des projets", <p-02>)
#toc_part_row("03", "Étape 1 — Catalogue des 500 idées rentables (20 secteurs)", <p-03>)
#toc_part_row("04", "Étape 2 — Validation Express en 48h (Méthode VIN & Grille /30)", <p-04>)
#toc_part_row("05", "Étape 3 — Plan d'action 7 jours, Scripts & 3 Enveloppes", <p-05>)
#toc_part_row("∞", "Conclusion — Fiche d'engagement 48h & À propos de l'auteur", <p-conc>)

#v(8pt)
#text(font: "JetBrains Mono", size: 7.0pt, weight: "bold", fill: c_emerald, tracking: 0.14em)[INDEX DES 20 SECTEURS · 25 IDÉES PAR SECTEUR (CLIQUER POUR ACCÉDER)]
#v(4pt)

#let sec_toc_cell(s) = context {
  let lbl = label("sec-" + str(s.num))
  let pg = counter(page).at(lbl).first()
  link(lbl)[
    #box(
      width: 100%,
      fill: if calc.rem(s.num, 2) == 1 { c_paper_alt } else { c_paper },
      stroke: (bottom: 0.45pt + c_rule),
      inset: (x: 5.5pt, y: 3.1pt),
    )[
      #grid(
        columns: (24pt, 1fr, auto),
        column-gutter: 5pt,
        align: top,
        text(font: "JetBrains Mono", size: 7.6pt, weight: "bold", fill: c_emerald)[S#if s.num < 10 [0] else []#s.num],
        block[
          #text(size: 7.85pt, weight: "bold", fill: c_ink)[#s.title]
          #v(0.5pt)
          #text(font: "JetBrains Mono", size: 6.2pt, fill: c_muted)[Idées #s.start_code–#s.end_code]
        ],
        text(font: "JetBrains Mono", size: 7.8pt, weight: "bold", fill: c_clay)[#pg]
      )
    ]
  ]
}

#grid(
  columns: (1fr, 1fr),
  column-gutter: 10pt,
  block(
    stroke: (top: 1.2pt + c_emerald),
  )[#for s in sectors.slice(0, 10) [#sec_toc_cell(s)]],
  block(
    stroke: (top: 1.2pt + c_gold),
  )[#for s in sectors.slice(10, 20) [#sec_toc_cell(s)]]
)

#pagebreak()

// ============================================================================
// PARTIE 01 : INTRODUCTION
// ============================================================================
#chapter_opener("01", data.part01.kicker, data.part01.title, data.part01.workbook_question, "p-01")
#v(9pt)

// Deck asymétrique éditorial
#grid(
  columns: (33%, 1fr),
  column-gutter: 13pt,
  box(
    width: 100%,
    stroke: (top: 1.5pt + c_gold, bottom: 0.5pt + c_rule),
    inset: (y: 7pt),
  )[
    #text(font: "Instrument Serif", size: 12.2pt, style: "italic", fill: c_emerald)[
      « Le vrai blocage n'est pas le manque de courage, mais l'absence de filtre adapté au terrain. »
    ]
  ],
  block[
    #text(size: 9.1pt, fill: c_ink)[#data.part01.lead]
    #v(4pt)
    #for pb in data.part01.problem_blocks [
      #text(size: 8.9pt, weight: "bold", fill: c_deep)[#pb.title]
      #v(1.5pt)
      #text(size: 8.4pt, fill: c_ink2)[#pb.body]
      #v(4pt)
    ]
  ]
)

#section_subhead("DYNAMIQUES 2027", "Les 5 méga-tendances qui créent les gagnants")

#grid(
  columns: (1fr, 1fr),
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..data.part01.trends.enumerate().map(((i, t)) => {
    let span_full = (i == 4)
    grid.cell(
      colspan: if span_full { 2 } else { 1 },
      fill: if span_full { c_paper_sage } else { c_paper_alt },
      stroke: (left: 2pt + if i < 2 { c_emerald } else { c_gold }),
      inset: (x: 9pt, y: 5.5pt),
    )[
      #grid(
        columns: (20pt, 1fr),
        column-gutter: 6pt,
        text(font: "Instrument Serif", size: 16pt, fill: c_gold_ink)[0#(i + 1)],
        block[
          #text(size: 8.5pt, weight: "bold", fill: c_deep)[#t.title]
          #v(1.5pt)
          #text(size: 7.9pt, fill: c_ink2)[#t.body]
        ]
      )
    ]
  })
)

#pagebreak()

#section_subhead("ORIENTATION RAPIDE", "Par quel secteur commencer selon ton profil ?")
#table(
  columns: (28%, 22%, 50%),
  stroke: (x: none, y: 0.45pt + c_rule),
  fill: (_, row) => if row == 0 { c_deep } else if calc.odd(row) { c_paper } else { c_paper_alt },
  inset: (x: 8pt, y: 7pt),
  table.header(
    text(font: "JetBrains Mono", size: 7.5pt, weight: "bold", fill: c_gold_hi)[PROFIL],
    text(font: "JetBrains Mono", size: 7.5pt, weight: "bold", fill: c_gold_hi)[BUDGET RÉALISTE],
    text(font: "JetBrains Mono", size: 7.5pt, weight: "bold", fill: c_gold_hi)[SECTEURS PRIORITAIRES],
  ),
  ..data.part01.profiles.map(p => (
    text(size: 8.7pt, weight: "bold", fill: c_deep)[#p.profile],
    text(font: "JetBrains Mono", size: 7.6pt, fill: c_clay_ink)[#p.budget],
    text(size: 8.5pt, fill: c_ink)[#p.sectors],
  )).flatten()
)

#v(14pt)
#box(
  width: 100%,
  fill: c_paper_sage,
  stroke: (left: 2.5pt + c_emerald, rest: 0.5pt + c_sage_rule),
  inset: 12pt,
)[
  #text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_emerald, tracking: 0.10em)[MODE D'EMPLOI EN 3 TEMPS (WORKBOOK JOUR 2)]
  #v(5pt)
  #grid(
    columns: (1fr, 1fr, 1fr),
    column-gutter: 10pt,
    block[
      #text(font: "Instrument Serif", size: 15pt, fill: c_emerald)[1. Filtrer]
      #v(2pt)
      #text(size: 8.3pt, fill: c_ink2)[Repère 3 idées dans tes secteurs prioritaires en Partie 03.]
    ],
    block[
      #text(font: "Instrument Serif", size: 15pt, fill: c_gold_ink)[2. Valider (48h)]
      #v(2pt)
      #text(size: 8.3pt, fill: c_ink2)[Applique le score VIN /30 en Partie 04 avant d'acheter du stock.]
    ],
    block[
      #text(font: "Instrument Serif", size: 15pt, fill: c_clay_ink)[3. Encaisser (7j)]
      #v(2pt)
      #text(size: 8.3pt, fill: c_ink2)[Exécute le plan Jour 1 à Jour 7 et signe ton engagement en Conclusion.]
    ],
  )
]

#pagebreak()

// ============================================================================
// PARTIE 02 : LES 7 ERREURS FATALES (SPREAD TABLEAU DIAGNOSTIC)
// ============================================================================
#chapter_opener("02", data.part02.kicker, data.part02.title, data.part02.workbook_question, "p-02")
#v(8pt)
#text(size: 9pt, style: "italic", fill: c_ink2)[#data.part02.intro]
#v(8pt)

#table(
  columns: (28pt, 46%, 1fr),
  stroke: (x: none, y: 0.5pt + c_rule),
  fill: (_, row) => if row == 0 { c_paper_alt } else if calc.odd(row) { c_paper } else { rgb("#F6F1E9") },
  inset: (x: 6pt, y: 6.2pt),
  table.header(
    text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_muted)[N°],
    text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_clay_ink)[PIÈGE FRÉQUENT & CONSÉQUENCE],
    text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_emerald)[RÉFLEXE GAGNANT 2027],
  ),
  ..data.part02.errors.enumerate().map(((idx, err)) => (
    align(top)[
      #text(font: "Instrument Serif", size: 17pt, fill: c_clay)[0#(idx + 1)]
    ],
    block[
      #text(size: 8.7pt, weight: "bold", fill: c_deep)[#err.title]
      #v(2pt)
      #text(size: 8pt, fill: c_clay_ink)[#err.consequence]
    ],
    block[
      #text(size: 8.2pt, weight: "bold", fill: c_emerald)[→ ]
      #text(size: 8.2pt, fill: c_ink)[#err.fix]
    ]
  )).flatten()
)

#pagebreak()

// ============================================================================
// PARTIE 03 : ÉTAPE 1 — LES 500 IDÉES EN 20 SECTEURS (1 SECTEUR = 1 PAGE OU 2?)
// ============================================================================
#chapter_opener(
  "03",
  "PARTIE 03 · ÉTAPE 1",
  "Les 500 idées de business classées en 20 secteurs porteurs",
  "Réponse à la section 03 du Workbook : Première action concrète — Explorer et sélectionner ton Top 3.",
  "p-03"
)
#v(10pt)
#box(
  width: 100%,
  fill: c_paper_alt,
  stroke: (left: 2.2pt + c_gold, rest: 0.45pt + c_rule),
  inset: (x: 12pt, y: 8pt),
)[
  #grid(
    columns: (auto, 1fr),
    column-gutter: 12pt,
    align: horizon,
    text(font: "JetBrains Mono", size: 8pt, weight: "bold", fill: c_gold_ink)[MÉTHODE 30 MIN],
    text(size: 8.5pt, fill: c_ink)[
      Ne lis pas les 500 fiches d'un trait : ouvre le *Sommaire* pour cibler 3 à 4 secteurs adaptés à ton budget, coche 5 idées qui résonnent immédiatement, puis soumets ton *Top 3* au test terrain de la *Partie 04*.
    ]
  )
]
#v(8pt)

#let idea_cell(it) = block(
  breakable: false,
  width: 100%,
  inset: (top: 4.8pt, bottom: 5.2pt, x: 2pt),
  stroke: (top: 0.45pt + c_rule),
)[
  #grid(
    columns: (auto, 1fr),
    align: horizon,
    text(font: "JetBrains Mono", size: 7.5pt, weight: "bold", fill: c_emerald)[#("#" + it.code)],
    align(right)[#pill_budget(it.budget)]
  )
  #v(2pt)
  #text(size: 8.9pt, weight: "bold", fill: c_deep)[#it.title]
  #v(1.5pt)
  #text(size: 8.0pt, fill: c_ink2)[#it.desc]
]

#let sector_masthead(s) = {
  set_sec("Secteur " + if s.num < 10 { "0" + str(s.num) } else { str(s.num) } + " · " + s.title)
  [#metadata(s.title)#label("sec-" + str(s.num))]
  let p_cnt = s.counts.Petit
  let m_cnt = s.counts.Moyen
  let st_cnt = s.counts.Structuré
  box(
    width: 100%,
    fill: c_paper_alt,
    stroke: (top: 2pt + c_emerald, bottom: 0.8pt + c_gold),
    inset: (x: 10pt, y: 7pt),
  )[
    #grid(
      columns: (38pt, 1fr, 118pt),
      column-gutter: 10pt,
      align: horizon,
      box(
        width: 38pt, height: 38pt, radius: 2pt, fill: c_deep,
        align(center + horizon)[
          #text(font: "Instrument Serif", size: 22pt, fill: c_gold_hi)[#if s.num < 10 [0] else []#s.num]
        ]
      ),
      block[
        #text(font: "JetBrains Mono", size: 6.8pt, weight: "bold", fill: c_clay_ink, tracking: 0.10em)[
          SECTEUR #if s.num < 10 [0] else []#s.num / 20  ·  IDÉES #("#" + s.start_code) – #("#" + s.end_code)
        ]
        #v(1.5pt)
        #text(font: "Instrument Serif", size: 16.5pt, fill: c_deep)[#s.title]
        #v(2pt)
        #text(size: 8.0pt, fill: c_ink2)[#s.intro]
      ],
      block[
        #text(font: "JetBrains Mono", size: 6.3pt, weight: "bold", fill: c_muted)[RÉPARTITION BUDGETS]
        #v(3pt)
        #box(width: 116pt, height: 6pt, radius: 2pt, clip: true)[
          #grid(
            columns: (p_cnt * 1fr, m_cnt * 1fr, st_cnt * 1fr),
            rect(width: 100%, height: 6pt, fill: c_emerald),
            rect(width: 100%, height: 6pt, fill: c_gold),
            rect(width: 100%, height: 6pt, fill: c_clay),
          )
        ]
        #v(3pt)
        #text(font: "JetBrains Mono", size: 6.3pt, fill: c_ink2)[
          #p_cnt Petit · #m_cnt Moy · #st_cnt Str
        ]
      ]
    )
  ]
}

// Secteur 1 : démarre sous le bandeau Partie 03 puis les suivants chacun sur une page dédiée ou flux aéré !
#for (idx_s, s) in sectors.enumerate() [
  #if idx_s > 0 { pagebreak() }
  #sector_masthead(s)
  #v(5pt)
  #grid(
    columns: (1fr, 1fr),
    column-gutter: 12pt,
    row-gutter: 1pt,
    ..s.ideas.map(it => idea_cell(it)),
    // 26e cellule : Mini-fiche d'action du secteur pour équilibrer la grille 2 colonnes !
    block(
      breakable: false,
      width: 100%,
      fill: c_paper_sage,
      stroke: (top: 1.5pt + c_emerald, rest: 0.4pt + c_sage_rule),
      inset: 7pt,
    )[
      #text(font: "JetBrains Mono", size: 6.8pt, weight: "bold", fill: c_emerald, tracking: 0.08em)[SÉLECTION SECTEUR #if s.num < 10 [0] else []#s.num]
      #v(3pt)
      #text(size: 7.7pt, fill: c_ink)[Note tes 2 pépites favorites ici avant de passer à la validation 48h :]
      #v(4pt)
      #text(font: "JetBrains Mono", size: 7.2pt, fill: c_ink2)[
        #checkbox() N° \_\_\_\_   #h(8pt) #checkbox() N° \_\_\_\_
      ]
    ]
  )
]

#pagebreak()

// ============================================================================
// PARTIE 04 : ÉTAPE 2 — VALIDATION EXPRESS 48H
// ============================================================================
#chapter_opener("04", data.part04.kicker, data.part04.title, data.part04.workbook_question, "p-04")
#v(8pt)
#text(size: 9.2pt, fill: c_ink)[#data.part04.intro]

#section_subhead("MÉTHODE VIN", "Les 3 filtres impératifs avant d'investir")
#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 8pt,
  ..data.part04.vin.enumerate().map(((i, vin_it)) => {
    let acc = if i == 0 { c_emerald } else if i == 1 { c_gold } else { c_clay }
    box(
      width: 100%,
      height: 82pt,
      fill: c_paper_alt,
      stroke: (top: 2pt + acc, rest: 0.45pt + c_rule),
      inset: 9pt,
    )[
      #text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: acc)[#vin_it.title]
      #v(4pt)
      #text(size: 8.1pt, fill: c_ink2)[#vin_it.desc]
    ]
  })
)

#section_subhead("CHRONOGRAMME", "Le protocole terrain en 48 heures chrono")
#for st in data.part04.steps_48h [
  #box(width: 100%, inset: (y: 3.5pt), stroke: (bottom: 0.4pt + c_rule))[
    #grid(
      columns: (132pt, 1fr),
      column-gutter: 8pt,
      text(font: "JetBrains Mono", size: 7.4pt, weight: "bold", fill: c_emerald)[#st.title],
      text(size: 8.5pt, fill: c_ink)[#st.desc],
    )
  ]
]

#pagebreak()

#section_subhead("MATRICE COMPARATIVE", "Grille de notation de tes 3 idées finalistes (/30)")
#table(
  columns: (1fr, 64pt, 64pt, 64pt),
  stroke: (x: 0.4pt + c_rule, y: 0.45pt + c_rule),
  fill: (_, row) => if row == 0 { c_deep } else if row == 7 { c_paper_sage } else if calc.odd(row) { c_paper } else { c_paper_alt },
  inset: (x: 7pt, y: 6pt),
  table.header(
    text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_gold_hi)[CRITÈRE (NOTE DE 1 À 5)],
    align(center, text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_gold_hi)[IDÉE A]),
    align(center, text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_gold_hi)[IDÉE B]),
    align(center, text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_gold_hi)[IDÉE C]),
  ),
  ..data.part04.scoring.map(c => (
    block[
      #text(size: 8.5pt, weight: "bold", fill: c_deep)[#c.title]
      #v(1.5pt)
      #text(size: 7.8pt, fill: c_ink2)[#c.desc]
    ],
    align(center + horizon, text(font: "JetBrains Mono", size: 8.5pt, fill: c_muted)[\_\_\_ / 5]),
    align(center + horizon, text(font: "JetBrains Mono", size: 8.5pt, fill: c_muted)[\_\_\_ / 5]),
    align(center + horizon, text(font: "JetBrains Mono", size: 8.5pt, fill: c_muted)[\_\_\_ / 5]),
  )).flatten(),
  text(size: 8.6pt, weight: "bold", fill: c_emerald)[TOTAL FINAL (/30) — Garde uniquement les idées ≥ 20/30],
  align(center + horizon, text(font: "JetBrains Mono", size: 8.5pt, weight: "bold", fill: c_emerald)[\_\_\_ / 30]),
  align(center + horizon, text(font: "JetBrains Mono", size: 8.5pt, weight: "bold", fill: c_emerald)[\_\_\_ / 30]),
  align(center + horizon, text(font: "JetBrains Mono", size: 8.5pt, weight: "bold", fill: c_emerald)[\_\_\_ / 30]),
)

#v(12pt)
#box(
  width: 100%,
  fill: rgb("#FBF1DC"),
  stroke: (left: 2.5pt + c_gold, rest: 0.45pt + rgb("#E4C98C")),
  inset: 12pt,
)[
  #text(font: "JetBrains Mono", size: 7.2pt, weight: "bold", fill: c_gold_ink, tracking: 0.08em)[CAS PRATIQUE COMPLÉTÉ · IDÉE \#002]
  #v(3pt)
  #text(font: "Instrument Serif", size: 14pt, fill: c_deep)[#data.part04.example_title]
  #v(4pt)
  #for ln in data.part04.example_lines [
    #text(size: 8.3pt, fill: c_ink)[#ln]
    #v(2.5pt)
  ]
]

#pagebreak()

// ============================================================================
// PARTIE 05 : ÉTAPE 3 — PLAN DE LANCEMENT 7 JOURS
// ============================================================================
#chapter_opener("05", data.part05.kicker, data.part05.title, data.part05.workbook_question, "p-05")
#v(8pt)
#text(size: 9.1pt, fill: c_ink)[#data.part05.intro]

#section_subhead("FEUILLE DE ROUTE", "Chronologie d'exécution : Jour 1 à Jour 7")
#for (idx, d) in data.part05.days.enumerate() [
  #box(
    width: 100%,
    fill: if calc.even(idx) { c_paper_alt } else { c_paper },
    stroke: (left: 2pt + if idx < 3 { c_emerald } else if idx < 6 { c_gold } else { c_clay }, bottom: 0.4pt + c_rule),
    inset: (x: 9pt, y: 5.5pt),
  )[
    #grid(
      columns: (52pt, 1fr),
      column-gutter: 8pt,
      align: top,
      text(font: "JetBrains Mono", size: 8.2pt, weight: "bold", fill: c_emerald)[#upper(d.day)],
      block[
        #text(size: 8.8pt, weight: "bold", fill: c_deep)[#d.title]
        #v(1.5pt)
        #text(size: 8.1pt, fill: c_ink2)[#d.desc]
      ]
    )
  ]
]

#pagebreak()

#section_subhead("SCRIPTS DE CONVERSION", "3 messages prêts à copier-coller sur WhatsApp & Facebook")
#for sc in data.part05.scripts [
  #box(
    width: 100%,
    fill: c_paper_alt,
    stroke: (left: 2.2pt + c_gold, rest: 0.45pt + c_rule),
    inset: (x: 11pt, y: 8pt),
  )[
    #text(font: "JetBrains Mono", size: 7.3pt, weight: "bold", fill: c_gold_ink)[#sc.title]
    #v(3pt)
    #text(size: 8.4pt, style: "italic", fill: c_ink)[#sc.body]
  ]
  #v(6pt)
]

#section_subhead("GESTION DU CASH", "Fixer le prix juste & Règle des 3 Enveloppes")
#for pf in data.part05.pricing [
  #text(size: 8.4pt, fill: c_ink)[#pf]
  #v(2pt)
]
#v(6pt)

// Barre visuelle des 3 enveloppes (50% / 30% / 20%)
#box(width: 100%, height: 14pt, radius: 2pt, clip: true)[
  #grid(
    columns: (50%, 30%, 20%),
    rect(width: 100%, height: 14pt, fill: c_emerald, align(center + horizon, text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_paper)[50 % STOCK])),
    rect(width: 100%, height: 14pt, fill: c_gold, align(center + horizon, text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_deep)[30 % CHARGES])),
    rect(width: 100%, height: 14pt, fill: c_clay, align(center + horizon, text(font: "JetBrains Mono", size: 7pt, weight: "bold", fill: c_paper)[20 % TOI])),
  )
]
#v(7pt)

#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 8pt,
  ..data.part05.envelopes.enumerate().map(((i, env)) => {
    let acc = if i == 0 { c_emerald } else if i == 1 { c_gold } else { c_clay }
    box(
      width: 100%,
      height: 82pt,
      fill: c_paper_sage,
      stroke: (top: 2pt + acc, rest: 0.45pt + c_sage_rule),
      inset: 8pt,
    )[
      #text(size: 8.2pt, weight: "bold", fill: c_deep)[#env.title]
      #v(3pt)
      #text(size: 7.7pt, fill: c_ink2)[#env.desc]
    ]
  })
)

#pagebreak()

// ============================================================================
// CONCLUSION & FICHE D'ENGAGEMENT TERRAIN
// ============================================================================
#chapter_opener("∞", data.conclusion.kicker, data.conclusion.title, data.conclusion.workbook_question, "p-conc")
#v(5pt)
#text(size: 8.7pt, fill: c_ink)[#data.conclusion.message]
#v(5pt)

#box(
  width: 100%,
  fill: rgb("#FBF1DC"),
  stroke: (left: 2.5pt + c_gold),
  inset: (x: 11pt, y: 5.5pt),
)[
  #text(font: "JetBrains Mono", size: 6.6pt, weight: "bold", fill: c_gold_ink, tracking: 0.12em)[MANTRA DU WORKBOOK JOUR 2]
  #v(1.5pt)
  #text(font: "Instrument Serif", size: 11.6pt, style: "italic", fill: c_deep)[#data.conclusion.mantra]
]

#v(5pt)
#text(font: "JetBrains Mono", size: 6.8pt, weight: "bold", fill: c_gold_ink, tracking: 0.12em)[PASSAGE À L'ACTION · TES 3 PROCHAINS PAS]
#v(2pt)
#line(length: 100%, stroke: 0.45pt + c_rule)
#v(3pt)
#for ns in data.conclusion.next_steps [
  #text(size: 8.2pt, fill: c_ink)[#ns]
  #v(1.5pt)
]

#v(4pt)
#text(font: "JetBrains Mono", size: 6.8pt, weight: "bold", fill: c_emerald, tracking: 0.12em)[MA FICHE D'ENGAGEMENT TERRAIN (À COMPLÉTER MAINTENANT)]
#v(2pt)
#box(
  width: 100%,
  fill: c_paper_alt,
  stroke: 0.7pt + c_gold,
  radius: 2pt,
  inset: (x: 10pt, y: 4pt),
)[
  #for (idx_a, ln) in data.conclusion.action_sheet.enumerate() [
    #box(
      width: 100%,
      inset: (y: 2.2pt),
      stroke: if idx_a < data.conclusion.action_sheet.len() - 1 { (bottom: 0.4pt + c_rule) } else { none },
    )[
      #checkbox(accent: c_emerald) #h(6pt) #text(size: 7.9pt, fill: c_ink)[#ln]
    ]
  ]
]

#v(6pt)
#box(
  width: 100%,
  fill: c_deep,
  radius: 3pt,
  inset: (x: 11pt, y: 8pt),
  stroke: (top: 2pt + c_gold),
)[
  #text(font: "JetBrains Mono", size: 6.6pt, weight: "bold", fill: c_gold_hi, tracking: 0.12em)[À PROPOS DE L'AUTEUR]
  #v(1.5pt)
  #text(font: "Instrument Serif", size: 14.5pt, fill: c_paper)[#cfg.author_name]
  #h(8pt)
  #text(size: 8.0pt, fill: c_gold_hi)[· #cfg.author_role]
  #v(2pt)
  #text(size: 7.8pt, fill: rgb("#DCE5E0"))[#cfg.author_bio]
  #v(4pt)
  #line(length: 100%, stroke: 0.4pt + rgb("#C5881E55"))
  #v(3pt)
  #text(font: "JetBrains Mono", size: 7.0pt, fill: c_gold_hi)[
    WhatsApp : #cfg.contact_whatsapp  ·  Réseaux : #cfg.contact_social  ·  Email : #cfg.contact_email
  ]
]
