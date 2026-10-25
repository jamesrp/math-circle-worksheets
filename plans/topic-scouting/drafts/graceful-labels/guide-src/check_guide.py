"""Independent checks for every answer printed in the Graceful labels
facilitator guide, against the FINAL student pages.

Run:  python3 check_guide.py pagesrc/figs/registry.json > check_guide.txt
(The registry comes from running a COPY of the pages' gen.py:
cp <pages>/src/gen.py pagesrc/ && python3 pagesrc/gen.py.  The output of the
run used for the guide is in check_guide.txt. Takes about two minutes.)

The networks are typed in by hand from the rendered pages. If a registry
(figs/registry.json produced by the pages' gen.py) is given, each hand-typed
network is also compared with the drawn one, so the drawings are checked too.

A labelling is graceful when the dots get different whole numbers from 0..m (m = number of links) and the
link differences are exactly 1..m, each once. For K-1, a tower height is the
label and the single empty dot is 0 (towers taken from the tray, each at
most once, exactly one empty dot).
"""
import sys
import json
from itertools import permutations, combinations
import networkx as nx


# ------------------------------------------------------------ enumeration
def graceful_all(n, edges, fixed=None, limit=None):
    """All graceful labellings (tuples indexed by dot), by plain search over
    injective maps into 0..m with pruning on repeated differences."""
    m = len(edges)
    fixed = fixed or {}
    adj = {v: [] for v in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    order = list(nx.dfs_preorder_nodes(nx.Graph(edges), 0)) if n > 1 else [0]
    order += [v for v in range(n) if v not in order]
    lab = [None] * n
    out = []
    used, diffs = set(), set()

    def rec(i):
        if limit and len(out) >= limit:
            return
        if i == n:
            out.append(tuple(lab))
            return
        v = order[i]
        for x in ([fixed[v]] if v in fixed else range(m + 1)):
            if x in used:
                continue
            new = [abs(x - lab[w]) for w in adj[v] if lab[w] is not None]
            if len(set(new)) < len(new) or any(d in diffs for d in new):
                continue
            lab[v] = x
            used.add(x)
            diffs.update(new)
            rec(i + 1)
            lab[v] = None
            used.discard(x)
            diffs.difference_update(new)

    rec(0)
    return out


def is_graceful_labelling(edges, lab):
    m = len(edges)
    if len(set(lab)) != len(lab) or min(lab) < 0 or max(lab) > m:
        return False
    return sorted(abs(lab[a] - lab[b]) for a, b in edges) == list(range(1, m + 1))


def tower_rule(n, edges, towers):
    """K-1 printed rule: towers from the tray, each at most once, never two on
    a dot, exactly one empty dot (0). Count by brute force, independent of
    graceful_all."""
    m = len(edges)
    sols = []
    pieces = [0] + list(towers)
    for combo in permutations(pieces, n):
        if combo.count(0) != 1:
            continue
        if sorted(abs(combo[a] - combo[b]) for a, b in edges) == list(range(1, m + 1)):
            sols.append(combo)
    return sols


def path(n):
    return n, [(i, i + 1) for i in range(n - 1)]


def cycle(n):
    return n, [(i, (i + 1) % n) for i in range(n)]


def star(k):
    return k + 1, [(0, i) for i in range(1, k + 1)]


def complete(n):
    return n, list(combinations(range(n), 2))


# Networks as drawn (dot numbering follows the pages' drawing order).
FORK = (5, [(0, 1), (1, 2), (2, 3), (1, 4)])   # row of 4, extra dot under the 2nd
HTREE = (6, [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5)])   # two joined centres, two leaves each
SPIDER = (7, [(0, 1), (1, 2), (0, 3), (3, 4), (0, 5), (5, 6)])  # centre, three legs of 2
CAT = (8, [(0, 1), (1, 2), (2, 3), (1, 4), (1, 5), (2, 6), (3, 7)])
PAW = (4, [(0, 1), (1, 2), (0, 2), (2, 3)])   # launch: triangle 0,1,2 with tail 2-3

HAND = {
    "k_p1_big": path(3), "k_p2_big": path(4), "k_p3_big": path(5), "k_p4_big": FORK,
    "k_p5_big": star(3), "k_p6_big": cycle(3), "k_p7_big": cycle(4), "k_p8_big": star(4),
    "path4": path(4), "path5": path(5), "path6": path(6), "path11": path(11),
    "tree_fork": FORK, "tree_h": HTREE, "star5": star(5),
    "loop3": cycle(3), "loop4": cycle(4), "loop5": cycle(5), "loop6": cycle(6), "loop7": cycle(7),
    "loop7_track": cycle(7), "loop8_track": cycle(8), "k4": complete(4), "k5": complete(5),
    "tree_spider": SPIDER, "tree_cat": CAT,
}

