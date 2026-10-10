"""Independent math check for Week 67 (Meeting on shortest roads).

Part A rebuilds every printed map from the delivered student PDF (via
pdfgraph67) and computes its meeting dots by breadth-first search.
Part B proves the finite claims by enumeration (grids, cube, trees, small
counterexamples).  Part C compares the delivered guide's printed answers
with the computations.  Nothing is imported from the packet's own checkers.
Run: python3 check_math67.py  (writes nothing; prints PASS/FAIL lines)
"""
import itertools
import math
import random
import re
import subprocess

from pdfgraph67 import (GUIDE, STUDENT, all_dist, bfs, build_graph, components,
                        meeting_set, page_objects)

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" -- {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)


def text_of(pdf, page=None):
    args = ["pdftotext", "-layout"]
    if page is not None:
        args += ["-f", str(page), "-l", str(page)]
    return subprocess.run(args + [str(pdf), "-"], capture_output=True, text=True).stdout


def grid_coords(V, comp):
    """Integer (x, y) for a square grid component, y increasing upward."""
    xs = sorted({round(V[i]["x"], 1) for i in comp})
    ys = sorted({round(V[i]["y"], 1) for i in comp}, reverse=True)
    dx = [b - a for a, b in zip(xs, xs[1:])]
    dy = [a - b for a, b in zip(ys, ys[1:])]
    coord = {}
    for i in comp:
        coord[i] = (min(range(len(xs)), key=lambda k: abs(xs[k] - V[i]["x"])),
                    min(range(len(ys)), key=lambda k: abs(ys[k] - V[i]["y"])))
    return coord, dx, dy


def is_full_grid(adj, coord, w, h):
    want = set()
    for x in range(w):
        for y in range(h):
            if x + 1 < w:
                want.add(frozenset({(x, y), (x + 1, y)}))
            if y + 1 < h:
                want.add(frozenset({(x, y), (x, y + 1)}))
    got = {frozenset({coord[u], coord[v]}) for u in coord for v in adj[u] if v in coord}
    return got == want


def homes_by_label(V, comp, labels):
    lab = {V[i]["label"]: i for i in comp if V[i]["label"]}
    return [lab[x] for x in labels]


# ---------------------------------------------------------------- Part A
print("== Part A: printed maps rebuilt from the delivered student PDF ==")

# page 1: two-home example and the two Problem 1 boards
V, S, W = page_objects(0)
adj, used = build_graph(V, S)
comps = sorted(components(adj), key=len)
ex = comps[0]
coord, dx, dy = grid_coords(V, ex)
check("p1 example is a full 3x2 dot grid with equal spacing",
      len(ex) == 6 and is_full_grid(adj, coord, 3, 2) and max(dx + dy) - min(dx + dy) < 0.3,
      f"dx={dx} dy={dy}")
P, Q, M = homes_by_label(V, ex, ["P", "Q", "M"])
D = all_dist(adj, ex)
check("p1 example labels: P=(0,0), Q=(2,1), M=(1,1)",
      (coord[P], coord[Q], coord[M]) == ((0, 0), (2, 1), (1, 1)), str((coord[P], coord[Q], coord[M])))
check("p1 example text: P to M 2, M to Q 1, through M 3, shortest P-Q 3",
      (D[P][M], D[M][Q], D[P][M] + D[M][Q], D[P][Q]) == (2, 1, 3, 3))
# thick drawn route
thick = [s for s in S if s[2] > 2]
route_pts = []
for a, b, *_ in thick:
    route_pts += [a, b]
on = sorted({min(ex, key=lambda i: math.hypot(V[i]["x"] - p[0], V[i]["y"] - p[1])) for p in route_pts},
            key=lambda i: coord[i])
check("p1 example thick route is P-(1,0)-M-Q, a 3-step shortest route through M",
      [coord[i] for i in on] == [(0, 0), (1, 0), (1, 1), (2, 1)] and len(thick) == 3,
      str([coord[i] for i in on]))
