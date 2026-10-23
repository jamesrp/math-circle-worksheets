#!/usr/bin/env python3
"""Build the Week 87 student packets and materials from the problem files.

The problem files are the student pages' only source. In the portable ZIP they are in
../problem-files/ with the tools in ../problem-files/tools/; in the repository they are
in lowell-math-circle-year-2/source/week-87/ with the tools in
lowell-math-circle-year-2/source/problem-files/. The shared, line and upper packets are the
week's three bands; the materials pages come from materials_tex() in figures.py.

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
    sys.exit('Cannot find the Week 87 problem files (week.toml) and tools (atoms.py); see README.md.')
sys.path.insert(0, str(tools))
import atoms  # noqa: E402

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('--out', type=Path, default=HERE.parent)
parser.add_argument('--work', type=Path)
args = parser.parse_args()
ROOT = args.out.resolve()
SRC = (args.work or ROOT / 'build').resolve()
ROOT.mkdir(parents=True, exist_ok=True)
SRC.mkdir(parents=True, exist_ok=True)

week = atoms.load_week(week_dir)
texts = {week.bands[band]['file']: atoms.student_tex(week, band) for band in week.bands}
texts['materials'] = week.figures['materials_tex']()
latex = os.environ.get('PDFLATEX', shutil.which('pdflatex') or '/Library/TeX/texbin/pdflatex')
for name, tex in texts.items():
    (SRC / (name + '.tex')).write_text(tex)
    for _ in range(2):
        subprocess.run([latex, '-interaction=nonstopmode', '-halt-on-error', '-output-directory', str(SRC),
                        str(SRC / (name + '.tex'))], check=True, stdout=subprocess.DEVNULL)
    shutil.copy2(SRC / (name + '.pdf'), ROOT / (name + '.pdf'))
    print(name, tex.count('\\newpage') + 1)
