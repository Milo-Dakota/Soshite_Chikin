"""Static screen-link and lexical checks, not Ren'Py runtime validation."""
from pathlib import Path
import io, json, re, tokenize
from collections import Counter

root = Path(__file__).resolve().parents[1]
for output_folder in ('.build/reports', '.build/exports'):
    (root / output_folder).mkdir(parents=True, exist_ok=True)
paths = [root / 'game' / n for n in ('screens.rpy', 'ch_main_menu.rpy', 'ch_menu_pages.rpy', 'ch_reading_bar.rpy', 'ch_splash.rpy')]
sources = [p.read_text(encoding='utf-8-sig') for p in paths]
names = [n for s in sources for n in re.findall(r'^screen (\w+)\(', s, re.M)]
identities = []
for source in sources:
    for match in re.finditer(r'^screen (\w+)\([^\n]*\):\s*\n((?:[ \t]+[^\n]*\n|\n)*)', source, re.M):
        variant = re.search(r'^    variant "([^"]+)"', match[2], re.M)
        identities.append((match[1], variant[1] if variant else 'default'))
duplicates = [n for n, count in Counter(identities).items() if count > 1]
assert not duplicates, duplicates
for p, s in zip(paths, sources):
    list(tokenize.generate_tokens(io.StringIO(s).readline))
    # add accepts transform properties, not container fill style properties.
    assert not re.search(r'^\s*add\b[^\n]*\b(?:xfill|yfill)\b', s, re.M), p.name
refs = {n for s in sources for n in re.findall(r'\b(?:use\s+|ShowMenu\("|Show\(")(ch_\w+)', s)}
missing = sorted(refs - set(names))
assert not missing, missing
assert (root / 'game/images/ui/menu_theatre_v1.png').is_file()
report = {'duplicate_screens': duplicates, 'missing_custom_screens': missing,
          'lexical_checks': [p.name for p in paths], 'runtime_tested': False,
          'layout_tested': False, 'save_load_executed': False}
(root / '.build/reports/menu_pages_check.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report))