ok_all = True


def check(cond, msg):
    global ok_all
    print(("  ok   " if cond else "  FAIL ") + msg)
    ok_all &= bool(cond)


if len(sys.argv) > 1:
    print("== drawn networks versus hand-typed ones ==")
    reg = json.load(open(sys.argv[1]))
    drawn = {}
    for net in reg:
        drawn.setdefault(net["name"].split("[")[0], net)
    for name, (n, e) in HAND.items():
        net = drawn[name]
        gd = nx.Graph([tuple(x) for x in net["edges"]])
        same_numbering = sorted(map(sorted, net["edges"])) == sorted(map(sorted, e))
        check(nx.is_isomorphic(gd, nx.Graph(e)) and same_numbering and len(net["pts"]) == n,
              f"{name}: {n} dots, {len(e)} links, same shape and dot numbering as drawn"
              + (f", caption '{net['caption']}'" if net["caption"] else ""))
        if net["caption"]:
            check(net["caption"] == f"cards 0 to {len(e)}", f"{name}: caption matches link count")
    paw = nx.Graph(PAW[1])
    check(not any(nx.is_isomorphic(paw, nx.Graph(e)) for _, e in HAND.values()),
          "launch network (triangle with a tail) is not any printed network")
    print()

print("== launch attempt on the triangle with a tail ==")
# PAW dots: 0 = top corner, 1 = lower left corner, 2 = lower right corner
# (the corner with three links), 3 = tail dot.  Links: top-left, top-right,
# left-right (triangle) and right-tail.
P3S = [(0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 3), (1, 2, 3)]   # rows of 3 dots (middle in centre)
P4S = [(0, 1, 2, 3), (1, 0, 2, 3)]                                # rows of 4 dots
TRI = (0, 1, 2)
STAR = (2, (0, 1, 3))                                             # the corner with three links


def lk(lab, a, b):
    return abs(lab[a] - lab[b])


def launch_problems(lab):
    """Ways a launch attempt could show a student-page answer or case.
    Returns a list of reasons (empty = clean)."""
    why = []
    for p in P3S:
        labs = sorted(lab[v] for v in p)
        if labs == [0, 1, 2]:
            why.append(f"row {tuple(lab[v] for v in p)} is a K-1 Problem 1 case (or the pages' example)")
    for p in P4S:
        labs = sorted(lab[v] for v in p)
        if labs == [0, 1, 2, 3]:
            why.append(f"row {tuple(lab[v] for v in p)} is a K-1 Problem 2 / 2-3 Problem 1 case")
    tl = sorted(lab[v] for v in TRI)
    if 0 in tl and max(tl) <= 3:
        why.append(f"triangle {tl} is a K-1 Problem 6 case")
    if sorted([lk(lab, 0, 1), lk(lab, 0, 2), lk(lab, 1, 2)]) == [1, 2, 3] and max(tl) <= 3:
        why.append(f"triangle {tl} is a loop-of-3 answer")
    sl = sorted([lab[STAR[0]]] + [lab[v] for v in STAR[1]])
    if max(sl) <= 3:
        why.append(f"star at the 3-link corner, middle {lab[STAR[0]]}, is a K-1 Problem 5 case")
    return why


def paw_links(lab):
    # in the order of the figure: top-left, left-right, top-right, tail
    return [lk(lab, 0, 1), lk(lab, 1, 2), lk(lab, 0, 2), lk(lab, 2, 3)]


old = (0, 1, 2, 4)   # draft guide: top empty, 1 and 2 on the lower corners, 4 on the tail
print("  draft attempt (top, left, right, tail) =", old, "links", paw_links(old))
for w in launch_problems(old):
    print("     shows:", w)
check(launch_problems(old) != [], "the draft's attempt shows page answers or cases (the review's must-fix)")

att = (4, 3, 1, 0)   # revised: top 4, lower left 3, lower right 1, tail empty
d = paw_links(att)
print("  revised attempt (top, left, right, tail) =", att, "links (top-left, left-right, top-right, tail):", d)
check(sorted(d) == [1, 1, 2, 3] and not is_graceful_labelling(PAW[1], att),
      "revised attempt fails: links 1, 2, 3, 1 -- two 1s and no 4")
