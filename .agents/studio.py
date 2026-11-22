"""Atelier local des skills d’édition. Aucune publication ni requête réseau."""
import argparse
from contextlib import contextmanager
from hashlib import sha256
import json
from pathlib import Path
from shutil import copy2, copytree, ignore_patterns
import subprocess
import sys
from tempfile import TemporaryDirectory, mkdtemp

AGENTS = Path(__file__).resolve().parent
KIT = AGENTS.parent / 'bourse-france'
sys.path.insert(0, str(KIT / 'edition'))
LIVRES = {'france': 'Mon-dossier-France.pdf', 'top10': 'bonus/Top-10-bourses-internationales.pdf',
          'extrait': 'vente/Extrait-gratuit.pdf'}
TEXTES = {'france': 'guide.md', 'top10': 'panorama.md'}


def skills():
    return sorted(p.parent.name for p in (AGENTS / 'skills').glob('*/SKILL.md'))


def verifier_installation():
    locaux = {'maquette-livre-mobile', 'verification-bourses', 'redaction-debutants', 'controle-kit'}
    origines = json.loads((AGENTS / 'origines.json').read_text(encoding='utf-8'))
    manquants = (locaux | set(origines)) - set(skills())
    if manquants:
        raise ValueError('Skills absents : ' + ', '.join(sorted(manquants)))
    for nom, source in origines.items():
        dossier = AGENTS / 'skills' / nom
        empreintes = {p.relative_to(dossier).as_posix(): sha256(p.read_bytes()).hexdigest()
                      for p in dossier.rglob('*') if p.is_file()}
        if empreintes != source['sha256']:
            raise ValueError(f'{nom} ne correspond plus à la version enregistrée dans origines.json.')
    print(f'{len(skills())} skills présents ; copies de pdf et theme-factory conformes aux empreintes.', flush=True)


@contextmanager
def edition(brouillon):
    """Par défaut, lecture du kit livré ; en mode brouillon, construire ailleurs."""
    if not brouillon:
        yield KIT
        return
    with TemporaryDirectory(prefix='dossier-france-') as tmp:
        copie = Path(tmp) / 'bourse-france'
        copytree(KIT / 'edition', copie / 'edition', ignore=ignore_patterns('__pycache__', '*.pyc'))
        (copie / 'vente').mkdir()
        for rel in ('README.md', 'vente/Fiche-Chariow.md'):
            copy2(KIT / rel, copie / rel)
        subprocess.run([sys.executable, str(copie / 'edition/fabriquer.py')], cwd=tmp, check=True)
        yield copie


def sources(livre, cle):
    from commun import LIENS
    from livret import read_pages
    pages = read_pages(TEXTES[livre])
    if not cle:
        for p in pages:
            if p['refs']:
                print(f"{p['key']:16} {p['title']}")
        return
    page = next((p for p in pages if p['key'] == cle), None)
    if page is None or not page['refs']:
        raise ValueError(f'Pas de fiche sourcée « {cle} ». Relance sources {livre} sans identifiant pour voir la liste.')
    print(f"# À vérifier : {page['title']} ({livre} / {cle})\n\nLiens déjà cités dans le manuscrit, non consultés par cet outil :\n")
    for ref in dict.fromkeys(page['refs']):
        nom, url = LIENS[ref]
        print(f'- [{nom}]({url}) — `{ref}`')
    fiche = AGENTS / 'skills/verification-bourses/references/fiche-preuve.md'
    print('\n' + fiche.read_text(encoding='utf-8'))


def index_pages(livre):
    from livret import EXTRAIT, read_pages
    if livre == 'extrait':
        return {'couverture': 1, **{k:i for i,k in enumerate(EXTRAIT,2)}}
    ids = ['couverture', 'sommaire', *(p['key'] for p in read_pages(TEXTES[livre]))]
    if livre == 'france':
        ids.append('liens')
    return {k:i for i,k in enumerate(ids,1)}


def contraste(a, b):
    def luminance(c):
        rgb = [int(c[i:i+2],16)/255 for i in (1,3,5)]
        linear = [v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in rgb]
        return sum(v*w for v,w in zip(linear,(.2126,.7152,.0722)))
    sombre, clair = sorted((luminance(a),luminance(b)))
    return (clair+.05)/(sombre+.05)


