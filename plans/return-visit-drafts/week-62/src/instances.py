"""Every network, list puzzle, move task and arrow task printed in the final packets.

check_all() verifies each printed claim by brute force (python3 instances.py).
"""
from mathlib import *

def L(s):
    """'A:12 B:3' -> {'A': {1, 2}, 'B': {3}}"""
    return {k: set(int(c) for c in v) for k, v in (x.split(':') for x in s.split())}

PATH2 = "AB"
PATH3 = "AB BC"
PATH4 = "AB BC CD"
TRI = "AB BC CA"
SQUARE = "AB BC CD DA"
STAR3 = "AB AC AD"
STAR5 = "AB AC AD AE AF"
K23 = "AC AD AE BC BD BE"
K24 = "AC AD AE AF BC BD BE BF"
RING5 = ring_name(5)
RING6 = ring_name(6)
RING7 = ring_name(7)
RING4 = ring_name(4)
RING5LEAF = RING5 + " AF"
RING6LEAVES = RING6 + " AG DH"
TREEB = "HA HB BC HD DE DF FG"
PAW = "AB BC CA CD"   # demo network only

# ---------------- list puzzles: (band, problem, board, network, lists, expected) ------
# expected: 'unique', 'yes' (at least one), or 'no'
LISTS = [
    # K-1 Problem 1
    ("K", 1, "a", PATH3, "A:2 B:23 C:13", "unique"),
    ("K", 1, "b", TRI, "A:12 B:1 C:123", "unique"),
    ("K", 1, "c", STAR3, "A:123 B:1 C:2 D:13", "unique"),
    ("K", 1, "d", SQUARE, "A:1 B:12 C:123 D:13", "unique"),
    # K-1 Problem 2
    ("K", 2, "a", PATH3, "A:1 B:12 C:2", "no"),
    ("K", 2, "b", PATH4, "A:1 B:12 C:23 D:13", "unique"),
    ("K", 2, "c", TRI, "A:12 B:12 C:12", "no"),
    ("K", 2, "d", SQUARE, "A:12 B:12 C:12 D:12", "yes"),
    # K-1 Problem 3
    ("K", 3, "a", RING6, "A:1 B:12 C:23 D:13 E:12 F:13", "unique"),
    ("K", 3, "b", K23, "A:123 B:124 C:1 D:2 E:3", "no"),
    # Grades 2-3 Problem 1
    ("M", 1, "a", TREEB, "H:12 A:24 B:23 C:13 D:13 E:14 F:23 G:2", "unique"),
    ("M", 1, "b", RING6LEAVES, "G:3 A:13 B:12 C:23 D:23 H:3 E:24 F:14", "no"),
    # Grades 2-3 Problem 2 and grades 4-5 Problem 4 (rings with two numbers each)
    ("M", 2, "a", RING5, "A:12 B:12 C:12 D:12 E:12", "no"),
    ("M", 2, "b", RING5, "A:12 B:12 C:13 D:12 E:12", "yes"),
    ("M", 2, "c", RING6, "A:12 B:12 C:12 D:12 E:12 F:12", "yes"),
    ("M", 2, "d", RING5LEAF, "A:23 B:23 C:23 D:23 E:23 F:13", "no"),
    # Grades 2-3 Problem 3 and grades 4-5 Problem 1 (six cards; the 4-5 packet reuses these keys)
    ("M", 3, "a", K24, "A:12 B:34 C:13 D:14 E:23 F:24", "no"),
    ("M", 3, "b", K24, "A:12 B:34 C:13 D:14 E:23 F:34", "yes"),
    # Grades 4-5 Problem 4 boards
    ("U", 4, "a", RING5, "A:12 B:12 C:12 D:12 E:12", "no"),
    ("U", 4, "b", RING5, "A:12 B:23 C:13 D:12 E:23", "yes"),
    ("U", 4, "c", RING5LEAF, "A:12 B:12 C:13 D:12 E:12 F:12", "yes"),
    ("U", 4, "d", RING6, "A:34 B:34 C:34 D:34 E:34 F:34", "yes"),
]

# ---------------- move tasks: (band, problem, network, k, start, goal, expected fewest or None)
MOVES = [
    ("K", 4, PATH2, 2, "A1 B2", "A2 B1", None),
    ("K", 4, PATH2, 3, "A1 B2", "A2 B1", 3),
    ("K", 5, PATH3, 3, "A1 B2 C1", "A2 B1 C2", 4),
    ("K", 6, STAR5, 3, "A1 B2 C2 D2 E2 F2", "A2 B1 C1 D1 E1 F1", 7),
    ("K", 7, SQUARE, 3, "A1 B2 C1 D2", "A2 B1 C2 D1", 6),
    ("K", 8, TRI, 3, "A1 B2 C3", "A2 B3 C1", None),
    ("K", 8, TRI, 4, "A1 B2 C3", "A2 B3 C1", 4),
    ("M", 5, PATH2, 3, "A1 B2", "A2 B1", 3),
    ("M", 5, PATH3, 3, "A1 B2 C1", "A2 B1 C2", 4),
    ("M", 6, PATH4, 3, "A1 B2 C1 D2", "A2 B1 C2 D1", 6),
    ("M", 6, STAR5, 3, "A1 B2 C2 D2 E2 F2", "A2 B1 C1 D1 E1 F1", 7),
    ("M", 7, TRI, 3, "A1 B2 C3", "A2 B3 C1", None),
    ("M", 7, TRI, 4, "A1 B2 C3", "A2 B3 C1", 4),
    ("U", 5, TRI, 3, "A1 B2 C3", "A2 B3 C1", None),
    ("U", 5, TRI, 4, "A1 B2 C3", "A2 B3 C1", 4),
    ("U", 7, RING5, 3, "A1 B2 C3 D1 E2", "A2 B3 C1 D2 E3", 5),
    ("U", 7, RING5, 3, "A1 B2 C3 D1 E2", "A1 B3 C2 D1 E3", None),
    ("U", 8, RING5, 4, "A1 B2 C3 D1 E2", "A1 B3 C2 D1 E3", 4),
]