check(launch_problems(att) == [], "revised attempt shows no row, triangle or star that is a page answer or case")
check(lk(att, 1, 2) == 2 and {att[1], att[2]} == {3, 1}, "the measured step: the 3 is two cubes taller than the 1")
check(sorted(x for x in att if x) == [1, 3, 4], "launch pieces: towers 1, 3, 4 (cards 0, 1, 3, 4)")
# all clean attempts with one empty dot and three of the towers 1-4, for the record
clean = []
for towers in combinations((1, 2, 3, 4), 3):
    for lab in permutations((0,) + towers):
        if not is_graceful_labelling(PAW[1], lab) and not launch_problems(lab):
            clean.append(lab)
print(f"  {len(clean)} clean failing attempts in all (of 96); revised one among them: {att in clean}")
print("  (the network itself can be labelled:", len(graceful_all(*PAW)), "labellings; not shown to children)")

print()
print("== K-1 (printed tower rule, brute force) ==")
s1 = tower_rule(*path(3), [1, 2])
print("  P1 path of 3, towers 1,2:", s1)
check(sorted(s1) == sorted([(1, 0, 2), (2, 0, 1), (0, 2, 1), (1, 2, 0)]), "P1 exactly 4 ways")
check(sorted(graceful_all(*path(3))) == sorted(s1), "P1 tower rule = graceful labellings")
s2 = tower_rule(*path(4), [1, 2, 3])
print("  P2 path of 4, towers 1,2,3:", s2)
check(sorted(s2) == sorted([(0, 3, 1, 2), (2, 1, 3, 0), (3, 0, 2, 1), (1, 2, 0, 3)]), "P2 exactly 4 ways")
s3 = tower_rule(*path(5), [1, 2, 3, 4])
print("  P3 path of 5:", len(s3), "ways:", s3)
check(len(s3) == 8 and (0, 4, 1, 3, 2) in s3, "P3 8 ways incl. 0-4-1-3-2")
s4 = tower_rule(*FORK, [1, 2, 3, 4])
print("  P4 fork (row of 4 = dots 0..3, dot 4 under dot 1):", len(s4), "ways:", s4)
check(len(s4) == 12 and (0, 4, 2, 3, 1) in s4, "P4 12 ways incl. left 0, branch 4, then 2, 3; below 1")
for c in range(4):
    sc = [s for s in tower_rule(*star(3), [1, 2, 3]) if s[0] == c]
    print(f"  P5 star, middle {c}: {len(sc)} ways")
    check((len(sc) > 0) == (c in (0, 3)), f"P5 middle {c} {'works' if c in (0, 3) else 'impossible'}")
for name, g, k, exp in (("P6 triangle", cycle(3), 3, {1, 2}), ("P7 square", cycle(4), 4, {1, 3})):
    sols = tower_rule(*g, list(range(1, k + 1)))
    left = {(set(range(1, k + 1)) - set(s)).pop() for s in sols}
    print(f"  {name}: {len(sols)} ways, left over {sorted(left)}; e.g. {sols[0]}")
    check(left == exp, f"{name} circle {sorted(exp)}")
s8 = tower_rule(*star(4), [1, 2, 3, 4])
mid = sorted({s[0] for s in s8})
print("  P8 star of 4: middle", mid, "(0 = empty);", len(s8), "ways")
check(mid == [0, 4] and len(s8) == 48, "P8 middle empty or 4-tower; 24 each")
# tower rule and graceful counts agree everywhere
for nm, g, t in (("P3", path(5), 4), ("P4", FORK, 4), ("P5", star(3), 3), ("P6", cycle(3), 3),
                 ("P7", cycle(4), 4), ("P8", star(4), 4)):
    check(len(tower_rule(*g, list(range(1, t + 1)))) == len(graceful_all(*g)), f"{nm} tower count = graceful count")

print()
print("== Grades 2-3 ==")
ex = {"path4": ((0, 3, 1, 2), path(4)), "path5": ((0, 4, 1, 3, 2), path(5)),
      "path6": ((0, 5, 1, 4, 2, 3), path(6)), "path11": ((0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5), path(11)),
      "fork": ((0, 4, 2, 3, 1), FORK), "H": ((0, 5, 1, 4, 2, 3), HTREE)}
for k, (lab, (n, e)) in ex.items():
    cnt = len(graceful_all(n, e))
    check(is_graceful_labelling(e, lab), f"{k}: example {lab} works; {cnt} labellings in all")
