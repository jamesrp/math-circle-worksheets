"""Independent reviewer checks for the Week 53 return-visit guide (W53-RV-FAC-v1).

Maps are transcribed from the rendered final student PDFs (k-1, grades-2-3,
grades-4-5 in plans/return-visit-drafts/week-53). Every answer the guide prints
is recomputed by brute force over link subsets, simple routes and trips.
Run: python3 check_answers.py
"""
from itertools import combinations, product
from collections import deque

def L(s):
    out = []
    for tok in s.split():
        e, p = tok.split("=")
        out.append((e[0], e[1], int(p)))
    return out

MAPS = {
    "k1_p1_tie4": (L("AB=1 BC=1 AC=1 CD=2 AD=3"), "ABCD", ""),
    "k1_p2_kmap": (L("AB=1 AC=2 BC=2 CD=3 BD=4 CE=4 DE=2 EF=1 DF=4"), "ABCDEF", ""),
    "k1_p4_star222": (L("AB=4 BC=4 AC=4 SA=2 SB=2 SC=2"), "ABC", "S"),
    "k1_p5_star333": (L("AB=4 BC=4 AC=4 SA=3 SB=3 SC=3"), "ABC", "S"),
    "k1_p5_star224": (L("AB=4 BC=4 AC=4 SA=2 SB=2 SC=4"), "ABC", "S"),
    "k1_p6_diamond": (L("AB=4 BC=4 CD=4 DA=4 XA=2 XB=2 XC=2 XD=2"), "ABCD", "X"),
    "k1_p7_twosq": (L("AS=1 BS=1 ST=2 TC=1 TD=1 AB=3 CD=3 AC=4"), "ABCD", "ST"),
    "vmap": (L("AB=1 AC=1 BC=1 CD=2 BD=3 CE=4 DE=4 EF=1 DF=5"), "ABCDEF", ""),
    "cycle4": (L("AB=1 BC=1 CD=1 DA=4"), "ABCD", ""),
    "sixmap": (L("AB=1 BC=2 AC=3 CD=2 DE=1 EF=2 DF=4 BD=5 CE=6"), "ABCDEF", ""),
    "tie5": (L("AB=1 AC=1 BC=1 CD=2 CE=3 DE=2 AD=5 BE=6"), "ABCDE", ""),
    "samsq": (L("AB=1 BC=3 CD=3 DA=3"), "ABCD", ""),
    "sixAF": (L("AB=1 BC=2 AC=3 CD=2 DE=1 EF=2 DF=4 BD=5 CE=6"), "AF", "BCDE"),
}

def name(e):
    return "".join(sorted(e[:2]))

def connected(edges, req):
    if not req:
        return True
    adj = {}
    for u, v, _ in edges:
        adj.setdefault(u, set()).add(v); adj.setdefault(v, set()).add(u)
    start = req[0]; seen = {start}; q = [start]
    while q:
        x = q.pop()
        for y in adj.get(x, ()):
            if y not in seen:
                seen.add(y); q.append(y)
    return all(r in seen for r in req)

def cheapest(edges, req, must_use=None, forbid=()):
    best = None; sols = []
    ed = [e for e in edges if e[0] not in forbid and e[1] not in forbid]
    for r in range(1, len(ed) + 1):
        for sub in combinations(ed, r):
            if must_use and not any(must_use in e[:2] for e in sub):
                continue
            if not connected(list(sub), list(req)):
                continue
            c = sum(e[2] for e in sub)
            if best is None or c < best:
                best, sols = c, [sub]
            elif c == best:
                sols.append(sub)
    return best, sorted(sorted(name(e) for e in s) for s in sols)

def groups(edges, places, k):
    par = {p: p for p in places}
    def f(x):
        while par[x] != x:
            x = par[x]
        return x
    for u, v, w in edges:
        if w <= k:
            par[f(u)] = f(v)
    g = {}
    for p in places:
        g.setdefault(f(p), []).append(p)
    return sorted("".join(sorted(x)) for x in g.values())

