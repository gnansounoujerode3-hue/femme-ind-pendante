# -*- coding: utf-8 -*-
"""Générateur éditorial Typst 0.15 des livrables PDF et exports Markdown :
- 500-Idees-de-Business-a-Lancer-en-Afrique-en-2027.pdf
- Workbook-Jour-2-Rempli-500-Idees-Business-Afrique-2027.pdf
Système éditorial sobre « Savane Sobre & Papier Munken » (.agents/skills/).
"""

import json
from pathlib import Path

import pymupdf
import typst

from ebook_content import (
    BUDGET_GUIDE,
    CONCLUSION_CONTENT,
    PART_01_INTRO,
    PART_02_ERRORS,
    PART_04_VALIDATION,
    PART_05_LAUNCH,
    get_workbook_pages_data,
)
from ideas_500 import get_numbered_sectors

ROOT_DIR = Path(__file__).resolve().parent.parent
SOURCE_DIR = Path(__file__).resolve().parent

OUT_EBOOK_PDF = ROOT_DIR / "500-Idees-de-Business-a-Lancer-en-Afrique-en-2027.pdf"
OUT_WORKBOOK_PDF = ROOT_DIR / "Workbook-Jour-2-Rempli-500-Idees-Business-Afrique-2027.pdf"
OUT_EBOOK_MD = SOURCE_DIR / "ebook-500-idees-business-afrique-2027.md"
OUT_WORKBOOK_MD = SOURCE_DIR / "workbook-jour-2-rempli.md"
CONFIG_PATH = SOURCE_DIR / "author_config.json"
DATA_JSON_PATH = SOURCE_DIR / "ebook_data.json"
EBOOK_TYP_PATH = SOURCE_DIR / "ebook.typ"
WORKBOOK_TYP_PATH = SOURCE_DIR / "workbook.typ"

FONT_PATHS = [
    str(ROOT_DIR / ".agents" / "skills" / "canvas-design" / "canvas-fonts"),
]


