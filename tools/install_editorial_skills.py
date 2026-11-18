"""Installe une sélection épinglée de ressources publiques sans exécuter leur code."""
from pathlib import Path
import hashlib
import io
import json
import tarfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
COMMIT = 'e4bb5d960d87126ff3b3a8af1a104b7db67560ba'
SKILLS = ('pdf', 'canvas-design', 'theme-factory')
URL = f'https://codeload.github.com/anthropics/skills/tar.gz/{COMMIT}'


def main():
    archive = urllib.request.urlopen(URL, timeout=60).read()
    manifest = {'repository': 'https://github.com/anthropics/skills', 'commit': COMMIT,
                'archive_sha256': hashlib.sha256(archive).hexdigest(), 'skills': {}}
    with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as bundle:
        for name in SKILLS:
            prefix = f'skills-{COMMIT}/skills/{name}/'
            files = {}
            for member in bundle.getmembers():
                if not member.isfile() or not member.name.startswith(prefix):
                    continue
                relative = Path(member.name[len(prefix):])
                if relative.is_absolute() or '..' in relative.parts:
                    raise ValueError('Chemin non autorisé')
                target = ROOT / '.agents' / 'skills' / name / relative
                data = bundle.extractfile(member).read()
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                files[str(relative)] = hashlib.sha256(data).hexdigest()
            assert 'SKILL.md' in files
            manifest['skills'][name] = files
        for filename in ('LICENSE', 'LICENSE.txt', 'README.md'):
            member_name = f'skills-{COMMIT}/{filename}'
            try:
                member = bundle.getmember(member_name)
            except KeyError:
                continue
            out = ROOT / '.agents' / 'upstream' / filename
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(bundle.extractfile(member).read())
    out = ROOT / '.agents' / 'upstream' / 'manifest.json'
    out.write_text(json.dumps(manifest, indent=2) + '\n')
    print('Installés : ' + ', '.join(SKILLS))
    print('Source et empreintes : .agents/upstream/manifest.json')

if __name__ == '__main__':
    main()
