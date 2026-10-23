#!/usr/bin/env python3
"""Write students.tex from the Week 65 problem files.

The problem files (week.toml, figures.py, problems/) sit beside build.py one folder up.
The problem-file tools are in tools/ in the portable ZIP and in
lowell-math-circle-year-2/source/problem-files/ in the repository.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WEEK = HERE.parent
for tools in (WEEK / 'tools', WEEK.parent / 'problem-files'):
    if (tools / 'atoms.py').exists():
        break
else:
    sys.exit('Cannot find the problem-file tools (atoms.py) in tools/ or ../problem-files/; see README.md.')
sys.path.insert(0, str(tools))
import atoms  # noqa: E402

w = atoms.load_week(WEEK)
(HERE / 'students.tex').write_text(atoms.student_tex(w, '3-5'))
print(f'Wrote students.tex from {WEEK}')
