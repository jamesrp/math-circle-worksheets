#!/usr/bin/env python3
"""Write students.tex from the Week 64 problem files.

The problem files (week.toml, figures.py, problems/) sit beside build.py one folder up.
The problem-file tools are in tools/ in the portable ZIP and in
lowell-math-circle-year-2/source/problem-files/ in the repository.

    python3 regenerate.py            rewrite students.tex beside this script
    python3 regenerate.py --check    fail if students.tex differs from the problem files
"""
import argparse
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
sys.dont_write_bytecode = True
import atoms  # noqa: E402

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--check', action='store_true')
args = ap.parse_args()
try:
    tex = atoms.student_tex(atoms.load_week(WEEK), 'shared')
except atoms.ProblemFileError as e:
    sys.exit(f'error: {e}')
if args.check:
    same = (HERE / 'students.tex').read_text() == tex
    print('students.tex matches the problem files' if same else 'students.tex differs from the problem files; run regenerate.py')
    sys.exit(0 if same else 1)
(HERE / 'students.tex').write_text(tex)
print(f'Wrote students.tex from {WEEK / "problems"}')
