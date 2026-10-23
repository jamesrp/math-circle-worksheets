#!/usr/bin/env python3
"""Check the October 23, 2026 critic follow-up of Week 36 (guide only) against the print PDFs.

The guide's straight-line warning now names every printed nine-tile grid: K-1 p. 3, Grades 2-3
pp. 3-4 and Grades 4-5 pp. 2-4. This script reads the tiles drawn on every student page (circle,
triangle or square; open, striped or solid), finds each complete nine-tile grid, checks that every
one sits in rows by shape and columns by fill (so the guide's facts about straight lines apply to
it), and checks that the pages holding such grids are exactly the ones the guide names. It also
recomputes the warning's facts for that layout: the 8 straight lines are allowed threes and 4
allowed threes are bent. The student packets stay v3. Run from the repository root:
    python3 plans/review/checks/week-36/check_critic_fixes.py
Needs PyMuPDF."""
from itertools import combinations, product
from pathlib import Path
import sys
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
Y2 = ROOT / 'lowell-math-circle-year-2'
fails = 0


def check(ok, msg):
    global fails
    print(('ok   ' if ok else 'FAIL ') + msg)
    fails += not ok


def flat(page):
    return ' '.join(page.get_text().split())


# The layout's mathematics: tile (shape row, fill column); a three is allowed when each
# attribute is all the same or all different.
tiles = list(product(range(3), range(3)))
allowed = lambda t: all(len({x[i] for x in t}) in (1, 3) for i in (0, 1))
lines = [t for t in combinations(tiles, 3) if allowed(t)]
straight = lambda t: (len({x[0] for x in t}) == 1 or len({x[1] for x in t}) == 1
                      or all(x[0] == x[1] for x in t) or all(x[0] + x[1] == 2 for x in t))
geo = [t for t in combinations(tiles, 3) if straight(t)]
check(len(lines) == 12 and len(geo) == 8 and all(allowed(t) for t in geo), 'rows-by-shape layout: all 8 straight lines are allowed threes')
check(len([t for t in lines if not straight(t)]) == 4, 'and 4 allowed threes are bent')


def tile_shapes(page):
    out = []
    for d in page.get_drawings():
        kinds = ''.join(i[0] for i in d['items'])
        r = d['rect']
        if r.width > 70 or r.width < 10 or kinds not in ('cccc', 'lll', 'llll'):
            continue
        shape = {'cccc': 'circle', 'lll': 'triangle', 'llll': 'square'}[kinds]
        fill = d.get('fill')
        fill = 'striped' if fill is None else ('open' if fill == (1.0, 1.0, 1.0) else 'solid')
        out.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2, r.width, shape, fill))
    # A record board's cell outline is an unfilled square around a smaller tile: drop it.
    return [s for s in out if not any(o is not s and o[2] < s[2] and abs(o[0] - s[0]) < s[2] / 4 and abs(o[1] - s[1]) < s[2] / 4 for o in out)]


def grids(page):
    """Complete nine-tile grids: connected groups of tiles whose neighbours lie within 1.3 times
    the smallest centre-to-centre spacing on the page."""
    ts = tile_shapes(page)
    if len(ts) < 9:
        return []
    dist = lambda a, b: ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** .5
    step = min(dist(a, b) for a, b in combinations(ts, 2))
    comp = list(range(len(ts)))

    def root(i):
        while comp[i] != i:
            i = comp[i]
        return i
    for i, j in combinations(range(len(ts)), 2):
        if dist(ts[i], ts[j]) <= 1.3 * step:
            comp[root(i)] = root(j)
    out = {}
    for i, tl in enumerate(ts):
        out.setdefault(root(i), []).append(tl)
    return [g for g in out.values() if len(g) == 9]


def rows_by_shape(g):
    ys = sorted({round(t[1]) for t in g}); xs = sorted({round(t[0]) for t in g})
    if len(ys) != 3 or len(xs) != 3:
        return False
    rows = [{t[3] for t in g if round(t[1]) == y} for y in ys]
    cols = [{t[4] for t in g if round(t[0]) == x} for x in xs]
    return all(len(r) == 1 for r in rows) and all(len(c) == 1 for c in cols) \
        and len({next(iter(r)) for r in rows}) == 3 and len({next(iter(c)) for c in cols}) == 3


named = {'k-1': [3], 'grades-2-3': [3, 4], 'grades-4-5': [2, 3, 4]}
for band, tag in (('k-1', 'W36-k-1-v3'), ('grades-2-3', 'W36-grades-2-3-v3'), ('grades-4-5', 'W36-grades-4-5-v3')):
    D = pymupdf.open(Y2 / 'week-36' / f'week-36-{band}.pdf')
    check(all(tag in flat(p) for p in D), f'{band}: unchanged, footer {tag}')
    with_grid, ok = [], True
    for i, p in enumerate(D):
        gs = grids(p)
        if gs:
            with_grid.append(i + 1)
            ok &= all(rows_by_shape(g) for g in gs)
    check(with_grid == named[band], f'{band}: nine-tile grids on pages {with_grid}, as the guide names')
    check(ok, f'{band}: every printed nine-tile grid sits in rows by shape and columns by fill')

G = ' '.join(flat(p) for p in pymupdf.open(Y2 / 'week-36' / 'week-36-facilitator.pdf'))
check('On every printed nine-tile grid (K-1 p. 3, Grades 2-3 pp. 3-4, Grades 4-5 pp. 2-4) the tiles sit in rows by shape and columns by fill' in G,
      'guide p. 1: the warning names every printed nine-tile grid')
check('On the record boards (Grades 2-3 p. 4' not in G, 'guide: the old record-boards-only wording is gone')
check(len(pymupdf.open(Y2 / 'week-36' / 'week-36-facilitator.pdf')) == 6, 'guide: still six pages')
print('PASS' if not fails else f'FAIL ({fails})')
sys.exit(1 if fails else 0)
