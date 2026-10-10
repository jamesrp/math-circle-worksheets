"""Independent exact checks of the Week 48 base packets (K-1, 2-3, 4-5) and the
base facilitator guide.

Run pdf_extract.py first: every shape is read from pdf_geometry.json (taken
from the delivered PDFs). Coordinates are in big-square units, origin at the
top-left corner of the board, y DOWN (statuses do not depend on orientation).

Writes check_base.out.
"""
import json
import os
import random
import re
import sys
from fractions import Fraction as F
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, PDFS, Log, area, bounds, classify, fmt, grid_status,  # noqa: E402
                    is_simple, page_text)

log = Log('Week 48 base packets: independent exact checks')
G = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))
GUIDE = re.sub(r'\s+', ' ', page_text(PDFS['guide']))
HALF = F(1, 2)


def shape(band, page, k=0):
    b = G[band]['pages'][page - 1]['boards'][k]
    return [(F(x), F(y)) for x, y in b['outline_big']], b


def coarse(poly):
    return grid_status(poly, 4, F(1))


def fine(poly):
    return grid_status(poly, 8, HALF)


def children(poly, i, j):
    """Statuses of the four half-size children of big cell (i,j)."""
    return [classify(poly, i + a * HALF, j + b * HALF, HALF)[0] for b in range(2) for a in range(2)]


def summary(st):
    return {s: sum(1 for v, _ in st.values() if v == s) for s in 'WPO'}


# ----------------------------------------------------------- shapes from PDF
TRI, _ = shape('k-1', 1)
TRAP, _ = shape('k-1', 2)
TRI_FINE, _ = shape('k-1', 3)
DIA_FINE_K, _ = shape('k-1', 4)
DIA, _ = shape('grades-2-3', 2)
DIA_FINE, _ = shape('grades-2-3', 4)
TRAP45, _ = shape('grades-4-5', 5)

log.head('All boards: same shapes across bands')
for band in ('k-1', 'grades-2-3', 'grades-4-5'):
    log.check(shape(band, 1)[0] == TRI and shape(band, 3)[0] == TRI_FINE == TRI,
              f'{band}: P1 and P3 triangle is {[(fmt(x), fmt(y)) for x, y in TRI]} (big units), the same on both pages')
for band in ('grades-2-3', 'grades-4-5'):
    log.check(shape(band, 2)[0] == DIA and shape(band, 4)[0] == DIA,
              f'{band}: P2 and P4 diamond is {[(fmt(x), fmt(y)) for x, y in DIA]}')
log.check(DIA_FINE_K == DIA, 'K-1 P4 diamond is the same diamond')
log.check(TRAP == TRAP45, f'K-1 P2 and 4-5 P5 trapezoid is {[(fmt(x), fmt(y)) for x, y in TRAP]}')
for nm, p in [('triangle', TRI), ('diamond', DIA), ('trapezoid', TRAP)]:
    log.info(f'{nm}: exact area {fmt(abs(area(p)))}, simple polygon {is_simple(p)}')

# ----------------------------------------------------------- triangle P1, P3
log.head('Triangle (all bands P1, P3; 4-5 P7)')
st = coarse(TRI)
lo, hi, w, c = bounds(st)
log.check((w, c) == (6, 10), f'P1 coarse: {w} whole, {c} cover cells -> {fmt(lo)} <= area <= {fmt(hi)}; partial {c - w}')
rows_w = [sum(1 for i in range(4) if st[(i, j)][0] == 'W') for j in range(4)]
rows_c = [sum(1 for i in range(4) if st[(i, j)][0] != 'O') for j in range(4)]
log.check(rows_w == [0, 1, 2, 3] and rows_c == [1, 2, 3, 4],
          f'guide P1: rows top to bottom have {rows_w} whole and {rows_c} cover cells')
