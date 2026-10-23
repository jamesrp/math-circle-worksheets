#!/usr/bin/env python3
"""Write k-1.tex, grades-2-3.tex and grades-4-5.tex from the Week 21 problem files, then check every board.

The problem files are the student pages' source. In the portable ZIP they are in
../problem-files/ with the tools in ../problem-files/tools/; in the repository they
are in lowell-math-circle-year-2/source/week-21/ with the tools in
lowell-math-circle-year-2/source/problem-files/. build.sh compiles the written files.
As the old builder did, it checks that every dot and its reflection fit the board and
that every same-side pair's best contact lies between the end marks, writes those
contacts to geometry-checks.json, and checks the board facts the tasks rely on.
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
    sys.exit('Cannot find the Week 21 problem files (week.toml) and tools (atoms.py); see README.md.')
sys.path.insert(0, str(tools))
import atoms  # noqa: E402

w = atoms.load_week(week)
checks, pages = [], 0
for band, slug in (('K-1', 'k-1'), ('2-3', 'grades-2-3'), ('4-5', 'grades-4-5')):
    tex = atoms.student_tex(w, band)
    (HERE / f'{slug}.tex').write_text(tex)
    pages += tex.count('\\newpage') + 1
    checks += w.figures['contacts']()
(HERE / 'geometry-checks.json').write_text(json.dumps(checks, indent=2))
# Board-specific mathematical checks, independent of printed student text.
lookup = {(c['packet'], c['page'], c['pair']): c for c in checks}
assert abs(lookup['grades-4-5', 4, 'AB']['contact'] - 6.2) < 1e-10
assert abs(lookup['grades-4-5', 4, 'CD']['contact'] - 6.2) < 1e-10
assert abs(lookup['grades-2-3', 6, 'AB']['minimum_cm'] - lookup['grades-2-3', 6, 'AC']['minimum_cm']) < 1e-10
assert abs(lookup['grades-4-5', 6, 'AB']['contact'] - 6.5) < 1e-10
print(f'Wrote 3 packets, {pages} pages; verified {len(checks)} same-side endpoint pairs.')
