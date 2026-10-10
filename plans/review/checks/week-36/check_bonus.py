#!/usr/bin/env python3
"""Week 36 bonus (W36-BONUS-v1) and its guide: independent brute-force checks.

Standard library only; the rule is common.allowed (any number of attributes).
Run: python3 check_bonus.py > out_check_bonus.txt
"""
import sys
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import TILES, SHAPES, FILLS, LINES, allowed, is_cap, name, ok, note, finish  # noqa: E402

IDX = {t: i for i, t in enumerate(TILES)}
LM = [sum(1 << IDX[t] for t in L) for L in LINES]


def has_line(mask):
    return any(mask & m == m for m in LM)


print("== P1: private-collection game, first player to own an allowed three loses")


@lru_cache(None)
def mover_wins(me, other):
    """Position: 'me' is to move.  A move that makes me own a three loses at once."""
    free = [i for i in range(9) if not (me | other) >> i & 1]
    if not free:
        return None  # cannot happen (the first player would own five tiles)
    for i in free:
        nxt = me | 1 << i
        if has_line(nxt):
            continue
        if not mover_wins(other, nxt):
            return True
    return False


ok(mover_wins(0, 0), "the first player can force a win")
first_moves = [i for i in range(9) if not mover_wins(0, 1 << i)]
ok(len(first_moves) == 9, "every one of the 9 first claims is winning (guide: 'claim any center')")
ok(all((1 << i) and True for i in range(9)), "9 tiles")


# can a filled board ever have no owner of a three?  (first owns 5)
ok(all(has_line(sum(1 << IDX[t] for t in S)) for S in combinations(TILES, 5)), "every 5 tiles contain an allowed three, so the game always ends")

# The guide's strategy: claim c, answer x with the point opposite x about c.
def opposite(c, x):
    for y in TILES:
        if y not in (c, x) and allowed((c, x, y)):
            return y


leaves = Counter()
fails = []


def run(c, first, second, k):
    for x in TILES:
        if x in first or x in second:
            continue
        s2 = second | {x}
        if not is_cap(s2):
            leaves[k + 1] += 1          # second player loses on its (k+1)-th claim
            continue
        y = opposite(c, x)
        if y in first or y in s2:
            fails.append(("taken", c, first, s2, y))
            continue
        f2 = first | {y}
        if not is_cap(f2):
            fails.append(("first owns three", c, f2))
            continue
        run(c, f2, s2, k + 1)


for c in TILES:
    run(c, frozenset({c}), frozenset(), 0)
ok(not fails, "the response is always free and the first player never owns a three, for all 9 centres")
ok(sum(leaves.values()) == 3024, "terminal branches over all centres: %d (guide: 3,024)" % sum(leaves.values()))
ok(max(leaves) == 4, "latest loss is on the second player's fourth claim: %s" % dict(leaves))
ok(Counter({3: 48 * 9, 4: 288 * 9}) == leaves, "per centre: 48 losses on claim 3 and 288 on claim 4")
# opposite pairs through the open circle (guide P1 solution)
CO = ("circle", "open")
got = {frozenset((x, opposite(CO, x))) for x in TILES if x != CO}
want = {frozenset({("circle", "striped"), ("circle", "solid")}), frozenset({("triangle", "open"), ("square", "open")}),
        frozenset({("triangle", "striped"), ("square", "solid")}), frozenset({("triangle", "solid"), ("square", "striped")})}
ok(got == want, "guide's four opposite pairs about the open circle")


# shared-three variant (guide 'upper continuation'): one shared collection, whoever completes a three loses
@lru_cache(None)
def shared_wins(S):
    free = [i for i in range(9) if not S >> i & 1]
    safe = [i for i in free if not has_line(S | 1 << i)]
    if not safe:
        return False          # must complete a three (or cannot move): loses
    return any(not shared_wins(S | 1 << i) for i in safe)


ok(not shared_wins(0), "shared-collection version: the first player loses (the winner changes)")

print()
print("== P2: ownership colours, no allowed three all one colour")
two = [v for v in product(range(2), repeat=9) if all(len({v[IDX[t]] for t in L}) > 1 for L in LINES)]
ok(not two, "no valid two-colour assignment (of 512)")
three = [v for v in product(range(3), repeat=9) if all(len({v[IDX[t]] for t in L}) > 1 for L in LINES)]
ok(len(three) == 3762, "valid assignments with three named colours: %d (guide: 3,762)" % len(three))
prof = Counter(tuple(sorted(Counter(v).values(), reverse=True)) for v in three)
note("colour-class sizes among valid assignments: %s" % dict(prof))
ok((3, 3, 3) in prof, "a 3/3/3 design exists (guide extension)")
witness = {("circle", "open"): "R", ("circle", "striped"): "R", ("circle", "solid"): "B",
           ("triangle", "open"): "R", ("triangle", "striped"): "R", ("triangle", "solid"): "B",
           ("square", "open"): "B", ("square", "striped"): "B", ("square", "solid"): "G"}
ok(all(len({witness[t] for t in L}) > 1 for L in LINES), "guide witness RRB/RRB/BBG has no one-colour three")