diag = [(i, j) for (i, j), (s, _) in st.items() if s == 'P']
log.check(sorted(diag) == [(0, 3), (1, 2), (2, 1), (3, 0)], f'the four partial cells are the diagonal cells {sorted(diag)}')
stf = fine(TRI)
lo2, hi2, w2, c2 = bounds(stf, HALF)
log.check((w2, c2, lo2, hi2) == (28, 36, 7, 9), f'P3 fine: {w2} whole, {c2} cover small cells -> {fmt(lo2)} <= area <= {fmt(hi2)}')
pats = sorted(tuple(sorted(children(TRI, i, j))) for i, j in diag)
log.check(all(p == ('O', 'P', 'P', 'W') for p in pats), f'guide P3: each partial big triangle cell splits into 1 whole, 2 partial, 1 outside: {pats[0]}')
log.check((hi - lo, hi2 - lo2) == (4, 2), f'guide: triangle gap falls from {fmt(hi - lo)} to {fmt(hi2 - lo2)}')
A_tri = abs(area(TRI))
log.check(A_tri == 8 and lo <= A_tri <= hi and lo2 <= A_tri <= hi2,
          f'4-5 P7: exact area {fmt(A_tri)} = 16/2, inside [6,10] and [7,9]')
# Other reading of K-1 P1 "as few grid-square tiles as you can": tiles not on the grid.
# Ten points with pairwise L-infinity distance 4/3 > 1 lie in the closed triangle, so no
# axis-parallel unit square holds two of them: 10 tiles are needed even off the grid.
pts = [(F(4, 3) * i, F(4, 3) * j) for i in range(4) for j in range(4) if i + j <= 3]
in_tri = all(x >= 0 and y >= 0 and x + y <= 4 for x, y in pts)
sep = min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a, b in combinations(pts, 2))
log.check(len(pts) == 10 and in_tri and sep > 1,
          f'K-1 P1 other reading: {len(pts)} points of the triangle are pairwise > 1 apart in L-inf (min {fmt(sep)}), so even unaligned axis-parallel tiles need 10')

# ----------------------------------------------------------- diamond P2, P4
log.head('Diamond (2-3 and 4-5 P2, P4; K-1 P4)')
sd = coarse(DIA)
lo, hi, w, c = bounds(sd)
centre = sorted(k for k, (s, _) in sd.items() if s == 'W')
log.check((w, c) == (4, 12) and centre == [(1, 1), (1, 2), (2, 1), (2, 2)],
          f'P2 coarse: whole {centre} (the four central cells), {c - w} partial -> {fmt(lo)} <= area <= {fmt(hi)}')
log.check(lo > 3 and hi < 13, 'P2: "more than 3" and "less than 13" are both certain (4 > 3, 12 < 13)')
sdf = fine(DIA)
lo2, hi2, w2, c2 = bounds(sdf, HALF)
log.check((w2, c2, lo2, hi2) == (24, 40, 6, 10), f'P4 fine: {w2} whole, {c2} cover small cells -> {fmt(lo2)} <= area <= {fmt(hi2)}')
log.check((hi - lo, hi2 - lo2) == (8, 4), f'guide P4: diamond gap falls from {fmt(hi - lo)} to {fmt(hi2 - lo2)}')
dpart = [k for k, (s, _) in sd.items() if s == 'P']
pats = {tuple(sorted(children(DIA, i, j))) for i, j in dpart}
log.check(pats == {('O', 'P', 'P', 'W')}, f'guide: every partial big diamond cell has children 1 whole, 2 partial, 1 outside {pats}')
log.check(abs(area(DIA)) == 8, 'diamond exact area 8 (inside both pairs of bounds)')

