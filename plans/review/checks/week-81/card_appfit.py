"""Week 81 card: checks behind the App fit section and two card claims.

Independent of the package checker and of math.md's scripts. Plain recursion
over legal moves of the bucket game: remove `take` counters (default 1) from a
nonempty bucket j, then add 0..cap counters to each bucket left of j.
Buckets are listed left to right (bucket 1 first). Normal play.

Checks:
 1. Cap 0 versus cap 1: with no refills the second player wins exactly when the
    total is even; with cap 1 exactly when every bucket is even. (1,1) differs.
 2. Second-player starts among the two-bucket cards 0-3 and three-bucket 0-3.
 3. Number of distinct first moves from small all-even starts (cap 1), for an
    "every reply" round.
 4. Longest game under cap K equals sum a_i (K+1)^i (bucket 1 has i = 0), and
    every play that always refills fully reaches it.
 5. Encore: take 1..3, refill 0..3 per bucket: second player wins iff every
    bucket is a multiple of 4 (small cases).
"""
from functools import lru_cache
from itertools import product
import random


def moves(pos, cap, takes=(1,)):
    out = set()
    for j, c in enumerate(pos):
        for t in takes:
            if c >= t:
                for adds in product(range(cap + 1), repeat=j):
                    new = list(pos)
                    new[j] -= t
                    for i, a in enumerate(adds):
                        new[i] += a
                    out.add(tuple(new))
    return out


def make_win(cap, takes=(1,)):
    @lru_cache(maxsize=None)
    def win(pos):
        return any(not win(q) for q in moves(pos, cap, takes))
    return win


def longest(cap):
    @lru_cache(maxsize=None)
    def L(pos):
        ms = moves(pos, cap)
        return 0 if not ms else 1 + max(L(q) for q in ms)
    return L


fails = 0

# 1. cap 0 vs cap 1
w0, w1 = make_win(0), make_win(1)
for n in (1, 2, 3):
    for pos in product(range(5), repeat=n):
        if w0(pos) != (sum(pos) % 2 == 1):
            fails += 1; print("cap0 parity fails", pos)
        if w1(pos) != any(c % 2 for c in pos):
            fails += 1; print("cap1 all-even fails", pos)
print("1. cap 0: second player wins iff total even; cap 1: iff all even (1-3 buckets, 0-4 each).")
print("   (1,1): cap 0 ->", "first" if w0((1, 1)) else "second", "player; cap 1 ->", "first" if w1((1, 1)) else "second", "player")

# 2. second-player starts
two = [p for p in product(range(4), repeat=2) if not w1(p)]
three = [p for p in product(range(4), repeat=3) if not w1(p)]
print("2. two-bucket 0-3 second-player starts:", two, f"({len(two)} of 16)")
print("   three-bucket 0-3 second-player starts:", len(three), "of 64, nonempty:", len([p for p in three if any(p)]), "of 63")

# 3. first moves from all-even starts
for pos in [(2, 0), (0, 2), (2, 2), (0, 2, 0), (2, 2, 2), (2, 0, 2), (0, 0, 2)]:
    print("3. first moves from", pos, "under cap 1:", len(moves(pos, 1)))

# 4. longest game
for K in (1, 2, 3):
    L = longest(K)
    for n in (1, 2, 3):
        for pos in product(range(3), repeat=n):
            phi = sum(c * (K + 1) ** i for i, c in enumerate(pos))
            if L(pos) != phi:
                fails += 1; print("longest fails", K, pos, L(pos), phi)
    # greedy full refill reaches it from (1,1,1) whatever bucket is chosen
    rng = random.Random(81 + K)
    for _ in range(200):
        pos, steps = (1, 1, 1), 0
        while any(pos):
            j = rng.choice([i for i, c in enumerate(pos) if c])
            pos = tuple((c + K if i < j else c - 1 if i == j else c) for i, c in enumerate(pos))
            steps += 1
        if steps != 1 + (K + 1) + (K + 1) ** 2:
            fails += 1; print("greedy fails", K, steps)
print("4. longest game under cap K = buckets read in base K+1 (K = 1-3, 0-2 each, 1-3 buckets);")
print("   always refilling fully reaches it in 200 random plays from (1,1,1) per K. (1,1,1), K=1: 7 moves.")

# 5. encore
we = make_win(3, takes=(1, 2, 3))
bad = []
for n in (1, 2):
    for pos in product(range(7), repeat=n):
        if we(pos) != any(c % 4 for c in pos):
            bad.append(pos)
for pos in product(range(5), repeat=3):
    if we(pos) != any(c % 4 for c in pos):
        bad.append(pos)
fails += len(bad)
print("5. encore take 1-3, refill 0-3: second player iff all multiples of 4;", "holds" if not bad else f"fails at {bad[:5]}",
      "(1-2 buckets 0-6, 3 buckets 0-4)")

print("FAILURES:", fails)