# demo moves (paw, three counters): start A1 B2 C3 D2, move D1
DEMO_MOVE = (PAW, 3, "A1 B2 C3 D2", ("D", 1))

# ---------------- arrow tasks: (band, problem, board, arrows, expected fewest or None)
ARROWS = [
    ("M", 9, "", "AB BC CD EB FC GH", 4),
    ("U", 9, "a", "AB BC CD EB FC GH", 4),
    ("M", 10, "a", "AB BC CA", None),
    ("M", 10, "b", "AB BC CD DE", 5),
    ("M", 10, "c", "AD BD BE CE DF EF FG", 4),
    ("M", 10, "d", "AD BD BE CE DF EF FG ED", 5),
    ("U", 10, "a", "HA AC BC CF GD DE EF", 4),
    ("U", 10, "b", "HA AC BC CF GD DE EF EC", 5),
]

# boards where children try to write two numbers from 1-4 next to every circle without numbers so that the
# puzzle is impossible (grades 2-3 Problem 4, grades 4-5 Problems 2 and 3):
# (band, problem, board, network, printed lists, expected number of failing assignments of the other circles)
INVENT = [
    ("M", 4, "a", K24, "A:13", 24),
    ("M", 4, "b", K23, "A:13", 0),
    ("U", 2, "", K23, "", 0),
    ("U", 3, "", TREEB, "", 0),
]
DEMO_ARROWS = "AB AC"

# conflict networks for arrows (grades 4-5 Problem 11): expected min longest path
ORIENT = [
    ("U", 11, "a", RING5LEAF, 3),
    ("U", 11, "b", RING6LEAVES, 2),
]


def check_all():
    ok = True
    for band, p, b, net, lists, exp in LISTS:
        sols = list_schedules(net, L(lists))
        nodes, _ = parse(net)
        assert set(L(lists)) == set(nodes), (band, p, b)
        got = "no" if not sols else ("unique" if len(sols) == 1 else "yes")
        good = (got == exp) or (exp == "yes" and got == "unique")
        ok &= good
        sol = " ".join(f"{k}{v}" for k, v in sorted(sols[0].items())) if len(sols) == 1 else ""
        print(f"lists {band}{p}{b}: {len(sols)} solutions {sol} expected {exp} {'OK' if good else 'FAIL'}")
    for band, p, net, k, s, g, exp in MOVES:
        n, path = bfs_moves(net, k, parse_state(s), parse_state(g))
        for st in (s, g):
            d = parse_state(st)
            nodes, edges = parse(net)
            assert all(d[u] != d[v] for u, v in edges) and max(d.values()) <= k
        good = n == exp
        ok &= good
        word = " ".join(f"{v}{c}" for v, c in path) if path else "-"
        print(f"moves {band}{p} k={k} {s} -> {g}: {n} ({word}) expected {exp} {'OK' if good else 'FAIL'}")
    for band, p, b, arr, exp in ARROWS:
        arrows = [tuple(x) for x in arr.split()]
        nodes = sorted({v for e in arrows for v in e})
        e = earliest(arrows, nodes)
        lp = longest_path_cards(arrows, nodes)
        fs = fewest_slots_arrows(arrows, nodes, 6)
        good = fs == exp and (e is None or max(e.values()) == lp == fs)
        ok &= good
        es = " ".join(f"{k}{v}" for k, v in sorted(e.items())) if e else "circle"
        print(f"arrows {band}{p}{b}: fewest {fs} longest {lp} earliest {es} expected {exp} {'OK' if good else 'FAIL'}")
    for band, p, b, net, exp in ORIENT:
        best, dist = orientation_min_longest(net)
        good = best == exp
        ok &= good
        print(f"orient {band}{p}{b}: min longest {best} distribution {dict(sorted(dist.items()))} {'OK' if good else 'FAIL'}")
    from itertools import combinations, product as _prod
    pairs = [frozenset(p) for p in combinations([1, 2, 3, 4], 2)]
    for band, p, b, net, printed, exp in INVENT:
        nodes, edges = parse(net)
        a = adj(nodes, edges)
        given = L(printed) if printed else {}
        free = [v for v in nodes if v not in given]
        # fast check: every network here is a tree or K23; use backtracking search per assignment
        def ok_lists(lists, order=nodes):
            col = {}
            def bt(i):
                if i == len(order):
                    return True
                v = order[i]
                for c in lists[v]:
                    if all(col.get(w) != c for w in a[v]):
                        col[v] = c
                        if bt(i + 1):
                            return True
                        del col[v]
                return False
            return bt(0)
        fails = sum(1 for ch in _prod(pairs, repeat=len(free)) if not ok_lists({**given, **dict(zip(free, ch))}))
        good = fails == exp
        ok &= good
        print(f"invent {band}{p}{b} {net} printed {printed or '-'}: {6**len(free)} assignments, {fails} fail {'OK' if good else 'FAIL'}")
    # stuck rings with three counters
    for n in range(3, 9):
        print(f"ring {n}: stuck placements with 3 counters: {len(stuck(ring_name(n), 3))}")
    print(f"five-ring components with 3: {sorted(len(c) for c in components(RING5, 3))}")
    for n in range(3, 9):
        comps = components(ring_name(n), 4)
        print(f"ring {n} with 4 counters: {len(comps)} family(ies)")
    print("ALL OK" if ok else "SOME FAILED")
    return ok


if __name__ == "__main__":
    check_all()
