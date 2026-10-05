"""Independent mathematical check of the Week 16 base packet (three-colour
triangles / Sperner) and its adult guide.

Enumerates every legal filling of every printed board with this review's own
code (sperner16.py), recomputes every answer, count, witness and route, and
compares them with the numbers and row codes printed in the delivered adult
guide (text read with pdftotext).  The packet's own check scripts and JSON
are not used.
Run: python3 check_math.py   (writes out_check_math.txt beside itself)
"""
import collections
import itertools
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfgeom16 as G  # noqa: E402  (paths and pdftotext only)
from sperner16 import (lattice, fan2, row_code, from_code, legal,  # noqa: E402
                       door_components, random_triangulation, random_label)

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


GUIDE = G.text(G.PDF['guide'])
GUIDE_L = G.text(G.PDF['guide'], layout=True)
GFLAT = re.sub(r'\s+', ' ', GUIDE)


def in_guide(s):
    return re.sub(r'\s+', ' ', s) in GFLAT


def dist(b, **rules):
    d = collections.Counter()
    for lab in b.labelings(**rules):
        d[len(b.rainbow(lab))] += 1
    return dict(sorted(d.items()))


# =================================================================== statements
say('== Problem statements as printed (pdftotext), for reference')
for band in ('K-1', '2-3', '4-5'):
    paras = [re.sub(r'\s+', ' ', q).strip() for q in G.text(G.PDF[band]).split('\n\n')]
    probs = []
    for q in paras:
        m = re.search(r'Problem (\d+): (.*)', q)
        if m:
            probs.append((m.group(1), m.group(2)))
    nums = [int(n_) for n_ in re.findall(r'Problem (\d+):', G.text(G.PDF[band]))]
    uniq = []
    for n_, txt in probs:
        if not uniq or uniq[-1][0] != n_:
            uniq.append((n_, txt))
    check([int(n_) for n_, _ in uniq] == list(range(1, 7)), '%s: Problems 1-6 numbered consecutively (Problem 1 printed %d times)' % (band, nums.count(1)))
    for n_, txt in uniq:
        say('   %s P%s: %s' % (band, n_, txt))
say('')

# =================================================================== side 2
say('== K-1 Problem 1: side-2 board (4 cells)')
b2 = lattice(2)
labs2 = list(b2.labelings())
d2 = collections.Counter(len(b2.rainbow(l)) for l in labs2)
check(len(labs2) == 8 and d2 == {1: 8}, 'side 2: 8 legal fillings, every one has exactly one all-three cell: %s' % dict(d2))
sole2 = collections.defaultdict(list)
for l in labs2:
    r = b2.rainbow(l)
    sole2[r[0] + 1].append(row_code(2, l))
check(sorted(sole2) == [1, 2, 3, 4], 'each of the four cells is the sole all-three cell in some filling')
for k in sorted(sole2):
    say('   cell %d sole in: %s' % (k, ', '.join(sole2[k])))
check(in_guide('All eight legal two-step fillings have exactly one'), 'guide states the same ("All eight ... exactly one")')

# =================================================================== side 3
say('')
say('== Side-3 board: K-1 P2, P3; Grades 2-3 P1; Grades 4-5 P1')
b3 = lattice(3)
labs3 = list(b3.labelings())
d3 = collections.Counter(len(b3.rainbow(l)) for l in labs3)
say('   distribution of all-three counts over %d legal fillings: %s' % (len(labs3), dict(sorted(d3.items()))))
check(len(labs3) == 192 and dict(d3) == {1: 108, 3: 72, 5: 12}, 'guide: "108 legal fillings have 1, 72 have 3, and 12 have 5, among 192"')
check(in_guide('108 legal fillings have 1, 72 have 3, and 12 have 5, among 192 legal fillings'), 'that sentence is in the guide')
check(min(d3) == 1 and max(d3) == 5 and sorted(d3) == [1, 3, 5], 'K-1 P2: zero impossible; K-1 P3/2-3 P1/4-5 P1: min 1, max 5, attainable {1,3,5}')
for code, want in [('RRRB/RRB/RB/Y', [9]), ('RRRB/RRY/RB/Y', None), ('RBRB/RYB/RB/Y', [2, 3, 4, 7, 9])]:
    n, lab = from_code(code)
    got = [k + 1 for k in b3.rainbow(lab)]
    check(legal(b3, lab), 'witness %s is legal' % code)
    say('   %s -> all-three cells %s (count %d)' % (code, got, len(got)))
    if want:
        check(got == want, '%s gives cells %s' % (code, want))
