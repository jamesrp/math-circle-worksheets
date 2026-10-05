#!/usr/bin/env python3
"""Week 34 (Hidden turns) math check: independent brute-force verification.

Uses only my own code and the standard library.  Ring geometry comes from
extracted.json (made by extract.py from the delivered PDFs); every claim from
the student pages and the two adult guides is transcribed by hand below and
tested.  Run: python3 check.py > out_check.txt
"""
import itertools
import json
import math
from collections import Counter, defaultdict
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


# --------------------------------------------------------------- group tools
def motions(n):
    """All 2n dihedral maps on spots 0..n-1 (clockwise from the top):
    rotations i -> i+k and reflections i -> k-i, as tuples."""
    rots = [("r", k, tuple((i + k) % n for i in range(n))) for k in range(n)]
    refs = [("s", k, tuple((k - i) % n for i in range(n))) for k in range(n)]
    return rots + refs


def act(word, perm):
    """Move the copy: the kind at spot i lands on spot perm[i]."""
    out = [None] * len(word)
    for i, p in enumerate(perm):
        out[p] = word[i]
    return tuple(out)


def stab(word):
    """Matching nonidentity motions of a word (kinds fixed)."""
    n = len(word)
    return [(t, k) for t, k, p in motions(n) if not (t == "r" and k == 0) and act(word, p) == tuple(word)]


def distinguishing(word):
    return not stab(word)


def W(s):
    return tuple(s)


def orbit(word):
    return {act(word, p) for _, _, p in motions(len(word))}


def gaps(positions, n):
    ps = sorted(positions)
    return sorted(((ps[(j + 1) % len(ps)] - ps[j]) % n) or n for j in range(len(ps)))


# --------------------------------------------------- A. printed ring geometry
print("A. Printed rings (from extracted.json)")


def isometries(pts, tol=0.05):
    n = len(pts)
    D = [[math.dist(pts[i], pts[j]) for j in range(n)] for i in range(n)]
    found = []
    for perm in itertools.permutations(range(n)):
        if all(abs(D[i][j] - D[perm[i]][perm[j]]) < tol for i in range(n) for j in range(i + 1, n)):
            found.append(perm)
    return found


expected_rings = {
    # file: list of (page, n) for the task rings in order
    "week-34-k-1.pdf": [(1, 3), (2, 4), (3, 5), (4, 6), (5, 8)],
    "week-34-grades-2-3.pdf": [(1, 3), (2, 4), (3, 5), (4, 6), (5, 8)],
    "week-34-grades-4-5.pdf": [(1, 3), (2, 4), (3, 5), (4, 6), (5, 8)],
}
for fn, pages in DATA.items():
    for pg in pages:
        for r in pg["rings"]:
            n = r["n"]
            ok(r["spot_round"] and r["max_angle_error_deg"] < 0.01 and r["max_radius_error_mm"] < 0.01
               and r["first_spot_angle_deg"] < 0.01,
               f"{fn} p{pg['page']} n={n} '{r['label'][:30]}': spots equally spaced on a circle, first at top, round")
            if n <= 8:
                iso = isometries(r["spot_centres_mm"])
                expect = {p for _, _, p in motions(n)}
                ok(len(iso) == 2 * n and set(iso) == expect,
                   f"   its {len(iso)} distance-preserving spot permutations are exactly i->i+k, i->k-i")
for fn, want in expected_rings.items():
    got = []
    for pg in DATA[fn]:
        for r in pg["rings"]:
            if r["spot_diam_mm"][0] > 20:
                got.append((pg["page"], r["n"]))
    ok(got == want, f"{fn}: task rings by page {got}")
    sizes = {tuple(r["spot_diam_mm"]) for pg in DATA[fn] for r in pg["rings"] if r["spot_diam_mm"][0] > 20}
    ok(sizes == {(28.0, 28.0)}, f"{fn}: all task spots 28 mm across (guide: 'roughly 28 mm')")

