"""Cross-checks with separately written code (Week 1 encore math check).

The other scripts use lat.py (pieces found from cell adjacency, exact cover in reading
order, Sprague-Grundy game values) and fastgame.py.  This script re-derives the key
answers a second way, using only the regions read from the PDFs by boards.py:

  * pieces generated from base shapes under the 12 lattice symmetries and translations
    (green, blue, red, yellow, and the purple chevron);
  * exact cover choosing the cell with the fewest candidate pieces, memoised on the
    covered set;
  * plain win/lose search of the placement game (no Grundy values, no symmetry);
  * maximum yellow packings by brute force over hexagon centres;
  * the fewest-piece answer for the 3x hexagon from the yellow argument alone;
  * two-down trapezoids counted from each trapezoid's middle cell;
  * the cube-face count of the 1,3,3 hexagon from rhombus directions.

Writes check_cross.out.
"""
import os
import sys
import time
from collections import Counter
from functools import lru_cache
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import stroked_boards, cluster, drawn_pieces, tiling_from_pieces, colour_name, Log
import boards as BD

log = Log(os.path.join(HERE, 'check_cross.out'))

# ---------------------------------------------------------------- lattice, written afresh
# point (i, j) = i*e1 + j*e2 with e2 at +60 degrees from e1


def up(i, j):
    return frozenset({(i, j), (i + 1, j), (i, j + 1)})


def dn(i, j):
    return frozenset({(i + 1, j), (i, j + 1), (i + 1, j + 1)})


def rot(p):            # +60 degrees
    return (-p[1], p[0] + p[1])


def flip(p):           # mirror across the e1 + e2 direction
    return (p[1], p[0])


BASE = {
    'green': [up(0, 0)],
    'blue': [up(0, 0), dn(0, 0)],
    'red': [up(0, 0), dn(0, 0), up(1, 0)],
    'yellow': [up(0, 0), dn(-1, 0), up(-1, 0), dn(-1, -1), up(0, -1), dn(0, -1)],
    'purple': [up(0, 0), dn(0, 0), up(0, 1), dn(-1, 1)],   # hexagon minus a rhombus (two blues on a shared edge)
}


def images(shape):
    out = set()
    for r in range(6):
        for s in range(2):
            def f(p, r=r, s=s):
                if s:
                    p = flip(p)
                for _ in range(r):
                    p = rot(p)
                return p
            out.add(frozenset(frozenset(f(v) for v in c) for c in shape))
    return out


def placements(kind, R):
    R = frozenset(R)
    verts = {v for c in R for v in c}
    out = set()
    for img in images(BASE[kind]):
        a = min(v for c in img for v in c)
        for b in verts:
            d = (b[0] - a[0], b[1] - a[1])
            P = frozenset(frozenset((v[0] + d[0], v[1] + d[1]) for v in c) for c in img)
            if P <= R:
                out.add(P)
    return list(out)


def count_cover(R, pieces):
    R = frozenset(R)
    by_cell = {c: [] for c in R}
    for P in pieces:
        for c in P:
            by_cell[c].append(P)

    @lru_cache(maxsize=None)
    def rec(free):
        if not free:
            return 1
        best = None
        for c in free:
            opts = [P for P in by_cell[c] if P <= free]
            if best is None or len(opts) < len(best):
                best = opts
                if len(opts) <= 1:
                    break
        return sum(rec(free - P) for P in best)
    n = rec(R)
    rec.cache_clear()
    return n


def all_covers(R, pieces):
    R = frozenset(R)
    by_cell = {c: [] for c in R}
    for P in pieces:
        for c in P:
            by_cell[c].append(P)
    out = []

    def rec(free, chosen):
        if not free:
            out.append(frozenset(chosen))
            return
        best = None
        for c in free:
            opts = [P for P in by_cell[c] if P <= free]
            if best is None or len(opts) < len(best):
                best = opts
        for P in best:
            chosen.append(P)
            rec(free - P, chosen)
            chosen.pop()
    rec(R, [])
    return out