n, lab = from_code('RRRB/RRY/RB/Y')
check(len(b3.rainbow(lab)) == 3, 'RRRB/RRY/RB/Y has exactly 3 (middle witness)')

# --- the guide's structural proof of "1, 3 or 5"
say('')
say('-- guide p.5 proof: rotate/rename so the centre is Y, then a formula')
sigma = {'R': 'B', 'B': 'Y', 'Y': 'R'}


def rot3(v):  # 120-degree rotation BL->BR->Top->BL on lattice coords of side 3
    i, j = v
    k = 3 - i - j
    return (k, i)  # barycentric (i along R->B, j along R->Y); rotate coordinates


# verify rot3 maps corners as intended
check(rot3((0, 0)) == (3, 0) and rot3((3, 0)) == (0, 3) and rot3((0, 3)) == (0, 0), 'rotation maps R corner->B corner->Y corner->R corner')
cellset = {frozenset(c) for c in b3.cells}
check({frozenset(rot3(v) for v in c) for c in b3.cells} == cellset, 'rotation maps cells to cells')
ok_rot = True
for lab in labs3:
    new = {rot3(v): sigma[l] for v, l in lab.items()}
    if not legal(b3, new) or len(b3.rainbow(new)) != len(b3.rainbow(lab)):
        ok_rot = False
check(ok_rot, 'rotate+rename (R->B->Y->R) maps legal fillings to legal fillings with the same count')
centre = (1, 1)
check({lab[centre] for lab in labs3} == set('RBY'), 'centre takes all three labels; rotating 1 or 2 times sends any centre label to Y')
L, M, V, U, A, D = (1, 0), (2, 0), (0, 2), (1, 2), (0, 1), (2, 1)
cells_num = {k + 1: c for k, c in enumerate(b3.cells)}
check(set(cells_num[6]) == {A, centre, V} and set(cells_num[8]) == {centre, D, U}, 'cells 6, 8 are the left/right middle-strip up cells')
check(set(cells_num[7]) == {V, U, centre} and set(cells_num[9]) == {V, U, (0, 3)}, 'cells 7, 9 are the two cells on edge V-U')
formula_ok = True
part_ok = True
for lab in labs3:
    if lab[centre] != 'Y':
        continue
    r = set(k + 1 for k in b3.rainbow(lab))
    f = (lab[L] != lab[M]) + (lab[L] == 'B') + (lab[M] == 'R') + 2 * (lab[V] == 'R' and lab[U] == 'B')
    if f != len(r):
        formula_ok = False
    if 6 in r or 8 in r:
        part_ok = False
    if (3 in r) != (lab[L] != lab[M]) or (len(r & {1, 2}) != (lab[L] == 'B')) or (len(r & {4, 5}) != (lab[M] == 'R')):
        part_ok = False
    if len(r & {7, 9}) != 2 * (lab[V] == 'R' and lab[U] == 'B'):
        part_ok = False
check(formula_ok and part_ok, 'with centre Y: count = [L!=M] + [L=B] + [M=R] + 2[V=R,U=B], and every group claim holds (64 fillings)')
table = {(l, m): (l != m) + (l == 'B') + (m == 'R') for l in 'RB' for m in 'RB'}
check(table == {('R', 'R'): 1, ('R', 'B'): 1, ('B', 'R'): 3, ('B', 'B'): 1}, 'bottom-contribution table RR 1, RB 1, BR 3, BB 1: %s' % table)

