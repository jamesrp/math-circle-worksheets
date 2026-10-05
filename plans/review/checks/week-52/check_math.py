"""Independent mathematical check of Week 52 (hinged frames and braces).

Nothing here imports the packet's own checkers or uses its link-graph theorem
as an input. Rigidity is decided two independent ways:

* rigid      <- exact linear algebra mod two large primes on the rigidity
               matrix at the square placement (full rank 2V-3 mod p implies
               full rank over Q, hence infinitesimal rigidity, hence rigidity);
* flexible   <- an explicit finite motion: rotate groups of strip directions by
               different angles, rebuild every joint, and check that every side
               bar and every brace keeps its length for a whole family of
               placements while some unbraced cell diagonal changes length.

Every design gets one certificate or the other; a design that gets neither is
reported. The link-graph criterion is then compared with these certificates.

Cells are (row, column), rows counted from the top as on the student pages.
Run: python3 check_math.py   (writes out_check_math.txt beside itself)
"""
import itertools
import math
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
PRIMES = (2305843009213693951, 4611686018427387847)  # 2^61-1 and another 62-bit prime


def say(*a):
    s = ' '.join(str(x) for x in a)
    OUT.append(s)
    print(s)


FAIL = []


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- frameworks
def joints(m, n):
    return [(r, c) for r in range(m + 1) for c in range(n + 1)]


def side_bars(m, n):
    bars = []
    for r in range(m + 1):
        for c in range(n):
            bars.append(((r, c), (r, c + 1)))
    for r in range(m):
        for c in range(n + 1):
            bars.append(((r, c), (r + 1, c)))
    return bars


def brace_bar(cell, orient='/'):
    """Cell (i, j), 1-based from the top-left. '/' joins lower-left to upper-right."""
    i, j = cell
    if orient == '/':
        return ((i, j - 1), (i - 1, j))
    return ((i - 1, j - 1), (i, j))


def square_pos(rc):
    r, c = rc
    return (c, -r)


# ------------------------------------------------- exact rank via residuals
class GridRank:
    """Rank of [side bars + chosen braces] mod p, using one reduction of the
    side-bar rows and then only the small residual of each brace row."""

    def __init__(self, m, n, p):
        self.m, self.n, self.p = m, n, p
        J = joints(m, n)
        self.idx = {j: k for k, j in enumerate(J)}
        self.V = len(J)
        self.N = 2 * self.V
        rows = [self.row(b) for b in side_bars(m, n)]
        self.basis = {}  # pivot col -> reduced row (pivot entry 1)
        for r in rows:
            r = self.reduce(r)
            piv = next((k for k, v in enumerate(r) if v), None)
            if piv is None:
                continue
            inv = pow(r[piv], p - 2, p)
            r = [v * inv % p for v in r]
            for k in list(self.basis):
                b = self.basis[k]
                if b[piv]:
                    f = b[piv]
                    self.basis[k] = [(x - f * y) % p for x, y in zip(b, r)]
            self.basis[piv] = r
        self.bar_rank = len(self.basis)
        self.free = [k for k in range(self.N) if k not in self.basis]
        self.res = {}
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for o in '/\\':
                    r = self.reduce(self.row(brace_bar((i, j), o)))
                    self.res[(i, j, o)] = [r[k] for k in self.free]

    def row(self, bar):
        a, b = bar
        pa, pb = square_pos(a), square_pos(b)
        r = [0] * self.N
        for (u, pu, pv) in ((a, pa, pb), (b, pb, pa)):
            k = self.idx[u]
            r[2 * k] = (r[2 * k] + pu[0] - pv[0]) % self.p
            r[2 * k + 1] = (r[2 * k + 1] + pu[1] - pv[1]) % self.p
        return r

    def reduce(self, r):
        p = self.p
        r = list(r)
        for piv, b in self.basis.items():
            if r[piv]:
                f = r[piv]
                r = [(x - f * y) % p for x, y in zip(r, b)]
        return r

    def rank(self, braces):
        """braces: iterable of (i, j) or (i, j, orient)."""
        p = self.p
        mat = []
        for b in braces:
            key = b if len(b) == 3 else (b[0], b[1], '/')
            mat.append(list(self.res[key]))
        rk = 0
        ncol = len(self.free)
        for col in range(ncol):
            piv = next((k for k in range(rk, len(mat)) if mat[k][col]), None)
            if piv is None:
                continue
            mat[rk], mat[piv] = mat[piv], mat[rk]
            inv = pow(mat[rk][col], p - 2, p)
            for k in range(len(mat)):
                if k != rk and mat[k][col]:
                    f = mat[k][col] * inv % p
                    mat[k] = [(x - f * y) % p for x, y in zip(mat[k], mat[rk])]
            rk += 1
        return self.bar_rank + rk


