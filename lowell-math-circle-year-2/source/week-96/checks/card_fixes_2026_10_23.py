#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card fixes to Week 96. Standard library only.

1. Grades 2-3 Problem 3 now asks "Does the bag with more tokens make more different
   values?": the bags {2,2,2,3} and {2,3,5} make 8 values each, so the answer is no.
2. The new prime wording, "a number greater than 1 that cannot split" (into two whole
   numbers greater than 1 that multiply to it), picks out exactly the primes.
3. Grades 4-5 Problem 5's example: two 2s and one 3, and two 5s and one 2, have one pattern.
4. The guide's K-1 route: rectangles of 12 with at least two rows and two columns, and
   the sort of 2-20 into "makes a rectangle" and "only one row".
5. The problem files carry the new wording.

Run from anywhere: python3 card_fixes_2026_10_23.py
"""
from collections import Counter
from itertools import product
from math import prod
from pathlib import Path

WEEK = Path(__file__).resolve().parent.parent
fails = []


def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)


def values(bag):
    """Distinct products of sub-bags (each token used at most once; empty bag = 1)."""
    return sorted({prod(t for t, keep in zip(bag, pick) if keep) for pick in product((0, 1), repeat=len(bag))})


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


a, b = values([2, 2, 2, 3]), values([2, 3, 5])
check(a == divisors(24) and b == divisors(30) and len(a) == len(b) == 8,
      f'2-3 Problem 3: 24 makes {a}, 30 makes {b}; 8 each, so more tokens do not make more values')


def can_split(n):
    return any(n % a == 0 and n // a >= 2 for a in range(2, n))


check([n for n in range(2, 200) if not can_split(n)] == [n for n in range(2, 200) if len(divisors(n)) == 2],
      'a number greater than 1 that cannot split is exactly a prime (checked to 199)')


def pattern(bag):
    return sorted(Counter(bag).values(), reverse=True)


check(pattern([2, 2, 3]) == pattern([5, 5, 2]) == [2, 1], '4-5 Problem 5: {2,2,3} and {5,5,2} share pattern (2,1)')

rects12 = sorted((r, 12 // r) for r in range(2, 12) if 12 % r == 0 and 12 // r >= 2)
check(rects12 == [(2, 6), (3, 4), (4, 3), (6, 2)], f'K-1: 12 counters make the rectangles {rects12} (rows, per row)')
makes = [n for n in range(2, 21) if any(n % r == 0 and n // r >= 2 for r in range(2, n))]
one_row = [n for n in range(2, 21) if n not in makes]
check(makes == [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20] and one_row == [2, 3, 5, 7, 11, 13, 17, 19],
      f'K-1 sort of 2-20: rectangle {makes}; only one row {one_row} (the primes)')

files = {f.name: f.read_text() for f in (WEEK / 'problems').glob('*.md')}
check('Does the bag with more tokens make more different values?' in files['04-more-tokens.md']
      and 'Which can make more' not in files['04-more-tokens.md'], 'problem file: 2-3 Problem 3 asks the open question')
check('a number greater than 1 that cannot split' in files['00-splitting-rules.md']
      and 'Tokens with the same number are the same.' in files['00-splitting-rules.md'],
      'problem file: the new prime and same-token wording')
print(f'{len(fails)} failures')
raise SystemExit(1 if fails else 0)
