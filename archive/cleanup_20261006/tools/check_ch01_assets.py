"""Read-only resource/font checks, with a report and embedded font license export."""
from pathlib import Path
import hashlib
import json
import re
import sys
import ast
import textwrap
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.build/deps'))
from fontTools.ttLib import TTFont
from PIL import Image

runtime = (ROOT / 'game/ch01_runtime.rpy').read_text(encoding='utf-8')
paths = sorted(set(re.findall(r'"(images/ch01/[^"\n]+)"', runtime)))
missing = [p for p in paths if not (ROOT / 'game' / p).is_file()]
images = []
for path in paths:
    full = ROOT / 'game' / path
    if not full.is_file():
        continue
    with Image.open(full) as im:
        row = {'file': path, 'size': im.size, 'mode': im.mode}
        if 'A' in im.getbands():
            row['alpha_range'] = im.getchannel('A').getextrema()
        images.append(row)

font = TTFont(ROOT / 'game/SourceHanSansLite.ttf')
copyright_text = '\n'.join(dict.fromkeys(n.toUnicode() for n in font['name'].names if n.nameID == 0))
notice = ('Font supplied with the existing project: SourceHanSansLite.ttf\n'
          'Not modified by this project. Embedded copyright notice:\n' + copyright_text + '\n\n'
          'License: SIL Open Font License 1.1. See SourceHanSans-OFL.txt.\n'
          'Upstream license source: https://github.com/adobe-fonts/source-han-sans/blob/release/LICENSE.txt\n'
          'Font SHA-256: ' + hashlib.sha256((ROOT / 'game/SourceHanSansLite.ttf').read_bytes()).hexdigest() + '\n')
(ROOT / 'game/licenses/SourceHanSansLite-NOTICE.txt').write_text(notice, encoding='utf-8')
cmap = font.getBestCmap()
manifest = json.loads((ROOT / 'voice/ch01_manifest.json').read_text(encoding='utf-8'))
scripts = '\n'.join(p.read_text(encoding='utf-8') for p in (ROOT / 'game/scripts/ch01').glob('*.rpy'))
quoted = r'("(?:\\.|[^"\\])*")'
say_pairs = re.findall(r'^    ch_\w+ ' + quoted + r' \(show_ja_text=' + quoted + r'\) id (ch01_\w+)$', scripts, re.M)
texts = [json.loads(t) for zh, ja, _ in say_pairs for t in (zh, ja)]
texts += ['そして只因チキンもいなくなった第一章終パンと、家出少女幕間帰り道ジム徐启星千夏馬皙鄭局長梅川備代着信連絡先父さん発信通話']
display = re.sub(r'\{[^}]*\}', '', ''.join(texts))
missing_glyphs = sorted({c for c in display if ord(c) > 127 and ord(c) not in cmap})
license_texts = list(dict.fromkeys(n.toUnicode() for n in font['name'].names if n.nameID == 13))
full_license = next((t for t in license_texts if 'PREAMBLE' in t and 'DISCLAIMER' in t), None)
if full_license:
    license_path = ROOT / 'game/licenses/SourceHanSansLite-OFL.txt'
    copyright_text = '\n'.join(dict.fromkeys(n.toUnicode() for n in font['name'].names if n.nameID == 0))
    license_path.write_text(copyright_text + '\n\n' + full_license, encoding='utf-8')

