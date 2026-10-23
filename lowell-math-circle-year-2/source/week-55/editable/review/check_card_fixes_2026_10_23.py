#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card fixes to Week 55 (plans/review/week-55.md).

Standard library only. A trial's totals are the different values a + b, a in A, b in B.

1. The rule (fix 2): with "no number repeats within an input; A and B may share numbers",
   Problem 5 has seven answers; the misreading "A and B share no number" would leave four.
2. K-1 route key (guide p. 2): Problem 1 gives 1, 3, 5 and 1, 3, 4, 6; Problem 2 gives
   five, six and nine places; with cards 0-5 three cards each make at least five totals,
   for example {0,1,2}+{0,1,2} and {1,3,5}+{0,2,4}, and every total is at most 10; every
   K-1 card is at most 6; the kits are 2 pairs x 2 decks x 7 = 28 dot cards and 40
   counters, more than any trial needs.
3. Problem 3's spoken four-card variant (guide p. 4): within 0-9, four cards each make at
   least 7 totals, and 16 only with {0,1,8,9} and four cards of gap 2.
4. Problem 6's spoken follow-up (guide p. 5): {0,2,4}+{0,3,6} gives 9 = 3 x 3 totals.
5. Problem 10, reordered (fix 6): for all inputs from 0-12 with at least two cards each and
   at most four, exactly m+n-1 totals happens if and only if both are runs with one gap.
6. Print set (fix 7): 5 x 3 + 2 x 2 + 7 = 26 landscape sheets.
"""
from itertools import combinations

FAILS = []


def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def totals(a, b):
    return sorted({x + y for x in a for y in b})


def run(s):
    return len({s[i + 1] - s[i] for i in range(len(s) - 1)}) == 1


A5 = (0, 3, 6)
fours = [b for b in combinations(range(10), 2) if len(totals(A5, b)) == 4]
check(len(fours) == 7, f'P5: seven two-card B give four totals with A = 0, 3, 6: {fours}')
check(len([b for b in fours if not set(b) & set(A5)]) == 4, 'P5: the misreading "A and B share no number" would leave four')

check(totals((0, 2), (1, 3)) == [1, 3, 5] and totals((0, 2), (1, 4)) == [1, 3, 4, 6], 'K-1 P1: 1, 3, 5 (three places) and 1, 3, 4, 6 (four)')
p2 = [totals((0, 1, 2), (0, 1, 2)), totals((0, 1, 3), (0, 1, 3)), totals((0, 1, 2), (0, 3, 6))]
check(p2 == [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 6], list(range(9))], 'K-1 P2: five, six and nine places')
T5 = list(combinations(range(6), 3))
check(min(len(totals(a, b)) for a in T5 for b in T5) == 5 and len(totals((0, 1, 2), (0, 1, 2))) == 5 and len(totals((1, 3, 5), (0, 2, 4))) == 5
      and max(max(totals(a, b)) for a in T5 for b in T5) == 10, 'K-1 P3: with cards 0-5 the fewest is 5 (e.g. 0,1,2 + 0,1,2); totals stay at 10 or less')
cards = [0, 1, 2, 3, 4] + [0, 1, 2, 3, 6] + list(range(6))
check(max(cards) <= 6 and 2 * 2 * 7 == 28 and max(len(t) for t in p2) <= 20, 'K-1 kit: every card is 0-6; 28 dot cards; 20 counters per pair cover every trial')

F = list(combinations(range(10), 4))
check(min(len(totals(a, b)) for a in F for b in F) == 7, 'P3 variant: four cards each make at least 7 totals')
best = [(a, b) for a in F for b in F if len(totals(a, b)) == 16]
check(best and all((0, 1, 8, 9) in (a, b) and run(b if a == (0, 1, 8, 9) else a) and (b if a == (0, 1, 8, 9) else a)[1] - (b if a == (0, 1, 8, 9) else a)[0] == 2 for a, b in best),
      f'P3 variant: 16 totals only with 0, 1, 8, 9 and four cards of gap 2 ({len(best)} ordered pairs)')

check(len(totals((0, 2, 4), (0, 3, 6))) == 9, 'P6 follow-up: 0, 2, 4 + 0, 3, 6, both equally spaced, give 9 totals')

ok = True
for m in range(2, 5):
    for n in range(2, 5):
        for a in combinations(range(13), m):
            for b in combinations(range(13), n):
                eq = len(totals(a, b)) == m + n - 1
                same_gap = run(a) and run(b) and a[1] - a[0] == b[1] - b[0]
                ok &= eq == same_gap
check(ok, 'P10: for 2-4 cards each from 0-12, exactly m+n-1 totals iff both are runs with the same gap')

check(5 * 3 + 2 * 2 + 7 == 26, 'print set: 26 landscape sheets')

print('PASS: all Week 55 card-fix checks' if not FAILS else f'FAIL: {len(FAILS)} checks failed')
raise SystemExit(1 if FAILS else 0)
