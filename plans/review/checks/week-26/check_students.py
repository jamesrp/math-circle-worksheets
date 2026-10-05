"""Independent check of every student problem in the three Week 26 bands.

Uses the shapes and grids read from the delivered PDFs by extract.py and my own
exhaustive enumeration of fixed polyominoes (Redelmeier) up to 12 cells, plus
exhaustive bounding-box searches where larger shapes matter.
Output: check_students.out
"""
import json
import math
import os
import subprocess
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, Log, perimeter, shared, connected, rows_cols, bbox,  # noqa: E402
                    intervals, has_block, longest_run, holes, canon, show,
                    neighbors_empty, redelmeier, box_subsets, from_rows,
                    load_extracted)

L = Log()
if not os.path.exists(os.path.join(HERE, 'extracted.json')):
    subprocess.run([sys.executable, os.path.join(HERE, 'extract.py')], check=True)
X = load_extracted(os.path.join(HERE, 'extracted.json'))

# ------------------------------------------------------------------ census
NMAX = 12
per_by_n = defaultdict(set)          # n -> perimeters of fixed shapes
free_by_np = defaultdict(set)        # (n, P) -> free classes (n <= 8)
min_fixed = defaultdict(dict)        # n -> {canon: cells} at minimal P (filled later)
change_min_n = {}                    # change -> least start size
lemma_ok = True
identity_ok = True
tree_hole4 = defaultdict(int)        # n -> trees with a side-only-complement hole
tree_hole8 = defaultdict(int)        # n -> trees with a corner-leak-proof hole
tree_block = 0
first_tree_hole = {}
store = defaultdict(list)            # n -> list of cells for n in (7, 10)


def cb(poly):
    global lemma_ok, identity_ok, tree_block
    n = len(poly)
    P = perimeter(poly)
    e = shared(poly)
    if P != 4 * n - 2 * e:
        identity_ok = False
    per_by_n[n].add(P)
    r, c = rows_cols(poly)
    if P < 2 * (r + c) or (P == 2 * (r + c)) != (intervals(poly) == r + c):
        lemma_ok = False
    if n <= 8:
        free_by_np[(n, P)].add(canon(poly))
    if n in (7, 10):
        store[n].append((P, tuple(poly)))
    if n <= 7:
        for t in neighbors_empty(poly):
            ch = perimeter(list(poly) + [t]) - P
            if ch not in change_min_n or n < change_min_n[ch]:
                change_min_n[ch] = n
    if e == n - 1:
        if has_block(poly):
            tree_block += 1
        if n >= 7:
            h4 = holes(poly)
            if h4:
                tree_hole4[n] += 1
                first_tree_hole.setdefault(n, show(poly))
                if holes(poly, eight=True):
                    tree_hole8[n] += 1


redelmeier(NMAX, cb)
L.out(f'Census of fixed polyominoes n <= {NMAX} done.')
L.ok(identity_ok, 'P = 4n - 2e on every fixed polyomino (direct edge count)')
L.ok(lemma_ok, 'P >= 2(rows + columns), with equality iff every row and column is one run')
for n in range(1, NMAX + 1):
    ps = sorted(per_by_n[n])
    L.ok(min(ps) == 2 * math.ceil(2 * math.sqrt(n) - 1e-12) and max(ps) == 2 * n + 2
         and ps == list(range(min(ps), max(ps) + 1, 2)),
         f'n={n}: perimeters {ps} (min 2*ceil(2*sqrt n), max 2n+2, every even value between)')
L.ok(tree_block == 0, 'no tree (e = n - 1) contains a 2-by-2 block')
L.out('trees with a hole when diagonal contact seals (complement 4-connected):',
      dict(tree_hole4), 'first examples', first_tree_hole)
L.ok(sum(tree_hole8.values()) == 0,
     'no tree has a hole when holes must be sealed by sides (corner gaps leak), n <= 12')

# --------------------------------------------------------------- helpers

def page(band, p):
    return X[band][p - 1]


def free_count(n, P):
    return len(free_by_np[(n, P)])


