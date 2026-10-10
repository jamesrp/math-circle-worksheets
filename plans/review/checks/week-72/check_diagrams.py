#!/usr/bin/env python3
"""Week 72 diagram check (review stage).

Reads the delivered student PDF's vector drawings and text positions with
pymupdf, converts each board to grid coordinates using its own printed grid
lines and column labels, and checks that every diagram encodes what the text
says: launch panels, P1/P2/P4 boards (origin, ring, labels, equal scaling),
the four P3 outlines (re-walked here to get their memories), and the page-5
apparatus sizes.  Uses no file from the source package.
"""
import sys
from pathlib import Path
try:
    import pymupdf as fitz
except ImportError:
    import fitz

REPO = Path(__file__).resolve().parents[4]
PDF = REPO / 'lowell-math-circle-year-2/week-72/week-72-students.pdf'
doc = fitz.open(PDF)
MM = 72 / 25.4
fails = []; n = 0
def check(cond, msg):
    global n
    n += 1
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond: fails.append(msg)

def is_gray(col):
    return col is not None and all(0.8 < c < 0.87 for c in col)

def circles(page):
    out = []
    for d in page.get_drawings():
        its = d['items']
        if len(its) == 4 and all(i[0] == 'c' for i in its):
            r = d['rect']
            out.append(dict(c=((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2), r=(r.x1 - r.x0) / 2,
                            filled=d.get('fill') is not None, stroked=d['type'] in ('s', 'fs'), w=d.get('width')))
    return out

def grids(page):
    gs = []
    for d in page.get_drawings():
        if d['type'] == 's' and is_gray(d.get('color')) and all(i[0] == 'l' for i in d['items']):
            xs = sorted({round(i[1].x, 1) for i in d['items'] if abs(i[1].x - i[2].x) < .01})
            ys = sorted({round(i[1].y, 1) for i in d['items'] if abs(i[1].y - i[2].y) < .01})
            gs.append(dict(xs=xs, ys=ys, rect=d['rect']))
    return gs

def ints(page):
    out = []
    for w in page.get_text('words'):
        t = w[4].replace('−', '-')
        try:
            out.append((int(t), (w[0] + w[2]) / 2, (w[1] + w[3]) / 2))
        except ValueError:
            pass
    return out

def spacing(v):
    d = [b - a for a, b in zip(v, v[1:])]
    return sum(d) / len(d), max(d) - min(d)

def col_labels(page, g):
    """integers centred under the grid's vertical lines, just below its bottom"""
    bottom = max(g['ys'])
    labs = {}
    for val, cx, cy in ints(page):
        if bottom < cy < bottom + 14:
            for X in g['xs']:
                if abs(cx - X) < 3.5:
                    labs[X] = val
    return labs

def row_labels(page, g):
    left = min(g['xs'])
    labs = {}
    for val, cx, cy in ints(page):
        if left - 16 < cx < left:
            for Y in g['ys']:
                if abs(cy - Y) < 4:
                    labs[Y] = val
    return labs

def to_grid(g, labs, pt, row0_y=None):
    ux, _ = spacing(g['xs']); uy, _ = spacing(g['ys'])
    X0 = min(labs); c0 = labs[X0]
    x = c0 + (pt[0] - X0) / ux
    Yb = max(g['ys']) if row0_y is None else row0_y
    y = (Yb - pt[1]) / uy
    return (round(x, 2), round(y, 2))

def board(page, g, name, cols, rows=None, origin=(0, 0), ring=None):
    ux, ex = spacing(g['xs']); uy, ey = spacing(g['ys'])
    check(abs(ux - uy) < 0.2 and ex < 0.3 and ey < 0.3, f'{name}: square cells, unit {ux:.1f} x {uy:.1f} pt')
    labs = col_labels(page, g)
    check([labs.get(X) for X in g['xs']] == list(cols), f'{name}: column labels {[labs.get(X) for X in g["xs"]]}')
    if rows is not None:
        rl = row_labels(page, g)
        check([rl.get(Y) for Y in sorted(g['ys'], reverse=True)] == list(rows),
              f'{name}: row labels bottom-to-top {[rl.get(Y) for Y in sorted(g["ys"], reverse=True)]}')
        row0 = [Y for Y, v in rl.items() if v == 0][0]
    else:
        row0 = max(g['ys'])
    cs = [c for c in circles(page) if g['rect'].x0 - 5 <= c['c'][0] <= g['rect'].x1 + 5
          and g['rect'].y0 - 5 <= c['c'][1] <= g['rect'].y1 + 5]
    dots = [to_grid(g, labs, c['c'], row0) for c in cs if c['filled']]
    rings = [to_grid(g, labs, c['c'], row0) for c in cs if not c['filled']]
    check(dots == [tuple(float(v) for v in origin)], f'{name}: one dot O at {origin} -> {dots}')
    if ring is not None:
        check(rings == [tuple(float(v) for v in ring)], f'{name}: one ring at {ring} -> {rings}')
    return labs

STEP = {'E': (1, 0), 'W': (-1, 0), 'N': (0, 1), 'S': (0, -1)}
def memory_around(corners):
    """walk the closed lattice polygon (corners in order) by unit steps; return memory"""
    z = 0
    pts = corners + corners[:1]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        if x1 == x2:
            z += x1 * (y2 - y1)          # each N adds the column, each S subtracts it
    return z

# ---------------- page 1 ----------------
p = doc[0]
gs = grids(p)
panels = sorted([g for g in gs if len(g['xs']) == 4 and len(g['ys']) == 2], key=lambda g: g['xs'][0])
check(len(panels) == 4, f'p1: four launch panels ({len(panels)})')
expect = [('start: memory 0', [], (0, 0)), ('EE: memory 0', [(0, 0), (2, 0)], (2, 0)),
          ('EEN: memory 2', [(0, 0), (2, 0), (2, 1)], (2, 1)),
          ('EENE: memory 2', [(0, 0), (2, 0), (2, 1), (3, 1)], (3, 1))]
draws = p.get_drawings()
for g, (cap, path, end) in zip(panels, expect):
    ux, _ = spacing(g['xs']); uy, _ = spacing(g['ys'])
    labs = col_labels(p, g)
    check([labs.get(X) for X in g['xs']] == [0, 1, 2, 3], f'p1 panel "{cap}": labels 0..3')
    inside = [d for d in draws if g['rect'].x0 - 8 <= d['rect'].x0 and d['rect'].x1 <= g['rect'].x1 + 8
              and g['rect'].y0 - 8 <= d['rect'].y0 and d['rect'].y1 <= g['rect'].y1 + 8 and not is_gray(d.get('color'))]
    segs = [(to_grid(g, labs, (i[1].x, i[1].y)), to_grid(g, labs, (i[2].x, i[2].y)))
            for d in inside if d['type'] == 's' for i in d['items'] if i[0] == 'l']
    heads = [d for d in inside if d['type'] == 'fs']
    dots = [to_grid(g, labs, c['c']) for c in circles(p) if c['filled']
            and g['rect'].x0 - 5 <= c['c'][0] <= g['rect'].x1 + 5 and g['rect'].y0 - 5 <= c['c'][1] <= g['rect'].y1 + 5]
    check(dots == [tuple(float(v) for v in end)], f'p1 panel "{cap}": robot dot at {end} -> {dots}')
    seglen = sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in segs)
    want = sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in zip(path, path[1:]))
    if path:
        # arrow shortened by the tip; compare corner vertices
        verts = [segs[0][0]] + [s[1] for s in segs]
        ok = all(abs(v[0] - w[0]) < .15 and abs(v[1] - w[1]) < .15 for v, w in zip(verts, path)) and len(verts) == len(path)
        check(ok and len(heads) == 1, f'p1 panel "{cap}": drawn path {verts} matches {path}')
    else:
        check(not segs and not heads,
              f'p1 panel "{cap}": no move drawn -> found {len(segs)} segment(s) of total length {seglen:.2f} units '
              f'and {len(heads)} arrowhead(s); head points '
              + ('up' if heads and min(i[1].y for i in heads[0]['items']) < max(i[1].y for i in heads[0]['items']) - 1 else '-'))
