"""Checks for draft weeks 150-156 (networks and counting, second group).

Standard library only. Run: python3 plans/drafts/weeks-101-plus/check_networks_counting_2.py
Each check_week_1NN() asserts the small numbers quoted in the matching draft.
"""

import itertools
import math
from bisect import bisect_left
from collections import Counter
from fractions import Fraction


# ---------------------------------------------------------------- week 150

def canon(n, edges):
    """Smallest sorted edge list over all relabellings: a complete invariant."""
    best = None
    for p in itertools.permutations(range(n)):
        e = tuple(sorted(tuple(sorted((p[a], p[b]))) for a, b in edges))
        if best is None or e < best:
            best = e
    return best


def degrees(n, edges):
    d = [0] * n
    for a, b in edges:
        d[a] += 1
        d[b] += 1
    return sorted(d, reverse=True)


def triangles(n, edges):
    s = set(frozenset(e) for e in edges)
    return sum(1 for a, b, c in itertools.combinations(range(n), 3)
               if {frozenset((a, b)), frozenset((b, c)), frozenset((a, c))} <= s)


def all_classes(n):
    pairs = list(itertools.combinations(range(n), 2))
    seen = set()
    for mask in range(1 << len(pairs)):
        edges = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
        seen.add(canon(n, edges))
    return seen


def is_tree(n, edges):
    if len(edges) != n - 1:
        return False
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
    return True


def check_week_150():
    # Unlabelled graphs on 1..5 dots: 1, 2, 4, 11, 34 (OEIS A000088).
    assert [len(all_classes(n)) for n in range(1, 6)] == [1, 2, 4, 11, 34]
    # 4 dots: 64 labelled drawings fall into 11 families.
    assert 2 ** 6 == 64
    # Trees: 3 shapes on 5 dots, 6 on 6 dots; Cayley n^(n-2) labelled trees.
    for n, shapes in ((4, 2), (5, 3), (6, 6)):
        pairs = list(itertools.combinations(range(n), 2))
        labelled = [e for e in itertools.combinations(pairs, n - 1) if is_tree(n, e)]
        assert len(labelled) == n ** (n - 2)
        assert len({canon(n, e) for e in labelled}) == shapes
    # Same degree list (3,2,2,1,1,1), no triangles, still different:
    # spider with legs 2,2,1 versus spider with legs 3,1,1.
    legs221 = [(0, 1), (1, 2), (0, 3), (3, 4), (0, 5)]
    legs311 = [(0, 1), (1, 2), (2, 3), (0, 4), (0, 5)]
    assert degrees(6, legs221) == degrees(6, legs311) == [3, 2, 2, 1, 1, 1]
    assert canon(6, legs221) != canon(6, legs311)
    # Hexagon versus two triangles: 6 dots, 6 links, every dot has 2 links.
    hexagon = [(i, (i + 1) % 6) for i in range(6)]
    two_tri = [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5)]
    assert degrees(6, hexagon) == degrees(6, two_tri) == [2] * 6
    assert triangles(6, hexagon) == 0 and triangles(6, two_tri) == 2
    # Three houses and three wells (K3,3) versus the prism: both 9 links,
    # every dot 3 links; K3,3 has no triangle, the prism has 2.
    k33 = [(a, b) for a in range(3) for b in range(3, 6)]
    prism = [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5), (0, 3), (1, 4), (2, 5)]
    assert degrees(6, k33) == degrees(6, prism) == [3] * 6
    assert triangles(6, k33) == 0 and triangles(6, prism) == 2
    # Two drawings that look different but are the same: a pentagon and a
    # five-pointed star (each dot joined to the dots two steps away).
    pent = [(i, (i + 1) % 5) for i in range(5)]
    star = [(i, (i + 2) % 5) for i in range(5)]
    assert canon(5, pent) == canon(5, star)
    # Equal invariants that still differ, with connected networks and the same
    # triangle count: two 3-regular networks on 8 dots with no triangles
    # (the cube, and an 8-ring with its 4 diameters, the Mobius ladder).
    cube = [(a, b) for a in range(8) for b in range(8)
            if a < b and bin(a ^ b).count("1") == 1]
    ring8 = [(i, (i + 1) % 8) for i in range(8)] + [(i, i + 4) for i in range(4)]
    assert degrees(8, cube) == degrees(8, ring8) == [3] * 8
    assert triangles(8, cube) == triangles(8, ring8) == 0
    # They differ: the cube has 6 four-cycles, the ring with diameters has 4.
    def four_cycles(n, edges):
        s = set(frozenset(e) for e in edges)
        count = 0
        for a, b, c, d in itertools.permutations(range(n), 4):
            if a == min(a, b, c, d) and b < d:
                if all(frozenset(p) in s for p in ((a, b), (b, c), (c, d), (d, a))):
                    count += 1
        return count
    assert four_cycles(8, cube) == 6 and four_cycles(8, ring8) == 4
    # Renamings to try: 5! = 120 for five beads, 6! = 720 for six.
    assert math.factorial(5) == 120 and math.factorial(6) == 720
    print("ok week 150")


