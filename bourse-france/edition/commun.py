"""Chemins et ressources partagés par les générateurs du kit."""
from pathlib import Path
import json

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent
BONUS = RACINE / 'bonus'
VENTE = RACINE / 'vente'
LIENS = json.loads((ICI / 'sources.json').read_text(encoding='utf-8'))
GUIDE = RACINE / 'Mon-dossier-France.pdf'
DOCX = BONUS / 'Atelier-dossier.docx'
XLSX = BONUS / 'Suivi-et-budget.xlsx'
KIT = RACINE / 'Kit-Mon-dossier-France.zip'
EDITION = 'Novembre 2026'
