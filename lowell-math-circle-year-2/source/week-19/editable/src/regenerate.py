#!/usr/bin/env python3
"""Write k-1.tex, grades-2-3.tex, grades-4-5.tex and materials.tex (the card sheet) from the Week 19 problem files, then run the answer checks.

The problem files are the student pages' source. In the portable ZIP they are in
../problem-files/ with the tools in ../problem-files/tools/; in the repository they
are in lowell-math-circle-year-2/source/week-19/ with the tools in
lowell-math-circle-year-2/source/problem-files/. build.sh compiles the written files.
It prints the page counts and the checks as JSON, as the old builder did.
"""
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
LAYOUTS = [(HERE.parent / 'problem-files', HERE.parent / 'problem-files' / 'tools'),
           (HERE.parent.parent, HERE.parent.parent.parent / 'problem-files')]
for week, tools in LAYOUTS:
    if (week / 'week.toml').exists() and (tools / 'atoms.py').exists():
        break
else:
    sys.exit('Cannot find the Week 19 problem files (week.toml) and tools (atoms.py); see README.md.')
sys.path.insert(0, str(tools))
sys.path.insert(0, str(HERE))
import atoms  # noqa: E402
import answer_checks  # noqa: E402

w = atoms.load_week(week)
pages = {}
for band, slug in (('K-1', 'k-1'), ('2-3', 'grades-2-3'), ('4-5', 'grades-4-5')):
    tex = atoms.student_tex(w, band)
    (HERE / f'{slug}.tex').write_text(tex)
    pages[slug] = tex.count('\\newpage') + 1
# v3: the adult card sheet (sixteen 4.5 cm cards), drawn by card_sheet_tex() in figures.py.
(HERE / 'materials.tex').write_text(w.figures['card_sheet_tex']())
pages['materials'] = 1
print(json.dumps({'pages': pages, 'checks': answer_checks.run()}, indent=2))
