#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card fixes to Week 87 (plans/review/week-87.md).

Standard library only. Card votes: each voter chooses the higher of the two offered
letters on an unchanged ranking card. Line votes: each voter chooses the nearer of two
locations; equal distances go to Tie; "beats" means strictly more votes.

1. Guide p. 3, shared Problem 3: of the 20 sets of three different cards, exactly two
   make the waiting letter matter, ABC/BCA/CAB and ACB/CBA/BAC; each card agrees with at
   most two of a cycle's three winning pairs; repeated cards never give a cycle except by
   using one of those sets; three different cards cannot share a first choice.
2. Line Problem 2's third set, now numbered out of left-to-right order (V1..V5 at
   9, 1, 10, 6, 0): 6 is the only location that beats every other, on the ticks and on a
   tenth-step grid, and it is V4's favorite, not V3's.
3. Line Problem 3's new question presupposes a winner: every one of the 3,003 ways to put
   five favorites on the ticks has exactly one tick that beats every other tick, the third
   favorite from the left, and it also beats every half-step location.
4. Upper Problem 1 ("for each set of cards"): in the first set A wins every knockout; in
   the second each waiting letter wins.
5. Guide p. 1, K-1 route key: A beats B, B beats C, C beats A, each 2 to 1; B/C first
   makes A win, C/A first makes B win, A/B first makes C win.
"""
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations, product

FAILS = []


def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def vote(cards, a, b):
    na = sum(c.index(a) < c.index(b) for c in cards)
    return a if 2 * na > len(cards) else b


def knockout(cards, waiting):
    first = [x for x in 'ABC' if x != waiting]
    return vote(cards, vote(cards, *first), waiting)


def winners_by_waiting(cards):
    return {w: knockout(cards, w) for w in 'ABC'}


RANKS = [''.join(p) for p in permutations('ABC')]
ROT, MIRROR = {'ABC', 'BCA', 'CAB'}, {'ACB', 'CBA', 'BAC'}

# 1. Shared Problem 3
dependent = [set(s) for s in combinations(RANKS, 3) if len(set(winners_by_waiting(s).values())) > 1]
check(len(list(combinations(RANKS, 3))) == 20 and sorted(map(sorted, dependent)) == sorted([sorted(ROT), sorted(MIRROR)]),
      f'P3: of 20 three-different-card sets exactly ABC/BCA/CAB and ACB/CBA/BAC make the waiting letter matter ({len(dependent)})')
for cyc in (['AB', 'BC', 'CA'], ['AC', 'CB', 'BA']):
    agree = {r: sum(r.index(x) < r.index(y) for x, y in cyc) for r in RANKS}
    check(max(agree.values()) == 2 and {r for r, n in agree.items() if n == 2} == (ROT if cyc[0] == 'AB' else MIRROR),
          f'P3: each card agrees with at most two of the cycle {"/".join(x + ">" + y for x, y in cyc)}; exactly the set\'s three cards agree with two')
cyclic = [p for p in product(RANKS, repeat=3) if len(set(winners_by_waiting(p).values())) > 1]
check(all(set(p) in (ROT, MIRROR) for p in cyclic) and len(cyclic) == 12,
      f'P3: all {len(cyclic)} three-voter profiles with repeats allowed that make the waiting letter matter use one of the two sets, in some order')
check(all(sum(r[0] == x for r in RANKS) == 2 for x in 'ABC'), 'guide: only two rankings start with each letter, so three different cards cannot share a first choice')


# 2-3. Line votes
def tally(favs, a, b):
    va = sum(abs(f - a) < abs(f - b) for f in favs)
    vb = sum(abs(f - b) < abs(f - a) for f in favs)
    return va, vb


def strict_winners(favs, places):
    return [a for a in places if all(tally(favs, a, b)[0] > tally(favs, a, b)[1] for b in places if b != a)]


TICKS = list(range(11))
FINE = [Fraction(k, 10) for k in range(-20, 121)]
set3 = [9, 1, 10, 6, 0]
check(strict_winners(set3, TICKS) == [6] and strict_winners(set3, FINE) == [6],
      'line P2 third set (V1..V5 at 9, 1, 10, 6, 0): 6 is the only winner on the ticks and on a tenth-step grid from -2 to 12')
check(set3.index(6) + 1 == 4 and set3[2] != 6, 'line P2 third set: the winner is V4\'s favorite; V3 is at 10')
for favs, m in [([0, 2, 4, 7, 10], 4), ([0, 0, 0, 8, 10], 0), ([1, 4, 4, 4, 9], 4), ([9, 1, 10, 6, 0], 6)]:
    check(strict_winners(favs, TICKS) == [m], f'line favorites {favs}: winner {m} (guide)')
HALF = [Fraction(k, 2) for k in range(0, 21)]
n = bad = 0
for favs in combinations_with_replacement(TICKS, 5):
    n += 1
    med = sorted(favs)[2]
    if strict_winners(favs, TICKS) != [med] or not all(tally(favs, med, q)[0] > tally(favs, med, q)[1] for q in HALF if q != med):
        bad += 1
check(n == 3003 and bad == 0, f'line P3: each of the {n} five-favorite sets has one winner, the third favorite, against ticks and half-steps ({bad} exceptions)')

# 4. Upper Problem 1
check(set(winners_by_waiting(['ABC', 'ACB', 'BAC']).values()) == {'A'}, 'upper P1 first set: A wins every knockout, so the waiting letter cannot change the winner')
check(winners_by_waiting(['ACB', 'CBA', 'BAC']) == {'A': 'A', 'B': 'B', 'C': 'C'}, 'upper P1 second set: the waiting letter always wins')

# 5. K-1 route key
cards = ['ABC', 'BCA', 'CAB']
check([vote(cards, a, b) for a, b in ['AB', 'BC', 'CA']] == list('ABC')
      and all(sum(c.index(a) < c.index(b) for c in cards) == 2 for a, b in ['AB', 'BC', 'CA']),
      'K-1 key: A beats B, B beats C, C beats A, each two tokens to one')
check(winners_by_waiting(cards) == {'A': 'A', 'B': 'B', 'C': 'C'}, 'K-1 key: whichever letter waits wins (B/C first -> A, C/A first -> B, A/B first -> C)')

print('PASS: all Week 87 card-fix checks' if not FAILS else f'FAIL: {len(FAILS)} checks failed')
raise SystemExit(1 if FAILS else 0)