def min_cover(R, pieces):
    """Fewest pieces in an exact cover (memoised; for regions up to about 30 cells)."""
    R = frozenset(R)
    by_cell = {c: [] for c in R}
    for P in pieces:
        for c in P:
            by_cell[c].append(P)

    @lru_cache(maxsize=None)
    def rec(free):
        if not free:
            return 0
        c = min(free, key=lambda c: (len([P for P in by_cell[c] if P <= free]), sorted(c)))
        best = 10 ** 9
        for P in by_cell[c]:
            if P <= free:
                best = min(best, 1 + rec(free - P))
        return best
    m = rec(R)
    rec.cache_clear()
    return m


def is_up(c):
    js = sorted(v[1] for v in c)
    return js[0] == js[1]


def board(band, page, ncells=None, k=0, min_lw=1.5):
    bs = [o for o in stroked_boards(band, page, min_lw=min_lw)]
    if ncells is not None:
        bs = [o for o in bs if len(o.R) == ncells]
    return bs[k]


# ---------------------------------------------------------------- 1. tiling counts
log('1. One-colour tiling counts, recomputed with separately generated pieces and a different search order')
cases = [
    ('K-1 P1 2x triangle, greens', 'k-1', 1, 4, 'green', 1),
    ('K-1 P1 2x rhombus, blues', 'k-1', 1, 8, 'blue', 1),
    ('K-1 P1 2x hexagon, yellows', 'k-1', 1, 24, 'yellow', 0),
    ('K-1 P1 2x trapezoid, reds', 'k-1', 1, 12, 'red', 1),
    ('K-1 P5 arrow, reds', 'k-1', 5, 12, 'red', 3),
    ('K-1 P5 arrow, blues', 'k-1', 5, 12, 'blue', 1),
    ('K-1 P5 trapezoid, reds', 'k-1', 5, 15, 'red', 5),
    ('K-1 P5 trapezoid, blues', 'k-1', 5, 15, 'blue', 0),
    ('K-1 P5 hexagon 2,1,2, reds', 'k-1', 5, 16, 'red', 0),
    ('K-1 P5 hexagon 2,1,2, blues', 'k-1', 5, 16, 'blue', 6),
    ('K-1 P7 hexagon, reds', 'k-1', 7, 6, 'red', 3),
    ('K-1 P7 hexagon, blues', 'k-1', 7, 6, 'blue', 2),
    ('2-3 P4 triangle 3, reds', 'grades-2-3', 4, 9, 'red', 2),
    ('2-3 P3/P4 hexagon 2,2,2, reds', 'grades-2-3', 3, 24, 'red', 9),
    ('2-3 P7 triangle 6, reds', 'grades-2-3', 7, 36, 'red', 220),
    ('4-5 P4 hexagon 2,2,2, blues', 'grades-4-5', 4, 24, 'blue', 20),
    ('4-5 P6 hexagon 1,3,3, blues', 'grades-4-5', 6, 30, 'blue', 20),
    ('4-5 P7 hexagon 2,2,2, reds', 'grades-4-5', 4, 24, 'red', 9),
]
for name, band, pg, n, kind, expect in cases:
    if name.startswith('K-1 P1'):
        o = [b for b in stroked_boards(band, pg, min_lw=1.5) if len(b.R) == n][0]
    else:
        o = board(band, pg, n)
    c = count_cover(o.R, placements(kind, o.R))
    log(f'  {name}: {c} (other scripts and the guide: {expect}) {"ok" if c == expect else "MISMATCH"}')

# 3x Upscale pieces, as lattice shapes with 3 small edges per side
log('  3x pieces modelled as lattice shapes with 3 small edges per side:')
tri3x = frozenset(c for i in range(3) for j in range(3 - i) for c in ([up(i, j)] + ([dn(i, j)] if i + j < 2 else [])))
rh3x = frozenset(c for i in range(3) for j in range(3) for c in (up(i, j), dn(i, j)))
trap3x = frozenset(c for i in range(6) for j in range(3) if i + j < 6 for c in ([up(i, j)] + ([dn(i, j)] if i + j < 5 else [])))
hex3x = frozenset(c for i in range(-3, 4) for j in range(-3, 4) for c in (up(i, j), dn(i, j))
                  if all(max(abs(x), abs(y), abs(x + y)) <= 3 for x, y in c))
