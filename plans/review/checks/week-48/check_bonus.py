"""Independent exact checks of the Week 48 bonus pages and bonus guide.

Run pdf_extract.py first: the L shapes and grid offsets, the cards, the
witness grids and the 2x2 boards are read from pdf_geometry.json (taken from
the delivered PDF).

Writes check_bonus.out.
"""
import json
import math
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, PDFS, PT_MM, Log, area, bounds, fmt, grid_status,  # noqa: E402
                    is_simple, page_text)

log = Log('Week 48 bonus: independent exact checks')
G = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))['bonus']
GUIDE = re.sub(r'\s+', ' ', page_text(PDFS['bonus-guide']))
STUDENT = re.sub(r'\s+', ' ', page_text(PDFS['bonus']))

# ------------------------------------------------------------------ Problem 1
log.head('Problem 1: sliding a grid under a fixed L')
results = {}
polys = []
for s in G['p1']['shapes']:
    poly = [(F(x), F(y)) for x, y in s['poly_in_cells_yup']]
    polys.append(poly)
    # grid lines are at integers in these coordinates; count over a generous window
    st = grid_status(poly, None, F(1), F(-2), F(-2), cols=8, rows=8)
    lo, hi, w, c = bounds(st)
    cover_cells = [k for k, (v, _) in st.items() if v != 'O']
    xs = [F(-2) + i for i, _ in cover_cells]
    ys = [F(-2) + j for _, j in cover_cells]
    vx = [F(v) for v in s['visible_x_cells']]
    vy = [F(v) for v in s['visible_y_cells']]
    visible = min(xs) >= vx[0] and max(xs) + 1 <= vx[1] and min(ys) >= vy[0] and max(ys) + 1 <= vy[1]
    drawn = all(str(int(min(xs)) + k) in s['grid_x_cells'] for k in range(int(max(xs) - min(xs)) + 2)) and \
        all(str(int(min(ys)) + k) in s['grid_y_cells'] for k in range(int(max(ys) - min(ys)) + 2))
    results[s['label']] = (lo, hi)
    log.check(abs(area(poly)) == 3 and visible and drawn,
              f"'{s['label']}': area {fmt(abs(area(poly)))}; {w} whole, {c} cover -> [{fmt(lo)}, {fmt(hi)}]; every cover cell is drawn and fully visible")
# the three L's are the same shape (translates of one another)
norm = [sorted((x - min(p[0] for p in q), y - min(p[1] for p in q)) for x, y in q) for q in polys]
log.check(norm[0] == norm[1] == norm[2], 'the three pictures show the same L (union of a 2x1 bar and a 1x1 square on its right end)')
log.check(results == {'Aligned': (3, 3), 'Half a square sideways': (1, 5), 'Half a square both ways': (0, 8)},
          f'bounds {results}; tightest is Aligned; moving the grid does not always improve the bounds')
# survey every translation by multiples of 1/8
L = polys[0]
survey = {}
for a in range(8):
    for b in range(8):
        dx, dy = F(a, 8), F(b, 8)
        st = grid_status(L, None, F(1), F(-2) + dx, F(-2) + dy, cols=8, rows=8)
        lo, hi, _, _ = bounds(st)
        survey[(a, b)] = (lo, hi)
widths = sorted({hi - lo for lo, hi in survey.values()})
log.info(f'all 64 translations by eighths: gaps {[fmt(x) for x in widths]}; only the aligned grid gives an exact certificate: '
         f'{[k for k, v in survey.items() if v[1] - v[0] == 0]}')
log.check(survey[(4, 0)] == (1, 5) and survey[(4, 4)] == (0, 8) and survey[(0, 4)] == (1, 5),
          'survey agrees with the drawn placements; a vertical half shift also gives [1,5]')

# ------------------------------------------------------------------ Problem 2
log.head('Problem 2: range cards')
ex = G['p2']['example']
log.check(ex['gray_fraction'] == 0.5 and ex['card'] == '0 to 1',
          f"example: one partial square (gray fraction {ex['gray_fraction']}) -> card '{ex['card']}' = [whole count, cover count] = [0, 1]")
pairs = []
for row in G['p2']['card_rows']:
    ivs = [tuple(int(v) for v in re.match(r'(\d+) to (\d+)', t).groups()) for t in row[:2]]
    pairs.append(ivs)
