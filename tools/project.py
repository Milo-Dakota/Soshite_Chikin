"""Small production entry point. No game launch or implicit next chapter."""
from pathlib import Path
import argparse
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def run(name, *arguments):
    subprocess.run([sys.executable, str(ROOT / 'tools' / name), *arguments], cwd=ROOT, check=True)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['export', 'recording', 'reading', 'build', 'check', 'check-ui', 'audit'])
    parser.add_argument('chapter', nargs='?', choices=['ch01','ch02'])
    args = parser.parse_args()
    if args.action not in ('check-ui','audit') and not args.chapter:
        parser.error('A chapter is required.')
    for folder in ['.build/reports','.build/exports']:
        (ROOT/folder).mkdir(parents=True,exist_ok=True)
    if args.action == 'audit':
        run('check_project.py')
    elif args.action == 'check-ui':
        run('check_menu_pages.py')
    elif args.action in ('export','recording'):
        run(f'export_{args.chapter}.py', *(['--recording'] if args.action == 'recording' else []))
        if args.action == 'recording':
            target = ROOT/f'handoff/{args.chapter}/voice.md'
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(ROOT/f'.build/exports/{args.chapter}_recording.md',target)
            print(target)
    elif args.action == 'reading':
        run('export_localization.py', args.chapter, '--reading')
    elif args.action == 'build':
        if args.chapter == 'ch02':
            run('export_ch02.py')
        run('export_localization.py', args.chapter)
        run(f'build_{args.chapter}.py')
    else:
        run(f'export_{args.chapter}.py')
        run('export_localization.py', args.chapter)
        checks = ['check_ch01_assets.py','check_ch01_expressions.py'] if args.chapter=='ch01' else ['check_ch02.py']
        for name in checks:
            run(name)

if __name__ == '__main__':
    main()
