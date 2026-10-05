#!/usr/bin/env python3
"""Week 62 math check: independent verification of every printed network and of
the adult guide's answers.  Reads extracted.json (made by extract.py from the
delivered student PDF); the guide's claims below are transcribed by hand from
lowell-math-circle-year-2/week-62/week-62-facilitator.pdf and checked here.
Standard library only.  Run: python3 check.py > out_check.txt
"""
import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "extracted.json").read_text())
PT_PER_MM = 72 / 25.4
FAIL = []


def ok(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- graph tools
def adj_of(V, E):
    adj = {v: set() for v in V}
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def proper(E, col):
    return all(col[a] != col[b] for a, b in E)


def colorings(V, E, k):
    V = list(V)
    for t in itertools.product(range(1, k + 1), repeat=len(V)):
        col = dict(zip(V, t))
        if proper(E, col):
            yield col


def count_colorings(V, E, k):
    return sum(1 for _ in colorings(V, E, k))


def chi(V, E):
    if not V:
        return 0
    for k in range(1, len(V) + 1):
        if next(colorings(V, E, k), None) is not None:
            return k


def omega(V, E):
    adj = adj_of(V, E)
    best = 1 if V else 0
    for r in range(2, len(V) + 1):
        for S in itertools.combinations(V, r):
            if all(b in adj[a] for a, b in itertools.combinations(S, 2)):
                best = r
    return best


def simple_cycles(V, E):
    """All simple cycles (>=3 vertices) as canonical vertex tuples."""
    adj = adj_of(V, E)
    order = {v: i for i, v in enumerate(sorted(V))}
    found = set()

    def dfs(start, cur, path):
        for n in adj[cur]:
            if n == start and len(path) >= 3:
                cyc = tuple(path)
                # canonical: rotate to min, choose direction
                i = cyc.index(min(cyc, key=order.get))
                r = cyc[i:] + cyc[:i]
                rr = (r[0],) + tuple(reversed(r[1:]))
                found.add(min(r, rr))
            elif n not in path and order[n] > order[start]:
                dfs(start, n, path + [n])

    for s in V:
        dfs(s, s, [s])
    return sorted(found, key=lambda c: (len(c), c))


def is_cycle_in(E, cyc):
    es = {frozenset(e) for e in E}
    return len(set(cyc)) == len(cyc) >= 3 and all(
        frozenset((cyc[i], cyc[(i + 1) % len(cyc)])) in es for i in range(len(cyc)))


def bipartite(V, E):
    return chi(V, E) <= 2


def first_fit(adj, order):
    col = {}
    for v in order:
        used = {col[n] for n in adj[v] if n in col}
        s = 1
        while s in used:
            s += 1
        col[v] = s
    return col


def parse_sched(s):
    """'1: A,C; 2: B,D' -> {A:1, C:1, B:2, D:2}"""
    col = {}
    for part in s.split(";"):
        slot, cards = part.split(":")
        for c in cards.split(","):
            col[c.strip()] = int(slot)
    return col


def parse_assign(s):
    """'A1, B2, C1' -> dict"""
    return {t.strip()[0]: int(t.strip()[1:]) for t in s.split(",")}


def check_sched(V, E, col, nslots, label):
    ok(set(col) == set(V), f"{label}: schedule covers exactly {''.join(sorted(V))}")
    ok(proper(E, col), f"{label}: schedule is legal")
    ok(len(set(col.values())) == nslots, f"{label}: schedule uses {nslots} slots")


# ----------------------------------------------------------------- networks
NETS = {}
for p in DATA["pages"]:
    for i, n in enumerate(p["networks"], 1):
        NETS[(p["page"], i)] = n


def net(page, i):
    n = NETS[(page, i)]
    return n["vertices"], [tuple(e) for e in n["edges"]], n


# --------------------------------------------------------------- geometry
def seg_point_dist(p, q, c):
    (x1, y1), (x2, y2), (x0, y0) = p, q, c
    dx, dy = x2 - x1, y2 - y1
    L2 = dx * dx + dy * dy
    t = max(0, min(1, ((x0 - x1) * dx + (y0 - y1) * dy) / L2))
    return math.hypot(x1 + t * dx - x0, y1 + t * dy - y0)


def segs_cross(p1, p2, p3, p4):
    def orient(a, b, c):
        v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        return 0 if abs(v) < 1e-9 else (1 if v > 0 else -1)
    if {tuple(p1), tuple(p2)} & {tuple(p3), tuple(p4)}:
        return False
    return (orient(p1, p2, p3) * orient(p1, p2, p4) < 0 and
            orient(p3, p4, p1) * orient(p3, p4, p2) < 0)


def geometry_report(page, i, V, E, n, extra_pairs=()):
    g = n["geometry"]
    C = {v: g[v]["center_pt"] for v in V}
    r_mm = {v: g[v]["w_mm"] / 2 for v in V}
    ok(all(abs(g[v]["w_mm"] - 20) < 0.05 and abs(g[v]["h_mm"] - 20) < 0.05 for v in V),
       f"p{page} n{i}: all {len(V)} sites are round 20 mm circles")
    gaps = [(math.dist(C[a], C[b]) / PT_PER_MM - r_mm[a] - r_mm[b], a + b)
            for a, b in itertools.combinations(V, 2)]
    mg = min(gaps)
    ok(mg[0] > 2, f"p{page} n{i}: closest pair of circles {mg[1]} leaves {mg[0]:.1f} mm gap (>2 mm)")
    if E:
        vis = min((math.dist(C[a], C[b]) / PT_PER_MM - r_mm[a] - r_mm[b], a + b) for a, b in E)
        print(f"  info p{page} n{i}: shortest visible conflict line {vis[1]} = {vis[0]:.1f} mm")
    worst = None
    for a, b in list(E) + list(extra_pairs):
        for c in V:
            if c in (a, b):
                continue
            d = seg_point_dist(C[a], C[b], C[c]) / PT_PER_MM
            if worst is None or d < worst[0]:
                worst = (d, a + b, c)
    if worst:
        ok(worst[0] > 10 + 2, f"p{page} n{i}: {'lines and candidate lines' if extra_pairs else 'lines'}"
           f" clear other sites; closest {worst[1]} passes {worst[0]:.1f} mm from centre of {worst[2]}"
           f" (radius 10 mm)")
    crosses = [(a + b, c + d) for (a, b), (c, d) in itertools.combinations(E, 2)
               if segs_cross(C[a], C[b], C[c], C[d])]
    if crosses:
        print(f"  info p{page} n{i}: printed lines cross (no site at crossing): {crosses}")


# ================================================================== checks
print("== Extracted networks (from the delivered student PDF) ==")
for (pg, i), n in sorted(NETS.items()):
    print(f"p{pg} n{i}: V={''.join(n['vertices'])}  E={' '.join(a + b for a, b in n['edges'])}")
ok(len(NETS) == 18, f"18 task networks found (guide says 18): {len(NETS)}")

print("\n== Geometry of every printed network ==")
for (pg, i), n in sorted(NETS.items()):
    V, E = n["vertices"], [tuple(e) for e in n["edges"]]
    extra = ()
    if pg == 6:
        es = {frozenset(e) for e in E}
        extra = [p for p in itertools.combinations(V, 2) if frozenset(p) not in es]
    geometry_report(pg, i, V, E, n, extra)
    ok(not n["unattached_segments"], f"p{pg} n{i}: every conflict line ends at two distinct sites")

print("\n== Summary invariants of each network ==")
for (pg, i), n in sorted(NETS.items()):
    V, E = n["vertices"], [tuple(e) for e in n["edges"]]
    cyc = simple_cycles(V, E)
    odd = [c for c in cyc if len(c) % 2]
    print(f"p{pg} n{i}: chi={chi(V, E)} omega={omega(V, E)} maxdeg="
          f"{max(len(s) for s in adj_of(V, E).values())} cycles={['-'.join(c) for c in cyc]}"
          f" odd={['-'.join(c) for c in odd]}")

# ------------------------------------------------------------------ P1
print("\n== Problem 1 (p1) ==")
V, E, _ = net(1, 1)
ok(chi(V, E) == 2, "path: fewest slots 2")
check_sched(V, E, parse_sched("1: A,C; 2: B,D"), 2, "guide path schedule")
V, E, _ = net(1, 2)
ok(chi(V, E) == 2, "star: fewest slots 2")
check_sched(V, E, parse_sched("1: A; 2: B,C,D,E,F"), 2, "guide star schedule")

# ------------------------------------------------------------------ P2
print("\n== Problem 2 (p2) ==")
V, E, _ = net(2, 1)
ok(chi(V, E) == 3 and omega(V, E) == 3, "diamond: fewest 3, triangle certificate")
check_sched(V, E, parse_sched("1: A; 2: B; 3: C,D"), 3, "guide diamond schedule")
ok(omega(["A", "B", "C"], [e for e in E if set(e) <= {"A", "B", "C"}]) == 3 and
   omega(["A", "B", "D"], [e for e in E if set(e) <= {"A", "B", "D"}]) == 3,
   "guide: ABC and ABD are both triangles")
V, E, _ = net(2, 2)
ok(chi(V, E) == 4 and len(E) == 6, "complete graph: fewest 4, six lines")
check_sched(V, E, parse_sched("1: A; 2: B; 3: C; 4: D"), 4, "guide K4 schedule")
V, E, _ = net(2, 3)
ok(chi(V, E) == 2 and len(E) == 6, "every A/B to every C/D/E: fewest 2, six lines")
check_sched(V, E, parse_sched("1: A,B; 2: C,D,E"), 2, "guide K2,3 schedule")

# ------------------------------------------------------------------ P3
print("\n== Problem 3 (p3) ==")
V, E, _ = net(3, 1)
ok(chi(V, E) == 3 and omega(V, E) == 2, "five-cycle with leaf: fewest 3, largest every-pair group 2")
check_sched(V, E, parse_sched("1: A,C; 2: B,D,F; 3: E"), 3, "guide five-cycle schedule")
Vr = [v for v in V if v != "F"]
Er = [e for e in E if "F" not in e]
ok(chi(Vr, Er) == 3 and omega(Vr, Er) == 2, "guide: removing leaf F changes neither answer")
V, E, _ = net(3, 2)
ok(chi(V, E) == 2 and omega(V, E) == 2, "six-cycle with two leaves: fewest 2, largest group 2")
check_sched(V, E, parse_sched("1: A,C,E,H; 2: B,D,F,G"), 2, "guide six-cycle schedule")
Vr = [v for v in V if v not in "GH"]
Er = [e for e in E if not set(e) & {"G", "H"}]
ok(chi(Vr, Er) == 2 and omega(Vr, Er) == 2, "guide: removing leaves G,H changes neither answer")

# ------------------------------------------------------------------ P4
print("\n== Problem 4 (p4) ==")
V, E, _ = net(4, 1)
ok(chi(V, E) == 2, "upper (six-cycle, chord AD, leaf BG, isolated H): two slots work")
check_sched(V, E, parse_sched("1: A,C,E,G,H; 2: B,D,F"), 2, "guide upper schedule")
cyc = simple_cycles(V, E)
ok(sorted(len(c) for c in cyc) == [4, 4, 6], f"guide: chord AD creates two four-cycles (cycles {cyc})")
V, E, _ = net(4, 2)
ok(chi(V, E) == 3, "lower (seven-cycle, chord AD, leaf GH): two slots fail, minimum 3")
ok(is_cycle_in(E, ("A", "D", "E", "F", "G")), "guide certificate A-D-E-F-G-A is a 5-cycle")
ok(is_cycle_in(E, tuple("ABCDEFG")), "guide alternative: outer seven-cycle")
check_sched(V, E, parse_sched("1: A,C,E,H; 2: B,D,F; 3: G"), 3, "guide lower 3-slot schedule")
cyc = simple_cycles(V, E)
ok(sorted(len(c) for c in cyc) == [4, 5, 7], f"guide: chord creates a four-cycle and a five-cycle (cycles {cyc})")

# ------------------------------------------------------------------ P5
print("\n== Problem 5 (p5) ==")
V, E, _ = net(5, 1)
ok(chi(V, E) == 2, "square + EF + isolated G: two slots")
check_sched(V, E, parse_sched("1: A,C,E,G; 2: B,D,F"), 2, "guide square schedule")
ok(all(proper(E, {**parse_sched("1: A,C,E; 2: B,D,F"), "G": s}) for s in (1, 2)), "guide: G can go in either")
V, E, _ = net(5, 2)
ok(chi(V, E) == 3, "five-cycle + branch C-F-G + isolated H: minimum 3")
check_sched(V, E, parse_sched("1: A,C,G,H; 2: B,D,F; 3: E"), 3, "guide five-cycle-branch schedule")
ok(("C", "F") in E and ("F", "G") in E, "guide: branch is C-F-G")

# BFS layers in guide's concrete bridge
V, E, _ = net(5, 1)
adj = adj_of(V, E)


def layers(adj, root):
    dist, frontier, out = {root: 0}, [root], [[root]]
    while frontier:
        nxt = sorted({n for v in frontier for n in adj[v] if n not in dist})
        for n in nxt:
            dist[n] = len(out)
        if nxt:
            out.append(nxt)
        frontier = nxt
    return out


ok(layers(adj, "A") == [["A"], ["B", "D"], ["C"]], f"guide: layers from A are {{A}},{{B,D}},{{C}}: {layers(adj, 'A')}")
ok(layers(adj, "E") == [["E"], ["F"]], "guide: layers from E are {E},{F}")

# ------------------------------------------------------------------ P6
print("\n== Problem 6 (p6) ==")
for idx, name in ((1, "upper tree"), (2, "lower empty")):
    V, E, _ = net(6, idx)
    es = {frozenset(e) for e in E}
    missing = [p for p in itertools.combinations(V, 2) if frozenset(p) not in es]
    best, sols = None, []
    for k in range(0, 4):
        for add in itertools.combinations(missing, k):
            if not bipartite(V, E + list(add)):
                sols.append(add)
        if sols:
            best = k
            break
    print(f"  {name}: {len(missing)} missing pairs; minimum added lines {best}; {len(sols)} minimum solutions:"
          f" {[' '.join(a + b for a, b in s) for s in sols]}")
    if idx == 1:
        ok(best == 1, "upper: one added line is necessary and sufficient")
        ok(sorted("".join(s[0]) for s in sols) == sorted(["AC", "AE", "CE", "BD", "BF", "DF"]),
           "guide's six one-edge answers are exactly the solutions")
        cross = sorted("".join(p) for p in missing if not any(set(p) == set(s[0]) for s in sols))
        ok(cross == sorted(["AF", "CD", "DE", "EF"]), f"guide: non-answers are AF, CD, DE, EF: {cross}")
        for add, cert in [("AC", "ABC"), ("AE", "ABE"), ("CE", "CBE"), ("BD", "BAD"), ("BF", "BCF"),
                          ("DF", "DABCF")]:
            ok(is_cycle_in(E + [tuple(add)], tuple(cert)) and len(cert) % 2 == 1,
               f"guide certificate for {add}: {'-'.join(cert)}-{cert[0]} is an odd cycle")
        ok(len(missing) == 10, "guide: ten missing pairs")
    else:
        ok(best == 3, "lower: three added lines are necessary and sufficient")
        tri = sorted("".join(sorted(set().union(*s))) for s in sols)
        guide = sorted("ABC ABD ABE ABF ACD ACE ACF ADE ADF AEF BCD BCE BCF BDE BDF BEF CDE CDF CEF DEF".split())
        ok(tri == guide and all(len(set().union(*s)) == 3 for s in sols),
           "guide: every minimum solution is a triangle; the 20 listed triples are exactly them")

# ------------------------------------------------------------------ P7
print("\n== Problem 7 (p7) ==")
for idx in (1, 2):
    V, E, _ = net(7, idx)
    adj = adj_of(V, E)
    res = Counter()
    for order in itertools.permutations(V):
        col = first_fit(adj, order)
        assert proper(E, col)
        res[max(col.values())] += 1
    print(f"  network {idx}: first-fit slot counts over all 24 orders: {dict(res)}")
    ok(min(res) == 2 and max(res) == 3, f"network {idx}: first-fit fewest 2, most 3")
V, E, _ = net(7, 1)
adj = adj_of(V, E)
ok(first_fit(adj, "ABCD") == parse_assign("A1, B2, C1, D2"), "guide: order A,B,C,D gives A1,B2,C1,D2")
ok(first_fit(adj, "ADBC") == parse_assign("A1, D1, B2, C3"), "guide: order A,D,B,C gives A1,D1,B2,C3")
s0 = parse_assign("A1, D1, B2, C3")
s1 = dict(s0, D=2)
s2 = dict(s1, C=1)
ok(proper(E, s1) and proper(E, s2) and len(set(s2.values())) == 2,
   "guide repair: D 1->2 then C 3->1 legal at each step, ends {A,C}/{B,D}")
three_orders = ["".join(o) for o in itertools.permutations(V) if max(first_fit(adj, o).values()) == 3]
print(f"  orders using three slots: {three_orders}")

# ------------------------------------------------------------------ P8
print("\n== Problem 8 (p8) ==")
V, E, _ = net(8, 1)
adj = adj_of(V, E)
ok(sorted("".join(sorted(e)) for e in E) == sorted(["AH", "BH", "BC", "DH", "DE", "DF", "FG"]),
   "guide edges HA,HB,BC,HD,DE,DF,FG match the page")
res = Counter()
for order in itertools.permutations(V):
    res[max(first_fit(adj, order).values())] += 1
print(f"  first-fit slot counts over all 40320 orders: {dict(sorted(res.items()))}")
ok(max(res) == 4 and min(res) == 2 and 5 not in res, "four reachable, two reachable, five impossible")
ok(chi(V, E) == 2, "tree minimum 2")
ok(max(len(s) for s in adj.values()) == 3 and {v for v in V if len(adj[v]) == 3} == {"H", "D"},
   "guide: maximum degree 3, at H and D")
col = first_fit(adj, "ACBHEGFD")
ok(col == parse_assign("A1, C1, B2, H3, E1, G1, F2, D4"), f"guide four-slot table A,C,B,H,E,G,F,D: {col}")
col = first_fit(adj, "HABDCEFG")
ok(col == parse_assign("H1, A2, B2, D2, C1, E1, F1, G2"), f"guide two-slot order H,A,B,D,C,E,F,G: {col}")
# guide extension: root-first by distance always uses 2 on a tree with an edge (all roots, all BFS orders)
good = True
for root in V:
    L = layers(adj, root)
    for perms in itertools.product(*[itertools.permutations(l) for l in L]):
        order = [v for l in perms for v in l]
        if max(first_fit(adj, order).values()) != 2:
            good = False
ok(good, "guide extension: every root-first increasing-distance order on this tree uses 2")

# ------------------------------------------------------------------ P9
print("\n== Problem 9 (p9) ==")
V, E, _ = net(9, 1)
c3, c4 = count_colorings(V, E, 3), count_colorings(V, E, 4)
ok((c3, c4) == (24, 108), f"path: 3 slots {c3}, 4 slots {c4} (guide 24, 108)")
ok(all(count_colorings(V, E, k) == k * (k - 1) ** 3 for k in range(0, 6)), "path formula k(k-1)^3")
ok(count_colorings(V, E, 2) == 2, "guide: path with two named slots has 2")
V, E, _ = net(9, 2)
c3, c4 = count_colorings(V, E, 3), count_colorings(V, E, 4)
ok((c3, c4) == (6, 48), f"diamond: 3 slots {c3}, 4 slots {c4} (guide 6, 48)")
ok(all(count_colorings(V, E, k) == k * (k - 1) * (k - 2) ** 2 for k in range(0, 6)), "diamond formula k(k-1)(k-2)^2")
ok(count_colorings(V, E, 2) == 0, "guide: diamond has zero two-slot assignments")
# Worked example: X-Y, X fixed in slot 1
for k in (3, 4):
    n_ex = sum(1 for c in colorings(["X", "Y"], [("X", "Y")], k) if c["X"] == 1)
    print(f"  worked example X-Y with X in slot 1: {n_ex} completions when slots 1..{k} are available")
# Path assignments with unused names (guide's remark on dividing by k!)
V, E, _ = net(9, 1)
two_of_four = sum(1 for c in colorings(V, E, 4) if len(set(c.values())) == 2)
print(f"  path assignments using exactly two of four names: {two_of_four}; 108/4! = {108/24}")
ok(108 % 24 != 0, "guide: dividing 108 by 4! is not an integer, so renaming classes have different sizes")

# ------------------------------------------------------------------ worked examples
print("\n== Worked examples on student pages ==")
pg = {p["page"]: p for p in DATA["pages"]}
sf = pg[1]["small_figures"]
ok([e["ends"] for e in sf["edges"]] == [["X", "Y"], ["X 1", "Y 2"]],
   "p1 rules figure: only X-Y conflicts; finished record X1-Y2, Z1 is legal and uses 2 slots")
sf = pg[4]["small_figures"]
thick = [("-".join(e["ends"]), e["x"]) for e in sf["edges"] if e["width"] > 2]
mid = sorted(t for t, x in thick if 250 < x < 350)
right = sorted(t for t, x in thick if x >= 350)
ok(mid == ["W-X", "X-Y"], f"p4 cycle figure 'partway' thickens W-X, X-Y (caption W-X-Y): {mid}")
ok(right == ["W-X", "W-Z", "X-Y", "Y-Z"], f"p4 'back at W' thickens all four sides (W-X-Y-Z-W): {right}")
sf = pg[7]["small_figures"]
ok(sorted("-".join(e["ends"]) for e in sf["edges"]) == ["W 2-X 1", "W 2-Y 1", "W-X", "W-Y"],
   "p7 first-fit figure: X-W and Y-W conflict, X,Y share slot 1, W forced to 2")
adj = adj_of("XYW", [("X", "W"), ("Y", "W")])
ok(first_fit(adj, "XYW") == {"X": 1, "Y": 1, "W": 2}, "p7 figure order X,Y,W gives X1,Y1,W2")

# ------------------------------------------------------------------ edge cases and other readings
print("\n== Edge cases and other readings ==")
# Kits have slot headers 1-4: can any first-fit order on p7/p8 need a fifth header?
for (pg, i) in [(7, 1), (7, 2), (8, 1)]:
    V, E, _ = net(pg, i)
    adj = adj_of(V, E)
    m = max(max(first_fit(adj, o).values()) for o in itertools.permutations(V))
    ok(m <= 4, f"p{pg} n{i}: worst first-fit order needs {m} headers (kit has 4)")
ok(max(chi(n["vertices"], [tuple(e) for e in n["edges"]]) for n in NETS.values()) <= 4,
   "no printed network needs more than the kit's 4 headers")
# Guide overview p.1: "Swapping slot numbers gives a different assignment."
V, E, _ = net(9, 1)
swap34 = {1: 1, 2: 2, 3: 4, 4: 3}
fixed = [c for c in colorings(V, E, 4) if {v: swap34[s] for v, s in c.items()} == c]
print(f"  path, slots 1-4: {len(fixed)} assignments are unchanged by swapping slot numbers 3 and 4: "
      f"{[''.join(f'{v}{c[v]}' for v in V) for c in fixed]}")
ok(len(fixed) == 2, "overview's 'swapping slot numbers gives a different assignment' fails for two unused names")
# p9 worked example: the caption's 'two' holds only when slots 1-3 are available
n3 = sum(1 for c in colorings(["X", "Y"], [("X", "Y")], 3) if c["X"] == 1)
n4 = sum(1 for c in colorings(["X", "Y"], [("X", "Y")], 4) if c["X"] == 1)
ok((n3, n4) == (2, 3), f"p9 example X-Y with X in slot 1: {n3} completions (slots 1-3), {n4} (slots 1-4)")
naive = 4 * 2 * 2 * 2
print(f"  if a child carries 'two choices for the neighbour' to 4 slots on the path: {naive} instead of 108")
# Guide p.1: many lines / large degree need not demand many slots
V1, E1, _ = net(1, 2)
V2, E2, _ = net(2, 3)
V3, E3, _ = net(2, 2)
ok(chi(V1, E1) == 2 and max(len(s) for s in adj_of(V1, E1).values()) == 5,
   "star: degree 5 but 2 slots")
ok(len(E2) == len(E3) == 6 and (chi(V2, E2), chi(V3, E3)) == (2, 4), "six lines: K2,3 needs 2, K4 needs 4")
# Guide p.2 preparation arithmetic
ok((8 * 6, 8 * 6 + 8, 4 * 6, 4 * 6 + 4, 32 * 6, 32 * 6 + 32, 2 * 6, 2 * 6 + 2, 6 + 1) ==
   (48, 56, 24, 28, 192, 224, 12, 14, 7), "kit table totals")
ok(3 * 3 + 6 * 1 + 1 * 2 + 9 == 26 and 3 * 10 == 30, "print plan: 26 student sheets, 30 guide sheets")
# Count printed full-size sites (README says 104)
ok(sum(len(n["vertices"]) for n in NETS.values()) == 104, "104 full-size network circles")

# ------------------------------------------------------------------ general claims
print("\n== General statements in the guide, checked exhaustively on small graphs ==")


def all_graphs(n):
    V = [chr(65 + i) for i in range(n)]
    pairs = list(itertools.combinations(V, 2))
    for mask in range(1 << len(pairs)):
        yield V, [pairs[i] for i in range(len(pairs)) if mask >> i & 1]


bad = 0
cnt = 0
for n in range(1, 7):
    for V, E in all_graphs(n):
        cnt += 1
        has_odd = any(len(c) % 2 for c in simple_cycles(V, E))
        if bipartite(V, E) == has_odd:
            bad += 1
ok(bad == 0, f"two slots iff no odd cycle: all {cnt} labeled graphs on 1-6 vertices")

bad = 0
for n in range(1, 6):
    for V, E in all_graphs(n):
        adj = adj_of(V, E)
        D = max(len(s) for s in adj.values())
        x = chi(V, E)
        if omega(V, E) > x:
            bad += 1
        for order in itertools.permutations(V):
            col = first_fit(adj, order)
            m = max(col.values())
            if not proper(E, col) or m > D + 1 or m < x:
                bad += 1
ok(bad == 0, "omega <= chi; first-fit legal with chi <= slots <= maxdeg+1 (all graphs, all orders, n<=5)")

bad = 0
for n in range(1, 6):
    for V, E in all_graphs(n):
        for e in E:
            u, v = e
            Em = [f for f in E if f != e]
            # contract v into u, suppress duplicates
            Vc = [w for w in V if w != v]
            Ec = {tuple(sorted((u if a == v else a, u if b == v else b))) for a, b in Em}
            Ec = [f for f in Ec if f[0] != f[1]]
            for k in range(0, 5):
                if count_colorings(V, E, k) != count_colorings(V, Em, k) - count_colorings(Vc, Ec, k):
                    bad += 1
            break
ok(bad == 0, "deletion-contraction P_G = P_{G-e} - P_{G/e} (all graphs n<=5, k<=4)")


def prufer_trees(n):
    V = list(range(n))
    for seq in itertools.product(V, repeat=n - 2):
        deg = [1] * n
        for s in seq:
            deg[s] += 1
        E = []
        for s in seq:
            leaf = min(i for i in V if deg[i] == 1)
            E.append((leaf, s))
            deg[leaf] -= 1
            deg[s] -= 1
        u, w = [i for i in V if deg[i] == 1]
        E.append((u, w))
        yield V, E


bad = 0
for n in range(2, 7):
    for V, E in prufer_trees(n):
        adj = adj_of(V, E)
        for a, b in itertools.combinations(V, 2):
            if b in adj[a]:
                continue
            d = {a: 0}
            fr = [a]
            while fr:
                fr2 = []
                for x in fr:
                    for y in adj[x]:
                        if y not in d:
                            d[y] = d[x] + 1
                            fr2.append(y)
                fr = fr2
            if (d[b] % 2 == 1) != bipartite(V, E + [(a, b)]):
                bad += 1
        # connected two-colorable with an edge has exactly 2 named two-colorings
        if count_colorings(V, E, 2) != 2:
            bad += 1
ok(bad == 0, "tree + one edge stays two-slot iff odd tree distance; trees have exactly 2 two-slot colorings (n<=6)")

print("\nFAILURES:", len(FAIL))
for f in FAIL:
    print("  -", f)
