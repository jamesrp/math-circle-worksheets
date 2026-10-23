#!/usr/bin/env python3
"""Write students.tex from the Week 74 problem files.

The problem files are the student pages' source. In the portable ZIP they are in
../problem-files/ with the tools in ../problem-files/tools/; in the repository they
are in lowell-math-circle-year-2/source/week-74/ with the tools in
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
    sys.exit('Cannot find the Week 74 problem files (week.toml) and tools (atoms.py); see README.md.')
sys.path.insert(0, str(tools))
import atoms  # noqa: E402

w = atoms.load_week(week)
(HERE / 'students.tex').write_text(atoms.student_tex(w, '4-5'))
print(f'Wrote students.tex from {week}')
