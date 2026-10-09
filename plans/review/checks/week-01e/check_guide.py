"""Adult guide (F01E-FAC-v1): every answer picture, read from the delivered PDF, checked
against the student boards; plus the guide's stated facts that need computation
(materials counts, MacMahon numbers, centre parity rule, fewest-piece bounds).
Writes check_guide.out."""
import os
import sys
from collections import Counter
from math import hypot, prod
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import *
from fastgame import Board

log = Log(os.path.join(HERE, 'check_guide.out'))
FAC = 'facilitator'
ALL = lambda R: greens(R) + blues(R) + reds(R) + yellows(R)

# student shapes, canonical up to lattice symmetry
STUDENT = {}
SHORT = {'hexagon sides [1, 1, 1, 1, 1, 1]': 'hex111', 'parallelogram 2x2 (sides in order [2, 2, 2, 2])': 'par2x2',
         'parallelogram 1x3 (sides in order [1, 3, 1, 3])': 'strip3x1', 'triangle side 3': 'tri3',
         'parallelogram 2x3 (sides in order [2, 3, 2, 3])': 'par3x2', 'parallelogram 2x4 (sides in order [2, 4, 2, 4])': 'par4x2',
         'trapezoid sides [3, 1, 3, 4] turns [120, 60, 60, 120]': 'trap41', 'hexagon sides [2, 1, 2, 2, 1, 2]': 'hex212',
         'hexagon sides [2, 2, 2, 2, 2, 2]': 'hex2', 'hexagon sides [2, 1, 1, 2, 1, 1]': 'hex112', 'triangle side 4': 'tri4',
         'parallelogram 3x3 (sides in order [3, 3, 3, 3])': 'par3x3', 'hexagon sides [3, 3, 3, 3, 3, 3]': 'hex3'}
for band, pg in [('k-1', 2), ('k-1', 3), ('k-1', 4), ('k-1', 5), ('k-1', 6), ('grades-2-3', 1), ('grades-2-3', 3),
                 ('grades-2-3', 5), ('grades-2-3', 6)]:
    for o in stroked_boards(band, pg, min_lw=1.5):
        cl = BD.classify(o)
        nm = SHORT.get(cl)
        if nm is None:
            nm = {12: 'star' if pg == 3 else 'arrow', 16: 'boat'}[len(o.R)]
        STUDENT.setdefault(nm, o.R)
CANON = {}
for nm, R in STUDENT.items():
    CANON.setdefault(canon(R), nm)


def which(R):
    return CANON.get(canon(R), '?')


W = PP.words(FAC)


def label_below(pg, t):
    pts = [t['frame'].to_page(v) for c in t['region'] for v in c]
    x0, x1 = min(p[0] for p in pts), max(p[0] for p in pts)
    bottom = min(p[1] for p in pts)
    cands = [w for w in W if w[0] == pg - 1 and bottom - 0.22 < w[4] < bottom + 0.02 and w[3] > x0 - 0.05 and w[1] < x1 + 0.05]
    cands.sort(key=lambda w: w[1])
    return ' '.join(w[5] for w in cands)


def mix(T):
    c = Counter(kind_of(p) for p in T)
    return ', '.join(f'{c[k]} {k}' for k in ('yellow', 'red', 'blue', 'green') if c[k])


def colour_ok(t):
    return all(colour_name(t['colours'][p]) == kind_of(p) for p in t['tiling'])


def board_outlines(pg):
    """Game boards in the guide: stroked closed outlines of lw ~0.7."""
    return [o for o in outlines(FAC, pg) if o.path['op'] == 'S' and 0.6 < o.lw < 0.8]


def game_picture(pg, t):
    """The blue piece t lies on a board outline: check it is the centre (self-symmetric) blue
    and a winning first move."""
    blue = next(iter(t['tiling']))
    cx, cy = t['centre']
    boards = [o for o in board_outlines(pg) if point_in_poly((cx, cy), o.page_poly)]
    if not boards:
        return 'no board found'
    o = boards[0]
    lp = [t['frame'].to_lat(q)[0] for q in o.page_poly]
    R = cells_in_lattice_polys([lp])
    ht = half_turn_centre(R)
    (si, sj), kind = ht
    selfimg = frozenset(frozenset((si - v[0], sj - v[1]) for v in c) for c in blue) == blue
    Bd = Board(R)
    w, good, moves = Bd.solve()
    goodcells = [Bd.move_cells(m) for m in good]
    return f'board {which(R)} ({describe(R)}): the blue is the centre blue: {selfimg}; it is a winning first move: {blue in goodcells}; winner {w}, {len(good)} winning first moves'


def report_page(pg):
    groups = cluster(drawn_pieces(FAC, pg))
    pics = []
    for g in groups:
        t = tiling_from_pieces(g)
        pics.append(t)
    return pics


