#!/usr/bin/env python3
"""Check the small deferred coulds made on October 23, 2026 (Week 25, card coulds 11 and 13).

Could 11: on K-1 p. 2, Grades 2-3 pp. 1 and 5 and Grades 4-5 p. 3 one grid's circled column
counts sat 2-3 mm above the next grid's column labels. Those grid rows are now spaced
further apart, and Grades 4-5 p. 3 uses the 18.5 mm cells of Problem 1. Could 13: the guide's
overview and p. 1 now carry the theme name of the student headers, "Row and column shadows".

Read from the reference PDFs (the print copies): the footers, every task cell's size, the gap
between each circled count and the nearest column label below it on every page, the student
headers and the guide's titles and supplies line. With --before DIR (a folder holding the
previous print PDFs, such as the project's week-25/archive-before-small-coulds-2026-10-23/),
also check that the student text is unchanged apart from the footer ids, that only the
intended pages' drawings moved, and that the guide changed only on its first two pages.

Run from anywhere: python3 review/verify_small_coulds_2026_10_23.py [--before DIR]
"""
import collections
import re
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / 'reference-pdfs'
MM = 72 / 25.4
FAIL = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        FAIL.append(msg)


def text(page):
    return ' '.join(page.get_text().split())


def circles(page):
    """Circled counts: drawings about 7.2 mm across (radius 3.6 mm), in mm."""
    out = []
    for d in page.get_drawings():
        r = d['rect']
        if 6.5 < r.width / MM < 8 and 6.5 < r.height / MM < 8 and any(it[0] == 'c' for it in d['items']):
            out.append((r.x0 / MM, r.y0 / MM, r.x1 / MM, r.y1 / MM))
    return out


def hlines(page):
    """Horizontal lines at least 7 mm long, as (x0, x1, y) in mm."""
    out = []
    for d in page.get_drawings():
        for it in d['items']:
            if it[0] == 'l' and abs(it[1].y - it[2].y) < 0.01 and abs(it[1].x - it[2].x) > 7 * MM:
                out.append((min(it[1].x, it[2].x) / MM, max(it[1].x, it[2].x) / MM, it[1].y / MM))
    return out


def column_labels(page, circs):
    """Digits outside every circle, directly above a horizontal grid line (within 6 mm)."""
    lines = hlines(page)
    out = []
    for x0, y0, x1, y1, w, *_ in page.get_text('words'):
        x0, y0, x1, y1 = x0 / MM, y0 / MM, x1 / MM, y1 / MM
        if not w.isdigit() or y1 > 260:
            continue
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        if any(a - .5 < cx < c + .5 and b - .5 < cy < e + .5 for a, b, c, e in circs):
            continue
        if any(a <= cx <= c and 0 < y - y1 < 6 for a, c, y in lines):
            out.append((x0, y0, x1, y1))
    return out


def least_gap(page):
    """The smallest vertical gap from a task grid's circled column count down to a column label
    it overlaps. A task grid's bottom line is over 20 mm long and within 3 mm above its counts;
    the 8 mm switch examples (16 mm wide) are left out."""
    circs = circles(page)
    lines = hlines(page)
    counts = [c for c in circs if any(a <= (c[0] + c[2]) / 2 <= b and b - a > 20 and 0 <= c[1] - y <= 3 for a, b, y in lines)]
    best = None
    for lx0, ly0, lx1, ly1 in column_labels(page, circs):
        for cx0, cy0, cx1, cy1 in counts:
            if lx1 > cx0 - 1 and lx0 < cx1 + 1 and ly0 > cy1:
                g = ly0 - cy1
                best = g if best is None else min(best, g)
    return best


def cells(page):
    """Grid pitches in mm between neighbouring vertical lines that start at the same height."""
    groups = collections.defaultdict(set)
    for d in page.get_drawings():
        for it in d['items']:
            if it[0] == 'l' and abs(it[1].x - it[2].x) < 0.01 and abs(it[1].y - it[2].y) > 10 * MM:
                groups[round(min(it[1].y, it[2].y), 1)].add(round(it[1].x, 2))
    found = set()
    for xs in groups.values():
        xs = sorted(xs)
        found |= {round((b - a) / MM, 2) for a, b in zip(xs, xs[1:]) if 10 * MM < b - a < 23 * MM}
    return found


PACKETS = {'k-1.pdf': ('K–1', 'W25-K-v5', 'W25-K-v4', 8, {2}),
           'grades-2-3.pdf': ('Grades 2–3', 'W25-23-v4', 'W25-23-v3', 6, {1, 5}),
           'grades-4-5.pdf': ('Grades 4–5', 'W25-45-v4', 'W25-45-v3', 8, {3})}
before = Path(sys.argv[sys.argv.index('--before') + 1]) if '--before' in sys.argv else None