# =================================================================== fan board
say('')
say('== Fan board (K-1 P4 with printed letters; 2-3 P6 and 4-5 P5 free)')
fb = fan2()
check(len(fb.cells) == 12 and len(fb.xy) == 10, 'fan board: 10 vertices, 12 little cells')
check(len(fb.boundary_edges) == 6 and len(fb.interior_edges) == 15, 'edge-to-edge: 6 boundary + 15 interior edges, each interior edge in two cells')
dfan = dist(fb)
say('   free fan board distribution over %d fillings: %s' % (sum(dfan.values()), dfan))
check(min(dfan) >= 1 and all(k % 2 for k in dfan), '2-3 P6 / 4-5 P5: no legal filling of the fan board has zero; all counts odd')
fixed = {(0, 0): 'R', (1, 0): 'R', (2, 0): 'B', (0, 1): 'Y', (1, 1): 'B', (0, 2): 'Y'}
check(in_guide('bottom RRB, next row YB, top Y'), 'guide reads the K-1 P4 printed letters as bottom RRB, next row YB, top Y')
best = collections.defaultdict(list)
for lab in fb.labelings(fixed=fixed):
    best[len(fb.rainbow(lab))].append(tuple(lab[k] for k in ('lowerleft', 'central', 'lowerright', 'top')))
mx = max(best)
say('   K-1 P4 counts over the 81 centre choices: %s' % {k: len(v) for k, v in sorted(best.items())})
check(mx == 7, 'K-1 P4 maximum is 7')
check(sorted(best[7]) == sorted([('B', c, 'Y', 'R') for c in 'RBY']), 'exactly three maximum fillings: lower-left B, lower-right Y, top R, central any: %s' % best[7])
# per region maxima as in the guide's proof
for reg, want in [('lowerleft', 2), ('central', 1), ('lowerright', 2), ('top', 2)]:
    vals = {}
    for x in 'RBY':
        lab = dict(fixed)
        lab.update({k: 'R' for k in ('lowerleft', 'central', 'lowerright', 'top')})
        lab[reg] = x
        vals[x] = sum(1 for k in fb.rainbow(lab) if fb.region[fb.cells[k]] == reg)
    if reg == 'central':
        check(set(vals.values()) == {1}, 'central RBY region contributes exactly 1 for any centre: %s' % vals)
    else:
        check(max(vals.values()) == want and [x for x in vals if vals[x] == want] == [{'lowerleft': 'B', 'lowerright': 'Y', 'top': 'R'}[reg]],
              '%s region max %d, only with %s: %s' % (reg, want, {'lowerleft': 'B', 'lowerright': 'Y', 'top': 'R'}[reg], vals))

# =================================================================== side 4
say('')
say('== Side-4 board: K-1 P5, 2-3 P5, 4-5 P2, 4-5 P6')
b4 = lattice(4)
d4 = collections.Counter()
sole4 = collections.defaultdict(int)
for lab in b4.labelings():
    r = b4.rainbow(lab)
    d4[len(r)] += 1
    if len(r) == 1:
        sole4[r[0] + 1] += 1
say('   distribution over %d fillings: %s' % (sum(d4.values()), dict(sorted(d4.items()))))
check(dict(d4) == {1: 2920, 3: 6192, 5: 3840, 7: 848, 9: 24}, 'guide: 1,3,5,7,9 in 2,920; 6,192; 3,840; 848; 24')
check(in_guide('1,3,5,7,9 all-three cells in 2,920; 6,192; 3,840; 848; 24 fillings'), 'that sentence is in the guide')
check(sorted(sole4) == list(range(1, 17)), 'K-1 P5: each of the 16 cells is the only all-three cell in some filling')
say('   number of one-cell fillings per sole cell: %s' % dict(sorted(sole4.items())))
check(d4[3] > 0, '2-3 P5: fillings with exactly three exist (%d)' % d4[3])
# the guide table
tab = {}
for m in re.finditer(r'^\s*(\d+)\s+([RBY/]{19})\s+(\d+)\s+([RBY/]{19})\s*$', GUIDE_L, re.M):
    tab[int(m.group(1))] = m.group(2)
    tab[int(m.group(3))] = m.group(4)
