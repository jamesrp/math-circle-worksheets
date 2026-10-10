#!/usr/bin/env python3
"""Independent math check for Week 69 (Thin and fat road triangles).

Reads tree coordinates/edges and grid sizes from the student TeX source,
then verifies every numbered claim on the student pages and in the adult guide
by BFS on explicit graphs (no Manhattan shortcut), including padded grids and
subdivided (continuous-edge) versions.  Finds the repo four folders up.
"""
import re, random, itertools
from collections import deque
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
SRC = REPO / "lowell-math-circle-year-2/source/week-69"
TEX = (SRC / "student/students.tex").read_text()
GUIDE = (SRC / "guide/facilitator.tex").read_text()

def bfs(adj, sources):
    d = {s: 0 for s in sources}; q = deque(sources)
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v] = d[u] + 1; q.append(v)
    return d

def count_shortest(adj, s, t):
    d = bfs(adj, [s]); ways = {s: 1}
    for u in sorted(d, key=d.get):
        for v in adj[u]:
            if d.get(v) == d[u] + 1:
                ways[v] = ways.get(v, 0) + ways[u]
    return d[t], ways[t]

def grid_graph(x0, y0, x1, y1):
    adj = {}
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            adj[(x, y)] = [(x + dx, y + dy) for dx, dy in ((1,0),(-1,0),(0,1),(0,-1))
                           if x0 <= x + dx <= x1 and y0 <= y + dy <= y1]
    return adj

def gaps(adj, sides):
    """sides: list of 3 vertex sets. Returns {(side_index, dot): gap}."""
    out = {}
    for i, S in enumerate(sides):
        others = set().union(*(sides[j] for j in range(3) if j != i))
        d = bfs(adj, list(others))
        for p in S:
            out[(i, p)] = d[p]
    return out

print("== Diagrams on page 1/2 ==")
# P-Q example: grid 2x1, route (0,0)-(1,0)-(1,1)-(2,1)
m = re.search(r"grid \(2,1\).*?\\draw\[line width=2pt\] (\S+);", TEX, re.S)
pts = [tuple(map(int, c.strip("()").split(","))) for c in m.group(1).split("--")]
adj = grid_graph(0, 0, 2, 1)
L, W = count_shortest(adj, (0, 0), (2, 1))
assert all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(pts, pts[1:]))
print("P-Q route", pts, "uses", len(pts) - 1, "roads; shortest =", L, "; #shortest routes =", W)
assert len(pts) - 1 == L == 3
# gap example: 3x2 grid, dark side x=3, P=(0,1)
adj = grid_graph(0, 0, 3, 2)
d = bfs(adj, [(3, y) for y in range(3)])
print("Gap example: P=(0,1) distance to dark side x=3 is", d[(0, 1)])
assert d[(0, 1)] == 3

print("\n== Problem 1 / 5: printed trees ==")
trees = {}
for name in ("treeone", "treetwo"):
    body = re.search(r"\\newcommand\{\\" + name + r"\}\{(.*?)\n\\foreach \\n in", TEX, re.S).group(1)
    coords = {n: (int(x), int(y)) for n, x, y in re.findall(r"(\w)/(-?\d)/(-?\d)", body)}
    draw = re.search(r"\\draw\[line width=\.9pt\] (.*?);", body).group(1)
    edges = []
    for chain in re.findall(r"((?:\(\w\)--)+\(\w\))", draw):
        ns = re.findall(r"\((\w)\)", chain)
        edges += list(zip(ns, ns[1:]))
    trees[name] = (coords, edges)

def seg_contains(a, b, p):
    (ax, ay), (bx, by), (px, py) = a, b, p
    cross = (bx-ax)*(py-ay) - (by-ay)*(px-ax)
    return cross == 0 and min(ax,bx) <= px <= max(ax,bx) and min(ay,by) <= py <= max(ay,by)

def segs_cross(a, b, c, d):
    def o(p, q, r):
        v = (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0]); return (v > 0) - (v < 0)
    return o(a,b,c)*o(a,b,d) < 0 and o(c,d,a)*o(c,d,b) < 0

