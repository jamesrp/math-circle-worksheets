#!/usr/bin/env python3
"""Independent mathematical checks for the Week 2 compact and upper catalogs.

Model: lamps = vertices, lines = edges; a move toggles both ends of one edge.
For every printed start->target pair (decoded from the PDFs by
verify_diagrams.py and confirmed equal to the data files), this computes:
  * reachability and the minimum number of moves by BFS over all 2^n states,
  * every edge subset (each line pressed at most once) that solves it,
and checks the guides' stated answers, move lists, rules and records.
"""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
import itertools
import math
from collections import deque

# ---------- graphs (vertex numbering as in the data files; checked against the PDFs) ----------

def cycle(n):
    return n, [(i, i % n + 1) for i in range(1, n + 1)]

G = {
    "square": (4, [(1, 2), (2, 3), (3, 4), (4, 1)]),
    "ring4": cycle(4), "ring5": cycle(5), "ring6": cycle(6), "ring7": cycle(7), "ring8": cycle(8),
    "tree8": (8, [(1, 2), (2, 3), (3, 4), (4, 5), (3, 6), (6, 7), (6, 8)]),
    "grid9": (9, [(1, 2), (2, 3), (4, 5), (5, 6), (7, 8), (8, 9), (1, 4), (4, 7), (2, 5), (5, 8), (3, 6), (6, 9)]),
    "islands8": (8, [(1, 2), (2, 3), (3, 4), (4, 1), (5, 6), (6, 7), (7, 8), (8, 5)]),
    "path6": (6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]),
    "star5": (5, [(1, 2), (1, 3), (1, 4), (1, 5)]),
    "triangle_pair": (5, [(1, 2), (2, 3), (3, 1), (4, 5)]),
    "triangle_bridge": (5, [(1, 2), (2, 3), (3, 1), (4, 5), (3, 4)]),
    "two_squares": (8, [(1, 2), (2, 3), (3, 4), (4, 1), (5, 6), (6, 7), (7, 8), (8, 5)]),
    "two_trees": (7, [(1, 2), (2, 3), (4, 5), (4, 6), (4, 7)]),
    "tree6": (6, [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6)]),
    "star7": (7, [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]),
}


def mask(s):
    m = 0
    for v in s:
        m |= 1 << (v - 1)
    return m


def unmask(m, n):
    return [v for v in range(1, n + 1) if m >> (v - 1) & 1]


def bfs(name, start):
    n, E = G[name]
    moves = [mask(e) for e in E]
    dist = {mask(start): 0}
    q = deque([mask(start)])
    while q:
        s = q.popleft()
        for mv in moves:
            t = s ^ mv
            if t not in dist:
                dist[t] = dist[s] + 1
                q.append(t)
    return dist


def subsets_solving(name, start, target):
    n, E = G[name]
    need = mask(start) ^ mask(target)
    sols = []
    for r in range(len(E) + 1):
        for comb in itertools.combinations(range(len(E)), r):
            m = 0
            for i in comb:
                m ^= mask(E[i])
            if m == need:
                sols.append([E[i] for i in comb])
    return sols


