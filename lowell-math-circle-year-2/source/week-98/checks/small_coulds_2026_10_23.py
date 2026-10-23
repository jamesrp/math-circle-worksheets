#!/usr/bin/env python3
"""Check the review card's coulds 8, 9 and 11 (October 23, 2026) in the delivered PDFs.

Reads the print PDFs with PyMuPDF (vector drawings and words), never the TeX:
  could 8  : Grades 2-3 page 5 prints the four-seed start at 30 mm cells, larger than
             its four deletion boards, whose seeds are the four one-seed removals.
  could 9  : Grades 4-5 Problem 1 is followed by an extra-workspace page of four 30 mm
             3-by-3 boards, so the problem has six boards for its four possible finishes.
  could 11 : Grades 4-5 Problem 3 has a spare 10-by-10 board beside the first.
It also checks the footers (W98-23-v3, W98-45-v3, W98-FAC-v4), consecutive problem
numbers, the guide's workboard pages, and by enumeration the finishes the pages rely on.
Run: python3 small_coulds_2026_10_23.py [folder with the three PDFs]
"""
import itertools
import sys
from pathlib import Path

import pymupdf

MM = 72 / 25.4
fails = []


def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        fails.append(msg)


def closure(n, seeds):
    filled = set(seeds)
    grew = True
    while grew:
        grew = False
        for r, c in itertools.product(range(n), repeat=2):
            if (r, c) not in filled and sum((r + dr, c + dc) in filled for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))) >= 2:
                filled.add((r, c))
                grew = True
    return filled


