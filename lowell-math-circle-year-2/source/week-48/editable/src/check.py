#!/usr/bin/env python3
"""Check every count and key the Week 48 student pages and guide rely on.

Usage: python3 check.py

Each shape is clipped against each grid cell with exact fractions (the shapes are
convex), so a cell is whole when its gray area equals the cell, outside when the gray
area is 0 (a touch at an edge or corner adds no square) and partial otherwise. The
shapes are those drawn by figures.py on the 4-by-4 frame, in big-square units, y down.
The first two asserts are the old builder's (make.py, archived in the repository's
source/week-48/archive-before-problem-files-2026-10-23/); the rest were added with the
review card's fixes on October 23, 2026.
"""
from fractions import Fraction as F
from itertools import combinations

# For a diagonal triangle on an n-by-n grid, count cells below and cut by diagonal.
assert 4*3//2 == 6 and 4*5//2 == 10
assert 8*7//2/4 == 7 and 8*9//2/4 == 9

h = F(1, 2)
SHAPES = {
    'triangle': [(0, 4), (4, 4), (4, 0)],
    'diamond': [(0, 2), (2, 0), (4, 2), (2, 4)],
    'trap': [(h, h), (F(7, 2), h), (3, F(7, 2)), (1, F(7, 2))],
}


def area(poly):
    return abs(sum(x0*y1 - x1*y0 for (x0, y0), (x1, y1) in zip(poly, poly[1:] + poly[:1]))) / 2


def clip(poly, x0, y0, x1, y1):
    """Sutherland-Hodgman clip of a convex polygon to the box [x0,x1] x [y0,y1]."""
    for inside, cut in ((lambda p: p[0] >= x0, lambda p, q: (x0, p[1] + (q[1]-p[1])*(x0-p[0])/(q[0]-p[0]))),
                        (lambda p: p[0] <= x1, lambda p, q: (x1, p[1] + (q[1]-p[1])*(x1-p[0])/(q[0]-p[0]))),
                        (lambda p: p[1] >= y0, lambda p, q: (p[0] + (q[0]-p[0])*(y0-p[1])/(q[1]-p[1]), y0)),
                        (lambda p: p[1] <= y1, lambda p, q: (p[0] + (q[0]-p[0])*(y1-p[1])/(q[1]-p[1]), y1))):
        out = []
        for i, p in enumerate(poly):
            q = poly[(i + 1) % len(poly)]
            if inside(p):
                out.append(p)
                if not inside(q):
                    out.append(cut(p, q))
            elif inside(q):
                out.append(cut(p, q))
        poly = out
        if not poly:
            return []
    return poly


def cells(kind, n):
    """{(col, row): 'W'|'P'|'O'} with columns and rows numbered from 1, rows from the top."""
    s = F(4, n)
    out = {}
    for c in range(n):
        for r in range(n):
            a = area(clip(SHAPES[kind], c*s, r*s, (c+1)*s, (r+1)*s))
            out[(c+1, r+1)] = 'W' if a == s*s else ('O' if a == 0 else 'P')
    return out


def bounds(kind, n):
    m = cells(kind, n)
    w = sum(v == 'W' for v in m.values())
    p = sum(v == 'P' for v in m.values())
    return F(w*16, n*n), F((w+p)*16, n*n)


def children(kind, c, r):
    fine = cells(kind, 8)
    return [fine[(2*c-1+a, 2*r-1+b)] for a in (0, 1) for b in (0, 1)]


# Bounds on both grids, in big-square units (guide key table; 2-3 trapezoid problem).
want = {('triangle', 4): (6, 10), ('triangle', 8): (7, 9), ('diamond', 4): (4, 12), ('diamond', 8): (6, 10),
        ('trap', 4): (4, 16), ('trap', 8): (6, 9)}
for (kind, n), b in want.items():
    assert bounds(kind, n) == b, (kind, n, bounds(kind, n))
print('PASS bounds: triangle 6-10 then 7-9, diamond 4-12 then 6-10, trapezoid 4-16 then 6-9 (big-square units).')

gaps = {k: [bounds(k, n)[1] - bounds(k, n)[0] for n in (4, 8)] for k in SHAPES}
assert gaps == {'triangle': [4, 2], 'diamond': [8, 4], 'trap': [12, 3]}, gaps
for k in ('triangle', 'diamond'):
    coarse = cells(k, 4)
    assert all(sorted(children(k, c, r)) == ['O', 'P', 'P', 'W'] for (c, r), v in coarse.items() if v == 'P')
print('PASS gaps: the triangle (4 to 2) and diamond (8 to 4) halve because every partial big cell splits into '
      'one whole, two partial and one outside; the trapezoid falls from 12 to 3, so splitting does not always halve.')

# Exact trapezoid area: a 2-by-3 rectangle and two right triangles with legs 1/2 and 3.
assert area(SHAPES['trap']) == F(15, 2) == 2*3 + 2*(h*3/2)
assert bounds('trap', 4)[0] < F(15, 2) < bounds('trap', 4)[1]
assert bounds('trap', 8)[0] < F(15, 2) < bounds('trap', 8)[1]
print('PASS trapezoid area: exactly 15/2 = 6 + 3/4 + 3/4, strictly inside 4-16 and 6-9.')