def components(name):
    n, E = G[name]
    parent = list(range(n + 1))

    def f(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in E:
        parent[f(u)] = f(v)
    comp = {}
    for v in range(1, n + 1):
        comp.setdefault(f(v), []).append(v)
    return list(comp.values())


def parity_rule(name, start, target):
    need = set(start) ^ set(target)
    return all(len(need & set(c)) % 2 == 0 for c in components(name))


def play(name, start, presses, one_light=False):
    n, E = G[name]
    Es = {frozenset(e) for e in E}
    s = set(start)
    seen = set(s)
    for a, b in presses:
        assert frozenset((a, b)) in Es, f"{name}: {a}-{b} is not a line"
        s ^= {a, b}
        seen |= s
        if one_light:
            assert len(s) == 1, f"{name}: {presses} leaves {sorted(s)} on"
    return sorted(s), seen


def p(*a):
    print(*a)


problems = []


def report(label, ok, detail=""):
    p(("OK  " if ok else "FAIL"), label, detail)
    if not ok:
        problems.append(label + " " + detail)


# ============ Compact catalog F02-S-CAT-v2 ============
p("=== Compact catalog (F02-S-CAT-v2) ===")
compact = [
    ("C-P1", "square", [], [[1, 2], [1, 3], [1, 2, 3, 4]]),
    ("C-P2", "ring6", [1], [[3], [4]]),
    ("C-P3", "ring6", [1], [[1]]),
    ("C-P4", "tree8", [1], [[5], [7], [8]]),
    ("C-P5", "tree8", [], [[1, 8]]),
    ("C-P6", "ring6", [], [[1, 2], [1, 4], [1, 2, 4, 5], [1, 2, 3, 4, 5, 6]]),
    ("C-P7", "grid9", [], [[1, 5], [2, 8], [1, 3, 7, 9], [1, 3, 4, 6, 7, 9]]),
    ("C-P8", "islands8", [1], [[5]]),
]
for label, name, st, tgs in compact:
    d = bfs(name, st)
    for t in tgs:
        r = mask(t) in d
        p(f"{label} {name} {st}->{t}: reachable={r} min={d.get(mask(t))} rule={parity_rule(name, st, t)}")

# P3 tour: is there a one-light walk visiting every lamp and returning (a Hamilton cycle on C6: yes)
fin, seen = play("ring6", [1], [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)], one_light=True)
report("C-P3 guide tour 1-2..6-1", fin == [1] and seen == set(range(1, 7)))

# P9: every possible bridge between the islands makes 1 -> 5 reachable with one light kept ON
left, right = [1, 2, 3, 4], [5, 6, 7, 8]
allok = True
for a in left:
    for b in right:
        n, E = G["islands8"]
        G["tmp"] = (n, E + [(a, b)])
        # one-light walk exists iff 1 and 5 are connected
        comps = components("tmp")
        conn = any(1 in c and 5 in c for c in comps)
        allok &= conn and mask([5]) in bfs("tmp", [1])
report("C-P9 every one-line bridge makes the trip possible", allok)

# Archived shared guide move lists (P2, P5-P12)
p("--- archived shared guide (F02-S-FAC-v1) move lists for catalog problems ---")
guide_lists = [
    ("guide P2 {1,2}", "square", [], [(1, 2)], [1, 2], False),
    ("guide P2 {1,3}", "square", [], [(1, 2), (2, 3)], [1, 3], False),
    ("guide P2 all", "square", [], [(1, 2), (3, 4)], [1, 2, 3, 4], False),
    ("guide P5 to 3", "ring6", [1], [(1, 2), (2, 3)], [3], True),
    ("guide P5 to 4", "ring6", [1], [(1, 2), (2, 3), (3, 4)], [4], True),
    ("guide P7 to 5", "tree8", [1], [(1, 2), (2, 3), (3, 4), (4, 5)], [5], True),
    ("guide P7 to 7", "tree8", [1], [(1, 2), (2, 3), (3, 6), (6, 7)], [7], True),
    ("guide P7 to 8", "tree8", [1], [(1, 2), (2, 3), (3, 6), (6, 8)], [8], True),
    ("guide P8 {1,8}", "tree8", [], [(1, 2), (2, 3), (3, 6), (6, 8)], [1, 8], False),
    ("guide P9 {1,2}", "ring6", [], [(1, 2)], [1, 2], False),
    ("guide P9 {1,4}", "ring6", [], [(1, 2), (2, 3), (3, 4)], [1, 4], False),
    ("guide P9 {1,2,4,5}", "ring6", [], [(1, 2), (4, 5)], [1, 2, 4, 5], False),
    ("guide P9 all", "ring6", [], [(1, 2), (3, 4), (5, 6)], [1, 2, 3, 4, 5, 6], False),
    ("guide P10 {1,5}", "grid9", [], [(1, 2), (2, 5)], [1, 5], False),
    ("guide P10 {2,8}", "grid9", [], [(2, 5), (5, 8)], [2, 8], False),
    ("guide P10 corners", "grid9", [], [(1, 2), (2, 3), (7, 8), (8, 9)], [1, 3, 7, 9], False),
    ("guide P10 six", "grid9", [], [(1, 2), (2, 3), (4, 7), (6, 9)], [1, 3, 4, 6, 7, 9], False),
]
for label, name, st, presses, want, one in guide_lists:
    try:
        fin, _ = play(name, st, presses, one)
        report(label, fin == want, f"got {fin}")
    except AssertionError as e:
        report(label, False, str(e))
