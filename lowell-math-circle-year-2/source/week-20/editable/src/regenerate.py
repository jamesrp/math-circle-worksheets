#!/usr/bin/env python3
"""Write k-1.tex, grades-2-3.tex and grades-4-5.tex from the Week 20 problem files, then solve every board.

The problem files are the student pages' source. In the portable ZIP they are in
../problem-files/ with the tools in ../problem-files/tools/; in the repository they
are in lowell-math-circle-year-2/source/week-20/ with the tools in
lowell-math-circle-year-2/source/problem-files/. build.sh compiles the written files.
As the old builder did, it writes checked-values.txt (every board with fixed values,
solved exactly) and prints the page counts and those lines.
"""
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
    sys.exit('Cannot find the Week 20 problem files (week.toml) and tools (atoms.py); see README.md.')
sys.path.insert(0, str(tools))
sys.path.insert(0, str(HERE))
import atoms  # noqa: E402
import answer_checks  # noqa: E402

w = atoms.load_week(week)
pages, lines = [], []
for band, slug in (('K-1', 'k-1'), ('2-3', 'grades-2-3'), ('4-5', 'grades-4-5')):
    tex = atoms.student_tex(w, band)
    (HERE / f'{slug}.tex').write_text(tex)
    pages.append(tex.count('\\newpage') + 1)
    lines += [answer_checks.line(c) for c in w.figures['CHECKS']]
(HERE / 'checked-values.txt').write_text('\n'.join(lines) + '\n')
print('Generated', *pages, 'pages.')
for s in lines:
    print(s)