check(sorted(tab) == list(range(1, 17)), 'read all 16 row codes from the guide table')
for k in sorted(tab):
    n, lab = from_code(tab[k])
    r = [x + 1 for x in b4.rainbow(lab)]
    check(n == 4 and legal(b4, lab) and r == [k], 'table cell %2d: %s legal, all-three cells %s' % (k, tab[k], r))
n, lab = from_code('RRRRB/RRRB/RRB/RB/Y')
check([x + 1 for x in b4.rainbow(lab)] == [16], 'example RRRRB/RRRB/RRB/RB/Y makes only cell 16 all-three')

# =================================================================== exceptions
say('')
say('== Boundary exceptions: K-1 P6 (whole bottom side may use Y) and 4-5 P6 (one starred dot)')
zeros6 = [l for l in b3.labelings(bottom='RBY') if not b3.rainbow(l)]
say('   K-1 P6: %d zero-cell fillings of the side-3 board when the bottom side allows R/B/Y' % len(zeros6))
check(len(zeros6) >= 4, 'K-1 P6: at least four zero-cell fillings exist')
codes6 = re.search(r'Their row codes, in the same order, are (.*?)\. Every corner', GFLAT).group(1).split('; ')
check(len(codes6) == 4 and len(set(codes6)) == 4, 'guide gives four distinct codes: %s' % codes6)
for c in codes6:
    n, lab = from_code(c)
    check(n == 3 and legal(b3, lab, bottom='RBY') and not b3.rainbow(lab) and c[:4] == 'RRYB',
          'K-1 P6 code %s: legal with the new bottom rule, zero all-three cells, bottom RRYB' % c)
bot_patterns = collections.Counter(row_code(3, l).split('/')[0] for l in zeros6)
say('   bottom rows among the zero fillings: %s' % dict(bot_patterns))
star = (2, 0)


zeros45 = []
total45 = 0
# enumerate with the star free: bottom rule for the star only is RBY
free = [v for v in b4.xy if v not in b4.corners.values()]
choices = [('RBY' if v == star else b4.allowed(v)) for v in free]
for combo in itertools.product(*choices):
    lab = {b4.corners[k]: k for k in 'RBY'}
    lab.update(zip(free, combo))
    total45 += 1
    if not b4.rainbow(lab):
        zeros45.append(lab)
check(len(zeros45) == 208, '4-5 P6: %d zero-cell fillings with the one-dot exception (guide: 208)' % len(zeros45))
check(all(l[star] == 'Y' for l in zeros45), 'every zero-cell filling puts Y on the starred dot')
n, lab = from_code('RRYBB/RRYB/RRY/RY/Y')
ok = n == 4 and lab[star] == 'Y' and all(lab[v] in b4.allowed(v) for v in b4.xy if v != star) and not b4.rainbow(lab)
check(ok, '4-5 P6 witness RRYBB/RRYB/RRY/RY/Y: only the star breaks the rule, zero all-three cells')

# =================================================================== routes
say('')
say('== Grades 2-3 Problem 2 (printed board)')


def describe(b, lab, comps):
    n = b.n
    seg = {frozenset(((i, 0), (i + 1, 0))): i + 1 for i in range(n)}
    out = []
    for c in comps:
        parts = []
        for node in c['walk']:
            if node[0] == 'cell':
                parts.append('c%d' % (node[1] + 1))
            else:
                parts.append('seg%d' % seg.get(node[1], 0))
        out.append((parts, c['loop'], c['doors']))
    return out


n, lab = from_code('RBRB/RRB/RB/Y')
check(legal(b3, lab), 'printed board RBRB/RRB/RB/Y obeys the side rules')
doors = b3.doors(lab)
bdoors = [e for e in doors if e in b3.boundary_edges]
check(len(doors) == 9 and len(bdoors) == 3 and all(all(v[1] == 0 for v in e) for e in bdoors), '9 doors, the 3 boundary doors are the 3 bottom edges')
check([k + 1 for k in b3.rainbow(lab)] == [9], 'cell 9 is the only all-three cell')
comps = describe(b3, lab, door_components(b3, lab))
for parts, loop, nd in comps:
    say('   component: %s  loop=%s doors=%d' % (' - '.join(parts), loop, nd))