# K-1 P4: which outside small cells can become partial without changing a big status?
outside_small = [k for k, (s, _) in sdf.items() if s == 'O']
in_partial_big = [(i, j) for (i, j) in outside_small if sd[(i // 2, j // 2)][0] == 'P']
in_outside_big = [(i, j) for (i, j) in outside_small if sd[(i // 2, j // 2)][0] == 'O']
log.check(len(outside_small) == 24 and len(in_partial_big) == 8 and len(in_outside_big) == 16,
          f'K-1 P4: {len(outside_small)} outside small cells; {len(in_partial_big)} lie in partial big cells (one each), '
          f'{len(in_outside_big)} lie in the four outside corner big cells (any gray there would change that big cell)')


def touch_points(poly, cells):
    """For each outside small cell, the boundary point(s) of the polygon it touches."""
    res = {}
    for (i, j) in cells:
        x0, y0 = i * HALF, j * HALF
        cs = [(x0, y0), (x0 + HALF, y0), (x0, y0 + HALF), (x0 + HALF, y0 + HALF)]
        on = [p for p in cs if abs(p[0] - 2) + abs(p[1] - 2) == 2]  # the diamond |x-2|+|y-2|<=2
        res[(i, j)] = on
    return res


tp = touch_points(DIA, in_partial_big)
log.check(all(len(v) == 1 for v in tp.values()), 'K-1 P4: each of those 8 cells touches the diamond at exactly one corner point (a corner touch, so it is outside)')


def bulged(poly, points, e=F(1, 16), d=F(1, 8)):
    """Insert an outward triangular bulge at each given boundary point."""
    out = []
    n = len(poly)
    for k in range(n):
        a, b = poly[k], poly[(k + 1) % n]
        out.append(a)
        on_edge = []
        for p in points:
            # p on segment ab (strictly inside)?
            cross = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
            if cross == 0 and min(a[0], b[0]) < p[0] < max(a[0], b[0]):
                t = (p[0] - a[0]) / (b[0] - a[0])
                on_edge.append((t, p))
        for t, p in sorted(on_edge):
            ux, uy = (b[0] - a[0]), (b[1] - a[1])
            L1 = abs(ux) + abs(uy)
            ux, uy = ux / L1 * 2, uy / L1 * 2   # unit-ish step along the edge (|ux|=|uy|=1 for 45-degree edges)
            nx, ny = (1 if p[0] > 2 else -1), (1 if p[1] > 2 else -1)  # outward diagonal for the diamond
            out += [(p[0] - e * ux, p[1] - e * uy), (p[0] + d * nx, p[1] + d * ny), (p[0] + e * ux, p[1] + e * uy)]
    return out


for k in (4, 8):
    chosen = sorted(in_partial_big)[:k] if k == 8 else [c for c in sorted(in_partial_big)][::2]
    pts = [tp[c][0] for c in chosen]
    new = bulged(DIA, pts)
    ns, nsf = coarse(new), fine(new)
    big_same = all(ns[c][0] == sd[c][0] for c in sd)
    became = [c for c in outside_small if nsf[c][0] == 'P']
    other_changes = [c for c in sdf if sdf[c][0] != nsf[c][0] and c not in became]
    log.check(is_simple(new) and big_same and len(became) == k and not other_changes,
              f'K-1 P4: bulging the diamond at {k} corner points makes exactly {len(became)} outside small cells partial, '
              f'no other small-cell change, every big status unchanged (area {fmt(abs(area(new)))})')
log.info('So the K-1 P4 target of four is reachable, and up to eight such cells can change; never more.')

# ----------------------------------------------------------- trapezoid
log.head('Trapezoid (K-1 P2, 4-5 P5)')
stz = coarse(TRAP)
lo, hi, w, c = bounds(stz)
log.check((w, c) == (4, 16), f'coarse: {w} whole, all {c} cells in the cover -> {fmt(lo)} <= area <= {fmt(hi)}; exact area {fmt(abs(area(TRAP)))}')
smallest = min((a for (s, a) in stz.values() if s == 'P'))
which = [k for k, (s, a) in stz.items() if a == smallest]
log.info(f'smallest gray piece in a cover cell: {fmt(smallest)} of a big square ({float(smallest) * 900:.1f} mm^2) in cells {which}')
kids = {k: children(TRAP, *k) for k in stz}
types = {}
for k, ch in kids.items():
    sig = (ch.count('W'), ch.count('P'), ch.count('O'))
    old_gap = 1 if stz[k][0] == 'P' else 0
    new_gap = F(ch.count('P'), 4)
    types.setdefault((sig, old_gap - new_gap), []).append(k)
for (sig, red), ks in sorted(types.items()):
    log.info(f'children I/P/O = {sig}, gap reduction {fmt(red)}: cells (col,row from 0) {sorted(ks)}')
corners = [(0, 0), (3, 0), (0, 3), (3, 3)]
topbot = [(1, 0), (2, 0), (1, 3), (2, 3)]
sides = [(0, 1), (0, 2), (3, 1), (3, 2)]
centre = [(1, 1), (2, 1), (1, 2), (2, 2)]
exp = {((0, 1, 3), F(3, 4)): corners, ((2, 0, 2), F(1)): topbot, ((0, 2, 2), F(1, 2)): sides, ((4, 0, 0), F(0)): centre}
log.check({k: sorted(v) for k, v in types.items()} == {k: sorted(v) for k, v in exp.items()},
          'guide 4-5 P5 table: top/bottom middle 2/0/2 (1), corners 0/1/3 (3/4), left/right middle 0/2/2 (1/2), centre 4/0/0 (0)')

# K-1 P2: split two big tiles; remove the most small tiles (outside children) keeping the shape covered
removable = {k: kids[k].count('O') for k in stz}
best = max(removable[a] + removable[b] for a, b in combinations(stz, 2))
arg = sorted(tuple(sorted((a, b))) for a, b in combinations(stz, 2) if removable[a] + removable[b] == best)
log.check(best == 6 and all(set(p) <= set(corners) for p in arg) and len(arg) == 6,
          f'K-1 P2: most removable small tiles with two splits = {best}; optimal pairs = the {len(arg)} pairs of corner cells')
log.check(max(removable.values()) == 3 and all(kids[k].count('O') < 4 for k in stz if stz[k][0] != 'O'),
          'guide K-1 P2: no covered big cell can lose all four children; 3 is the per-tile maximum')
log.check(16 - F(best, 4) == F(29, 2), 'guide K-1 P2: remaining cover 16 - 6/4 = 14.5 big units')

# 4-5 P5: three splits, minimise the gap
gap0 = hi - lo


def bounds_after(split):
    inside = sum(1 for k in stz if stz[k][0] == 'W' and k not in split)
    cover = sum(1 for k in stz if stz[k][0] != 'O' and k not in split)
    for k in split:
        inside += F(kids[k].count('W'), 4)
        cover += F(kids[k].count('W') + kids[k].count('P'), 4)
    return inside, cover


res = {}
for tri3 in combinations(sorted(stz), 3):
    i, cv = bounds_after(tri3)
    res[tri3] = (i, cv, cv - i)
best_gap = min(v[2] for v in res.values())
opt = sorted(k for k, v in res.items() if v[2] == best_gap)
i, cv, g = res[opt[0]]
log.check(len(res) == 560 and best_gap == 9 and all(set(t) <= set(topbot) for t in opt) and len(opt) == 4 and (i, cv) == (F(11, 2), F(29, 2)),
          f'4-5 P5: over all 560 triples the least gap is {fmt(best_gap)} (from {fmt(gap0)}), reached only by the {len(opt)} triples of top/bottom middle cells; bounds {fmt(i)} and {fmt(cv)}')
# other reading: "gap" as the NUMBER of uncertain (partial) cells, big or small
cnt = {}
for tri3 in combinations(sorted(stz), 3):
    n_unc = sum(1 for k in stz if stz[k][0] == 'P' and k not in tri3) + sum(kids[k].count('P') for k in tri3)
    cnt[tri3] = n_unc
least = min(cnt.values())
opt_cnt = sorted(k for k, v in cnt.items() if v == least)
log.check(opt_cnt == opt, f'4-5 P5 other reading (count uncertain cells, not area): least count {least}, reached by the same {len(opt_cnt)} triples')
kbest = max(res, key=lambda t: sum(removable[k] for k in t))
log.info(f'contrast: the K-1 removal count is largest for corners ({sum(removable[k] for k in kbest)} tiles for three corners), '
         f'but three corners leave gap {fmt(res[tuple(sorted(corners[:3]))][2])}')

# ----------------------------------------------------------- shape-building tasks
log.head('Shape-building tasks (K-1 P5-6, 2-3 P5-6)')


def rect(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


for h, want in [(F(7, 6), F(7, 2)), (F(11, 6), F(11, 2)), (F(23, 12), F(23, 4))]:
    r = rect(F(0), F(0), F(3), h)
    s = summary(coarse(r))
    a = abs(area(r))
    log.check(s['W'] == 3 and s['P'] == 3 and a == want,
              f'K-1 P5/P6 witness: width 3, height {fmt(h)} -> {s["W"]} whole, {s["P"]} partial, area {fmt(a)}')
same = [k for k, (st_, _) in coarse(rect(F(0), F(0), F(3), F(7, 6))).items() if st_ != 'O'] == \
    [k for k, (st_, _) in coarse(rect(F(0), F(0), F(3), F(23, 12))).items() if st_ != 'O']
log.check(same, 'K-1 P5/P6 witnesses use the same whole and partial cells')
for h, want in [(F(9, 8), F(9, 2)), (F(15, 8), F(15, 2))]:
    r = rect(F(0), F(0), F(4), h)
    s = summary(coarse(r))
    a = abs(area(r))
    log.check(s['W'] == 4 and s['P'] == 4 and a == want and (a < 5 or a > 7),
              f'2-3 P5 witness: width 4, height {fmt(h)} -> {s["W"]} whole, {s["P"]} partial, area {fmt(a)}')
# 2-3 P6 / K-1 P6 range: survey a family of shapes with fixed markings (rectangles of every height
# 1 < h < 2 in steps of 1/96, and every width 3 or 4) - area always strictly between whole and cover counts.
ok = True
for wdt in (3, 4):
    for k in range(1, 96):
        h = 1 + F(k, 96)
        r = rect(F(0), F(0), F(wdt), h)
        s = summary(coarse(r))
        a = abs(area(r))
        ok &= s['W'] == wdt and s['P'] == wdt and wdt < a < 2 * wdt
log.check(ok, '2-3 P6 / K-1 P6: with w whole and w partial cells the area is strictly between w and 2w in every surveyed case')

# ----------------------------------------------------------- refinement monotonicity (4-5 P6)
log.head('Refinement monotonicity (4-5 P6, guide overview)')
rng = random.Random(48)
bad = 0
tested = 0
for trial in range(300):
    # random simple (star-shaped) polygon with rational vertices inside [0,4]^2
    n = rng.randint(3, 9)
    cx, cy = F(rng.randint(12, 36), 12), F(rng.randint(12, 36), 12)
    angs = sorted(rng.random() for _ in range(n))
    import math
    poly = []
    for t in angs:
        r = rng.uniform(0.3, 1.9)
        x = min(max(cx + F(round(r * math.cos(2 * math.pi * t) * 24), 24), F(0)), F(4))
        y = min(max(cy + F(round(r * math.sin(2 * math.pi * t) * 24), 24), F(0)), F(4))
        poly.append((x, y))
    if len(set(poly)) < 3 or area(poly) == 0 or not is_simple(poly):
        continue
    tested += 1
    c4 = coarse(poly)
    for k, (s, _) in c4.items():
        ch = children(poly, *k)
        inside_old = 1 if s == 'W' else 0
        cover_old = 0 if s == 'O' else 1
        inside_new = F(ch.count('W'), 4)
        cover_new = F(4 - ch.count('O'), 4)
        if inside_new < inside_old or cover_new > cover_old:
            bad += 1
log.check(bad == 0 and tested > 200, f'on {tested} random simple polygons, no single big-cell split ever lowered the inside bound or raised the cover')
small = [(F(0), F(1)), (F(1), F(1)), (F(1), F(0))]  # 4-5 P6 diagram, one big cell
ch = children(small, 0, 0)
log.check(classify(small, F(0), F(0), F(1))[0] == 'P' and sorted(ch) == ['O', 'P', 'P', 'W'],
          f'4-5 P6 diagram: the diagonal big cell is partial and its children are {ch} (row by row): inside 0 -> 1/4, cover 1 -> 3/4')
p6 = G['grades-4-5']['pages'][5]['boards']
log.check(p6[0]['side_mm'] == p6[1]['side_mm'] == 30.0 and p6[1]['cells'] == 2,
          '4-5 P6 diagram: before and after squares are both 30 mm; the split is 2x2 of 15 mm')
log.check(p6[2]['cells'] == 4 and p6[3]['cells'] == 8 and p6[3]['cells_per_big'] == 2.0,
          '4-5 P7 small pictures: a 4x4 and an 8x8 (bold every 2) copy of the triangle')

# ----------------------------------------------------------- guide text
log.head('Guide statements (base facilitator guide)')
for pat in [r'All bands P1 triangle 6 big 10 big 6 ≤ area ≤ 10', r'Older P2 diamond 4 big 12 big 4 ≤ area ≤ 12',
            r'All bands P3 triangle 28 small 36 small 7 ≤ area ≤ 9', r'Older P4 diamond 24 small 40 small 6 ≤ area ≤ 10']:
    log.check(pat in GUIDE, f'guide table row present and verified above: "{pat}"')
for pat in ['successive rows from top to bottom contain 0,1,2,3 whole cells and 1,2,3,4 cover cells',
            'one whole, two partial and one outside small cell', 'falls from 8 to 4 big units', "triangle’s gap falls from 4 to 2",
            '16 - 6/4 = 14.5', 'Width 3 and height 7/6 gives area 3.5; width 3 and height 11/6 gives 5.5',
            'height 23/12, for example: area 5.75', 'heights 9/8 and 15/8 have areas 4.5 and 7.5',
            'The initial bounds 4 and 16 become 5.5 and 14.5, so the gap falls from 12 to 9',
            'exact area is 8 big-square units', 'Refine any three of (2,1), (3,1), (2,4), (3,4)']:
    log.check(pat in GUIDE, f'guide says "{pat}" (verified above)')
# guide coordinates (col,row) numbered from 1, columns left to right, rows top to bottom
named = [(1, 0), (2, 0), (1, 3), (2, 3)]
log.check(sorted(named) == sorted(topbot), 'guide (2,1),(3,1),(2,4),(3,4) as (column,row) from 1 are exactly the top/bottom middle cells')
# materials arithmetic
log.check('at least 8 paper 15 mm squares' in GUIDE, 'guide preparation lists "at least 8 paper 15 mm squares"')
need_k1 = 2 * 4
need_45 = 3 * 4
log.check(need_45 <= 8, f'paper small tiles needed: K-1 P2 two splits = {need_k1}; 4-5 P5 three splits = {need_45} '
          f'(the guide\'s "at least 8" covers K-1 P2 but not a paper version of 4-5 P5)')
present = 'Exactly four previously outside small cells can become partial' in GUIDE
log.check(present and len(in_partial_big) == 4,
          f'guide K-1 P4: "Exactly four previously outside small cells can become partial" read as a limit: '
          f'the most that can change with every big status kept is {len(in_partial_big)} (the 8-bulge shape above), not four')
log.write('check_base.out')
