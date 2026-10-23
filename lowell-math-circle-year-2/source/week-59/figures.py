"""Figures for the Week 59 problem files (Constant width).

A problem file's `## figure` section is a Python expression evaluated here; it
returns the LaTeX for that figure. The pictures are drawn by the old student
builder's make_assets.py (in the repository editable/student/, in the portable ZIP
../student/), carried over unchanged: asset(name) returns the TikZ code that its
macro of that name held, so the page is the same as when students.tex input
assets.tex. make_assets.py also writes every picture as a macro for materials.tex.
"""
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for _student in (_HERE / 'editable' / 'student', _HERE.parent / 'student'):
    if (_student / 'make_assets.py').exists():
        sys.path.insert(0, str(_student))
        break
sys.dont_write_bytecode = True
import make_assets  # noqa: E402

_PICTURES = {p.name: p for p in make_assets.pictures()}


def asset(name):
    """The TikZ picture make_assets.py draws under this name, as its macro held it."""
    p = _PICTURES[name]
    return "\n".join(p.code) + "\n\\end{tikzpicture}\\par"