def simple_routes(edges, s, t):
    adj = {}
    for u, v, w in edges:
        adj.setdefault(u, []).append((v, w)); adj.setdefault(v, []).append((u, w))
    out = []
    def go(x, path, ws):
        if x == t:
            out.append(("".join(path), ws)); return
        for y, w in adj[x]:
            if y not in path:
                go(y, path + [y], ws + [w])
    go(s, [s], [])
    return out

def minimax(edges, s, t):
    rs = simple_routes(edges, s, t)
    m = min(max(ws) for _, ws in rs)
    return m, sorted(r for r, ws in rs if max(ws) == m)

def cheapest_trips(edges, s, t):
    rs = simple_routes(edges, s, t)
    m = min(sum(ws) for _, ws in rs)
    return m, sorted(r for r, ws in rs if sum(ws) == m)

def reprice(edges, f):
    return [(u, v, f(w)) for u, v, w in edges]

def show(label, val, expect):
    ok = val == expect
    print(("OK  " if ok else "FAIL"), label, "->", val, "" if ok else f"(guide says {expect})")
    return ok

allok = True
def chk(label, val, expect):
    global allok
    allok &= show(label, val, expect)

# ---------------- K-1 ----------------
E, P, O = MAPS["k1_p1_tie4"]
chk("K1 P1 min/sets", cheapest(E, P), (4, [["AB","AC","CD"],["AB","BC","CD"],["AC","BC","CD"]]))
E, P, O = MAPS["k1_p2_kmap"]
chk("K1 P2 groups k=1", groups(E, P, 1), ["AB","C","D","EF"])
chk("K1 P2 groups k=2", groups(E, P, 2), ["ABC","DEF"])
chk("K1 P2 groups k=3", groups(E, P, 3), ["ABCDEF"])
chk("K1 P2 A-F first joins", minimax(E, "A", "F")[0], 3)
chk("K1 P3 min/sets", cheapest(E, P), (9, [["AB","AC","CD","DE","EF"],["AB","BC","CD","DE","EF"]]))
chk("K1 P3 no network avoids 3/4", cheapest([e for e in E if e[2] <= 2], P)[0], None)
for key, wo, us, us_sets in [
    ("k1_p4_star222", 8, 6, [["AS","BS","CS"]]),
    ("k1_p5_star333", 8, 9, [["AS","BS","CS"]]),
    ("k1_p5_star224", 8, 8, [["AC","AS","BS"],["AS","BC","BS"],["AS","BS","CS"]]),
]:
    E, P, O = MAPS[key]
    w = cheapest(E, P, forbid=O)
    u = cheapest(E, P, must_use="S")
    chk(f"{key} without", (w[0], len(w[1])), (wo, 3))
    chk(f"{key} using", (u[0], u[1]), (us, us_sets))
E, P, O = MAPS["k1_p5_star224"]
chk("star224 overall #cheapest", (lambda r: (r[0], len(r[1])))(cheapest(E, P)), (8, 6))
E, P, O = MAPS["k1_p6_diamond"]
w = cheapest(E, P, forbid="X"); u = cheapest(E, P, must_use="X")
chk("K1 P6 without", (w[0], len(w[1])), (12, 4))
chk("K1 P6 using", u, (8, [["AX","BX","CX","DX"]]))
E, P, O = MAPS["k1_p7_twosq"]
chk("K1 P7 min", cheapest(E, P), (6, [["AS","BS","CT","DT","ST"]]))
chk("K1 P7 no squares", cheapest(E, P, forbid="ST")[0], 10)
chk("K1 P7 only S", cheapest(E, P, forbid="T")[0], 9)
chk("K1 P7 only T", cheapest(E, P, forbid="S")[0], 9)
# K-1 P8: spokes x,y,z, triangle 4,4,4; cheapest join using S == 8 (without is 8)
sols = set()
for x, y, z in product(range(1, 13), repeat=3):
    E = L(f"AB=4 BC=4 AC=4 SA={x} SB={y} SC={z}")
    if cheapest(E, "ABC", must_use="S")[0] == 8:
        sols.add(tuple(sorted((x, y, z))))
rule = set()
for x, y, z in product(range(1, 13), repeat=3):
    t = tuple(sorted((x, y, z)))
    a, b, c = t
    if (a, b) in [(1, 3), (2, 2)] and c >= 4 or t == (2, 3, 3):
        rule.add(t)
