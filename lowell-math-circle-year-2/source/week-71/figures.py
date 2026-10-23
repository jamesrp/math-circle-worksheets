"""Week 71 figures: the two exact-reflection window macros of the student packet.

The package's generator, student/make_diagrams.py (editable/student/ in the repository,
../student/ beside problem-files/ in the portable ZIP), draws them, carried over
unchanged. The old students.tex read them from windows.tex in its preamble; here the
first problem file's `## figure` section, windows(), writes the same \\newcommand
definitions at the start of the body, before Problem 2 uses them.
"""
import importlib.util as _util
from pathlib import Path as _Path

_HERE = _Path(__file__).resolve().parent
_FILE = next(p for p in (_HERE / 'editable' / 'student' / 'make_diagrams.py', _HERE.parent / 'student' / 'make_diagrams.py')
             if p.exists())
_spec = _util.spec_from_file_location('week71_make_diagrams', _FILE)
_diagrams = _util.module_from_spec(_spec)
_spec.loader.exec_module(_diagrams)


def windows():
    """\\squareABA and \\rhombusABA, as student/make_diagrams.py writes them."""
    return _diagrams.generate()
