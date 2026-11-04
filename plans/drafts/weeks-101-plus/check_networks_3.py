"""Checks for draft weeks 182-188 (networks group 3).

Standard library only. Run: python3 plans/drafts/weeks-101-plus/check_networks_3.py
Each check_week_1NN() asserts the small numbers quoted in the matching draft.
"""

import itertools
import random
from collections import Counter, deque
from fractions import Fraction
from math import comb, factorial


# ---------------------------------------------------------------- helpers

def all_graphs(n):
    """Yield (edges) for every simple graph on vertices 0..n-1."""
    pairs = list(itertools.combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        yield [pairs[i] for i in range(len(pairs)) if mask >> i & 1]


def adjacency(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def connected(n, edges, removed=None):
    adj = [set() for _ in range(n)]
    for e in edges:
        if e is removed:
            continue
        a, b = e
        adj[a].add(b)
        adj[b].add(a)
    seen, stack = {0}, [0]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == n


def distances_from(adj, s):
    dist = {s: 0}
    q = deque([s])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if w not in dist:
                dist[w] = dist[v] + 1
                q.append(w)
    return dist


# ---------------------------------------------------------------- week 182

def gossip_done(n, calls):
    know = [1 << i for i in range(n)]
    for a, b in calls:
        know[a] = know[b] = know[a] | know[b]
    return all(k == (1 << n) - 1 for k in know)


def gossip_min_calls(n, limit):
    """Breadth-first search over multisets of knowledge (people are interchangeable)."""
    full = (1 << n) - 1
    start = tuple(sorted(1 << i for i in range(n)))
    frontier, seen = {start}, {start}
    for depth in range(limit + 1):
        if any(all(k == full for k in s) for s in frontier):
            return depth
        nxt = set()
        for s in frontier:
            for i, j in itertools.combinations(range(n), 2):
                if s[i] == s[j]:
                    continue  # a call between equal knowers changes nothing
                t = list(s)
                t[i] = t[j] = s[i] | s[j]
                t = tuple(sorted(t))
                if t not in seen:
                    seen.add(t)
                    nxt.add(t)
        frontier = nxt
    return None


def scheme_2n_minus_4(n):
    # Baker and Shostak: four chiefs 0..3; others call chief 0 first and last.
    others = list(range(4, n))
    return [(0, x) for x in others] + [(0, 1), (2, 3), (0, 2), (1, 3)] + [(0, x) for x in others]


def check_week_182():
    # Fewest calls: 1, 3, 4, 6, 8 for 2, 3, 4, 5, 6 people (exhaustive search).
    assert [gossip_min_calls(n, 2 * n) for n in (2, 3, 4, 5, 6)] == [1, 3, 4, 6, 8]
    # The 2n - 4 scheme works for 4 to 14 people.
    for n in range(4, 15):
        s = scheme_2n_minus_4(n)
        assert len(s) == 2 * n - 4 and gossip_done(n, s)
    # Four friends: AB, CD, AC, BD works; 3 calls never do (all 6^3 orders tried).
    assert gossip_done(4, [(0, 1), (2, 3), (0, 2), (1, 3)])
    pairs4 = list(itertools.combinations(range(4), 2))
    assert not any(gossip_done(4, c) for c in itertools.product(pairs4, repeat=3))
    # Of the 6^4 = 1296 four-call lists, 24 work.
    works4 = sum(gossip_done(4, c) for c in itertools.product(pairs4, repeat=4))
    assert len(pairs4) ** 4 == 1296 and works4 == 24
    # Hub method (collect, then send back): n - 1 + n - 2 = 2n - 3 calls.
    for n in range(3, 12):
        hub = [(0, x) for x in range(1, n)] + [(0, x) for x in range(1, n - 1)]
        assert len(hub) == 2 * n - 3 and gossip_done(n, hub)
    # Everyone calls everyone: C(n, 2) calls; 28 for 8 people against 12.
    assert comb(8, 2) == 28 and 2 * 8 - 4 == 12
    # Five people: 6 calls; a hub needs 7.
    assert gossip_min_calls(5, 10) == 6 and 2 * 5 - 3 == 7
    # Cheap first lower bound: someone first knows everything after at least n - 1 calls.
    for n in (3, 4, 5):
        pairs = list(itertools.combinations(range(n), 2))
        for c in itertools.product(pairs, repeat=n - 2):
            know = [1 << i for i in range(n)]
            for a, b in c:
                know[a] = know[b] = know[a] | know[b]
            assert max(bin(k).count("1") for k in know) <= n - 1
    # The children's bound: (n - 1) calls before anyone knows everything, then the other
    # n - 2 people need ceil((n - 2) / 2) more calls. It is exact for 4 and 5 people
    # (4 and 6) but one short for 6 people (7 against the true 8).
    bound = lambda n: (n - 1) + (n - 1) // 2
    assert [bound(n) for n in (4, 5, 6)] == [4, 6, 7]
    assert [gossip_min_calls(n, 2 * n) for n in (4, 5, 6)] == [4, 6, 8]
    print("ok week 182")


# ---------------------------------------------------------------- week 183

def max_matching(rows, n_cols):
    """rows[i] = set of acceptable columns. Augmenting paths."""
    match_col = [-1] * n_cols

    def try_row(r, seen):
        for c in rows[r]:
            if c not in seen:
                seen.add(c)
                if match_col[c] == -1 or try_row(match_col[c], seen):
                    match_col[c] = r
                    return True
        return False

    return sum(try_row(r, set()) for r in range(len(rows)))


def hall_ok(rows):
    n = len(rows)
    for k in range(1, n + 1):
        for group in itertools.combinations(range(n), k):
            if len(set().union(*(rows[i] for i in group))) < k:
                return False
    return True


def min_line_cover(rows, n_cols):
    n = len(rows)
    best = n + n_cols
    for rmask in range(1 << n):
        cols_needed = set()
        for r in range(n):
            if not rmask >> r & 1:
                cols_needed |= rows[r]
        best = min(best, bin(rmask).count("1") + len(cols_needed))
    return best


def tables(n):
    cells = [(r, c) for r in range(n) for c in range(n)]
    for mask in range(1 << (n * n)):
        rows = [set() for _ in range(n)]
        for i, (r, c) in enumerate(cells):
            if mask >> i & 1:
                rows[r].add(c)
        yield rows


def check_week_183():
    # Hall: a full pairing exists exactly when every group accepts at least as many partners
    # as it has members. Exhaustive on all 3-by-3 (512) and 4-by-4 (65,536) tables.
    full3 = full4 = 0
    for rows in tables(3):
        m = max_matching(rows, 3)
        assert (m == 3) == hall_ok(rows)
        assert m == min_line_cover(rows, 3)  # Konig on every 3-by-3 table
        full3 += m == 3
    for rows in tables(4):
        ok = max_matching(rows, 4) == 4
        assert ok == hall_ok(rows)
        full4 += ok
    assert full3 == 247 and full4 == 37823
    # Konig on 2,000 random 5-by-5 tables: most rooks = fewest lines.
    rng = random.Random(183)
    for _ in range(2000):
        rows = [{c for c in range(5) if rng.random() < 0.4} for _ in range(5)]
        assert max_matching(rows, 5) == min_line_cover(rows, 5)
    # The five-child example: A {1,2}, B {2}, C {1,2}, D {3,4,5}, E {3}.
    ex = [{0, 1}, {1}, {0, 1}, {2, 3, 4}, {2}]
    assert not hall_ok(ex) and max_matching(ex, 5) == 4 and min_line_cover(ex, 5) == 4
    # The blocking group is A, B, C (3 children, 2 partners); no group of 2 or fewer blocks.
    blocking = [g for k in range(1, 6) for g in itertools.combinations(range(5), k)
                if len(set().union(*(ex[i] for i in g))) < k]
    assert min(blocking, key=len) == (0, 1, 2) and min(len(g) for g in blocking) == 3
    # Fix it: let C also accept 4 -> full pairing.
    fixed = [{0, 1}, {1}, {0, 1, 3}, {2, 3, 4}, {2}]
    assert hall_ok(fixed) and max_matching(fixed, 5) == 5
    # Every table where each child accepts exactly k and each partner is accepted by
    # exactly k (k >= 1) has a full pairing (checked on all 4-by-4 tables).
    for rows in tables(4):
        degs = [len(r) for r in rows]
        cols = Counter(c for r in rows for c in r)
        if degs[0] >= 1 and len(set(degs)) == 1 and all(cols[c] == degs[0] for c in range(4)):
            assert max_matching(rows, 4) == 4
    print("ok week 183")


# ---------------------------------------------------------------- week 184

def friend_stats(n, edges):
    adj = adjacency(n, edges)
    k = [len(a) for a in adj]
    people_avg = Fraction(sum(k), n)
    notes_avg = Fraction(sum(x * x for x in k), sum(k))  # each person writes k on k notes
    fewer = sum(1 for v in range(n) if k[v] and Fraction(sum(k[w] for w in adj[v]), k[v]) > k[v])
    return k, people_avg, notes_avg, fewer


def check_week_184():
    # Star of five: hub 4 friends, others 1. Average 8/5; notes average 20/8 = 5/2.
    star = [(0, i) for i in range(1, 5)]
    k, pa, na, fewer = friend_stats(5, star)
    assert pa == Fraction(8, 5) and na == Fraction(5, 2) and fewer == 4
    # The eight-child yarn network in the plan (A..H = 0..7).
    net = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (3, 4), (4, 5), (5, 6), (6, 7), (0, 5)]
    k, pa, na, fewer = friend_stats(8, net)
    assert k == [5, 2, 2, 2, 3, 3, 2, 1]
    assert sum(k) == 20 and pa == Fraction(5, 2)
    assert sum(x * x for x in k) == 60 and na == 3
    assert fewer == 6  # six of eight children have fewer friends than their friends' average
    # A ring of six: everyone has 2; both averages 2 (equality).
    ring = [(i, (i + 1) % 6) for i in range(6)]
    k, pa, na, fewer = friend_stats(6, ring)
    assert pa == na == 2 and fewer == 0
    # Every graph on up to 6 people with at least one friendship: notes average >= people
    # average, equal exactly when everyone has the same number of friends.
    for n in range(2, 7):
        for edges in all_graphs(n):
            if not edges:
                continue
            k, pa, na, _ = friend_stats(n, edges)
            assert na >= pa
            assert (na == pa) == (len(set(k)) == 1)
            # Sum-of-squares form: n * sum(k^2) >= (sum k)^2.
            assert n * sum(x * x for x in k) >= sum(k) ** 2
    # Per-person version (no one friendless): average over people of
    # (friends' average - own count) >= 0, since each friendship adds a/b + b/a >= 2.
    for n in range(2, 7):
        for edges in all_graphs(n):
            adj = adjacency(n, edges)
            k = [len(a) for a in adj]
            if min(k) == 0:
                continue
            total = sum(Fraction(sum(k[w] for w in adj[v]), k[v]) for v in range(n))
            assert total >= sum(k)
            per_edge = sum(Fraction(k[a], k[b]) + Fraction(k[b], k[a]) for a, b in edges)
            assert per_edge == total
    # But one person can have more friends than their friends' average (the star's hub).
    print("ok week 184")


# ---------------------------------------------------------------- week 185

def strongly_connected(n, arcs):
    out = [[] for _ in range(n)]
    inn = [[] for _ in range(n)]
    for a, b in arcs:
        out[a].append(b)
        inn[b].append(a)
    for nbrs in (out, inn):
        seen, stack = {0}, [0]
        while stack:
            v = stack.pop()
            for w in nbrs[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        if len(seen) != n:
            return False
    return True


def strong_orientations(n, edges):
    count = 0
    for flips in itertools.product((0, 1), repeat=len(edges)):
        arcs = [(b, a) if f else (a, b) for (a, b), f in zip(edges, flips)]
        count += strongly_connected(n, arcs)
    return count


def has_bridge(n, edges):
    return any(not connected(n, edges, removed=e) for e in edges)


def grid_edges(r, c):
    idx = lambda i, j: i * c + j
    e = []
    for i in range(r):
        for j in range(c):
            if j + 1 < c:
                e.append((idx(i, j), idx(i, j + 1)))
            if i + 1 < r:
                e.append((idx(i, j), idx(i + 1, j)))
    return e


def check_week_185():
    # Robbins on every graph with 3, 4 and 5 places (and at least one road).
    for n in (3, 4, 5):
        for edges in all_graphs(n):
            if not edges:
                continue
            good = connected(n, edges) and not has_bridge(n, edges)
            assert (strong_orientations(n, edges) > 0) == good
    # A ring of k roads has exactly 2 good orientations.
    for k in range(3, 9):
        assert strong_orientations(k, [(i, (i + 1) % k) for i in range(k)]) == 2
    # Town of 3-by-3 crossings (4 blocks, 12 roads): 78 of the 4096 orientations are good.
    g = grid_edges(3, 3)
    assert len(g) == 12
    GOOD33 = strong_orientations(9, g)
    assert GOOD33 == 78
    # Alternating streets (Manhattan style): every row and every column one-way, neighbours
    # opposite. On r-by-c crossings (r, c = 2..5) this can work exactly when r and c are
    # both even (and then for 2 of the 4 phase choices); on the 3-by-3 town a corner
    # always becomes a dead end or a no-entry spot.
    def alternating(r, c, rs, cs):
        idx = lambda i, j: i * c + j
        arcs = []
        for i in range(r):
            for j in range(c - 1):
                a, b = idx(i, j), idx(i, j + 1)
                arcs.append((a, b) if (i + rs) % 2 == 0 else (b, a))
        for j in range(c):
            for i in range(r - 1):
                a, b = idx(i, j), idx(i + 1, j)
                arcs.append((a, b) if (j + cs) % 2 == 0 else (b, a))
        return strongly_connected(r * c, arcs)
    for r in range(2, 6):
        for c in range(2, 6):
            ok = [alternating(r, c, rs, cs) for rs in (0, 1) for cs in (0, 1)]
            assert sum(ok) == (2 if r % 2 == 0 and c % 2 == 0 else 0)
    idx = lambda i, j: i * 3 + j
    # All one way (every row east): no orientation of columns can save it.
    for flips in itertools.product((0, 1), repeat=6):
        arcs3 = [(idx(i, j), idx(i, j + 1)) for i in range(3) for j in range(2)]
        cols = [(idx(i, j), idx(i + 1, j)) for j in range(3) for i in range(2)]
        arcs3 += [(b, a) if f else (a, b) for (a, b), f in zip(cols, flips)]
        assert not strongly_connected(9, arcs3)
    # A town with one bridge road (two rings joined by one road): 0 good orientations.
    two_rings = [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (2, 3)]
    assert has_bridge(6, two_rings) and strong_orientations(6, two_rings) == 0
    # Join them by a second road (0-5) and it works: 18 of the 256 orientations are good.
    two_rings2 = two_rings + [(0, 5)]
    assert not has_bridge(6, two_rings2) and strong_orientations(6, two_rings2) == 18
    print("ok week 185  (3-by-3 town good orientations: %d of 4096)" % GOOD33)
    return GOOD33


# ---------------------------------------------------------------- week 186

def is_tree(n, edges):
    return len(edges) == n - 1 and connected(n, edges)


def labelled_trees(n):
    pairs = list(itertools.combinations(range(n), 2))
    return [e for e in itertools.combinations(pairs, n - 1) if is_tree(n, list(e))]


def canon_tree(n, edges):
    """Canonical string of an unlabelled tree via its centre (AHU encoding)."""
    adj = adjacency(n, edges)

    def enc(v, parent):
        return "(" + "".join(sorted(enc(w, v) for w in adj[v] if w != parent)) + ")"

    return min(enc(v, -1) for v in range(n))


def prufer(n, edges):
    adj = adjacency(n, edges)
    code = []
    for _ in range(n - 2):
        leaf = min(v for v in range(n) if len(adj[v]) == 1)
        nb = next(iter(adj[leaf]))
        code.append(nb)
        adj[nb].discard(leaf)
        adj[leaf].clear()
    return tuple(code)


def check_week_186():
    counts = {n: len(labelled_trees(n)) for n in range(2, 8)}
    assert counts == {2: 1, 3: 3, 4: 16, 5: 125, 6: 1296, 7: 16807}
    assert all(counts[n] == n ** (n - 2) for n in counts)
    # By shape: 4 points: 12 paths + 4 stars; 5 points: 60 paths + 60 forks + 5 stars.
    for n, expect in ((4, [4, 12]), (5, [5, 60, 60]), (6, None)):
        shapes = Counter(canon_tree(n, list(t)) for t in labelled_trees(n))
        sizes = sorted(shapes.values())
        if expect:
            assert sizes == expect
        else:
            assert len(shapes) == 6 and sum(sizes) == 1296
            SIX = sizes
        # labellings of each shape = n! / symmetries of the shape
        for c in shapes.values():
            assert factorial(n) % c == 0
    assert SIX == [6, 90, 120, 360, 360, 360]
    # Prufer: a one-to-one match between trees and words of n - 2 labels.
    for n in (4, 5, 6):
        codes = {prufer(n, list(t)) for t in labelled_trees(n)}
        assert len(codes) == n ** (n - 2)
    # Example from the plan: path 1-2-3-4 has code (2, 3); star at 1 has code (1, 1).
    assert prufer(4, [(0, 1), (1, 2), (2, 3)]) == (1, 2)
    assert prufer(4, [(0, 1), (0, 2), (0, 3)]) == (0, 0)
    # Each label appears in the code (its number of links - 1) times.
    for t in labelled_trees(5):
        code = prufer(5, list(t))
        adj = adjacency(5, list(t))
        assert all(code.count(v) == len(adj[v]) - 1 for v in range(5))
    # Pointing pictures (everyone points at someone): n^n = n^2 * n^(n-2).
    assert 4 ** 4 == 256 == 16 * 16 and 5 ** 5 == 25 * 125
    # 3 straws among the C(4,2) = 6 links of 4 points: 20 choices, 16 trees, the other 4 a
    # triangle plus a lonely point. 4 straws among 10 links of 5 points: 210 choices, 125 trees.
    assert comb(6, 3) == 20 and counts[4] == 16 and 20 - 16 == 4
    assert sum(1 for e in itertools.combinations(list(itertools.combinations(range(4), 2)), 3)
               if not is_tree(4, list(e))) == 4
    assert comb(10, 4) == 210
    print("ok week 186")


# ---------------------------------------------------------------- week 187

HEX_NB = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1))
SQ_NB = ((-1, 0), (1, 0), (0, -1), (0, 1))