chk("K1 P8 guide rule == brute force (prices 1..12)", sols == rule, True)
chk("K1 P8 formula min(x+y+z,x+y+4,x+8)", all(
    cheapest(L(f"AB=4 BC=4 AC=4 SA={x} SB={y} SC={z}"), "ABC", must_use="S")[0]
    == min(sum(sorted((x,y,z))), sum(sorted((x,y,z))[:2]) + 4, min(x,y,z) + 8)
    for x, y, z in product(range(1, 9), repeat=3)), True)
chk("K1 P8 1,1,6 using S", cheapest(L("AB=4 BC=4 AC=4 SA=1 SB=1 SC=6"), "ABC", must_use="S")[0], 6)

# ---------------- grades 2-3 / 4-5 shared ----------------
E, P, O = MAPS["vmap"]
six = [["AB","AC","CD","CE","EF"],["AB","AC","CD","DE","EF"],["AB","BC","CD","CE","EF"],
       ["AB","BC","CD","DE","EF"],["AC","BC","CD","CE","EF"],["AC","BC","CD","DE","EF"]]
chk("vmap min/sets (2-3 P1, 4-5 P2)", cheapest(E, P), (9, sorted(six)))
for s, t, m, r in [("A","D",2,"ACD"),("B","D",2,"BCD"),("D","F",4,"DEF"),("A","F",4,"ACEF")]:
    mm = minimax(E, s, t)
    chk(f"vmap minimax {s}-{t}", (mm[0], r in mm[1]), (m, True))
chk("vmap groups", [groups(E, P, k) for k in range(0, 5)],
    [["A","B","C","D","E","F"],["ABC","D","EF"],["ABCD","EF"],["ABCD","EF"],["ABCDEF"]])
chk("vmap counts c0..c4", [len(groups(E, P, k)) for k in range(0, 5)], [6,3,2,2,1])
# price list of all cheapest networks
pl = {tuple(sorted(dict(((name(e)), e[2]) for e in E)[n] for n in s)) for s in six}
chk("vmap price lists", pl, {(1,1,1,2,4)})

E, P, O = MAPS["cycle4"]
for lab, f, nc, trip in [("orig", lambda w: w, 3, (3, ["ABCD"])), ("+1", lambda w: w+1, 6, (5, ["AD"])),
                         ("+2", lambda w: w+2, 9, (6, ["AD"]))]:
    EE = reprice(E, f)
    chk(f"cycle4 {lab} network", cheapest(EE, P), (nc, [["AB","BC","CD"]]))
    chk(f"cycle4 {lab} A-D trip", cheapest_trips(EE, "A", "D"), trip)

E, P, O = MAPS["sixmap"]
for lab, f, nc, trip in [("orig", lambda w: w, 8, (8, ["ABCDEF","ACDEF"])),
                         ("+2", lambda w: w+2, 18, (15, ["ACDF"])),
                         ("x2", lambda w: 2*w, 16, (16, ["ABCDEF","ACDEF"])),
                         ("sq", lambda w: w*w, 14, (14, ["ABCDEF"]))]:
    EE = reprice(E, f)
    chk(f"sixmap {lab} network", cheapest(EE, P), (nc, [["AB","BC","CD","DE","EF"]]))
    chk(f"sixmap {lab} A-F trips", cheapest_trips(EE, "A", "F"), trip)
    # guide's distance table
    dist = {x: (0 if x == "A" else cheapest_trips(EE, "A", x)[0]) for x in "ABCDEF"}
    print("     ", lab, "distances", dist)
chk("sixmap +2 network route A-F cost", 3+4+4+3+4, 18)

# 2-3 P6: AB=a, BC=b, AC=c; through B strictly cheaper; after +2 direct strictly cheaper
sol = [(a,b,c) for a,b,c in product(range(1,15), repeat=3) if a+b < c and c+2 < a+b+4]
chk("2-3 P6 rule c=a+b+1", all(c == a+b+1 for a,b,c in sol) and len(sol) > 0, True)
chk("2-3 P6 examples", all((a,b,c) in sol for a,b,c in [(1,1,3),(1,2,4),(2,2,5)]), True)

