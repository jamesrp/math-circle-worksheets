"""Grades 2-3 packet (F01E-M-v1): every problem, from the boards as drawn in the delivered PDF.
Writes check_middle.out."""
import os
import sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import *
from fastgame import Board

log = Log(os.path.join(HERE, 'check_middle.out'))
BAND = 'grades-2-3'
ALL = lambda R: greens(R) + blues(R) + reds(R) + yellows(R)


def mix_str(m):
    y, r, b, g = m
    return ', '.join(f'{n} {k}' for n, k in ((y, 'yellow'), (r, 'red'), (b, 'blue'), (g, 'green')) if n)


def page_up(c, frame):
    """True if the cell points up on the printed page (two vertices share the lowest y)."""
    ys = sorted(frame.to_page(v)[1] for v in c)
    return abs(ys[0] - ys[1]) < 1e-6


def game(o, label=''):
    Bd = Board(o.R)
    w, good, moves = Bd.solve()
    ht = half_turn_centre(o.R)
    s = f'  {label}{BD.classify(o)}: {describe(o.R)}; {len(moves)} first moves; winner {w}'
    if w == '1st':
        s += f'; {len(good)} winning first moves'
    if ht:
        (si, sj), kind = ht
        s += f'; half-turn centre is a lattice {"point" if kind == "vertex" else "edge midpoint"}'
        if kind == 'edge':
            selfimg = [mv for mv in moves if frozenset(frozenset((si - v[0], sj - v[1]) for v in c) for c in Bd.move_cells(mv)) == Bd.move_cells(mv)]
            s += f'; {len(selfimg)} self-symmetric blue(s), winning: {[mv in good for mv in selfimg]}'
    else:
        s += '; no half-turn symmetry'
    log(s)
    return w, good, moves


log('Grades 2-3 packet, delivered PDF', os.path.relpath(PP.PDFS[BAND], PP.ROOT))

log('\nProblem 1 (page 1): four small boards')
for o in stroked_boards(BAND, 1, min_lw=1.5):
    game(o)

log('\nProblem 2 (page 2): two triangles and the 4-by-2 board')
for o in stroked_boards(BAND, 2, min_lw=1.5):
    game(o)
    if o.sides and len(o.sides) == 3:
        log(f'    possible game lengths: {sorted(game_lengths(o.R))}')
        # corner partners of the down cells
        downs = [c for c in o.R if not is_up(c)]
        corner_ups = [c for c in o.R if is_up(c) and len(nbrs(o.R, c)) == 1]
        log(f'    {len(downs)} down cells, {len(corner_ups)} up cells with a single neighbour (private partners): '
            f'{sorted(len([u for u in corner_ups if adjacent(u, d)]) for d in downs)} per down cell')

log('\nProblem 3 (page 3): fewest pieces on the 2x hexagon and triangle 4')
P3 = stroked_boards(BAND, 3, min_lw=1.5)
for o in P3:
    mn, cnt, mixes, by_y = fewest(o.R, ALL(o.R))
    log(f'  {BD.classify(o)}: {describe(o.R)}; fewest {mn} in {cnt} tilings; mixes {[mix_str(m) for m in sorted(mixes)]}; '
        f'by yellows {[(y, v[0]) for y, v in sorted(by_y.items())]}')
    ys = yellows(o.R)
    mx, packs = max_packing(o.R, ys)
    log(f'    max yellows {mx} in {len(packs)} placements; leftover components with a max placement: '
        f'{[sorted(len(c) for c in components(o.R - frozenset().union(*pk))) for pk in packs]}')
    if len(o.R) == 24:
        pts = Counter(v for c in o.R for v in c)
        centre = [p for p, k in pts.items() if k == 6 and all(unit_hex(p) <= o.R for _ in [0])]
        # the middle point is the one whose six cells are all interior and whose distance to all corners is equal
        cx = sum(centroid(c)[0] for c in o.R) / len(o.R)
        cy = sum(centroid(c)[1] for c in o.R) / len(o.R)
        mid = min(pts, key=lambda p: (lcart(p)[0] - cx) ** 2 + (lcart(p)[1] - cy) ** 2)
        H = unit_hex(mid)
        log(f'    each possible yellow covers this many of the six cells round the middle point: {sorted(len(y & H) for y in ys)}')
        # min with exactly 2 yellows: any 2 yellows + 4 reds?
        log(f'    fewest with exactly 2 yellows: {by_y.get(2, (None,))[0]}; with 1: {by_y.get(1, (None,))[0]}; with 0: {by_y.get(0, (None,))[0]}')