def boards(page):
    """Each board: outer 0.65 pt rectangle in mm, its cell pitch and the cells holding dots."""
    outer, lines, dots = [], [], []
    for d in page.get_drawings():
        kinds = [it[0] for it in d['items']]
        w = round(d.get('width') or 0, 2)
        r = d['rect']
        box = (r.x0 / MM, r.y0 / MM, r.x1 / MM, r.y1 / MM)
        if d['type'] == 'f' and all(k == 'c' for k in kinds) and max(d.get('fill') or (1,)) < 0.1:
            dots.append(((box[0] + box[2]) / 2, (box[1] + box[3]) / 2))
        elif d['type'] == 's' and w == 0.65 and kinds == ['l'] * 4:
            outer.append(box)
        elif d['type'] == 's' and w == 0.45 and kinds == ['l']:
            lines.append(box)
    out = []
    for x0, y0, x1, y1 in sorted(outer, key=lambda b: (round(b[1] / 20), b[0])):
        inner_x = sorted({round(a, 2) for a, b, c, e in lines if abs(a - c) < .01 and x0 + .1 < a < x1 - .1 and b >= y0 - .1 and e <= y1 + .1})
        inner_y = sorted({round(b, 2) for a, b, c, e in lines if abs(b - e) < .01 and y0 + .1 < b < y1 - .1 and a >= x0 - .1 and c <= x1 + .1})
        n = len(inner_x) + 1
        cell = (x1 - x0) / n
        seeds = {(int((y - y0) // cell), int((x - x0) // cell)) for x, y in dots if x0 < x < x1 and y0 < y < y1}
        out.append(dict(box=(round(x0), round(y0)), n=n, rows=len(inner_y) + 1, cell=round(cell, 2), seeds=seeds))
    return out


folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[3] / 'week-98'
d23 = pymupdf.open(folder / 'week-98-grades-2-3.pdf')
d45 = pymupdf.open(folder / 'week-98-grades-4-5.pdf')
guide = pymupdf.open(folder / 'week-98-facilitator.pdf')
flat = lambda p: ' '.join(p.get_text().split())

# Footers, headers and problem numbers
for doc, band, foot, count, probs in ((d23, '2–3', 'W98-23-v3', 5, 5), (d45, '4–5', 'W98-45-v3', 7, 6)):
    check(len(doc) == count, f'Grades {band}: {count} pages')
    texts = [flat(p) for p in doc]
    check(all(f'Week 98 / Growing from a few seeds / Grades {band}' in t and f'Bellingham Math Circle / Week 98 / {foot}' in t for t in texts),
          f'Grades {band}: every page has the header and footer {foot}')
    found = [n for n in range(1, 10) if any(f'Problem {n}:' in t for t in texts)]
    check(found == list(range(1, probs + 1)), f'Grades {band}: problems numbered 1-{probs} ({found})')
check(all('W98-FAC-v4' in flat(p) for p in guide), 'guide: every page has footer W98-FAC-v4')

# Could 8: Grades 2-3 page 5
four = {(0, 0), (0, 1), (1, 2), (2, 2)}
b5 = boards(d23[4])
check(len(b5) == 5 and all(b['n'] == b['rows'] == 3 for b in b5), 'Grades 2–3 p. 5: five 3-by-3 boards')
start, dels = b5[0], b5[1:]
check(start['cell'] == 30.0 and start['seeds'] == four, f'Grades 2–3 p. 5: the four-seed start has 30 mm cells ({start["cell"]}) and seeds {sorted(start["seeds"])}')
check(all(b['cell'] < start['cell'] for b in dels), f'Grades 2–3 p. 5: each deletion board is smaller than the start ({[b["cell"] for b in dels]} mm)')
check(sorted(map(sorted, (b['seeds'] for b in dels))) == sorted(sorted(four - {s}) for s in four),
      'Grades 2–3 p. 5: the four deletion boards are the four one-seed removals')
check(len(closure(3, four)) == 9 and [len(closure(3, b['seeds'])) for b in dels] == [6, 3, 3, 6],
      f'Grades 2–3 p. 5: the start fills; the printed removals stop at {[len(closure(3, b["seeds"])) for b in dels]} (guide: 6, 3, 3, 6)')

# Could 9: Grades 4-5 Problem 1 and its extra workspace
finishes = sorted({len(closure(3, s)) for s in itertools.combinations(itertools.product(range(3), repeat=2), 3)})
p1, p2 = boards(d45[0]), boards(d45[1])
big1 = [b for b in p1 if b['cell'] == 30.0]
check(len(big1) == 2, 'Grades 4–5 p. 1: two 30 mm boards under Problem 1')
t2 = flat(d45[1])
check('Extra workspace' in t2 and 'Problem' not in t2.replace('Bellingham', ''), 'Grades 4–5 p. 2: labelled Extra workspace, no new problem')
check(len(p2) == 4 and all(b['n'] == 3 and b['cell'] == 30.0 and not b['seeds'] for b in p2), 'Grades 4–5 p. 2: four empty 3-by-3 boards with 30 mm cells')
check(finishes == [3, 4, 6, 9] and len(big1) + len(p2) == 6 != len(finishes),
      f'Grades 4–5 Problem 1: six boards for the {len(finishes)} possible finishes {finishes}, so the board count does not give the answer')

# Could 11: Grades 4-5 Problem 3
p4 = boards(d45[3])
check('Problem 3:' in flat(d45[3]) and 'Extra workspace' in flat(d45[3]), 'Grades 4–5 p. 4: Problem 3 with an Extra workspace label')
check(sorted((b['n'], b['cell']) for b in p4) == [(5, 20.0), (10, 7.0), (10, 7.0)], f'Grades 4–5 p. 4: a 5-by-5 board and two 10-by-10 boards at 7 mm ({[(b["n"], b["cell"]) for b in p4]})')

# The guide names the workboards on their new pages
g = ' '.join(flat(p) for p in guide)
check('3 × 3 boards on Grades 2–3 pages 1, 3, 4 and 5 and Grades 4–5 pages 1, 2 and 7, and the 4 × 4 board on Grades 2–3 page 2 and Grades 4–5 page 3' in g,
      'guide: the workboard pages match the new layout')
named = [(d23, 1, 3), (d23, 3, 3), (d23, 4, 3), (d23, 5, 3), (d45, 1, 3), (d45, 2, 3), (d45, 7, 3), (d23, 2, 4), (d45, 3, 4)]
check(all(any(b['n'] == n and b['cell'] == 30.0 for b in boards(doc[p - 1])) for doc, p, n in named),
      'every page the guide names as a workboard page has a 30 mm board of that size')

print(f'{len(fails)} failures')
sys.exit(1 if fails else 0)