print()
print("== P3: one numbered version of each shape-fill tile, no allowed three")
CARDS = [(s, f, n) for s in SHAPES for f in FILLS for n in (1, 2, 3)]
ok(all(sum(1 for c in CARDS if c not in (a, b) and allowed((a, b, c))) == 1 for a, b in combinations(CARDS, 2)),
   "27 numbered cards: every pair has exactly one completion")
designs = []
for v in product((1, 2, 3), repeat=9):
    nine = [(t[0], t[1], v[IDX[t]]) for t in TILES]
    if not any(allowed(c) for c in combinations(nine, 3)):
        designs.append(v)
ok(len(designs) > 0, "valid designs exist: %d of 19,683 number choices" % len(designs))
ok(all(len(set(v)) == 3 for v in designs), "every valid design already uses all three numbers ('All three numbers must appear' is automatic)")
note("number-usage profiles of valid designs: %s" % dict(Counter(tuple(sorted(Counter(v).values(), reverse=True)) for v in designs)))
# guide witness: rows circle/triangle/square, columns open/striped/solid
M = [[1, 2, 2], [2, 3, 3], [2, 3, 3]]
wv = tuple(M[SHAPES.index(t[0])][FILLS.index(t[1])] for t in TILES)
ok(wv in designs, "guide witness 122/233/233 is valid")
ok(all(M[r][c] - 1 == (r * r + c * c) % 3 for r in range(3) for c in range(3)), "witness is number-1 = x^2+y^2 mod 3 (C,T,S and O,H,F = 0,1,2)")
ok(all((d1 * d1 + d2 * d2) % 3 != 0 for d1 in range(3) for d2 in range(3) if (d1, d2) != (0, 0)), "d1^2+d2^2 is never 0 mod 3 for a nonzero direction")
shift = all(tuple((x - 1 + k) % 3 + 1 for x in v) in set(designs) for v in designs for k in (1, 2))
ok(shift, "adding the same amount mod 3 to every number keeps every design valid")
D = set(designs)
perm_ok = True
for ps in permutations(range(3)):
    for pf in permutations(range(3)):
        for pn in permutations((1, 2, 3)):
            for v in designs[:50]:
                w = [0] * 9
                for t in TILES:
                    u = (SHAPES[ps[SHAPES.index(t[0])]], FILLS[pf[FILLS.index(t[1])]])
                    w[IDX[u]] = pn[v[IDX[t]] - 1]
                perm_ok &= tuple(w) in D
ok(perm_ok, "renaming the values of any attribute keeps designs valid")
ok(all(any(allowed(c) for c in combinations([(t[0], t[1], 1) for t in TILES], 3)) for _ in [0]) and
   sum(1 for c in combinations([(t[0], t[1], 1) for t in TILES], 3) if allowed(c)) == 12,
   "changing every number to 1 makes exactly the 12 shape/fill threes allowed")
single = Counter()
for v in designs:
    for i in range(9):
        for n in (1, 2, 3):
            if n == v[i]:
                continue
            w = list(v)
            w[i] = n
            single[tuple(w) in D] += 1
note("changing exactly one number of a valid design: still valid %d times, creates an allowed three %d times" % (single[True], single[False]))
# P3 versus P2: a number design is a three-colouring with no one-number three AND no all-different three
p2_441 = {v for v in three if sorted(Counter(v).values()) == [1, 4, 4]}
p3_as_colours = {tuple(x - 1 for x in v) for v in designs}
ok(p3_as_colours == p2_441, "the 162 number designs are exactly the 162 P2 colourings with class sizes 4/4/1")
rainbow_free = {v for v in three if all(len({v[IDX[t]] for t in L}) == 2 for L in LINES)}
ok(rainbow_free == p3_as_colours, "equivalently: P2 colourings in which no allowed three uses all three colours")
wit = tuple("RBG".index(witness[t]) for t in TILES)
ok(wit in p3_as_colours, "the guide's P2 witness RRB/RRB/BBG, read as numbers, is also a P3 design")

# numbered-copy extension: nine-card line-free sets of the 27 cards that repeat a shape/fill tile
caps9 = []
def grow(chosen, start):
    if len(chosen) == 9:
        caps9.append(tuple(chosen))
        return
    for i in range(start, 27):
        c = CARDS[i]
        if any(allowed((a, b, c)) for a, b in combinations(chosen, 2)):
            continue
        chosen.append(c)
        grow(chosen, i + 1)
        chosen.pop()
grow([], 0)
dup = [S for S in caps9 if len({(c[0], c[1]) for c in S}) < 9]
note("line-free 9-card sets among all 27 cards: %d; with a repeated shape/fill tile: %d; one per tile: %d" % (
    len(caps9), len(dup), len(caps9) - len(dup)))
ok(len(caps9) - len(dup) == len(designs), "the one-per-tile 9-card line-free sets are exactly the P3 designs")
ok(all(not any(allowed(c) for c in combinations(S, 3)) for S in dup[:5]), "examples with a repeat are line-free")
if dup:
    print("  example with a repeated tile:", sorted((name((c[0], c[1])), c[2]) for c in dup[0]))
finish()
