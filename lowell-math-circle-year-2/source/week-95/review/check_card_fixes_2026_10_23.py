#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card fixes to Week 95. Standard library only.

1. Live game (both bands, Problem 1). If the hidden bag is the run A, B, C, ..., the
   highest letter caught gives the total away (review math check, item 1). The fix:
   the adult keeper turns the whole kit letter-down, mixes it and counts the hidden
   total into the bag, so the bag is a uniformly random set of letters from A-X.
   a. Reproduce the leak under run filling.
   b. Under shuffled filling, check by exact enumeration (small kit) that the letters
      seen tell nothing about the total beyond how many different letters were seen;
      then, at the real sizes, compare the best possible guess of the total from the
      letters under run and shuffled filling with the best guess from that count alone.
2. Grades 4-5 Problem 5 (new wording): the bag holds 12 to 20 objects (the zero round
   proves at least 12; the keeper says at most 20). Which catch sizes make overlap 0
   impossible? Key: each catch at most 12 and the two totalling at least 21.
3. K-1 route: 5 counters with 3 dotted; can a catch of 3 miss every dot? With 6?

Run: python3 check_card_fixes_2026_10_23.py
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import comb

fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def possible_overlaps(N, M, n):
    """Overlaps realised by some pair of catches, by enumeration over second catches."""
    first = set(range(M))
    return sorted({len(first & set(c)) for c in combinations(range(N), n)})


# ---------------------------------------------------------------- 1a. the leak
KIT = 24
LIVE = {'2-3': (4, range(8, 21)), '4-5': (6, range(12, 25))}
print('== 1a. Run filling A, B, C, ...: P(highest letter caught = total) over three rounds ==')
for band, (c, totals) in LIVE.items():
    row = []
    for N in totals:
        miss = F(comb(N - 1, c), comb(N, c))          # one object misses one catch of c
        p = 1 - miss ** 6                              # six catches in three rounds
        row.append(p)
        if N % 4 == 0:
            print(f'  {band} N={N:2d}: {float(p):.3f}')
    check(min(row) > F(7, 10), f'{band}: under run filling the highest letter equals the total with probability '
                               f'{float(min(row)):.2f} to {float(max(row)):.2f} (the leak the card measured)')

# ------------------------------------------------- 1b. shuffled filling, exact small case
print('== 1b. Shuffled filling: letters add nothing beyond the count of different letters seen ==')
K, C, ROUNDS = 7, 2, 2                                  # small kit, catches of 2, two rounds
records = defaultdict(lambda: defaultdict(F))          # N -> (overlaps, seen set) -> probability
for N in range(4, K + 1):
    bags = list(combinations(range(K), N))
    for bag in bags:
        pb = F(1, len(bags))
        rounds = [((), F(1))]                          # (list of (overlap, seen set)), probability
        catches = list(combinations(bag, C))
        for _ in range(ROUNDS):
            nxt = []
            for hist, p in rounds:
                for a in catches:
                    for b in catches:
                        nxt.append((hist + ((len(set(a) & set(b)), frozenset(a) | frozenset(b)),),
                                    p / len(catches) ** 2))
            rounds = nxt
        for hist, p in rounds:
            overlaps = tuple(h[0] for h in hist)
            seen = frozenset().union(*(h[1] for h in hist))
            records[N][(overlaps, seen)] += pb * p
ok = True
for N, dist in records.items():
    by_summary = defaultdict(list)
    for (overlaps, seen), p in dist.items():
        by_summary[(overlaps, len(seen))].append(p)
    for (overlaps, k), ps in by_summary.items():
        # every k-set of letters occurs, each equally likely, whatever the total
        ok &= len(ps) == comb(K, k) and len(set(ps)) == 1
check(ok, f'kit of {K}, totals 4-{K}, two rounds of catches of {C}: given the overlaps and the number of '
          f'different letters seen, every set of that many letters is equally likely for every total, so the '
          f'letters themselves carry no information about the total')


def union_dist(N, sizes):
    """Distribution of |A1 u ... u Ar| for independent uniform subsets of {1..N} of the given sizes."""
    d = {0: F(1)}
    for s in sizes:
        e = defaultdict(F)
        for u, p in d.items():
            for j in range(0, min(u, s) + 1):           # j of the new set already seen
                w = comb(u, j) * comb(N - u, s - j)
                if w:
                    e[u + s - j] += p * F(w, comb(N, s))
        d = dict(e)
    return d


