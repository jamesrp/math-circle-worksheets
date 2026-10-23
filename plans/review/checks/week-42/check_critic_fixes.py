#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 42 (W42-grades-4-5-v4) in the print PDFs.

The Grades 4-5 Problem 2 grid has the heads R1, R2, R3, B on both axes and did not say which
axis is the first draw, though the question compares RB with BR. It now outlines the R2-row,
B-column cell, as Grades 2-3 does, beside "R2 then B is one labeled pair. Its cell is
outlined." Run from the repository root:
    python3 plans/review/checks/week-42/check_critic_fixes.py
Needs PyMuPDF."""
from itertools import product
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y2 = ROOT / 'lowell-math-circle-year-2'
PRINT, VIEWS = Y2 / 'week-42', Y2 / 'band-views' / 'week-42'
CM = 2.54 / 72
fails = 0


def check(ok, msg):
    global fails
    print(('ok   ' if ok else 'FAIL ') + msg)
    fails += not ok


bag = ['R1', 'R2', 'R3', 'B']
classes = {}
for a, b in product(bag, repeat=2):
    classes.setdefault(a[0] + b[0], []).append((a, b))
check({k: len(v) for k, v in classes.items()} == {'RR': 9, 'RB': 3, 'BR': 3, 'BB': 1} and ('R2', 'B') in classes['RB'],
      'three red, one blue: RR 9, RB 3, BR 3, BB 1 of 16 labeled pairs; R2 then B is an RB pair')

for band, tag, n in (('k-1', 'k-1-v3', 6), ('grades-2-3', 'grades-2-3-v3', 4), ('grades-4-5', 'grades-4-5-v4', 4)):
    d = pymupdf.open(PRINT / f'week-42-{band}.pdf')
    check(len(d) == n and all(f'W42-{tag}' in p.get_text() for p in d), f'{band}: {n} pages, footer W42-{tag}')


def outlined_cell(page):
    """The heads of the row and column of the one thick square drawn over a 1.85 cm grid cell."""
    cells = [dr['rect'] for dr in page.get_drawings() if abs(dr['rect'].width * CM - 1.85) < .03 and abs(dr['rect'].height * CM - 1.85) < .03]
    thick = [dr['rect'] for dr in page.get_drawings() if (dr.get('width') or 0) > 1.2
             and abs(dr['rect'].width * CM - 1.85) < .03 and abs(dr['rect'].height * CM - 1.85) < .03]
    if len(thick) != 1:
        return None, len(cells)
    r = thick[0]
    words = page.get_text('words')
    left, top = min(c.x0 for c in cells), min(c.y0 for c in cells)
    row = [w[4] for w in words if r.y0 < (w[1] + w[3]) / 2 < r.y1 and w[2] < left and w[4] in bag]
    col = [w[4] for w in words if r.x0 < (w[0] + w[2]) / 2 < r.x1 and w[3] < top and top - w[3] < 40 and w[4] in bag]
    return (row, col), len({(round(c.x0), round(c.y0)) for c in cells})


for label, path in (('full packet', PRINT / 'week-42-grades-4-5.pdf'), ('first view', VIEWS / 'week-42-grades-4-5-first.pdf')):
    p = pymupdf.open(path)[0]
    heads, n = outlined_cell(p)
    t = ' '.join(p.get_text().split())
    check(heads == (['R2'], ['B']) and n == 16 and 'R2 then B is one labeled pair. Its cell is outlined.' in t,
          f'{label} p. 1: the 16-cell grid outlines one cell, row {heads and heads[0]}, column {heads and heads[1]}, '
          'and the caption says so')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