gaps = {}
for name, (band, new_id, old_id, n, changed) in PACKETS.items():
    doc = pymupdf.open(REF / name)
    check(len(doc) == n and all(new_id in text(p) and old_id not in text(p) for p in doc),
          f'{name}: {n} pages, footer {new_id} on every page')
    check(all(text(p).startswith(f'Week 25 / Row and column shadows / {band}') for p in doc),
          f'{name}: every header reads "Week 25 / Row and column shadows / {band}"')
    for i, p in enumerate(doc, 1):
        g = least_gap(p)
        if g is not None:
            gaps[(name, i)] = g
    for i in sorted(changed):
        check(gaps[(name, i)] >= 5.5, f'{name} p. {i}: circled counts clear the next column labels by {gaps[(name, i)]:.1f} mm (at least 5.5)')
    sizes = {i: cells(p) for i, p in enumerate(doc, 1)}
    if name == 'grades-4-5.pdf':
        check(sizes[1] == sizes[2] == sizes[3] == {18.5} and all(sizes[i] == {22.0} for i in range(4, n + 1)),
              'grades-4-5.pdf: task cells 18.5 mm on pp. 1-3 (P1 and P2) and 22 mm on pp. 4-8')
    else:
        check(all(s <= {22.0} for s in sizes.values()), f'{name}: every task cell 22 mm')
worst = min(gaps, key=gaps.get)
print(f'      tightest remaining gap: {gaps[worst]:.1f} mm on {worst[0]} p. {worst[1]}; '
      + ', '.join(f'{k[0].split(".")[0]} p. {k[1]} {v:.1f}' for k, v in sorted(gaps.items())))
check(gaps[worst] >= 4.5, 'no task grid\'s circled count is within 4.5 mm of the column labels below it on any page')

guide = pymupdf.open(REF / 'facilitator-guide.pdf')
g1, g2 = text(guide[0]), text(guide[1])
all_text = ' '.join(text(p) for p in guide)
check(len(guide) == 20 and 'FACILITATOR GUIDE Row and column shadows Mathematical overview' in g1
      and 'Row and column shadows facilitator guide Discrete tomography / Final student packets W25-K-v5, W25-23-v4, W25-45-v4' in g2,
      'guide: the overview and p. 1 are titled "Row and column shadows" and p. 1 names W25-K-v5, W25-23-v4, W25-45-v4')
check('Hidden pictures and line counts' not in all_text and 'Discrete tomography facilitator guide' not in all_text,
      'guide: the old titles "Hidden pictures and line counts" and "Discrete tomography facilitator guide" are gone')
check('student task cells are 22 mm, except upper pp. 1-3 (18.5 mm), so a 16 mm counter leaves at least 1 mm' in g2
      and '20 mm' not in all_text, 'guide p. 1: task cells 22 mm except upper pp. 1-3 (18.5 mm); no 20 mm cells remain')

if before:
    for name, (band, new_id, old_id, n, changed) in PACKETS.items():
        a, b = pymupdf.open(before / f'week-25-{name}'), pymupdf.open(REF / name)
        same_text = len(a) == len(b) and all(text(p).replace(old_id, new_id) == text(q) for p, q in zip(a, b))
        moved = {i for i, (p, q) in enumerate(zip(a, b), 1)
                 if [d['rect'] for d in p.get_drawings()] != [d['rect'] for d in q.get_drawings()]}
        check(same_text and moved == changed,
              f'{name}: text unchanged apart from the footer id; drawings moved only on p. {", ".join(map(str, sorted(changed)))}')
        for i in sorted(changed):
            old = least_gap(a[i - 1])
            check(old < 3, f'{name} p. {i}: the gap was {old:.1f} mm before')
    a, b = pymupdf.open(before / 'week-25-facilitator.pdf'), guide
    diff = {i for i, (p, q) in enumerate(zip(a, b), 1) if text(p) != text(q)}
    old2 = text(a[1]).replace('Discrete tomography facilitator guide Row and column shadows / Final student packets W25-K-v4, W25-23-v3, W25-45-v3',
                              'Row and column shadows facilitator guide Discrete tomography / Final student packets W25-K-v5, W25-23-v4, W25-45-v4')
    old2 = old2.replace('except upper pp. 1-2 (18.5 mm) and p. 3 (20 mm),', 'except upper pp. 1-3 (18.5 mm),')
    check(len(a) == len(b) and diff == {1, 2} and text(a[0]).replace('Hidden pictures and line counts', 'Row and column shadows') == g1
          and old2 == g2, 'guide: only the two titles, p. 1\'s packet ids and its cell-size clause changed')

print('PASS' if not FAIL else f'{len(FAIL)} FAILED')
raise SystemExit(1 if FAIL else 0)
