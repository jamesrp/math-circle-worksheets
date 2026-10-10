#!/usr/bin/env python3
"""Week 36 (Making threes) base packet: independent brute-force checks.

Every claim on the three student packets and in week-36-facilitator.pdf that
has a mathematical answer is transcribed below and tested by enumeration from
the printed rule (common.allowed).  Standard library only.
Run: python3 check_math.py > out_check_math.txt
"""
import sys
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (TILES, SHAPES, FILLS, LINES, allowed, is_cap, completions, name,  # noqa: E402
                    ok, note, finish)

T = {name(t): t for t in TILES}


def N(*codes):
    return frozenset(T[c] for c in codes)


print("== Rule, completion and incidence (guide p.1 'Unique completion and incidence')")
pairs = list(combinations(TILES, 2))
ok(len(pairs) == 36, "36 unordered pairs")
ok(all(len(completions(a, b)) == 1 for a, b in pairs), "every pair of distinct tiles has exactly one completing tile")


def rule(a, b):
    """Guide: keep the shared value, or use the missing value when the two differ."""
    out = []
    for k, vals in enumerate((SHAPES, FILLS)):
        out.append(a[k] if a[k] == b[k] else [v for v in vals if v not in (a[k], b[k])][0])
    return tuple(out)


ok(all(completions(a, b) == [rule(a, b)] for a, b in pairs), "the guide's keep/missing-value rule gives that tile")
ok(all(rule(a, b) not in (a, b) for a, b in pairs), "the completion always differs from both inputs")
# z = -x - y mod 3 under EVERY encoding of the values as 0,1,2
good = 0
for es in permutations(range(3)):
    for ef in permutations(range(3)):
        enc = {t: (es[SHAPES.index(t[0])], ef[FILLS.index(t[1])]) for t in TILES}
        dec = {v: k for k, v in enc.items()}
        good += all(dec[tuple((-enc[a][i] - enc[b][i]) % 3 for i in range(2))] == rule(a, b) for a, b in pairs)
ok(good == 36, "completion z = -x-y (mod 3) holds for all 36 encodings of the values as 0,1,2")
ok(len(LINES) == 12, "12 allowed threes")
ok(all(sum(t in L for L in LINES) == 4 for t in TILES), "four allowed threes through each tile")
meets = Counter(len(A & B) for A, B in combinations(LINES, 2))
ok(set(meets) == {0, 1}, "distinct threes meet in 0 or 1 tile: %s" % dict(meets))
kinds = Counter(("shape-same" if len({t[0] for t in L}) == 1 else "fill-same" if len({t[1] for t in L}) == 1 else "both-different") for L in LINES)
ok(kinds == Counter({"shape-same": 3, "fill-same": 3, "both-different": 6}),
   "3 same-shape + 3 same-fill + 6 all-different-both threes (guide p.4 direct count): %s" % dict(kinds))
ok(not any(len({t[0] for t in c}) == 1 and len({t[1] for t in c}) == 1 for c in combinations(TILES, 3)),
   "no three different tiles are all-same in both attributes")

print()
print("== Partitions into three allowed threes (K-1 P2, 2-3 P2, 4-5 P4, guide p.4 key)")
parts = set()
for A, B, C in combinations(LINES, 3):
    if len(A | B | C) == 9:
        parts.add(frozenset((A, B, C)))
ok(len(parts) == 4, "exactly %d unordered splits" % len(parts))
key = [
    [N("CO", "CH", "CF"), N("TO", "TH", "TF"), N("SO", "SH", "SF")],
    [N("CO", "TO", "SO"), N("CH", "TH", "SH"), N("CF", "TF", "SF")],
    [N("CO", "TH", "SF"), N("CH", "TF", "SO"), N("CF", "TO", "SH")],
    [N("CO", "TF", "SH"), N("CH", "TO", "SF"), N("CF", "TH", "SO")],
]
ok({frozenset(s) for s in key} == parts, "the guide's Splits 1-4 are exactly the four splits")
ok({L for s in key for L in s} == set(LINES) and len([L for s in key for L in s]) == 12,
   "the 12 triples of the key are the 12 allowed threes, each once")
ok(all(sum(1 for M in LINES if not (L & M) and M != L) == 2 for L in LINES),
   "each allowed three is disjoint from exactly two others (its split companions)")
# direction argument: coordinates C,T,S = 0,1,2 and O,H,F = 0,1,2
co = {t: (SHAPES.index(t[0]), FILLS.index(t[1])) for t in TILES}


def direction(L):
    a, b = sorted(co[t] for t in L)[:2]
    d = ((b[0] - a[0]) % 3, (b[1] - a[1]) % 3)
    return d if d in ((1, 0), (0, 1), (1, 1), (1, 2)) else ((2 * d[0]) % 3, (2 * d[1]) % 3)


ok(all((direction(A) == direction(B)) == (not (A & B)) for A, B in combinations(LINES, 2)),
   "two distinct threes are disjoint iff they have the same direction (4 directions)")
ok(Counter(direction(L) for L in LINES) == Counter({d: 3 for d in ((1, 0), (0, 1), (1, 1), (1, 2))}),
   "three threes in each of the four directions")

