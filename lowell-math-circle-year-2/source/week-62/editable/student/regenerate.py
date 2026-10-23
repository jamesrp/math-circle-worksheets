#!/usr/bin/env python3
"""Write students.tex and graphs.json from the Week 62 problem files.

The problem files are the student packet's only source: week.toml, template.tex and
problems/*.md. In the portable ZIP they are in ../problem-files/ with the tools in
../problem-files/tools/; in the repository they are in lowell-math-circle-year-2/source/week-62/
with the tools in lowell-math-circle-year-2/source/problem-files/.

    python3 regenerate.py                 rewrite students.tex and graphs.json beside this script
    python3 regenerate.py --out FILE      write the LaTeX to FILE, and graphs.json beside it
    python3 regenerate.py --check         fail if students.tex or graphs.json differs from the problem files

graphs.json lists every printed network (vertices, edges, coordinates); verify.py reads it.
"""
import argparse
import json
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
    sys.exit('Cannot find the Week 62 problem files (week.toml) and tools (atoms.py); see ../README.md.')
sys.path.insert(0, str(tools))
sys.dont_write_bytecode = True
import atoms  # noqa: E402

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--out', type=Path, default=HERE / 'students.tex')
ap.add_argument('--check', action='store_true')
args = ap.parse_args()
try:
    w = atoms.load_week(week)
    tex = atoms.student_tex(w, 'shared')
except atoms.ProblemFileError as e:
    sys.exit(f'error: {e}')
graphs = json.dumps(w.figures['GRAPHS'], indent=2) + '\n'
if args.check:
    same = (HERE / 'students.tex').read_text() == tex and (HERE / 'graphs.json').read_text() == graphs
    print('students.tex and graphs.json match the problem files' if same else 'students.tex or graphs.json differs from the problem files; run regenerate.py')
    sys.exit(0 if same else 1)
args.out.write_text(tex)
args.out.with_name('graphs.json').write_text(graphs)
print(f'Wrote {args.out} and graphs.json from {week / "problems"}')
