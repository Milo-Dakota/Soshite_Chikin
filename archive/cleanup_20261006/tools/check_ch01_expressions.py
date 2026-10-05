"""Inspect expression assets and staging without launching the engine."""
from pathlib import Path
import hashlib
import json
import re
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'assets/manifests/ch01_expression_imports.json').read_text(encoding='utf-8'))
assert hashlib.sha256((ROOT / 'script_ja/ch01.yaml').read_bytes()).hexdigest() == manifest['script_sha256']
runtime = (ROOT / 'game/ch01_runtime.rpy').read_text(encoding='utf-8')
scripts = '\n'.join(p.read_text(encoding='utf-8') for p in sorted((ROOT / 'game/scripts/ch01').glob('*.rpy')))
rows = []
for item in manifest['assets']:
    path = ROOT / item['game']
    im = Image.open(path)
    ref = Image.open(ROOT / item['reference'])
    assert im.size == ref.size == (1024, 1536)
    assert im.mode == 'RGBA' and im.getchannel('A').getextrema()[0] == 0
    character, expression = item['name'].split('_', 1)
    symbol = 'ch_' + character + ' ' + expression
    assert 'image ' + symbol + ' = ' in runtime
    assert re.search(r'^    show ' + re.escape(symbol) + r' at ', scripts, re.M), symbol
    assert path.read_bytes() == (ROOT / item['archive']).read_bytes()
    a, b = np.asarray(im).astype(float), np.asarray(ref).astype(float)
    # Compare body geometry below the head; do not rewrite generated pixels.
    mask_a, mask_b = a[300:, :, 3] > 128, b[300:, :, 3] > 128
    iou = float((mask_a & mask_b).sum() / (mask_a | mask_b).sum())
    assert iou > 0.98, (item['name'], iou)
    premul_a = a[300:, :, :3] * a[300:, :, 3:] / 255
    premul_b = b[300:, :, :3] * b[300:, :, 3:] / 255
    rows.append({'name': item['name'], 'file': item['game'], 'size': im.size,
                 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                 'body_alpha_iou': round(iou, 6),
                 'body_premultiplied_mean_absolute_difference': round(float(abs(premul_a-premul_b).mean()), 4)})
# All sprite changes must happen in background shots, never over a full-frame CG.
for script in sorted((ROOT / 'game/scripts/ch01').glob('*.rpy')):
    cg = False
    for line in script.read_text(encoding='utf-8').splitlines():
        if line.strip().startswith('scene '):
            cg = line.strip().startswith('scene ch_cg ')
        if re.match(r'\s+show ch_(qixing|chinatsu|maxi) ', line):
            assert not cg, (script.name, line)
assert len(rows) == 11
report = {'script_sha256': manifest['script_sha256'], 'expression_count': 11,
          'checks': ['canvas_and_alpha', 'body_silhouette_alignment', 'all_assets_used',
                     'archive_hash_matches', 'no_sprite_over_cg'],
          'runtime_tested': False, 'files': rows}
(ROOT / 'docs/reports/ch01_expression_check.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report))