G["bridged"] = (8, G["islands8"][1] + [(2, 5)])
fin, _ = play("bridged", [1], [(1, 2), (2, 5)], True)
report("guide P12 bridge 2-5 then 1-2; 2-5", fin == [5])
# P11 claim: impossible even allowing extra lights
report("guide P11 impossible on printed map", mask([5]) not in bfs("islands8", [1]))

# ============ Upper catalog F02-S-CAT-UP-v1 ============
p("\n=== Upper catalog (F02-S-CAT-UP-v1) ===")
P1 = [("A", "ring4", [], [1, 3], True), ("B", "ring5", [1], [3], True), ("C", "ring6", [], [1, 3, 5], False),
      ("D", "star5", [1, 2, 3], [2], True), ("E", "grid9", [1, 5], [3, 7, 9], False), ("F", "path6", [1, 2], [5, 6], True)]
for L, name, st, t, guide in P1:
    d = bfs(name, st)
    r = mask(t) in d
    report(f"U-P1{L} {name} {st}->{t} guide says {'possible' if guide else 'impossible'}", r == guide,
           f"reachable={r} min={d.get(mask(t))} on-count {len(st)}->{len(t)}")
# rule on connected graphs: reachable iff parity of ON-count equal, over ALL start/target pairs
for name in ["ring4", "ring5", "ring6", "star5", "grid9", "path6"]:
    n, _ = G[name]
    ok = True
    for s in range(1 << n):
        d = bfs(name, unmask(s, n))
        for t in range(1 << n):
            ok &= ((t in d) == (bin(s).count("1") % 2 == bin(t).count("1") % 2))
        if n > 6:
            break  # one start suffices by symmetry of the group action (reachability is coset membership)
    report(f"U-P1 parity rule exact on {name}", ok)

P2 = [("A", "triangle_pair", [1], [3], True), ("B", "triangle_pair", [1], [4], False),
      ("C", "triangle_bridge", [1], [4], True), ("D", "two_squares", [1, 5], [2, 8], True),
      ("E", "two_trees", [], [1, 4], False), ("F", "two_trees", [1, 4], [2, 6], True)]
for L, name, st, t, guide in P2:
    d = bfs(name, st)
    r = mask(t) in d
    report(f"U-P2{L} {name} {st}->{t} guide says {'possible' if guide else 'impossible'}", r == guide,
           f"reachable={r} min={d.get(mask(t))} per-component rule={parity_rule(name, st, t)}")
for name in ["triangle_pair", "triangle_bridge", "two_squares", "two_trees"]:
    n, _ = G[name]
    d = bfs(name, [])
    ok = all(((t in d) == parity_rule(name, [], unmask(t, n))) for t in range(1 << n))
    report(f"U-P2 per-component rule exact on {name}", ok)
# guide: D and F odd in each component before and after; E even total
for L, name, st, t in [("D", "two_squares", [1, 5], [2, 8]), ("F", "two_trees", [1, 4], [2, 6])]:
    oddall = all(len(set(st) & set(c)) % 2 == 1 and len(set(t) & set(c)) % 2 == 1 for c in components(name))
    report(f"U-P2{L} guide: odd ON count in each component before and after", oddall)

P3 = [("A", "ring4", [], []), ("B", "ring5", [1], [3]), ("C", "ring6", [], [1, 4]), ("D", "ring7", [1, 3], [2, 4])]
guide_sizes = {"A": (0, 4), "B": (2, 3), "C": (3, 3), "D": (2, 5)}
for L, name, st, t in P3:
    sols = subsets_solving(name, st, t)
    n, E = G[name]
    sizes = tuple(sorted(len(s) for s in sols))
    comp = len(sols) == 2 and {frozenset(sols[0]) | frozenset(sols[1])} == {frozenset(E)} and not set(sols[0]) & set(sols[1])
    report(f"U-P3{L} {name} {st}->{t}", len(sols) == 2 and comp and sizes == guide_sizes[L],
           f"{len(sols)} solutions sizes {sizes}: {sols}")
