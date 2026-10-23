#!/usr/bin/env python3
"""Write grades-3-5.tex from the Week 100 problem files.

The problem files (week.toml, template.tex, problems/) are the student pages' source
and sit beside build.py. The tools are in tools/ in the portable ZIP and in
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
for band in w.bands:
    name = w.bands[band].get('file', {'2-3': 'grades-2-3', '4-5': 'grades-4-5'}.get(band))
    (HERE / f'{name}.tex').write_text(atoms.student_tex(w, band))
    print(f'Wrote student/{name}.tex from the problem files')