# launch figure (same on all three bands)
for fn in expected_rings:
    small = [r for r in DATA[fn][0]["rings"] if r["n"] == 4 and r["ring_radius_mm"] < 20]
    seqs = [tuple(r["contents_cw_from_top"]) for r in small]
    start, two, one = seqs
    ok(start == ("dot", "ring", "dot", "ring"), f"{fn} launch start = {start} (alternating)")
    rot2 = act(start, motions(4)[2][2])
    rot1 = act(start, motions(4)[1][2])
    ok(two == rot2 and rot2 == start, f"   'turn 2 spots: match' picture = start turned 2 = start")
    ok(one == rot1 and rot1 != start, f"   'turn 1 spot: no match' picture = start turned 1, which differs")
    ok(len(stab(start)) == 3, f"   alternating 4-ring has 3 nonidentity matches (half-turn + 2 flips): {stab(start)}")

# --------------------------------------------- B. distinguishing numbers
print("\nB. Fewest kinds that stop every turn and flip (brute force)")
Dn = {}
for n in range(3, 13):
    for k in range(1, 4):
        if any(distinguishing(w) for w in itertools.product(range(k), repeat=n)):
            Dn[n] = k
            break
print("  D(C_n):", Dn)
ok(all(Dn[n] == 3 for n in (3, 4, 5)) and all(Dn[n] == 2 for n in range(6, 13)),
   "3 kinds for n=3,4,5 and 2 kinds for n=6..12 (guide overview 'Exact optimum')")

counts = []
for n in range(3, 11):
    counts.append(sum(distinguishing(w) for w in itertools.product("AB", repeat=n)))
print("  distinguishing binary words in fixed positions, n=3..10:", counts)
ok(counts == [0, 0, 0, 12, 28, 96, 252, 600], "guide p5 counts 0,0,0,12,28,96,252,600")

for n in range(3, 13):
    bad = [w for w in itertools.product("AB", repeat=n) if min(w.count("A"), w.count("B")) <= 2 and distinguishing(w)]
    ok(not bad, f"n={n}: every binary word with a kind used at most twice has a matching flip")
mins = {}
for n in range(6, 13):
    mins[n] = min(min(w.count("A"), w.count("B")) for w in itertools.product("AB", repeat=n) if distinguishing(w))
ok(all(v == 3 for v in mins.values()), f"least minority count on distinguishing binary rings n=6..12 is 3: {mins}")

# --------------------------------------------- C. witnesses in the guide
print("\nC. Guide witnesses")
for s in ["ABC", "ABCC", "ABCCC", "AABABB", "AABABBBB", "AABBABBB"]:
    ok(distinguishing(W(s)), f"{s} is distinguishing")
for n in range(6, 31):
    w = tuple("A" if i in (0, 1, 3) else "B" for i in range(n))
    g = gaps([0, 1, 3], n)
    if n <= 10 or n == 30:
        ok(distinguishing(w) and len(set(g)) == 3, f"n={n}: A at 0,1,3 distinguishes; gaps {g}")
    elif not distinguishing(w):
        FAIL.append(f"construction fails n={n}")
for n in range(3, 21):
    w = tuple(["A", "B"] + ["C"] * (n - 2))
    if not distinguishing(w):
        FAIL.append(f"adjacent unique kinds fail n={n}")
ok(True, "unique A, B adjacent + C elsewhere distinguishes every n=3..20 (no FAIL lines above)")
ok(W("AABABB") == tuple("A" if i in (0, 1, 3) else "B" for i in range(6)), "AABABB has A at 0,1,3")
ok(gaps([0, 1, 3], 8) == [1, 2, 5] and gaps([0, 1, 4], 8) == [1, 3, 4], "8-ring A gaps {1,2,5} and {1,3,4}")
ok(W("AABBABBB") not in orbit(W("AABABBBB")), "the two K-1 P6 key patterns cannot match each other")
# mixed 3-ring: no rotation
mixed3 = [w for w in itertools.product("AB", repeat=3) if len(set(w)) == 2]
ok(all(all(t == "s" for t, _ in stab(w)) and len(stab(w)) == 1 for w in mixed3),
   "every mixed two-kind 3-ring has exactly one matching flip and no matching turn")