def epreuve(args):
    import pymupdf
    from PIL import Image, ImageDraw
    from livret import INK, PAPER, TEAL, SOFT, FOREST, FADE
    index = index_pages(args.livre)
    if args.liste:
        for cle, n in index.items():
            print(f'{n:2}  {cle}')
        return
    demandes = args.pages or list(index)[:3]
    numeros = []
    for cle in demandes:
        n = int(cle) if cle.isdecimal() else index.get(cle)
        if n not in index.values():
            raise ValueError(f'Page inconnue : {cle}. Utilise « epreuve {args.livre} --liste ».')
        if n not in numeros:
            numeros.append(n)
    if len(numeros) > 8:
        raise ValueError('Choisis au plus huit pages par épreuve pour pouvoir les examiner.')
    with edition(args.brouillon) as projet, pymupdf.open(projet / LIVRES[args.livre]) as pdf:
        if len(pdf) != len(index):
            raise ValueError('Le nombre de pages du PDF ne correspond pas au manuscrit. Essaie --brouillon.')
        cache = KIT.parent / '.cache/epreuves'
        cache.mkdir(parents=True, exist_ok=True)
        sortie = Path(mkdtemp(prefix=args.livre+'-', dir=cache))
        cols = min(3,len(numeros)); largeur, hauteur = 207, 460
        planche = Image.new('RGB', (cols*largeur, ((len(numeros)+cols-1)//cols)*hauteur), '#F2F0E9')
        dessin = ImageDraw.Draw(planche)
        for i,n in enumerate(numeros):
            page = pdf[n-1]; zoom = args.largeur/page.rect.width
            pixels = page.get_pixmap(matrix=pymupdf.Matrix(zoom,zoom), colorspace=pymupdf.csRGB, alpha=False)
            image = Image.frombytes('RGB', (pixels.width,pixels.height), pixels.samples)
            image.save(sortie/f'page-{n:02}.png')
            image.thumbnail((largeur-12, hauteur-30), Image.Resampling.LANCZOS)
            x,y = (i%cols)*largeur, (i//cols)*hauteur
            planche.paste(image, (x+6,y+6)); dessin.text((x+6,y+hauteur-21),f'{args.livre} | p. {n}',fill='#163E3D')
        planche.save(sortie/'planche.png')
    print(f'Images de lecture ({args.largeur} px) et planche : {sortie}')
    erreurs = []
    for label,a,b in [('corps/papier',INK,PAPER),('secondaire/papier',FADE,PAPER),('lien/encadré',TEAL,SOFT),('clair/fond sombre',PAPER,FOREST)]:
        ratio = contraste(a,b); print(f'{label} : {ratio:.2f}:1')
        if ratio < 4.5:
            erreurs.append(label)
    if erreurs:
        raise ValueError('Contraste du texte inférieur au repère de 4,5:1 : '+', '.join(erreurs))
    print('Quatre paires de la charte contrôlées ; ouvrir les PNG pour juger les pages réelles.')


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    sous = cli.add_subparsers(dest='action', required=True)
    sous.add_parser('liste',help='Lister les skills installés dans ce projet.')
    s = sous.add_parser('sources',help='Lister les fiches sourcées ou préparer une fiche de vérification.')
    s.add_argument('livre',choices=TEXTES); s.add_argument('cle',nargs='?')
    e = sous.add_parser('epreuve',help='Rendre de vraies pages à la largeur d’un téléphone (PNG).')
    e.add_argument('livre',choices=LIVRES); e.add_argument('pages',nargs='*',metavar='PAGE')
    e.add_argument('--liste',action='store_true',help='Afficher les numéros et les identifiants de page.')
    e.add_argument('--largeur',type=int,choices=(360,390),default=390,help='Largeur de lecture en pixels.')
    t = sous.add_parser('tester',help='Vérifier l’installation et exécuter la recette du kit.')
    for commande in (e,t):
        commande.add_argument('--brouillon',action='store_true',help='Refabriquer dans un dossier temporaire, sans écraser le kit livré.')
    args = cli.parse_args()
    try:
        if args.action == 'liste': print('\n'.join(skills()))
        elif args.action == 'sources': sources(args.livre,args.cle)
        elif args.action == 'epreuve': epreuve(args)
        else:
            verifier_installation()
            with edition(args.brouillon) as proj:
                subprocess.run([sys.executable,str(proj/'edition/verifier.py')],cwd=proj,check=True)
    except (ValueError, FileNotFoundError) as err:
        cli.exit(1,f'{err}\n')
    except ModuleNotFoundError as err:
        cli.exit(1,f'Module manquant : {err.name}. Utilise le Python de .venv avec les dépendances d’édition.\n')
    except subprocess.CalledProcessError as err:
        cli.exit(err.returncode,'Échec de la fabrication ou des contrôles. Aucun livrable remplacé.\n')


if __name__ == '__main__':
    main()
