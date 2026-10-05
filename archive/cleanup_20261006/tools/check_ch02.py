"""Check source/runtime mapping and prepare the Ren'Py chapter reading test."""
from pathlib import Path
import hashlib
import json
import re
import sys
import textwrap
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.build/deps'))
import yaml
from fontTools.ttLib import TTFont

ja = yaml.safe_load((ROOT / 'script_ja/ch02.yaml').read_text(encoding='utf-8'))
zh = json.loads((ROOT / 'script_zh/ch02.json').read_text(encoding='utf-8-sig'))
entries = [e for s in ja['scenes'] for e in s['entries'] if e['type'] != 'direction']
scripts = '\n'.join(p.read_text(encoding='utf-8') for p in sorted((ROOT / 'game/scripts/ch02').glob('*.rpy')))
ids = re.findall(r' id (ch02_sc\d\d_\d+)\s*$', scripts, re.M)
assert ids == [e['id'] for e in entries], 'Missing/reordered/duplicate runtime text'
assert len(ids) == 125
voice_calls = re.findall(r'^\s*\$ ch_voice\((None|\x27[^\x27]+\x27), "([^"]+)"\)', scripts, re.M)
assert voice_calls == [(repr(e['speaker']) if e['type'] == 'dialogue' else 'None', e['id']) for e in entries], 'Voice/silent line mapping'
shared = (ROOT / 'game/ch01_runtime.rpy').read_text(encoding='utf-8')
helpers = textwrap.dedent(shared.split('init python:\n', 1)[1].split('\ndefine ch_title_text', 1)[0])
voice_events, filters = [], []
fake = SimpleNamespace(
    music=SimpleNamespace(register_channel=lambda *a, **k: None,
        stop=lambda **k: voice_events.append(('stop', k)),
        set_audio_filter=lambda channel, effect: filters.append(effect)),
    audio=SimpleNamespace(filter=SimpleNamespace(Highpass=lambda f: ('highpass', f), Lowpass=lambda f: ('lowpass', f))),
    loadable=lambda path: (ROOT / 'game' / path).is_file())
namespace = {'renpy': fake, 'voice': lambda path: voice_events.append(('voice', path))}
exec(compile(helpers, '<shared audio routing>', 'exec'), namespace)
for e in entries:
    voice_events.clear()
    speaker = e['speaker'] if e['type'] == 'dialogue' else None
    namespace['ch_voice'](speaker, e['id'])
    path = next((f'audio/voice/{speaker}/{e["id"]}{ext}' for ext in ('.wav', '.ogg')
                 if speaker and (ROOT / f'game/audio/voice/{speaker}/{e["id"]}{ext}').is_file()), None)
    assert voice_events[0] == ('stop', {'channel': 'voice'})
    assert voice_events[1:] == ([('voice', path)] if path else []), e['id']
    telephone = e['id'] in ('ch02_sc01_016', 'ch02_sc01_017', 'ch02_sc08_004')
    assert filters[-1] == ([('highpass', 300), ('lowpass', 3400)] if telephone else None), e['id']
# Existing first-chapter OGG clips must still resolve through the shared helper.
for p in (ROOT / 'game/audio/voice').glob('*/ch01*.ogg'):
    voice_events.clear()
    namespace['ch_voice'](p.parent.name, p.stem)
    assert voice_events[-1] == ('voice', p.relative_to(ROOT / 'game').as_posix()), p