# Gap reduction for one split = (whole children + outside children) / 4.
coarse = cells('trap', 4)
gain = {cr: F(sum(ch in 'WO' for ch in children('trap', *cr)), 4) for cr, v in coarse.items() if v == 'P'}
types = {cr: ''.join(sorted(children('trap', *cr))) for cr in gain}
assert {cr for cr, g in gain.items() if g == 1} == {(2, 1), (3, 1), (2, 4), (3, 4)}
assert all(types[cr] == 'OOWW' for cr in [(2, 1), (3, 1), (2, 4), (3, 4)])
assert all(types[cr] == 'OOOP' and gain[cr] == F(3, 4) for cr in [(1, 1), (4, 1), (1, 4), (4, 4)])
assert all(types[cr] == 'OOPP' and gain[cr] == F(1, 2) for cr in [(1, 2), (1, 3), (4, 2), (4, 3)])
assert all(coarse[cr] == 'W' for cr in [(2, 2), (3, 2), (2, 3), (3, 3)])
best = max(combinations(gain, 3), key=lambda t: sum(gain[cr] for cr in t))
lo = 4 + sum(F(children('trap', *cr).count('W'), 4) for cr in best)
hi = 16 - sum(F(children('trap', *cr).count('O'), 4) for cr in best)
assert (lo, hi, hi - lo) == (F(11, 2), F(29, 2), 9) and all(gain[cr] == 1 for cr in best)
assert lo < F(15, 2) < hi
print('PASS 4-5 split budget: the top and bottom middle cells each remove a whole unit (2 whole, 2 outside '
      'children); three of them give 5.5 and 14.5, gap 9; the exact area 7.5 lies between.')

# K-1 removal-only objective: tiles removed = outside children; corners free three each.
removed = {cr: children('trap', *cr).count('O') for cr in gain}
assert max(removed.values()) == 3 and {cr for cr, v in removed.items() if v == 3} == {(1, 1), (4, 1), (1, 4), (4, 4)}
assert max(sum(removed[cr] for cr in t) for t in combinations(removed, 2)) == 6
assert 16 - F(6, 4) == F(29, 2)
print('PASS K-1 two splits: only the four corners free three small tiles each, so two splits remove at most 6; '
      'the cover becomes 14.5.')

# The bottom corner cells keep only a sliver: the slanted side is at most 1/12 unit inside the cell.
for c, edge in ((1, ((h, h), (1, F(7, 2)))), (4, ((F(7, 2), h), (3, F(7, 2))))):
    (xa, ya), (xb, yb) = edge
    x_at_3 = xa + (xb - xa)*(3 - ya)/(yb - ya)
    depth = (1 - x_at_3) if c == 1 else (x_at_3 - 3)
    assert depth == F(1, 12) and depth*30 == F(5, 2)
print('PASS slivers: in each bottom corner cell the gray reaches at most 1/12 of a big square, 2.5 mm on the '
      '120 mm board.')

# K-1 small diamond: each partial big cell has exactly one outside child, so up to eight can change.
dia = cells('diamond', 4)
outside_kids = [cr for cr, v in dia.items() if v == 'P' for ch in children('diamond', *cr) if ch == 'O']
assert sum(v == 'P' for v in dia.values()) == 8 and len(outside_kids) == 8
assert all(ch != 'O' for cr, v in dia.items() if v == 'W' for ch in children('diamond', *cr))
print('PASS K-1 small diamond: eight partial big cells each have one outside small child; whole big cells have '
      'none, and outside big cells must stay outside, so at most eight outside small cells can become partly gray.')

# Same markings, different areas: rectangles in the guide's keys.
def rect_marks(width, height):
    """A rectangle from the top-left corner of a 4-by-4 grid: (whole, partial) big cells."""
    poly = [(0, 0), (width, 0), (width, height), (0, height)]
    w = p = 0
    for c in range(4):
        for r in range(4):
            a = area(clip(poly, c, r, c+1, r+1))
            w += a == 1
            p += 0 < a < 1
    return w, p, width*height


assert rect_marks(3, F(7, 6)) == (3, 3, F(7, 2)) and rect_marks(3, F(11, 6)) == (3, 3, F(11, 2))
assert rect_marks(3, F(23, 12)) == (3, 3, F(23, 4))
assert rect_marks(4, F(9, 8)) == (4, 4, F(9, 2)) and rect_marks(4, F(15, 8)) == (4, 4, F(15, 2))
assert F(9, 2) < 5 and F(15, 2) > 7 and F(7, 2) < 4 and F(11, 2) > 5
print('PASS same markings: K-1 rectangles 3.5 and 5.5 (then 5.75) keep 3 whole and 3 partial squares; '
      '2-3 rectangles 4.5 and 7.5 keep 4 whole and 4 partial; every such area lies strictly between w and w + p.')
print('PASS student checks.')