def min_shapes_box(n):
    """Least perimeter for n tiles and the free shapes reaching it.  By the
    census lemma P >= 2(r + c), every shape with P <= 2s has a bounding box
    w-by-h with w + h <= s, so searching all such boxes is exhaustive."""
    s = 1
    while True:
        P = 2 * s
        found = set()
        for w in range(1, s):
            for h in range(1, s - w + 1):
                if w * h < n:
                    continue
                for comb in box_subsets(w, h, n):
                    if perimeter(comb) <= P:
                        found.add(canon(comb))
        if found:
            exact = {f for f in found if perimeter(f) == P}
            return P, found, exact
        s += 1


def span_box_perimeters(w, h):
    """Perimeters (by tile count) of every connected shape whose bounding box
    is exactly w-by-h, by bitmask search over all 2^(wh) subsets."""
    N = w * h
    full = (1 << N) - 1
    left = sum(1 << (y * w) for y in range(h))
    right = sum(1 << (y * w + w - 1) for y in range(h))
    rowm = [((1 << w) - 1) << (y * w) for y in range(h)]
    colm = [sum(1 << (y * w + x) for y in range(h)) for x in range(w)]
    out = defaultdict(set)
    for m in range(1, full + 1):
        if any(not (m & r) for r in rowm) or any(not (m & c) for c in colm):
            continue
        f = m & -m
        while True:
            g = f | ((f << 1) & ~left) | ((f >> 1) & ~right) | (f << w) | (f >> w)
            g &= m
            if g == f:
                break
            f = g
        if f != m:
            continue
        cells = [(i % w, i // w) for i in range(N) if m >> i & 1]
        out[len(cells)].add(perimeter(cells))
    return out


# ------------------------------------------------------------------- K-1
L.out('\n=== K-1')
tet = free_by_np[(4, 8)] | free_by_np[(4, 10)]
L.ok(len(tet) == 5 and free_count(4, 8) == 1 and free_count(4, 10) == 4,
     'P1: five tetrominoes; square P=8, other four P=10; 6 grids printed (one spare)')
L.ok(all(g['cols'] >= 4 and g['rows'] >= 4 for g in page('k1', 1)['grids'])
     and len(page('k1', 1)['grids']) == 6, 'P1: six 4x4 grids, every tetromino fits')
for n, pg in [(5, 2), (6, 2), (7, 3), (8, 3)]:
    ps = sorted(per_by_n[n])
    L.out(f'P{pg - 0}: n={n}: shortest {ps[0]} ({free_count(n, ps[0])} free shapes), '
          f'longest {ps[-1]} ({free_count(n, ps[-1])} free shapes)')
g2 = page('k1', 2)['grids']
g3 = page('k1', 3)['grids']
L.ok(all(g['cols'] >= 6 for g in g2) and all(g['cols'] >= 8 for g in g3),
     'P2/P3 grids hold a straight row of 6 (7 cols) and of 8 (8 cols)')
for P in (10, 12, 14):
    L.out(f'P4: six tiles, P={P}: {free_count(6, P)} free shapes')
L.ok(free_count(6, 10) == 1 and free_count(6, 12) >= 2 and free_count(6, 14) >= 2,
     'P4: only 12 and 14 can be made in two different ways (10 is the 2x3 only)')
L.ok(sorted(per_by_n[5]) == [10, 12], 'P5: with five tiles only 10 and 12 occur among 8..13')

starts = [s['cells'] for s in page('k1', 6)['shapes']]
L.out('P6 starts (from PDF):', [show(s) for s in starts], [perimeter(s) for s in starts])
best = []
for s in starts:
    S = set(map(tuple, s))
    res = []
    for src in S:
        rest = S - {src}
        for dst in neighbors_empty(rest):
            if dst == src:
                continue
            new = rest | {dst}
            if connected(new):
                res.append((perimeter(new), src, dst, canon(new)))
    m = min(r[0] for r in res)
    best.append(m)
    opt = [r for r in res if r[0] == m]
    L.out(f'  start {show(s)}: best after one move {m}, optimal (source, destination) moves {len(opt)},'
          f' optimal results {sorted({show(r[3]) for r in opt})}')
L.ok(best == [14, 10, 12], 'P6: best one-move boundaries 14, 10, 12; middle and bottom can shorten')
L.ok(all(g['cols'] >= 6 and g['rows'] >= 2 for g in page('k1', 6)['grids']),
     'P6: result grids (8x5) hold the 6-row and the 2x3 result')

# ------------------------------------------------------------- Grades 2-3
L.out('\n=== Grades 2-3')
L.ok(min(per_by_n[8]) == 12 and max(per_by_n[8]) == 18 and free_count(8, 12) == 2
     and free_count(8, 18) >= 2,
     f'P1: eight tiles: shortest 12 ({free_count(8, 12)} free shapes: '
     f'{[show(f) for f in free_by_np[(8, 12)]]}), longest 18 ({free_count(8, 18)} free shapes)')

starts2 = [s['cells'] for s in page('g23', 2)['shapes']]
want = [{2}, {0, 2}, {-2, 2}, {-4, 2}]
for s, w in zip(starts2, want):
    S = set(map(tuple, s))
    ch = {}
    for t in neighbors_empty(S):
        ch.setdefault(perimeter(S | {t}) - perimeter(S), []).append(t)
    L.ok(set(ch) == w, f'P2: {show(s)} before {perimeter(s)}: changes {sorted(ch)} '
         f'(cells per change {dict((k, len(v)) for k, v in ch.items())})')
L.ok(all(g['cols'] >= 4 and g['rows'] >= 4 for g in page('g23', 2)['grids']),
     'P2: two 6x4 recording grids per start; at most two changes per start')

ps10 = sorted(per_by_n[10])
L.ok(all(40 - 2 * e in ps10 for e in range(9, 14)),
     f'P3: ten tiles: e = 9..13 all possible (P range {ps10}); P = 40 - 2e gives 22, 20, 18, 16, 14')
L.ok(max(per_by_n[10]) == 22 and min(per_by_n[10]) == 14, 'P3: e cannot exceed 13 or go below 9 for 10 tiles')
L.ok([max(per_by_n[n]) for n in (4, 7, 10, 12)] == [10, 16, 22, 26],
     'P4: longest boundaries 10, 16, 22, 26 (grids 14 wide hold a 12-row)')

shapes5 = [s['cells'] for s in page('g23', 5)['shapes']]
L.out('P5 shapes (PDF reading order by row, then x):',
      [(show(s), len(s), perimeter(s), shared(s), longest_run(s)) for s in shapes5])
L.ok([perimeter(s) for s in shapes5] == [18, 18, 16, 12] and all(len(s) == 8 for s in shapes5),
     'P5: the row and the branch reach 18; the frame (16) and the 2x4 (12) do not')
long8 = [f for f in free_by_np[(8, 18)] if longest_run(f) <= 3]
L.ok(len(long8) >= 2, f'P5: {len(long8)} free 8-tile shapes with P=18 and no straight run of four')
fit = [f for f in long8 if min(bbox(f)) <= 5 and max(bbox(f)) <= 10]
L.ok(len(fit) >= 2, f'P5: {len(fit)} of them fit the 10x5 drawing grids')

L.ok(change_min_n == {2: 1, 0: 3, -2: 5, -4: 7},
     f'P6: least start sizes per change {change_min_n} (exhaustive over starts of <= 7 tiles)')

# ------------------------------------------------------------- Grades 4-5
L.out('\n=== Grades 4-5')
for n in (7, 10, 13):
    P, found, exact = min_shapes_box(n)
    fit = [f for f in exact if (bbox(f)[0] <= 7 and bbox(f)[1] <= 5) or (bbox(f)[1] <= 7 and bbox(f)[0] <= 5)]
    L.ok(len(exact) >= 2 and P == 2 * math.ceil(2 * math.sqrt(n)),
         f'P1: n={n}: least boundary {P}; {len(exact)} free shapes reach it; {len(fit)} fit a 7x5 grid')

L.ok(max(per_by_n[12]) == 26, 'P2: twelve tiles: longest boundary 26')
L.out('   (trees of 12 cells contain no 2x2 block; holes exist only if a diagonal contact seals: see census)')
hole12 = [(1, 0), (2, 0), (0, 1), (2, 1)] + [(x, 2) for x in range(8)]
L.ok(len(hole12) == 12 and connected(hole12) and perimeter(hole12) == 26 and holes(hole12) == 1
     and holes(hole12, eight=True) == 0,
     'P2: a 12-tile P=26 shape whose centre is enclosed only through a corner contact: '
     'hole if corners seal, no hole if corner gaps leak')

g3 = [s['cells'] for s in page('g45', 3)['shapes']]
for s in g3:
    r, c = rows_cols(s)
    L.out(f'P3 given {show(s)}: n={len(s)} rows {r} columns {c} boundary {perimeter(s)}')
L.ok([(rows_cols(s), perimeter(s)) for s in g3] == [((2, 6), 16), ((3, 4), 14), ((4, 5), 18)],
     'P3: (rows, columns, boundary) = (2,6,16), (3,4,14), (4,5,18)')
allP = span_box_perimeters(5, 4)
minP = min(min(v) for v in allP.values())
L.ok(minP == 18, f'P3: least boundary over every connected shape spanning exactly 4 rows and 5 columns = {minP}')
L.ok(len(allP[12]) >= 2, f'P3: twelve-tile 4x5-span shapes have boundaries {sorted(allP[12])}')

for P, want in [(12, 9), (14, 12), (16, 16), (18, 20)]:
    s_ = P // 2
    a, b = s_ // 2, (s_ + 1) // 2
    rect = [(x, y) for x in range(a) for y in range(b)]
    nxt = min_shapes_box(want + 1)[0]
    L.ok(a * b == want and perimeter(rect) == P and nxt > P,
         f'P4: boundary {P}: the {a}x{b} rectangle has {want} tiles and P={P}; '
         f'{want + 1} tiles need at least {nxt} (exhaustive box search)')
for n, want in [(12, 14), (13, 16), (17, 18), (20, 18), (21, 20)]:
    P, found, exact = min_shapes_box(n)
    L.ok(P == want and 2 * math.ceil(2 * math.sqrt(n)) == want,
         f'P5: n={n}: least boundary {P} (exhaustive box search; {len(exact)} free shapes reach it)')
ok6 = True
for P in range(4, 81, 2):
    s = P // 2
    if (s // 2) * ((s + 1) // 2) != max(r * (s - r) for r in range(1, s)) or (s // 2) * ((s + 1) // 2) != P * P // 16:
        ok6 = False
L.ok(ok6, 'P6: greatest area for even P >= 4 is floor(s/2)*ceil(s/2) = floor(P^2/16), s = P/2 (P <= 80)')
for n, want in [(37, 26), (50, 30), (73, 36)]:
    s = min(r + c for r in range(1, n + 1) for c in range(1, n + 1) if r * c >= n)
    L.ok(2 * s == want, f'P6: n={n}: least boundary {2 * s}')
L.ok(all(g['cols'] >= 9 and g['rows'] >= 9 for g in page('g45', 6)['grids']),
     'P6: 11x10 grids hold 6x6+1, 7x7+1 and 8x9+1 shapes')

# -------------------------------------------------------- page conventions
L.out('\n=== Diagrams')
sq = all(abs(g['cell_w_mm'] - g['cell_h_mm']) < 0.05 for b in ('k1', 'g23', 'g45') for p in X[b] for g in p['grids'])
sq2 = all(abs(s['cell_w_mm'] - s['cell_h_mm']) < 0.05 for b in ('k1', 'g23', 'g45') for p in X[b] for s in p['shapes'])
L.ok(sq and sq2, 'every working grid and printed tile is square')
for b in ('k1', 'g23', 'g45'):
    nums = [int(p['problem_lines'][0].split(':')[0].split()[1]) for p in X[b]]
    L.ok(nums == list(range(1, len(nums) + 1)), f'{b}: problems numbered {nums}, one per page')

L.save(os.path.join(HERE, 'check_students.out'))