def crosses(board, n, colour, nbs, top_bottom=True):
    if top_bottom:
        start = [(0, c) for c in range(n) if board[0][c] == colour]
        goal = lambda r, c: r == n - 1
    else:
        start = [(r, 0) for r in range(n) if board[r][0] == colour]
        goal = lambda r, c: c == n - 1
    seen, stack = set(start), list(start)
    while stack:
        r, c = stack.pop()
        if goal(r, c):
            return True
        for dr, dc in nbs:
            rr, cc = r + dr, c + dc
            if 0 <= rr < n and 0 <= cc < n and (rr, cc) not in seen and board[rr][cc] == colour:
                seen.add((rr, cc))
                stack.append((rr, cc))
    return False


def boards(n):
    for mask in range(1 << (n * n)):
        yield [[mask >> (r * n + c) & 1 for c in range(n)] for r in range(n)]


def check_week_187():
    # Hex rhombus: every colouring has exactly one crossing (green top-bottom XOR
    # white left-right), on 2-by-2, 3-by-3 and 4-by-4 boards.
    for n in (2, 3, 4):
        wins = 0
        for b in boards(n):
            g = crosses(b, n, 1, HEX_NB, True)
            w = crosses(b, n, 0, HEX_NB, False)
            assert g != w
            wins += g
        assert Fraction(wins, 2 ** (n * n)) == Fraction(1, 2)
    # Exact crossing chance on 4-by-4 hexes as the share of green cells changes.
    def hex_poly(n, p):
        tot = Fraction(0)
        for b in boards(n):
            k = sum(map(sum, b))
            if crosses(b, n, 1, HEX_NB, True):
                tot += p ** k * (1 - p) ** (n * n - k)
        return tot
    p3, p4, p5, p6, p7 = (hex_poly(4, Fraction(x, 10)) for x in (3, 4, 5, 6, 7))
    assert p5 == Fraction(1, 2) and p3 + p7 == 1 and p4 + p6 == 1
    assert round(float(p3), 3) == 0.111 and round(float(p7), 3) == 0.889
    assert round(float(p4), 3) == 0.276 and round(float(p6), 3) == 0.724
    # On a 2-by-2 board the same 40 per cent green crosses 0.352 of the time: bigger is sharper.
    assert hex_poly(2, Fraction(2, 5)) == Fraction(44, 125) and round(44 / 125, 3) == 0.352
    # Square cells (only side neighbours), 4-by-4, coin flips: green crosses top-bottom
    # less than half the time, and sometimes neither colour crosses.
    g_sq = neither = 0
    for b in boards(4):
        g = crosses(b, 4, 1, SQ_NB, True)
        w = crosses(b, 4, 0, SQ_NB, False)
        g_sq += g
        neither += (not g) and (not w)
    assert g_sq == 22193 and neither > 0
    assert round(g_sq / 65536, 3) == 0.339
    # Larger hex board (11-by-11), seeded simulation: the change gets sharper.
    rng = random.Random(187)
    sim = {}
    for p in (0.4, 0.5, 0.6):
        hits = 0
        for _ in range(2000):
            b = [[1 if rng.random() < p else 0 for _ in range(11)] for _ in range(11)]
            hits += crosses(b, 11, 1, HEX_NB, True)
        sim[p] = hits / 2000
    assert sim[0.4] < 0.15 and 0.45 < sim[0.5] < 0.55 and sim[0.6] > 0.85
    print("ok week 187  (4x4 hex p=0.3/0.7: %.3f/%.3f; 11x11 sim: %s)" % (float(p3), float(p7), sim))


