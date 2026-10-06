"""Check current organization, source bindings and media mappings. Reports only."""
from pathlib import Path
from urllib.parse import unquote
import ast
import hashlib
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
import yaml

errors=[]
def require(condition,message):
    if not condition: errors.append(message)

docs=[ROOT/'AGENTS.md',ROOT/'README.md']
for directory in ['docs','assets','audio','handoff','tools']:
    docs.extend((ROOT/directory).rglob('*.md'))
for path in docs:
    for ref in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8-sig')):
        target=unquote(ref.strip('<>').split('#')[0])
        if target and not re.match(r'\w+://',target):
            require((path.parent/target).exists(),f'Broken link: {path.relative_to(ROOT)} -> {target}')
for directory in ['tools','scripts/staging']:
    for path in (ROOT/directory).rglob('*.py'):
        try: ast.parse(path.read_text(encoding='utf-8-sig'),filename=str(path))
        except SyntaxError as e: errors.append(str(e))
count=0
for chapter in ['ch01','ch02']:
    ja_path=ROOT/f'scripts/ja/{chapter}.yaml'
    ja=yaml.safe_load(ja_path.read_text(encoding='utf-8'))
    zh=json.loads((ROOT/f'scripts/zh/{chapter}.json').read_text(encoding='utf-8-sig'))
    entries=[e for s in ja['scenes'] for e in s['entries']]
    require(len({e['id'] for e in entries})==len(entries),f'{chapter}: duplicate IDs')
    require(zh['source_ja_sha256'].lower()==hashlib.sha256(ja_path.read_bytes()).hexdigest(),f'{chapter}: stale Chinese source binding')
    require(set(zh['lines'])=={e['id'] for e in entries if e['type']!='direction'},f'{chapter}: subtitle coverage')
    staging=json.loads((ROOT/f'scripts/staging/{chapter}/directions.json').read_text(encoding='utf-8'))
    require(set(staging['directions'])=={e['id'] for e in entries if e['type']=='direction'},f'{chapter}: direction coverage')
for path in (ROOT/'assets/records').glob('*.json'):
    data=json.loads(path.read_text(encoding='utf-8'))
    for row in data.get('runtime_images',[]):
        target=ROOT/row['runtime']
        require(target.is_file(),f'Missing runtime: {target}')
        if row.get('derived_from'):
            require((ROOT/row['derived_from']).is_file(),f'Missing derived image source: {row["derived_from"]}')
        for original in row['originals']:
            src=ROOT/original
            require(src.is_file(),f'Missing original: {original}')
            if src.is_file() and target.is_file():
                require(src.read_bytes()==target.read_bytes(),f'Image copies differ: {original}')
        count+=1
    for row in data.get('references',[]):
        require((ROOT/row['file']).is_file(),f'Missing reference: {row["file"]}')
report={'errors':errors,'documents_checked':len(docs),'runtime_images_checked':count,
        'runtime_tested':False,'note':'Organization checks only; user-confirmed completion lives in docs/status.md.'}
(ROOT/'.build/reports').mkdir(parents=True,exist_ok=True)
(ROOT/'.build/reports/organization_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=True))
raise SystemExit(bool(errors))