EBOOK_TYP = r'''
#let data = json("ebook_data.json")
#let cfg = data.config
#let sectors = data.sectors

// Palette éditoriale sobre — Papier Munken, encre charbon, vert forêt profond
#let c_paper    = rgb("#FCFBF8")
#let c_tint     = rgb("#F5F2EC")
#let c_ink      = rgb("#161B19")
#let c_ink2     = rgb("#4B5450")
#let c_muted    = rgb("#78807C")
#let c_accent   = rgb("#103E33")
#let c_deep     = rgb("#07221B")
#let c_ocre     = rgb("#8A5808")
#let c_clay     = rgb("#8E3C1D")
#let c_gold_hi  = rgb("#E9AF43")
#let c_rule     = rgb("#DDD6CA")
#let c_hair     = rgb("#EAE4DA")

#let set_sec(name) = [#metadata(name)<sec-marker>]

// Case à cocher dessinée vectoriellement (zéro glyphe fallback ni emoji)
#let checkbox(checked: false, accent: c_accent) = box(
  width: 8pt, height: 8pt,
  fill: if checked { accent } else { none },
  stroke: 0.7pt + accent,
  baseline: 1pt,
  if checked {
    place(center + horizon)[
      #curve(
        stroke: (paint: c_paper, thickness: 1.1pt, cap: "round", join: "round"),
        curve.move((1.4pt, 4.1pt)),
        curve.line((3.2pt, 5.9pt)),
        curve.line((6.6pt, 2.2pt)),
      )
    ]
  }
)

// Indication discrète du budget sans pilule ni boîte répétitive
#let budget_label(tier) = {
  let col = if tier == "Petit" { c_accent } else if tier == "Moyen" { c_ocre } else { c_clay }
  let lbl = if tier == "Petit" { "Petit budget" } else if tier == "Moyen" { "Budget moyen" } else { "Structuré" }
  text(size: 7.3pt, weight: "semibold", fill: col)[#lbl]
}

// Ouverture de chapitre authentique de maison d'édition (sur fond papier pur)
#let chapter_opener(kicker, title, epigraph, lbl_name) = {
  set_sec(kicker)
  [#metadata(kicker)#label(lbl_name)]
  block(width: 100%, below: 11pt)[
    #text(size: 8.3pt, weight: "semibold", fill: c_accent, tracking: 0.06em)[#kicker]
    #v(4pt)
    #text(font: "Instrument Serif", size: 24.5pt, fill: c_ink, weight: "regular")[#title]
    #v(7pt)
    #line(length: 44pt, stroke: 0.9pt + c_accent)
    #v(6pt)
    #text(size: 9.2pt, style: "italic", fill: c_ink2)[#epigraph]
    #v(9pt)
    #line(length: 100%, stroke: 0.4pt + c_rule)
  ]
}

// Intertitre sans sur-titre mécanique au-dessus
#let section_head(title) = {
  v(11pt)
  block(breakable: false, sticky: true, below: 6pt)[
    #text(font: "Instrument Serif", size: 15.5pt, fill: c_ink)[#title]
    #v(3pt)
    #line(length: 100%, stroke: 0.45pt + c_rule)
  ]
}

#set document(
  title: cfg.ebook_title,
  author: cfg.author_name,
)

#set text(
  font: "Instrument Sans",
  size: 9.3pt,
  fill: c_ink,
  lang: "fr",
  region: "FR",
)

#set par(leading: 0.64em, justify: false)

// ============================================================================
// PAGE 1 : COUVERTURE D'ÉDITION ÉPURÉE (SANS CADRE NI WIDGETS)
// ============================================================================
#page(
  paper: "a4",
  margin: 0mm,
  fill: c_deep,
  header: none,
  footer: none,
)[
  #place(top + left, image("cover_art.png", width: 210mm, height: 297mm, fit: "cover"))

  // Dégradés doux assurant un contraste naturel du texte sur l'illustration
  #place(top + left, rect(
    width: 210mm, height: 126mm,
    fill: gradient.linear(
      rgb("#061E18F5"), rgb("#061E18E0"), rgb("#061E1894"), rgb("#061E1800"),
      angle: 90deg,
    )
  ))
  #place(bottom + left, rect(
    width: 210mm, height: 84mm,
    fill: gradient.linear(
      rgb("#061E1800"), rgb("#061E18AD"), rgb("#061E18EB"), rgb("#061E18F5"),
      angle: 90deg,
    )
  ))

  // En-tête éditorial léger en tête de couverture
  #place(top + left, dx: 20mm, dy: 14mm, box(width: 170mm)[
    #text(size: 8.2pt, fill: rgb("#DCE3DF"), tracking: 0.14em)[#upper(cfg.edition)]
  ])

  // Titre sculptural avec hiérarchie pure, entièrement au-dessus des rayons solaires
  #place(top + left, dx: 20mm, dy: 23mm, box(width: 170mm)[
    #text(font: "Instrument Serif", size: 40pt, fill: rgb("#FAF7F2"), tracking: -0.01em)[
      500 Idées de Business
    ]
    #v(-4pt)
    #text(font: "Instrument Serif", size: 30pt, fill: c_gold_hi, tracking: -0.01em)[
      à lancer en Afrique en 2027
    ]
    #v(7pt)
    #line(length: 40pt, stroke: 0.9pt + c_gold_hi)
    #v(6pt)
    #text(size: 10.0pt, fill: rgb("#F3EFE6"))[#cfg.ebook_subtitle]
  ])

  // Zone inférieure : promesse librement posée + mention auteur sobre
  #place(bottom + left, dx: 20mm, dy: -16mm, box(width: 170mm)[
    #text(font: "Instrument Serif", size: 13.8pt, style: "italic", fill: rgb("#FAF7F2"))[
      « #cfg.promise_formula »
    ]
    #v(12pt)
    #line(length: 100%, stroke: 0.4pt + rgb("#FAF7F244"))
    #v(7pt)
    #grid(
      columns: (1fr, auto),
      text(size: 9.2pt, weight: "semibold", fill: rgb("#FAF7F2"))[#cfg.author_name],
      text(size: 8.4pt, fill: rgb("#D5DED9"))[Vingt secteurs · Cinq cents fiches pratiques]
    )
  ])
]

// ============================================================================
// PAGES INTÉRIEURES : PAPIER MUNKEN, FOLIOS DISCRETS, EN-TÊTE COURANT SOBRE
// ============================================================================
#set page(
  paper: "a4",
  fill: c_paper,
  margin: (top: 21mm, bottom: 20mm, left: 17mm, right: 17mm),
  header: context {
    let pg = here().page()
    let markers = query(selector(<sec-marker>)).filter(m => m.location().page() <= pg)
    let sec = if markers.len() > 0 { markers.last().value } else { "Avant-propos" }
    box(width: 100%, inset: (bottom: 5pt), stroke: (bottom: 0.35pt + c_rule))[
      #grid(
        columns: (auto, 1fr),
        column-gutter: 12pt,
        align(left)[
          #text(size: 7.6pt, fill: c_muted)[500 Idées de Business à Lancer en Afrique en 2027]
        ],
        align(right)[
          #text(size: 7.6pt, weight: "semibold", fill: c_accent)[#sec]
        ]
      )
    ]
  },
  footer: context {
    let pg = counter(page).get().first()
    box(width: 100%, inset: (top: 5pt), stroke: (top: 0.35pt + c_rule))[
      #grid(
        columns: (1fr, auto),
        align(left)[
          #text(size: 7.4pt, fill: c_muted)[Guide pratique & répertoire · Afrique francophone]
        ],
        align(right)[
          #text(size: 8.2pt, weight: "semibold", fill: c_ink)[#pg]
        ]
      )
    ]
  },
)

// ============================================================================
// PAGE 2 : PAGE DE TITRE INTÉRIEURE, AVANT-PROPOS & NIVEAUX DE BUDGET
// ============================================================================
#set_sec("Avant-propos")
#metadata("garde") <p-garde>

#v(4pt)
#text(font: "Instrument Serif", size: 28pt, fill: c_ink)[#cfg.ebook_title]
#v(6pt)
#text(size: 10.4pt, style: "italic", fill: c_ink2)[#cfg.ebook_subtitle]
#v(11pt)
#line(length: 44pt, stroke: 0.9pt + c_accent)
#v(16pt)

// Exergue ouverte (zéro boîte fermée ni fond coloré)
#box(
  width: 100%,
  stroke: (left: 1pt + c_accent),
  inset: (left: 13pt, y: 4pt),
)[
  #text(font: "Instrument Serif", size: 14.2pt, style: "italic", fill: c_ink)[
    « #cfg.promise_formula »
  ]
]

#section_head("Les trois niveaux de budget utilisés dans ce catalogue")
#text(size: 9.2pt, fill: c_ink2)[
  Chaque fiche du répertoire précise le capital réaliste requis pour lancer une première version vérifiable sur le terrain dès cette semaine :
]
#v(10pt)

#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 12pt,
  ..data.budget_guide.enumerate().map(((idx, b)) => {
    let accent = if idx == 0 { c_accent } else if idx == 1 { c_ocre } else { c_clay }
    grid.cell(
      stroke: (top: 1.2pt + accent, bottom: 0.35pt + c_rule),
      inset: (top: 8pt, bottom: 9pt),
    )[
      #text(size: 7.4pt, weight: "semibold", fill: accent)[Niveau 0#(idx + 1)]
      #v(2pt)
      #text(font: "Instrument Serif", size: 15pt, fill: c_ink)[#b.label]
      #v(3pt)
      #text(size: 8.0pt, weight: "semibold", fill: c_ink)[#b.range]
      #v(5pt)
      #text(size: 8.2pt, fill: c_ink2)[#b.desc]
    ]
  })
)

#section_head("Comment lire et exploiter cet ouvrage")
#text(size: 9.0pt, fill: c_ink)[
  Ce livre suit une progression volontairement pragmatique en cinq parties : comprendre pourquoi 2027 favorise les lancements légers (*Première partie*), éviter les sept fautes qui immobilisent les débutants (*Deuxième partie*), explorer vingt secteurs regroupant cinq cents activités concrètes (*Troisième partie*), vérifier la demande réelle en quarante-huit heures sans engager de stock (*Quatrième partie*) puis encaisser ses premiers clients en sept jours (*Cinquième partie*).
]

#v(1fr)
#line(length: 100%, stroke: 0.45pt + c_rule)
#v(6pt)
#grid(
  columns: (1fr, auto),
  text(size: 8.1pt, fill: c_ink2)[*Édition :* #cfg.author_name · #cfg.date_creation],
  text(size: 8.1pt, fill: c_accent)[#cfg.contact_email]
)

#pagebreak()

// ============================================================================
// PAGE 3 : SOMMAIRE ÉDITORIAL CLICABLE (1 PAGE)
// ============================================================================
#set_sec("Sommaire")
#metadata("sommaire") <p-sommaire>

#text(font: "Instrument Serif", size: 24pt, fill: c_ink)[Sommaire]
#v(5pt)
#line(length: 100%, stroke: 0.9pt + c_ink)
#v(8pt)

#let toc_part_row(num, title, target_lbl) = context {
  let pg = counter(page).at(target_lbl).first()
  link(target_lbl)[
    #box(width: 100%, inset: (y: 3.4pt), stroke: (bottom: 0.35pt + c_hair))[
      #grid(
        columns: (28pt, 1fr, 44pt, 20pt),
        column-gutter: 6pt,
        align: horizon,
        text(size: 8.2pt, weight: "semibold", fill: c_accent)[#num],
        text(font: "Instrument Serif", size: 11.6pt, fill: c_ink)[#title],
        line(length: 100%, stroke: (paint: c_rule, thickness: 0.5pt, dash: "dotted")),
        align(right, text(size: 8.6pt, weight: "semibold", fill: c_ink)[#pg])
      )
    ]
  ]
}

#toc_part_row("00", "Avant-propos et niveaux de budget", <p-garde>)
#toc_part_row("01", "Première partie · Pourquoi entreprendre en Afrique en 2027", <p-01>)
#toc_part_row("02", "Deuxième partie · Les sept erreurs à éviter", <p-02>)
#toc_part_row("03", "Troisième partie · Catalogue des 500 idées (20 secteurs)", <p-03>)
#toc_part_row("04", "Quatrième partie · Validation express en 48 heures (Méthode VIN)", <p-04>)
#toc_part_row("05", "Cinquième partie · Plan d'action en 7 jours et gestion du cash", <p-05>)
#toc_part_row("Fin", "Conclusion · Fiche d'engagement et à propos de l'auteur", <p-conc>)

#v(12pt)
#text(font: "Instrument Serif", size: 14pt, fill: c_ink)[Répertoire des vingt secteurs]
#h(8pt)
#text(size: 8.1pt, style: "italic", fill: c_muted)[(25 idées par secteur · cliquer sur un secteur pour y accéder)]
#v(6pt)

#let sec_toc_cell(s) = context {
  let lbl = label("sec-" + str(s.num))
  let pg = counter(page).at(lbl).first()
  link(lbl)[
    #box(
      width: 100%,
      stroke: (bottom: 0.35pt + c_hair),
      inset: (y: 3.2pt),
    )[
      #grid(
        columns: (20pt, 1fr, auto),
        column-gutter: 6pt,
        align: top,
        text(size: 8.0pt, weight: "semibold", fill: c_accent)[#if s.num < 10 [0] else []#s.num],
        block[
          #text(size: 7.95pt, weight: "semibold", fill: c_ink)[#s.title]
          #v(0.5pt)
          #text(size: 7.0pt, fill: c_muted)[Idées #s.start_code à #s.end_code]
        ],
        text(size: 8.1pt, weight: "semibold", fill: c_ink2)[#pg]
      )
    ]
  ]
}

#grid(
  columns: (1fr, 1fr),
  column-gutter: 16pt,
  block(stroke: (top: 0.8pt + c_accent))[#for s in sectors.slice(0, 10) [#sec_toc_cell(s)]],
  block(stroke: (top: 0.8pt + c_accent))[#for s in sectors.slice(10, 20) [#sec_toc_cell(s)]]
)

#pagebreak()

// ============================================================================
// PARTIE 01 : INTRODUCTION
// ============================================================================
#chapter_opener(data.part01.kicker, data.part01.title, data.part01.epigraph, "p-01")

#grid(
  columns: (32%, 1fr),
  column-gutter: 16pt,
  box(
    width: 100%,
    stroke: (top: 0.9pt + c_accent),
    inset: (top: 8pt),
  )[
    #text(font: "Instrument Serif", size: 13pt, style: "italic", fill: c_accent)[
      « L'envie d'entreprendre est immense ; ce qui manque le plus souvent, c'est un filtre adapté aux réalités du terrain. »
    ]
  ],
  block[
    #text(size: 9.1pt, fill: c_ink)[#data.part01.lead]
    #v(6pt)
    #for pb in data.part01.problem_blocks [
      #text(size: 9.0pt, weight: "bold", fill: c_ink)[#pb.title]
      #v(2pt)
      #text(size: 8.6pt, fill: c_ink2)[#pb.body]
      #v(5pt)
    ]
  ]
)

#section_head("Cinq dynamiques porteuses en 2027")

#grid(
  columns: (1fr, 1fr),
  column-gutter: 16pt,
  row-gutter: 6pt,
  ..data.part01.trends.enumerate().map(((i, t)) => {
    let span_full = (i == 4)
    grid.cell(
      colspan: if span_full { 2 } else { 1 },
      stroke: (bottom: 0.35pt + c_rule),
      inset: (top: 4pt, bottom: 7pt),
    )[
      #grid(
        columns: (22pt, 1fr),
        column-gutter: 6pt,
        text(font: "Instrument Serif", size: 17pt, fill: c_accent)[0#(i + 1)],
        block[
          #text(size: 8.8pt, weight: "bold", fill: c_ink)[#t.title]
          #v(2pt)
          #text(size: 8.2pt, fill: c_ink2)[#t.body]
        ]
      )
    ]
  })
)

#pagebreak()

#section_head("Par quel secteur commencer selon ton profil ?")
#table(
  columns: (28%, 25%, 47%),
  stroke: (x, y) => (bottom: if y == 0 { 0.9pt + c_ink } else { 0.35pt + c_hair }),
  fill: none,
  inset: (x: 4pt, y: 8pt),
  table.header(
    text(size: 8.0pt, weight: "bold", fill: c_accent)[Profil],
    text(size: 8.0pt, weight: "bold", fill: c_accent)[Budget réaliste],
    text(size: 8.0pt, weight: "bold", fill: c_accent)[Secteurs prioritaires],
  ),
  ..data.part01.profiles.map(p => (
    text(size: 8.8pt, weight: "semibold", fill: c_ink)[#p.profile],
    text(size: 8.3pt, fill: c_clay)[#p.budget],
    text(size: 8.6pt, fill: c_ink2)[#p.sectors],
  )).flatten()
)

#v(18pt)
#box(
  width: 100%,
  stroke: (top: 0.8pt + c_accent, bottom: 0.45pt + c_rule),
  inset: (y: 12pt),
)[
  #text(font: "Instrument Serif", size: 14.5pt, fill: c_ink)[La progression recommandée en trois étapes]
  #v(8pt)
  #grid(
    columns: (1fr, 1fr, 1fr),
    column-gutter: 14pt,
    block[
      #text(size: 8.6pt, weight: "bold", fill: c_accent)[1. Filtrer]
      #v(2pt)
      #text(size: 8.3pt, fill: c_ink2)[Repère trois idées dans tes secteurs prioritaires au fil du catalogue.]
    ],
    block[
      #text(size: 8.6pt, weight: "bold", fill: c_ocre)[2. Valider en 48 heures]
      #v(2pt)
      #text(size: 8.3pt, fill: c_ink2)[Applique le score sur 30 points avant tout achat de stock ou de matériel.]
    ],
    block[
      #text(size: 8.6pt, weight: "bold", fill: c_clay)[3. Encaisser en 7 jours]
      #v(2pt)
      #text(size: 8.3pt, fill: c_ink2)[Suis le plan jour par jour et signe ton engagement écrit en fin d'ouvrage.]
    ],
  )
]

#pagebreak()

// ============================================================================
// PARTIE 02 : LES SEPT ERREURS
// ============================================================================
#chapter_opener(data.part02.kicker, data.part02.title, data.part02.epigraph, "p-02")
#text(size: 9.1pt, fill: c_ink)[#data.part02.intro]
#v(8pt)

#table(
  columns: (24pt, 46%, 1fr),
  stroke: (x, y) => (bottom: if y == 0 { 0.9pt + c_ink } else { 0.35pt + c_hair }),
  fill: none,
  inset: (x: 4pt, y: 7.5pt),
  table.header(
    text(size: 7.8pt, weight: "bold", fill: c_muted)[N°],
    text(size: 7.8pt, weight: "bold", fill: c_clay)[Piège fréquent & conséquence],
    text(size: 7.8pt, weight: "bold", fill: c_accent)[Alternative rentable],
  ),
  ..data.part02.errors.enumerate().map(((idx, err)) => (
    align(top)[
      #text(font: "Instrument Serif", size: 16pt, fill: c_clay)[0#(idx + 1)]
    ],
    block[
      #text(size: 8.8pt, weight: "bold", fill: c_ink)[#err.title]
      #v(2pt)
      #text(size: 8.1pt, fill: c_ink2)[#err.consequence]
    ],
    text(size: 8.3pt, fill: c_ink)[#err.fix]
  )).flatten()
)

#pagebreak()

// ============================================================================
// PARTIE 03 : CATALOGUE DES 500 IDÉES EN 20 SECTEURS
// ============================================================================
#chapter_opener(
  "Troisième partie · Catalogue des 500 idées",
  "Cinq cents idées classées en vingt secteurs porteurs",
  "Parcours le sommaire pour cibler trois ou quatre secteurs adaptés à ton budget, retiens cinq pistes, puis soumets ton Top 3 au test des 48 heures.",
  "p-03"
)

#let idea_cell(it) = block(
  breakable: false,
  width: 100%,
  inset: (top: 5.8pt, bottom: 6.4pt),
  stroke: (top: 0.35pt + c_hair),
)[
  #grid(
    columns: (auto, 1fr),
    align: horizon,
    text(size: 7.6pt, weight: "bold", fill: c_accent)[#("#" + it.code)],
    align(right)[#budget_label(it.budget)]
  )
  #v(2.2pt)
  #text(size: 8.9pt, weight: "semibold", fill: c_ink)[#it.title]
  #v(1.8pt)
  #text(size: 8.0pt, fill: c_ink2)[#it.desc]
]

#let sector_masthead(s) = {
  set_sec("Secteur " + if s.num < 10 { "0" + str(s.num) } else { str(s.num) } + " — " + s.title)
  [#metadata(s.title)#label("sec-" + str(s.num))]
  let p_cnt = s.counts.Petit
  let m_cnt = s.counts.Moyen
  let st_cnt = s.counts.Structuré
  box(
    width: 100%,
    stroke: (top: 1.1pt + c_accent, bottom: 0.45pt + c_rule),
    inset: (top: 9pt, bottom: 9pt),
  )[
    #grid(
      columns: (32pt, 1fr),
      column-gutter: 10pt,
      align: top,
      text(font: "Instrument Serif", size: 28pt, fill: c_accent)[#if s.num < 10 [0] else []#s.num],
      block[
        #text(font: "Instrument Serif", size: 17.5pt, fill: c_ink)[#s.title]
        #v(3pt)
        #text(size: 8.2pt, fill: c_ink2)[#s.intro]
        #v(3.5pt)
        #text(size: 7.4pt, style: "italic", fill: c_muted)[
          Idées #s.start_code à #s.end_code · #p_cnt petit budget, #m_cnt budget moyen, #st_cnt structuré
        ]
      ]
    )
  ]
}

#for (idx_s, s) in sectors.enumerate() [
  #if idx_s > 0 { pagebreak() }
  #sector_masthead(s)
  #v(6pt)
  #grid(
    columns: (1fr, 1fr),
    column-gutter: 14pt,
    row-gutter: 3pt,
    ..s.ideas.map(it => idea_cell(it)),
    block(
      breakable: false,
      width: 100%,
      stroke: (top: 0.6pt + c_accent),
      inset: (top: 7pt, bottom: 4pt),
    )[
      #text(size: 7.8pt, weight: "semibold", fill: c_accent)[Sélection secteur #if s.num < 10 [0] else []#s.num]
      #v(3pt)
      #text(size: 7.8pt, fill: c_ink2)[Idées retenues pour le test de 48 heures :]
      #v(5pt)
      #text(size: 8.0pt, fill: c_ink)[
        #checkbox() #h(4pt) N° ………… #h(14pt) #checkbox() #h(4pt) N° …………
      ]
    ]
  )
]

#pagebreak()

// ============================================================================
// PARTIE 04 : VALIDATION EXPRESS EN 48 HEURES
// ============================================================================
#chapter_opener(data.part04.kicker, data.part04.title, data.part04.epigraph, "p-04")
#text(size: 9.2pt, fill: c_ink)[#data.part04.intro]

#section_head("Les trois filtres VIN avant d'investir")
#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 12pt,
  ..data.part04.vin.enumerate().map(((i, vin_it)) => {
    let acc = if i == 0 { c_accent } else if i == 1 { c_ocre } else { c_clay }
    grid.cell(
      stroke: (top: 1.1pt + acc, bottom: 0.35pt + c_rule),
      inset: (top: 7pt, bottom: 8pt),
    )[
      #text(size: 8.2pt, weight: "bold", fill: acc)[#vin_it.title]
      #v(4pt)
      #text(size: 8.2pt, fill: c_ink2)[#vin_it.desc]
    ]
  })
)

#section_head("Le protocole terrain en quarante-huit heures")
#for st in data.part04.steps_48h [
  #box(width: 100%, inset: (y: 5pt), stroke: (bottom: 0.35pt + c_hair))[
    #grid(
      columns: (146pt, 1fr),
      column-gutter: 10pt,
      text(size: 8.3pt, weight: "semibold", fill: c_accent)[#st.title],
      text(size: 8.5pt, fill: c_ink)[#st.desc],
    )
  ]
]

#pagebreak()

#section_head("Grille de notation de tes trois idées finalistes (/30)")
#table(
  columns: (1fr, 58pt, 58pt, 58pt),
  stroke: (x, y) => (bottom: if y == 0 or y == 6 { 0.8pt + c_ink } else { 0.35pt + c_hair }),
  fill: none,
  inset: (x: 5pt, y: 7pt),
  table.header(
    text(size: 7.9pt, weight: "bold", fill: c_accent)[Critère (note de 1 à 5)],
    align(center, text(size: 7.9pt, weight: "bold", fill: c_accent)[Idée A]),
    align(center, text(size: 7.9pt, weight: "bold", fill: c_accent)[Idée B]),
    align(center, text(size: 7.9pt, weight: "bold", fill: c_accent)[Idée C]),
  ),
  ..data.part04.scoring.map(c => (
    block[
      #text(size: 8.6pt, weight: "semibold", fill: c_ink)[#c.title]
      #v(1.5pt)
      #text(size: 7.9pt, fill: c_ink2)[#c.desc]
    ],
    align(center + horizon, text(size: 8.6pt, fill: c_muted)[…… / 5]),
    align(center + horizon, text(size: 8.6pt, fill: c_muted)[…… / 5]),
    align(center + horizon, text(size: 8.6pt, fill: c_muted)[…… / 5]),
  )).flatten(),
  text(size: 8.6pt, weight: "bold", fill: c_accent)[Total final (/30) — Retenir à partir de 20 / 30],
  align(center + horizon, text(size: 8.8pt, weight: "bold", fill: c_accent)[…… / 30]),
  align(center + horizon, text(size: 8.8pt, weight: "bold", fill: c_accent)[…… / 30]),
  align(center + horizon, text(size: 8.8pt, weight: "bold", fill: c_accent)[…… / 30]),
)

#v(16pt)
#box(
  width: 100%,
  stroke: (left: 1pt + c_accent),
  inset: (left: 13pt, y: 4pt),
)[
  #text(font: "Instrument Serif", size: 14.5pt, fill: c_ink)[#data.part04.example_title]
  #v(5pt)
  #for ln in data.part04.example_lines [
    #text(size: 8.5pt, fill: c_ink2)[#ln]
    #v(3pt)
  ]
]

#pagebreak()

// ============================================================================
// PARTIE 05 : PLAN DE LANCEMENT EN 7 JOURS
// ============================================================================
#chapter_opener(data.part05.kicker, data.part05.title, data.part05.epigraph, "p-05")
#text(size: 9.1pt, fill: c_ink)[#data.part05.intro]

#section_head("Chronologie d'exécution : Jour 1 à Jour 7")
#for d in data.part05.days [
  #box(
    width: 100%,
    stroke: (bottom: 0.35pt + c_hair),
    inset: (y: 5.5pt),
  )[
    #grid(
      columns: (52pt, 1fr),
      column-gutter: 10pt,
      align: top,
      text(font: "Instrument Serif", size: 13.5pt, fill: c_accent)[#d.day],
      block[
        #text(size: 8.9pt, weight: "bold", fill: c_ink)[#d.title]
        #v(1.5pt)
        #text(size: 8.2pt, fill: c_ink2)[#d.desc]
      ]
    )
  ]
]

#pagebreak()

#section_head("Trois messages prêts à adapter sur WhatsApp et Facebook")
#for sc in data.part05.scripts [
  #box(
    width: 100%,
    stroke: (left: 0.9pt + c_accent),
    inset: (left: 11pt, y: 3pt),
  )[
    #text(size: 8.4pt, weight: "bold", fill: c_accent)[#sc.title]
    #v(2.5pt)
    #text(size: 8.4pt, style: "italic", fill: c_ink)[#sc.body]
  ]
  #v(8pt)
]

#section_head("Fixer le prix juste et répartir chaque encaissement")
#for pf in data.part05.pricing [
  #text(size: 8.5pt, fill: c_ink)[#pf]
  #v(2.5pt)
]
#v(8pt)

// Barre proportionnelle fine (3pt) + trois colonnes épurées
#box(width: 100%, height: 4pt)[
  #grid(
    columns: (50%, 30%, 20%),
    rect(width: 100%, height: 4pt, fill: c_accent),
    rect(width: 100%, height: 4pt, fill: c_ocre),
    rect(width: 100%, height: 4pt, fill: c_clay),
  )
]
#v(8pt)

#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 12pt,
  ..data.part05.envelopes.enumerate().map(((i, env)) => {
    let acc = if i == 0 { c_accent } else if i == 1 { c_ocre } else { c_clay }
    grid.cell(
      stroke: (bottom: 0.35pt + c_rule),
      inset: (bottom: 8pt),
    )[
      #text(size: 8.5pt, weight: "bold", fill: acc)[#env.title]
      #v(3pt)
      #text(size: 8.0pt, fill: c_ink2)[#env.desc]
    ]
  })
)

#pagebreak()

// ============================================================================
// CONCLUSION, FICHE D'ENGAGEMENT & À PROPOS DE L'AUTEUR
// ============================================================================
#chapter_opener(data.conclusion.kicker, data.conclusion.title, data.conclusion.epigraph, "p-conc")
#text(size: 8.9pt, fill: c_ink)[#data.conclusion.message]
#v(8pt)

#box(
  width: 100%,
  stroke: (left: 1pt + c_accent),
  inset: (left: 12pt, y: 3pt),
)[
  #text(font: "Instrument Serif", size: 12.6pt, style: "italic", fill: c_ink)[#data.conclusion.mantra]
]

#v(9pt)
#text(font: "Instrument Serif", size: 14.5pt, fill: c_ink)[Trois prochains pas]
#v(3pt)
#line(length: 100%, stroke: 0.4pt + c_rule)
#v(4pt)
#for ns in data.conclusion.next_steps [
  #text(size: 8.4pt, fill: c_ink2)[#ns]
  #v(2.5pt)
]

#v(8pt)
#text(font: "Instrument Serif", size: 14.5pt, fill: c_ink)[Fiche d'engagement terrain]
#v(3pt)
#line(length: 100%, stroke: 0.4pt + c_rule)
#v(2pt)
#for ln in data.conclusion.action_sheet [
  #box(
    width: 100%,
    inset: (y: 4.5pt),
    stroke: (bottom: 0.35pt + c_hair),
  )[
    #grid(
      columns: (auto, auto, 1fr),
      column-gutter: 6pt,
      align: horizon,
      checkbox(accent: c_accent),
      text(size: 8.2pt, fill: c_ink)[#ln],
      align(bottom, line(length: 100%, stroke: (paint: c_muted, thickness: 0.4pt, dash: "dotted")))
    )
  ]
]

#v(1fr)
#box(
  width: 100%,
  stroke: (top: 0.9pt + c_accent, bottom: 0.45pt + c_rule),
  inset: (top: 9pt, bottom: 9pt),
)[
  #text(size: 7.6pt, weight: "semibold", fill: c_accent)[À propos de l'auteur]
  #v(2pt)
  #text(font: "Instrument Serif", size: 15.5pt, fill: c_ink)[#cfg.author_name]
  #h(8pt)
  #text(size: 8.2pt, style: "italic", fill: c_ink2)[#cfg.author_role]
  #v(3pt)
  #text(size: 8.1pt, fill: c_ink2)[#cfg.author_bio]
  #v(5pt)
  #text(size: 7.8pt, fill: c_accent)[
    WhatsApp : #cfg.contact_whatsapp  ·  Réseaux : #cfg.contact_social  ·  Courriel : #cfg.contact_email
  ]
]
'''


