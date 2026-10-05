"""Check Ogg structure, cue paths and unchanged bilingual text, without game QA."""
from pathlib import Path
import hashlib
import json
import re
import struct

ROOT = Path(__file__).resolve().parents[1]
for output_folder in ('.build/reports', '.build/exports'):
    (ROOT / output_folder).mkdir(parents=True, exist_ok=True)


def ogg_info(path):
    data = path.read_bytes()
    offset, last_granule, first_packet = 0, 0, b''
    while offset < len(data):
        assert data[offset:offset+4] == b'OggS', path
        count = data[offset+26]
        laces = data[offset+27:offset+27+count]
        size = sum(laces)
        body = offset+27+count
        assert body+size <= len(data), path
        if not first_packet:
            first_packet = data[body:body+size]
        granule = struct.unpack_from('<Q', data, offset+6)[0]
        if granule != 0xffffffffffffffff:
            last_granule = granule
        offset = body+size
    assert first_packet.startswith(b'\x01vorbis'), path
    rate = struct.unpack_from('<I', first_packet, 12)[0]
    return {'seconds': round(last_granule/rate, 3), 'sample_rate': rate,
            'channels': first_packet[11], 'sha256': hashlib.sha256(data).hexdigest()}


runtime = (ROOT/'game/ch02_audio.rpy').read_text(encoding='utf-8')
match = re.search(r'    CH02_AUDIO = (\{.*?\n    \})', runtime, re.S)
import ast
audio = ast.literal_eval(match[1])
scripts = '\n'.join(p.read_text(encoding='utf-8') for p in sorted((ROOT/'game/scripts/ch02').glob('*.rpy')))
keys = set(re.findall(r'\$ ch02_audio\("([a-z_]+)"\)', scripts))
assert keys <= audio.keys(), keys-audio.keys()
assert set(audio) == keys, set(audio)-keys
assert audio['phone_ring'][2] is False, 'Phone ring must match Chapter 1 one-shot playback'
assert audio['notification'][2] is False
assert not re.search(r'^\s*(voice |\$ ch_voice\()', scripts, re.M)
assert '$ ch02_audio_stop("sound", 0)' in scripts.split('# ch02_sc01_016')[1].split('# ch02_sc01_017')[0]
scene1 = (ROOT/'game/scripts/ch02/sc01.rpy').read_text(encoding='utf-8')
incoming = scene1.split('# ch02_sc01_dir005')[1].split('# ch02_sc01_016')[0]
assert re.search(r'^    pause$', incoming, re.M), 'Incoming call must wait for player'
tv_shot = scene1.split('# ch02_sc01_dir002')[1].split('# ch02_sc01_005')[0]
assert 'scene ch02_cg television' in tv_shot and 'scene ch02_bg living' not in tv_shot
assert 'show ch02_chinatsu' not in tv_shot
files, missing = {}, []
for key, (path, channel, loop, volume) in audio.items():
    path = path.split('>', 1)[-1]
    if not (ROOT/'game'/path).exists():
        missing.append(path)
        continue
    files[path] = ogg_info(ROOT/'game'/path)
    assert files[path]['seconds'] > 0, path
for path in ('audio/bgm/ch01_daily_calm.ogg', 'audio/ambience/ch01_street_day.ogg'):
    files[path] = ogg_info(ROOT/'game'/path)
assert set(missing) <= {'audio/bgm/ch02_theater_ensemble.ogg'}, missing
assert files['audio/bgm/ch02_tv_piano.ogg']['seconds'] > 145
assert (ROOT/'game/audio/bgm/lobby.ogg').read_bytes() == (ROOT/'game/audio/bgm/ch02_tv_piano.ogg').read_bytes()
ja_hash = hashlib.sha256((ROOT/'scripts/ja/ch02.yaml').read_bytes()).hexdigest()
zh_hash = hashlib.sha256((ROOT/'scripts/zh/ch02.json').read_bytes()).hexdigest()
for p in (ROOT/'game/scripts/ch02').glob('*.rpy'):
    content = p.read_text(encoding='utf-8')
    assert ja_hash in content and zh_hash in content, p
report = {'ja_sha256': ja_hash, 'zh_sha256': zh_hash, 'voice_deferred': True,
          'audio_keys': sorted(keys), 'files': files, 'missing': missing,
          'license_check': 'deferred_by_user', 'listening_and_game_qa': 'user'}
(ROOT/'.build/reports/ch02_audio_check.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