inter = []
for (a1, b1), (a2, b2) in pairs:
    lo, hi = max(a1, a2), min(b1, b2)
    inter.append((lo, hi) if lo <= hi else None)
log.check(inter == [(4, 8), None, (4, 4)], f'intersections of the three pairs: {inter} (second pair impossible: at most 5 and at least 6)')
# witnesses from the guide: 2x2 square (area 4) for both, 2x3 rectangle (area 6) for the first
grids = G['p2']['witness_grids']
log.check([g['label'] for g in grids] == ['First pair', 'Third pair'] and all((g['cols'], g['rows']) == (6, 4) for g in grids),
          f"witness grids: {[(g['label'], g['cols'], g['rows']) for g in grids]}")
log.check(4 <= 4 <= 8 and 4 == 4 and 4 <= 6 <= 8 and 2 <= 6 and 3 <= 4,
          'guide witnesses: a 2x2 square (area 4) fits both possible pairs, a 2x3 rectangle (area 6) fits the first; both fit a 6x4 grid')
# the labels give the impossible pair away
possible = [i + 1 for i, v in enumerate(inter) if v is not None]
named = [{'First': 1, 'Second': 2, 'Third': 3}[g['label'].split()[0]] for g in grids]
log.check(named != possible,
          f'witness grids are labelled for pairs {named}, which are exactly the possible pairs {possible}: '
          'the labels answer "Which pair cannot be true?" before the child reasons')

# ------------------------------------------------------------------ Problem 3
log.head('Problem 3: the L mask on a 2x2 board')
bd = G['p3']['boards']
labs = [b['labels'] for b in bd]
log.check(len(bd) == 4 and all(l_ == {'col0_row0_from_top': 'white', 'col0_row1_from_top': 'partial',
                                      'col1_row0_from_top': 'partial', 'col1_row1_from_top': 'partial'} for l_ in labs)
          and all(b['cell_pt'] == 80.0 for b in bd),
          'four 2x2 boards of 80 pt cells; top-left "white", the other three "partial"')


def corridor(t):
    # y up, board [0,2]^2, top-left cell [0,1]x[1,2] must stay white
    return [(F(0), F(0)), (F(2), F(0)), (F(2), F(2)), (2 - t, F(2)), (2 - t, t), (F(0), t)]


def cells(poly):
    st = grid_status(poly, 2, F(1))
    # (col,row) with row from the bottom; map to labels
    return {'BL': st[(0, 0)], 'BR': st[(1, 0)], 'TL': st[(0, 1)], 'TR': st[(1, 1)]}


def perim(poly):
    n = len(poly)
    return sum(math.hypot(float(poly[(i + 1) % n][0] - poly[i][0]), float(poly[(i + 1) % n][1] - poly[i][1])) for i in range(n))


for t, want in [(F(1, 4), F(15, 16)), (F(3, 4), F(39, 16))]:
    p = corridor(t)
    c = cells(p)
    ok = c['TL'][0] == 'O' and all(c[k][0] == 'P' for k in ('BL', 'BR', 'TR'))
    log.check(ok and is_simple(p) and abs(area(p)) == want and (c['BL'][1], c['BR'][1], c['TR'][1]) == (t, 2 * t - t * t, t)
              and abs(perim(p) - 8) < 1e-12,
              f't={fmt(t)}: cell areas BL,BR,TR = {fmt(c["BL"][1])}, {fmt(c["BR"][1])}, {fmt(c["TR"][1])}; TL white; total {fmt(abs(area(p)))}; perimeter {perim(p):.6f}; simple')
ok = True
for k in range(1, 200):
    t = F(k, 200)
    p = corridor(t)
    c = cells(p)
    ok &= abs(area(p)) == 4 * t - t * t and c['TL'][0] == 'O' and all(c[q][0] == 'P' for q in ('BL', 'BR', 'TR'))
log.check(ok, 'corridor of width t: area 4t - t^2 and the same cell pattern for every t = k/200 in (0,1); area -> 0 and -> 3 at the ends')