log('\nProblem 4 (page 4): red trapezoid fillings and their two-up / two-down counts')
P4 = stroked_boards(BAND, 4)
tri = [o for o in P4 if o.lw > 1.5][0]
hexb = P3[0] if len(P3[0].R) == 24 else P3[1]
for name, o in (('triangle 3 (page 4)', tri), ('2x hexagon (from Problem 3, page 3)', hexb)):
    Ts = all_tilings(o.R, reds(o.R))
    kinds = Counter()
    for T in Ts:
        up2 = sum(1 for p in T if sum(page_up(c, o.frame) for c in p) == 2)
        kinds[(up2, len(T) - up2)] += 1
    nup = sum(page_up(c, o.frame) for c in o.R)
    log(f'  {name}: {len(o.R)} cells, {nup} pointing up and {len(o.R) - nup} down on the page; {len(Ts)} red fillings; '
        f'(two-up, two-down) counts: {dict(kinds)}')
    if len(o.R) == 9:
        T1, T2 = Ts
        mirror = lambda T: frozenset(frozenset(frozenset(refl(v) for v in c) for c in p) for p in T)
        log(f'    the two triangle fillings are mirror images of each other: {translate_to(frozenset().union(*mirror(T1)), o.R) is not None and shift(mirror(T1), translate_to(frozenset().union(*mirror(T1)), o.R)) == T2}')
small_tri = [o for o in P4 if o.lw < 1.5 and len(o.R) == 9]
small_hex = [o for o in P4 if o.lw < 1.5 and len(o.R) == 24]
log(f'  recording copies: {len(small_tri)} triangles, {len(small_hex)} hexagons; all drawn with horizontal grid lines '
    f'(theta 0): {all(abs(o.theta) < 0.5 for o in P4)}')

log('\nProblem 5 (page 5): strategy on the 2x hexagon and the 3-by-3 board')
for o in stroked_boards(BAND, 5, min_lw=1.5):
    game(o)

log('\nProblem 6 (page 6): fewest pieces on the 3x hexagon')
o = stroked_boards(BAND, 6, min_lw=1.5)[0]
mn, cnt, mixes, by_y = fewest(o.R, ALL(o.R))
log(f'  {BD.classify(o)}: {describe(o.R)}; fewest {mn} in {cnt} tilings; mixes {[mix_str(m) for m in sorted(mixes)]}')
log(f'  fewest for each number of yellows: {[(y, v[0], v[1]) for y, v in sorted(by_y.items())]}  (yellows, fewest, how many tilings)')
ys = yellows(o.R)
mx, packs = max_packing(o.R, ys)
for pk in packs:
    left = o.R - frozenset().union(*pk)
    comps = components(left)
    f = fewest(left, ALL(left))
    log(f'  a placement of {mx} yellows leaves components of sizes {sorted(len(c) for c in comps)}; fewest total {mx + f[0]}')
Tmin = min_tilings(o.R, ALL(o.R), mn)
if len(Tmin) == 2:
    A_, B_ = Tmin
    rel = []
    for k, f in enumerate(SYMS):
        img = map_cells(f, frozenset().union(*A_))
        d = translate_to(img, o.R)
        if d is not None:
            imgT = shift(frozenset(map_cells(f, p) for p in A_), d)
            if imgT == B_:
                rel.append(k)
    log(f'  the two fewest tilings are related by lattice symmetries with index {rel} '
        f'(index = 2*rotation_steps + reflection; rotation by 60 degrees is index 2)')

log('\nProblem 7 (page 7): triangle 6 with reds')
o = stroked_boards(BAND, 7, min_lw=1.5)[0]
nup = sum(page_up(c, o.frame) for c in o.R)
n = count_tilings(o.R, reds(o.R))
Ts = all_tilings(o.R, reds(o.R))
dist = Counter(sum(1 for p in T if sum(page_up(c, o.frame) for c in p) == 1) for T in Ts)
log(f'  {BD.classify(o)}: {len(o.R)} cells, {nup} up, {len(o.R) - nup} down; {n} red fillings (enumerated {len(Ts)}); '
    f'number of two-down trapezoids -> fillings: {dict(dist)}')
log(f'  recording copies: {len([b for b in stroked_boards(BAND, 7) if b.lw < 1.5])}')

log.save()
