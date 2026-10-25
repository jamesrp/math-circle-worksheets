"""Mathematical checks for the Graceful labels packets.

A labelling is graceful when the dots get different labels from 0..m
(m = number of links) and the link differences are exactly 1..m.
For K-1 a label is a tower height and 0 is the one empty dot.

Part 1 counts the labellings of every network actually drawn on the pages
(read from figs/registry.json, so the drawings themselves are checked).
Part 2 checks the answers each problem relies on.
"""
import json
import os
from itertools import combinations
import networkx as nx  # only used for tree enumeration

HERE = os.path.dirname(os.path.abspath(__file__))


def graceful(n, edges, fixed=None, limit=None):
    """All graceful labellings, by backtracking on the largest difference."""
    m = len(edges)
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    lab = [None] * n
    used_lab = set()
    used_diff = set()
    out = []
    fixed = fixed or {}
    order = sorted(range(n), key=lambda v: -len(adj[v]))
    # visit in BFS order so most new dots have a labelled neighbour
    seen, bfs = set(), []
    for s in order:
        if s in seen:
            continue
        seen.add(s); q = [s]
        while q:
            v = q.pop(0); bfs.append(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w); q.append(w)

    def rec(i):
        if limit and len(out) >= limit:
            return
        if i == n:
            out.append(tuple(lab)); return
        v = bfs[i]
        cands = [fixed[v]] if v in fixed else range(m + 1)
        for x in cands:
            if x in used_lab:
                continue
            ds = [abs(x - lab[w]) for w in adj[v] if lab[w] is not None]
            if len(set(ds)) != len(ds) or any(d == 0 or d in used_diff for d in ds):
                continue
            lab[v] = x; used_lab.add(x); used_diff.update(ds)
            rec(i + 1)
            lab[v] = None; used_lab.discard(x); used_diff.difference_update(ds)

    rec(0)
    return out


def path(n):
    return n, [(i, i + 1) for i in range(n - 1)]


def cycle(n):
    return n, [(i, (i + 1) % n) for i in range(n)]


def star(k):
    return k + 1, [(0, i) for i in range(1, k + 1)]


def complete(n):
    return n, list(combinations(range(n), 2))


def tower_rule_count(n, edges, towers):
    """K-1 rule as printed: each tower used at most once, exactly one empty
    dot (counts as 0); links must measure 1..m each once."""
    m = len(edges)
    count = 0
    def rec(lab, avail):
        nonlocal count
        if len(lab) == n:
            if sorted(lab).count(0) != 1:
                return
            d = sorted(abs(lab[a] - lab[b]) for a, b in edges)
            if d == list(range(1, m + 1)):
                count += 1
            return
        for x in [0] + sorted(avail):
            rec(lab + [x], avail - {x} if x else avail)
    rec([], set(towers))
    return count


print("== Part 1: every network drawn on the pages ==")
reg = json.load(open(os.path.join(HERE, "figs", "registry.json")))
seen = set()
for net in reg:
    base = net["name"].split("[")[0]
    if base in seen:
        continue
    seen.add(base)
    n, e = len(net["pts"]), [tuple(x) for x in net["edges"]]
    m = len(e)
    g = nx.Graph(e)
    kind = "tree" if nx.is_tree(g) else ("loop" if all(d == 2 for _, d in g.degree()) else "other")
    sols = graceful(n, e)
    cap = net["caption"] or ""
    capok = (cap == f"cards 0 to {m}") if cap else True
    print(f"{base:14s} {n:2d} dots {m:2d} links {kind:5s} labellings {len(sols):6d}"
          f"  {cap}{'' if capok else '  <-- caption does not match link count'}"
          f"  e.g. {sols[0] if sols else '-'}")

print()
print("== Part 2: answers ==")
print("K-1 P1 path of 3, towers 1,2:", len(graceful(*path(3))), "ways;",
      "printed rule gives", tower_rule_count(*path(3), [1, 2]))
