"""Week 53 figures: the TikZ map macros of the student packet.

The package's student/diagrams.py draws every map from student/networks.json
(places, links, prices and label positions); the verifiers beside it read the
same JSON. problems/00-diagram-macros.md calls diagram_definitions() at the start
of the packet, so later files can use \\TriangleOne, \\SixCert and the other
macros. In the repository the package is ./editable; in the portable ZIP this
file sits in problem-files/ inside the package.
"""
import importlib.util as _util
from pathlib import Path as _Path

_HERE = _Path(__file__).resolve().parent
_FILE = next(p for p in (_HERE / 'editable' / 'student' / 'diagrams.py', _HERE.parent / 'student' / 'diagrams.py')
             if p.exists())
_spec = _util.spec_from_file_location('week53_diagrams', _FILE)
_diagrams = _util.module_from_spec(_spec)
_spec.loader.exec_module(_diagrams)


def diagram_definitions():
    """\\newcommand definitions for every map macro, as student/diagrams.py writes them."""
    return _diagrams.generate()