# ---------------------------------------------------------------- week 151

# Faces: 0 top, 1 bottom, 2 front, 3 back, 4 left, 5 right.
def rotations():
    def turn_x(c):   # top -> front -> bottom -> back
        t, b, f, k, l, r = c
        return (k, f, t, b, l, r)

    def turn_z(c):   # front -> right -> back -> left about the vertical
        t, b, f, k, l, r = c
        return (t, b, l, r, k, f)

    def turn_y(c):   # top -> right -> bottom -> left
        t, b, f, k, l, r = c
        return (l, r, f, k, b, t)
    start = tuple(range(6))
    seen, todo = {start}, [start]
    while todo:
        c = todo.pop()
        for g in (turn_x, turn_y, turn_z):
            d = g(c)
            if d not in seen:
                seen.add(d)
                todo.append(d)
    return sorted(seen)


def cube_from_pairs(pairs):
    (a, b), (c, d), (e, f) = pairs
    return (a, b, c, d, e, f)


def tower_solutions(cubes):
    rots = rotations()
    orients = [sorted({tuple(cube[i] for i in r) for r in rots}) for cube in cubes]
    colours = set(itertools.chain(*cubes))
    sols = 0
    for combo in itertools.product(*[[r for r in rots] for _ in cubes]):
        ok = True
        for side in (2, 3, 4, 5):
            if {cubes[i][combo[i][side]] for i in range(len(cubes))} != colours:
                ok = False
                break
        if ok:
            sols += 1
    return sols, orients


def graph_pairs(cubes):
    """Pairs of edge-disjoint 'one link per cube, every colour twice' subgraphs."""
    k = len(cubes)
    colours = sorted(set(itertools.chain(*cubes)))
    opp = [[(c[0], c[1]), (c[2], c[3]), (c[4], c[5])] for c in cubes]
    factors = []
    for choice in itertools.product(range(3), repeat=k):
        deg = Counter()
        for i, j in enumerate(choice):
            a, b = opp[i][j]
            deg[a] += 1
            deg[b] += 1
        if all(deg[c] == 2 for c in colours):
            factors.append(choice)
    pairs = [(f, g) for f, g in itertools.combinations(factors, 2)
             if all(x != y for x, y in zip(f, g))]
    return factors, pairs