# ------------------------------------------------------------------ page 3 (K-1 answers)
log('Guide page 3: K-1 answer pictures')
for t in report_page(3):
    lab = label_below(3, t)
    T = t['tiling']
    s = f'  "{lab}": {len(T)} pieces ({mix(T)}), colours match shapes: {colour_ok(t)}, disjoint: {t["disjoint"]}, snap {t["snap_err"]:.3f}'
    if len(T) == 1 and kind_of(next(iter(T))) == 'blue' and len(t['region']) == 2:
        s += '; ' + game_picture(3, t)
    else:
        nm = which(t['region'])
        s += f'; region = student shape {nm}'
        if nm != '?':
            R = t['region']
            kinds = {kind_of(p) for p in T}
            if len(kinds) == 1:
                k = kinds.pop()
                f = {'red': reds, 'blue': blues, 'green': greens, 'yellow': yellows}[k]
                s += f'; one-colour {k} tilings of this shape: {count_tilings(R, f(R))}'
            else:
                mn = fewest(R, ALL(R))[0]
                s += f'; fewest possible: {mn}'
    log(s)

# ------------------------------------------------------------------ page 6 (2-3 answers)
log('\nGuide page 6: grades 2-3 answer pictures')
for t in report_page(6):
    lab = label_below(6, t)
    T = t['tiling']
    s = f'  "{lab}": {len(T)} pieces ({mix(T)}), colours match: {colour_ok(t)}, disjoint: {t["disjoint"]}'
    if len(T) == 1 and kind_of(next(iter(T))) == 'blue':
        s += '; ' + game_picture(6, t)
    else:
        nm = which(t['region'])
        R = t['region']
        s += f'; region = student shape {nm}'
        kinds = {kind_of(p) for p in T}
        if kinds == {'red'}:
            s += f'; red tilings of this shape: {count_tilings(R, reds(R))}'
        else:
            s += f'; fewest possible: {fewest(R, ALL(R))[0]}'
    log(s)

def norm_pieces(t):
    """Pieces as sets of cell centroids in centred, unit-scaled page coordinates."""
    fr = t['frame']
    R = t['region']
    pts = [fr.to_page(v) for c in R for v in c]
    cx = (min(p[0] for p in pts) + max(p[0] for p in pts)) / 2
    cy = (min(p[1] for p in pts) + max(p[1] for p in pts)) / 2
    out = set()
    for p in t['tiling']:
        cs = []
        for c in p:
            q = [fr.to_page(v) for v in c]
            cs.append((round((sum(x for x, _ in q) / 3 - cx) / fr.unit, 3) + 0.0, round((sum(y for _, y in q) / 3 - cy) / fr.unit, 3) + 0.0))
        out.add(frozenset(cs))
    return frozenset(out)


def distinct_report(pg):
    pics = report_page(pg)
    groups = {}
    for t in pics:
        if len(t['tiling']) > 1:
            groups.setdefault((which(t['region']), tuple(sorted(Counter(kind_of(p) for p in t['tiling']).items()))), []).append(t)
    for k, ts in groups.items():
        if len(ts) > 1:
            keys = [norm_pieces(t) for t in ts]
            log(f'  page {pg}: {len(ts)} pictures of {k[0]} with {dict(k[1])}: all different as drawn: {len(set(keys)) == len(keys)}')


# ------------------------------------------------------------------ page 7 (4-5 trapezoid grid)
distinct_report(3)
distinct_report(6)
log('\nGuide page 7: the 9 red fillings (rows = rings, columns = cuts) and C, D')
pics = report_page(7)
pics = [t for t in pics if len(t['tiling']) == 8]
log(f'  pictures with 8 trapezoids: {len(pics)}; all valid and disjoint: {all(t["disjoint"] for t in pics)}; '
    f'snap {max(t["snap_err"] for t in pics):.3f}')


rows = {}
for t in pics:
    rows.setdefault(round(t['centre'][1], 1), []).append(t)
grid = [sorted(v, key=lambda t: t['centre'][0]) for k, v in sorted(rows.items(), reverse=True)]
G = [[norm_pieces(t) for t in row] for row in grid]
allp = [x for row in G for x in row]
log(f'  grid shape {[len(r) for r in grid]}; all 9 distinct: {len(set(allp)) == 9}')


def split(P):
    # the middle hexagon: centroids within distance 1 of the centre
    mid = frozenset(p for p in P if all(hypot(x, y) < 1.0 for x, y in p))
    return P - mid, mid


rings_by_row = [{split(P)[0] for P in row} for row in G]
mids_by_col = [{split(G[r][c])[1] for r in range(3)} for c in range(3)]
log(f'  each row has one ring: {[len(s) for s in rings_by_row]}; each column has one middle: {[len(s) for s in mids_by_col]}')


def is_frame(ring):
    # frame: every ring trapezoid touches the outer boundary along its long side, i.e. its three
    # cell centroids are as far out as possible on average
    far = [sum(hypot(x, y) for x, y in p) / 3 for p in ring]
    return round(min(far), 3), round(max(far), 3)


ring_rows = [next(iter(s)) for s in rings_by_row]


def mirror(ring):
    return frozenset(frozenset((-x + 0.0, y) for x, y in p) for p in ring)


