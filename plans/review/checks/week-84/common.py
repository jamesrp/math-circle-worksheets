"""Shared helpers for the Week 84 math check (Public knowledge).

Written from scratch for this review. Nothing here imports or reads the
packet's own builder or checker (source/week-84/build.py, check_math.py).

Printed data are read from the DELIVERED PDFs with PyMuPDF:
  * page.get_text('words') -> every printed word with its bounding box;
  * page.get_drawings()     -> rectangles, dashed card outlines and the
                               filled headband disks with their colours.
Coordinates are PDF points (1/72 in), y measured downward from the top.
"""
import os
import re
import warnings

warnings.filterwarnings('ignore', category=FutureWarning)
try:
    import pymupdf as fitz  # noqa: F401
except ImportError:  # older PyMuPDF
    import fitz  # noqa: F401

HERE = os.path.dirname(os.path.abspath(__file__))
# Committed location: plans/review/checks/week-84/ -> four folders up.
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    # Fallback when run from the scratch run folder (tmp/review-runs/week-84/).
    d = HERE
    while d != os.path.dirname(d) and not os.path.isdir(os.path.join(d, 'lowell-math-circle-year-2')):
        d = os.path.dirname(d)
    ROOT = d

WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-84')
PDFS = {
    'students': os.path.join(WEEK, 'week-84-students.pdf'),
    'guide': os.path.join(WEEK, 'week-84-facilitator.pdf'),
}
# Re-pointed on 2026-10-23: the card's shoulds (3c1af9b) and the critic coulds (f9d1bc1) changed the packet and
# guide, so the review checks read the copies as reviewed, in week-84/archive-before-card-fixes-2026-10-23/.
# DELIVERED keeps the current print copies.
DELIVERED = dict(PDFS)
PDFS = {k: os.path.join(WEEK, 'archive-before-card-fixes-2026-10-23', os.path.basename(v)) for k, v in DELIVERED.items()}

BLUE = (40 / 255, 98 / 255, 171 / 255)
RED = (193 / 255, 70 / 255, 67 / 255)


def colour_name(rgb):
    if rgb is None:
        return None
    for name, ref in (('B', BLUE), ('R', RED)):
        if all(abs(a - b) < 0.01 for a, b in zip(rgb, ref)):
            return name
    return 'other'


def page_text(path, pages=None):
    doc = fitz.open(path)
    out = []
    for i, p in enumerate(doc):
        if pages is None or i in pages:
            out.append(p.get_text())
    return '\n'.join(out)


def flat(s):
    """Collapse whitespace and undo hyphenation at line ends for phrase search."""
    s = s.replace('’', "'").replace('‘', "'")
    s = s.replace('“', '"').replace('”', '"')
    s = re.sub(r'-\n(?=[a-z])', '', s)
    return re.sub(r'\s+', ' ', s)


class Log:
    def __init__(self, title):
        self.lines = [title, '=' * len(title)]
        self.fails = 0

    def __call__(self, *a):
        self.lines.append(' '.join(str(x) for x in a))

    def check(self, ok, msg):
        self.lines.append(('PASS  ' if ok else 'FAIL  ') + msg)
        if not ok:
            self.fails += 1
        return ok

    def note(self, msg):
        self.lines.append('NOTE  ' + msg)

    def write(self, path):
        self.lines.append('')
        self.lines.append(f'{self.fails} failure(s)')
        text = '\n'.join(self.lines) + '\n'
        with open(path, 'w') as f:
            f.write(text)
        print(text)