WORKBOOK_TYP = r'''
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
'''


def build_json_payload(config, sectors, ebook_pages=None):
    """Prépare le JSON complet consommé nativement par Typst."""
    wb = get_workbook_pages_data(config, ebook_pages=ebook_pages)

    sectors_data = []
    for s in sectors:
        counts = {"Petit": 0, "Moyen": 0, "Structuré": 0}
        for it in s["ideas"]:
            counts[it["budget"]] += 1
        sectors_data.append({
            "num": s["num"],
            "title": s["title"],
            "intro": s["intro"],
            "start_code": f"{s['start_id']:03d}",
            "end_code": f"{s['end_id']:03d}",
            "counts": counts,
            "ideas": s["ideas"],
        })

    payload = {
        "config": config,
        "budget_guide": BUDGET_GUIDE,
        "sectors": sectors_data,
        "part01": {
            "kicker": PART_01_INTRO["kicker"],
            "title": PART_01_INTRO["title"],
            "epigraph": PART_01_INTRO["epigraph"],
            "lead": PART_01_INTRO["lead"],
            "problem_blocks": [{"title": t, "body": b} for t, b in PART_01_INTRO["problem_blocks"]],
            "trends": [{"title": t, "body": b} for t, b in PART_01_INTRO["trends_2027"]],
            "profiles": [{"profile": p, "budget": b, "sectors": sec} for p, b, sec in PART_01_INTRO["profiles"]],
        },
        "part02": {
            "kicker": PART_02_ERRORS["kicker"],
            "title": PART_02_ERRORS["title"],
            "epigraph": PART_02_ERRORS["epigraph"],
            "intro": PART_02_ERRORS["intro"],
            "errors": [{"title": t, "consequence": c, "fix": f} for t, c, f in PART_02_ERRORS["errors"]],
        },
        "part04": {
            "kicker": PART_04_VALIDATION["kicker"],
            "title": PART_04_VALIDATION["title"],
            "epigraph": PART_04_VALIDATION["epigraph"],
            "intro": PART_04_VALIDATION["intro"],
            "vin": [{"title": t, "desc": d} for t, d in PART_04_VALIDATION["vin_reminders"]],
            "steps_48h": [{"title": t, "desc": d} for t, d in PART_04_VALIDATION["steps_48h"]],
            "scoring": [{"title": t, "desc": d} for t, d in PART_04_VALIDATION["scoring_criteria"]],
            "example_title": PART_04_VALIDATION["example_box_title"],
            "example_lines": PART_04_VALIDATION["example_box_lines"],
        },
        "part05": {
            "kicker": PART_05_LAUNCH["kicker"],
            "title": PART_05_LAUNCH["title"],
            "epigraph": PART_05_LAUNCH["epigraph"],
            "intro": PART_05_LAUNCH["intro"],
            "days": [{"day": d, "title": t, "desc": desc} for d, t, desc in PART_05_LAUNCH["days"]],
            "scripts": [{"title": t, "body": b} for t, b in PART_05_LAUNCH["scripts"]],
            "pricing": PART_05_LAUNCH["pricing_formula"],
            "envelopes": [{"title": t, "desc": d} for t, d in PART_05_LAUNCH["envelopes"]],
        },
        "conclusion": {
            "kicker": CONCLUSION_CONTENT["kicker"],
            "title": CONCLUSION_CONTENT["title"],
            "epigraph": CONCLUSION_CONTENT["epigraph"],
            "message": CONCLUSION_CONTENT["message"],
            "mantra": CONCLUSION_CONTENT["mantra"],
            "next_steps": CONCLUSION_CONTENT["next_steps_reader"],
            "action_sheet": CONCLUSION_CONTENT["action_sheet"],
        },
        "workbook": wb,
    }
    return payload


