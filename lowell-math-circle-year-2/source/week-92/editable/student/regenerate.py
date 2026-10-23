#!/usr/bin/env python3
"""Write students.tex from the Week 92 problem files.

The problem files are the student packet's source. In the portable ZIP they are in
../problem-files/ with the tools in ../problem-files/tools/; in the repository they
are in lowell-math-circle-year-2/source/week-92/ with the tools in
lowell-math-circle-year-2/source/problem-files/.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
LAYOUTS = [(PACKAGE / 'problem-files', PACKAGE / 'problem-files' / 'tools'),
           (PACKAGE.parent, PACKAGE.parent.parent / 'problem-files')]
for week, tools in LAYOUTS:
    if (week / 'week.toml').exists() and (tools / 'atoms.py').exists():
        break
else:
    sys.exit('Cannot find the Week 92 problem files (week.toml) and tools (atoms.py); see README.md.')
sys.dont_write_bytecode = True
sys.path.insert(0, str(tools))
import atoms  # noqa: E402

w = atoms.load_week(week)
(HERE / 'students.tex').write_text(atoms.student_tex(w, 'shared'))
print(f'Wrote students.tex from {week}')
