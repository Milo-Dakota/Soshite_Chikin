"""Verify organized documentation, asset provenance and the preserved game snapshot."""
from pathlib import Path
from urllib.parse import unquote
import ast
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

errors = []
links = 0
for folder in ['docs', 'assets', 'tools']:
    for path in (ROOT / folder).rglob('*.md'):
        if 'archive' in path.relative_to(ROOT).parts:
            continue
        text = path.read_text(encoding='utf-8-sig')
        for match in re.finditer(r'\]\(([^)]+)\)', text):
            target = unquote(match[1].strip('<>')).split('#', 1)[0]
            if not target or re.match(r'\w+://', target):
                continue
            links += 1
            if not (path.parent / target).exists():
                errors.append(f'Broken link: {path.relative_to(ROOT)} -> {target}')

manifest_count = 0
for path in sorted((ROOT / 'assets/manifests').glob('*.json')):
    payload = json.loads(path.read_text(encoding='utf-8-sig'))
    entries = payload if isinstance(payload, list) else payload.get('assets', [payload])
    for row in entries:
        for key in ['archive', 'game', 'reference']:
            if key in row:
                manifest_count += 1
                if not (ROOT / row[key]).is_file():
                    errors.append(f'Missing {key}: {row[key]}')
        for reference in row.get('references', []):
            if not (ROOT / reference).is_file():
                errors.append(f'Missing reference: {reference}')

inventory = json.loads((ROOT / 'assets/inventory.json').read_text(encoding='utf-8'))
for row in inventory['files']:
    path = ROOT / row['file']
    if not path.is_file() or sha(path) != row['sha256']:
        errors.append(f'Changed inventory asset: {row["file"]}')
    for copy in row['preserved_copies']:
        if not (ROOT / copy).is_file() or sha(ROOT / copy) != row['sha256']:
            errors.append(f'Mismatched preserved copy: {copy}')
    for record in row['provenance_records']:
        if not (ROOT / record).is_file():
            errors.append(f'Missing provenance: {record}')

baseline = json.loads((ROOT / 'docs/release/workspace_manifest.json').read_text(encoding='utf-8'))['files']
current = {p.relative_to(ROOT).as_posix(): sha(p) for p in (ROOT / 'game').rglob('*')
           if p.is_file() and not {'saves', 'cache', '__pycache__'} & set(p.relative_to(ROOT / 'game').parts)}
differences = sorted(k for k in set(baseline) | set(current) if baseline.get(k) != current.get(k))
errors.extend('Runtime snapshot differs: ' + k for k in differences)

moves = json.loads((ROOT / 'docs/reports/organization_moves.json').read_text(encoding='utf-8'))
for old, new in moves.items():
    if not (ROOT / new).is_file():
        errors.append('Missing moved destination: ' + new)
for path in (ROOT / 'tools').glob('*.py'):
    text = path.read_text(encoding='utf-8')
    ast.parse(text, filename=str(path))
    for old in moves:
        if old in text:
            errors.append(f'Stale tool reference: {path.name}: {old}')
    # Inspect static report destinations without running exporters that modify the game.
    for match in re.finditer(r"['\"](docs/[^'\"]+)['\"]", text):
        if not (ROOT / match[1]).parent.is_dir():
            errors.append('Missing report directory: ' + match[1])

report = {'markdown_links_checked': links, 'manifest_paths_checked': manifest_count,
          'inventory_files_checked': len(inventory['files']),
          'runtime_files_unchanged': len(current) if not differences else False,
          'moved_files': len(moves), 'errors': errors,
          'checks': ['local_markdown_links', 'provenance_paths', 'inventory_hashes',
                     'preserved_copy_hashes', 'runtime_snapshot', 'tool_syntax', 'tool_report_paths'],
          'engine_launched': False, 'published_package_verified': False}
(ROOT / 'docs/reports/organization_check.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False))
if errors:
    raise SystemExit(1)