# P1 board
big = [g for g in gs if len(g['xs']) == 4 and len(g['ys']) == 4]
check(len(big) == 1, 'p1: one P1 board')
board(p, big[0], 'P1 board', cols=[0, 1, 2, 3], origin=(0, 0), ring=(2, 2))
lines = [d for d in draws if d['type'] == 's' and abs((d.get('width') or 0) - .2) < .02]
check(len(lines) >= 6, f'P1: {len(lines)} answer lines for 6 routes')

# ---------------- page 2 ----------------
p = doc[1]
g = grids(p)[0]
board(p, g, 'P2 board', cols=[-2, -1, 0, 1, 2], rows=[-2, -1, 0, 1, 2], origin=(0, 0))

# ---------------- page 3 ----------------
p = doc[2]
gs = sorted(grids(p), key=lambda g: (round(g['rect'].y0), g['rect'].x0))
check(len(gs) == 4, 'p3: four P3 boards')
expect3 = [([0, 1, 2, 3], 2), ([2, 3, 4, 5], 2), ([-3, -2, -1, 0], 2), ([0, 1, 2, 3], 3)]
for k, (g, (cols, area)) in enumerate(zip(gs, expect3), 1):
    ux, ex = spacing(g['xs']); uy, ey = spacing(g['ys'])
    check(abs(ux - uy) < .2, f'P3 board {k}: square cells ({ux:.1f} x {uy:.1f})')
    labs = col_labels(p, g)
    check([labs.get(X) for X in g['xs']] == cols, f'P3 board {k}: column labels {[labs.get(X) for X in g["xs"]]}')
    outl = [d for d in p.get_drawings() if d['type'] == 's' and abs((d.get('width') or 0) - 1.2) < .05
            and g['rect'].x0 - 2 <= d['rect'].x0 <= g['rect'].x1 and g['rect'].y0 - 2 <= d['rect'].y0 <= g['rect'].y1]
    check(len(outl) == 1, f'P3 board {k}: one thick outline')
    d = outl[0]
    if d['items'][0][0] == 're':
        r = d['items'][0][1]
        pts = [(r.x0, r.y1), (r.x1, r.y1), (r.x1, r.y0), (r.x0, r.y0)]
    else:
        pts = [(i[1].x, i[1].y) for i in d['items'] if i[0] == 'l']
    corners = [tuple(int(round(v)) for v in to_grid(g, labs, q)) for q in pts]
    raw = [to_grid(g, labs, q) for q in pts]
    check(all(abs(a - b) < .03 for c, r_ in zip(corners, raw) for a, b in zip(c, r_)), f'P3 board {k}: outline on lattice points {corners}')
    # orient counterclockwise (shoelace > 0)
    A2 = sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(corners, corners[1:] + corners[:1]))
    if A2 < 0: corners = corners[::-1]
    dots = [tuple(int(round(v)) for v in to_grid(g, labs, c['c'])) for c in circles(p) if c['filled']
            and g['rect'].x0 - 5 <= c['c'][0] <= g['rect'].x1 + 5 and g['rect'].y0 - 5 <= c['c'][1] <= g['rect'].y1 + 5]
    check(len(dots) == 1 and dots[0] in corners, f'P3 board {k}: start dot {dots} on the outline')
    i0 = corners.index(dots[0]); ccw = corners[i0:] + corners[:i0]
    cw = [ccw[0]] + ccw[:0:-1]
    mc, mw = memory_around(ccw), memory_around(cw)
    print(f'   P3 board {k}: corners {ccw}, memory CCW {mc}, CW {mw}, area {A2 // 2 if A2 > 0 else -A2 // 2}')
    check((mc, mw) == (area, -area), f'P3 board {k}: memories +{area}/-{area}')
    if k <= 3:
        xs = sorted({c[0] for c in ccw}); ys = sorted({c[1] for c in ccw})
        check(xs[-1] - xs[0] == 2 and ys[-1] - ys[0] == 1 and len(ccw) == 4, f'P3 board {k}: a 2-by-1 rectangle, left column {xs[0]}')