def seen_count_dist(N, c, rounds=3):
    """Different objects seen in three rounds of two catches of c from a bag of N."""
    first = F(1)
    per_round = {}
    for r in range(0, c + 1):
        w = comb(c, r) * comb(N - c, c - r)
        if w:
            per_round[2 * c - r] = F(w, comb(N, c))
    total = defaultdict(F)
    def go(i, sizes, p):
        if i == rounds:
            for u, q in union_dist(N, sizes).items():
                total[u] += p * q
            return
        for s, q in per_round.items():
            go(i + 1, sizes + [s], p * q)
    go(0, [], first)
    return dict(total)


print('== 1b. Real sizes: the best possible guess of the total from the letters seen, letters A-X ==')
# Shuffled filling: the bag is a uniform N-set of the 24 letters and, given k, the letters seen
# are a uniform k-set of the bag (catches are uniform in the bag; checked exactly above on a
# small kit), hence a uniform k-set of all 24 letters: P(highest = m | k, N) = C(m-1,k-1)/C(24,k).
# Run filling: the bag is letters 1..N, so P(highest = m | k, N) = C(m-1,k-1)/C(N,k).
# With every allowed total equally likely, compare the best possible guess (most probable
# total) from k and the highest letter, under each filling, with the best guess from k alone.
for band, (c, totals) in LIVE.items():
    totals = list(totals)
    pk = {N: seen_count_dist(N, c) for N in totals}
    for N in totals:
        assert sum(pk[N].values()) == 1
    prior = F(1, len(totals))
    ks = sorted({k for N in totals for k in pk[N]})
    k_only = sum(max(prior * pk[N].get(k, 0) for N in totals) for k in ks)
    def best(cond):
        return sum(max(prior * pk[N].get(k, 0) * cond(m, k, N) for N in totals)
                   for k in ks for m in range(1, KIT + 1))
    run = best(lambda m, k, N: F(comb(m - 1, k - 1), comb(N, k)) if k <= m <= N else 0)
    shuf = best(lambda m, k, N: F(comb(m - 1, k - 1), comb(KIT, k)))
    print(f'  {band}: best guess right with probability {float(run):.3f} (run filling), {float(shuf):.3f} '
          f'(shuffled), {float(k_only):.3f} (count of different letters only), {float(prior):.3f} (blind)')
    check(shuf == k_only < run,
          f'{band}: with shuffled filling the letters add nothing to the count of different letters seen '
          f'(best guess {float(shuf):.3f} either way); with run filling they lift it to {float(run):.3f}')

# ------------------------------------------------------------- 2. Grades 4-5 Problem 5
print('== 2. Grades 4-5 Problem 5: bag of 12 to 20; which catch sizes rule out overlap 0? ==')
check(possible_overlaps(11, 6, 6)[0] > 0 and 0 in possible_overlaps(12, 6, 6),
      'a record of 6 and 6 with overlap 0 needs at least 12 objects')
for N in range(1, 21):
    for M in range(1, N + 1):
        for n in range(1, N + 1):
            if (0 not in possible_overlaps(N, M, n)) != (M + n > N):
                check(False, f'zero impossible exactly when M + n > N fails at N={N}, M={M}, n={n}')
check(True, 'for every bag up to 20 and every pair of catches, overlap 0 is impossible exactly when M + n > N')
allowed = range(12, 21)
answers = sorted((M, n) for M in range(1, 25) for n in range(1, 25)
                 if all(M <= N and n <= N for N in allowed)
                 and all(0 not in possible_overlaps(N, M, n) for N in allowed))
check(answers == sorted((M, n) for M in range(1, 13) for n in range(1, 13) if M + n >= 21),
      f'the catch sizes are exactly the pairs with each at most 12 and total at least 21: {answers}')
check((12, 9) in answers and (11, 10) in answers and (10, 10) not in answers and (13, 8) not in answers,
      '12 + 9 and 11 + 10 work; 10 + 10 still allows 0 in a bag of 20; 13 cannot be caught from a bag of 12')

# ------------------------------------------------------------------- 3. K-1 route
print('== 3. K-1 route ==')
check(possible_overlaps(5, 3, 3) == [1, 2, 3], 'bag of 5, 3 dotted, catch 3: every catch has at least one dot')
check(0 in possible_overlaps(6, 3, 3), 'bag of 6, 3 dotted, catch 3: the 3 undotted counters miss every dot')

print(f'{len(fails)} failures')
raise SystemExit(1 if fails else 0)