# --------------------------------------------- D. proof lemmas
print("\nD. Lemmas used on guide p5")
for n in range(3, 21):
    for size in range(0, 3):
        for S in itertools.combinations(range(n), size):
            if not any(t == "s" and {p[i] for i in S} == set(S) for t, _, p in motions(n)):
                FAIL.append(f"lemma1 n={n} S={S}")
ok(True, "n=3..20: every set of at most two spots is preserved by some reflection")
for n in range(3, 21):
    for t, k, p in motions(n):
        if t == "s":
            fixed = [i for i in range(n) if p[i] == i]
            if len(fixed) == 2 and (fixed[1] - fixed[0]) % n not in (n // 2,):
                FAIL.append(f"lemma2 n={n} k={k}")
            if any((i + 1) % n in fixed for i in fixed):
                FAIL.append(f"lemma2b n={n} k={k} adjacent fixed")
ok(True, "n=3..20: a reflection fixes at most two spots, which are opposite; never two adjacent spots")
for n in range(3, 21):
    for S in itertools.combinations(range(n), 3):
        w = tuple("A" if i in S else "B" for i in range(n))
        if distinguishing(w) != (len(set(gaps(S, n))) == 3):
            FAIL.append(f"lemma3 n={n} S={S}")
ok(True, "n=3..20: a 3-spot marked set has no matching motion exactly when its three gaps differ")
ok(not [f for f in FAIL if f.startswith(("lemma", "construction", "adjacent"))], "no lemma failures recorded")

# --------------------------------------------- E. K-1 Problem 3 edits
print("\nE. K-1 P3: one-counter changes")


def edits(word, kinds):
    for i in range(len(word)):
        for k in kinds:
            if k != word[i]:
                yield i, k, word[:i] + (k,) + word[i + 1:]


start = W("ABCC")
res = {(i, k): distinguishing(w) for i, k, w in edits(start, "ABCD")}
print("  from ABCC (D = a fourth kind):", {f"{i}->{k}": v for (i, k), v in res.items()})
fl = [k for t, k in stab(W("ABAC")) if t == "s"]
ok(not res[(2, "A")] and fl == [2] and motions(4)[4 + 2][2][1] == 1 and motions(4)[4 + 2][2][3] == 3,
   f"ABCC -> ABAC (third spot C->A) matches only the flip k={fl}, which fixes the B spot (1) and C spot (3)")
ok(res[(2, "B")], "ABCC -> ABBC stays distinguishing")
ok(any(res.values()) and not all(res.values()), "both outcomes occur from ABCC")
# every 3-kind distinguishing 4-ring (fixed positions): do both outcomes occur using kinds A,B,C only?
dist4 = [w for w in itertools.product("ABC", repeat=4) if distinguishing(w)]
both = all(any(distinguishing(x) for _, _, x in edits(w, "ABC")) and any(not distinguishing(x) for _, _, x in edits(w, "ABC"))
           for w in dist4)
ok(both, f"every one of the {len(dist4)} three-kind distinguishing 4-rings allows both kinds of change")
w4 = W("ABCD")
r4 = [distinguishing(x) for _, _, x in edits(w4, "ABCD")]
ok(any(r4) and not all(r4), "from a four-kind 4-ring both outcomes also occur")

# --------------------------------------------- F. K-1 P6 / 2-3 P5 on the 8-ring
print("\nF. Eight-ring two-kind patterns")
d8 = [w for w in itertools.product("AB", repeat=8) if distinguishing(w)]
orbs = {}
for w in d8:
    key = min(orbit(w))
    orbs.setdefault(key, w)
by = defaultdict(list)
for key in orbs:
    S = [i for i in range(8) if key[i] == "A"]
    by[len(S)].append(("".join(key), gaps(S, 8)))
print("  orbits of distinguishing two-kind 8-rings (kinds fixed), by number of A:", dict(by))
ok(len(orbs) == 6, f"{len(orbs)} different (non-matching) distinguishing two-kind 8-rings")
p = W("AABABBBB")
swap = tuple("B" if c == "A" else "A" for c in p)
ok(distinguishing(swap) and swap not in orbit(p),
   f"swapping the kinds of AABABBBB gives {''.join(swap)}, also distinguishing and unable to match it")
ok(min(min(w.count("A"), w.count("B")) for w in d8) == 3, "2-3 P5: fewest counters of one kind = 3")
# counter budget: 8 of each of three kinds per pair
need = Counter("AABABBBB") + Counter("AABBABBB")
note(f"guide's two K-1 P6 key patterns together use {dict(need)} (pair kit: 8 of each kind; this fits "
     "because the page keeps each pattern on its own tracing copy, so they can be built one at a time)")
note("other cheap second answers under the fixed-kind rule: the same arrangement built in kinds A and C "
     "cannot match an A/B pattern, because kinds are never exchanged")

# --------------------------------------------- G. bonus P1-P2 flip counts
print("\nG. Bonus P1-P2: number of matching flips")


def nflips(w):
    return sum(1 for t, _ in stab(w) if t == "s")


for n in (6, 8):
    c = Counter(nflips(w) for w in itertools.product("AB", repeat=n))
    print(f"  n={n}: flip counts over all two-kind words: {dict(sorted(c.items()))}")
c6 = Counter(nflips(w) for w in itertools.product("AB", repeat=6))
ok(set(c6) == {0, 1, 2, 3, 6}, "six-ring two-kind flip counts are 0,1,2,3,6; never 4")
c6b = Counter(nflips(w) for w in itertools.product("ABC", repeat=6))
ok(4 not in c6b, "never 4 even with three kinds")
c8 = Counter(nflips(w) for w in itertools.product("AB", repeat=8))
ok(set(c8) == {0, 1, 2, 4, 8}, "eight-ring positive flip counts 1,2,4,8 (bonus guide p2)")
for s, want in [("AABBBB", [1]), ("ABBABB", [0, 3]), ("ABABAB", [0, 2, 4]), ("AABABB", [])]:
    ks = [k for t, k in stab(W(s)) if t == "s"]
    ok(ks == want, f"{s}: matching reflections k={ks} (guide {want})")
for s, want in [("AABBBBBB", 1), ("AABBAABB", 2), ("ABABABAB", 4), ("AAAAAAAA", 8)]:
    ok(nflips(W(s)) == want, f"{s}: {nflips(W(s))} matching flips (guide {want})")
# theorem: flips in {0, n/d}
viol = 0
for n in range(3, 11):
    for w in itertools.product("AB", repeat=n):
        st = stab(w)
        rots = [k for t, k in st if t == "r"]
        d = min(rots) if rots else n
        f = sum(1 for t, _ in st if t == "s")
        if n % d or f not in (0, n // d):
            viol += 1
for n in range(3, 9):
    for w in itertools.product("ABC", repeat=n):
        st = stab(w)
        rots = [k for t, k in st if t == "r"]
        d = min(rots) if rots else n
        f = sum(1 for t, _ in st if t == "s")
        if n % d or f not in (0, n // d):
            viol += 1
ok(viol == 0, "least turn step d divides n and flips number 0 or n/d (all 2-kind words n<=10, 3-kind n<=8)")

# --------------------------------------------- H. bonus P3-P4 repairs
print("\nH. Bonus P3-P4: fewest changes from AAABBABB")
start8 = W("AAABBABB")
bonus_start = [r["contents_cw_from_top"] for pg in DATA["week-34-bonus.pdf"] for r in pg["rings"]
               if r["label"] == "starting pattern"]
ok(all(tuple(s) == start8 for s in bonus_start) and len(bonus_start) == 2,
   "both printed starting patterns read AAABBABB clockwise from the top")


def ham(a, b):
    return sum(x != y for x, y in zip(a, b))


def best_repairs(word, perm, kinds="AB"):
    cands = [w for w in itertools.product(kinds, repeat=len(word)) if act(w, perm) == w]
    m = min(ham(word, w) for w in cands)
    return m, sorted("".join(w) for w in cands if ham(word, w) == m)


M8 = {(t, k): p for t, k, p in motions(8)}
half = best_repairs(start8, M8[("r", 4)])
print("  half-turn:", half)
ok(half == (2, sorted(["AAABAAAB", "AABBAABB", "BAABBAAB", "BABBBABB"])), "P3: minimum 2, exactly the guide's four words")
flipv = best_repairs(start8, M8[("s", 0)])
t1 = best_repairs(start8, M8[("r", 1)])
t2 = best_repairs(start8, M8[("r", 2)])
print("  vertical flip (through spots 0 and 4):", flipv[0], len(flipv[1]))
print("  turn 1 spot:", t1)
print("  turn 2 spots:", t2)
ok((flipv[0], len(flipv[1]), t1[0], len(t1[1]), t2[0], len(t2[1])) == (3, 8, 4, 2, 4, 4),
   "P4: flip 3 (8 best), turn 1 spot 4 (2 best), turn 2 spots 4 (4 best); the flip is cheapest")
dl = [ln for pg in DATA["week-34-bonus.pdf"] for r in pg["rings"] for ln in r["dashed_lines"]]
ok(len(dl) == 1 and dl[0]["spots_on_line"] == [0, 4], "the printed flip card's dashed line runs through spots 0 and 4 (k=0)")
arcs = {r["label"]: r["arcs"][0] for pg in DATA["week-34-bonus.pdf"] for r in pg["rings"] if r["arcs"]}
for lab, want in [("half-turn: 4 spots", 4), ("turn 1 spot", 1), ("turn 2 spots", 2)]:
    a = arcs[lab]
    ok(abs(a["tip_sweep_in_spots"] - want) < 0.1, f"card '{lab}': arrow sweeps {a['tip_sweep_in_spots']} spots clockwise")
allref = {k: best_repairs(start8, M8[("s", k)])[0] for k in range(8)}
note(f"cost of every flip from AAABBABB, by k: {allref} (printed card is k=0)")
ok(stab(start8) == [("s", 2)],
   "FINDING: the printed start AAABBABB already matches one flip, k=2 (axis through spots 1 and 5, "
   "upper-right A and lower-left A), with 0 changes; the guide does not say so")
# formula check: cost = sum over cycles of (length - max frequency)


def cycles(perm):
    seen, out = set(), []
    for i in range(len(perm)):
        if i not in seen:
            c, j = [], i
            while j not in seen:
                seen.add(j)
                c.append(j)
                j = perm[j]
            out.append(c)
    return out


bad = 0
for n in range(3, 9):
    for word in itertools.product("AB", repeat=n):
        for t, k, perm in motions(n):
            m, _ = best_repairs(word, perm)
            f = sum(len(c) - max(Counter(word[i] for i in c).values()) for c in cycles(perm))
            bad += m != f
ok(bad == 0, "cycle formula (length minus top frequency, summed) equals brute-force minimum, all 2-kind words n<=8")

# other readings of 'change'
print("  other readings of 'change':")


def min_swaps(word, perm, limit=4):
    frontier = {word}
    seen = {word}
    for steps in range(limit + 1):
        if any(act(w, perm) == w for w in frontier):
            return steps
        nxt = set()
        for w in frontier:
            for i, j in itertools.combinations(range(len(w)), 2):
                if w[i] != w[j]:
                    x = list(w)
                    x[i], x[j] = x[j], x[i]
                    x = tuple(x)
                    if x not in seen:
                        seen.add(x)
                        nxt.add(x)
        frontier = nxt
    return None


for lab, key in [("half-turn", ("r", 4)), ("vertical flip", ("s", 0)), ("turn 1", ("r", 1)), ("turn 2", ("r", 2))]:
    note(f"if a 'change' is exchanging two counters: {lab} needs {min_swaps(start8, M8[key])} exchanges"
         " (None = impossible by exchanges alone)")
allA = tuple("A" for _ in start8)
note(f"if 'change as few counter kinds' counts kinds: recolour every B as A -> {''.join(allA)}, "
     f"matches half-turn: {act(allA, M8[('r', 4)]) == allA}, changing 1 kind (4 counters)")
sw = list(start8)
sw[0], sw[6] = sw[6], sw[0]
note(f"exchange spots 0 and 6: {''.join(sw)} matches the half-turn: {act(tuple(sw), M8[('r', 4)]) == tuple(sw)}")

# --------------------------------------------- I. bonus P5-P6 layers
print("\nI. Bonus P5-P6: layers")
lay = [r for r in DATA["week-34-bonus.pdf"][3]["rings"] if r["n"] == 4]
ok([tuple(r["contents_cw_from_top"]) for r in lay] ==
   [("dot", "dot", "-", "-"), ("-", "square", "-", "square"), ("dot", "dot+square", "-", "square")],
   "printed layer example: first {0,1}, second {1,3}, stack first-only 0, both 1, neither 2, second-only 3")
n = 6
subsets = list(itertools.product((0, 1), repeat=n))


def stack(a, b):
    return tuple(zip(a, b))


viol = 0
for a in subsets:
    sa = set(stab(a))
    for b in subsets:
        if set(stab(stack(a, b))) != sa & set(stab(b)):
            viol += 1
ok(viol == 0, "six-ring: stack's matching motions = intersection of the two layers' (all 4096 pairs)")
one = [a for a in subsets if sum(1 for t, _ in stab(a) if t == "s") == 1]
ok(all(not any(t == "r" for t, _ in stab(a)) for a in one), f"{len(one)} layers with exactly one flip; none has a matching turn")
good = [(a, b) for a in one for b in one if not stab(stack(a, b))]
ok(len(good) > 0, f"P5 is possible: {len(good)} ordered pairs of one-flip layers give a stack with no match")
L0 = tuple(1 if i == 0 else 0 for i in range(6))
L1 = tuple(1 if i == 1 else 0 for i in range(6))
L3 = tuple(1 if i == 3 else 0 for i in range(6))
ok(stab(L0) == [("s", 0)] and stab(L1) == [("s", 2)] and not stab(stack(L0, L1)),
   "guide witness: mark 0 has only k=0, mark 1 only k=2, stack has no match")
ok(("s", 0) in stab(stack(L0, L3)), "guide: marks at opposite spots 0 and 3 share k=0, so that stack keeps it")
H = ("r", 3)
hl = [a for a in subsets if H in stab(a)]
ok(all(H in stab(stack(a, b)) for a in hl for b in hl), f"P6: all {len(hl)**2} pairs of half-turn layers keep the half-turn")
A03 = tuple(1 if i in (0, 3) else 0 for i in range(6))
A14 = tuple(1 if i in (1, 4) else 0 for i in range(6))
ok(H in stab(A03) and H in stab(A14) and H in stab(stack(A03, A14)), "guide example {0,3}, {1,4}")
# two different surviving reflections can disappear
ex = [(a, b) for a in subsets for b in subsets
      if any(t == "s" for t, _ in stab(a)) and any(t == "s" for t, _ in stab(b)) and not stab(stack(a, b))]
ok(len(ex) > 0, "two layers that each keep a flip can stack to nothing (overview claim)")

print("\nSUMMARY:", "all checks passed" if not FAIL else f"{len(FAIL)} FAIL: {FAIL}")