# ---------------- page 4 ----------------
p = doc[3]
g = grids(p)[0]
board(p, g, 'P4 board', cols=[-1, 0, 1, 2, 3, 4], rows=[-1, 0, 1, 2, 3, 4], origin=(0, 0), ring=(2, 2))

# ---------------- page 5 ----------------
p = doc[4]
dr = p.get_drawings()
ticks = sorted([d for d in dr if d['type'] == 's' and len(d['items']) == 1 and d['items'][0][0] == 'l'
                and abs(d['items'][0][1].x - d['items'][0][2].x) < .01
                and 5 < abs(d['items'][0][1].y - d['items'][0][2].y) < 6.5], key=lambda d: (round(d['rect'].y0), d['rect'].x0))
rows = {}
for t in ticks:
    rows.setdefault(round(t['rect'].y0), []).append(t['rect'].x0)
strip = sorted(rows.items())
main_y, main_x = strip[0]
check(len(main_x) == 21, f'p5: main strip has 21 ticks ({len(main_x)})')
sp, var = spacing(sorted(main_x))
check(abs(sp / MM - 7.2) < .02 and var < .1, f'p5: tick spacing {sp / MM:.3f} mm (guide: 7.2 mm)')
labs = {}
for val, cx, cy in ints(p):
    if main_y < cy < main_y + 16:
        for X in main_x:
            if abs(cx - X) < 4: labs[X] = val