def canon(walks):
    return {min(tuple(w), tuple(w[::-1])) for w in walks}


want = [['seg1', 'c1', 'c2', 'c3', 'seg2'], ['seg3', 'c5', 'c4', 'c8', 'c7', 'c9']]
check(canon(p for p, _, _ in comps) == canon(want) and not any(l for _, l, _ in comps),
      'routes: entrance 1 - cells 1,2,3 - entrance 2; entrance 3 - cells 5,4,8,7,9; no internal component')

say('')
say('== Grades 4-5 Problem 2 (printed board) and the 2-3 P5 key that reuses it')
n, lab = from_code('RRBRB/YBRB/RBB/RB/Y')
check(legal(b4, lab), 'printed board RRBRB/YBRB/RBB/RB/Y obeys the side rules')
doors = b4.doors(lab)
bdoors = sorted(e for e in doors if e in b4.boundary_edges)
segs = sorted(min(v[0] for v in e) + 1 for e in bdoors if all(v[1] == 0 for v in e))
check(len(doors) == 14, '14 doors (got %d)' % len(doors))
check(len(bdoors) == 3 and segs == [2, 3, 4], 'boundary doors are bottom segments 2,3,4 (got %s)' % segs)
rb = [k + 1 for k in b4.rainbow(lab)]
check(rb == [2, 8, 16], 'all-three cells 2, 8, 16 (got %s)' % rb)
comps = describe(b4, lab, door_components(b4, lab))
for parts, loop, nd in comps:
    say('   component: %s  loop=%s doors=%d' % (' - '.join(parts), loop, nd))
want = [['seg2', 'c3', 'c2'], ['seg3', 'c5', 'c4', 'c10', 'c11', 'c12', 'c6', 'c7', 'seg4'], ['c8', 'c9', 'c13', 'c14', 'c16']]
check(canon(p for p, _, _ in comps) == canon(want), 'three components exactly as the guide lists them')
check(sorted(nd for _, _, nd in comps) == [2, 4, 8] and not any(l for _, l, _ in comps), 'door counts 2, 8, 4 (total 14); no closed loop')
check(all('c1' not in p for p, _, _ in comps), 'cell 1 has no door')
check(len(b4.rainbow(lab)) == 3, '2-3 P5 key: this filling has exactly three all-three cells')

# =================================================================== local types
say('')
say('== Problem 3 (both older bands): one triangle, labels R/B/Y, turns and flips identified')
orbits = {}
for lab in itertools.product('RBY', repeat=3):
    key = ''.join(sorted(lab, key='RBY'.index))
    orbits.setdefault(key, set()).add(lab)
check(len(orbits) == 10, '10 classes (S3 acts on the three vertices, so classes = multisets)')
bydoors = collections.defaultdict(list)
for key in orbits:
    nd = sum(1 for a, b in itertools.combinations(key, 2) if {a, b} == {'R', 'B'})
    bydoors[nd].append(key)
say('   by door count: %s' % dict(bydoors))
check(sorted(bydoors[0]) == sorted(['RRR', 'BBB', 'YYY', 'RRY', 'RYY', 'BBY', 'BYY']) and bydoors[1] == ['RBY']
      and sorted(bydoors[2]) == sorted(['RRB', 'RBB']) and 3 not in bydoors, 'guide table: 0 doors 7 classes, 1 door RBY only, 2 doors RRB/RBB, never 3')

# =================================================================== rows
say('')
say('== Problem 4 rows')


def row_counts(ends, edges):
    out = set()
    for mid in itertools.product('RB', repeat=edges - 1):
        row = ends[0] + ''.join(mid) + ends[1]
        out.add(sum(1 for a, b in zip(row, row[1:]) if a != b))
    return sorted(out)