for name, R, kind, area in (('3x triangle', tri3x, 'green', 9), ('3x rhombus', rh3x, 'blue', 18),
                            ('3x trapezoid', trap3x, 'red', 27), ('3x hexagon', hex3x, 'yellow', 54)):
    c = count_cover(R, placements(kind, R))
    log(f'  {name}: {len(R)} cells (expected {area}); tilings by its own colour: {c}'
        + (f', {len(R) // len(BASE[kind])} pieces each' if c else ' (X)'))

# ---------------------------------------------------------------- 2. games by plain search
log('\n2. Placement game by plain win/lose search (no Grundy values, no symmetry)')


def plain_game(R, limit_s=240):
    cells = sorted(R, key=sorted)
    idx = {c: k for k, c in enumerate(cells)}
    moves = []
    for a, b in combinations(cells, 2):
        if len(a & b) == 2:
            moves.append((1 << idx[a]) | (1 << idx[b]))
    memo = {}
    t0 = time.time()

    def win(free):
        v = memo.get(free)
        if v is not None:
            return v
        if time.time() - t0 > limit_s:
            raise TimeoutError
        r = False
        for m in moves:
            if free & m == m and not win(free & ~m):
                r = True
                break
        memo[free] = r
        return r
    full = (1 << len(cells)) - 1
    good = [m for m in moves if not win(full & ~m)]
    return ('1st' if good else '2nd'), len(good), len(moves), len(memo), time.time() - t0


sys.setrecursionlimit(10000)
games = [
    ('K-1 P2 hexagon 1,1,1', 'k-1', 2, 6, 0, ('2nd', 0)),
    ('K-1 P2 2-by-2', 'k-1', 2, 8, 0, ('2nd', 0)),
    ('K-1 P2 3-by-1 strip', 'k-1', 2, 6, 1, ('1st', 1)),
    ('K-1 P4 3-by-2', 'k-1', 4, 12, 0, ('1st', 1)),
    ('K-1 P4 triangle 3', 'k-1', 4, 9, 0, ('1st', 9)),
    ('K-1 P4 4-by-2', 'k-1', 4, 16, 0, ('2nd', 0)),
    ('2-3 P1 hexagon 1,1,2', 'grades-2-3', 1, 10, 0, ('1st', 1)),
    ('2-3 P1 3-by-2', 'grades-2-3', 1, 12, 0, ('1st', 1)),
    ('2-3 P2 triangle 4', 'grades-2-3', 2, 16, 0, ('2nd', 0)),
    ('2-3 P5 3-by-3', 'grades-2-3', 5, 18, 0, ('1st', None)),
    ('4-5 P9 5-by-2', 'grades-4-5', 9, 20, 0, ('1st', None)),
    ('4-5 P9 hexagon 1,2,3', 'grades-4-5', 9, 22, 0, ('1st', 1)),
    ('2-3 P5 hexagon 2,2,2', 'grades-2-3', 5, 24, 0, ('2nd', 0)),
]
for name, band, pg, n, k, (ew, eg) in games:
    lw = 0.5 if band == 'grades-4-5' and pg == 9 else 1.5
    os_ = [b for b in stroked_boards(band, pg, min_lw=lw) if len(b.R) == n]
    o = os_[k]
    try:
        w, g, nm, mem, t = plain_game(o.R)
        ok = (w == ew) and (eg is None or g == eg)
        log(f'  {name}: winner {w}, {g} winning first moves of {nm} ({mem} positions, {t:.1f} s) {"ok" if ok else "MISMATCH"}')
    except TimeoutError:
        log(f'  {name}: plain search stopped at the 240 s bound (not finished)')

# ---------------------------------------------------------------- 3. yellow packings by brute force
log('\n3. Most yellows that fit, by brute force over hexagon centres')


def centres(R):
    R = frozenset(R)
    out = []
    for P in placements('yellow', R):
        common = frozenset.intersection(*P)
        out.append((next(iter(common)), P))
    return out


def max_yellows(R):
    C = centres(R)
    best, sets = 0, []
    n = len(C)
    for r in range(n, 0, -1):
        found = []
        for S in combinations(range(n), r):
            cells = [C[i][1] for i in S]
            if sum(len(x) for x in cells) == len(frozenset().union(*cells)):
                found.append([C[i][1] for i in S])
        if found:
            return r, found, len(C)
    return 0, [], len(C)