# 2-3 P7 / 4-5 P8 general (no squares): random checks of add-constant and monotone repricing
import random
random.seed(53)
def all_places_maps(trials=300):
    for _ in range(trials):
        n = random.randint(3, 5); pl = "ABCDE"[:n]
        pairs = list(combinations(pl, 2)); random.shuffle(pairs)
        k = random.randint(n-1, len(pairs))
        E = [(u, v, random.randint(1, 5)) for u, v in pairs[:k]]
        if connected(E, list(pl)):
            yield E, pl
bad_add = bad_mono = bad_dbl_trip = 0
for E, pl in all_places_maps():
    base = cheapest(E, pl)[1]
    if cheapest(reprice(E, lambda w: w+3), pl)[1] != base: bad_add += 1
    if cheapest(reprice(E, lambda w: w*w), pl)[1] != base: bad_mono += 1
    if cheapest_trips(E, pl[0], pl[-1])[1] != cheapest_trips(reprice(E, lambda w: 2*w), pl[0], pl[-1])[1]:
        bad_dbl_trip += 1
chk("random no-square maps: +3 never changes cheapest networks", bad_add, 0)
chk("random no-square maps: squaring never changes cheapest networks", bad_mono, 0)
chk("random maps: doubling never changes cheapest trips", bad_dbl_trip, 0)

# group-count cost formula and shared price list on random integer maps
bad_formula = bad_list = bad_route = 0
for E, pl in all_places_maps(250):
    best, sols = cheapest(E, pl)
    W = {name(e): e[2] for e in E}
    K = max(W.values())
    c = [len(groups(E, pl, k)) for k in range(0, K+1)]
    if best != sum(ci - 1 for ci in c): bad_formula += 1
    if len({tuple(sorted(W[x] for x in s)) for s in sols}) != 1: bad_list += 1
    for s in sols:
        T = [e for e in E if name(e) in s]
        for u, v in combinations(pl, 2):
            if minimax(T, u, v)[0] != minimax(E, u, v)[0]: bad_route += 1
chk("random: cost == sum(c_k - 1)", bad_formula, 0)
chk("random: one price list", bad_list, 0)
chk("random: every cheapest-network route is lowest-dearest", bad_route, 0)

# ---------------- grades 4-5 specific ----------------
E, P, O = MAPS["tie5"]
chk("4-5 P4 min/sets", cheapest(E, P), (6, [["AB","AC","CD","DE"],["AB","BC","CD","DE"],["AC","BC","CD","DE"]]))
chk("4-5 P4 groups k=1,2", [groups(E, P, 1), groups(E, P, 2)], [["ABC","D","E"],["ABCDE"]])
chk("4-5 P4 counts", [len(groups(E, P, k)) for k in range(0, 4)], [5,3,1,1])

E, P, O = MAPS["samsq"]
trees = []
for sub in combinations(E, 3):
    if connected(list(sub), list(P)):
        trees.append((sorted(name(e) for e in sub), sum(e[2] for e in sub), max(e[2] for e in sub)))
chk("4-5 P5 every tree has max 3", {t[2] for t in trees}, {3})
chk("4-5 P5 costs", sorted(t[1] for t in trees), [7,7,7,9])
chk("4-5 P5 dear tree", [t[0] for t in trees if t[1] == 9], [["AD","BC","CD"]])

for key, exp in [("k1_p5_star333", (8, [["AB","AC"],["AB","BC"],["AC","BC"]])),
                 ("k1_p5_star224", (8, sorted([["AB","AC"],["AB","BC"],["AC","BC"],["AS","BS","CS"],["AC","AS","BS"],["AS","BC","BS"]])))]:
    E, P, O = MAPS[key]
    chk(f"4-5 P9 {key}", cheapest(E, P), exp)
E, P, O = MAPS["k1_p5_star333"]
chk("4-5 P9 left: tree using S >= 9", cheapest(E, P, must_use="S")[0], 9)
E, P, O = MAPS["sixAF"]
chk("4-5 P9 bottom (A,F only)", cheapest(E, P), (8, [["AB","BC","CD","DE","EF"],["AC","CD","DE","EF"]]))
E, P, O = MAPS["k1_p5_star224"]
pls = {tuple(sorted({name(e): e[2] for e in E}[x] for x in s)) for s in cheapest(E, P)[1]}
chk("4-5 P6 limit: star224 price lists", pls, {(4,4),(2,2,4)})

