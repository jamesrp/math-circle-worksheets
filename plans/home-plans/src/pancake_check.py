#!/usr/bin/env python3
"""Check every factual claim in plans/home-plans/2026-11-14-pancake-flips.md.

    python3 plans/home-plans/src/pancake_check.py

Conventions (the plan's). A stack is written top to bottom, sizes 1 (smallest)
to n (biggest): (4, 2, 3, 1) has the biggest on top and the smallest at the
bottom. Sorted means 1, 2, ..., n from top to bottom, biggest on the plate.
A flip of k lifts the top k together and turns them over, which reverses their
order. Flipping 1 changes nothing in the plain game. In the burnt game each lid
also has a side (rim down is right; a negative size means rim up), and every
lid in a flip turns over, so flipping 1 does something.

Exits non-zero if any claim fails.
"""
from collections import Counter, deque
from itertools import permutations
import sys

FAILS = []


def check(ok, text):
    print(("PASS  " if ok else "FAIL  ") + text)
    if not ok:
        FAILS.append(text)


def flip(s, k):
    return s[:k][::-1] + s[k:]


def distances(n):
    """Fewest flips from every stack of n to sorted (BFS from sorted; flips undo themselves)."""
    goal = tuple(range(1, n + 1))
    d = {goal: 0}
    q = deque([goal])
    while q:
        s = q.popleft()
        for k in range(2, n + 1):
            t = flip(s, k)
            if t not in d:
                d[t] = d[s] + 1
                q.append(t)
    return d


def breakpoints(s):
    """Neighbouring pairs that don't belong together (sizes not one apart),
    counting the bottom lid against the plate, which counts as size n + 1."""
    t = list(s) + [len(s) + 1]
    return sum(abs(t[i] - t[i + 1]) != 1 for i in range(len(s)))


def recipe(s):
    """Biggest unsorted lid to the top, then down to its place; skip a flip that
    isn't needed. Returns the number of flips."""
    s = list(s)
    n = len(s)
    flips = 0
    for m in range(n, 1, -1):          # place lid m at depth m
        if s[m - 1] == m:
            continue
        i = s.index(m)
        if i != 0:
            s = flip(s, i + 1)
            flips += 1
        s = flip(s, m)
        flips += 1
    assert s == sorted(s)
    return flips


# ------------------------------------------------------------ plain pancakes
D = {n: distances(n) for n in range(2, 8)}
worst = {n: max(D[n].values()) for n in D}
for n in D:
    check(len(D[n]) == len(list(permutations(range(n)))), f"BFS reaches all stacks of {n}")
check(worst[2] == 1 and worst[3] == 3 and worst[4] == 4 and worst[5] == 5 and worst[6] == 7 and worst[7] == 8,
      "fewest flips that always suffice: 2 lids 1, 3 lids 3, 4 lids 4, 5 lids 5, 6 lids 7, 7 lids 8")

hard = {n: sorted(s for s in D[n] if D[n][s] == worst[n]) for n in D}
check(hard[3] == [(1, 3, 2)], "3 lids: only one stack needs 3 flips: small, big, middle (top to bottom)")
check(hard[4] == [(2, 4, 1, 3), (3, 1, 4, 2), (4, 2, 3, 1)],
      "4 lids: exactly three stacks need 4 flips: 2-4-1-3, 3-1-4-2, 4-2-3-1")
check(len(hard[5]) == 20, "5 lids: 20 of the 120 stacks need 5 flips")
check(hard[6] == [(4, 6, 2, 5, 1, 3), (5, 3, 6, 1, 4, 2)], "6 lids: only two stacks need 7 flips: 4-6-2-5-1-3 and 5-3-6-1-4-2")
check(Counter(D[4].values()) == Counter({0: 1, 1: 3, 2: 6, 3: 11, 4: 3}),
      "4 lids, how many stacks need 0..4 flips: 1, 3, 6, 11, 3")
check(sum(1 for s in D[5] if D[5][s] >= 4) == 68, "5 lids: 68 stacks need 4 or 5 flips")

check(all(flip(flip(s, k), k) == s for s in D[5] for k in range(2, 6)),
      "a flip undoes itself, so a stack scrambled in k flips can be sorted in k")