def comps(cells):
    cells = set(cells)
    out = []
    while cells:
        st = [cells.pop()]
        comp = set(st)
        while st:
            x = st.pop()
            for y in list(cells):
                if len(x & y) == 2:
                    cells.discard(y)
                    comp.add(y)
                    st.append(y)
        out.append(len(comp))
    return sorted(out)


for name, band, pg, n in (('K-1 P1/P6 hexagon 2,2,2', 'k-1', 6, 24), ('2-3 P3 triangle 4', 'grades-2-3', 3, 16),
                          ('2-3 P6 hexagon 3,3,3', 'grades-2-3', 6, 54)):
    o = board(band, pg, n)
    m, found, nc = max_yellows(o.R)
    log(f'  {name}: {nc} possible yellow positions; at most {m} fit, in {len(found)} ways; leftover pieces per way: '
        f'{[comps(o.R - frozenset().union(*f)) for f in found]}')
m, found, nc = max_yellows(hex3x)
log(f'  3x Upscale hexagon (modelled): at most {m} small yellows fit, in {len(found)} ways')

# ---------------------------------------------------------------- 4. fewest pieces
log('\n4. Fewest pieces (green, blue, red, yellow), recomputed')
KINDS = ('green', 'blue', 'red', 'yellow')
for name, band, pg, n, expect in (('K-1 P3 triangle 3', 'k-1', 3, 9, 3), ('K-1 P3 star', 'k-1', 3, 12, 6),
                                  ('K-1 P6 boat', 'k-1', 6, 16, 5), ('K-1 P6 hexagon 2,2,2', 'k-1', 6, 24, 6),
                                  ('2-3 P3 triangle 4', 'grades-2-3', 3, 16, 5)):
    o = board(band, pg, n)
    pcs = [P for k in KINDS for P in placements(k, o.R)]
    m = min_cover(o.R, pcs)
    pcs_p = pcs + placements('purple', o.R)
    mp = min_cover(o.R, pcs_p)
    log(f'  {name}: fewest {m} (expected {expect}) {"ok" if m == expect else "MISMATCH"}; with purple chevrons allowed: {mp}')