# 4-5 P10: BFS over legal changes from {AB,BC} with a cost cap
E, P, O = MAPS["k1_p4_star222"]
W = {name(e): e[2] for e in E}
ALL = sorted(W)
def conn(S):
    return connected([(x[0], x[1], W[x]) for x in S], list("ABC"))
def reach(cap):
    start = frozenset(["AB","BC"]); seen = {start}; q = deque([start])
    while q:
        S = q.popleft()
        nbrs = []
        for x in ALL:
            if x not in S: nbrs.append(S | {x})
            else: nbrs.append(S - {x})
        for x in S:
            for y in ALL:
                if y not in S: nbrs.append((S - {x}) | {y})
        for T in nbrs:
            if T and conn(T) and sum(W[z] for z in T) <= cap and T not in seen:
                seen.add(T); q.append(T)
    return seen
chk("4-5 P10 cheapest", cheapest(E, P), (6, [["AS","BS","CS"]]))
for cap, exp in [(8, False), (9, False), (10, True)]:
    R = reach(cap)
    chk(f"4-5 P10 cap {cap} reaches 6", frozenset(["AS","BS","CS"]) in R, exp)
    if cap < 10:
        chk(f"4-5 P10 cap {cap} reachable = outer pairs", sorted(sorted(s) for s in R),
            [["AB","AC"],["AB","BC"],["AC","BC"]])
# the guide's chain
chain = [{"AB","BC","AS"}, {"BS","BC","AS"}, {"AS","BS","CS"}]
chk("4-5 P10 chain costs", [sum(W[z] for z in S) for S in chain], [10, 8, 6])
chk("4-5 P10 chain all connected", all(conn(S) for S in chain), True)

E, P, O = MAPS["k1_p7_twosq"]
best, sols = cheapest(E, P)
deg = {}
for x in sols[0]:
    for c in x: deg[c] = deg.get(c, 0) + 1
chk("4-5 P11 min & S,T degrees", (best, deg["S"], deg["T"]), (6, 3, 3))

# k-2 bound on random maps with optional places (4 required)
viol = 0
for _ in range(200):
    pl = "ABCDSTU"; req = "ABCD"
    pairs = list(combinations(pl, 2)); random.shuffle(pairs)
    E = [(u, v, random.randint(1, 4)) for u, v in pairs[:random.randint(8, 12)]]
    if not connected(E, list(req)): continue
    b, ss = cheapest(E, req)
    for s in ss:
        d = {}
        for x in s:
            for c in x: d[c] = d.get(c, 0) + 1
        if sum(1 for c in "STU" if d.get(c, 0) >= 3) > 2: viol += 1
        if any(d.get(c, 0) == 1 for c in "STU"): viol += 1
chk("random optional maps: no optional leaf, <= r-2 optional branch places", viol, 0)

# launch line X-Y-Z
chk("launch trays", (0, 2, 2+3), (0, 2, 5))
chk("launch trip XYZY", 2+3+3, 8)


# Order-reversing change on the P8 map (for the review's suggested counterexample)
E, P, O = MAPS["sixmap"]
rev = cheapest(reprice(E, lambda w: 7 - w), P)
print("     sixmap with every price p -> 7-p:", rev)
chk("order-reversing change alters the cheapest network", rev[1] != [["AB","BC","CD","DE","EF"]], True)
# Lee's test on P5's cost-9 network BC, CD, DA: pair A-B
E, P, O = MAPS["samsq"]
T = [e for e in E if name(e) in ("BC","CD","AD")]
chk("P5 cost-9 network fails Lee's test at A-B (tree 3 vs map 1)", (minimax(T,"A","B")[0], minimax(E,"A","B")[0]), (3, 1))
# record boards vs answers
chk("record boards: K1 P1 4 for 3, 2-3 P1/4-5 P2 8 for 6, 4-5 P4 6 for 3", (4-3, 8-6, 6-3), (1, 2, 3))

print("\nALL OK" if allok else "\nSOME CHECKS FAILED")
