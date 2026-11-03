"""Checks for draft weeks 101-107 (counting and networks group).

Standard library only. Run: python3 plans/drafts/weeks-101-plus/check_counting_networks.py
Each check_week_1NN() asserts the small numbers quoted in the matching draft.
"""

import itertools
import random
from collections import Counter
from fractions import Fraction
from math import comb


# ---------------------------------------------------------------- week 101

def odd_count_row(n):
    return sum(comb(n, k) % 2 for k in range(n + 1))


def check_week_101():
    # Bead paths: n rows of pegs, 2^n left/right words, bin k reached by C(n, k).
    for n in range(1, 11):
        bins = Counter(sum(w) for w in itertools.product((0, 1), repeat=n))
        assert [bins[k] for k in range(n + 1)] == [comb(n, k) for k in range(n + 1)]
        assert sum(bins.values()) == 2 ** n
    # Year 1 Handout 5 machine: three drops, bins 1, 3, 3, 1 out of 8.
    assert [comb(3, k) for k in range(4)] == [1, 3, 3, 1]
    # Four rows: 1, 4, 6, 4, 1 out of 16; 32 beads expect 2, 8, 12, 8, 2.
    assert [comb(4, k) for k in range(5)] == [1, 4, 6, 4, 1]
    assert [32 * comb(4, k) // 16 for k in range(5)] == [2, 8, 12, 8, 2]
    # Middle bin shrinks while still the largest: 6/16, 20/64, 70/256, 252/1024.
    mids = [Fraction(comb(n, n // 2), 2 ** n) for n in (4, 6, 8, 10)]
    assert mids == [Fraction(3, 8), Fraction(5, 16), Fraction(35, 128), Fraction(63, 256)]
    assert round(float(mids[-1]), 3) == 0.246
    # Two outer bins of a 10-row board: 2/1024, about 1 bead in 500.
    assert Fraction(2, 2 ** 10) == Fraction(1, 512)
    # Odd entries in row n = 2^(number of 1s in binary n), rows 0..63.
    for n in range(64):
        assert odd_count_row(n) == 2 ** bin(n).count("1")
    assert [odd_count_row(n) for n in range(16)] == [
        1, 2, 2, 4, 2, 4, 4, 8, 2, 4, 4, 8, 4, 8, 8, 16]
    # Lucas mod 2: C(n, k) is odd exactly when k's binary 1s sit inside n's.
    for n in range(64):
        for k in range(n + 1):
            assert (comb(n, k) % 2 == 1) == ((k & n) == k)
    # Rows 2^m - 1 are all odd; row 2^m has only its two end 1s odd.
    for m in range(1, 6):
        assert odd_count_row(2 ** m - 1) == 2 ** m
        assert odd_count_row(2 ** m) == 2
    # The first 2^k rows hold 3^k odd entries: 27 of 36 for 8 rows, 81 of 136 for 16.
    for k in range(7):
        rows = range(2 ** k)
        assert sum(odd_count_row(n) for n in rows) == 3 ** k
    assert sum(n + 1 for n in range(8)) == 36 and sum(n + 1 for n in range(16)) == 136
    # The odd share keeps falling: 3^k / (2^k (2^k + 1) / 2).
    shares = [Fraction(3 ** k, 2 ** k * (2 ** k + 1) // 2) for k in range(1, 8)]
    assert all(a > b for a, b in zip(shares, shares[1:]))
    # Mod 3 version: entries not divisible by 3 in row n = product of (base-3 digit + 1).
    for n in range(81):
        prod, m = 1, n
        while m:
            prod *= m % 3 + 1
            m //= 3
        assert sum(1 for k in range(n + 1) if comb(n, k) % 3) == prod
    # Rigged pegs on a two-row board: top peg 2/3 left, then a fair peg on the
    # left and an always-right peg on the right gives three equal bins.
    p, a, b = Fraction(2, 3), Fraction(1, 2), Fraction(0)
    bins = [p * a, p * (1 - a) + (1 - p) * b, (1 - p) * (1 - b)]
    assert bins == [Fraction(1, 3)] * 3


# ---------------------------------------------------------------- week 102

def aztec_cells(n):
    cells = set()
    for i in range(2 * n):
        for j in range(2 * n):
            if abs(i - n + 0.5) + abs(j - n + 0.5) <= n:
                cells.add((i, j))
    return frozenset(cells)


def domino_tilings(cells):
    out = []

    def rec(rem, cur):
        if not rem:
            out.append(frozenset(cur))
            return
        c = min(rem)
        i, j = c
        for d in ((i, j + 1), (i + 1, j)):
            if d in rem:
                rec(rem - {c, d}, cur + [frozenset((c, d))])

    rec(frozenset(cells), [])
    return out


def flips(tiling):
    """Tilings one 2x2 flip away."""
    doms = list(tiling)
    res = []
    for x in range(len(doms)):
        for y in range(x + 1, len(doms)):
            sq = sorted(doms[x] | doms[y])
            i0, j0 = sq[0]
            box = [(i0, j0), (i0, j0 + 1), (i0 + 1, j0), (i0 + 1, j0 + 1)]
            if sq == box:
                h = {frozenset(box[:2]), frozenset(box[2:])}
                v = {frozenset((box[0], box[2])), frozenset((box[1], box[3]))}
                new = h if doms[x] in v else v
                res.append(frozenset((set(tiling) - {doms[x], doms[y]}) | new))
    return res


def bfs(start):
    dist = {start: 0}
    frontier = [start]
    while frontier:
        nxt = []
        for t in frontier:
            for u in flips(t):
                if u not in dist:
                    dist[u] = dist[t] + 1
                    nxt.append(u)
        frontier = nxt
    return dist


def check_week_102():
    counts = []
    for n in range(1, 5):
        cells = aztec_cells(n)
        assert len(cells) == 2 * n * (n + 1)          # 4, 12, 24, 40 squares
        tilings = domino_tilings(cells)
        assert len(tilings) == 2 ** (n * (n + 1) // 2)
        counts.append(len(tilings))
        d = bfs(tilings[0])
        assert len(d) == len(tilings)                 # flips connect every tiling
        # Farthest apart: 1, 5, 14, 30 flips = 1 + 4 + ... + n^2.
        # (all starts for n <= 3; for n = 4 one start already reaches 30)
        if n <= 3:
            diam = max(max(bfs(t).values()) for t in tilings)
        else:
            diam = max(d.values())
        assert diam == n * (n + 1) * (2 * n + 1) // 6
        # Flips available in one tiling: between n and n(n+1)/2.
        fl = [len(flips(t)) for t in tilings]
        assert min(fl) == n and max(fl) == n * (n + 1) // 2
    assert counts == [2, 8, 64, 1024]
    # Sorting by the top two squares: one flat domino or two standing ones.
    # Order 2 splits 6 + 2, order 3 splits 56 + 8, order 4 splits 960 + 64;
    # the "two standing" pile always has the previous order's count.
    splits = []
    for n in range(2, 5):
        cells = aztec_cells(n)
        cap = frozenset(x for x in cells if x[0] == 0)
        tilings = domino_tilings(cells)
        flat = sum(1 for t in tilings if cap in t)
        splits.append((flat, len(tilings) - flat))
    assert splits == [(6, 2), (56, 8), (960, 64)]
    assert [counts[k + 1] // counts[k] for k in range(3)] == [4, 8, 16]
    # Contrast: 2-by-n strips (Fibonacci), the 4-by-4 square has 36.
    strip = [len(domino_tilings({(i, j) for i in range(2) for j in range(n)}))
             for n in range(1, 8)]
    assert strip == [1, 2, 3, 5, 8, 13, 21]
    assert len(domino_tilings({(i, j) for i in range(4) for j in range(4)})) == 36
    # Order 3: 12 squares of each colour, so the colour count never blocks it.
    cells = aztec_cells(3)
    assert sum((i + j) % 2 for i, j in cells) == 12


# ---------------------------------------------------------------- week 103

def hanoi_moves(n, a=0, b=2, c=1):
    if n == 0:
        return []
    return hanoi_moves(n - 1, a, c, b) + [(n, a, b)] + hanoi_moves(n - 1, c, b, a)


def hanoi_graph(n, linear=False):
    """States are tuples peg[disc] for discs 1 (smallest) .. n."""
    states = list(itertools.product(range(3), repeat=n))
    adj = {s: [] for s in states}
    for s in states:
        for disc in range(n):
            # disc can move if no smaller disc sits on its peg
            if any(s[d] == s[disc] for d in range(disc)):
                continue
            for peg in range(3):
                if peg == s[disc]:
                    continue
                if linear and abs(peg - s[disc]) != 1:
                    continue
                if any(s[d] == peg for d in range(disc)):
                    continue
                adj[s].append(s[:disc] + (peg,) + s[disc + 1:])
    return adj


def dist_from(adj, s):
    d = {s: 0}
    fr = [s]
    while fr:
        nx = []
        for v in fr:
            for w in adj[v]:
                if w not in d:
                    d[w] = d[v] + 1
                    nx.append(w)
        fr = nx
    return d


def check_week_103():
    for n in range(1, 7):
        moves = hanoi_moves(n)
        assert len(moves) == 2 ** n - 1                       # 1, 3, 7, 15, 31, 63
        ruler = [1 + ((k & -k).bit_length() - 1) for k in range(1, 2 ** n)]
        assert [m[0] for m in moves] == ruler                 # disc moved = ruler sequence
        gray = [k ^ (k >> 1) for k in range(2 ** n)]
        changed = [(gray[k] ^ gray[k - 1]).bit_length() for k in range(1, 2 ** n)]
        assert changed == ruler                               # Gray-code bit = same sequence
        assert len(set(gray)) == 2 ** n
    assert [m[0] for m in hanoi_moves(3)] == [1, 2, 1, 3, 1, 2, 1]
    assert [k ^ (k >> 1) for k in range(8)] == [0, 1, 3, 2, 6, 7, 5, 4]  # 000 001 011 010 110 111 101 100
    # Smallest disc moves on every odd-numbered move, always the same way round.
    for n in range(1, 7):
        small = [m for m in hanoi_moves(n) if m[0] == 1]
        assert len(small) == 2 ** (n - 1)
        steps = {(b - a) % 3 for _, a, b in small}
        assert len(steps) == 1
    for n in range(1, 6):
        adj = hanoi_graph(n)
        assert len(adj) == 3 ** n                             # 3, 9, 27, 81, 243 states
        edges = sum(len(v) for v in adj.values()) // 2
        assert edges == 3 * (3 ** n - 1) // 2                 # 3, 12, 39, 120, 363
        degs = Counter(len(v) for v in adj.values())
        assert degs[2] == 3 and degs[3] == 3 ** n - 3         # three corner states
        start, goal = (0,) * n, (2,) * n
        assert dist_from(adj, start)[goal] == 2 ** n - 1
        # Neighbour-pegs-only version: 3^n - 1 moves, so it passes every state.
        lin = hanoi_graph(n, linear=True)
        d = dist_from(lin, start)
        assert d[goal] == 3 ** n - 1                          # 2, 8, 26, 80, 242
        assert len(d) == 3 ** n
    # The two-disc map: 9 states, 3 moves corner to corner, 8 with neighbour pegs only.
    assert len(hanoi_graph(2)) == 9
    assert dist_from(hanoi_graph(2, True), (0, 0))[(2, 2)] == 8


# ---------------------------------------------------------------- week 104

def latin_squares(n):
    rows = list(itertools.permutations(range(n)))
    out = []

    def rec(sq):
        if len(sq) == n:
            out.append(tuple(sq))
            return
        for r in rows:
            if all(r[c] != s[c] for s in sq for c in range(n)):
                rec(sq + [r])

    rec([])
    return out


def orthogonal(a, b, n):
    return len({(a[i][j], b[i][j]) for i in range(n) for j in range(n)}) == n * n


def diagonals_ok(a, n):
    return (len({a[i][i] for i in range(n)}) == n
            and len({a[i][n - 1 - i] for i in range(n)}) == n)


def dihedral(sq_pair, n):
    """All 8 rotations and reflections of a card arrangement."""
    a, b = sq_pair
    grid = tuple(tuple((a[i][j], b[i][j]) for j in range(n)) for i in range(n))
    out = set()
    g = grid
    for _ in range(4):
        g = tuple(tuple(g[n - 1 - j][i] for j in range(n)) for i in range(n))
        out.add(g)
        out.add(tuple(tuple(row[::-1]) for row in g))
    return out


def check_week_104():
    L2, L3, L4 = latin_squares(2), latin_squares(3), latin_squares(4)
    assert (len(L2), len(L3), len(L4)) == (2, 12, 576)
    # 2-by-2: four cards (2 ranks x 2 suits) can never work.
    assert not any(orthogonal(a, b, 2) for a in L2 for b in L2)
    # 3-by-3: nine cards work in 72 ways, but never with both diagonals too.
    p3 = [(a, b) for a in L3 for b in L3 if orthogonal(a, b, 3)]
    assert len(p3) == 72
    assert not any(diagonals_ok(a, 3) and diagonals_ok(b, 3) for a, b in p3)
    # 4-by-4: 16 face cards, rows and columns: 6912 arrangements;
    # adding both diagonals: 1152, which is 144 up to turning and flipping.
    p4 = [(a, b) for a in L4 for b in L4 if orthogonal(a, b, 4)]
    assert len(p4) == 6912
    assert len({a for a, _ in p4}) == 144             # rank patterns that have a suit partner
    d4 = [(a, b) for a, b in p4 if diagonals_ok(a, 4) and diagonals_ok(b, 4)]
    assert len(d4) == 1152
    orbits = {min(dihedral(pr, 4)) for pr in d4}
    assert len(orbits) == 144 == 1152 // 8
    # The cyclic 4-by-4 rank pattern (i + j mod 4) has no suit partner.
    cyc = tuple(tuple((i + j) % 4 for j in range(4)) for i in range(4))
    assert not any(orthogonal(cyc, b, 4) for b in L4)
    # 5-by-5 works: ranks i + j, suits i + 2j (mod 5), diagonals included.
    a5 = tuple(tuple((i + j) % 5 for j in range(5)) for i in range(5))
    b5 = tuple(tuple((i + 2 * j) % 5 for j in range(5)) for i in range(5))
    assert orthogonal(a5, b5, 5) and diagonals_ok(b5, 5)
    # A one-move hint for adults: one completed 4-by-4 with diagonals.
    a, b = d4[0]
    assert orthogonal(a, b, 4) and diagonals_ok(a, 4) and diagonals_ok(b, 4)


# ---------------------------------------------------------------- week 105

def knight_graph(r, c):
    cells = [(i, j) for i in range(r) for j in range(c)]
    adj = {x: [] for x in cells}
    for (i, j) in cells:
        for di, dj in ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)):
            if 0 <= i + di < r and 0 <= j + dj < c:
                adj[(i, j)].append((i + di, j + dj))
    return cells, adj


def tour_starts(r, c, closed=False):
    """Directed tours counted by starting square (closed: from (0, 0) only)."""
    cells, adj = knight_graph(r, c)
    n = len(cells)
    counts = Counter()

    def dfs(v, seen, s):
        if len(seen) == n:
            if not closed or s in adj[v]:
                counts[s] += 1
            return
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                dfs(w, seen, s)
                seen.discard(w)

    for s in ([cells[0]] if closed else cells):
        dfs(s, {s}, s)
    return counts


def warnsdorff(r, c, s):
    cells, adj = knight_graph(r, c)
    path, seen = [s], {s}
    while len(path) < r * c:
        opts = [w for w in adj[path[-1]] if w not in seen]
        if not opts:
            break
        w = min(opts, key=lambda w: (sum(u not in seen for u in adj[w]), w))
        path.append(w)
        seen.add(w)
    return path


def check_week_105():
    # 3-by-3: the centre has no moves; the outer 8 squares form one knight loop.
    cells, adj = knight_graph(3, 3)
    assert adj[(1, 1)] == []
    ring = [x for x in cells if x != (1, 1)]
    assert all(len(adj[x]) == 2 for x in ring)
    seen, v, prev = [ring[0]], ring[0], None
    while True:
        nxt = [w for w in adj[v] if w != prev][0]
        if nxt == ring[0]:
            break
        seen.append(nxt)
        prev, v = v, nxt
    assert len(seen) == 8
    # 3-by-4: 16 directed open tours (8 up to reversal), none closed;
    # they start only at the four corners and the two middle-row end squares.
    s34 = tour_starts(3, 4)
    assert sum(s34.values()) == 16
    assert set(s34) == {(0, 0), (0, 3), (2, 0), (2, 3), (1, 0), (1, 3)}
    assert sum(tour_starts(3, 4, closed=True).values()) == 0
    # 4-by-4, 3-by-5 and 3-by-6 have no open tour at all; 3-by-7 has 104.
    for rc in [(4, 4), (3, 5), (3, 6)]:
        assert sum(tour_starts(*rc).values()) == 0
    s37 = tour_starts(3, 7)
    assert sum(s37.values()) == 104 and s37[(0, 0)] == 8
    # Colouring: a knight always changes colour, so a closed tour needs an even
    # number of squares, and on 5-by-5 (13 + 12) an open tour starts and ends on the 13.
    for r, c in [(3, 4), (5, 5), (8, 8)]:
        cells, adj = knight_graph(r, c)
        assert all((i + j) % 2 != (x + y) % 2 for (i, j) in cells for (x, y) in adj[(i, j)])
    cells, _ = knight_graph(5, 5)
    assert sum((i + j) % 2 == 0 for i, j in cells) == 13
    # Warnsdorff (fewest onward exits, ties to the lowest row then column):
    # succeeds from the corner of 5-by-5 and 8-by-8 and of 3-by-4,
    # but sticks after 15 squares from the corner of 3-by-7, where 8 tours start.
    assert len(warnsdorff(5, 5, (0, 0))) == 25
    assert len(warnsdorff(8, 8, (0, 0))) == 64
    assert len(warnsdorff(3, 4, (0, 0))) == 12
    assert len(warnsdorff(3, 7, (0, 0))) == 15
    # Schwenk's list: 3-by-4 has no closed tour (checked above); 3-by-8 none either.
    assert sum(tour_starts(3, 8, closed=True).values()) == 0


# ---------------------------------------------------------------- week 106

def chromatic_number(vertices, edges):
    for k in range(1, len(vertices) + 1):
        for col in itertools.product(range(k), repeat=len(vertices)):
            c = dict(zip(vertices, col))
            if all(c[a] != c[b] for a, b in edges):
                return k
    return len(vertices)


def check_week_106():
    # Straight-line maps: 4 lines; neighbouring regions differ in one line,
    # so "how many lines am I above?" mod 2 is a 2-colouring.
    lines = [(1, 0, -0.3), (0, 1, -0.2), (1, 1, -1.1), (1, -1, 0.15)]   # ax + by + c

    def signs(x, y):
        return tuple(a * x + b * y + c > 0 for a, b, c in lines)

    pts = [[signs(-2 + i * 0.01, -2 + j * 0.01) for j in range(400)] for i in range(400)]
    regions = {s for row in pts for s in row}
    assert len(regions) == 11 == 1 + 4 + comb(4, 2)
    for i in range(399):
        for j in range(399):
            for s, t in ((pts[i][j], pts[i + 1][j]), (pts[i][j], pts[i][j + 1])):
                if s != t:
                    diff = sum(u != v for u, v in zip(s, t))
                    if diff == 1:
                        assert sum(s) % 2 != sum(t) % 2
    # Circles work the same way: inside-count parity. Three overlapping circles.
    circles = [(0, 0, 1), (1, 0, 1), (0.5, 0.8, 1)]

    def inside(x, y):
        return tuple((x - a) ** 2 + (y - b) ** 2 < r * r for a, b, r in circles)

    grid = [[inside(-1.5 + i * 0.01, -1.5 + j * 0.01) for j in range(400)] for i in range(400)]
    assert len({s for row in grid for s in row}) == 8   # 7 pieces inside + outside
    # Ring maps: a country ringed by 4 neighbours needs 3 colours, by 5 needs 4.
    for ring, need in ((3, 4), (4, 3), (5, 4), (6, 3)):
        vs = list(range(ring + 1))
        es = [(i, (i + 1) % ring) for i in range(ring)] + [(ring, i) for i in range(ring)]
        assert chromatic_number(vs, es) == need
    # A ring alone (no middle country): even ring 2 colours, odd ring 3.
    assert chromatic_number(list(range(5)), [(i, (i + 1) % 5) for i in range(5)]) == 3
    # Planar maps have a country with at most 5 neighbours: E <= 3V - 6 < 3V.
    for v in range(3, 50):
        assert 2 * (3 * v - 6) < 6 * v
    # Seven countries on a torus, each touching all six others (dual of K7):
    # triangles {i, i+1, i+3} and {i, i+2, i+3} mod 7.
    tris = [frozenset({i, (i + 1) % 7, (i + 3) % 7}) for i in range(7)] + \
           [frozenset({i, (i + 2) % 7, (i + 3) % 7}) for i in range(7)]
    assert len(set(tris)) == 14
    edge_use = Counter(frozenset(e) for t in tris for e in itertools.combinations(sorted(t), 2))
    assert len(edge_use) == 21 and set(edge_use.values()) == {2}   # every pair once, two faces
    assert 7 - 21 + 14 == 0                                         # Euler characteristic of a torus
    for v in range(7):                                              # each corner is a disc (6-cycle link)
        link = [tuple(sorted(t - {v})) for t in tris if v in t]
        g = Counter(x for e in link for x in e)
        assert len(link) == 6 and set(g.values()) == {2}
        comp, stack = set(), [link[0][0]]
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            stack += [y for e in link if x in e for y in e]
        assert len(comp) == 6
    # Heawood numbers: floor((7 + sqrt(49 - 24 chi)) / 2) gives 4 (sphere) and 7 (torus).
    def heawood(chi):
        return int((7 + (49 - 24 * chi) ** 0.5) / 2)
    assert heawood(2) == 4 and heawood(0) == 7


# ---------------------------------------------------------------- week 107

def grid_graph(m, n):
    V = [(i, j) for i in range(m) for j in range(n)]
    E = [((i, j), (i, j + 1)) for i in range(m) for j in range(n - 1)] + \
        [((i, j), (i + 1, j)) for i in range(m - 1) for j in range(n)]
    return V, E


def det(M):
    M = [[Fraction(x) for x in r] for r in M]
    n, d = len(M), Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return 0
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n):
                M[r][k] -= f * M[c][k]
    return d


def spanning_trees(m, n):
    V, E = grid_graph(m, n)
    idx = {v: k for k, v in enumerate(V)}
    L = [[0] * len(V) for _ in V]
    for a, b in E:
        i, j = idx[a], idx[b]
        L[i][i] += 1
        L[j][j] += 1
        L[i][j] -= 1
        L[j][i] -= 1
    return det([r[1:] for r in L[1:]])


def wilson(V, nbrs, rng):
    root = V[0]
    in_tree = {root}
    nxt = {}
    for v in V:
        u = v
        while u not in in_tree:            # random walk, remembering last exit (erases loops)
            nxt[u] = rng.choice(nbrs[u])
            u = nxt[u]
        u = v
        while u not in in_tree:
            in_tree.add(u)
            u = nxt[u]
    return frozenset(frozenset((v, nxt[v])) for v in V if v != root)


def right_hand_walk(doors, start, heading, stop, limit):
    """Cell-level right-hand rule: try right, straight, left, back."""
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]       # N E S W
    cell, h, path = start, heading, [start]
    for _ in range(limit):
        for turn in (1, 0, -1, 2):
            nh = (h + turn) % 4
            nb = (cell[0] + dirs[nh][0], cell[1] + dirs[nh][1])
            if frozenset((cell, nb)) in doors:
                cell, h = nb, nh
                path.append(cell)
                break
        if stop(cell, path):
            break
    return path


def tremaux(nbrs, start, goal, rng):
    """Trémaux: mark passages; never use one a third time. Returns passage uses."""
    marks = Counter()
    v, came = start, None
    steps = 0
    while v != goal and steps < 10000:
        steps += 1
        options = nbrs[v]
        if came is not None and sum(marks[frozenset((v, w))] for w in options) > 1 and \
                marks[frozenset((v, came))] == 1:
            # reached an old junction by a new passage: turn back
            w = came
        else:
            fresh = [w for w in options if marks[frozenset((v, w))] == 0]
            once = [w for w in options if marks[frozenset((v, w))] == 1]
            w = rng.choice(fresh) if fresh else rng.choice(once)
        marks[frozenset((v, w))] += 1
        came, v = v, w
    return v, marks


def check_week_107():
    # A perfect maze on an m-by-n grid of rooms is a spanning tree:
    # mn - 1 open doors and (m - 1)(n - 1) inner walls left standing.
    for m, n in [(2, 2), (3, 3), (4, 4), (5, 7)]:
        inner = (m - 1) * n + m * (n - 1)
        assert inner - (m * n - 1) == (m - 1) * (n - 1)
    assert (4 - 1) * 4 + 4 * (4 - 1) == 24
    counts = [spanning_trees(*mn) for mn in [(2, 2), (2, 3), (3, 3), (3, 4), (4, 4)]]
    assert counts == [4, 15, 192, 2415, 100352]
    # Knocking down walls in a random order (skipping any that would make a loop)
    # is NOT fair on 2-by-3: six mazes get 300/5040 = 5/84, nine get 360/5040 = 1/14.
    V, E = grid_graph(2, 3)

    def find(p, x):
        while p[x] != x:
            x = p[x]
        return x

    tally = Counter()
    for perm in itertools.permutations(range(len(E))):
        p = {v: v for v in V}
        kept = []
        for k in perm:
            a, b = E[k]
            ra, rb = find(p, a), find(p, b)
            if ra != rb:
                p[ra] = rb
                kept.append(k)
        tally[frozenset(kept)] += 1
    assert len(tally) == 15
    assert sorted(Counter(tally.values()).items()) == [(300, 6), (360, 9)]
    assert Fraction(300, 5040) == Fraction(5, 84) and Fraction(360, 5040) == Fraction(1, 14)
    # Wilson's loop-erased walks: every one of the 15 mazes about equally often.
    nbrs = {v: [w for e in E for w in e if v in e and w != v] for v in V}
    rng = random.Random(107)
    trials = 30000
    w = Counter(wilson(V, nbrs, rng) for _ in range(trials))
    assert len(w) == 15
    assert all(abs(c / trials - 1 / 15) < 0.01 for c in w.values())
    # Hand on the wall in a perfect maze: from the entrance room the walker
    # passes every door exactly twice and visits every room before returning.
    V4, E4 = grid_graph(4, 4)
    nb4 = {v: [w for e in E4 for w in e if v in e and w != v] for v in V4}
    for seed in range(20):
        tree = wilson(V4, nb4, random.Random(seed))
        path = right_hand_walk(tree, (0, 0), 0, lambda c, p: len(p) == 2 * 15 + 1, 200)
        assert path[-1] == (0, 0) and len(path) - 1 == 2 * 15
        assert set(path) == set(V4)
        uses = Counter(frozenset(e) for e in zip(path, path[1:]))
        assert set(uses.values()) == {2}
    # Hand on the wall can circle forever: in an all-open 3-by-3 block, starting
    # in the centre facing north, the right-hand walker never reaches corner (2, 0).
    V3, E3 = grid_graph(3, 3)
    doors3 = {frozenset(e) for e in E3}
    path = right_hand_walk(doors3, (1, 1), 0, lambda c, p: c == (2, 0), 100)
    assert (2, 0) not in path
    # Trémaux reaches the goal in a maze full of loops, using no passage more than twice.
    V5, E5 = grid_graph(5, 5)
    nb5 = {v: [w for e in E5 for w in e if v in e and w != v] for v in V5}
    for seed in range(50):
        end, marks = tremaux(nb5, (0, 0), (4, 4), random.Random(seed))
        assert end == (4, 4) and max(marks.values()) <= 2


def main():
    for name in sorted(k for k in globals() if k.startswith("check_week_")):
        globals()[name]()
        print(name.replace("check_", ""), "ok")


if __name__ == "__main__":
    main()