defined_images = set(re.findall(r'^image (.+?) =', runtime, re.M))
used_images = set(re.findall(r'^    (?:show|scene) (ch_(?:bg|cg|qixing|chinatsu|maxi|beidai) \w+)', scripts, re.M))
undefined = sorted(used_images - defined_images)
say_ids = [line_id for _, _, line_id in say_pairs]
# Regressions reported during the user's first playtest: no default say style,
# and Ruby styles must exist before screens.rpy's init offset -1.
characters = re.findall(r'^define ch_\w+ = Character\(.*\)$', runtime, re.M)
assert len(characters) == 7 and all('what_style="ch_dialogue"' in c for c in characters)
assert all('who_style="ch_name"' in c and 'who_size=26' in c for c in characters)
import xml.etree.ElementTree as ET
panel = ET.parse(ROOT / 'game/gui/reading_panel_a.svg').getroot()
assert panel.attrib['width'] == '1776' and panel.attrib['height'] == '350'
assert 'background "gui/reading_panel_a.svg"' in runtime
assert re.search(r'init -2:\s+style ch_ruby is default:', runtime)
assert 'yoffset -38' in runtime
assert 'style ch_subtitle_ruby is ch_ruby:' in runtime and 'yoffset -26' in runtime
# Each save/history entry carries the two languages together; no screen-global
# line lookup can accidentally show the current Japanese beneath an older line.
translated = json.loads((ROOT / 'script_zh/ch01.json').read_text(encoding='utf-8-sig'))
assert translated['source_ja_sha256'].lower() == hashlib.sha256((ROOT / 'script_ja/ch01.yaml').read_bytes()).hexdigest()
assert {line_id for _, _, line_id in say_pairs} == set(translated['lines'])
for encoded_zh, encoded_ja, line_id in say_pairs:
    zh, ja = json.loads(encoded_zh), json.loads(encoded_ja)
    assert zh == translated['lines'][line_id].replace('[', '[['), line_id
    assert ja.startswith('{size=24}{color=#aebdce}') and ja.endswith('{/color}{/size}'), line_id
    assert '{cps=' not in ja and '{cps=' not in zh, line_id
screens = (ROOT / 'game/screens.rpy').read_text(encoding='utf-8')
assert 'text what id "what"' in runtime, 'Native say widget must receive exact what'
assert 'screen ch_say(who, what, ja_text="", retained=False,' in runtime
assert 'what.partition(' not in runtime
assert 'get("ja_text", "")' in screens and 'filter_text_tags(history_bilingual' in screens
assert '"size", "color"' in screens and 'ruby_style style.ch_subtitle_ruby' in screens
assert '"font"' in screens, 'History must preserve the Japanese font tag'
import runpy
runpy.run_path(str(ROOT / 'tools/check_ch01_fonts.py'))

# Exercise optional-audio control flow with a fake engine, without playing audio
# or launching Ren'Py. This verifies routing, not engine compatibility or sound.
calls, playing, available = [], {}, set()
def play(path, **kw):
    calls.append(('play', path, kw))
    playing[kw['channel']] = path
def stop(**kw):
    calls.append(('stop', kw))
    playing.pop(kw['channel'], None)
fake = SimpleNamespace(music=SimpleNamespace(register_channel=lambda *a, **k: None,
                        play=play, stop=stop, get_playing=lambda channel: playing.get(channel),
                        set_audio_filter=lambda channel, effect: filter_calls.append((channel, effect))),
                       audio=SimpleNamespace(filter=SimpleNamespace(
                           Highpass=lambda frequency: ('highpass', frequency),
                           Lowpass=lambda frequency: ('lowpass', frequency))),
                       loadable=lambda path: path in available)
filter_calls = []
helpers = textwrap.dedent(runtime.split('init python:\n', 1)[1].split('\ndefine ch_title_text', 1)[0])
ast.parse(helpers)
# Ren'Py exposes voice() in the store, not renpy.exports. Do not add a
# nonexistent renpy.voice to the fake: that previously masked a runtime crash.
namespace = {'renpy': fake, 'voice': lambda path: calls.append(('voice', path))}
exec(compile(helpers, '<audio helpers>', 'exec'), namespace)
namespace['ch_voice']('zheng', 'ch01_sc02_011')
assert filter_calls[-1] == ('voice', [('highpass', 300), ('lowpass', 3400)])
namespace['ch_voice']('zheng', 'future_in_person_line')
assert filter_calls[-1] == ('voice', None)
namespace['ch_voice'](None, '')
assert filter_calls[-1] == ('voice', None)
calls.clear()
for speaker in (None, 'qixing', 'chinatsu'):
    namespace['ch_voice'](speaker, 'missing')
