"""Week 57 (Area from dots): the student figures, drawn from the checked polygon data.

The packet's pictures are TikZ macros, \\Figure{name}, generated from
assets/polygons.json by the package's student/generate_figures.py. The first setup
file's figure section, definitions(), puts those macro definitions at the start of the
body, where the old students.tex loaded them with \\input{figures.tex}.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for _d in (HERE / 'editable' / 'student', HERE.parent / 'student'):   # repository, then the ZIP's layout
    if (_d / 'generate_figures.py').exists():
        sys.path.insert(0, str(_d))
        break
sys.dont_write_bytecode = True
import generate_figures  # noqa: E402


def definitions():
    return generate_figures.definitions().rstrip('\n')