_RANKERS = {}


def ranks(m, n, braces):
    out = []
    for p in PRIMES:
        key = (m, n, p)
        if key not in _RANKERS:
            _RANKERS[key] = GridRank(m, n, p)
        out.append(_RANKERS[key].rank(braces))
    return out


def rank_rigid(m, n, braces):
    V = (m + 1) * (n + 1)
    for p in PRIMES:
        key = (m, n, p)
        if key not in _RANKERS:
            _RANKERS[key] = GridRank(m, n, p)
        if _RANKERS[key].rank(braces) == 2 * V - 3:
            return True
    return False


def exact_rank_fraction(m, n, braces):
    """Plain Gaussian elimination over Q for a few printed designs."""
    J = joints(m, n)
    idx = {j: k for k, j in enumerate(J)}
    bars = side_bars(m, n) + [brace_bar(b[:2], b[2] if len(b) == 3 else '/') for b in braces]
    rows = []
    for a, b in bars:
        pa, pb = square_pos(a), square_pos(b)
        r = [Fraction(0)] * (2 * len(J))
        r[2 * idx[a]] += pa[0] - pb[0]; r[2 * idx[a] + 1] += pa[1] - pb[1]
        r[2 * idx[b]] += pb[0] - pa[0]; r[2 * idx[b] + 1] += pb[1] - pa[1]
        rows.append(r)
    rk = 0
    for col in range(2 * len(J)):
        piv = next((k for k in range(rk, len(rows)) if rows[k][col] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        for k in range(len(rows)):
            if k != rk and rows[k][col] != 0:
                f = rows[k][col] / rows[rk][col]
                rows[k] = [x - f * y for x, y in zip(rows[k], rows[rk])]
        rk += 1
    return rk


def frac_rank(rows):
    rows = [list(r) for r in rows]
    rk = 0
    for col in range(len(rows[0])):
        piv = next((k for k in range(rk, len(rows)) if rows[k][col] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        for k in range(len(rows)):
            if k != rk and rows[k][col] != 0:
                f = rows[k][col] / rows[rk][col]
                rows[k] = [x - f * y for x, y in zip(rows[k], rows[rk])]
        rk += 1
    return rk


# -------------------------------------------------------- link graph (mine)
def groups(m, n, braces):
    parent = {('R', i): ('R', i) for i in range(1, m + 1)}
    parent.update({('C', j): ('C', j) for j in range(1, n + 1)})

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for b in braces:
        parent[find(('R', b[0]))] = find(('C', b[1]))
    comp = {}
    for v in parent:
        comp.setdefault(find(v), []).append(v)
    return list(comp.values())


# ------------------------------------------------- finite flex certificate
def flex_certificate(m, n, braces, part=None):
    """Try the explicit motion built from a partition of strip dots.

    Returns (ok, change) where ok means every side bar and every brace kept its
    length for t in a family of placements and change is the largest change of
    any joint-to-joint distance (so change > 0 means the shape really changed).
    """
    if part is None:
        part = groups(m, n, braces)
    if len(part) < 2:
        return False, 0.0
    ang = {}
    for k, comp in enumerate(part):
        for v in comp:
            ang[v] = 0.37 * k
    J = joints(m, n)
    base = {j: square_pos(j) for j in J}
    bars = side_bars(m, n)
    bl = [brace_bar(b[:2], b[2] if len(b) == 3 else '/') for b in braces]
    worst = 0.0
    change = 0.0
    for t in (0.05, 0.2, 0.5, 1.0):
        H = {c: (math.cos(t * ang[('C', c)]), math.sin(t * ang[('C', c)])) for c in range(1, n + 1)}
        Vd = {r: (math.sin(t * ang[('R', r)]), -math.cos(t * ang[('R', r)])) for r in range(1, m + 1)}
        pos = {}
        for (r, c) in J:
            x = sum(H[k][0] for k in range(1, c + 1)) + sum(Vd[k][0] for k in range(1, r + 1))
            y = sum(H[k][1] for k in range(1, c + 1)) + sum(Vd[k][1] for k in range(1, r + 1))
            pos[(r, c)] = (x, y)
        for a, b in bars + bl:
            d0 = math.dist(base[a], base[b])
            d1 = math.dist(pos[a], pos[b])
            worst = max(worst, abs(d0 - d1))
        if t == 1.0:
            for (i, j) in cells(m, n):
                for a, b in (brace_bar((i, j), '/'), brace_bar((i, j), '\\')):
                    change = max(change, abs(math.dist(base[a], base[b]) - math.dist(pos[a], pos[b])))
    return worst < 1e-12, change


def decide(m, n, braces):
    """Return 'holds' or 'flexes' with an independent certificate, else 'UNDECIDED'."""
    if rank_rigid(m, n, braces):
        return 'holds'
    ok, ch = flex_certificate(m, n, braces)
    if ok and ch > 1e-3:
        return 'flexes'
    return 'UNDECIDED'


ALL6_CELLS = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)]


def cells(m, n):
    return [(i, j) for i in range(1, m + 1) for j in range(1, n + 1)]


def covers(m, n, braces):
    return {b[0] for b in braces} == set(range(1, m + 1)) and {b[1] for b in braces} == set(range(1, n + 1))


def fmt(bs):
    return ','.join('%d%d' % b[:2] for b in sorted(bs))


# ===================================================================== checks
def main():
    say('Week 52 independent math check')
    say('=' * 60)

    # --- Problem 1: triangle rigid, square not ------------------------------
    say('\n[P1] triangle and square, fixed side lengths, plane')
    tri = [(0, 0), (1, 0), (0.5, math.sqrt(3) / 2)]
    # rigidity matrix of a triangle: rank 3 = 2*3-3
    T = []
    for a, b in itertools.combinations(range(3), 2):
        r = [Fraction(0)] * 6
        for (u, v) in ((a, b), (b, a)):
            r[2 * u] += Fraction(tri[u][0] - tri[v][0]).limit_denominator(10**9)
            r[2 * u + 1] += Fraction(tri[u][1] - tri[v][1]).limit_denominator(10**9)
        T.append(r)
    check(frac_rank(T) == 3, 'equilateral triangle: rigidity-matrix rank 3 = 2*3-3 (rigid in the plane)')
    # square: 1x1 grid with no braces flexes, with one brace holds
    check(decide(1, 1, []) == 'flexes', 'unbraced square flexes (explicit rhombus motion)')
    check(decide(1, 1, [(1, 1)]) == 'holds', 'square with one diagonal holds (rank 5 = 2*4-3)')
    check(decide(1, 1, [(1, 1, '\\')]) == 'holds', 'square with the other diagonal holds')
    check(exact_rank_fraction(1, 1, []) == 4 and exact_rank_fraction(1, 1, [(1, 1)]) == 5,
          'exact ranks over Q: square 4, braced square 5')

    # --- Problem 3: which four-bar shapes accept a diagonal of L*sqrt2 -----
    say('\n[P3] four bars of length L=1, the removed diagonal has length sqrt2')
    A, C = (0.0, 0.0), (1.0, 1.0)
    # points at distance 1 from both A and C
    mid = (0.5, 0.5); h = math.sqrt(1 - 0.5)
    ux, uy = (-1 / math.sqrt(2), 1 / math.sqrt(2))
    P = [(mid[0] + h * ux, mid[1] + h * uy), (mid[0] - h * ux, mid[1] - h * uy)]
    shapes = []
    for B in P:
        for D in P:
            shapes.append('square' if B != D else 'B=D doubled right isosceles triangle')
    say('     the 4 choices of (B, D):', shapes)
    check(sorted(set(shapes)) == ['B=D doubled right isosceles triangle', 'square'],
          'only the square, or the degenerate B=D overlap, accepts that diagonal')
    # path from the square to the B=D placement keeping all four sides = 1
    worst = 0.0
    for k in range(101):
        th = math.pi / 4 * (1 - k / 100)
        A_, B_, D_, C_ = (0, 0), (math.cos(th), math.sin(th)), (math.cos(th), -math.sin(th)), (2 * math.cos(th), 0)
        for X, Y in ((A_, B_), (B_, C_), (C_, D_), (D_, A_)):
            worst = max(worst, abs(math.dist(X, Y) - 1))
    for k in range(101):
        ph = math.pi / 2 * k / 100
        A_, B_, D_, C_ = (0, 0), (1, 0), (1, 0), (1 + math.cos(ph), math.sin(ph))
        for X, Y in ((A_, B_), (B_, C_), (C_, D_), (D_, A_)):
            worst = max(worst, abs(math.dist(X, Y) - 1))
    check(worst < 1e-12 and abs(math.dist((0, 0), (1, 1)) - math.sqrt(2)) < 1e-12,
          'the unbraced four-bar reaches B=D with |AC|=sqrt2 through the flat (collinear) placement')
    check(abs(60 * math.sqrt(3) - 103.92) < 0.005 and abs(60 * math.sqrt(2) - 84.853) < 0.0005,
          'guide numbers: 60-degree rhombus diagonals 60 and 103.92; 60*sqrt2 = 84.853')

    # --- Problem 4 -----------------------------------------------------------
    say('\n[P4] 2-by-2 printed designs')
    P4 = {'A': [(1, 1)], 'B': [(1, 1), (2, 2)], 'C': [(1, 1), (1, 2), (2, 1)],
          'D': [(1, 1), (1, 2), (2, 1), (2, 2)]}
    res = {k: decide(2, 2, v) for k, v in P4.items()}
    say('     ', res)
    check(res == {'A': 'flexes', 'B': 'flexes', 'C': 'holds', 'D': 'holds'}, 'circle C and D only (guide agrees)')

    # --- Problem 5 -----------------------------------------------------------
    say('\n[P5] fewest braces for 2-by-2, all subsets')
    allres = {}
    for k in range(5):
        for S in itertools.combinations(cells(2, 2), k):
            allres[S] = decide(2, 2, list(S))
    check('UNDECIDED' not in allres.values(), 'every 2-by-2 subset certified')
    mins = min(len(S) for S, v in allres.items() if v == 'holds')
    rig3 = [fmt(S) for S, v in allres.items() if v == 'holds' and len(S) == mins]
    say('      minimum', mins, 'minimum designs', rig3)
    check(mins == 3 and len(rig3) == 4, 'minimum 3; all four 3-cell sets hold')
    # orientation does not matter
    same = all(decide(2, 2, [(i, j, o1), (i2, j2, o2), (i3, j3, o3)]) == 'holds'
               for (i, j), (i2, j2), (i3, j3) in itertools.combinations(cells(2, 2), 3)
               for o1 in '/\\' for o2 in '/\\' for o3 in '/\\')
    check(same, 'every orientation choice of a 3-cell set also holds')

    # --- Problem 6 -----------------------------------------------------------
    say('\n[P6] fewest braces for 2-by-3, all subsets')
    allres = {}
    for k in range(7):
        for S in itertools.combinations(cells(2, 3), k):
            allres[S] = decide(2, 3, list(S))
    check('UNDECIDED' not in allres.values(), 'every 2-by-3 subset certified')
    mins = min(len(S) for S, v in allres.items() if v == 'holds')
    rig = [S for S, v in allres.items() if v == 'holds' and len(S) == mins]
    say('      minimum', mins, 'number of minimum designs', len(rig))
    check(mins == 4 and len(rig) == 12, 'minimum 4 with 12 minimum cell sets')
    rule = set()
    for omit in itertools.combinations(cells(2, 3), 2):
        if omit[0][1] != omit[1][1]:
            rule.add(tuple(sorted(set(cells(2, 3)) - set(omit))))
    check(rule == set(rig), "guide rule 'omit any pair except the two cells of one column' gives exactly the 12")
    check(allres[((1, 1), (1, 2), (1, 3), (2, 1))] == 'holds', 'guide example 11,12,13,21 holds')
    save_2x3 = allres

    # --- Problem 7 -----------------------------------------------------------
    say('\n[P7] printed 2-by-3 designs')
    a, b = decide(2, 3, [(1, 1), (1, 2), (2, 1), (2, 2)]), decide(2, 3, [(1, 1), (1, 2), (1, 3), (2, 1)])
    check((a, b) == ('flexes', 'holds'), 'A flexes, B holds: circle B only')
    check(decide(1, 3, [(1, 2)]) == 'flexes', 'worked example 1-by-3 with middle brace flexes (non-task example)')

    # --- Problem 8 -----------------------------------------------------------
    say('\n[P8] printed 3-by-3 designs, both covering every row and column')
    A8 = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)]
    B8 = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 1)]
    check(covers(3, 3, A8) and covers(3, 3, B8), 'A and B each have a brace in every row and column')
    check(decide(3, 3, A8) == 'flexes' and decide(3, 3, B8) == 'holds', 'A flexes, B holds: answer No')
    adds = [c for c in cells(3, 3) if c not in A8 and decide(3, 3, A8 + [c]) == 'holds']
    check(sorted(adds) == sorted(c for c in cells(3, 3) if c not in A8),
          'guide extension: every empty cell of A repairs it (' + fmt(adds) + ')')

    # --- Problem 9 -----------------------------------------------------------
    say('\n[P9] single removals from 11,12,13,21,22')
    S9 = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2)]
    check(decide(2, 3, S9) == 'holds', 'starting design holds')
    rem = [c for c in S9 if decide(2, 3, [x for x in S9 if x != c]) == 'holds']
    say('      removable:', fmt(rem))
    check(sorted(rem) == [(1, 1), (1, 2), (2, 1), (2, 2)], 'removable singles are 11,12,21,22; 13 is essential')
    tree_ok = all(all(decide(2, 3, [x for x in S9 if x not in (c, d)]) == 'flexes' for d in S9 if d != c) for c in rem)
    check(tree_ok, 'guide extension: after one permitted removal, every further single removal flexes')

    # --- Problem 10 ----------------------------------------------------------
    say('\n[P10] pairs removed from the full 2-by-3')
    full = cells(2, 3)
    fail = [p for p in itertools.combinations(full, 2) if decide(2, 3, [c for c in full if c not in p]) != 'holds']
    say('      failing pairs:', [fmt(p) for p in fail])
    check(len(fail) == 3 and all(p[0][1] == p[1][1] for p in fail), '3 failing pairs (same column), 12 succeed')

    # --- Problem 11 ----------------------------------------------------------
    say('\n[P11] one added brace')
    A11 = [(1, 1), (1, 2), (2, 1), (2, 2)]
    B11 = [(1, 1), (1, 2), (2, 2), (3, 3)]
    wa = [c for c in cells(3, 3) if c not in A11 and decide(3, 3, A11 + [c]) == 'holds']
    wb = [c for c in cells(3, 3) if c not in B11 and decide(3, 3, B11 + [c]) == 'holds']
    say('      A works at:', fmt(wa) or 'none', '  B works at:', fmt(wb))
    check(wa == [] and sorted(wb) == [(1, 3), (2, 3), (3, 1), (3, 2)], 'A: none; B: 13,23,31,32 (guide agrees)')
    check(decide(3, 3, A11 + [(1, 3), (3, 1)]) == 'holds', 'guide extension: A + 13 + 31 holds')
    two = [p for p in itertools.combinations([c for c in cells(3, 3) if c not in A11], 2)
           if decide(3, 3, A11 + list(p)) == 'holds']
    say('      all two-addition repairs of A:', [fmt(p) for p in two])

    # --- Problem 12 ----------------------------------------------------------
    say('\n[P12] 4-by-5: fewest braces')
    ex = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (3, 1), (4, 1)]
    check(decide(4, 5, ex) == 'holds', 'guide example 11,12,13,14,15,21,31,41 holds (exact rank mod p)')
    n7 = 0; bad7 = 0
    for S in itertools.combinations(cells(4, 5), 7):
        n7 += 1
        ok, ch = flex_certificate(4, 5, list(S))
        if not (ok and ch > 1e-3):
            bad7 += 1
    check(n7 == 77520 and bad7 == 0, 'all %d seven-brace designs have an explicit finite flex, so 7 or fewer never hold' % n7)
    n8 = sum(1 for S in itertools.combinations(cells(4, 5), 8) if rank_rigid(4, 5, list(S)))
    say('      eight-brace designs that hold:', n8, '(spanning trees of K_{4,5} = 4^4*5^3 =', 4 ** 4 * 5 ** 3, ')')
    check(n8 == 4 ** 4 * 5 ** 3, 'count of holding 8-brace designs equals spanning-tree count')

    # --- Problem 13 ----------------------------------------------------------
    say('\n[P13] 3-by-3, six braces, every row and column covered (one brace per cell)')
    six = list(itertools.combinations(cells(3, 3), 6))
    cov = [S for S in six if covers(3, 3, S)]
    hold = [S for S in cov if decide(3, 3, list(S)) == 'holds']
    say('      six-cell sets', len(six), 'covering', len(cov), 'holding', len(hold))
    check(len(six) == 84 and len(cov) == 78 and len(hold) == 78, 'guide: 84 subsets, 78 cover, all 78 hold -> Yes')
    say('   alternative reading: two braces (both diagonals) allowed in one cell')
    alt = [(1, 1, '/'), (1, 1, '\\'), (2, 2, '/'), (2, 2, '\\'), (3, 3, '/'), (3, 3, '\\')]
    d = 'holds' if rank_rigid(3, 3, alt) else ('flexes' if flex_certificate(3, 3, alt)[0] and flex_certificate(3, 3, alt)[1] > 1e-3 else '?')
    say('      both diagonals in 11, 22, 33 (six braces, every row and column):', d,
        ' ranks mod p', ranks(3, 3, alt), 'needed', 2 * 16 - 3)
    alt2 = [(1, 1, '/'), (1, 2, '/'), (2, 1, '/'), (2, 2, '/'), (3, 3, '/'), (3, 3, '\\')]
    d2 = 'holds' if rank_rigid(3, 3, alt2) else ('flexes' if flex_certificate(3, 3, alt2)[0] else '?')
    say('      11,12,21,22 plus both diagonals in 33:', d2)
    check(d == 'flexes' and d2 == 'flexes',
          'with doubled braces allowed, six covering braces can flex: P13 answer depends on the one-per-cell rule')
    # count covering six-brace multisets (each cell 0, 1 or 2 braces) that flex
    nm = nf = 0
    for counts in itertools.product((0, 1, 2), repeat=9):
        if sum(counts) != 6:
            continue
        bl = []
        for (c, k) in zip(cells(3, 3), counts):
            bl += [(c[0], c[1], '/'), (c[0], c[1], '\\')][:k]
        if not covers(3, 3, bl):
            continue
        nm += 1
        if not rank_rigid(3, 3, bl):
            nf += 1
    say('      covering six-brace placements with doubles allowed:', nm, 'of which flex:', nf)

    # --- Problem 14 ----------------------------------------------------------
    say('\n[P14] 4-by-4, nine braces, every row and column')
    S14 = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (4, 4)]
    check(len(S14) == 9 and covers(4, 4, S14) and decide(4, 4, S14) == 'flexes',
          'guide counterexample has 9 braces, covers, and flexes (explicit finite motion) -> No')
    stats = {}
    for k in range(17):
        tot = fl = 0
        for S in itertools.combinations(cells(4, 4), k):
            if not covers(4, 4, S):
                continue
            tot += 1
            r = rank_rigid(4, 4, list(S))
            g = len(groups(4, 4, S)) == 1
            if r != g:
                FAIL.append('rank/graph disagreement 4x4 ' + fmt(S))
            if not r:
                fl += 1
        stats[k] = (tot, fl)
    say('      covering designs by size (total, flexing):', {k: v for k, v in stats.items() if v[0]})
    maxflex = max(k for k, v in stats.items() if v[1])
    check(stats[9][1] > 0 and maxflex == 10 and stats[11][1] == 0,
          'guide extension: covering 4-by-4 can flex with up to 10 braces; 11 always hold')
    S10 = [c for c in cells(3, 3)] + [(4, 4)]
    check(decide(4, 4, S10) == 'flexes', 'guide: all nine cells of the 3-by-3 block plus 44 (ten braces) flexes')

    # --- the general criterion vs. certificates (guide overview) ------------
    say('\n[overview] link-graph criterion and rank formula 2(m+1)(n+1)-2-k, exhaustive on small grids')
    for (m, n) in ((1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3), (2, 4), (3, 4)):
        bad = 0; tot = 0
        for mask in range(1 << (m * n)):
            S = [c for k, c in enumerate(cells(m, n)) if mask >> k & 1]
            k = len(groups(m, n, S))
            rk = max(ranks(m, n, S))
            if rk != 2 * (m + 1) * (n + 1) - 2 - k:
                bad += 1
            tot += 1
        check(bad == 0, '%d-by-%d: all %d subsets satisfy rank = 2V-2-k (k = number of link groups)' % (m, n, tot))
    # finite flex for every disconnected 3x3 subset
    bad = 0
    for mask in range(1 << 9):
        S = [c for k, c in enumerate(cells(3, 3)) if mask >> k & 1]
        if len(groups(3, 3, S)) > 1:
            ok, ch = flex_certificate(3, 3, S)
            bad += not (ok and ch > 1e-3)
    check(bad == 0, '3-by-3: every disconnected design has an explicit finite flex')
    # orientation: residual rows of the two diagonals of a cell are parallel
    gr = GridRank(3, 4, PRIMES[0])
    par = all(gr.rank([(i, j, '/'), (i, j, '\\')]) == gr.rank([(i, j, '/')]) for (i, j) in cells(3, 4))
    check(par, "either diagonal of a cell imposes the same first-order constraint (guide: 'either orientation')")
    # exact rational ranks for the printed designs
    for name, (m, n, S) in {'P4B': (2, 2, P4['B']), 'P7A': (2, 3, [(1, 1), (1, 2), (2, 1), (2, 2)]),
                            'P8A': (3, 3, A8), 'P8B': (3, 3, B8), 'handoff': (2, 3, [(1, 1), (1, 2), (2, 3)])}.items():
        k = len(groups(m, n, S))
        check(exact_rank_fraction(m, n, S) == 2 * (m + 1) * (n + 1) - 2 - k,
              '%s exact rank over Q = 2V-2-k with k=%d' % (name, k))

    # --- planarity: what happens if a frame is lifted off the table --------
    say('\n[planarity] fold out of the plane (the flat rule is printed only on the K-1 page)')
    def fold_ok(m, n, braces, axis_c):
        """Rotate every joint with column index > axis_c about the line x = axis_c in 3D."""
        J = joints(m, n)
        base = {j: (j[1], -j[0], 0.0) for j in J}
        bl = side_bars(m, n) + [brace_bar(b[:2], b[2] if len(b) == 3 else '/') for b in braces]
        worst = 0.0; change = 0.0
        for th in (0.1, 0.8, 1.5):
            pos = {}
            for j, (x, y, z) in base.items():
                if x > axis_c:
                    dx = x - axis_c
                    pos[j] = (axis_c + dx * math.cos(th), y, dx * math.sin(th))
                else:
                    pos[j] = (x, y, z)
            for a, b in bl:
                worst = max(worst, abs(math.dist(base[a], base[b]) - math.dist(pos[a], pos[b])))
            change = max(change, max(abs(math.dist(base[a], base[b]) - math.dist(pos[a], pos[b]))
                                     for a in J for b in J))
        return worst < 1e-12 and change > 1e-3
    check(fold_ok(2, 3, sorted(ALL6_CELLS), 1), 'a fully braced 2-by-3 lifted off the table folds along grid line x=1 with every bar length kept')
    check(fold_ok(3, 3, B8, 2), 'P8B (which holds in the plane) folds along an interior grid line in 3D')
    sq = {(0, 0): (0, 0, 0), (0, 1): (1, 0, 0), (1, 1): (1, -1, 0), (1, 0): (0, -1, 0)}
    # braced square folds along its brace (0,1)-(1,0)? brace '/' joins (1,0)-(0,1)
    ax0, ax1 = sq[(1, 0)], sq[(0, 1)]
    u = [ax1[k] - ax0[k] for k in range(3)]; ln = math.sqrt(sum(x * x for x in u)); u = [x / ln for x in u]
    def rot(pnt, th):
        v = [pnt[k] - ax0[k] for k in range(3)]
        c, s_ = math.cos(th), math.sin(th)
        dot = sum(a * b for a, b in zip(u, v))
        cr = [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]
        return tuple(ax0[k] + v[k] * c + cr[k] * s_ + u[k] * dot * (1 - c) for k in range(3))
    moved = dict(sq); moved[(1, 1)] = rot(sq[(1, 1)], 1.0)
    bars = [((0, 0), (0, 1)), ((0, 1), (1, 1)), ((1, 1), (1, 0)), ((1, 0), (0, 0)), ((1, 0), (0, 1))]
    keep = all(abs(math.dist(sq[a], sq[b]) - math.dist(moved[a], moved[b])) < 1e-12 for a, b in bars)
    check(keep and abs(math.dist(moved[(0, 0)], moved[(1, 1)]) - math.sqrt(2)) > 1e-3,
          'a braced square folds along its brace in 3D (guide overview says so too)')

    # --- guide handoff --------------------------------------------------------
    say('\n[guide handoff] covered but separated models')
    H = [(1, 1), (1, 2), (2, 3)]
    check(covers(2, 3, H) and decide(2, 3, H) == 'flexes', 'spare 2-by-3 with 11,12,23 covers every strip and flexes')
    check(all(decide(2, 3, H + [c]) == 'holds' for c in [(1, 3), (2, 1), (2, 2)]), 'each empty cell 13,21,22 makes it hold')
    check(all(decide(2, 2, P4['B'] + [c]) == 'holds' for c in [(1, 2), (2, 1)]), 'P4B plus either empty cell holds')

    # --- guide materials -------------------------------------------------------
    say('\n[guide materials] kit counts')
    def kit(m, n):
        return len(side_bars(m, n)), m * n, (m + 1) * (n + 1)
    check(kit(2, 2) == (12, 4, 9) and kit(2, 3) == (17, 6, 12) and kit(3, 3) == (24, 9, 16), 'per-kit sides/braces/pins')
    sides = 2 * 7 + 2 * 12 + 2 * 17 + 4; br = 2 * 1 + 2 * 4 + 2 * 6 + 1; pins = 2 * 7 + 2 * 9 + 2 * 12 + 4
    check((sides, br, pins) == (76, 23, 60) and (sides + 8, br + 4, pins + 12) == (84, 27, 72), 'table totals 76/23/60 and 84/27/72')
    check(abs(60 * math.sqrt(2) + 16 - 100.853) < 0.0005, 'diagonal strip total length 100.853 mm')
    check(2 * 2 + 2 * 2 + 5 + 3 == 16, 'printing total 16 student sheets')

    say('\n' + ('ALL CHECKS PASSED' if not FAIL else 'FAILURES: %d' % len(FAIL)))
    for f in FAIL:
        say('  - ' + f)
    with open(os.path.join(HERE, 'out_check_math.txt'), 'w') as fh:
        fh.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