total = 0
for name, (coords, edges) in trees.items():
    V = list(coords); adj = {v: [] for v in V}
    for u, v in edges: adj[u].append(v); adj[v].append(u)
    connected = len(bfs(adj, [V[0]])) == len(V)
    assert connected and len(edges) == len(V) - 1
    # drawing sanity: no edge passes through a non-endpoint dot; no crossings
    for u, v in edges:
        for p in V:
            if p not in (u, v): assert not seg_contains(coords[u], coords[v], coords[p]), (u, v, p)
    for (u, v), (s, t) in itertools.combinations(edges, 2):
        if len({u, v, s, t}) == 4: assert not segs_cross(coords[u], coords[v], coords[s], coords[t])
    dist = {v: bfs(adj, [v]) for v in V}
    def path(a, b):
        p = [a]
        while p[-1] != b:
            p.append(next(w for w in adj[p[-1]] if dist[w][b] == dist[p[-1]][b] - 1))
        return p
    mult_seen = set(); maxgap = 0; n_trip = 0
    for A, B, C in itertools.combinations(V, 3):
        routes = [path(A, B), path(B, C), path(C, A)]
        for u, v in edges:
            k = sum(any({r[i], r[i+1]} == {u, v} for i in range(len(r)-1)) for r in routes)
            mult_seen.add(k)
        g = gaps(adj, [set(r) for r in routes])
        maxgap = max(maxgap, max(g.values())); n_trip += 1
    print(f"{name}: {len(V)} dots, {len(edges)} roads, tree={connected}; triples={n_trip}; "
          f"road multiplicities seen={sorted(mult_seen)}; max gap={maxgap}")
    assert mult_seen <= {0, 2} and maxgap == 0
    total += n_trip
print("total printed-tree triples:", total)
assert total == 385

