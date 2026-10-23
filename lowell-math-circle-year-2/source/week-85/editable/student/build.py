#!/usr/bin/env python3
"""Build the Week 85 student packets and materials from the problem files.

The problem files are the student pages' only source. In the portable ZIP they are in
../problem-files/ with the tools in ../problem-files/tools/; in the repository they are
in lowell-math-circle-year-2/source/week-85/ with the tools in
lowell-math-circle-year-2/source/problem-files/. The shared and upper packets are the
week's two bands; the materials pages come from materials_tex() in figures.py.

    python3 build.py --out OUT --work WORK
"""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
LAYOUTS = [(HERE.parent / 'problem-files', HERE.parent / 'problem-files' / 'tools'),
           (HERE.parent.parent, HERE.parent.parent.parent / 'problem-files')]
for week_dir, tools in LAYOUTS:
    if (week_dir / 'week.toml').exists() and (tools / 'atoms.py').exists():
        break
else:
    sys.exit('Cannot find the Week 85 problem files (week.toml) and tools (atoms.py); see README.md.')
sys.path.insert(0, str(tools))
import atoms  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out', type=Path, default=HERE.parent)
    ap.add_argument('--work', type=Path, default=HERE.parent / 'build')
    a = ap.parse_args()
    out, work = a.out.resolve(), a.work.resolve()
    out.mkdir(parents=True, exist_ok=True)
    work.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(HERE / 'check_math.py'), str(week_dir / 'figures.py')], check=True)
    week = atoms.load_week(week_dir)
    texts = {week.bands[band]['file']: atoms.student_tex(week, band) for band in week.bands}
    texts['materials'] = week.figures['materials_tex']()
    latex = shutil.which('pdflatex') or '/Library/TeX/texbin/pdflatex'
    env = dict(os.environ, SOURCE_DATE_EPOCH='1792195200', FORCE_SOURCE_DATE='1')
    for name in ('shared', 'upper', 'materials'):
        folder = work / name
        folder.mkdir(exist_ok=True)
        (folder / (name + '.tex')).write_text(texts[name])
        for _ in range(2):
            p = subprocess.run([latex, '-interaction=nonstopmode', '-halt-on-error', name + '.tex'], cwd=folder, env=env,
                               text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (work / (name + '.log')).write_text(p.stdout)
            if p.returncode or 'Overfull' in p.stdout:
                raise SystemExit(p.stdout[-7000:])
        shutil.copy2(folder / (name + '.pdf'), out / (name + '.pdf'))
    print('Built shared.pdf, upper.pdf, materials.pdf from the problem files')


if __name__ == '__main__':
    main()
