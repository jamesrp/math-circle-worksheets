"""
Independent re-checks of the facts the student pages rely on, using the same board
regions that gen.py draws (design-checks/instances.py).  Run: python3 verify.py
"""
import os
import sys
from collections import deque
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'design-checks'))
import tri                # noqa: E402
import lozenge as L       # noqa: E402
import instances as I     # noqa: E402
from gen import POINT_NUMBER  # noqa: E402

UP, DN = tri.UP, tri.DN
B = I.boards()
ok = True


def claim(c, msg):
    global ok
    print(('PASS ' if c else 'FAIL ') + msg)
    ok = ok and c


def greens(region, pieces=('B',)):
    return tri.min_greens(region, list(pieces))[0]


# ---------------- K-1
print('== K-1')
for k, want in [('K1-P1a', True), ('K1-P1b', False), ('K1-P1c', True), ('K1-P1d', False)]:
    n = tri.count_tilings(B[k], ['B'])
    claim((n > 0) == want, '%s blue coverings: %d' % (k, n))
for k, want in [('K1-P2a', 2), ('K1-P2b', 3), ('K1-P2c', 4)]:
    claim(greens(B[k]) == want, '%s fewest greens %d' % (k, want))
for k, copies in [('K1-P3a', 3), ('K1-P3b', 4), ('K1-P3c', 5)]:
    n = tri.count_tilings(B[k], ['B'])
    claim(n == copies - 1, '%s has %d ways; page gives %d copies (one spare)' % (k, n, copies))
for k, want in [('K1-P4a', 3), ('K1-P4b', 6), ('K1-P4c', 5)]:
    m = tri.min_pieces(B[k], ['Y', 'R', 'B', 'G'])[0]
    claim(m == want, '%s fewest blocks %d' % (k, m))
for k, piece, possible in [('K1-P5a', 'G', True), ('K1-P5b', 'R', True), ('K1-P5c', 'Y', False), ('K1-P5d', 'P', False)]:
    n = tri.count_tilings(B[k], [piece])
    claim((n > 0) == possible, '%s from %s only: %d coverings' % (k, piece, n))


def game_first_wins(cells):
    """Normal-play game: players alternately place a blue rhombus on free cells; last move wins."""
    cells = frozenset(cells)
    pls = [frozenset(p) for p in tri.placements(cells, 'B')]
    memo = {}

    def win(free):
        if free in memo:
            return memo[free]
        r = any(p <= free and not win(free - p) for p in pls)
        memo[free] = r
        return r
    return win(cells)


for k, first in [('K1-P6a', False), ('K1-P6b', True), ('K1-P6c', True)]:
    claim(game_first_wins(B[k]) == first, '%s: %s player wins' % (k, 'first' if first else 'second'))

# ---------------- grades 2-3
print('== grades 2-3')
for k, want in [('23-P1a', True), ('23-P1b', False), ('23-P1c', False), ('23-P1d', True)]:
    n = tri.count_tilings(B[k], ['B'])
    claim((n > 0) == want, '%s blue coverings: %d' % (k, n))
for k, want in [('23-P2a', 3), ('23-P2b', 4), ('23-P2c', 5), ('23-P4', 7)]:
    claim(greens(B[k]) == want, '%s fewest greens %d' % (k, want))
for k, want in [('23-P3a', True), ('23-P3b', False), ('23-P3c', True), ('23-P3d', False)]:
    n = tri.count_tilings(B[k], ['B'])
    claim((n > 0) == want, '%s blue coverings: %d' % (k, n))
for k, wb, wp in [('23-P5a', 3, 5), ('23-P5b', 4, 4), ('23-P5c', 6, 8)]:
    gb, gp = greens(B[k]), greens(B[k], ('P',))
    claim((gb, gp) == (wb, wp), '%s greens with blue %d, with purple %d' % (k, gb, gp))
for k, want in [('23-P6a', 2), ('23-P6b', 4)]:
    u, d = tri.counts(B[k])
    claim(greens(B[k]) == want and u == d, '%s: %d up = %d down, fewest greens %d' % (k, u, d, want))

# grades 2-3 Problem 7: smallest one-piece board needing at least 3 greens, by enumeration
def neighbors_all(t):
    return tri.neighbors(t)


def canon(cells):
    best = None
    cur = list(cells)
    for _ in range(6):
        for m in (False, True):
            c = [tri.reflect(t) for t in cur] if m else cur
            n = tri.normalize(c)
            if best is None or n < best:
                best = n
        cur = [tri.rot60(t) for t in cur]
    return best