# general cycle claim: every reachable target has exactly two complementary subsets
for n in range(3, 11):
    name = f"c{n}"
    G[name] = cycle(n)
    ok = True
    for t in range(1 << n):
        sols = subsets_solving(name, [], unmask(t, n)) if n <= 8 else None
        if sols is None:
            break
        ok &= (len(sols) == 2) if bin(t).count("1") % 2 == 0 else (len(sols) == 0)
    if n <= 8:
        report(f"cycle C{n}: even targets have exactly 2 subset solutions, odd none", ok)

P4 = [("A", "ring8", [1, 2, 5, 6], 2), ("B", "ring8", [1, 3, 5, 7], 4), ("C", "ring6", [1, 2, 3, 4, 5, 6], 3),
      ("D", "path6", [1, 6], 5), ("E", "star5", [2, 3, 4, 5], 4), ("F", "grid9", [1, 3, 7, 9], 4)]
for L, name, t, gmin in P4:
    d = bfs(name, [])
    report(f"U-P4{L} {name} min to {t} (guide {gmin})", d.get(mask(t)) == gmin, f"BFS min={d.get(mask(t))}")
# guide's sample shortest solutions
for label, name, presses, want in [
    ("U-P4A guide: the two lit adjacent pairs", "ring8", [(1, 2), (5, 6)], [1, 2, 5, 6]),
    ("U-P4C guide: alternate edges", "ring6", [(1, 2), (3, 4), (5, 6)], [1, 2, 3, 4, 5, 6]),
    ("U-P4D guide: all five", "path6", [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)], [1, 6]),
    ("U-P4E guide: four spokes", "star5", [(1, 2), (1, 3), (1, 4), (1, 5)], [2, 3, 4, 5]),
    ("U-P4F guide: top and bottom rows", "grid9", [(1, 2), (2, 3), (7, 8), (8, 9)], [1, 3, 7, 9]),
    ("U-P4F guide: outer columns", "grid9", [(1, 4), (4, 7), (3, 6), (6, 9)], [1, 3, 7, 9]),
]:
    fin, _ = play(name, [], presses)
    report(label, fin == want, f"got {fin}")

# P5: hardest solvable target on rings, start all OFF
p("--- U-P5 ring records ---")
for n in range(3, 13):
    name = f"c{n}"
    G[name] = cycle(n)
    d = bfs(name, [])
    rec = max(d.values())
    hard = [unmask(t, n) for t, v in d.items() if v == rec]
    ok = rec == n // 2
    report(f"ring {n}: record {rec} (floor(n/2)={n//2})", ok, f"{len(hard)} record targets, e.g. {hard[:3]}")
    if n in (5, 6, 7, 8):
        # guide: two lamps floor(n/2) apart attain it
        report(f"ring {n}: lamps 1 and {1 + n//2} attain record", d[mask([1, 1 + n // 2])] == rec)

P6 = [("A", "tree6", [], [1, 3, 5, 6], 1), ("B", "star7", [2, 4], [3, 5, 6, 7], 1),
      ("C", "tree8", [1, 7], [5], 0), ("D", "path6", [2, 5], [2, 5], 1)]
for L, name, st, t, cnt in P6:
    sols = subsets_solving(name, st, t)
    report(f"U-P6{L} {name} {st}->{t} solution count (data {cnt})", len(sols) == cnt, f"{sols}")
for name in ["tree6", "star7", "tree8", "path6"]:
    n, _ = G[name]
    ok = all(len(subsets_solving(name, [], unmask(t, n))) == (1 if bin(t).count("1") % 2 == 0 else 0)
             for t in range(1 << n))
    report(f"tree {name}: every even target exactly one subset, odd none", ok)

# Guide: complement works on a graph iff every vertex has even degree (check on small graphs)
def even_degree(name):
    n, E = G[name]
    deg = [0] * (n + 1)
    for a, b in E:
        deg[a] += 1
        deg[b] += 1
    return all(x % 2 == 0 for x in deg[1:])

ok = True
for name in ["ring5", "grid9", "tree8", "star5", "two_squares", "triangle_bridge"]:
    n, E = G[name]
    full = 0
    for e in E:
        full ^= mask(e)
    ok &= ((full == 0) == even_degree(name))
report("guide P3 extension: complementing preserves the result iff all degrees even", ok)

p("\nFAILURES:" if problems else "\nAll checks passed.")
for x in problems:
    p("  ", x)