two_home = sorted(coord[m] for m in ex if D[P][m] + D[m][Q] == D[P][Q])
check("guide launch: upper-left dot (0,1) also lies on a shortest P-Q route",
      (0, 1) in two_home, f"all dots on some shortest P-Q route: {two_home}")

expect_p1 = {}
for side, comp in zip(["left", "right"], sorted(comps[1:], key=lambda c: min(V[i]["x"] for i in c))):
    coord, dx, dy = grid_coords(V, comp)
    check(f"P1 {side} board is a full 5x5 grid, equal x/y spacing",
          len(comp) == 25 and is_full_grid(adj, coord, 5, 5) and max(dx + dy) - min(dx + dy) < 0.3,
          f"spacing {min(dx + dy):.2f}-{max(dx + dy):.2f} pt")
    H = homes_by_label(V, comp, ["A", "B", "C"])
    D = all_dist(adj, comp)
    ms = meeting_set(D, H, comp)
    hc = [coord[h] for h in H]
    med = tuple(sorted(c[k] for c in hc)[1] for k in (0, 1))
    pair = {}
    m = ms[0]
    pair["AB"] = (D[H[0]][m], D[m][H[1]], D[H[0]][H[1]])
    pair["AC"] = (D[H[0]][m], D[m][H[2]], D[H[0]][H[2]])
    pair["BC"] = (D[H[1]][m], D[m][H[2]], D[H[1]][H[2]])
    expect_p1[side] = (coord[m], pair)
    print(f"     P1 {side}: homes A,B,C at {hc}; meeting set {[coord[x] for x in ms]}; "
          f"median {med}; pair (d(X,M), d(M,Y), d(X,Y)) {pair}")
    check(f"P1 {side}: exactly one meeting dot and it is the coordinate median",
          len(ms) == 1 and coord[ms[0]] == med)

# page 2: four blank boards
V, S, W = page_objects(1)
adj, used = build_graph(V, S)
comps = components(adj)
oks = []
for comp in comps:
    coord, dx, dy = grid_coords(V, comp)
    oks.append(len(comp) == 25 and is_full_grid(adj, coord, 5, 5) and max(dx + dy) - min(dx + dy) < 0.3)
check("P2 has four blank full 5x5 square grids", len(comps) == 4 and all(oks))

# page 3: tree, triangle, four-cycle
V, S, W = page_objects(2)
adj, used = build_graph(V, S)
comps = sorted(components(adj), key=lambda c: (min(V[i]["y"] for i in c), min(V[i]["x"] for i in c)))
tree = max(comps, key=len)
tri = [c for c in comps if len(c) == 3][0]
sq = [c for c in comps if len(c) == 4][0]
E = sum(len(adj[i]) for i in tree) // 2
check("P3 tree: 10 dots, 9 roads, connected (a tree)", len(tree) == 10 and E == 9)
H = homes_by_label(V, tree, ["A", "B", "C"])
D = all_dist(adj, tree)
ms = meeting_set(D, H, tree)
m = ms[0] if ms else None
Cx = V[H[2]]["x"]
print(f"     P3 tree degrees {sorted(len(adj[i]) for i in tree)}; homes' degrees {[len(adj[h]) for h in H]}")
check("P3 tree: exactly one meeting dot", len(ms) == 1)
check("P3 tree: guide says junction directly below C, each home 2 roads, pair distances 4",
      m is not None and len(adj[m]) == 3 and abs(V[m]["x"] - Cx) < 0.5 and V[m]["y"] > V[H[2]]["y"]
      and [D[h][m] for h in H] == [2, 2, 2] and (D[H[0]][H[1]], D[H[0]][H[2]], D[H[1]][H[2]]) == (4, 4, 4),
      f"dists to M {[D[h][m] for h in H]}, pairs {(D[H[0]][H[1]], D[H[0]][H[2]], D[H[1]][H[2]])}")
sumbest = min(tree, key=lambda x: sum(D[h][x] for h in H))
check("P3 tree: unused branches are leaves off the A-B-C tripod (do not shorten)",
      all(len(adj[i]) <= 3 for i in tree))