runtime = (ROOT / 'game/ch02_runtime.rpy').read_text(encoding='utf-8')
cg_names = set(re.findall(r'^image ch02_cg ([a-z_0-9]+)\s*=', runtime, re.M))
cg_shots = re.findall(r'^\s*scene ch02_cg ([a-z_0-9]+)', scripts, re.M)
assert set(cg_shots) <= cg_names, 'Missing CG declaration'
assert len(set(cg_shots)) == 17, 'Unexpected active CG states'
assert 'beidai_phone_recoil_v1' not in cg_shots
assert 'qixing_street_stopped_v1' not in cg_shots
scene5 = (ROOT/'game/scripts/ch02/sc05.rpy').read_text(encoding='utf-8')
assert 'show ch_qixing troubled at ch_left' in scene5.split('# ch02_sc05_dir007')[1]
scene7 = (ROOT/'game/scripts/ch02/sc07.rpy').read_text(encoding='utf-8')
after_assault = scene7.split('# ch02_sc07_dir007')[1].split('# ch02_sc07_dir009')[0]
assert 'show ch02_chinatsu dress_angry at ch_right' in after_assault
assert 'show ch02_beidai disheveled_furious at ch_left' in after_assault
assert 'ch02_chinatsu_face' not in scene7
assert after_assault.count('scene ch02_bg piano') == 1
assert not re.search(r'^\s*show ch02_handover', scripts, re.M), 'Retired handover still displayed'
pose_manifest = json.loads((ROOT/'assets/manifests/ch02_pose_sprite_imports.json').read_text(encoding='utf-8-sig'))
sprite_module = __import__('ch02_sprite_staging')
expression_manifest = json.loads((ROOT/'assets/manifests/ch02_expression_imports.json').read_text(encoding='utf-8-sig'))
expression_module = __import__('ch02_expression_staging')
for item in expression_manifest['images']:
    name = next(key for key, stem in expression_module.EXPRESSIONS.items() if stem == item['id'])
    assert f'image ch02_{name} =' in runtime, item['id']
    used = re.search(r'^\s*show ch02_' + re.escape(name) + r' at ', scripts, re.M)
    # TV CG now holds the first two lines, replacing this former sprite cue.
    unused = expression_module.RETIRED_EXPRESSIONS | {'chinatsu_indoor_awkward_v1'}
    assert bool(used) == (item['id'] not in unused), item['id']
for item in pose_manifest['images']:
    sprite_name = next(key for key, stem in sprite_module.SPRITES.items() if stem == item['id'])
    assert f'image ch02_{sprite_name} =' in runtime, item['id']
    names = [sprite_name] + [key for key, stem in expression_module.EXPRESSIONS.items()
                            if any(e['id'] == stem and e['refs'][0] == item['output'] for e in expression_manifest['images'])]
    if item['id'] in {'chinatsu_indoor_knees_closed_v1', 'beidai_home_phone_dismiss_v1'}:
        assert not any(re.search(r'^\s*show ch02_' + re.escape(name) + r' at ', scripts, re.M) for name in names), item['id']
    else:
        assert any(re.search(r'^\s*show ch02_' + re.escape(name) + r' at ', scripts, re.M) for name in names), item['id']
scene2 = (ROOT/'game/scripts/ch02/sc02.rpy').read_text(encoding='utf-8')
scene3 = (ROOT/'game/scripts/ch02/sc03.rpy').read_text(encoding='utf-8')
assert 'scene ch02_bg entry_shoes' in scene2
assert 'scene ch02_bg entry_shoes' not in scene3
assert 'show ch02_chinatsu' not in scene2.split('# ch02_sc02_dir004')[1]
scene8 = (ROOT/'game/scripts/ch02/sc08.rpy').read_text(encoding='utf-8')
assert scene8.index('hide ch02_house_servant') < scene8.index('# ch02_sc08_004')
assert 'show ch02_beidai phone_afraid at ch02_phone_recoil' in scene8
for e in entries:
    assert json.dumps(zh['lines'][e['id']].replace('[', '[['), ensure_ascii=False) in scripts, e['id']
manifest = json.loads((ROOT / 'docs/reports/ch02_build_check.json').read_text(encoding='utf-8'))
for asset in manifest['assets']:
    assert hashlib.sha256((ROOT / asset['runtime']).read_bytes()).hexdigest() == asset['sha256']

ruby = re.compile(r'〖([^〖〗｜]+)｜([^〖〗｜]+)〗')
samples = {
    'SourceHanSerifSC-Medium.otf': ''.join(zh['lines'].values()) + zh['chapter_title_zh'] + ja['title_ja'] + '第一章第二章徐启星千夏马皙文钢剧院工作人员司机梅川备代佣人电话里的声音寻人启事幕间琴房深夜回到视点',
    'SourceHanSerifJP-Medium.otf': ''.join(ruby.sub(lambda m: m[1], e['ja']) for e in entries),
    'SourceHanSansJP-Regular.otf': ''.join(m[2] for e in entries for m in ruby.finditer(e['ja'])),
    'ShipporiMincho-SemiBold.ttf': '第二章終幕間千夏梅川邸杏城徐启星二日後朝',
}
fonts = {}
for name, sample in samples.items():
    with TTFont(ROOT / 'game/fonts' / name) as font:
        cmap = font.getBestCmap()
        fonts[name] = sorted({c for c in sample if ord(c) > 127 and ord(c) not in cmap})