# random trees: general claim (Problems 1,5; guide overview)
random.seed(69)
for trial in range(400):
    nv = random.randint(3, 25); adj = {i: [] for i in range(nv)}; edges = []
    for i in range(1, nv):
        j = random.randrange(i); adj[i].append(j); adj[j].append(i); edges.append((i, j))
    dist = {v: bfs(adj, [v]) for v in adj}
    def path(a, b):
        p = [a]
        while p[-1] != b:
            p.append(next(w for w in adj[p[-1]] if dist[w][b] == dist[p[-1]][b] - 1))
        return p
    for A, B, C in random.sample(list(itertools.combinations(range(nv), 3)), min(30, nv*(nv-1)*(nv-2)//6)):
        routes = [path(A, B), path(B, C), path(C, A)]
        es = [set(frozenset(e) for e in zip(r, r[1:])) for r in routes]
        for e in edges: assert sum(frozenset(e) in s for s in es) in (0, 2)
        assert max(gaps(adj, [set(r) for r in routes]).values()) == 0
print("400 random trees x up to 30 triples: all road multiplicities in {0,2}, all gaps 0")

print("\n== Problems 2-4: corner triangles A=(0,0), B=(n,0), C=(n,n) ==")
sizes2 = [int(s) for s in re.findall(r"\\grid\{(\d)\}\\corners\{\1\}", TEX)]
print("printed grid sizes (P2 then P3):", sizes2)
assert sizes2 == [4, 4, 2, 4, 6]
def monotone_paths(n):
    for east in itertools.combinations(range(2*n), n):
        x = y = 0; p = [(0, 0)]
        for i in range(2*n):
            if i in east: x += 1
            else: y += 1
            p.append((x, y))
        yield p
summary = {}
for n in range(1, 8):
    adj = grid_graph(0, 0, n, n)
    lab, wab = count_shortest(adj, (0, 0), (n, 0))
    lbc, wbc = count_shortest(adj, (n, 0), (n, n))
    lac, wac = count_shortest(adj, (0, 0), (n, n))
    assert (lab, wab, lbc, wbc, lac) == (n, 1, n, 1, 2*n)
    AB = {(x, 0) for x in range(n+1)}; BC = {(n, y) for y in range(n+1)}
    pad = grid_graph(-n-2, -n-2, 2*n+2, 2*n+2)          # same triangle inside a larger grid
    best = -1; argbest = []; zero = []; count = 0; ge2 = 0; bound_ok = True
    for p in monotone_paths(n):
        AC = set(p); count += 1
        g = gaps(adj, [AB, BC, AC]); mg = max(g.values())
        # guide's bound: AC dot (x,y) has gap <= min(y, n-x); AB/BC dots <= n
        for (i, q), v in g.items():
            if i == 2 and v > min(q[1], n - q[0]): bound_ok = False
            if i < 2 and v > n: bound_ok = False
        if n <= 4:
            assert max(gaps(pad, [AB, BC, AC]).values()) == mg   # outside roads do not change it
        if mg > best: best, argbest = mg, [p]
        elif mg == best: argbest.append(p)
        if mg == 0: zero.append(p)
        if mg >= 2: ge2 += 1
    lefttop = [(0, y) for y in range(n+1)] + [(x, n) for x in range(1, n+1)]
    botright = [(x, 0) for x in range(n+1)] + [(n, y) for y in range(1, n+1)]
    assert bound_ok and best == n and argbest == [lefttop] and zero == [botright]
    summary[n] = (count, best, ge2)
    print(f"n={n}: AB,BC unique shortest (len {n}); {count} shortest AC routes; max gap={best} "
          f"(only left-then-top); gap-0-everywhere only bottom-then-right; routes with a gap>=2: {ge2}")
assert summary[2][0] == 6 and summary[4][0] == 70 and summary[6][0] == 924

# continuous edges: subdivide every road into 2 half-roads; thinness (in road units) of left/top triangle
for n in range(1, 7):
    N = 2*n; adj = grid_graph(0, 0, N, N)
    # keep only points on original roads (x or y even)
    keep = {p for p in adj if p[0] % 2 == 0 or p[1] % 2 == 0}
    adj = {p: [q for q in adj[p] if q in keep] for p in keep}
    AB = {(x, 0) for x in range(N+1)}; BC = {(N, y) for y in range(N+1)}
    AC = {(0, y) for y in range(N+1)} | {(x, N) for x in range(N+1)}
    mg = max(gaps(adj, [AB, BC, AC]).values()) / 2
    assert mg == n
print("continuous (half-edge) version: left/top triangle thinness exactly n for n=1..6")

print("\n== Problem 4: k -> n=k+1 ==")
for k in range(0, 12):
    n = k + 1; adj = grid_graph(0, 0, n, n)
    AB = {(x, 0) for x in range(n+1)}; BC = {(n, y) for y in range(n+1)}
    AC = {(0, y) for y in range(n+1)} | {(x, n) for x in range(n+1)}
    g = gaps(adj, [AB, BC, AC])
    assert g[(2, (0, n))] == n > k
print("k=0..11: marked top-left dot has gap k+1 > k")

print("\n== Guide Problem 2 specifics (n=4) ==")
n = 4; adj = grid_graph(0, 0, n, n)
d = bfs(adj, [(x, 0) for x in range(n+1)] + [(n, y) for y in range(n+1)])
print("top-left (0,4) distance to bottom-or-right =", d[(0, 4)])
assert d[(0, 4)] == 4

print("\n== Guide Problem 3 hint: measuring only along colored roads ==")
n = 4; adj = grid_graph(0, 0, n, n)
AB = {(x, 0) for x in range(n+1)}; BC = {(n, y) for y in range(n+1)}
over = 0; fake_opt = 0
for p in monotone_paths(n):
    AC = set(p); col = AB | BC | AC
    cadj = {q: [r for r in adj[q] if r in col and q in col and
                (abs(r[0]-q[0]) + abs(r[1]-q[1]) == 1) and
                ((q in AB and r in AB) or (q in BC and r in BC) or (q in AC and r in AC and abs(p.index(q)-p.index(r)) == 1))]
            for q in col}
    true = max(gaps(adj, [AB, BC, AC]).values()); outline = max(gaps(cadj, [AB, BC, AC]).values())
    if outline > true: over += 1
    if outline == n and true < n: fake_opt += 1
print(f"n=4: {over} of 70 AC routes have outline-only max gap larger than the true max gap; "
      f"{fake_opt} look optimal (gap 4) outline-only but are not")
assert over > 0

print("\n== Alternative modest Problem 2 example: AC = up 2, right 4, up 2 ==")
AC = {(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)}
g = gaps(adj, [AB, BC, AC]); mg = max(g.values())
print("max gap =", mg, "at", sorted(q for (i, q), v in g.items() if v == mg))
assert mg == 2
print("\nALL CHECKS PASSED")
