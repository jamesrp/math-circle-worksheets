#!/usr/bin/env python3
"""Write and compile k-1.tex, grades-2-3.tex and grades-4-5.tex from the Week 31 problem files.

The problem files are the student pages' source. In the portable ZIP they are in
../problem-files/ with the tools in ../problem-files/tools/; in the repository they
are in lowell-math-circle-year-2/source/week-31/ with the tools in
lowell-math-circle-year-2/source/problem-files/. Each packet is compiled twice with
pdfLaTeX into ../qa/ and copied to the package folder, as the old builder did.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
QA = OUT / 'qa'
LAYOUTS = [(HERE.parent / 'problem-files', HERE.parent / 'problem-files' / 'tools'),
           (HERE.parent.parent, HERE.parent.parent.parent / 'problem-files')]
for week, tools in LAYOUTS:
    if (week / 'week.toml').exists() and (tools / 'atoms.py').exists():
        break
else:
    sys.exit('Cannot find the Week 31 problem files (week.toml) and tools (atoms.py); see README.md.')
sys.path.insert(0, str(tools))
import atoms  # noqa: E402

QA.mkdir(exist_ok=True)
w = atoms.load_week(week)
for band, slug in (('K-1', 'k-1'), ('2-3', 'grades-2-3'), ('4-5', 'grades-4-5')):
    fn = HERE / f'{slug}.tex'
    fn.write_text(atoms.student_tex(w, band))
    for pass_no in (1, 2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', f'-output-directory={QA}', str(fn)],
                           cwd=HERE, env=os.environ.copy(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        (QA / f'{slug}-build-{pass_no}.log').write_text(r.stdout)
        if r.returncode:
            raise RuntimeError(r.stdout[-3000:])
    shutil.copy(QA / f'{slug}.pdf', OUT / f'{slug}.pdf')
    subprocess.run(['pdftoppm', '-r', '60', '-png', str(OUT / f'{slug}.pdf'), str(QA / slug)], check=True)
    print(31, slug, f'from {week}')