# 3x hexagon from the yellow argument
o = board('grades-2-3', 6, 54)
C = centres(o.R)
reds = placements('red', o.R)
log('  2-3 P6 / 4-5 P10 hexagon 3,3,3 (54 cells): with h yellows, every other piece covers at most 3 cells, '
    'so at least h + ceil((54 - 6h)/3) = 18 - h pieces: ' + str([(h, h + -(-(54 - 6 * h) // 3)) for h in range(8)]))
# 12 pieces needs h >= 6; h = 7 is the most (section 3).  Count 12-piece fillings: 6 yellows + 6 reds.
n12 = 0
n6sets = 0
for S in combinations(range(len(C)), 6):
    cells = [C[i][1] for i in S]
    U = frozenset().union(*cells)
    if len(U) != 36:
        continue
    n6sets += 1
    rest = o.R - U
    cnt = count_cover(rest, [P for P in reds if P <= rest])
    n12 += cnt
log(f'  6 non-overlapping yellows: {n6sets} placements; 12-piece fillings (6 yellows + 6 reds): {n12}')
m7, found7, _ = max_yellows(o.R)
for f in found7:
    rest = o.R - frozenset().union(*f)
    pcs = [P for k in KINDS for P in placements(k, rest)]
    log(f'  a placement of {m7} yellows: the rest needs {min_cover(rest, pcs)} more pieces, total {m7 + min_cover(rest, pcs)}')

# ---------------------------------------------------------------- 5. two-down trapezoids by middle cell
log('\n5. Two-up / two-down trapezoids: a trapezoid is two-down exactly when its middle cell points up')


def two_down_counts(R, frame):
    Ts = all_covers(R, placements('red', R))
    out = Counter()
    for T in Ts:
        k = 0
        for P in T:
            mid = [c for c in P if sum(1 for d in P if len(c & d) == 2) == 2][0]
            ys = sorted(frame.to_page(v)[1] for v in mid)
            page_up = abs(ys[0] - ys[1]) < 1e-6
            k += page_up
        out[(len(T) - k, k)] += 1
    return out


for name, band, pg, n in (('2-3 P4 triangle 3', 'grades-2-3', 4, 9), ('2-3 P3/P4 hexagon 2,2,2', 'grades-2-3', 3, 24),
                          ('2-3 P7 triangle 6', 'grades-2-3', 7, 36)):
    o = board(band, pg, n)
    log(f'  {name}: (two-up, two-down) -> number of fillings: {dict(two_down_counts(o.R, o.frame))}')

# ---------------------------------------------------------------- 6. what the purple chevron would change
log('\n6. Guide p. 2: "Take the purple ... pieces off all tables ... they change the fewest-piece answers"')
log('  (see the "with purple chevrons allowed" figures in section 4)')

# ---------------------------------------------------------------- 7. shades of the 1,3,3 hexagon from rhombus directions
log('\n7. Rhombus directions (light = tops) on the 4-5 boards')
# In the drawn A picture (4-5 page 4), find the direction of the shared edge of the light rhombi.
groups = cluster(drawn_pieces('grades-4-5', 4))
light_dirs = Counter()
for g in groups:
    t = tiling_from_pieces(g)
    for P in t['tiling']:
        a, b = list(P)
        e = sorted(a & b)
        p, q = t['frame'].to_page(e[0]), t['frame'].to_page(e[1])
        ang = round((__import__('math').degrees(__import__('math').atan2(q[1] - p[1], q[0] - p[0]))) % 180)
        light_dirs[(colour_name(t['colours'][P]), ang)] += 1
log(f'  page 4 pictures A and B: (shade, direction of the edge shared by the rhombus\'s two triangles) -> count: {dict(light_dirs)}')
o = board('grades-4-5', 6, 30)
dirs = Counter()
for T in all_covers(o.R, placements('blue', o.R)):
    d = Counter()
    for P in T:
        a, b = list(P)
        e = sorted(a & b)
        p, q = o.frame.to_page(e[0]), o.frame.to_page(e[1])
        ang = round((__import__('math').degrees(__import__('math').atan2(q[1] - p[1], q[0] - p[0]))) % 180)
        d[ang] += 1
    dirs[tuple(sorted(d.items()))] += 1
log(f'  4-5 P6 hexagon (sides in order {[round(s) for s in o.sides]}): rhombi by shared-edge direction, over all fillings: {dict(dirs)}')
# which sides meet at the lowest corner of the page outline
P = o.page_poly
low = min(range(len(P)), key=lambda k: (P[k][1], P[k][0]))
from math import hypot
s1 = hypot(P[low][0] - P[low - 1][0], P[low][1] - P[low - 1][1]) / o.unit
s2 = hypot(P[(low + 1) % len(P)][0] - P[low][0], P[(low + 1) % len(P)][1] - P[low][1]) / o.unit
log(f'  sides meeting at the bottom corner of the page outline: {round(s1)} and {round(s2)} (floor {round(s1) * round(s2)} squares)')

# ---------------------------------------------------------------- 8. piles counted by the guide's P4 wording
log('\n8. Guide p. 6, 4-5 P4: "20 fillings, one for each pile in a 2 by 2 by 2 box with no overhangs"')
from itertools import product as _product
cols = list(_product(range(3), repeat=4))          # heights of back, left, right, front stacks, 0..2 each
pushed = [h for h in cols if h[0] >= h[1] and h[0] >= h[2] and h[1] >= h[3] and h[2] >= h[3]]
log(f'  stacks of 0-2 cubes standing on the floor (no overhangs): {len(cols)}; of these, pushed into the corner '
    f'(no stack taller than the one behind it toward either wall): {len(pushed)}')

# ---------------------------------------------------------------- 9. longest games (materials table)
log('\n9. Guide p. 1 materials: blues needed for a game')
for name, band, pg, n in (('hexagon 2,2,2 (4-5 P2)', 'grades-4-5', 2, 24), ('3-by-3 (4-5 P2)', 'grades-4-5', 2, 18),
                          ('hexagon 1,3,3 (4-5 P6, "when attention runs out")', 'grades-4-5', 6, 30)):
    o = board(band, pg, n)
    t = count_cover(o.R, placements('blue', o.R))
    log(f'  {name}: {len(o.R)} cells; blue fillings {t}, so a game can last {len(o.R) // 2 if t else "fewer than " + str(len(o.R) // 2)} moves')

log.save()
