"""Independent reviewer check: strip (K-1 P4, 2-3 P3, 4-5 P3), X Y Z exact halves (4-5 P4),
marking game in all six orders (2-3 P5/P6, 4-5 P5/P6), card row (4-5 P7), two reds (4-5 P8).
Exact rational arithmetic throughout. Cut searches use a 0.5 mm grid in exact fractions plus
the algebraic uniqueness arguments printed alongside."""
from fractions import Fraction as F
from itertools import combinations, product, permutations

# ---------- piecewise-uniform rows ----------
def make_row(segs):
    """segs: list of (length, {person: value of whole segment})"""
    out = []; x = F(0)
    for L, vals in segs:
        out.append((x, x + L, vals)); x += L
    return out

def val(row, person, a, b):
    s = F(0)
    for (x0, x1, vals) in row:
        lo, hi = max(a, x0), min(b, x1)
        if hi > lo:
            s += vals.get(person, 0) * (hi - lo) / (x1 - x0)
    return s

def exact_shares(row, people, cuts):
    L = row[-1][1]
    pts = [F(0)] + sorted(cuts) + [L]
    pieces = [(pts[i], pts[i+1]) for i in range(len(pts)-1)]
    sols = []
    for assign in product([0, 1], repeat=len(pieces)):
        if assign[0]:
            continue
        good = True
        for p in people:
            t0 = sum(val(row, p, a, b) for (a, b), s in zip(pieces, assign) if s == 0)
            tot = val(row, p, F(0), L)
            if t0 * 2 != tot:
                good = False; break
        if good:
            sols.append(assign)
    return sols

def search(row, people, k, step=F(1, 2)):
    L = row[-1][1]
    grid = [step * i for i in range(1, int(L / step))]
    found = []
    for cuts in combinations(grid, k):
        s = exact_shares(row, people, list(cuts))
        if s:
            found.append((cuts, s))
    return found

# Strip: red 0-120, blue 120-240. A (3,1), B (1,3); colour-only "people" for K-1: R-amount, B-amount.
strip = make_row([(F(120), {'A': 3, 'B': 1, 'red': 1}), (F(120), {'A': 1, 'B': 3, 'blue': 1})])
for people, label in [(['A', 'B'], '2-3/4-5 P3 (cards A and B)'), (['red', 'blue'], 'K-1 P4 (same red, same blue)')]:
    one = search(strip, people, 1)
    two = search(strip, people, 2)
    print(f'== Strip {label}: one-cut solutions {[(tuple(map(float,c)),s) for c,s in one]}; '
          f'two-cut solutions {[(tuple(map(float,c)),s) for c,s in two]}')
for p in 'AB':
    print(f'   one-cut exact point for {p} alone:', [float(c[0]) for c, s in search(strip, [p], 1)])
print('   middle piece 60-180 value to A, B:', val(strip, 'A', F(60), F(180)), val(strip, 'B', F(60), F(180)))
# Any other uniform-per-colour card (a, b): the 60/180 split gives half to everyone
ok = all(2 * (F(a) * F(60, 120) + F(b) * F(60, 120)) == a + b for a in range(0, 10) for b in range(0, 10))
print('   60/180 exact for every card (a,b) with 0<=a,b<=9:', ok)

# X Y Z: three-person cards
cards = {'A': {'X': 4, 'Y': 8, 'Z': 0}, 'B': {'X': 0, 'Y': 4, 'Z': 8}, 'C': {'X': 8, 'Y': 0, 'Z': 4}}
def xyz_row(order):
    return make_row([(F(50), {p: cards[p][pan] for p in cards}) for pan in order])
row = xyz_row('XYZ')
for k in (1, 2):
    print(f'== XYZ exact halves with {k} cut(s), 0.5 mm grid:', len(search(row, list('ABC'), k)), 'solutions')
three = search(row, list('ABC'), 3, step=F(5, 2))  # 2.5 mm grid suffices to show the answer; uniqueness is algebraic
print('   3 cuts (2.5 mm grid):', [(tuple(map(float, c)), s) for c, s in three])
# algebra: 4x+8y=6, 4y+8z=6, 8x+4z=6
import itertools
M = [[4, 8, 0], [0, 4, 8], [8, 0, 4]]
det = (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0]) + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
print('   determinant', det, '; x=y=z=1/2 satisfies:', all(sum(F(M[i][j], 1) * F(1, 2) for j in range(3)) == 6 for i in range(3)))
# guide's reduced equations x+2y=3/2, y+2z=3/2, 2x+z=3/2 are the card equations divided by 4
print('   guide equations equal card equations /4:', [[c / 4 for c in r] for r in M] == [[1, 2, 0], [0, 1, 2], [2, 0, 1]])