assert all(call[0] == 'stop' for call in calls)
voice_path = 'audio/voice/chinatsu/ch01_sc01_006.ogg'
available.add(voice_path)
namespace['ch_voice']('chinatsu', 'ch01_sc01_006')
assert calls[-1] == ('voice', voice_path)
# Check all supplied voices through the same helper, including silent lines.
for row in manifest['lines']:
    path = row['output_path'].removeprefix('game/')
    assert (ROOT / 'game' / path).is_file(), path
    available.add(path)
    namespace['ch_voice'](row['character'], row['line_id'])
    assert calls[-1] == ('voice', path)
    for silent_speaker in (None, 'qixing'):
        calls.clear()
        namespace['ch_voice'](silent_speaker, row['line_id'])
        assert calls == [('stop', {'channel': 'voice'})]
calls.clear()
namespace['ch_audio']('daily')
assert calls[-1][0] == 'stop'
available.add(namespace['CH_AUDIO']['daily'][0])
namespace['ch_audio']('daily')
count = len(calls)
namespace['ch_audio']('daily')
assert len(calls) == count, 'Same looping music must not restart'
namespace['ch_stop_audio']()
assert not playing
# All supplied room tones share the ambience channel, never the music channel.
for key in ('street_room', 'gym_room', 'restaurant_room', 'shower'):
    path, channel, loop, volume = namespace['CH_AUDIO'][key]
    assert (ROOT / 'game' / path).is_file(), path
    assert channel == 'ch_ambience' and loop
    available.add(path)
    namespace['ch_audio'](key)
    assert playing['ch_ambience'] == path
    assert calls[-1][2]['fadeout'] == 0.6
# Non-dialogue pauses preserve the bilingual text without adding history.
keeper = textwrap.dedent(runtime.split('init python:\n    def ch_keep_dialogue_window', 1)[1].split('\ndefine config.empty_window', 1)[0])
keeper = 'def ch_keep_dialogue_window' + keeper
shown = []
history = [SimpleNamespace(who='test', what='Chinese', show_args={'ja_text': 'Japanese'}, who_args={'color': '#ffffff'})]
keeper_ns = {'_history_list': history, 'renpy': SimpleNamespace(
    show_screen=lambda *a, **kw: shown.append(kw), shown_window=lambda: None)}
exec(compile(keeper, '<retained dialogue>', 'exec'), keeper_ns)
keeper_ns['ch_keep_dialogue_window']()
assert shown[-1]['what'] == 'Chinese' and shown[-1]['ja_text'] == 'Japanese'
assert shown[-1]['retained'] and len(history) == 1
history.clear()
keeper_ns['ch_keep_dialogue_window']()
assert shown[-1]['what'] == ''
card = runtime.split('label ch_card(', 1)[1]
assert card.index('scene black') < card.index('hide screen ch_caption')
assert 'window auto' not in scripts
report = {'images': images, 'missing_files': missing, 'undefined_images': undefined,
          'missing_glyphs': missing_glyphs,
          'font_license_available': (ROOT / 'game/licenses/SourceHanSans-OFL.txt').is_file(),
          'regression_checks': ['character_style_binding', 'ruby_init_priority', 'optional_audio_fake_engine', '97_bilingual_pairs', 'translation_source_hash', 'history_subtitle_style', 'ambience_routing', 'retained_bilingual_window', 'title_clears_old_scene'],
          'say_count': len(say_ids), 'unique_say_ids': len(set(say_ids)),
          'source_novel_sha256': hashlib.sha256((ROOT / 'source/novel.txt').read_bytes()).hexdigest(),
          'agent_runtime_tested': False, 'agent_rendering_tested': False,
          'user_confirmed': ['startup', 'title_ruby', 'dialogue_ruby']}
(ROOT / 'docs/reports/ch01_resource_check.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=True))
assert not missing, missing
assert not undefined, undefined
assert not missing_glyphs, missing_glyphs
assert len(say_ids) == len(set(say_ids)) == 97