# ---------------------------------------------------------------- week 188

def ring(n, reach=1):
    return [(i, (i + d) % n) for i in range(n) for d in range(1, reach + 1)]


def dist_stats(n, edges):
    adj = adjacency(n, edges)
    total, diam = 0, 0
    for s in range(n):
        d = distances_from(adj, s)
        assert len(d) == n
        total += sum(d.values())
        diam = max(diam, max(d.values()))
    return Fraction(total, n * (n - 1)), diam


def check_week_188():
    # Ring of 16 children holding hands: diameter 8, average distance 64/15 (about 4.27).
    avg, diam = dist_stats(16, ring(16))
    assert diam == 8 and avg == Fraction(64, 15)
    # Ring of 24: diameter 12, average 144/23 (about 6.26).
    avg24, d24 = dist_stats(24, ring(24))
    assert d24 == 12 and avg24 == Fraction(144, 23)
    # Even rings: average n^2 / (4(n - 1)).
    for n in range(4, 41, 2):
        assert dist_stats(n, ring(n))[0] == Fraction(n * n, 4 * (n - 1))
    # Ring of 16 plus one shortcut across the middle (0-8): the farthest pair (4 and 12)
    # is still 8 apart, but the average falls to 421/120 (about 3.51).
    avg1, diam1 = dist_stats(16, ring(16) + [(0, 8)])
    assert diam1 == 8 and avg1 == Fraction(421, 120)
    # Add a second (4-12): diameter 5, average 44/15 (about 2.93).
    avg2, diam2 = dist_stats(16, ring(16) + [(0, 8), (4, 12)])
    assert diam2 == 5 and avg2 == Fraction(44, 15)
    # Knowing two neighbours each side (Watts-Strogatz start, 24 children): diameter 6,
    # average 78/23 (about 3.39).
    avgk, dk = dist_stats(24, ring(24, 2))
    assert dk == 6 and avgk == Fraction(78, 23)
    # Random shortcuts (seeded, 400 random choices each): the mean average distance falls fast.
    rng = random.Random(188)
    means = {}
    for n, ks in ((16, (0, 2, 4, 8)), (24, (0, 4, 8))):
        for k in ks:
            vals = []
            for _ in range(400):
                extra = []
                while len(extra) < k:
                    a, b = rng.sample(range(n), 2)
                    if (a - b) % n not in (1, n - 1) and (a, b) not in extra and (b, a) not in extra:
                        extra.append((a, b))
                vals.append(float(dist_stats(n, ring(n) + extra)[0]))
            means[(n, k)] = sum(vals) / len(vals)
    assert abs(means[(16, 0)] - 4.27) < 0.01 and abs(means[(24, 0)] - 6.26) < 0.01
    assert 3.2 < means[(16, 2)] < 3.6 and 2.7 < means[(16, 4)] < 3.1 and 2.2 < means[(16, 8)] < 2.6
    assert 3.8 < means[(24, 4)] < 4.3 and 3.1 < means[(24, 8)] < 3.5
    # Doubling the ring roughly doubles the average; adding shortcuts does not need that.
    assert dist_stats(48, ring(48))[0] == Fraction(48 * 48, 4 * 47)
    print("ok week 188  (16+1 shortcut avg %.2f; 16+2 avg %.2f; 24-ring k=4 avg %.2f; random means %s)"
          % (float(avg1), float(avg2), float(avgk), {k: round(v, 2) for k, v in means.items()}))


def main():
    check_week_182()
    check_week_183()
    check_week_184()
    check_week_185()
    check_week_186()
    check_week_187()
    check_week_188()


if __name__ == "__main__":
    main()