r23 = [row_counts('RB', e) for e in [2, 3, 4, 5, 6]]
check(r23 == [[1], [1, 3], [1, 3], [1, 3, 5], [1, 3, 5]], 'Grades 2-3 rows (2..6 edges): %s' % r23)
r45 = [row_counts(ends, e) for ends, e in zip(['RB', 'RR', 'RB', 'RR', 'RB'], [3, 4, 5, 6, 7])]
check(r45 == [[1, 3], [0, 2, 4], [1, 3, 5], [0, 2, 4, 6], [1, 3, 5, 7]], 'Grades 4-5 rows: %s' % r45)
for s, e in zip(['RRRB', 'RRRRR', 'RRRRRB', 'RRRRRRR', 'RRRRRRRB'], [3, 4, 5, 6, 7]):
    nd = sum(1 for a, b in zip(s, s[1:]) if a != b)
    check(len(s) == e + 1 and nd == min(row_counts(s[0] + s[-1], e)), 'sample %s has %d edges and the fewest doors (%d)' % (s, e, nd))
for n_ in range(1, 15):
    for ends in ('RB', 'RR', 'BB', 'BR'):
        cs = row_counts(ends, n_) if n_ <= 12 else None
        if cs:
            assert all(c % 2 == (ends[0] != ends[1]) for c in cs)
check(True, 'parity rule (odd iff the ends differ) holds for every row of 1..12 edges and all end pairs')

# =================================================================== general theorem
say('')
say('== The general statements in the guide overview and p.11, tested on random triangulations')
rng = random.Random(16)
n_tri = 0
odd_ok = incid_ok = path_ok = True
loops_seen = 0
exc_even = 0
for t in range(400):
    b = random_triangulation(rng, steps=rng.randint(5, 45))
    for _ in range(10):
        lab = random_label(b, rng)
        n_tri += 1
        T = len(b.rainbow(lab))
        doors = b.doors(lab)
        bd = sum(1 for e in doors if e in b.boundary_edges)
        idr = len(doors) - bd
        U = sum(1 for c in b.cells if sum(1 for e in itertools.combinations(c, 2) if {lab[v] for v in e} == {'R', 'B'}) == 2)
        if T % 2 != 1 or bd % 2 != 1:
            odd_ok = False
        if T + 2 * U != bd + 2 * idr:
            incid_ok = False
        comps = door_components(b, lab)
        mixed = 0
        for c in comps:
            if c['loop']:
                loops_seen += 1
                continue
            ends = [c['walk'][0], c['walk'][-1]]
            kinds = sorted(e[0] for e in ends)
            if kinds == ['cell', 'out']:
                mixed += 1
        if mixed % 2 != 1:
            path_ok = False
    # boundary exception: let bottom side use Y too, count even outcomes
    for _ in range(10):
        lab = random_label(b, rng, bottom='RBY')
        if len(b.rainbow(lab)) % 2 == 0:
            exc_even += 1
check(odd_ok, 'odd number of all-three cells and of boundary doors in %d random legal labelings of 400 random triangulations' % n_tri)
check(incid_ok, 'incidence identity T + 2U = b + 2I holds every time')
check(path_ok, 'odd number of paths joining an entrance to an all-three cell every time')
say('   closed door loops met in the random sample: %d (the overview allows them)' % loops_seen)
check(exc_even > 0, 'with Y allowed on the bottom side, even counts (including 0) occur: %d of 4000' % exc_even)

# =================================================================== preparation numbers
say('')
say('== Preparation arithmetic')
check(3 * 45 == 135 and 4 * 45 == 180 and 2 * 45 == 90, '3 sets x 45 = 135; 4 x 45 = 180; 2 x 45 = 90')
most = 0
for b, kw in [(lattice(2), {}), (lattice(3), {}), (lattice(4), {}), (lattice(3), {'bottom': 'RBY'})]:
    for lab in b.labelings(**kw):
        most = max(most, max(collections.Counter(lab.values()).values()))
fixed_fan = max(max(collections.Counter(l.values()).values()) for l in fb.labelings(fixed=fixed))
check(max(most, fixed_fan) <= 15, 'no K-1 board ever needs more than %d counters of one letter (15 provided)' % max(most, fixed_fan))
check(len(lattice(4).xy) == 15, 'largest K-1 board (side 4) has 15 vertices')

say('')
say('%d failures' % len(FAIL))
for f in FAIL:
    say('FAILED: ' + f)
open(os.path.join(HERE, 'out_check_math.txt'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