print()
print("== Collections with no allowed three (K-1 P3, 2-3 P3, 4-5 P2, guide p.1 and p.5)")
caps = {k: [frozenset(c) for c in combinations(TILES, k) if is_cap(c)] for k in range(10)}
counts = [len(caps[k]) for k in range(10)]
ok(counts[:6] == [1, 9, 36, 72, 54, 0], "line-free subsets of sizes 0..5: %s (guide: 1, 9, 36, 72, 54, 0)" % counts[:6])
ok(max(k for k in range(10) if caps[k]) == 4, "maximum line-free size is 4")
rects = [frozenset((s, f) for s in ss for f in ff) for ss in combinations(SHAPES, 2) for ff in combinations(FILLS, 2)]
ok(all(R in caps[4] for R in rects), "all 9 two-by-two attribute rectangles are line-free (guide witness)")
w = N("CO", "CH", "TO", "TH")
ok(w in caps[4], "K-1/2-3/4-5 witness {open circle, striped circle, open triangle, striped triangle} is line-free")
ok(all(any(Counter(t[k] for t in c).most_common(1)[0][1] == 2 for k in range(2)) for c in combinations(w, 3)),
   "every triple of the witness has exactly two of some shape or fill")
note("4-caps that are 2x2 rectangles: %d of %d" % (len(rects), len(caps[4])))
# ten-pair proof ingredients, tested on every 5-set (all of which contain a three)
dish_ok = True
for S in combinations(TILES, 5):
    for x in TILES:
        if x in S:
            continue
        P = [p for p in combinations(S, 2) if allowed(p + (x,))]
        if any(set(p) & set(q) for p, q in combinations(P, 2)) or len(P) > 2:
            dish_ok = False
ok(dish_ok, "for every 5-set S and tile x outside S: the pairs of S completed by x are disjoint and at most 2")
ok(all(len([p for p in combinations(TILES, 2) if x not in p and allowed(p + (x,))]) == 4 for x in TILES),
   "each tile completes exactly 4 pairs, and they partition the other 8 tiles")
for k in range(5):
    ext = Counter(sum(1 for t in TILES if t not in S and is_cap(S | {t})) for S in caps[k])
    want = {0: 9, 1: 8, 2: 6, 3: 3, 4: 0}[k]
    ok(set(ext) == {want}, "every line-free collection of size %d has exactly %d legal additions" % (k, want))
three_ok = all(
    {t for t in TILES if t not in S and not is_cap(S | {t})} == {completions(a, b)[0] for a, b in combinations(S, 2)}
    and len({completions(a, b)[0] for a, b in combinations(S, 2)}) == 3 for S in caps[3])
ok(three_ok, "for a line-free three, the forbidden fourth tiles are exactly the 3 distinct pair completions")
maximal = [S for k in range(10) for S in caps[k] if not any(is_cap(S | {t}) for t in TILES if t not in S)]
ok({len(S) for S in maximal} == {4}, "every maximal line-free collection has size 4 (%d of them)" % len(maximal))
# 2-3 P3: change one tile of a maximum collection, then add another
swap_add = any(is_cap((S - {a}) | {b, c}) for S in caps[4] for a in S for b in TILES for c in TILES
               if b not in S and c not in S and b != c)
ok(not swap_add, "2-3 P3: from any 4-tile collection, changing one tile and then adding another never works")

print()
print("== Shared adding game (2-3 P5, 4-5 P5)")
lengths = Counter()


def play(S, depth):
    moves = [t for t in TILES if t not in S and is_cap(S | {t})]
    if not moves:
        lengths[depth] += 1
        return
    for t in moves:
        play(S | {t}, depth + 1)


play(frozenset(), 0)
ok(set(lengths) == {4}, "every legal ordered play lasts exactly 4 moves (%d sequences)" % sum(lengths.values()))
ok(sum(lengths.values()) == 9 * 8 * 6 * 3, "number of ordered plays = 9*8*6*3 = 1296")
note("move 4 is made by the second player; the first player then cannot move and loses, whatever anyone chooses")

print()
print("== Guide keys (pp. 3-4) and launch")
ok(allowed((T["CO"], T["TF"], T["SH"])), "printed allowed triple: open circle, solid triangle, striped square")
ok(not allowed((T["CO"], T["TO"], T["SF"])), "printed near miss: open circle, open triangle, solid square")
key1 = [("CO", "CH", "CF"), ("CO", "TO", "SO"), ("CH", "TF", "SO"), ("TH", "SO", "CF")]
ok(all(completions(T[a], T[b]) == [T[c]] for a, b, c in key1), "guide's four printed-pair completions")
through = {frozenset({T["CH"], T["CF"]}), frozenset({T["TO"], T["SO"]}), frozenset({T["TH"], T["SF"]}), frozenset({T["TF"], T["SH"]})}
ok({L - {T["CO"]} for L in LINES if T["CO"] in L} == through, "guide K-1 P4: the four pairs through the open circle")
ok(not (N("CO", "CH", "CF") & N("TO", "TH", "TF")) and len(N("CO", "CH", "CF") & N("CO", "TO", "SO")) == 1,
   "4-5 P3 key examples: circles vs triangles disjoint; circles vs open tiles share one tile")
finish()
