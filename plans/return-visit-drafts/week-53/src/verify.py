#!/usr/bin/env python3
"""Exhaustive checks for every map and claim on the Week 53 return-visit pages.

Run: python3 verify.py   (prints results; asserts the facts the pages rely on)
"""
from itertools import combinations
from maps import MAPS


def links_of(m, prices=None):
    out = []
    for (u, v, p) in m["links"]:
        q = prices(p) if prices else p
        out.append((u, v, q))
    return out


def connected(nodes, edges, must=None):
    """True if every node in `must` (default: all nodes) is in one component."""
    must = list(must) if must is not None else list(nodes)
    if not must:
        return True
    parent = {n: n for n in nodes}

    def f(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for (u, v, _) in edges:
        parent[f(u)] = f(v)
    r = f(must[0])
    return all(f(x) == r for x in must)


def has_loop(nodes, edges):
    parent = {n: n for n in nodes}

    def f(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for (u, v, _) in edges:
        a, b = f(u), f(v)
        if a == b:
            return True
        parent[a] = b
    return False


def cost(edges):
    return sum(p for (_, _, p) in edges)


def name(edges):
    return " ".join(sorted("".join(sorted(u + v)) for (u, v, _) in edges))


def cheapest_purchases(nodes, edges, required):
    """All link sets joining the required places, at minimum cost (any size)."""
    best, sets = None, []
    for k in range(0, len(edges) + 1):
        for S in combinations(edges, k):
            if not connected(nodes, S, required):
                continue
            c = cost(S)
            if best is None or c < best:
                best, sets = c, [S]
            elif c == best:
                sets.append(S)
    return best, sets


def spanning_trees(nodes, edges):
    n = len(nodes)
    for S in combinations(edges, n - 1):
        if connected(nodes, S) and not has_loop(nodes, S):
            yield S


def routes(edges, s, t):
    """All simple routes from s to t, as (letters, list of prices)."""
    adj = {}
    for (u, v, p) in edges:
        adj.setdefault(u, []).append((v, p))
        adj.setdefault(v, []).append((u, p))
    out = []

    def go(x, path, prices):
        if x == t:
            out.append(("".join(path), prices[:]))
            return
        for (y, p) in adj.get(x, []):
            if y not in path:
                path.append(y); prices.append(p)
                go(y, path, prices)
                path.pop(); prices.pop()
    go(s, [s], [])
    return out


def bottleneck(edges, s, t):
    rs = routes(edges, s, t)
    h = min(max(pr) for (_, pr) in rs)
    return h, sorted(r for (r, pr) in rs if max(pr) == h)


def cheapest_trips(edges, s, t):
    rs = routes(edges, s, t)
    c = min(sum(pr) for (_, pr) in rs)
    return c, sorted(r for (r, pr) in rs if sum(pr) == c)


def groups_by_price(nodes, edges):
    out = {}
    for k in sorted(set(p for (_, _, p) in edges)):
        open_ = [e for e in edges if e[2] <= k]
        parent = {n: n for n in nodes}

        def f(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for (u, v, _) in open_:
            a, b = f(u), f(v)
            if a != b:
                parent[a] = b
        comps = {}
        for n in nodes:
            comps.setdefault(f(n), []).append(n)
        out[k] = sorted("".join(sorted(c)) for c in comps.values())
    return out


def tree_route(tree, s, t):
    rs = routes(tree, s, t)
    assert len(rs) == 1
    return rs[0]


def report_network(key, prices=None, label=""):
    m = MAPS[key]
    nodes = m["places"]
    E = links_of(m, prices)
    trees = list(spanning_trees(nodes, E))
    best = min(cost(T) for T in trees)
    cheapest = [T for T in trees if cost(T) == best]
    plists = sorted(set(tuple(sorted(p for (_, _, p) in T)) for T in cheapest))
    print(f"{key}{label}: cheapest network cost {best}, {len(cheapest)} cheapest: "
          + "; ".join(name(T) for T in cheapest) + f"; price lists {plists}")
    return best, cheapest, E


# ---------------------------------------------------------------- checks
print("== Networks and price lists ==")
b, ch, E = report_network("tie4")
assert b == 4 and len(ch) == 3
b, ch, E = report_network("kmap")
assert b == 9 and len(ch) == 2
g = groups_by_price(MAPS["kmap"]["places"], E)
print("  kmap groups:", g)
assert g[1] == ["AB", "C", "D", "EF"] and g[2] == ["ABC", "DEF"] and g[3] == ["ABCDEF"]
# K-1 P3: no network without a 3- or 4-dot link
small = [e for e in E if e[2] <= 2]
assert not connected(MAPS["kmap"]["places"], small)
print("  kmap: links of 1 or 2 dots alone cannot join every place (correct)")

b, ch, E = report_network("vmap")
assert b == 9 and len(ch) == 6
nodes = MAPS["vmap"]["places"]
g = groups_by_price(nodes, E)
print("  vmap groups:", g)
counts = [len(nodes)] + [len(g[k]) for k in sorted(g)]
print("  vmap group counts c0..:", counts, " sum(c_k - 1) =", sum(c - 1 for c in counts[:-1]))
for pair in ["AD", "BD", "DF", "AF"]:
    h, rs = bottleneck(E, pair[0], pair[1])
    first = min(k for k in g if any(pair[0] in c and pair[1] in c for c in g[k]))
    print(f"  vmap {pair}: lowest top price {h} via {rs}; first share a group at {first}")
    assert h == first
    for T in ch:  # theorem: every cheapest network route has top price h
        r, pr = tree_route(T, pair[0], pair[1])
        assert max(pr) == h
print("  vmap: every cheapest network's route has the lowest top price for every pair:",
      all(max(tree_route(T, u, v)[1]) == bottleneck(E, u, v)[0]
          for T in ch for (u, v) in combinations(nodes, 2)))

for pair in ["AD", "BD", "DF", "AF"]:  # 2-3 P2/P3 and 4-5 P1/P3 answers
    print(f"  vmap {pair}: lowest top price {bottleneck(E, pair[0], pair[1])[0]}")
assert [bottleneck(E, p[0], p[1])[0] for p in ["AD", "BD", "DF", "AF"]] == [2, 2, 4, 4]
assert counts == [6, 3, 2, 2, 1, 1]

print("\n== Five-place tie map (4-5 P4) ==")
b, ch, E = report_network("tie5")
nodes = MAPS["tie5"]["places"]
g = groups_by_price(nodes, E)
counts = [len(nodes)] + [len(g[k]) for k in sorted(g)]
print("  tie5 groups:", g, "counts", counts)
assert b == 6 and len(ch) == 3
assert set(tuple(sorted(p for (_, _, p) in T)) for T in ch) == {(1, 1, 2, 2)}
assert g[1] == ["ABC", "D", "E"] and g[2] == ["ABCDE"]
assert sum(c - 1 for c in counts[:-1]) == 6
shapes = sorted(sorted(sum(1 for (u, v, _) in T if x in (u, v)) for x in nodes) for T in ch)
print("  degree sequences of the three cheapest networks:", shapes)

print("\n== Sam's square (4-5) ==")
m = MAPS["samsq"]; E = links_of(m)
trees = list(spanning_trees(m["places"], E))
for T in trees:
    print("  ", name(T), "cost", cost(T), "most expensive", max(p for (_, _, p) in T))
assert min(max(p for (_, _, p) in T) for T in trees) == 3
assert any(cost(T) == 9 and max(p for (_, _, p) in T) == 3 for T in trees)
assert min(cost(T) for T in trees) == 7

print("\n== Trips ==")
for key, s, t, changes in [("cycle4", "A", "D", [("original", None), ("+1", lambda p: p + 1), ("+2", lambda p: p + 2)]),
                           ("sixmap", "A", "F", [("original", None), ("+2", lambda p: p + 2),
                                                 ("x2", lambda p: 2 * p), ("squared", lambda p: p * p)])]:
    for (lab, fn) in changes:
        b, ch, E = report_network(key, fn, f" [{lab}]")
        c, trips = cheapest_trips(E, s, t)
        own = [sum(tree_route(T, s, t)[1]) for T in ch]
        print(f"    cheapest {s}-{t} trip {c} via {trips}; along the cheapest network {own}")

print("\n== Optional places ==")
for key in ["star", "star3", "star224", "diamondx", "twosq", "sixAF", "optex"]:
    m = MAPS[key]
    E = links_of(m)
    req = [p for p in m["places"] if p not in m.get("optional", [])]
    best, sets = cheapest_purchases(m["places"], E, req)
    # cheapest without any optional place
    Eno = [e for e in E if e[0] in req and e[1] in req]
    bno, sno = cheapest_purchases(req, Eno, req)
    print(f"{key}: required {req}; cheapest {best} ({len(sets)} ways: "
          + "; ".join(name(S) for S in sets) + f"); without optional places {bno} ({len(sno)} ways)")
    if key == "star":
        assert best == 6 and len(sets) == 1 and bno == 8
    if key == "star3":
        assert best == 8 and len(sets) == 3 and bno == 8
        # with the square (S used): cheapest that uses S
        withS = [S for k in range(len(E) + 1) for S in combinations(E, k)
                 if connected(m["places"], S, req) and any("S" in (u, v) for (u, v, _) in S)]
        print("   star3 cheapest using S:", min(cost(S) for S in withS))
    if key == "star224":
        assert best == 8 and len(sets) == 6
    if key == "diamondx":
        assert best == 8 and bno == 12
    if key == "twosq":
        assert best == 6 and len(sets) == 1
    if key == "sixAF":
        assert best == 8 and len(sets) == 2

# K-1 P4/P5: cheapest using the square at least once, per map
for key in ["star", "star3", "star224", "diamondx"]:
    m = MAPS[key]; E = links_of(m)
    req = [p for p in m["places"] if p not in m.get("optional", [])]
    opt = m["optional"][0]
    withS = [S for k in range(len(E) + 1) for S in combinations(E, k)
             if connected(m["places"], S, req) and any(opt in (u, v) for (u, v, _) in S)]
    print(f"  {key}: cheapest purchase that uses the square: {min(cost(S) for S in withS)}")

# twosq: costs with only S, only T
m = MAPS["twosq"]; E = links_of(m)
req = ["A", "B", "C", "D"]
for allowed in [[], ["S"], ["T"], ["S", "T"]]:
    nodes = req + allowed
    Ea = [e for e in E if e[0] in nodes and e[1] in nodes]
    print("  twosq using only squares", allowed, "->", cheapest_purchases(nodes, Ea, req)[0])

print("\n== Stuck purchase on the star map ==")
m = MAPS["star"]; E = links_of(m); req = ["A", "B", "C"]
idx = {frozenset((u, v)): i for i, (u, v, _) in enumerate(E)}
start = frozenset([idx[frozenset("AB")], idx[frozenset("BC")]])


def ok(S):
    return connected(m["places"], [E[i] for i in S], req)


def c(S):
    return sum(E[i][2] for i in S)


def neighbours(S):
    allI = set(range(len(E)))
    for i in allI - S:
        yield S | {i}
    for i in S:
        yield S - {i}
    for i in S:
        for j in allI - S:
            yield (S - {i}) | {j}


for cap in [8, 9, 10]:
    seen, frontier = {start}, [start]
    while frontier:
        S = frontier.pop()
        for T in neighbours(S):
            T = frozenset(T)
            if T not in seen and ok(T) and c(T) <= cap:
                seen.add(T); frontier.append(T)
    reach6 = any(c(S) == 6 for S in seen)
    print(f"  cap {cap}: reachable purchases {len(seen)}; cheapest purchase (6) reachable: {reach6}")
    if cap < 10:
        assert not reach6
    else:
        assert reach6
# the start is stuck: no single change keeps A,B,C joined and costs less than 8
assert all(not (ok(frozenset(T)) and c(frozenset(T)) < 8) for T in neighbours(start))
print("  AB+BC: no single change is cheaper (stuck)")

print("\n== Without the square / using it (K-1 P4-P6, 2-3 P8) ==")
expect = {"star": (8, 6), "star3": (8, 9), "star224": (8, 8), "diamondx": (12, 8)}
for key, (w_no, w_use) in expect.items():
    m = MAPS[key]; E = links_of(m)
    req = [p for p in m["places"] if p not in m.get("optional", [])]
    opt = m["optional"][0]
    Eno = [e for e in E if e[0] in req and e[1] in req]
    bno = cheapest_purchases(req, Eno, req)[0]
    withS = [S for k in range(len(E) + 1) for S in combinations(E, k)
             if connected(m["places"], S, req) and any(opt in (u, v) for (u, v, _) in S)]
    buse = min(cost(S) for S in withS)
    print(f"  {key}: without {bno}, using the square {buse}")
    assert (bno, buse) == (w_no, w_use)

print("\n== General claims on random maps with every place circled (4-5 P6, P8, P12) ==")
import random
random.seed(53)
from itertools import permutations


def all_cheapest(nodes, E):
    trees = list(spanning_trees(nodes, E))
    best = min(cost(T) for T in trees)
    return best, [T for T in trees if cost(T) == best], trees


checked = 0
for trial in range(300):
    n = random.choice([4, 5, 6])
    nodes = list("ABCDEF"[:n])
    pairs = list(combinations(nodes, 2))
    while True:
        chosen = random.sample(pairs, random.randint(n - 1, min(len(pairs), 9)))
        E = [(u, v, random.randint(1, 5)) for (u, v) in chosen]
        if connected(nodes, E):
            break
    best, ch, trees = all_cheapest(nodes, E)
    # P6: lowest-dearest route along every cheapest network, same price lists, cost from groups
    for T in ch:
        for (u, v) in pairs:
            assert max(tree_route(T, u, v)[1]) == bottleneck(E, u, v)[0]
    assert len(set(tuple(sorted(p for (_, _, p) in T)) for T in ch)) == 1
    g = groups_by_price(nodes, E)
    cnt = [n] + [len(g[k]) for k in sorted(g)]
    ks = sorted(g)
    by_formula = sum(k * ((cnt[i]) - cnt[i + 1]) for i, k in enumerate(ks))
    assert by_formula == best
    # P12 (Lee): a loop-free network meeting the route condition for every pair is cheapest
    for T in trees:
        if all(max(tree_route(T, u, v)[1]) == bottleneck(E, u, v)[0] for (u, v) in pairs):
            assert cost(T) == best
    # P8: adding 1 or 2, doubling or squaring keeps the set of cheapest networks
    names = sorted(name(T) for T in ch)
    for fn in (lambda p: p + 1, lambda p: p + 2, lambda p: 2 * p, lambda p: p * p):
        E2 = [(u, v, fn(p)) for (u, v, p) in E]
        assert sorted(name(T) for T in all_cheapest(nodes, E2)[1]) == names
    checked += 1
print(f"  {checked} random maps: all four claims hold")

print("\n== The same claims fail once squares are allowed (why P6, P8, P12 say 'no squares') ==")
m = MAPS["star224"]; E = links_of(m); req = ["A", "B", "C"]
best, sets = cheapest_purchases(m["places"], E, req)
plists = set(tuple(sorted(p for (_, _, p) in S)) for S in sets)
print("  star224 cheapest price lists:", plists)
assert len(plists) > 1
E2 = [(u, v, p + 2) for (u, v, p) in E]
b2, s2 = cheapest_purchases(m["places"], E2, req)
assert sorted(name(S) for S in s2) != sorted(name(S) for S in sets)
print("  star224: adding 2 to every price changes the cheapest networks")

print("\n== 2-3 triangle design: AB+BC < AC and AB+BC+4 > AC+2 ==")
sols = [(ab, bc, ac) for ab in range(1, 6) for bc in range(1, 6) for ac in range(1, 6)
        if ab + bc < ac and ab + bc + 4 > ac + 2]
print("  solutions with prices 1..5:", sols)
assert all(ab + bc == ac - 1 for (ab, bc, ac) in sols)

print("\n== K-1 P8 design: spokes x<=y<=z, triangle 4,4,4; cheapest join using the square costs 8 ==")
sols = []
for x in range(1, 7):
    for y in range(x, 7):
        for z in range(y, 7):
            withS = min(x + y + z, x + y + 4, x + 8)
            if withS == 8:
                sols.append((x, y, z))
print("  ", sols)
assert sols == [(1, 3, 4), (1, 3, 5), (1, 3, 6), (2, 2, 4), (2, 2, 5), (2, 2, 6), (2, 3, 3)]
# brute-force check of the same thing on the actual star layout, spokes up to 4 dots
bf = []
for x in range(1, 5):
    for y in range(x, 5):
        for z in range(y, 5):
            E = [("A", "B", 4), ("B", "C", 4), ("A", "C", 4), ("S", "A", x), ("S", "B", y), ("S", "C", z)]
            withS = [S for k in range(len(E) + 1) for S in combinations(E, k)
                     if connected(list("ABCS"), S, list("ABC")) and any("S" in (u, v) for (u, v, _) in S)]
            if min(cost(S) for S in withS) == 8:
                bf.append((x, y, z))
assert bf == [(1, 3, 4), (2, 2, 4), (2, 3, 3)]
print("   with at most 4 dots per spoke:", bf)

print("\nAll assertions passed.")