mids = sorted({s[0] for s in graceful_all(*star(5))})
check(mids == [0, 5], f"P4 star of 5: middle cards {mids}")
for n in range(3, 13):
    c = len(graceful_all(*cycle(n)))
    t = n * (n + 1) // 2
    check((c > 0) == (t % 2 == 0) == (n % 4 in (0, 3)),
          f"loop {n:2d}: {c:6d} labellings; 1+...+{n} = {t} ({'even' if t % 2 == 0 else 'odd'})")
for lab, n in (((0, 1, 3), 3), ((0, 2, 3), 3), ((0, 2, 1, 4), 4), ((0, 4, 2, 3), 4),
               ((0, 7, 1, 6, 2, 4, 3), 7), ((0, 8, 1, 7, 2, 5, 3, 4), 8)):
    check(is_graceful_labelling(cycle(n)[1], lab), f"loop {n}: {lab} works")
for n in (7, 8):
    c = len(graceful_all(*cycle(n)))
    arr = (n + 1) * len(list(permutations(range(n)))) if n < 9 else None
    print(f"  loop {n}: {c} of {arr} card arrangements work = 1 in {arr // c}")

# odd-count form of the loop argument
for n in (5, 6):
    odd = sum(1 for d in range(1, n + 1) if d % 2)
    check(odd == 3, f"loop {n}: link numbers 1..{n} contain {odd} odd numbers")

rul = lambda L, k: [p for p in ((0,) + mid + (L,) for mid in combinations(range(1, L), k - 2))
                     if sorted(b - a for a, b in combinations(p, 2)) == list(range(1, L + 1))]
check(rul(6, 4) == [(0, 1, 4, 6), (0, 2, 5, 6)], f"P8 rulers 0..6 with 4 counters: {rul(6, 4)}")
check(sorted(b - a for a, b in combinations((0, 2, 7), 2)) == [2, 5, 7], "strip example 0,2,7 -> 2,5,7")

print()
print("== Grades 4-5 ==")