log(f'  row 2 ring is mirror-symmetric (the frame): {mirror(ring_rows[1]) == ring_rows[1]}; '
    f'rows 1 and 3 are mirror images (two pinwheels): {mirror(ring_rows[0]) == ring_rows[2]}; '
    f'rows 1, 3 mirror-symmetric themselves: {mirror(ring_rows[0]) == ring_rows[0]}, {mirror(ring_rows[2]) == ring_rows[2]}')

# C and D from the 4-5 packet, page 8
groups = cluster(drawn_pieces('grades-4-5', 8))
CD = [tiling_from_pieces(g) for g in groups]
CD.sort(key=lambda t: t['centre'][0])
C, D = norm_pieces(CD[0]), norm_pieces(CD[1])
posC = [(r + 1, c + 1) for r in range(3) for c in range(3) if G[r][c] == C]
posD = [(r + 1, c + 1) for r in range(3) for c in range(3) if G[r][c] == D]
log(f'  student C is at (row, column) {posC}; D is at {posD}  (guide: C ring 3, D ring 2, both column 3)')

# ------------------------------------------------------------------ facts in the text
log('\nFacts stated in the guide text')
# MacMahon numbers


def macmahon(a, b, c):
    return prod(Fraction(i + j + k - 1, i + j + k - 2) for i in range(1, a + 1) for j in range(1, b + 1) for k in range(1, c + 1))


for abc in [(2, 2, 2), (1, 3, 3), (1, 2, 2)]:
    M, _ = model_pictures(*abc)
    log(f'  MacMahon {abc}: formula {macmahon(*abc)}, plane partitions counted {len(M)}, most cubes {max(v[1] for v in M.values())}')

# centre parity rule over many boards
bad = []
for a in range(1, 6):
    for b in range(1, 6):
        R = cells_in_lattice_polys([[(0, 0), (a, 0), (a, b), (0, b)]])  # a-by-b parallelogram
        R = cells_in_lattice_polys([[(0, 0), (a, 0), (a + 0, b), (0, b)]])
        ht = half_turn_centre(R)
        claim = 'vertex' if a % 2 == 0 and b % 2 == 0 else 'edge'
        if not ht or ht[1] != claim:
            bad.append(('par', a, b, ht))
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            P = [(0, 0)]
            for d, n in ((0, a), (1, b), (2, c), (3, a), (4, b), (5, c)):
                dx, dy = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)][d]
                P.append((P[-1][0] + dx * n, P[-1][1] + dy * n))
            R = cells_in_lattice_polys([P[:-1]])
            ht = half_turn_centre(R)
            claim = 'vertex' if (a % 2 == b % 2 == c % 2) else 'edge'
            if not ht or ht[1] != claim:
                bad.append(('hex', a, b, c, ht))
log(f'  centre rule ("grid point exactly when a, b both even" / "a, b, c all even or all odd"): counterexamples {bad}')

# fewest-piece bounds for the 3x hexagon: h + ceil((54-6h)/3) = 18 - h
log(f'  3x hexagon lower bounds h + ceil((54 - 6h)/3) for h = 0..7: {[h + -(-(54 - 6 * h) // 3) for h in range(8)]}')

# up/down counts
for n in range(1, 8):
    R = cells_in_lattice_polys([[(0, 0), (n, 0), (0, n)]])
    u = sum(is_up(c) for c in R)
    assert u == n * (n + 1) // 2 and len(R) - u == n * (n - 1) // 2
log('  triangle n: U = n(n+1)/2, D = n(n-1)/2 checked for n = 1..7')
for abc in [(1, 1, 1), (2, 2, 2), (1, 3, 3), (2, 1, 2), (1, 2, 3)]:
    a, b, c = abc
    P = [(0, 0)]
    for d, n in ((0, a), (1, b), (2, c), (3, a), (4, b), (5, c)):
        dx, dy = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)][d]
        P.append((P[-1][0] + dx * n, P[-1][1] + dy * n))
    R = cells_in_lattice_polys([P[:-1]])
    u = sum(is_up(c) for c in R)
    Ts = all_tilings(R, blues(R), limit=2000)
    types = Counter()
    if Ts:
        T = Ts[0]
        for p in T:
            # orientation class of a rhombus: direction of the shared edge
            c1, c2 = list(p)
            e = tuple(sorted(c1 & c2))
            d = (e[1][0] - e[0][0], e[1][1] - e[0][1])
            types[d] += 1
    log(f'  hexagon {abc}: U = {u}, D = {len(R) - u}; rhombus counts by orientation in one filling: {sorted(types.values())} '
        f'(ab, bc, ca = {sorted([a * b, b * c, c * a])})')

# materials: pieces needed by the largest single tasks
log('\nMaterials claims')
hex133 = stroked_boards('grades-4-5', 6, min_lw=1.5)[0].R
hex2 = STUDENT['hex2']
log(f'  blues in one filling of the 1,3,3 hexagon: {len(hex133) // 2}; reds in one filling of the 2x hexagon: {len(hex2) // 3}; '
    f'most moves in a game on the 2x hexagon: {len(hex2) // 2} (a full filling); on the 3-by-3 board: {len(STUDENT["par3x3"]) // 2}')
log.save()