# ---------- marking game ----------
def mark(row, p, start, target):
    """leftmost point m >= start with val(start, m) >= target (first becomes worth target)."""
    acc = F(0)
    for (x0, x1, vals) in row:
        if x1 <= start:
            continue
        a = max(start, x0)
        v = vals.get(p, 0) * (x1 - a) / (x1 - x0)
        if acc + v >= target:
            if vals.get(p, 0) == 0:
                return a
            need = target - acc
            return a + need * (x1 - x0) / vals[p]
        acc += v
    return x1

def game(order):
    row = xyz_row(order)
    remaining = ['A', 'B', 'C']; start = F(0); pieces = {}; log = []
    for rnd in range(2):
        marks = {p: mark(row, p, start, F(4)) for p in remaining}
        m = min(marks.values())
        takers = [p for p in remaining if marks[p] == m]
        tie = len(takers) > 1
        t = takers[0]
        pieces[t] = (start, m)
        log.append((dict(marks), t, m, tie))
        remaining.remove(t); start = m
    pieces[remaining[0]] = (start, F(150))
    view = {o: tuple(val(row, o, *pieces[q]) for q in 'ABC') for o in 'ABC'}
    envy = [f'{o} to {q}' for o in 'ABC' for q in 'ABC' if q != o and view[o]['ABC'.index(q)] > view[o]['ABC'.index(o)]]
    return log, pieces, view, envy

fmt = lambda x: f'{float(x):g}'
for order in ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']:
    log, pieces, view, envy = game(order)
    r1, r2 = log
    print(f'== {order}: round1 marks A,B,C = {", ".join(fmt(r1[0][p]) for p in "ABC")}; {r1[1]} takes at {fmt(r1[2])} tie={r1[3]}; '
          f'round2 marks ' + ', '.join(f'{p}: {fmt(v)}' for p, v in r2[0].items()) + f'; {r2[1]} takes at {fmt(r2[2])} tie={r2[3]}')
    print('     pieces', {p: (fmt(a), fmt(b)) for p, (a, b) in pieces.items()},
          '| A sees', [fmt(v) for v in view['A']], 'B sees', [fmt(v) for v in view['B']], 'C sees', [fmt(v) for v in view['C']], '| envy', envy)

# whole-panel A:Y, B:Z, C:X
print('== whole panels A:Y B:Z C:X own values', cards['A']['Y'], cards['B']['Z'], cards['C']['X'])

# ---------- 4-5 P7: card row with card A (red 3, blue 1), value spread evenly across each 25 mm card ----------
vals = {'R': 3, 'B': 1}
def half_point(seq):
    tot = sum(vals[c] for c in seq); half = F(tot, 2); acc = F(0)
    for i, c in enumerate(seq):
        if acc + vals[c] >= half:
            frac = (half - acc) / vals[c]
            return i, c, frac, 25 * i + 25 * frac
        acc += vals[c]
i, c, frac, x = half_point('RBRBR')
print('== P7 printed R1 B1 R3 B2 R2: half point in card', i + 1, c, 'fraction', frac, 'at', float(x), 'mm')
res = set()
for perm in permutations(['R1', 'R2', 'R3', 'B1', 'B2']):
    seq = ''.join(p[0] for p in perm)
    i, c, frac, x = half_point(seq)
    res.add((c, 0 < frac < 1))
print('   all 120 orders: (card colour at half point, strictly inside):', res)

# ---------- 4-5 P8: three U-people, two reds of value 1 each, 25 mm each ----------
row2 = make_row([(F(25), {p: 1 for p in 'UVW'}), (F(25), {p: 1 for p in 'UVW'})])
s = F(0); rem = ['U', 'V', 'W']; cuts = []
for rnd in range(2):
    ms = {p: mark(row2, p, s, F(2, 3)) for p in rem}
    m = min(ms.values()); t = [p for p in rem if ms[p] == m][0]
    cuts.append(m); rem.remove(t); s = m
print('== P8 marking cuts at', [str(c) for c in cuts], 'mm (tie in each round, all equal)')
# only one card cut: one card whole to someone; best the other two can do is share one card
print('   one card cut: the two without the whole card share value 1, need 2/3 each =', F(4, 3), '> 1 -> impossible')
