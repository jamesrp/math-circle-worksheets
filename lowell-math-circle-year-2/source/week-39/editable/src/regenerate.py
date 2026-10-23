#!/usr/bin/env python3
"""Write k-1.tex, grades-2-3.tex and grades-4-5.tex from the Week 39 problem files.

The problem files are the student pages' source. In the portable ZIP they are in
../problem-files/ with the tools in ../problem-files/tools/; in the repository they
are in lowell-math-circle-year-2/source/week-39/ with the tools in
lowell-math-circle-year-2/source/problem-files/.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LAYOUTS = [(HERE.parent / 'problem-files', HERE.parent / 'problem-files' / 'tools'),
           (HERE.parent.parent, HERE.parent.parent.parent / 'problem-files')]
for week, tools in LAYOUTS:
    if (week / 'week.toml').exists() and (tools / 'atoms.py').exists():
        break
else:
    sys.exit('Cannot find the Week 39 problem files (week.toml) and tools (atoms.py); see README.md.')
sys.path.insert(0, str(tools))
import atoms  # noqa: E402

w = atoms.load_week(week)
for band, name in (('K-1', 'k-1'), ('2-3', 'grades-2-3'), ('4-5', 'grades-4-5')):
    (HERE / f'{name}.tex').write_text(atoms.student_tex(w, band))
print(f'Wrote k-1.tex, grades-2-3.tex and grades-4-5.tex from {week}')