check(Counter(D[3].values()) == Counter({0: 1, 1: 2, 2: 2, 3: 1}), "3 lids: 1, 2, 2, 1 stacks need 0, 1, 2, 3 flips")

# breakpoint lower bound
for n in D:
    ok = all(abs(breakpoints(flip(s, k)) - breakpoints(s)) <= 1 for s in D[n] for k in range(2, n + 1))
    check(ok, f"{n} lids: a flip changes the number of bad neighbour pairs by at most 1")
    check(all(D[n][s] >= breakpoints(s) for s in D[n]), f"{n} lids: flips needed >= bad neighbour pairs")
check([breakpoints(s) for s in hard[4]] == [4, 4, 3],
      "zigzags 2-4-1-3 and 3-1-4-2 have 4 bad pairs (so the pair count proves they need 4); 4-2-3-1 has only 3")
check(all(breakpoints(s) == 6 for s in hard[6]), "the two hardest 6-stacks have 6 bad pairs but need 7: the count doesn't prove it")
check(sorted(flip((4, 2, 3, 1), k) for k in range(2, 5)) == [(1, 3, 2, 4), (2, 4, 3, 1), (3, 2, 4, 1)]
      and all(D[4][flip((4, 2, 3, 1), k)] == 3 for k in range(2, 5)),
      "4-2-3-1: its three one-flip neighbours 2-4-3-1, 3-2-4-1, 1-3-2-4 all need 3, so it needs 4")

check([breakpoints(s) for s in [(2, 4, 3, 1), (3, 2, 4, 1), (1, 3, 2, 4)]] == [3, 3, 2] and D[4][(1, 3, 2, 4)] == 3,
      "bad pairs: 2-4-3-1 has 3, 3-2-4-1 has 3, 1-3-2-4 has 2 but needs 3")


def greedy_reaches_sorted(s):
    """Follow only flips that remove a bad pair. Can that ever reach sorted?"""
    seen, stack = {s}, [s]
    while stack:
        u = stack.pop()
        if breakpoints(u) == 0:
            return True
        for k in range(2, len(u) + 1):
            v = flip(u, k)
            if breakpoints(v) == breakpoints(u) - 1 and v not in seen:
                seen.add(v)
                stack.append(v)
    return False


check(all(not greedy_reaches_sorted(s) for s in hard[6]),
      "6 lids: from either hardest stack, flips that each fix a bad pair always get stuck, so 6 flips can't do it")
check([s for s in D[5] if breakpoints(s) == 5 and D[5][s] == 5] != [], "some hardest 5-stacks are proved by the pair count")
check(all(D[n][s] == breakpoints(s) for n in D for s in D[n] if breakpoints(s) == 0) and
      all(breakpoints(s) > 0 for n in D for s in D[n] if s != tuple(range(1, n + 1))),
      "no bad pairs exactly when the stack is sorted")

# the recipe
for n in range(2, 8):
    r = {s: recipe(s) for s in D[n]}
    check(max(r.values()) == 2 * n - 3, f"{n} lids: the recipe never needs more than 2n-3 = {2*n-3} flips, and some stack needs that many")
    check(all(r[s] >= D[n][s] for s in D[n]), f"{n} lids: the recipe never beats the fewest (sanity)")
r3 = {s: recipe(s) for s in D[3]}
check(all(r3[s] == D[3][s] for s in D[3]), "3 lids: the recipe always uses the fewest flips")
r4 = {s: recipe(s) for s in D[4]}
check(sorted(s for s in D[4] if r4[s] > D[4][s]) == [(1, 2, 4, 3), (1, 4, 3, 2), (2, 4, 3, 1), (3, 2, 4, 1)],
      "4 lids: the recipe wastes flips on exactly 4 of 24 stacks: 1-2-4-3, 1-4-3-2, 2-4-3-1, 3-2-4-1")
check(sorted(s for s in D[4] if r4[s] == 5) == [(2, 4, 3, 1), (3, 2, 4, 1)] and D[4][(2, 4, 3, 1)] == 3 and D[4][(3, 2, 4, 1)] == 3,
      "4 lids: the recipe takes 5 only on 2-4-3-1 and 3-2-4-1, and each can be done in 3")
