#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card fixes to Week 54 (plans/review/week-54.md).

Standard library only. A collection is a partition, written largest first. A join
replaces two equal strips q, q by 2q; a split replaces an even strip 2q by q, q.

1. K-1 route key (guide p. 2): 4 cubes make exactly the five collections listed, 5
   cubes seven; nine 1s end as (8, 1) whatever the order of joins; (5, 3, 1) has no
   join; 6 cubes give exactly four only-odd collections; every case fits a 12-cube kit;
   the kits total 3 x 24 + 12 + 2 x 12 = 108 cubes.
2. Problem 3's worked visual (fix 3): (3, 3, 1, 1, 1, 1) has two kinds of legal first
   join, 3 + 3 and 1 + 1, and every route ends at (6, 4).
3. Problem 2 (fix 4): no all-different collection of 7 has largest size 3 or less,
   since 3 + 2 + 1 = 6; for 6 the only one with largest size 3 is (3, 2, 1).
4. Problem 4's contrast (guide p. 5): (6, 6, 1) splits to (3, 3, 3, 3, 1) and rejoins
   as (12, 1), not (6, 6, 1); every printed P4 input returns.
5. Problem 7's new grids (fix 7): each result of exchanging rows and columns once or
   twice fits a 5 x 5 grid; the grid cells and the input squares are both 0.22 in.
6. Kit size (fix 2): the longest strip printed or made on any legal route in the
   printed cases is 12 units, 24 cm with 2 cm cubes.
7. The reworded Problems 6 and 9 still have the guide's answers: every only-odd
   collection up to 20 has one final collection whatever the joins (Problem 6's input
   ends at (12, 4, 2)), and only-odd and all-different counts agree up to 30.
"""
from functools import lru_cache

FAILS = []


def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def partitions(n, most=None):
    most = n if most is None else most
    if n == 0:
        yield ()
        return
    for k in range(min(n, most), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def norm(c):
    return tuple(sorted(c, reverse=True))


def joins(c):
    out = set()
    for q in set(c):
        if c.count(q) >= 2:
            d = list(c)
            d.remove(q), d.remove(q)
            out.add(norm(d + [2 * q]))
    return out


@lru_cache(maxsize=None)
def finals(c):
    """Every collection a sequence of joins can stop at (no join left)."""
    nxt = joins(c)
    if not nxt:
        return frozenset([c])
    return frozenset().union(*(finals(d) for d in nxt))


@lru_cache(maxsize=None)
def longest(c):
    nxt = joins(c)
    return max([max(c)] + [longest(d) for d in nxt])


def split_all(c):
    out = []
    for q in c:
        k = 1
        while q % 2 == 0:
            q //= 2
            k *= 2
        out += [q] * k
    return norm(out)


def join_all(c):
    (f,) = finals(norm(c))
    return f


def conj(c):
    return tuple(sum(1 for r in c if r > j) for j in range(c[0])) if c else ()


# 1. K-1 route key
check(list(partitions(4)) == [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)], 'K-1: 4 cubes make five collections: 4; 3 and 1; 2 and 2; 2, 1 and 1; four 1s')
check(len(list(partitions(5))) == 7, 'K-1: 5 cubes make seven collections')
check(finals((1,) * 9) == {(8, 1)}, 'K-1: nine 1s end as an 8 and a 1 whatever the order of joins')
check(joins((5, 3, 1)) == set(), 'K-1: (5, 3, 1) has no join, so nothing happens')
odd6 = [p for p in partitions(6) if all(x % 2 for x in p)]
check(odd6 == [(5, 1), (3, 3), (3, 1, 1, 1), (1,) * 6], 'K-1: 6 cubes give four only-odd collections: 5 and 1; 3 and 3; 3, 1, 1 and 1; six 1s')
check(max(4, 5, 9, 9, 6) <= 12 and 3 * 24 + 12 + 2 * 12 == 108, 'K-1: every case uses at most 9 cubes of a 12-cube kit; kits total 108 cubes')

# 2. Problem 3's worked visual
start = (3, 3, 1, 1, 1, 1)
check(joins(start) == {(6, 1, 1, 1, 1), (3, 3, 2, 1, 1)} and finals(start) == {(6, 4)},
      'P3 visual: 3 + 3 and 1 + 1 are both legal first joins; every route ends at (6, 4)')

# 3. Problem 2
dist = lambda n: [p for p in partitions(n) if len(set(p)) == len(p)]
check(not [p for p in dist(7) if p[0] <= 3] and 3 + 2 + 1 == 6, 'P2: no all-different collection of 7 has largest size 3 or less (3 + 2 + 1 = 6)')
check([p for p in dist(6) if p[0] == 3] == [(3, 2, 1)], 'P2: for 6 the only all-different collection with largest size 3 is (3, 2, 1)')

# 4. Problem 4
check(split_all((6, 6, 1)) == (3, 3, 3, 3, 1) and join_all(split_all((6, 6, 1))) == (12, 1),
      'P4 contrast: (6, 6, 1) splits to four 3s and a 1 and rejoins as (12, 1)')
check(all(join_all(split_all(c)) == c for c in [(10, 7, 4, 2, 1), (12, 6, 3), (7, 3, 1)]), 'P4: every printed input returns')

# 5. Problem 7's grids
fits = all(len(r) <= 5 and r[0] <= 5 for c in [(5, 2, 1), (4, 4), (3, 3, 1, 1)] for r in (conj(c), conj(conj(c))))
check(fits and all(conj(conj(c)) == c for c in [(5, 2, 1), (4, 4), (3, 3, 1, 1)]),
      'P7: every once and twice result fits 5 rows by 5 columns, and twice returns each input')
check(abs(5 * 0.22 - 1.1) < 1e-9 and round(0.22 * 25.4, 2) == 5.59, 'P7: 5 cells of 0.22 in (5.59 mm, the input squares) make the 1.1 in grid')

# 6. Kit size
printed = [(1,) * 9, (5, 5, 3, 3, 3, 1, 1), (5, 3, 1), (3, 3, 3, 3) + (1,) * 6] + [split_all(c) for c in [(10, 7, 4, 2, 1), (12, 6, 3), (7, 3, 1)]]
check(max(longest(norm(c)) for c in printed) == 12 and 12 * 2 == 24, 'kit: the longest strip on any legal route is 12 units, 24 cm with 2 cm cubes')

# 7. Problems 6 and 9
check(finals((3, 3, 3, 3) + (1,) * 6) == {(12, 4, 2)}, 'P6: four 3s and six 1s end at (12, 4, 2) on every route')
check(all(len(finals(p)) == 1 for n in range(1, 21) for p in partitions(n) if all(x % 2 for x in p)),
      'P6: every only-odd collection up to 20 has one final collection')
check(all(len([p for p in partitions(n) if all(x % 2 for x in p)]) == len(dist(n)) for n in range(31)), 'P9: only-odd and all-different counts agree for every total up to 30')

print('PASS: all Week 54 card-fix checks' if not FAILS else f'FAIL: {len(FAILS)} checks failed')
raise SystemExit(1 if FAILS else 0)
