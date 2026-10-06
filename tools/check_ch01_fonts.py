"""Check actual fonts against the chapter's text; no engine launch."""
from pathlib import Path
import sys, json, re
ROOT = Path(__file__).resolve().parents[1]
for output_folder in ('.build/reports', '.build/exports'):
    (ROOT / output_folder).mkdir(parents=True, exist_ok=True)
import yaml
from fontTools.ttLib import TTFont

ja = yaml.safe_load((ROOT / 'scripts/ja/ch01.yaml').read_text(encoding='utf-8'))
zh = json.loads((ROOT / 'scripts/zh/ch01.json').read_text(encoding='utf-8-sig'))
entries = [e['ja'] for s in ja['scenes'] for e in s['entries'] if 'ja' in e]
ruby = re.compile(r'〖([^〖〗｜]+)｜([^〖〗｜]+)〗')
ui = '\n'.join((ROOT / p).read_text(encoding='utf-8') for p in ['game/screens.rpy', 'game/options.rpy', 'game/ch_main_menu.rpy', 'game/ch_menu_pages.rpy', 'game/ch_reading_bar.rpy'])
# Skip indicator uses the existing dedicated DejaVuSans symbol style.
ui_strings = ''.join(re.findall(r'"([^"\n]*)"', ui)).replace('▸', '')
samples = {
    'SourceHanSerifSC-Medium.otf': ''.join(zh['lines'].values()) + '徐启星千夏少女马皙郑局长梅川备代パンと、家出少女ジム馬皙',
    'SourceHanSerifJP-Medium.otf': ''.join(ruby.sub(lambda m: m[1], s) for s in entries),
    'SourceHanSansJP-Regular.otf': ''.join(m[2] for s in entries for m in ruby.finditer(s)) + 'チキン',
    'ShipporiMincho-SemiBold.ttf': 'そして只因もいなくなった第一章・終幕間帰り道',
    'SourceHanSansSC-Regular.otf': ui_strings + '鄭局長父さん着信連絡先発信通話',
}
report = {}
for filename, sample in samples.items():
    font = TTFont(ROOT / 'game/fonts' / filename)
    cmap = font.getBestCmap()
    missing = sorted({c for c in sample if ord(c) > 127 and ord(c) not in cmap})
    report[filename] = {'missing_glyphs': missing, 'weight': font['OS/2'].usWeightClass}
    font.close()
(ROOT / '.build/reports/ch01_font_check.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=True))
assert not any(r['missing_glyphs'] for r in report.values()), 'Missing glyphs in assigned font'
