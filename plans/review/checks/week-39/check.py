#!/usr/bin/env python3
"""Week 39 (Road detours) math check.

Independent verification of every student problem in all three bands and of
every route, count and claim in the adult guide.  Reads extracted.json (made by
extract.py from the delivered student PDFs) for the maps, worked example and
printed routes; the guide's claims are transcribed by hand below from
lowell-math-circle-year-2/week-39/week-39-facilitator.pdf (page numbers given).

A journey is a vertex sequence v0 v1 ... vn on a simple graph; an immediate
reversal is v[i-1] == v[i+1] (step v[i-1]->v[i] then back along the same road),
and removing it deletes v[i], v[i+1].  Two independent reducers are used:
  * all_results(): breadth-first search over EVERY deletion order;
  * stack(): left-to-right stack reduction.
Standard library only.  Run: python3 check.py > out_check.txt
"""
import itertools
import json
import math
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "extracted.json").read_text())
FAIL = []


def ok(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


def note(msg):
    print("  note " + msg)


# ------------------------------------------------------------------ graphs
def graph(edges):
    adj = {}
    for e in edges:
        a, b = e
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    return adj


TREE = graph(["AB", "BC", "BD", "DE", "DF"])
RING = graph(["AB", "BC", "CD", "DA"])
BOW = graph(["HA", "AB", "BH", "HC", "CD", "DH"])


def edges_of(adj):
    return sorted({"".join(sorted(a + b)) for a in adj for b in adj[a]})


def valid(w, G):
    return len(w) >= 1 and all(w[i + 1] in G[w[i]] for i in range(len(w) - 1))


def roads(w):
    """Undirected roads used, as a Counter."""
    return Counter("".join(sorted(w[i:i + 2])) for i in range(len(w) - 1))


def steps(w):
    return len(w) - 1


def is_reduced(w):
    return all(w[i - 1] != w[i + 1] for i in range(1, len(w) - 1))


def one_deletions(w):
    """All journeys obtained by removing one immediate reversal."""
    out = []
    for i in range(1, len(w) - 1):
        if w[i - 1] == w[i + 1]:
            out.append(w[:i] + w[i + 2:])
    return out


@lru_cache(maxsize=None)
def all_results(w):
    """Set of terminal journeys over all deletion orders (exhaustive)."""
    nxt = one_deletions(w)
    if not nxt:
        return frozenset([w])
    res = set()
    for v in nxt:
        res |= all_results(v)
    return frozenset(res)


def stack(w):
    r = [w[0]]
    for v in w[1:]:
        if len(r) >= 2 and r[-2] == v:
            r.pop()
        else:
            r.append(v)
    return "".join(r)


def walks(G, s, n, t=None):
    """All journeys with n steps from s (ending at t if given)."""
    out = []

    def rec(w):
        if len(w) == n + 1:
            if t is None or w[-1] == t:
                out.append(w)
            return
        for v in sorted(G[w[-1]]):
            rec(w + v)

    rec(s)
    return out


def results_of(ws):
    res = Counter()
    for w in ws:
        r = all_results(w)
        assert len(r) == 1, (w, r)
        assert stack(w) in r
        res[next(iter(r))] += 1
    return res


def inverse(w):
    return w[::-1]


def concat(*ws):
    out = ws[0]
    for w in ws[1:]:
        assert out[-1] == w[0]
        out += w[1:]
    return out


def deletion_chain_ok(chain):
    """Each arrow deletes exactly one adjacent same-road reversal."""
    return all(b in one_deletions(a) for a, b in zip(chain, chain[1:]))


# ------------------------------------------------------------------ diagrams
print("== Diagrams (from extracted.json, i.e. from the delivered PDFs)")
INTENDED = {"tree": TREE, "ring": RING, "bow": BOW}


def kind_of(nodes):
    labs = {n["label"] for n in nodes}
    if "H" in labs:
        return "bow"
    if "E" in labs:
        return "tree"
    return "ring"


def mentioned(text):
    return {c for c in "ABCDEFH" if f" {c} " in f" {text.replace(',', ' ').replace('.', ' ').replace('?', ' ')} "}


for band, pages in DATA.items():
    for pg in pages:
        m = pg["map"]
        if not m["nodes"]:
            continue
        k = kind_of(m["nodes"])
        G = INTENDED[k]
        got = sorted("".join(sorted(e["a"] + e["b"])) for e in m["edges"])
        und = sorted("".join(sorted(e["a"] + e["b"])) for e in m["underlays"])
        labs = sorted(n["label"] for n in m["nodes"])
        tag = f"{band} p{pg['page']} {k}"
        ok(labs == sorted(G) and got == edges_of(G) and und == edges_of(G),
           f"{tag}: nodes {''.join(labs)}, black roads {got} and grey road bands match the intended map")
        P = {n["label"]: (n["x"], n["y"]) for n in m["nodes"]}
        radii = {(n["rx"], n["ry"]) for n in m["nodes"]}
        ok(all(abs(rx - ry) < 0.05 for rx, ry in radii) and len({r[0] for r in radii}) == 1,
           f"{tag}: all node circles round and equal, r = {radii.pop()[0]:.2f} pt")
        L = lambda a, b: math.dist(P[a], P[b])
        if k == "ring":
            sides = [L("A", "B"), L("B", "C"), L("C", "D"), L("D", "A")]
            ok(max(sides) - min(sides) < 0.05 and abs(L("A", "C") - L("B", "D")) < 0.05,
               f"{tag}: ring is a square (sides {sides[0]:.1f} pt, equal diagonals)")
        if k == "tree":
            u = L("A", "B")
            ok(abs(L("B", "C") - u) < 0.05 and abs(L("B", "D") - u) < 0.05
               and abs(L("D", "E") - u * 2 ** .5) < 0.05 and abs(L("D", "F") - u * 2 ** .5) < 0.05,
               f"{tag}: tree drawn on an equal-scale grid (unit {u:.1f} pt)")
        if k == "bow":
            ok(abs(L("H", "A") - L("H", "C")) < 0.05 and abs(L("H", "B") - L("H", "D")) < 0.05
               and abs(L("A", "B") - L("C", "D")) < 0.05,
               f"{tag}: two rings mirror-symmetric about H")
            ok(P["A"][0] < P["H"][0] < P["C"][0], f"{tag}: A,B on the left ring and C,D on the right ring")
        # Every vertex named in a problem on this page is on this page's map.
        for p in pg["problems"]:
            need = mentioned(p["text"])
            ok(need <= set(labs), f"{tag}: {p['text'][:10]} names {''.join(sorted(need))}, all on the map")

print("\n== Worked example (step tiles, every band, p1)")
for band, pages in DATA.items():
    t = pages[0]["tiles"]
    arrows = [(x["arrows"][0]["from"][0], x["arrows"][0]["to"][0]) for x in t]
    struck = [x["struck"] for x in t]
    ok(len(t) == 10, f"{band}: 10 step tiles (4 input, 4 remove, 2 output)")
    inp, rem, outp = arrows[:4], arrows[4:8], arrows[8:]
    w = inp[0][0] + "".join(b for a, b in inp)
    ok(all(inp[i][1] == inp[i + 1][0] for i in range(3)) and valid(w, TREE),
       f"{band}: input tiles chain to the journey {w}, legal on the tree map")
    ok(rem == inp and struck[4:8] == [False, True, True, False],
       f"{band}: remove row repeats the input with tiles 2-3 struck")
    ok(rem[1] == rem[2][::-1], f"{band}: struck tiles {rem[1]} {rem[2]} are one road in opposite directions, adjacent")
    out = outp[0][0] + "".join(b for a, b in outp)
    ok(out == "ABD" and stack(w) == out and all_results(w) == {out},
       f"{band}: output tiles {outp} = reduced journey {out}")
    ok(all(x["roads"] == ["AB", "BC", "BD"] for x in t), f"{band}: every tile shows mini map A-B, B-C, B-D")

# ------------------------------------------------------------------ K-1
print("\n== K-1")
print(" P1 (tree): 3-step A->E; 4-step B->B; 4-step A->D")
w = walks(TREE, "A", 3, "E")
ok(w == ["ABDE"], f"3-step A->E trips: {w} (only one; it cannot be shortened)")
w = walks(TREE, "B", 4, "B")
r = results_of(w)
ok(len(w) > 0 and set(r) == {"B"}, f"{len(w)} four-step B->B trips, all reduce to staying at B")
w = walks(TREE, "A", 4, "D")
r = results_of(w)
ok(len(w) > 0 and set(r) == {"ABD"}, f"{len(w)} four-step A->D trips {w}, all reduce to ABD")

print(" P2 (ring): 4-step A->A")
w = walks(RING, "A", 4, "A")
r = results_of(w)
ok(len(w) == 8 and r == Counter({"A": 6, "ABCDA": 1, "ADCBA": 1}),
   f"{len(w)} four-step home trips; results {dict(r)}; the two circuits keep all four steps")

print(" P3 (tree): 7-step A->E and C->F")
for s, t, want in [("A", "E", "ABDE"), ("C", "F", "CBDF")]:
    w = walks(TREE, s, 7, t)
    r = results_of(w)
    ok(len(w) > 0 and set(r) == {want}, f"{len(w)} seven-step {s}->{t} trips, all reduce to {want}")

print(" P4 (tree): A->A with 4, 6, 8, 12 steps")
for n in (4, 6, 8, 12):
    w = walks(TREE, "A", n, "A")
    r = results_of(w)
    ok(len(w) > 0 and set(r) == {"A"}, f"{n} steps: {len(w)} trips, all shorten to staying at A")

print(" P5 (tree): C->F using every road")
allr = set(edges_of(TREE))
first = None
for n in range(3, 14):
    w = [x for x in walks(TREE, "C", n, "F") if set(roads(x)) == allr]
    if w and first is None:
        first = n
    r = results_of(w)
    ok(set(r) <= {"CBDF"}, f"{n} steps: {len(w)} C->F trips use every road; results {set(r) or '-'}")
ok(first == 7, f"shortest C->F trip using every road has {first} steps (e.g. CBABDEDF); none keeps an extra step")

print(" P6 (ring): results of 8-step A->A")
w = walks(RING, "A", 8, "A")
r6 = results_of(w)
ok(set(r6) == {"A", "ABCDA", "ADCBA", "ABCDABCDA", "ADCBADCBA"},
   f"{len(w)} eight-step home trips; exactly 5 results {dict(r6)}")

print(" P7 (ring): results of 6-step A->C")
w = walks(RING, "A", 6, "C")
r7 = results_of(w)
ok(set(r7) == {"ABC", "ADC", "ABCDABC", "ADCBADC"}, f"{len(w)} six-step A->C trips; exactly 4 results {dict(r7)}")
res = sorted(r7)
print("   'visit exactly the same roads in a different order' under three readings:")
for name, f in [("set of roads", lambda x: frozenset(roads(x))),
                ("roads with repeats (tiles, ignoring arrows)", lambda x: frozenset(roads(x).items())),
                ("directed tiles with repeats", lambda x: frozenset(Counter(x[i:i + 2] for i in range(len(x) - 1)).items()))]:
    pairs = [(a, b) for a, b in itertools.combinations(res, 2) if f(a) == f(b)]
    print(f"     {name}: pairs = {pairs or 'none'} -> answer {'yes' if pairs else 'no'}")
for x in res:
    print(f"     {x}: roads {dict(sorted(roads(x).items()))}")
pairs_set = [(a, b) for a, b in itertools.combinations(res, 2) if set(roads(a)) == set(roads(b))]
pairs_ms = [(a, b) for a, b in itertools.combinations(res, 2) if roads(a) == roads(b)]
ok(pairs_set == [("ABCDABC", "ADCBADC")] and pairs_ms == [],
   "answer depends on the reading: yes for road SETS (the two 6-step results), no for road tiles with repeats")

# ------------------------------------------------------------------ Grades 2-3 and 4-5 P1
print("\n== Grades 2-3 and 4-5, Problem 1 (tree, printed routes)")
for band in ("grades-2-3", "grades-4-5"):
    rs = [r["route"] for r in DATA[band][0]["routes"] if r["route"]]
    ok(rs == ["ABABDFDE", "ABDFDE", "CBCBDF"], f"{band}: printed routes {rs}")
for x, want in [("ABABDFDE", "ABDE"), ("ABDFDE", "ABDE"), ("CBCBDF", "CBDF")]:
    ok(valid(x, TREE) and all_results(x) == {want}, f"{x} ({steps(x)} steps) is legal; every deletion order gives {want}")
w = walks(TREE, "C", 7, "F")
r = results_of(w)
ok(len(w) > 0 and set(r) == {"CBDF"}, f"{len(w)} seven-step C->F trips exist, all finishing as CBDF")

print("\n== Grades 2-3")
print(" P2 (tree): 12-step A->A using every road")
w = [x for x in walks(TREE, "A", 12, "A") if set(roads(x)) == allr]
r = results_of(w)
ok(len(w) >= 3 and set(r) == {"A"}, f"{len(w)} such trips; all reduce to A")
bad = [x for n in range(0, 15) for x in walks(TREE, "A", n, "A") if stack(x) != "A"]
ok(not bad, "every A->A tree trip of length 0..14 reduces to A (exhaustive)")
print(" P3 (ring): 8-step home results and fewest steps in a survivor")
ok(min(steps(x) for x in r6 if x != "A") == 4, "fewest steps in a nonempty surviving trip home = 4")
print(" P4 (ring): ABABCBADCDA")
rs = [r["route"] for r in DATA["grades-2-3"][2]["routes"] if r["route"]]
ok(rs == ["ABABCBADCDA"], f"printed route {rs}")
x = "ABABCBADCDA"


def count_orders(w):
    nxt = one_deletions(w)
    return 1 if not nxt else sum(count_orders(v) for v in nxt)


ok(valid(x, RING) and all_results(x) == {"A"},
   f"{x} is legal ({steps(x)} steps); all {count_orders(x)} complete deletion orders end at A")
print(" P5 (two rings): left-then-right vs right-then-left")
LEFT = ["HABH", "HBAH"]   # both directions pass through A
RIGHT = ["HCDH", "HDCH"]  # both directions pass through C
for a in LEFT:
    for c in RIGHT:
        x, y = concat(a, c), concat(c, a)
        ok(is_reduced(x) and is_reduced(y) and stack(x) != stack(y),
           f"left {a}, right {c}: {x} and {y} are already reduced and different")
print(" P6 (two rings): >= 12 steps, both rings, one vanishes, one loses nothing")
tot_van = tot_red = 0
for n in (12, 13, 14, 15):
    w = [x for x in walks(BOW, "H", n, "H")
         if set(roads(x)) & {"AH", "AB", "BH"} and set(roads(x)) & {"CH", "CD", "DH"}]
    van = sum(1 for x in w if stack(x) == "H")
    red = sum(1 for x in w if is_reduced(x))
    tot_van += van
    tot_red += red
    print(f"   {n} steps: {len(w)} trips use both rings; {van} vanish, {red} lose no steps")
ok(tot_van > 0 and tot_red > 0, "both kinds exist at >= 12 steps (vanishing needs even length, "
   "a no-loss home trip needs a multiple of 3; 12 serves both)")

print("\n== Grades 4-5")
print(" P2/P3 (tree): any length")
bad = [x for n in range(0, 15) for x in walks(TREE, "C", n, "F") if stack(x) != "CBDF"]
ok(not bad, "every C->F tree trip of length 0..14 reduces to CBDF (exhaustive)")
print(" P4 (ring): three printed routes, every deletion order")
rs = [r["route"] for r in DATA["grades-4-5"][2]["routes"] if r["route"]]
ok(rs == ["ABABCBADCDA", "ABADCBC", "ABCDABCBA"], f"printed routes {rs}")
for x, want in zip(rs, ["A", "ADC", "ABCDA"]):
    ok(valid(x, RING) and all_results(x) == {want},
       f"{x}: legal, {count_orders(x)} complete deletion orders, all end at {want}")
# Exhaustive confluence on the printed maps (finite check of the theorem the guide proves).
for G, nm, N in [(RING, "ring", 10), (BOW, "two-ring", 8), (TREE, "tree", 9)]:
    worst = 0
    for s in G:
        for n in range(N + 1):
            for x in walks(G, s, n):
                rr = all_results(x)
                worst = max(worst, len(rr))
                if rr != {stack(x)}:
                    FAIL.append("confluence " + x)
    ok(worst == 1, f"{nm}: every journey up to {N} steps from every start has one final route, equal to the stack result")
for x in rs:
    note(f"{x}: {len(one_deletions(x))} possible first reversal(s)")
ok(len(one_deletions("ABCDABCBA")) == 1 and count_orders("ABCDABCBA") == 1,
   "third route ABCDABCBA admits only ONE deletion order, so 'shorten each ... in different orders' cannot be done for it")
alt = "ABCBCDABA"
ok(valid(alt, RING) and steps(alt) == 8 and len(one_deletions(alt)) >= 2 and all_results(alt) == {"ABCDA"},
   f"possible replacement {alt}: legal, 8 steps, {len(one_deletions(alt))} first choices, {count_orders(alt)} orders, all end at ABCDA")
print(" P5 (two rings): commutator, either direction around each ring")
for a in LEFT:
    for c in RIGHT:
        x = concat(a, c, inverse(a), inverse(c))
        ok(steps(x) == 12 and is_reduced(x), f"a={a}, c={c}: {x} has no immediate reversal, so it cannot disappear")
print(" P6 (two rings): same counts, different result")
a, c = "HABH", "HCDH"
pieces = {"a": a, "a'": inverse(a), "c": c, "c'": inverse(c)}
van, surv = [], []
for perm in itertools.permutations(pieces):
    x = concat(*[pieces[p] for p in perm])
    (van if stack(x) == "H" else surv).append("".join(perm))
ok(van and surv, f"of the 24 orders of a, a', c, c': {len(van)} vanish {van}; {len(surv)} survive")

# ------------------------------------------------------------------ the adult guide
print("\n== Adult guide (claims transcribed from week-39-facilitator.pdf)")


def claim(route, G, start, end, n, reduces_to, msg):
    ok(valid(route, G) and route[0] == start and route[-1] == end and steps(route) == n
       and all_results(route) == {reduces_to}, f"{msg}: {route} legal, {start}->{end}, {n} steps, reduces to {reduces_to}")


print(" p3 K-1 key")
claim("ABABDFDE", TREE, "A", "E", 7, "ABDE", "P3 A->E example")
claim("CBABDEDF", TREE, "C", "F", 7, "CBDF", "P3 C->F example")
for k in (2, 3, 4, 6):
    claim("AB" * k + "A", TREE, "A", "A", 2 * k, "A", f"P4 witness, {k} out-and-back pairs")
x = "CBABDEDBDF"
claim(x, TREE, "C", "F", 9, "CBDF", "P5 example")
ok(set(roads(x)) == allr, "P5 example uses AB, BC, BD, DE, DF")
ok(deletion_chain_ok([x, "CBDEDBDF", "CBDBDF", "CBDF"]), "P5 deletions B-A-B, D-E-D, then D-B-D, in that order, are each legal")
for res_, inp in [("A", "ABABABABA"), ("ABCDA", "ABABABCDA"), ("ADCBA", "ABABADCBA"),
                  ("ABCDABCDA", "ABCDABCDA"), ("ADCBADCBA", "ADCBADCBA")]:
    claim(inp, RING, "A", "A", 8, res_, "P6 table row")
ok(set(r6) == {"A", "ABCDA", "ADCBA", "ABCDABCDA", "ADCBADCBA"}, "P6 'exactly five' matches enumeration")
claim("ABABABC", RING, "A", "C", 6, "ABC", "P7 input")
claim("ABABADC", RING, "A", "C", 6, "ADC", "P7 input")
red_AC = [x for n in range(0, 15) for x in walks(RING, "A", n, "C") if is_reduced(x)]
ok(all(steps(x) % 4 == 2 for x in red_AC), "P7 claim: every reduced A->C ring route has length 2 mod 4 (checked to 14)")
red_AA = [x for n in range(1, 17) for x in walks(RING, "A", n, "A") if is_reduced(x)]
ok(all(steps(x) % 4 == 0 for x in red_AA), "P6 claim: every nonempty reduced home ring route has length a multiple of 4 (to 16)")
ok(roads("ABCDABC") != roads("ADCBADC") and set(roads("ABCDABC")) == set(roads("ADCBADC")),
   "P7 key: 'both use all four roads ... not the same directed-edge multiset' is accurate (see K-1 P7 above)")

print(" p4 Grades 2-3 key")
claim("CBABDEDF", TREE, "C", "F", 7, "CBDF", "P1 new route")
p2 = ["ABABCBDEDFDBA", "ABABCBDFDEDBA", "ABABDEDFDBCBA"]
for x in p2:
    claim(x, TREE, "A", "A", 12, "A", "P2 example")
    ok(set(roads(x)) == allr, f"P2 example {x} uses every road")
ok(len(set(p2)) == 3, "P2 examples are three different trips")
ok(deletion_chain_ok(["ABABCBADCDA", "ABCBADCDA", "ABADCDA", "ADCDA", "ADA", "A"]), "P4 first chain: each arrow is one legal deletion")
ok(deletion_chain_ok(["ABABCBADCDA", "ABABADCDA", "ABADCDA", "ADCDA", "ADA", "A"]), "P4 second chain: each arrow is one legal deletion")
ok("ABABADCDA" in one_deletions("ABABCBADCDA") and "ABABCBADCDA".find("BCB") == 3,
   "P4 second chain begins by removing the B->C->B excursion")
ok(is_reduced("HABHCDH") and is_reduced("HCDHABH") and "HABHCDH" != "HCDHABH", "P5 key: HABHCDH vs HCDHABH")
claim("HABHBAHCDHDCH", BOW, "H", "H", 12, "H", "P6 vanishing example")
claim("HABHCDHBAHDCH", BOW, "H", "H", 12, "HABHCDHBAHDCH", "P6 survivor")

print(" p5 Grades 4-5 key")
ok(steps("CBCBDF") == 5, "P1: the listed C->F input has five steps")
ok(deletion_chain_ok(["ABADCBC", "ADCBC", "ADC"]), "P4 chain ABADCBC -> ADCBC -> ADC")
ok(deletion_chain_ok(["ABCDABCBA", "ABCDABA", "ABCDA"]), "P4 chain ABCDABCBA -> ABCDABA -> ABCDA")
ok(concat("HABH", "HCDH", inverse("HABH"), inverse("HCDH")) == "HABHCDHBAHDCH", "P5: HABHCDHBAHDCH = a b a^-1 b^-1")


def signed_counts(x):
    """Net signed traversals of the left and right rings (orientation H->A->B->H, H->C->D->H)."""
    pos = {"HA": ("L", 1), "AB": ("L", 1), "BH": ("L", 1), "HC": ("R", 1), "CD": ("R", 1), "DH": ("R", 1)}
    c = Counter()
    for i in range(len(x) - 1):
        e = x[i:i + 2]
        if e in pos:
            c[pos[e][0]] += 1
        else:
            c[pos[e[::-1]][0]] -= 1
    return dict(c)


ok(signed_counts("HABHBAHCDHDCH") == signed_counts("HABHCDHBAHDCH") == {"L": 0, "R": 0},
   "P6: aa^-1bb^-1 and the P5 survivor have the same (zero) signed ring counts")
claim("HABHBAHCDHDCH", BOW, "H", "H", 12, "H", "P6 aa^-1bb^-1")

print(" p6 stack proof: key lemma checked on every reduced stack up to 8 steps on each map")
bad = 0
for G in (TREE, RING, BOW):
    for s in G:
        for n in range(0, 9):
            for S in walks(G, s, n):
                if not is_reduced(S):
                    continue
                for e in G[S[-1]]:
                    # read e then e^-1 starting from stack S (as a vertex sequence)
                    if stack(S + e + S[-1]) != S:
                        bad += 1
ok(bad == 0, "reading e then e^-1 after any reduced stack S returns S")

print(" p7 route update (K-1 entry keys)")
claim("BABAB", TREE, "B", "B", 4, "B", "P1 B-A-B-A-B")
claim("ABABD", TREE, "A", "D", 4, "ABD", "P1 A-B-A-B-D")
ok(set(results_of(walks(RING, "A", 4, "A"))) == {"A", "ABCDA", "ADCBA"}, "P2 results stay at A, ABCDA, ADCBA")

print(" labels")
k1_ids = {f for pg in DATA["k-1"] for f in pg["footer"]}
note(f"K-1 packet footers: {sorted(k1_ids)}; guide p6 'Key alignment' line says K-1 is F39-K-v3")
ok(all("F39-K-v3" in f for f in k1_ids), "K-1 footer ID matches the guide's key-alignment ID")

print("\nSUMMARY:", "all checks passed" if not FAIL else f"{len(FAIL)} check(s) failed:")
for f in FAIL:
    print("  -", f)
