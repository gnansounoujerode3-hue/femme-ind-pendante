"""Contrôles techniques locaux. Ne certifie ni les droits ni la qualité visuelle."""
from pathlib import Path
import hashlib
import json
import re
import sys
from pypdf import PdfReader
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
STEM = 'LE-GUIDE-ULTIME-100-RECETTES-BENINOISES-AFRICAINES'


def main():
    errors, warnings, checks = [], [], []
    manifest = json.loads((ROOT / '.agents/upstream/manifest.json').read_text())
    for skill, files in manifest['skills'].items():
        for relative, expected in files.items():
            path = ROOT / '.agents/skills' / skill / relative
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                errors.append(f'Ressource publique absente ou modifiée : {skill}/{relative}')
    checks.append(f"{len(manifest['skills'])} skills publics : empreintes contrôlées")
    for skill in ('cookbook-layout', 'food-image-sourcing', 'recipe-editor', 'ebook-quality'):
        path = ROOT / '.agents/skills' / skill / 'SKILL.md'
        if not path.is_file() or not path.read_text().startswith('---\nname: '):
            errors.append(f'Skill local invalide : {skill}')
    checks.append('4 skills locaux : présence et en-têtes contrôlés')
    text = (ROOT / f'{STEM}.md').read_text()
    numbers = [int(x) for x in re.findall(r'^### (\d+)\.', text, re.M)]
    if numbers != list(range(1, 101)):
        errors.append('Numérotation des recettes incorrecte')
    for label in ('**Ingrédients**', '**Pas à pas**', '**Conseil débutant :**'):
        if text.count(label) != 100:
            errors.append(f'Nombre de sections incorrect : {label}')
    checks.append('100 recettes : numéros et sections contrôlés')
    pdf = PdfReader(ROOT / f'{STEM}.pdf')
    all_text = []
    for number, page in enumerate(pdf.pages, 1):
        page_text = page.extract_text() or ''
        all_text.append(page_text)
        if len(page_text.strip()) < 80:
            warnings.append(f'Page {number} presque vide : à inspecter')
    flattened = ' '.join(' '.join(all_text).split())
    titles = re.findall(r'^### (\d+\. .+)$', text, re.M)
    for title in titles:
        if ' '.join(title.split()) not in flattened:
            errors.append(f'Titre non retrouvé dans le PDF : {title}')
    checks.append(f'{len(pdf.pages)} pages PDF : extraction et présence des titres contrôlées')
    registry = json.loads((ROOT / 'assets/food/registry.json').read_text())
    entries = registry['images']
    if not entries:
        warnings.append('Aucune image culinaire acquise : sélection, droits et crédits restent à faire')
    for entry in entries:
        ident = entry.get('id', 'sans identifiant')
        for field in ('id', 'recipe_id', 'local_path', 'source_page_url', 'author', 'license',
                      'license_evidence', 'verified_on', 'attribution', 'commercial_use',
                      'modifications_allowed', 'modifications', 'status'):
            if field not in entry:
                errors.append(f'Image {ident} : champ manquant {field}')
        if entry.get('status') != 'approved':
            warnings.append(f'Image {ident} : non approuvée, ne pas publier')
        if entry.get('commercial_use') is not True:
            warnings.append(f'Image {ident} : usage commercial non confirmé')
        local = entry.get('local_path')
        if local:
            path = (ROOT / local).resolve()
            if not path.is_relative_to(ROOT):
                errors.append(f'Image {ident} : chemin hors du projet')
                continue
            try:
                with Image.open(path) as im:
                    im.verify()
            except Exception as exc:
                errors.append(f'Image {ident} illisible : {exc}')
    warnings.append('Inspection visuelle et essais culinaires non couverts par cet audit')
    report = {'checks': checks, 'warnings': warnings, 'errors': errors}
    out = ROOT / 'reports/audit-editorial.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    for label, lines in (('OK', checks), ('À FAIRE', warnings), ('ERREUR', errors)):
        for line in lines:
            print(f'{label} — {line}')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