def check_week_151():
    rots = rotations()
    assert len(rots) == 24
    # Jaap's Puzzle Page cubes, as opposite-face pairs (top/bottom, two side pairs).
    R, G, B, Y = "RGBY"
    jaap = [
        cube_from_pairs([(B, Y), (R, R), (R, G)]),
        cube_from_pairs([(R, B), (G, G), (Y, B)]),
        cube_from_pairs([(R, Y), (B, R), (G, Y)]),
        cube_from_pairs([(G, Y), (B, Y), (R, G)]),
    ]
    counts = Counter(itertools.chain(*jaap))
    assert sum(counts.values()) == 24 and set(counts) == set("RGBY")
    assert counts == Counter({"R": 7, "G": 6, "Y": 6, "B": 5})
    sols, _ = tower_solutions(jaap)
    # The tower can be turned 4 ways about its axis and flipped over: 8 copies.
    assert sols == 8
    # Positions: 24^4 / 8 = 41472 (turning or flipping the whole tower).
    assert 24 ** 4 // 8 == 41472
    factors, pairs = graph_pairs(jaap)
    assert len(factors) == 3 and len(pairs) == 1
    # A ladder of goals over all 24^4 = 331776 placements: front only 33280,
    # front and back 1536, three sides 172, all four sides 8.
    ladder = []
    for sides in ((2,), (2, 3), (2, 3, 4), (2, 3, 4, 5)):
        n = 0
        for combo in itertools.product(rots, repeat=4):
            if all({jaap[i][combo[i][sd]] for i in range(4)} == set("RGBY") for sd in sides):
                n += 1
        ladder.append(n)
    assert ladder == [33280, 1536, 172, 8] and 24 ** 4 == 331776
    # Brute force over 3^4 = 81 choices of a vertical pair per cube is the whole
    # graph search: one link per cube means choosing one opposite pair.
    assert 3 ** 4 == 81
    # Warm-up: three cubes, three colours, every side shows all three.
    a, b, c = "abc"
    warm = [
        cube_from_pairs([(a, b), (b, c), (c, a)]),
        cube_from_pairs([(a, a), (b, c), (a, c)]),
        cube_from_pairs([(b, b), (a, c), (a, b)]),
    ]
    wsols, _ = tower_solutions(warm)
    wf, wp = graph_pairs(warm)
    # 24 towers, which is 3 up to turning and flipping the tower; the graph has
    # 4 'every colour twice' choices and 2 disjoint pairs of them.
    assert (wsols, len(wf), len(wp)) == (24, 4, 2) and wsols // 8 == 3
    # A four-cube set with no solution: cube 1 has one colour on 4 faces.
    bad = [cube_from_pairs([(R, R), (R, R), (G, B)])] + jaap[1:]
    bsols, _ = tower_solutions(bad)
    assert bsols == 0
    print("ok week 151", "warm-up solutions", wsols, "factors", len(wf), "pairs", len(wp))


# ---------------------------------------------------------------- week 152