print("K-1 P2 path of 4, towers 1,2,3:", len(graceful(*path(4))), "ways", graceful(*path(4)), ";",
      "printed rule gives", tower_rule_count(*path(4), [1, 2, 3]))
print("K-1 P3 path of 5, towers 1-4:", len(graceful(*path(5))), "; printed rule", tower_rule_count(*path(5), [1, 2, 3, 4]))
fork = (5, [(0, 1), (1, 2), (2, 3), (1, 4)])
print("K-1 P4 fork, towers 1-4:", len(graceful(*fork)), "; printed rule", tower_rule_count(*fork, [1, 2, 3, 4]))
for c in range(4):
    print(f"K-1 P5 star of 3 links, middle {c}:", len(graceful(*star(3), fixed={0: c})))
for name, g, k in (("K-1 P6 triangle", cycle(3), 3), ("K-1 P7 square", cycle(4), 4)):
    sols = graceful(*g)
    print(name, "towers 1..%d, left over:" % k, sorted({(set(range(k + 1)) - set(s)).pop() for s in sols}),
          "; printed rule", tower_rule_count(*g, list(range(1, k + 1))), "=", len(sols))
sols = graceful(*star(4))
print("K-1 P8 star of 4 links: middle dot", sorted({s[0] for s in sols}), "(0 = empty);",
      len(sols), "labellings; printed rule", tower_rule_count(*star(4), [1, 2, 3, 4]))
print("2-3 P4 star of 5 links: middle", sorted({s[0] for s in graceful(*star(5))}))
for n in range(3, 13):
    sols = graceful(*cycle(n))
    print(f"loop {n:2d} links: {len(sols):6d} labellings; 1+..+n = {n*(n+1)//2:3d} ({'odd' if n*(n+1)//2 % 2 else 'even'})")
for n in (100, 101):
    print(f"loop {n} links: 1+..+n = {n*(n+1)//2} ({'odd' if n*(n+1)//2 % 2 else 'even'})")


def rosa_cycle_4k(k):
    """Rosa's graceful labelling of the loop with 4k links."""
    n = 4 * k
    lab = []
    for i in range(n):
        if i % 2 == 0:
            lab.append(i // 2)
        elif i < 2 * k:
            lab.append(n - i // 2)
        else:
            lab.append(n - 1 - i // 2)
    return lab


lab = rosa_cycle_4k(25)
d = sorted(abs(lab[i] - lab[(i + 1) % 100]) for i in range(100))
print("loop 100 links: Rosa labelling valid:", d == list(range(1, 101)) and len(set(lab)) == 100)

for n in range(2, 30):
    m = n - 1
    lab, lo, hi = [], 0, m
    for i in range(n):
        if i % 2 == 0:
            lab.append(lo); lo += 1
        else:
            lab.append(hi); hi -= 1
    assert sorted(abs(lab[i] - lab[i + 1]) for i in range(n - 1)) == list(range(1, n))
print("path rule 0, m, 1, m-1, ... verified for 2..29 dots")

for L, marks in ((6, 4), (10, 5)):
    rs = []
    for mid in combinations(range(1, L), marks - 2):
        pts = (0,) + mid + (L,)
        if sorted(b - a for a, b in combinations(pts, 2)) == list(range(1, L + 1)):
            rs.append(pts)
    print(f"rulers 0..{L} with {marks} counters:", rs)
print("ruler example 0, 2, 7 distances:", sorted(b - a for a, b in combinations((0, 2, 7), 2)))
print("K4:", len(graceful(*complete(4))), "labellings, e.g.", graceful(*complete(4))[0], "; K5:", len(graceful(*complete(5))))

for n in range(2, 10):
    trees = list(nx.nonisomorphic_trees(n))
    bad = sum(1 for t in trees if not graceful(n, list(t.edges()), limit=1))
    print(f"trees with {n} dots: {len(trees)} shapes, {bad} not graceful")