check([r4[s] for s in hard[4]] == [4, 4, 4],
      "4 lids, the three hardest stacks: the recipe uses 4, the fewest possible")
check(D[4][(1, 4, 3, 2)] == 3 and D[4][(1, 2, 4, 3)] == 3, "1-4-3-2 and 1-2-4-3: 3 flips, the recipe takes 4")
sol = {(2, 4, 3, 1): (3, 2, 4), (3, 2, 4, 1): (2, 3, 4), (1, 4, 3, 2): (4, 3, 4), (1, 2, 4, 3): (4, 2, 4)}
for s, ks in sol.items():
    u = s
    for k in ks:
        u = flip(u, k)
    check(u == (1, 2, 3, 4), "-".join(map(str, s)) + " sorted by flips " + ", ".join(map(str, ks)))
r5 = {s: recipe(s) for s in D[5]}
check(max(r5.values()) == 7 and sum(r5[s] > D[5][s] for s in D[5]) == 45 and max(r5[s] - D[5][s] for s in D[5]) == 3,
      "5 lids: the recipe can take 7, wastes flips on 45 of 120 stacks, at most 3 extra")
check(Counter(r5[s] for s in hard[5]) == Counter({5: 10, 6: 7, 7: 3}),
      "5 lids, the 20 hardest stacks: recipe uses 5 on 10, 6 on 7, 7 on 3")

# worked example in the plan: 3-1-4-2 in 4 flips
ex = [(3, 1, 4, 2)]
for k in (3, 4, 2, 3):
    ex.append(tuple(flip(list(ex[-1]), k)))
check(ex[-1] == (1, 2, 3, 4), "worked solution for 3-1-4-2: flip 3, 4, 2, 3 -> " + " ; ".join("-".join(map(str, s)) for s in ex))
ex2 = [(4, 2, 3, 1)]
for k in (4, 2, 3, 2):
    ex2.append(tuple(flip(list(ex2[-1]), k)))
check(ex2[-1] == (1, 2, 3, 4), "worked solution for 4-2-3-1: flip 4, 2, 3, 2 -> " + " ; ".join("-".join(map(str, s)) for s in ex2))
# launch demo stack 2-3-1 with the recipe
demo = [(2, 3, 1)]
for k in (2, 3):
    demo.append(tuple(flip(list(demo[-1]), k)))
check(demo[-1] == (1, 2, 3) and D[3][(2, 3, 1)] == 2, "launch demo 2-3-1: flip 2, then 3 -> sorted, and 2 is fewest")
check(D[3][(1, 3, 2)] == 3 and recipe((1, 3, 2)) == 3, "1-3-2 (Rose's tricky one): needs 3, recipe takes 3")


# ------------------------------------------------------------ burnt pancakes
def bflip(s, k):
    return tuple(-x for x in s[:k][::-1]) + s[k:]


def bdist(n):
    goal = tuple(range(1, n + 1))
    d = {goal: 0}
    q = deque([goal])
    while q:
        s = q.popleft()
        for k in range(1, n + 1):
            t = bflip(s, k)
            if t not in d:
                d[t] = d[s] + 1
                q.append(t)
    return d


BD = {n: bdist(n) for n in range(1, 6)}
check([max(BD[n].values()) for n in range(1, 6)] == [1, 4, 6, 8, 10],
      "burnt, fewest flips that always suffice: 1, 4, 6, 8, 10 for 1 to 5 lids")
check(all(BD[n][tuple(-x for x in range(1, n + 1))] == 2 * n for n in range(2, 6)),
      "burnt: the right order but every lid rim up needs 2n flips (2 lids: 4; 3 lids: 6; 4 lids: 8)")
check(len(BD[4]) == 384 and sum(v == 8 for v in BD[4].values()) == 3,
      "burnt 4 lids: 384 stacks, 3 need 8 flips")
check(BD[2][(-1, -2)] == 4 and BD[2][(1, -2)] == 3,
      "burnt 2 lids: both rim up needs 4; small right, big rim up needs 3")

print()
if FAILS:
    print(f"{len(FAILS)} claim(s) FAILED")
    sys.exit(1)
print("all claims pass")