def zigzag_with_skip(n):
    """Loop labelling: 0, n, 1, n-1, ... with one high value skipped
    (3k for n = 4k; 3k+2 for n = 4k+3). Returns None if n is not 0 or 3 mod 4."""
    if n % 4 == 0:
        skip = 3 * (n // 4)
    elif n % 4 == 3:
        skip = 3 * (n // 4) + 2
    else:
        return None
    highs = [h for h in range(n, -1, -1) if h != skip]
    lab, lo, hi = [], 0, 0
    for i in range(n):
        if i % 2 == 0:
            lab.append(lo)
            lo += 1
        else:
            lab.append(highs[hi])
            hi += 1
    return lab


good = all(is_graceful_labelling(cycle(n)[1], zigzag_with_skip(n))
           for n in range(3, 1001) if n % 4 in (0, 3))
check(good, "zigzag-with-one-skip labels every loop with 0 or 3 mod 4 links, 3..1000")
okskip = True
for n in range(3, 1001):
    if n % 4 not in (0, 3):
        continue
    z = zigzag_with_skip(n)
    pathd = [abs(z[i + 1] - z[i]) for i in range(n - 1)]
    steps = [pathd[i] - pathd[i + 1] for i in range(n - 2)]
    missing = sorted(set(range(1, n + 1)) - set(pathd))
    okskip &= (len(set(pathd)) == n - 1 and pathd[0] == n and missing == [z[-1]]
               and steps.count(2) == (1 if n > 3 else 0) and all(s in (1, 2) for s in steps))
check(okskip, "zigzag loop proof idea, n <= 1000: along the path part each link is one shorter than the last "
      "except once (two shorter, at the skipped label); the one length jumped over equals the last label, "
      "which the closing link to 0 supplies")
z8 = zigzag_with_skip(8)
check([abs(z8[i + 1] - z8[i]) for i in range(7)] == [8, 7, 6, 5, 3, 2, 1] and z8[-1] == 4,
      "loop of 8: links 8, 7, 6, 5, 3, 2, 1, then 4 - 0 = 4")
for n in (7, 8, 11, 12):
    print(f"  loop {n}: {zigzag_with_skip(n)}")
z100 = zigzag_with_skip(100)
check(is_graceful_labelling(cycle(100)[1], z100), "loop 100 labelled (zigzag, skipping 75)")
for n in (9, 10, 11, 12, 100, 101):
    t = n * (n + 1) // 2
    print(f"  P6 loop {n}: 1+...+{n} = {t} ({'odd: impossible' if t % 2 else 'even: parity allows it'})")

# path rule
check(all(is_graceful_labelling(path(n)[1], [i // 2 if i % 2 == 0 else n - 1 - i // 2 for i in range(n)])
          for n in range(2, 500)), "path rule 0, m, 1, m-1, ... works for 2..499 dots")

check(rul(10, 5) == [], "P7 no five-counter ruler 0..10")
# child case analysis: 0,10 fixed; 9 forces 1 (or 9 by mirror); 8 then forces 8; no fifth square
after = [x for x in (2, 3, 4, 5, 6, 7, 9) if sorted(b - a for a, b in combinations((0, 1, 8, 10, x), 2)) == list(range(1, 11))]
check(after == [], "P7 after 0,1,8,10 no fifth square works")
check(sorted({k * (5 - k) for k in range(6)}) == [0, 4, 6], "five marks: odd distances k(5-k) in {0,4,6}, never 5")
check(all(sum([x, x - 1, 8 - x, 10 - x]) == 17 for x in range(2, 8)), "a fifth counter on 2..7 adds four distances summing to 17; 3+4+5+6 = 18")
k4 = graceful_all(*complete(4))
check(len(k4) == 48 and {tuple(sorted(s)) for s in k4} == {(0, 1, 4, 6), (0, 2, 5, 6)},
      "K4: 48 labellings, label sets {0,1,4,6} or {0,2,5,6}")
check(len(graceful_all(*complete(5))) == 0, "K5: no labelling")
euler = [0, 1, 2, 3, 4, 0, 2, 4, 1, 3, 0]   # pentagon, then the star
used = sorted(tuple(sorted((euler[i], euler[i + 1]))) for i in range(10))
check(used == sorted(complete(5)[1]), "K5: pentagon-then-star walk uses each of the 10 links once and returns")
check(sum(range(1, 11)) % 2 == 1, "1+...+10 = 55 is odd")
for nn in range(4, 9):
    m = nn * (nn - 1) // 2
    need = (m + 1) // 2
    poss = any(k * (nn - k) == need for k in range(nn + 1))
    print(f"  K{nn}: {m} links, needs {need} odd differences; odd/even count {'allows' if poss else 'rules out'}")

sp = graceful_all(*SPIDER)
cat = graceful_all(*CAT)
print("  spider labellings:", len(sp), " caterpillar labellings:", len(cat))
ex_sp = (0, 6, 1, 4, 3, 2, 5)
ex_cat = (0, 7, 3, 5, 1, 2, 6, 4)
check(is_graceful_labelling(SPIDER[1], ex_sp), f"spider example {ex_sp} (centre, left near, left far, right near, right far, down near, down far)")


# caterpillar method: spine order, alternate low and high blocks
def caterpillar_method(spine_leaves):
    """spine_leaves[i] = number of leaves on spine dot i. Returns edges and a
    labelling: spine dot 0 gets 0; then its leaves and the next spine dot get
    high labels m, m-1, ... (spine dot last); then that dot's leaves and the
    next spine dot get low labels 1, 2, ...; and so on."""
    k = len(spine_leaves)
    n = k + sum(spine_leaves)
    m = n - 1
    edges, lab = [], {}
    nxt = k
    lo, hi = 0, m
    lab[0] = lo
    lo += 1
    for i in range(k):
        group = []
        for _ in range(spine_leaves[i]):
            edges.append((i, nxt))
            group.append(nxt)
            nxt += 1
        if i + 1 < k:
            edges.append((i, i + 1))
            group.append(i + 1)
        high_turn = (i % 2 == 0)
        for v in group:
            if high_turn:
                lab[v] = hi
                hi -= 1
            else:
                lab[v] = lo
                lo += 1
    return n, edges, [lab[v] for v in range(n)]


import random
random.seed(1)
okc = True
for _ in range(3000):
    k = random.randint(1, 8)
    sl = [random.randint(0, 4) for _ in range(k)]
    n, e, lab = caterpillar_method(sl)
    okc &= is_graceful_labelling(e, lab)
check(okc, "caterpillar method works on 3000 random caterpillars")
okc0 = True
for _ in range(3000):
    k = random.randint(2, 9)
    sl = [0] + [random.randint(0, 4) for _ in range(k - 1)]   # start on an end dot of a longest path
    n, e, lab = caterpillar_method(sl)
    okc0 &= is_graceful_labelling(e, lab)
check(okc0, "caterpillar rule as printed (0 on the end dot of a longest path) works on 3000 more")
# the printed caterpillar: spine 0-1-2-3, leaves: dot 0 is itself a leaf of 1...
# as a caterpillar with spine 1-2-3: leaves of 1 = {0,4,5}, of 2 = {6}, of 3 = {7}
check(is_graceful_labelling(CAT[1], ex_cat), f"caterpillar example {ex_cat} (dots in drawing order)")

def is_caterpillar(t):
    core = t.subgraph([v for v in t if t.degree(v) > 1])
    return core.number_of_nodes() <= 1 or all(d <= 2 for _, d in core.degree())


check(not is_caterpillar(nx.Graph(SPIDER[1])) and is_caterpillar(nx.Graph(CAT[1])),
      "spider is not a caterpillar; the printed caterpillar is one")
non_cat = {n: sum(1 for t in nx.nonisomorphic_trees(n) if not is_caterpillar(t)) for n in range(2, 8)}
check(non_cat == {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1}, f"the spider is the only non-caterpillar with 7 or fewer dots: {non_cat}")

for n in range(2, 11):
    trees = list(nx.nonisomorphic_trees(n))
    bad = [t for t in trees if not graceful_all(n, list(t.edges()), limit=1)]
    check(not bad, f"all {len(trees)} tree shapes with {n} dots can be labelled")


# ------------------------------------------------ piece clearance (registry)
import math


def _overlap(poly_a, poly_b):
    """Separating-axis test for two convex polygons (lists of points)."""
    for poly in (poly_a, poly_b):
        for i in range(len(poly)):
            (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % len(poly)]
            nx_, ny_ = y2 - y1, x1 - x2
            pa = [nx_ * x + ny_ * y for x, y in poly_a]
            pb = [nx_ * x + ny_ * y for x, y in poly_b]
            if max(pa) <= min(pb) or max(pb) <= min(pa):
                return False
    return True


def _square(cx, cy, s, th=0.0):
    h = s / 2
    c, si = math.cos(th), math.sin(th)
    return [(cx + c * x - si * y, cy + si * x + c * y) for x, y in ((-h, -h), (h, -h), (h, h), (-h, h))]


def largest_piece(net, th):
    """Largest square piece (cm) centred on every dot of net, turned by th,
    that touches no link box (boxes are axis-aligned squares)."""
    boxes = [_square(bx, by, net["box"]) for bx, by in net["boxes"]]
    best = 99.0
    for cx, cy in net["pts"]:
        lo, hi = 0.0, 6.0
        for _ in range(40):
            mid = (lo + hi) / 2
            if any(_overlap(_square(cx, cy, mid, th), b) for b in boxes):
                hi = mid
            else:
                lo = mid
        best = min(best, lo)
    return best


if len(sys.argv) > 1:
    print()
    print("== piece clearance on the working boards (from the drawn coordinates) ==")
    angles = [k * math.pi / 180 for k in range(0, 46)]
    rows = {"card": [], "tower": []}
    for net in reg:
        if net["r"] < 1.2 or net["kind"] not in rows:
            continue
        up = largest_piece(net, 0.0)
        worst = min(largest_piece(net, a) for a in angles)
        rows[net["kind"]].append((net["name"], up, worst))
    for kind, rr in rows.items():
        for name, up, worst in sorted(rr, key=lambda t: t[2]):
            print(f"  {kind:5s} {name:12s} largest square piece: kept square {up:5.2f} cm, any angle {worst:5.2f} cm")
    cards = rows["card"]
    up_min = min(cards, key=lambda t: t[1])
    any_min = min(cards, key=lambda t: t[2])
    print(f"  tightest card board kept square: {up_min[0]} {up_min[1]:.2f} cm; at any angle: {any_min[0]} {any_min[2]:.2f} cm")
    check(up_min[1] >= 2.0 + 0.2, "a 2 cm card kept square clears every box on every card board, at least 1 mm to spare each side")
    check(all(w >= 1.9 for _, _, w in cards), "turned to its worst angle, a 2 cm card overlaps a box corner by under 1 mm at most")
    print("  boards where a 2 cm card at its worst angle can touch a box:",
          [n for n, _, w in cards if w < 2.0])
    check(min(w for _, _, w in rows["tower"]) >= 2.0, "a 2 cm snap cube clears every box on every K-1 board at any angle "
          f"(tightest {min(w for _, _, w in rows['tower']):.2f} cm)")
print()
print("ALL CHECKS PASSED" if ok_all else "SOME CHECKS FAILED")
