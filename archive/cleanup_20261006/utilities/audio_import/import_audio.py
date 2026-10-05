"""Import root audio/ originals; normalize BGM/voice, copy ambience/SFX.

Standard-library Python + FFmpeg only. No modification of input files.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CATEGORIES = ('bgm', 'voice', 'ambience', 'sfx')
EXTENSIONS = {'.wav', '.ogg', '.mp3', '.flac', '.opus', '.mp2'}
VERSION = 1


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.audio-report-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            json.dump(data, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write('\n')
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)


def run(executable, arguments):
    result = subprocess.run([str(executable), '-hide_banner', '-nostdin', '-nostats', *arguments],
                            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
    output = result.stderr.decode('utf-8', errors='replace')
    if result.returncode:
        raise RuntimeError(output[-2400:])
    return output


def measure(executable, path, settings):
    filter_text = 'loudnorm=I={integrated_lufs}:TP={true_peak_dbtp}:LRA=50:print_format=json'.format(**settings)
    output = run(executable, ['-i', str(path), '-map', '0:a:0', '-af', filter_text, '-f', 'null', '-'])
    blocks = re.findall(r'\{\s*"input_i".*?\}', output, re.S)
    if not blocks:
        raise ValueError(f'Cannot measure loudness: {path}')
    raw = json.loads(blocks[-1])
    numbers = {k: float(raw[k]) for k in ('input_i', 'input_tp', 'input_lra', 'input_thresh', 'target_offset')}
    # Read source sample rate from the audio stream, preserving pitch/timebase.
    rate_match = re.search(r'Stream #.*?Audio:.*?,\s*(\d+) Hz', output)
    if not rate_match:
        raise ValueError(f'Cannot read sample rate: {path}')
    numbers['sample_rate'] = int(rate_match[1])
    duration = re.search(r'Duration: (\d+):(\d+):([\d.]+)', output)
    if duration:
        numbers['duration_seconds'] = int(duration[1]) * 3600 + int(duration[2]) * 60 + float(duration[3])
    return numbers


def public_measurement(value):
    return {k: (round(v, 3) if isinstance(v, float) and math.isfinite(v) else
                None if isinstance(v, float) else v) for k, v in value.items()}


def codec(extension):
    return {
        '.wav': ['-c:a', 'pcm_s16le'], '.ogg': ['-c:a', 'libvorbis', '-q:a', '6'],
        '.mp3': ['-c:a', 'libmp3lame', '-q:a', '2'], '.flac': ['-c:a', 'flac'],
        '.opus': ['-c:a', 'libopus', '-b:a', '128k'], '.mp2': ['-c:a', 'mp2', '-b:a', '192k'],
    }[extension]


def voice_catalog(root):
    result = {}
    for manifest in sorted((root / 'voice').glob('ch*_manifest.json')):
        data = json.loads(manifest.read_text(encoding='utf-8-sig'))
        chapter = data['chapter_id']
        script = root / 'script_ja' / (chapter + '.yaml')
        rows = data.get('lines', data.get('rows', []))
        result[chapter] = (script.is_file() and digest(script) == data.get('script_sha256'),
                           {row['line_id']: row for row in rows})
    return result


def scan(root, validate):
    source_root, output_root = root / 'audio', root / 'game/audio'
    if not source_root.resolve().is_relative_to(root) or not output_root.resolve().is_relative_to(root):
        raise ValueError('audio/ and game/audio/ must remain inside the project')
    if source_root.resolve() == output_root.resolve():
        raise ValueError('Originals and game output must be separate directories')
    catalog = voice_catalog(root) if validate else {}
    items, identities = [], set()
    for source in sorted(source_root.rglob('*')):
        if not source.is_file() or source.suffix.lower() not in EXTENSIONS:
            continue
        relative = source.relative_to(source_root)
        category = relative.parts[0]
        if category not in CATEGORIES:
            raise ValueError(f'Audio must be under bgm/voice/ambience/sfx: {relative}')
        if source.is_symlink() or not source.resolve().is_relative_to(source_root.resolve()):
            raise ValueError(f'Input must stay inside audio/: {relative}')
        output = output_root / relative
        if not output.resolve().is_relative_to(output_root.resolve()):
            raise ValueError(f'Output escapes game/audio/: {relative}')
        identity = str(relative.with_suffix('')).casefold()
        if identity in identities:
            raise ValueError(f'Two source formats share one filename; keep only one: {relative}')
        identities.add(identity)
        if category == 'voice':
            if source.suffix.lower() not in ('.wav', '.ogg'):
                raise ValueError(f'Voice playback currently supports WAV/OGG filenames only: {relative}')
            if len(relative.parts) != 3:
                raise ValueError(f'Voice needs voice/<character>/<line_id>.<extension>: {relative}')
            if validate:
                lid, speaker = source.stem, relative.parts[1]
                chapter = lid.split('_')[0]
                current, rows = catalog.get(chapter, (False, {}))
                if not current:
                    raise ValueError(f'Missing/stale voice/{chapter}_manifest.json; export current recording manifest first')
                row = rows.get(lid)
                if not row or speaker == 'qixing' or row.get('character', row.get('speaker')) != speaker:
                    raise ValueError(f'Not an approved voiced dialogue ID/speaker: {relative}')
            if output.parent.exists():
                collisions = [p for p in output.parent.iterdir() if p.is_file() and p.stem.casefold() == source.stem.casefold()
                              and p.suffix.lower() in EXTENSIONS and p.name.casefold() != output.name.casefold()]
                if collisions:
                    raise ValueError(f'Old alternate voice format would mask/conflict with new file: {collisions[0]}; archive it first')
        items.append((source, output, category, relative.as_posix()))
    return items


def process(executable, source, target, settings, max_boost):
    before = measure(executable, source, settings)
    if not math.isfinite(before['input_i']) or not math.isfinite(before['input_tp']):
        raise ValueError(f'Unmeasurable/silent audio; not automatically amplified: {source.name}')
    requested = settings['integrated_lufs']
    effective = min(requested, before['input_i'] + max_boost)
    working = {**settings, 'integrated_lufs': effective}
    if effective != requested:
        before = measure(executable, source, working)
    # LRA target never contracts the source range. FFmpeg uses linear gain when
    # peak headroom allows it, otherwise its dynamic true-peak limiter applies.
    lra = min(50.0, max(11.0, before['input_lra']))
    filter_text = (
        f'loudnorm=I={effective}:TP={settings["true_peak_dbtp"]}:LRA={lra}:'
        f'measured_I={before["input_i"]}:measured_TP={before["input_tp"]}:'
        f'measured_LRA={before["input_lra"]}:measured_thresh={before["input_thresh"]}:'
        f'offset={before["target_offset"]}:linear=true:print_format=json')
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.audio-import-', suffix=target.suffix, dir=target.parent)
    os.close(fd)
    temporary = Path(name)
    try:
        output = run(executable, ['-y', '-i', str(source), '-map', '0:a:0', '-vn', '-map_metadata', '0',
                                 '-af', filter_text, '-ar', str(48000 if target.suffix.lower() == '.opus' else before['sample_rate']), *codec(target.suffix.lower()), str(temporary)])
        raw = json.loads(re.findall(r'\{\s*"input_i".*?\}', output, re.S)[-1])
        after = measure(executable, temporary, working)
        # Recheck the encoded file, including lossy-codec peak overshoot.
        # A fixed attenuation, if needed, preserves its processed dynamics.
        correction = 0.0
        for attempt in range(3):
            if after['input_tp'] <= settings['true_peak_dbtp'] + 0.05:
                break
            adjustment = settings['true_peak_dbtp'] - after['input_tp'] - 0.5
            corrected = temporary.with_name(temporary.stem + '-corrected' + temporary.suffix)
            try:
                run(executable, ['-y', '-i', str(temporary), '-map', '0:a:0', '-af', f'volume={adjustment}dB',
                                 '-ar', str(after['sample_rate']), *codec(target.suffix.lower()), str(corrected)])
                os.replace(corrected, temporary)
                after = measure(executable, temporary, working)
                correction += adjustment
            finally:
                corrected.unlink(missing_ok=True)
        if after['input_tp'] > settings['true_peak_dbtp'] + 0.3:
            raise ValueError(f'Encoded true peak {after["input_tp"]} exceeds ceiling {settings["true_peak_dbtp"]}: {source.name}')
        if abs(after.get('duration_seconds', 0) - before.get('duration_seconds', 0)) > 0.15:
            raise ValueError(f'Output duration unexpectedly changed: {source.name}')
        os.replace(temporary, target)
        return dict(before=public_measurement(before), after=public_measurement(after), requested_lufs=requested,
                    effective_target_lufs=effective, normalization_type=raw.get('normalization_type'),
                    post_encode_attenuation_db=round(correction, 3),
                    warning='Final loudness differs from target; inspect short clip/peak limit' if abs(after['input_i'] - requested) > 1.0 else None)
    finally:
        temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='Project root (also useful for isolated verification)')
    parser.add_argument('--config', type=Path, default=HERE / 'config.json')
    parser.add_argument('--ffmpeg', help='Override configured FFmpeg executable')
    parser.add_argument('--dry-run', action='store_true', help='Validate and list; no output/report writes')
    parser.add_argument('--force', action='store_true', help='Reprocess unchanged sources')
    args = parser.parse_args()
    root = args.root.resolve()
    config = json.loads(args.config.read_text(encoding='utf-8-sig'))
    for category in ('voice', 'bgm'):
        settings = config[category]
        if not -70 <= settings['integrated_lufs'] <= -5 or not -9 <= settings['true_peak_dbtp'] <= 0:
            raise ValueError(f'Invalid loudness/peak target: {category}')
    if not 0 <= config['max_boost_db'] <= 24:
        raise ValueError('max_boost_db must be 0..24')
    executable = args.ffmpeg or config.get('ffmpeg') or shutil.which('ffmpeg')
    if not executable or not (Path(executable).is_file() or shutil.which(executable)):
        raise ValueError('FFmpeg not found; set ffmpeg in config.json or use --ffmpeg')
    run(executable, ['-version'])
    # -version is normally on stdout, intentionally suppressed; binary hash
    # includes encoder changes in the incremental-processing fingerprint.
    binary = Path(shutil.which(executable) or executable)
    fingerprint = hashlib.sha256(json.dumps(dict(version=VERSION, implementation_sha256=digest(Path(__file__)), config=config, ffmpeg_sha256=digest(binary)), sort_keys=True).encode()).hexdigest()
    items = scan(root, config.get('validate_voice_ids', True))
    if not items:
        print('No audio files found in root audio/. Place originals under bgm/voice/ambience/sfx.')
        return 0
    report_path = root / 'docs/reports/audio_import.json'
    previous = json.loads(report_path.read_text(encoding='utf-8')) if report_path.exists() else {}
    old = previous.get('files', {})
    report = dict(version=VERSION, updated_at=datetime.now(timezone.utc).isoformat(), fingerprint=fingerprint,
                  source='audio/', destination='game/audio/', files={}, errors=[], counts=dict(normalized=0, copied=0, skipped=0))
    for source, target, category, relative in items:
        source_hash = digest(source)
        cached = old.get(relative, {})
        unchanged = (not args.force and previous.get('fingerprint') == fingerprint and cached.get('source_sha256') == source_hash
                     and target.is_file() and cached.get('output_sha256') == digest(target))
        action = 'skip' if unchanged else 'normalize' if category in ('bgm', 'voice') else 'copy'
        print(f'{action.upper():9} {relative}', flush=True)
        if args.dry_run:
            continue
        try:
            if unchanged:
                report['files'][relative] = cached
                report['counts']['skipped'] += 1
                continue
            if action == 'normalize':
                details = process(executable, source, target, config[category], config['max_boost_db'])
                report['counts']['normalized'] += 1
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                fd, name = tempfile.mkstemp(prefix='.audio-copy-', suffix=target.suffix, dir=target.parent)
                os.close(fd)
                try:
                    shutil.copyfile(source, name)
                    os.replace(name, target)
                finally:
                    Path(name).unlink(missing_ok=True)
                details = {}
                report['counts']['copied'] += 1
            report['files'][relative] = dict(source_sha256=source_hash, output_sha256=digest(target), action=action, **details)
        except (ValueError, RuntimeError, OSError) as error:
            report['errors'].append(dict(path=relative, error=str(error)))
            print(f'FAILED: {relative}: {error}', file=sys.stderr)
    if not args.dry_run:
        write_json(report_path, report)
        print(json.dumps(dict(counts=report['counts'], failures=len(report['errors'])), ensure_ascii=False))
        print(f'Report: {report_path}')
    return 1 if report['errors'] else 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    try:
        sys.exit(main())
    except (ValueError, OSError, RuntimeError, KeyError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        sys.exit(1)
