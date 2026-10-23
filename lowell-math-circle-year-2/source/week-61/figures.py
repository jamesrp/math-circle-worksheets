"""Figures for the Week 61 problem files (Triangles on a ball).

The sphere pictures are drawn by the package's own generator, student/geometry.py
(editable/student/ in the repository, ../student/ beside problem-files/ in the ZIP),
carried over unchanged. The old builder wrote its macros to figures.tex and read them
in the preamble; here the first problem file's `## figure` section, macros(), writes
the same \\newcommand definitions at the start of the body, before any page uses them.
"""
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
for d in (HERE / 'editable' / 'student', HERE.parent / 'student'):
    if (d / 'geometry.py').exists():
        sys.path.insert(0, str(d))
        break
else:
    raise ImportError('Cannot find student/geometry.py beside the Week 61 problem files')
sys.dont_write_bytecode = True
import geometry  # noqa: E402


def macros():
    """The figure macros, exactly as geometry.write_figures writes figures.tex."""
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / 'figures.tex'
        geometry.write_figures(str(path))
        return path.read_text().rstrip('\n')