def write_markdown_exports(config, sectors, ebook_pages=None):
    """Écrit les versions Markdown complètes pour personnalisation libre dans Notion/Docs/Word."""
    wb = get_workbook_pages_data(config, ebook_pages=ebook_pages)
    wb_lines = [
        f"# Workbook Officiel Jour 2 — Dossier Rempli : {config['ebook_title']}",
        "",
        f"> Auteur : **{wb['author']}** | Date : **{wb['date']}**",
        "",
        "## Page 1 — Bienvenue",
        wb["page1"]["welcome"],
        "",
    ]
    for k, v in wb["page1"]["summary_rows"]:
        wb_lines.append(f"- **{k}** : {v}")
    wb_lines += [
        "",
        "## Page 2 — Objectif & Engagement personnel",
        wb["page2"]["intro"],
        f"\n> {wb['page2']['quote']}\n",
    ]
    for k, v in wb["page2"]["commitment"]:
        wb_lines.append(f"- **{k}** : {v}")
    wb_lines += [
        "",
        "## Page 3 — Validation Express (Méthode VIN)",
        f"- **V · Problème (Valeur)** : {wb['page3']['V']}",
        f"- **I · Intensité** : {wb['page3']['I_score']} — {wb['page3']['I_exp']}",
        f"- **N · Nombre** : {wb['page3']['N']}",
        f"- **{wb['page3']['conclusion']}**",
        "",
        "## Page 4 — Promesse Claire",
        f"- **1. Pour qui ?** {wb['page4']['q1']}",
        f"- **2. Résultat concret :** {wb['page4']['q2']}",
        f"- **3. Délai :** {wb['page4']['q3']}",
        f"- **Formule complétée :** {wb['page4']['formula_filled']}",
        "",
        "## Page 5 — Format PDF",
        f"- **Pourquoi le PDF :** {wb['page5']['why_chosen']}",
        f"- **Pagination :** {wb['page5']['pages_note']}",
        f"- **Titre :** {wb['page5']['provisional_title']}",
        "",
        "## Page 6 — Structure en 5 Parties + Conclusion",
    ]
    for num, lbl, desc in wb["page6"]["parts"]:
        wb_lines.append(f"- **{num} — {lbl}** : {desc}")
    wb_lines += [
        "",
        "## Page 7 — IA & Checklist",
        f"**Prompt appliqué :** {wb['page7']['prompt_applied']}",
        "",
        "**Checklist de création :**",
    ]
    for lbl, _ in wb["page7"]["checklist"]:
        wb_lines.append(f"- [x] {lbl}")
    wb_lines += ["", "## Page 8 — Récapitulatif"]
    for t_r, d_r, s_r in wb["page8"]["recap_cards"]:
        wb_lines.append(f"- **{t_r}** ({s_r}) : {d_r}")
    wb_lines += ["", "## Page 9 — Déclaration officielle & Posts Facebook"]
    for k, v in wb["page9"]["declaration"]:
        wb_lines.append(f"- **{k}** : {v}")
    wb_lines.append("")
    for pt, pb in wb["page9"]["social_posts"]:
        wb_lines.append(f"### {pt}\n{pb}\n")
    wb_lines += ["## Page 10 — Prochains pas"]
    for st_t, st_b in wb["page10"]["steps"]:
        wb_lines.append(f"- **{st_t}** : {st_b}")
    wb_lines.append(f"\n```\n{wb['page10']['whatsapp_testers']}\n```")
    OUT_WORKBOOK_MD.write_text("\n".join(wb_lines), encoding="utf-8")

    eb_lines = [
        f"# {config['ebook_title']}",
        f"*{config['ebook_subtitle']}*",
        "",
        f"**Promesse :** {config['promise_formula']}",
        "",
        f"**Auteur :** {config['author_name']} | **Date :** {config['date_creation']}",
        "",
        "---",
        "",
        f"## Partie 01 — {PART_01_INTRO['title']}",
        PART_01_INTRO["lead"],
        "",
    ]
    for bt, bb in PART_01_INTRO["problem_blocks"]:
        eb_lines.append(f"### {bt}\n{bb}\n")
    for tt, tb in PART_01_INTRO["trends_2027"]:
        eb_lines.append(f"- **{tt}** : {tb}")
    eb_lines += ["", f"## Partie 02 — {PART_02_ERRORS['title']}", PART_02_ERRORS["intro"], ""]
    for et, ec, ef in PART_02_ERRORS["errors"]:
        eb_lines.append(f"### {et}\n- {ec}\n- {ef}\n")
    eb_lines += ["", "## Partie 03 — Les 500 Idées de Business en 20 Secteurs", ""]
    for s in sectors:
        eb_lines.append(f"### Secteur {s['num']:02d} : {s['title']} (#{s['start_id']:03d}–#{s['end_id']:03d})")
        eb_lines.append(s["intro"])
        eb_lines.append("")
        for it in s["ideas"]:
            eb_lines.append(f"- **#{it['code']} — {it['title']}** *[{it['budget']}]* : {it['desc']}")
        eb_lines.append("")
    eb_lines += ["", f"## Partie 04 — {PART_04_VALIDATION['title']}", PART_04_VALIDATION["intro"], ""]
    for vt, vd in PART_04_VALIDATION["vin_reminders"]:
        eb_lines.append(f"- **{vt}** : {vd}")
    eb_lines += ["", f"## Partie 05 — {PART_05_LAUNCH['title']}", PART_05_LAUNCH["intro"], ""]
    for dn, dt, dd in PART_05_LAUNCH["days"]:
        eb_lines.append(f"- **{dn} — {dt}** : {dd}")
    eb_lines.append("")
    for st, sb in PART_05_LAUNCH["scripts"]:
        eb_lines.append(f"### {st}\n{sb}\n")
    eb_lines += [
        "",
        f"## Conclusion — {CONCLUSION_CONTENT['title']}",
        CONCLUSION_CONTENT["message"],
        "",
        f"> {CONCLUSION_CONTENT['mantra']}",
    ]
    OUT_EBOOK_MD.write_text("\n".join(eb_lines), encoding="utf-8")