check([labs.get(X) for X in sorted(main_x)] == list(range(-10, 11)), 'p5: labels -10..10 under the ticks')
ext = [x for y, x in strip[1:]]
allext = sorted(sum(ext, []))
left = [x for x in allext if x < 306]; right = [x for x in allext if x > 306]
for nm, e in (('left', left), ('right', right)):
    s2, v2 = spacing(e)
    check(len(e) == 11 and abs(s2 / MM - 7.2) < .02 and v2 < .1, f'p5: {nm} extension 11 unlabelled ticks at {s2 / MM:.3f} mm')
check(len(right) + len(left) - 2 == 20, 'p5: two extensions with one-tick overlap add 20 numbers (10..20 and -20..-10)')
cardgrid = [d for d in dr if d.get('dashes') and len(d['items']) > 8]
xs = sorted({round(i[1].x, 1) for d in cardgrid for i in d['items'] if i[0] == 'l' and abs(i[1].x - i[2].x) < .01})
ys = sorted({round(i[1].y, 1) for d in cardgrid for i in d['items'] if i[0] == 'l' and abs(i[1].y - i[2].y) < .01})
cs1, _ = spacing(xs); cs2, _ = spacing(ys)
check(len(xs) == 9 and len(ys) == 5 and abs(cs1 / MM - 18) < .05 and abs(cs2 / MM - 18) < .05,
      f'p5: card grid 8 x 4 of {cs1 / MM:.2f} x {cs2 / MM:.2f} mm')
words = [w for w in p.get_text('words') if w[1] > ys[0] and w[3] < ys[-1]]
from collections import Counter
cnt = Counter(w[4] for w in words if w[4] in 'EWNS')
check(cnt == Counter({'E': 8, 'W': 8, 'N': 8, 'S': 8}), f'p5: card letters {dict(cnt)}')

print(f'\n{n} checks, {len(fails)} failures')
for f in fails: print('  FAILED:', f)
sys.exit(1 if fails else 0)