def stationary(links, n, jump=Fraction(0)):
    """Exact long-run fractions for: with prob jump go to a uniform page,
    otherwise follow a uniformly chosen out-link. Solve by Gaussian elimination."""
    P = [[Fraction(0)] * n for _ in range(n)]
    for i in range(n):
        out = links[i]
        for j in range(n):
            P[i][j] += jump / n
        for j in out:
            P[i][j] += (1 - jump) / len(out)
    # Solve x P = x, sum x = 1.
    A = [[P[j][i] - (1 if i == j else 0) for j in range(n)] for i in range(n)]
    A[-1] = [Fraction(1)] * n
    rhs = [Fraction(0)] * (n - 1) + [Fraction(1)]
    M = [row + [r] for row, r in zip(A, rhs)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [v / pv for v in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return [M[i][n] for i in range(n)]


DICE152 = [0.288, 0.148, 0.238, 0.148, 0.089, 0.089]


def check_week_152():
    # Bryan and Leise's four-page web: 1->2,3,4; 2->3,4; 3->1; 4->1,3.
    web = {0: [1, 2, 3], 1: [2, 3], 2: [0], 3: [0, 2]}
    x = stationary(web, 4)
    assert x == [Fraction(12, 31), Fraction(4, 31), Fraction(9, 31), Fraction(6, 31)]
    assert [round(float(v), 3) for v in x] == [0.387, 0.129, 0.290, 0.194]
    xd = stationary(web, 4, Fraction(15, 100))
    assert [round(float(v), 3) for v in xd] == [0.368, 0.142, 0.288, 0.202]
    # Page 3 has the most incoming links (3) but ranks second.
    indeg = Counter(j for i in web for j in web[i])
    assert indeg[2] == 3 and max(indeg.values()) == 3
    assert sorted(range(4), key=lambda i: -x[i]) == [0, 2, 3, 1]
    # Six-chair room A..F (0..5): A->B,D; B->A,C; C->A; D->E,F; E->C; F->C.
    # Every chair has one or two arrows, so a coin chooses at a fork.
    room = {0: [1, 3], 1: [0, 2], 2: [0], 3: [4, 5], 4: [2], 5: [2]}
    indeg = Counter(j for i in room for j in room[i])
    assert [indeg[i] for i in range(6)] == [2, 1, 3, 1, 1, 1]
    assert sum(len(v) for v in room.values()) == 9
    plain = stationary(room, 6)
    assert plain == [Fraction(4, 13), Fraction(2, 13), Fraction(3, 13),
                     Fraction(2, 13), Fraction(1, 13), Fraction(1, 13)]
    # C has the most arrows in, but A is visited most (C sends all its visits to A).
    assert max(range(6), key=lambda i: indeg[i]) == 2
    assert max(range(6), key=lambda i: plain[i]) == 0
    # 26 steps: expected visits 8, 4, 6, 4, 2, 2.
    assert [26 * v for v in plain] == [8, 4, 6, 4, 2, 2]
    # Loops of length 2 (A-B-A) and 3 (A-B-C-A): the walk does not alternate.
    assert math.gcd(2, 3) == 1
    # With a die: on a 6, roll again and jump to that chair; else follow arrows.
    dice = stationary(room, 6, Fraction(1, 6))
    assert sum(dice) == 1 and all(v > 0 for v in dice)
    assert sorted(range(6), key=lambda i: -dice[i])[:2] == [0, 2]
    assert [round(float(v), 3) for v in dice] == DICE152
    # A trap: if E and F only pointed at each other, without the die the walker
    # would end up there for good; with the die they still hold most visits.
    trap = {0: [1, 3], 1: [0, 2], 2: [0], 3: [4, 5], 4: [5], 5: [4]}
    t = stationary(trap, 6, Fraction(1, 6))
    assert t[4] + t[5] > Fraction(1, 2)
    TRAP152 = round(float(t[4] + t[5]), 3)
    # Week 91 link: replace coins by rotor cards (each fork alternates, starting
    # with its first arrow, walker starts at A). Every block of 13 steps visits
    # A, B, C, D, E, F exactly 4, 2, 3, 2, 1, 1 times: the random walk's fractions.
    ptr, x, counts = [0] * 6, 0, [0] * 6
    for step in range(1, 1301):
        counts[x] += 1
        nxt = room[x][ptr[x]]
        ptr[x] = (ptr[x] + 1) % len(room[x])
        x = nxt
        if step % 13 == 0:
            assert counts == [step // 13 * v for v in (4, 2, 3, 2, 1, 1)]
    print("ok week 152", [round(float(v), 3) for v in dice], TRAP152)


# ---------------------------------------------------------------- week 153

def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def weiszfeld(pts, steps=5000):
    x = (sum(p[0] for p in pts) / 3, sum(p[1] for p in pts) / 3)
    for _ in range(steps):
        ws = []
        for p in pts:
            d = dist(x, p)
            if d < 1e-12:
                return p
            ws.append((p, 1 / d))
        s = sum(w for _, w in ws)
        x = (sum(p[0] * w for p, w in ws) / s, sum(p[1] * w for p, w in ws) / s)
    return x


def angle_at(x, p, q):
    v = (p[0] - x[0], p[1] - x[1])
    w = (q[0] - x[0], q[1] - x[1])
    c = (v[0] * w[0] + v[1] * w[1]) / (math.hypot(*v) * math.hypot(*w))
    return math.degrees(math.acos(max(-1, min(1, c))))


def mst_length(pts):
    n = len(pts)
    inside = {0}
    total = 0.0
    while len(inside) < n:
        d, j = min((dist(pts[i], pts[j]), j) for i in inside for j in range(n) if j not in inside)
        inside.add(j)
        total += d
    return total


def best_two_junction(pts, pairing):
    """Numerically minimise |a s| + |b s| + |s t| + |c t| + |d t| over s, t."""
    (a, b), (c, d) = pairing
    s = ((pts[a][0] + pts[b][0]) / 2, (pts[a][1] + pts[b][1]) / 2)
    t = ((pts[c][0] + pts[d][0]) / 2, (pts[c][1] + pts[d][1]) / 2)

    def L(s, t):
        return dist(pts[a], s) + dist(pts[b], s) + dist(s, t) + dist(pts[c], t) + dist(pts[d], t)
    h = 0.25
    cur = L(s, t)
    while h > 1e-9:
        improved = False
        for which in (0, 1):
            for dx, dy in ((h, 0), (-h, 0), (0, h), (0, -h)):
                ns = (s[0] + dx, s[1] + dy) if which == 0 else s
                nt = (t[0] + dx, t[1] + dy) if which == 1 else t
                v = L(ns, nt)
                if v < cur - 1e-15:
                    s, t, cur, improved = ns, nt, v, True
        if not improved:
            h /= 2
    return cur, s, t


def check_week_153():
    r3 = math.sqrt(3)
    # Equilateral triangle side 1: two sides 2, Fermat point network sqrt3.
    tri = [(0, 0), (1, 0), (0.5, r3 / 2)]
    f = weiszfeld(tri)
    L = sum(dist(f, p) for p in tri)
    assert abs(L - r3) < 1e-9 and abs(mst_length(tri) - 2) < 1e-12
    assert round(r3 / 2, 3) == 0.866
    # A lopsided triangle (0,0), (4,0), (1,3): junction angles all 120 degrees.
    t2 = [(0, 0), (4, 0), (1, 3)]
    f2 = weiszfeld(t2)
    for i, j in ((0, 1), (1, 2), (0, 2)):
        assert abs(angle_at(f2, t2[i], t2[j]) - 120) < 1e-6
    saved = mst_length(t2) - sum(dist(f2, p) for p in t2)
    assert saved > 0
    # A flat triangle with a 120-degree-or-more corner: the best junction is the corner.
    flat = [(0, 0), (6, 0), (3, 1)]
    assert angle_at(flat[2], flat[0], flat[1]) > 120
    f3 = weiszfeld(flat)
    assert dist(f3, flat[2]) < 1e-6
    # Unit square: spanning tree 3, two diagonals 2*sqrt2 = 2.828, best 1 + sqrt3 = 2.732.
    sq = [(0, 0), (1, 0), (1, 1), (0, 1)]
    assert abs(mst_length(sq) - 3) < 1e-12
    assert round(2 * math.sqrt(2), 3) == 2.828
    best, s, t = best_two_junction(sq, ((0, 3), (1, 2)))
    assert abs(best - (1 + r3)) < 1e-6 and round(1 + r3, 3) == 2.732
    for (x, p, q) in ((s, sq[0], sq[3]), (s, sq[0], t), (t, sq[1], sq[2])):
        assert abs(angle_at(x, p, q) - 120) < 1e-3
    # Two optimal trees (pair left-right or top-bottom), same length.
    best2, _, _ = best_two_junction(sq, ((0, 1), (3, 2)))
    assert abs(best - best2) < 1e-6
    # Ratio for the square: (1 + sqrt3)/3 = 0.911, above sqrt3/2.
    assert round((1 + r3) / 3, 3) == 0.911
    # 2-by-1 rectangle: 2 + sqrt3 = 3.732 against spanning tree 4.
    rect = [(0, 0), (2, 0), (2, 1), (0, 1)]
    b3, _, _ = best_two_junction(rect, ((0, 3), (1, 2)))
    assert abs(b3 - (2 + r3)) < 1e-6 and abs(mst_length(rect) - 4) < 1e-12
    b4, _, _ = best_two_junction(rect, ((0, 1), (3, 2)))
    assert b4 > b3 + 0.1   # pairing the long sides is worse
    # Ratio bounds quoted: Chung-Graham 0.824 < 0.8559 (2026 preprint) < 0.866.
    assert 0.824 < 0.8559 < r3 / 2
    print("ok week 153", round(saved, 3), round(b4, 3))


# ---------------------------------------------------------------- week 154

def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def bulgarian(p):
    q = [x - 1 for x in p if x > 1] + [len(p)]
    return tuple(sorted(q, reverse=True))


def cycles_of(n):
    found = set()
    for p in partitions(n):
        seen = []
        x = p
        while x not in seen:
            seen.append(x)
            x = bulgarian(x)
        cyc = seen[seen.index(x):]
        found.add(frozenset(cyc))
    return found


def necklaces(k, r):
    total = 0
    for d in range(1, math.gcd(r, k) + 1):
        if r % d == 0 and k % d == 0:
            phi = sum(1 for i in range(1, d + 1) if math.gcd(i, d) == 1)
            total += phi * math.comb(k // d, r // d)
    return total // k


def check_week_154():
    assert [sum(1 for _ in partitions(n)) for n in (6, 10, 15)] == [11, 42, 176]
    # Example run from 6 in one pile.
    run = [(6,)]
    while bulgarian(run[-1]) != run[-1]:
        run.append(bulgarian(run[-1]))
    assert run == [(6,), (5, 1), (4, 2), (3, 2, 1)]
    # Triangular totals: every start reaches the staircase in at most k(k-1)
    # moves, and some start needs exactly k(k-1) (checked k = 1..7).
    for k in range(1, 8):
        n = k * (k + 1) // 2
        stair = tuple(range(k, 0, -1))
        worst = 0
        for p in partitions(n):
            steps = 0
            while p != stair:
                p = bulgarian(p)
                steps += 1
            worst = max(worst, steps)
        assert worst == k * (k - 1), (k, worst)
    # 6 cards: worst start 2+2+1+1 needs 6 moves; 10 cards: 3+3+2+1+1 needs 12.
    def moves(p, stair):
        c = 0
        while p != stair:
            p, c = bulgarian(p), c + 1
        return c
    assert moves((2, 2, 1, 1), (3, 2, 1)) == 6 and moves((6,), (3, 2, 1)) == 3
    assert moves((3, 3, 2, 1, 1), (4, 3, 2, 1)) == 12
    # Non-triangular totals end in a cycle. Totals 1..20: the number of cycles
    # matches the necklace count, and cycle lengths divide k.
    for n in range(1, 21):
        k = 1
        while k * (k + 1) // 2 < n:
            k += 1
        r = n - (k - 1) * k // 2   # 0 < r <= k
        cyc = cycles_of(n)
        assert len(cyc) == necklaces(k, r), (n, len(cyc))
        for c in cyc:
            assert k % len(c) == 0
    # 4 cards: one cycle of 3 shapes, 3+1 -> 2+2 -> 2+1+1 -> 3+1.
    assert cycles_of(4) == {frozenset({(3, 1), (2, 2), (2, 1, 1)})}
    # 8 cards (k = 4, r = 2): two cycles, lengths 4 and 2.
    assert sorted(len(c) for c in cycles_of(8)) == [2, 4]
    # Shapes no move can produce (more piles than the largest pile + 1):
    # count for 6 cards.
    image6 = {bulgarian(p) for p in partitions(6)}
    eden6 = [p for p in partitions(6) if p not in image6]
    assert len(eden6) == 11 - len(image6)
    assert sorted(eden6) == [(1, 1, 1, 1, 1, 1), (2, 1, 1, 1, 1), (2, 2, 1, 1)]
    EDEN6 = len(eden6)
    print("ok week 154", "unreachable shapes of 6:", EDEN6)


# ---------------------------------------------------------------- week 155

def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_div(num, den):
    num = num[:]
    q = [0] * (len(num) - len(den) + 1)
    for i in range(len(q) - 1, -1, -1):
        c = num[i + len(den) - 1] // den[-1]
        if c * den[-1] != num[i + len(den) - 1]:
            return None
        q[i] = c
        for j, d in enumerate(den):
            num[i + j] -= c * d
    if any(num):
        return None
    return q


def die_poly(faces):
    p = [0] * (max(faces) + 1)
    for f in faces:
        p[f] += 1
    return p


def other_dice(sides):
    std = die_poly(range(1, sides + 1))
    target = poly_mul(std, std)
    maxface = 2 * sides - 1
    found = set()
    for rest in itertools.combinations_with_replacement(range(2, maxface + 1), sides - 1):
        a = (1,) + rest
        q = poly_div(target, die_poly(a))
        if q is None or any(c < 0 for c in q) or q[0] != 0 or sum(q) != sides:
            continue
        b = tuple(i for i, c in enumerate(q) for _ in range(c))
        found.add(tuple(sorted((a, b))))
    return found


def check_week_155():
    std = tuple(range(1, 7))
    sich_a, sich_b = (1, 2, 2, 3, 3, 4), (1, 3, 4, 5, 6, 8)
    def sums(a, b):
        return Counter(x + y for x in a for y in b)
    ordinary = sums(std, std)
    assert ordinary == sums(sich_a, sich_b)
    assert [ordinary[s] for s in range(2, 13)] == [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    assert sum(ordinary.values()) == 36
    # Only two pairs of positive six-sided dice give this: ordinary and Sicherman.
    assert other_dice(6) == {(std, std), (sich_a, sich_b)}
    # Four-sided: ordinary and {1,2,2,3} with {1,3,3,5}.
    assert other_dice(4) == {((1, 2, 3, 4), (1, 2, 3, 4)), ((1, 2, 2, 3), (1, 3, 3, 5))}
    # Factorisation x + ... + x^6 = x (1 + x)(1 + x + x^2)(1 - x + x^2).
    f = poly_mul(poly_mul([0, 1], [1, 1]), poly_mul([1, 1, 1], [1, -1, 1]))
    assert f == [0, 1, 1, 1, 1, 1, 1]
    # Sicherman dice: x(1+x)(1+x+x^2) and x(1+x)(1+x+x^2)(1-x+x^2)^2.
    a = poly_mul(poly_mul([0, 1], [1, 1]), [1, 1, 1])
    b = poly_mul(a, poly_mul([1, -1, 1], [1, -1, 1]))
    assert a == die_poly(sich_a) and b == die_poly(sich_b)
    # Shifting: {0,1,1,2,2,3} with {2,4,5,6,7,9} also matches (zero allowed).
    assert sums((0, 1, 1, 2, 2, 3), (2, 4, 5, 6, 7, 9)) == ordinary
    # Sicherman faces total 15 and 27; ordinary faces 21 each (42 = 15 + 27).
    assert sum(sich_a) == 15 and sum(sich_b) == 27 and 2 * sum(std) == 42
    # Doubles differ: 4 of 36 rolls show the same face twice, against 6 for ordinary dice.
    doubles = sum(1 for x in sich_a for y in sich_b if x == y)
    assert doubles == 4 and sum(1 for x in std for y in std if x == y) == 6
    # Ordinary die with 0,0,0,6,6,6: totals 1..12 each 3 of 36.
    uni = sums(std, (0, 0, 0, 6, 6, 6))
    assert sorted(uni) == list(range(1, 13)) and set(uni.values()) == {3}
    # Three-sided "dice" (1,2,3): only ordinary works.
    assert other_dice(3) == {((1, 2, 3), (1, 2, 3))}
    print("ok week 155")


# ---------------------------------------------------------------- week 156

def lis(seq):
    piles = []
    for x in seq:
        i = bisect_left(piles, x)
        if i == len(piles):
            piles.append(x)
        else:
            piles[i] = x
    return len(piles)


def lds(seq):
    return lis([-x for x in seq])


def lis_brute(seq):
    n = len(seq)
    best = 0
    for mask in range(1, 1 << n):
        sub = [seq[i] for i in range(n) if mask >> i & 1]
        if all(a < b for a, b in zip(sub, sub[1:])):
            best = max(best, len(sub))
    return best


def patience_piles(seq):
    """Greedy patience: put each card on the leftmost pile whose top is higher."""
    tops = []
    for x in seq:
        for i, t in enumerate(tops):
            if t > x:
                tops[i] = x
                break
        else:
            tops.append(x)
    return len(tops)


def check_week_156():
    # Patience piles = longest increasing run (skipping allowed), all orders of 7.
    for p in itertools.permutations(range(1, 8)):
        assert patience_piles(p) == lis(p)
    for p in itertools.permutations(range(1, 7)):
        assert lis(p) == lis_brute(p)
    # Each patience pile, in the order dealt, is a down-run; so 5 cards make
    # 3 piles or a pile of 3 (the card-pile proof of the theorem for n = 2).
    def piles_of(seq):
        piles = []
        for x in seq:
            for pl in piles:
                if pl[-1] > x:
                    pl.append(x)
                    break
            else:
                piles.append([x])
        return piles
    for p in itertools.permutations(range(5)):
        pl = piles_of(p)
        assert all(all(a > b for a, b in zip(q, q[1:])) for q in pl)
        assert len(pl) >= 3 or max(len(q) for q in pl) >= 3
    # 5 people: always an up or down run of 3. 4 people: 4 orders avoid it.
    assert all(max(lis(p), lds(p)) >= 3 for p in itertools.permutations(range(5)))
    avoid4 = [p for p in itertools.permutations(range(1, 5)) if lis(p) < 3 and lds(p) < 3]
    assert sorted(avoid4) == [(2, 1, 4, 3), (2, 4, 1, 3), (3, 1, 4, 2), (3, 4, 1, 2)]
    # 9 people: 1764 = 42^2 orders avoid an up or down run of 4.
    count9 = sum(1 for p in itertools.permutations(range(9)) if lis(p) <= 3 and lds(p) <= 3)
    assert count9 == 1764 == 42 ** 2
    # Hook length formula: 3-by-3 standard Young tableaux 9!/(5*4*3*4*3*2*3*2*1) = 42,
    # 2-by-2: 4!/(3*2*2*1) = 2, matching 42^2 and the 4 = 2^2 orders of 4.
    assert math.factorial(9) // (5 * 4 * 3 * 4 * 3 * 2 * 3 * 2 * 1) == 42
    assert math.factorial(4) // (3 * 2 * 2 * 1) == 2
    assert lis((3, 2, 1, 6, 5, 4, 9, 8, 7)) == 3 and lds((3, 2, 1, 6, 5, 4, 9, 8, 7)) == 3
    # The pair labels (longest up ending here, longest down ending here) differ
    # for every two people, in every order of 6.
    for p in itertools.permutations(range(6)):
        labels = []
        for i in range(6):
            up = 1 + max([lab[0] for j, lab in enumerate(labels) if p[j] < p[i]], default=0)
            dn = 1 + max([lab[1] for j, lab in enumerate(labels) if p[j] > p[i]], default=0)
            labels.append((up, dn))
        assert len(set(labels)) == 6
    # Average longest up-run over all orders of 8: exact fraction.
    total = sum(lis(p) for p in itertools.permutations(range(8)))
    avg8 = Fraction(total, math.factorial(8))
    assert avg8 == Fraction(7601, 2016) and round(float(avg8), 2) == 3.77
    # 2 * sqrt(n) is only the large-n rate: for 8 it gives 5.66, well above 3.77.
    assert round(2 * math.sqrt(8), 2) == 5.66
    # Orders of 5 with no up-run of 3: Catalan(5) = 42.
    assert sum(1 for p in itertools.permutations(range(5)) if lis(p) <= 2) == 42
    print("ok week 156", "average longest up-run of 8:", round(float(avg8), 3))


def main():
    check_week_150()
    check_week_151()
    check_week_152()
    check_week_153()
    check_week_154()
    check_week_155()
    check_week_156()


if __name__ == "__main__":
    main()