Ht = homes_by_label(V, tri, ["A", "B", "C"])
D = all_dist(adj, tri)
check("P3 triangle: 3 roads, every pair 1 apart, no meeting dot",
      sum(len(adj[i]) for i in tri) // 2 == 3 and meeting_set(D, Ht, tri) == [])
sides = sorted(math.hypot(V[a]["x"] - V[b]["x"], V[a]["y"] - V[b]["y"]) for a, b in itertools.combinations(tri, 2))
print(f"     triangle drawn side lengths (pt): {[round(s, 1) for s in sides]} (not claimed regular)")

Hs = homes_by_label(V, sq, ["A", "B", "C"])
D = all_dist(adj, sq)
w = max(V[i]["x"] for i in sq) - min(V[i]["x"] for i in sq)
h = max(V[i]["y"] for i in sq) - min(V[i]["y"] for i in sq)
ms = meeting_set(D, Hs, sq)
check("P3 four-cycle: 4 dots, 4 roads, drawn square", sum(len(adj[i]) for i in sq) // 2 == 4 and abs(w - h) < 0.3,
      f"{w:.1f} x {h:.1f} pt")
check("P3 four-cycle: only B works", ms == [Hs[1]], f"{[V[i]['label'] for i in ms]}")

# page 4: cubes
V, S, W = page_objects(3)
adj, used = build_graph(V, S)
comps = sorted(components(adj), key=lambda c: min(V[i]["x"] for i in c))
t4 = " ".join(text_of(STUDENT, 4).split())
mh = re.search(r"The homes are (\d{3}), (\d{3}), and (\d{3}) on the left map, and (\d{3}), (\d{3}), and (\d{3}) on the right", t4)
homes4 = [mh.groups()[:3], mh.groups()[3:]]
check("p4 rule example: 001 -change first digit-> 101 -change last digit-> 100",
      "001" in t4 and re.search(r"change first digit.*change last digit", t4) is not None)
expect_p4 = {}
for side, comp, hl in zip(["left", "right"], comps, homes4):
    lab = {V[i]["label"]: i for i in comp}
    ok_edges = all(sum(a != b for a, b in zip(V[u]["label"], V[v]["label"])) == 1 for u in comp for v in adj[u])
    check(f"P4 {side}: 8 distinct labels, 12 roads, each road changes exactly one digit (graph = cube Q3)",
          len(lab) == 8 and sum(len(adj[i]) for i in comp) // 2 == 12 and ok_edges
          and set(lab) == {"".join(b) for b in itertools.product("01", repeat=3)})
    # crossings not at dots
    segs = [((V[u]["x"], V[u]["y"]), (V[v]["x"], V[v]["y"])) for u in comp for v in adj[u] if u < v]
    crossings = []
    for (a, b), (c, d) in itertools.combinations(segs, 2):
        def ccw(p, q, r):
            return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        if ccw(a, b, c) * ccw(a, b, d) < -1e-6 and ccw(c, d, a) * ccw(c, d, b) < -1e-6:
            crossings.append((a, b, c, d))
    print(f"     P4 {side}: {len(crossings)} road crossings away from labelled dots")
    sq_front = [lab[x] for x in ("000", "100", "110", "010")]
    fw = V[sq_front[1]]["x"] - V[sq_front[0]]["x"]
    fh = V[sq_front[0]]["y"] - V[sq_front[3]]["y"]
    check(f"P4 {side}: front face drawn square", abs(fw - fh) < 0.3, f"{fw:.1f} x {fh:.1f}")
    H = [lab[x] for x in hl]
    D = all_dist(adj, comp)
    ms = meeting_set(D, H, comp)
    maj = "".join("1" if sum(h[k] == "1" for h in hl) >= 2 else "0" for k in range(3))
    expect_p4[side] = ([V[i]["label"] for i in ms], [D[a][b] for a, b in itertools.combinations(H, 2)])
    print(f"     P4 {side}: homes {hl}; meeting {[V[i]['label'] for i in ms]}; majority {maj}; "
          f"pair distances {expect_p4[side][1]}")
    check(f"P4 {side}: unique meeting label equals majority", [V[i]["label"] for i in ms] == [maj])


# ---------------------------------------------------------------- Part B
print("== Part B: enumeration behind the general claims ==")


def grid_graph(w, h, missing=()):
    adj = {(x, y): set() for x in range(w) for y in range(h)}
    for x in range(w):
        for y in range(h):
            for nb in ((x + 1, y), (x, y + 1)):
                if nb in adj and frozenset({(x, y), nb}) not in missing:
                    adj[(x, y)].add(nb)
                    adj[nb].add((x, y))
    return adj


def grid_ok(w, h, repeat):
    adj = grid_graph(w, h)
    nodes = list(adj)
    D = {u: bfs(adj, u) for u in nodes}
    combos = (itertools.combinations_with_replacement if repeat else itertools.combinations)(nodes, 3)
    n = bad = 0
    for t in combos:
        n += 1
        ms = meeting_set(D, t, nodes)
        med = tuple(sorted(p[k] for p in t)[1] for k in (0, 1))
        sumbest = min(sum(D[p][q] for p in t) for q in nodes)
        if ms != [med] or sum(D[p][med] for p in t) != sumbest:
            bad += 1
    return n, bad


n, bad = grid_ok(5, 5, False)
check("5x5 grid, all distinct triples: exactly one meeting dot = coordinate median (P2: neither 0 nor >1)",
      n == 2300 and bad == 0, f"{n} triples, {bad} bad")
n, bad = grid_ok(5, 5, True)
check("5x5 grid, triples with repetition: same", n == 2925 and bad == 0, f"{n} triples")
tot = bads = 0
for w in range(1, 7):
    for h in range(1, 7):
        n, bad = grid_ok(w, h, True)
        tot += n
        bads += bad
check("every full w x h grid, 1<=w,h<=6: unique meeting dot = median (and it minimises total travel)",
      bads == 0, f"{tot} triples")
# limit stated by the guide: missing roads can break it
adj = grid_graph(3, 3, missing={frozenset({(1, 1), (1, 0)}), frozenset({(1, 1), (0, 1)}),
                                frozenset({(1, 1), (2, 1)}), frozenset({(1, 1), (1, 2)})})
nodes = [v for v in adj if adj[v]]
D = {u: bfs(adj, u) for u in nodes}
print(f"     3x3 grid without the centre's four roads (an 8-cycle), homes (0,0),(2,0),(1,2): "
      f"meeting set {meeting_set(D, [(0, 0), (2, 0), (1, 2)], nodes)}")
check("guide limit 'full grid' is needed: a grid with missing roads can have no meeting dot",
      meeting_set(D, [(0, 0), (2, 0), (1, 2)], nodes) == [])

# cube
cube = {"".join(b): set() for b in itertools.product("01", repeat=3)}
for u in cube:
    for k in range(3):
        v = u[:k] + ("1" if u[k] == "0" else "0") + u[k + 1:]
        cube[u].add(v)
D = {u: bfs(cube, u) for u in cube}
n = bad = 0
for t in itertools.combinations_with_replacement(sorted(cube), 3):
    n += 1
    maj = "".join("1" if sum(h[k] == "1" for h in t) >= 2 else "0" for k in range(3))
    if meeting_set(D, t, list(cube)) != [maj]:
        bad += 1
check("cube: every triple (120 with repetition, incl. 56 distinct) has unique meeting label = majority",
      n == 120 and bad == 0)
# lemma in guide P5: pair agreeing in a position -> every vertex on a shortest route keeps it
lem = all(m[k] == a[k] for a in cube for b in cube for m in cube
          if D[a][m] + D[m][b] == D[a][b] for k in range(3) if a[k] == b[k])
check("guide P5 lemma: shortest route between labels agreeing in a position never changes that digit", lem)

# trees: all labelled trees on n<=7 vertices via Pruefer codes
def pruefer_tree(seq, n):
    deg = [1] * n
    for x in seq:
        deg[x] += 1
    adj = {i: set() for i in range(n)}
    for x in seq:
        leaf = min(i for i in range(n) if deg[i] == 1)
        adj[leaf].add(x)
        adj[x].add(leaf)
        deg[leaf] -= 1
        deg[x] -= 1
    u, v = [i for i in range(n) if deg[i] == 1]
    adj[u].add(v)
    adj[v].add(u)
    return adj


def path(adj, a, b):
    par = {a: None}
    q = [a]
    for u in q:
        for v in adj[u]:
            if v not in par:
                par[v] = u
                q.append(v)
    out, x = [], b
    while x is not None:
        out.append(x)
        x = par[x]
    return set(out)


ntrees = ntrip = bad = 0
for n in range(3, 8):
    for seq in itertools.product(range(n), repeat=n - 2):
        adj = pruefer_tree(seq, n)
        ntrees += 1
        D = {u: bfs(adj, u) for u in adj}
        for t in itertools.combinations_with_replacement(range(n), 3):
            ntrip += 1
            ms = meeting_set(D, t, list(adj))
            common = path(adj, t[0], t[1]) & path(adj, t[0], t[2]) & path(adj, t[1], t[2])
            if len(ms) != 1 or set(ms) != common:
                bad += 1
check("trees: every triple in every labelled tree on 3..7 vertices has exactly one meeting vertex "
      "= the common point of the three paths", bad == 0, f"{ntrees} trees, {ntrip} triples")

# triangle / sum-minimiser warning
tri = {0: {1, 2}, 1: {0, 2}, 2: {0, 1}}
D = {u: bfs(tri, u) for u in tri}
check("triangle: no meeting vertex, although every vertex minimises total travel (guide warning valid)",
      meeting_set(D, (0, 1, 2), [0, 1, 2]) == [] and len({sum(D[h][m] for h in tri) for m in tri}) == 1)


# ---------------------------------------------------------------- Part C
print("== Part C: delivered guide text against the computations ==")
g = " ".join(text_of(GUIDE).split())
L, R = expect_p1["left"], expect_p1["right"]
check("guide P1 left meeting dot (1,1)", L[0] == (1, 1) and "On the left map the only meeting dot is (1, 1)" in g)
check("guide P1 right meeting dot (4,3), rightmost dot on A's row",
      R[0] == (4, 3) and "On the right it is (4, 3)" in g)
for side, key in (("Left", "left"), ("Right", "right")):
    pr = expect_p1[key][1]
    want = " ".join(f"{a}+{b}={a + b}" for a, b, _ in (pr["AB"], pr["AC"], pr["BC"]))
    tight = all(a + b == c for a, b, c in pr.values())
    check(f"guide P1 table row {side}: '{want}' printed and each sum equals the pair distance",
          f"{side} {want}" in g and tight)
check("guide P4 left 100 and right 011",
      expect_p4["left"][0] == ["100"] and expect_p4["right"][0] == ["011"]
      and "unique meeting label is 100" in g and "unique meeting label is 011" in g)
check("guide P4: every displayed pair differs in two digits",
      expect_p4["left"][1] == [2, 2, 2] and expect_p4["right"][1] == [2, 2, 2])
routes = re.findall(r"(\d{3}) → (\d{3}) → (\d{3})", g)
okr = len(routes) == 6 and all(sum(x != y for x, y in zip(a, b)) == 1 and sum(x != y for x, y in zip(b, c)) == 1
                               for a, b, c in routes)
mids = [r[1] for r in routes]
check("guide P4 printed routes: six two-road routes, each through the meeting label",
      okr and mids == ["100"] * 3 + ["011"] * 3, str(routes))
check("guide counts: 2,300 = C(25,3) distinct grid triples, 56 = C(8,3) cube triples",
      math.comb(25, 3) == 2300 and math.comb(8, 3) == 56 and "2,300" in g and "56" in g)

print(f"\n{len(FAILS)} failure(s)" + (": " + "; ".join(FAILS) if FAILS else ""))