assert not any(fonts.values()), fonts

helper = '''# Generated by tools/check_ch02.py. Only executes under Ren'Py test runner.
init python:
    def ch02_test_reading_line(lid):
        assert ch_line_id == lid
        assert ch_chapter_label == "第二章"
        # Voice clips may have already finished; unvoiced text must stay silent.
        if lid not in CH02_TEST_VOICED_IDS:
            assert not renpy.music.get_playing(channel="voice"), lid
        primary = renpy.get_widget("ch_say", "what")
        secondary = renpy.get_widget("ch_say", "ch_japanese")
        assert primary is not None and secondary is not None, lid
        pw, ph = renpy.render(primary, 1648, 1080, 0, 0).get_size()
        jw, jh = renpy.render(secondary, 1648, 1080, 0, 0).get_size()
        assert ph + 8 + jh <= 214, (lid, ph, jh)
        assert pw <= 1648 and jw <= 1648, (lid, pw, jw)
        return True

testcase ch02_reading:
    $ preferences.text_cps = 0
    $ _test.screenshot_directory = "docs/reports/ch02_runtime_screens"
    run Start("ch02_start")
'''
voiced_ids = [e['id'] for e in entries if e['type'] == 'dialogue' and any(
    (ROOT / 'game/audio/voice' / e['speaker'] / (e['id'] + ext)).is_file() for ext in ('.wav', '.ogg'))]
helper = 'define CH02_TEST_VOICED_IDS = ' + repr(voiced_ids) + '\n' + helper
shots = {'ch02_sc01_007', 'ch02_sc01_011', 'ch02_sc03_006', 'ch02_sc04_011',
         'ch02_sc05_004', 'ch02_sc05_009', 'ch02_sc05_012', 'ch02_sc06_001',
         'ch02_sc06_018', 'ch02_sc07_008', 'ch02_sc08_004', 'ch02_sc09_018'}
for e in entries:
    lid = e['id']
    helper += f'    advance until eval (ch_line_id == "{lid}") timeout 30.0\n'
    helper += f'    assert eval ch02_test_reading_line("{lid}")\n'
    if lid in shots:
        helper += f'    screenshot "{lid}.png"\n'
helper += '''    advance until screen "ch_caption" timeout 30.0
    screenshot "ending.png"
    advance until screen "main_menu" timeout 30.0
    assert screen "main_menu"

testcase ch02_entry:
    run Start()
    advance until eval (ch_line_id == "ch01_sc01_001") timeout 30.0
    assert eval (ch_chapter_label == "第一章")
    run Jump("entry_ch01_sc06_return")
    advance until eval (ch_line_id == "ch02_sc01_001") timeout 30.0
    assert eval ch02_test_reading_line("ch02_sc01_001")
'''
(ROOT / '.build/testcases').mkdir(parents=True, exist_ok=True)
(ROOT / '.build/testcases/ch02_reading.rpy').write_text(helper, encoding='utf-8')
report = {'exact_text_id_order': True, 'translated_lines': len(ids), 'runtime_image_hashes': 'all_%d_match' % len(manifest['assets']),
          'voice_deferred': False, 'supplied_voice_lines': len(voiced_ids), 'non_voice_audio_enabled': True, 'cg_references_declared': True, 'cg_shots': len(cg_shots), 'missing_font_glyphs': fonts,
          'voice_routing_and_telephone_filter': 'passed_fake_engine', 'first_chapter_ogg_routing': 'passed_fake_engine',
          'runtime_test_prepared': '.build/testcases/ch02_reading.rpy'}
(ROOT / 'docs/reports/ch02_integration_check.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=True))
