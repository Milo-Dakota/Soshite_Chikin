"""Measure chapter voice loudness without changing audio or playback gain."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import re
import statistics
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
for output_folder in ('.build/reports', '.build/exports'):
    (ROOT / output_folder).mkdir(parents=True, exist_ok=True)


def main():
    executable = sys.argv[1]
    paths = sorted((ROOT / 'game/audio/voice').glob('*/ch0[12]*.*'))

    def measure(path):
        process = subprocess.run([executable, '-hide_banner', '-nostats', '-i', str(path),
                                  '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                                 stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, check=True)
        output = process.stderr.decode('utf-8', errors='replace').rsplit('Summary:', 1)[1]
        loudness = float(re.search(r'\bI:\s*([\d.+-]+) LUFS', output)[1])
        peak = float(re.search(r'Peak:\s*([\d.+-]+) dBFS', output)[1])
        return dict(path=path.relative_to(ROOT).as_posix(), character=path.parent.name, line_id=path.stem,
                    chapter=path.stem[:4], integrated_lufs=loudness, true_peak_dbfs=peak,
                    sha256=hashlib.sha256(path.read_bytes()).hexdigest())

    with ThreadPoolExecutor(max_workers=4) as pool:
        files = list(pool.map(measure, paths))
    summary = []
    for character in sorted({f['character'] for f in files}):
        row = {'character': character}
        for chapter in ('ch01', 'ch02'):
            group = [f for f in files if f['character'] == character and f['chapter'] == chapter]
            if group:
                row[chapter] = dict(count=len(group), median_lufs=round(statistics.median(f['integrated_lufs'] for f in group), 2),
                                    minimum_lufs=min(f['integrated_lufs'] for f in group), maximum_lufs=max(f['integrated_lufs'] for f in group),
                                    highest_true_peak_dbfs=max(f['true_peak_dbfs'] for f in group))
        if 'ch01' in row and 'ch02' in row:
            row['ch02_minus_ch01_lu'] = round(row['ch02']['median_lufs'] - row['ch01']['median_lufs'], 2)
        summary.append(row)
    report = dict(date='2026-10-05', method='FFmpeg EBU R128 integrated loudness and oversampled true peak; per-character median of individual raw clips',
                  scope='source clips before RenPy telephone filters and user mixer settings; no audio changed',
                  limits='Short phrases and differences in performance can affect LUFS; beidai has only one first-chapter reference clip. True peaks above 0 dBFS are reconstructed intersample peaks, not proof of sample clipping.',
                  summary=summary, files=files)
    (ROOT / '.build/reports/voice_levels_check.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