shapes = {1: {canon([(0, 0, UP)])}}
for n in range(2, 8):
    nxt = set()
    for s in shapes[n - 1]:
        S = set(s)
        for t in s:
            for u in neighbors_all(t):
                if u not in S:
                    nxt.add(canon(S | {u}))
    shapes[n] = nxt
best = None
for n in range(1, 8):
    good = [s for s in shapes[n] if n - 2 * tri.max_matching(s)[0] >= 3]
    if good and best is None:
        best = (n, good)
claim(best is not None and best[0] == 7 and len(best[1]) == 1 and best[1][0] == canon(I.SMALLEST_3GAP),
      'smallest one-piece board needing 3 greens has %d triangles; %d shape(s); it is the side-3 triangle minus a corner blue'
      % (best[0], len(best[1])))

# ---------------- grades 4-5
print('== grades 4-5')
for k, abc, want in [('45-P1a', (1, 1, 1), 2), ('45-P1b', (1, 2, 1), 3), ('45-P1c', (1, 2, 2), 6),
                     ('45-P4a', (1, 3, 2), 10), ('45-P4b', (1, 3, 3), 20), ('45-P4c', (1, 4, 4), 70)]:
    n = tri.count_tilings(B[k], ['B'])
    claim(n == want and B[k] == tri.hexagon_region(*abc), '%s hexagon %s: %d ways' % (k, abc, n))
claim(tri.count_tilings(I.H222, ['B']) == 20, 'regular hexagon: 20 ways')

# the example chain picture: hexagon (1,3,1), chain R L R R from the bottom up
R131, ts131 = L.tilings(1, 3, 1)
claim(any(L.ribbons(t, 1, 3, 1) == ('RLRR',) for t in ts131), 'example (1,3,1) covering with chain RLRR exists')

# flips on the regular hexagon, named by point numbers 1-7
R, ts, idx, adj = L.flip_graph(2, 2, 2)
NUM = {v: k for k, v in POINT_NUMBER.items()}


def flip_at(T, number):
    p = NUM[number]
    for q, nt in L.flips(T, R):
        if q == p:
            return nt
    return None


def run(T, route):
    for n in route:
        T = flip_at(T, n)
        if T is None:
            return None
    return T


def dist(a, b):
    d = {a: 0}
    q = deque([a])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v] = d[u] + 1
                q.append(v)
    return d[b]


routes = {'a': [6, 7], 'b': [6, 2, 4, 5, 7, 3], 'c': [1, 6, 2, 4, 5, 7, 3, 1]}
for part, (s, t) in I.P5_PAIRS.items():
    S, Tt = I.tiling_by_words(2, 2, 2, s), I.tiling_by_words(2, 2, 2, t)
    end = run(S, routes[part])
    d = dist(idx[S], idx[Tt])
    claim(end == Tt and d == len(routes[part]), 'P5%s: route %s reaches the finish; fewest flips %d' % (part, routes[part], d))

S6 = I.tiling_by_words(2, 2, 2, I.P6_START)
possible = sorted(POINT_NUMBER[q] for q, _ in L.flips(S6, R))
claim(possible == [2, 3, 4, 5, 6, 7], 'P6 start: flips possible at points %s' % possible)
for route in ([2, 5, 2, 5], [2, 4, 2, 6, 4, 6]):
    no_repeat = all(route[i] != route[i + 1] for i in range(len(route) - 1))
    claim(run(S6, route) == S6 and no_repeat, 'P6 round trip %s returns to the start' % route)
# no odd round trip: the flip map is two-coloured
col = {idx[S6]: 0}
q = deque([idx[S6]])
bip = True
while q:
    u = q.popleft()
    for v in adj[u]:
        if v not in col:
            col[v] = 1 - col[u]
            q.append(v)
        elif col[v] == col[u]:
            bip = False
claim(bip, 'flip map of the regular hexagon is two-coloured, so no round trip has an odd number of flips')

# the key's numbering: 1 centre, 2 right, then counterclockwise
cx, cy = tri.cart((0, 2))
pos = {n: tri.cart(p) for p, n in POINT_NUMBER.items()}
claim(pos[1] == (cx, cy) and pos[2][0] > cx and abs(pos[2][1] - cy) < 1e-9 and pos[5][0] < cx,
      'key numbering: 1 centre, 2 right, 5 left')

print('ALL PAGE CHECKS PASSED' if ok else 'SOME CHECK FAILED')