def main():
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    sectors = get_numbered_sectors()

    EBOOK_TYP_PATH.write_text(EBOOK_TYP.strip() + "\n", encoding="utf-8")
    WORKBOOK_TYP_PATH.write_text(WORKBOOK_TYP.strip() + "\n", encoding="utf-8")

    print("1/3 Compilation Typst de l'Ebook complet (mise en page éditoriale)...")
    payload = build_json_payload(config, sectors, ebook_pages=None)
    DATA_JSON_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    typst.compile(
        str(EBOOK_TYP_PATH),
        output=str(OUT_EBOOK_PDF),
        root=str(SOURCE_DIR),
        font_paths=FONT_PATHS,
    )
    with pymupdf.open(str(OUT_EBOOK_PDF)) as eb_doc:
        ebook_pages = len(eb_doc)
    print(f"    -> {OUT_EBOOK_PDF} ({ebook_pages} pages)")

    print("2/3 Compilation Typst du Workbook Jour 2 rempli (10 pages exactes)...")
    payload = build_json_payload(config, sectors, ebook_pages=ebook_pages)
    DATA_JSON_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    typst.compile(
        str(WORKBOOK_TYP_PATH),
        output=str(OUT_WORKBOOK_PDF),
        root=str(SOURCE_DIR),
        font_paths=FONT_PATHS,
    )
    with pymupdf.open(str(OUT_WORKBOOK_PDF)) as wb_doc:
        wb_pages = len(wb_doc)
    print(f"    -> {OUT_WORKBOOK_PDF} ({wb_pages} pages)")

    print("3/3 Export des sources Markdown éditables...")
    write_markdown_exports(config, sectors, ebook_pages=ebook_pages)
    print(f"    -> {OUT_WORKBOOK_MD}")
    print(f"    -> {OUT_EBOOK_MD}")
    print("Compilation éditoriale terminée avec succès !")


if __name__ == "__main__":
    main()