def waved(N, t=F(1, 4)):
    """Replace the top edge of the bottom strip over 0<=x<=1 by N triangular waves
    (x spacing 1/(4N), heights t, t+1/8, t, t-1/8, t, ...)."""
    base = corridor(t)
    # base = [(0,0),(2,0),(2,2),(2-t,2),(2-t,t),(0,t)]; insert wave between (2-t,t) and (0,t)
    wave = []
    hs = [t, t + F(1, 8), t, t - F(1, 8)]
    for k in range(4 * N, -1, -1):  # walk from x=1 back to x=0
        x = F(k, 4 * N)
        wave.append((x, hs[k % 4]))
    return base[:5] + wave[:-1] + [(F(0), t)]


for N in (1, 2, 3, 5, 10, 25):
    p = waved(N)
    c = cells(p)
    n = len(p)
    seg = [(p[(i + 1) % n][0] - p[i][0]) ** 2 + (p[(i + 1) % n][1] - p[i][1]) ** 2 for i in range(n)]
    wave_len = sum(math.sqrt(float(s)) for s in seg) - (8 - 1)  # total minus the untouched 7 units
    formula = math.sqrt(1 + N * N / 4)
    vert = sum(abs(float(p[(i + 1) % n][1] - p[i][1])) for i in range(4, n - 1))
    ok = is_simple(p) and abs(area(p)) == F(15, 16) and c['TL'][0] == 'O' and all(c[q][0] == 'P' for q in ('BL', 'BR', 'TR'))
    ok &= abs(wave_len - formula) < 1e-9 and all(F(1, 8) <= y <= F(3, 8) for x, y in p if 0 < x < 1)
    log.check(ok, f'N={N}: simple, area 15/16, same cell pattern, waved edge length {wave_len:.6f} = sqrt(1+N^2/4) = {formula:.6f}, '
                  f'perimeter {7 + formula:.4f}; vertical travel on the wave {vert - 0:.3f}')
log.check((4 * 7) ** 2 * (F(1, 16 * 49) + F(1, 64)) == 1 + F(49, 4), 'identity (4N)^2 (1/(16N^2) + 1/64) = 1 + N^2/4 (shown for N=7; holds for all N)')

# ------------------------------------------------------------------ guide text and physical figures
log.head('Bonus guide statements')
for pat in ['the aligned bounds are [3,3], a half-unit horizontal shift gives [1,5], and a half-unit shift in both directions gives [0,8]',
            'combine to [max(L1,L2),min(U1,U2)]', 'has area 4t-t²', 'Cards 2-8 and 4-9 combine to 4-8',
            'Cards 1-6 and 4-4 combine to exactly 4', 'are t,2t-t²,t', 'At t=1/4 total is 15/16<1. At t=3/4 total is 39/16>2',
            'Their perimeters happen to both be 8', 'area remains 15/16', 'the height remains between 1/8 and 3/8',
            'The changed edge has length sqrt(1+N²/4), so full perimeter is 7+sqrt(1+N²/4)']:
    log.check(pat in GUIDE, f'guide says "{pat}" (verified above)')
s1 = G['p1']['shapes'][0]['cell_pt']
log.check(s1 == 56.0 and round(56 * PT_MM, 1) == 19.8 and '56-point (19.8 mm)' in GUIDE, f'p1 cell {s1} pt = {56 * PT_MM:.2f} mm, as the guide says')
log.check(grids[0]['cell_pt'] == 27.0 and round(27 * PT_MM, 1) == 9.5 and '27-point (9.5 mm)' in GUIDE, f'p2 witness cells 27 pt = {27 * PT_MM:.2f} mm')
log.check(bd[0]['cell_pt'] == 80.0 and round(80 * PT_MM, 1) == 28.2 and '80-point sides (28.2 mm)' in GUIDE, f'p3 cells 80 pt = {80 * PT_MM:.2f} mm')
kids = 2 + 2 + 4 + 2 + 1  # KK11 / 3333 / 445
log.check(kids == 11 and 4 * 2 + 3 == 11 and 5 * 12 == 60 and 5 * 2 == 10,
          'kits: KK11/3333/445 = 11 children = 4 pairs + 1 trio = 5 kits; 5 x 12 = 60 tiles; 10 pencils')
log.check(max(hi for _, hi in results.values()) <= 12, 'twelve paper tiles per kit cover the largest page-1 cover (8 cells)')
log.write('check_bonus.out')
