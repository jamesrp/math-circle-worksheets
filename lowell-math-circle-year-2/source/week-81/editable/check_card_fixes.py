#!/usr/bin/env python3
"""Check the claims, keys and wording changed by the October 23, 2026 card fixes (v2).

Standard library only, with its own move generator (no import from check_math.py).
Reads student/students.tex (written from the problem files by student/regenerate.py)
and guide/facilitator.tex beside this file. Bucket tuples read left to right.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
fails = []

def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok:
        fails.append(name)

def moves(state, cap):
    """Take one from bucket j, then add 0..cap to each bucket left of j."""
    for j, count in enumerate(state):
        if count:
            for adds in product(range(cap + 1), repeat=j):
                yield tuple(state[i] + adds[i] if i < j else state[i] - (i == j) for i in range(len(state)))

@lru_cache(None)
def first_wins(state, cap):
    return any(not first_wins(nxt, cap) for nxt in moves(state, cap))

@lru_cache(None)
def longest(state, cap):
    return max((1 + longest(nxt, cap) for nxt in moves(state, cap)), default=0)

# Should 1: the repair move. The corrected wording (add 1 to each earlier odd bucket,
# 0 to each earlier even one) always reaches all-even; the old "add 0 or 1 to each earlier
# odd bucket" allowed adding 0 to an odd bucket, e.g. (1, 0, 1) -> (1, 0, 0).
def repair(state):
    j = max(i for i, a in enumerate(state) if a % 2)
    return tuple(a + a % 2 if i < j else a - (i == j) for i, a in enumerate(state))
ok = True
for n in range(1, 5):
    for s in product(range(4), repeat=n):
        if any(a % 2 for a in s):
            r = repair(s)
            ok &= r in set(moves(s, 1)) and all(a % 2 == 0 for a in r) and not first_wins(r, 1)
check('guide repair: rightmost odd bucket, +1 to each earlier odd one, reaches all-even (all 1-4 bucket starts 0-3)', ok)
check('the old wording\'s "add 0" to an odd bucket fails: (1, 0, 1) -> (1, 0, 0) is not all-even',
      (1, 0, 0) in set(moves((1, 0, 1), 1)) and (1, 0, 0)[0] % 2 == 1)

# Should 2: P5's two-bucket start (0, 3). Bucket 2 never refills, so every play removes from it
# exactly three times; between those, only bucket 1 can lose counters. Checked for refill caps
# K <= 6 by tracking every reachable state's possible numbers of bucket-2 removals.
@lru_cache(None)
def right_takes(state, cap):
    if not any(state):
        return frozenset([0])
    out = set()
    for nxt in moves(state, cap):
        took_right = nxt[1] == state[1] - 1
        out |= {t + took_right for t in right_takes(nxt, cap)}
    return frozenset(out)
check('P5 (0, 3): every play takes from bucket 2 exactly 3 times, for refill caps 1-6',
      all(right_takes((0, 3), k) == {3} for k in range(1, 7)))
check('P5 (0, 3): the longest capped play is 3(K + 1) moves, finite for each cap K <= 6',
      all(longest((0, 3), k) == 3 * (k + 1) for k in range(1, 7)))
check('P5 (0, 3) and (1, 1, 1) are first-player wins under any cap 1-4 (an odd bucket)',
      all(first_wins((0, 3), k) and first_wins((1, 1, 1), k) for k in range(1, 5)))

# Could 11: with cap K the longest game is a1 + a2 (K+1) + a3 (K+1)^2 + ...
check('return visit: longest game = sum a_i (K+1)^(i-1), K = 1-3, up to 3 buckets of 0-2',
      all(longest(s, k) == sum(a * (k + 1) ** i for i, a in enumerate(s))
          for k in range(1, 4) for n in range(1, 4) for s in product(range(3), repeat=n)))
check('return visit: 7 moves from (1, 1, 1) with a cap of one', longest((1, 1, 1), 1) == 7)

# Should 4: K-1 route on the nine cards (0..2, 0..2), cap one.
nine = [(a, b) for b in range(3) for a in range(3)]
second = [s for s in nine if not first_wins(s, 1)]
check('K-1 key: the second player wins exactly on (0,0), (0,2), (2,0), (2,2); the other five are first-player',
      second == [(0, 0), (2, 0), (0, 2), (2, 2)] and len(nine) - len(second) == 5)

# Student pages.
tex = (HERE / 'student' / 'students.tex').read_text()
three = [tuple(map(int, m)) for m in re.findall(r'\\smallstart\{(\d+)\}\{(\d+)\}\{(\d+)\}', tex)]
p1, p3 = three[:4], three[4:10]
check('P3 starts are (2,0,2), (1,2,2), (2,1,2), (2,2,1), (0,2,0), (3,3,1) and repeat no P1 start',
      p3 == [(2, 0, 2), (1, 2, 2), (2, 1, 2), (2, 2, 1), (0, 2, 0), (3, 3, 1)] and not set(p1) & set(p3))
check('P3 key: (2,0,2) and (0,2,0) are the second-player wins', [s for s in p3 if not first_wins(s, 1)] == [(2, 0, 2), (0, 2, 0)])
check('P5 pictures: (0, 3) drawn in the P1-P3 style beside (1, 1, 1) (critic follow-up; it had been drawn like P4)',
      tex.count(r'\foreach \x/\count in {0/0,1.3/3}') == 1 and three[10:] == [(1, 1, 1)]
      and tex.index(r'\problem{5}') < tex.index(r'\foreach \x/\count in {0/0,1.3/3}')
      and r'\dotsbucket' not in tex[tex.index(r'\problem{5}'):])
check('P5 says "Start from each picture." and no longer presumes the answer',
      'Start from each picture.' in tex and 'however big the refills, explain why.' in tex
      and 'cannot prevent it' not in tex)
check('p. 1 names the left side one way', 'to each bucket to the left of the one you took from' in tex
      and 'each earlier bucket' not in tex)
footer = re.search(r'\\fancyfoot\[L\]\{[^\n]*', tex).group(0)
check('footer W81-S-v3, no "draft"', footer.endswith('/ W81-S-v3}') and 'draft' not in footer)
check('five problems, four page breaks', re.findall(r'\\problem\{(\d+)\}', tex) == ['1', '2', '3', '4', '5']
      and tex.count(r'\newpage') == 4)

# Critic follow-up, October 23, 2026: the K-1 rule as read aloud. "Take one. If you took it
# from bucket 2, you may put one in bucket 1." on buckets 1 and 2 is exactly the cap-1 move on
# two buckets; the earlier wording "Take one. You may put one in bucket 1." also let a child take
# from bucket 1 and put it back, a move that changes nothing, so a game need not end.
def k1_moves(state):
    a, b = state
    out = set()
    if a:
        out.add((a - 1, b))                 # from bucket 1: nothing may be put back
    if b:
        out |= {(a, b - 1), (a + 1, b - 1)}  # from bucket 2: you may put one in bucket 1
    return out
@lru_cache(None)
def k1_first_wins(state):
    return any(not k1_first_wins(nxt) for nxt in k1_moves(state))
cards = [(a, b) for a in range(3) for b in range(3)]
check('K-1 rule as read equals the cap-1 move on two buckets', all(k1_moves(s) == set(moves(s, 1)) for s in cards))
check('K-1 key: the four even-even cards are second-player wins, the other five first-player wins',
      [s for s in cards if not k1_first_wins(s)] == [(0, 0), (0, 2), (2, 0), (2, 2)]
      and sum(k1_first_wins(s) for s in cards) == 5)
check('the old wording allowed a do-nothing move: take from bucket 1, put it back, e.g. (1, 0) -> (1, 0)',
      (1, 0) not in k1_moves((1, 0)))

# Adult guide.
flat = ' '.join((HERE / 'guide' / 'facilitator.tex').read_text().split())
for phrase in [r'\rhead{Adult guide}', 'add 1 to each earlier odd bucket (0 to each earlier even one)',
               'Grades 4--5 learn the move on Problem 1 and some Problem 2 cards',
               'ten minutes of Problem 1 and some Problem 2 cards', 'Problem 3 for a pair that finishes',
               'adding at most one counter to the bucket on its left', 'K--1, adult-led, after the launch',
               "``Take one. If you took it from bucket 2, you may put one in bucket 1.''", 'the other five cards',
               'Week 81 / W81-FAC-v2',
               'Problem 3: $(2,0,2)$ and $(0,2,0)$ are second-player wins', 'from $(0,3)$, the second bucket never refills',
               'which is 7 from $(1,1,1)$ with a cap of one']:
    check(f'guide says "{phrase}"', phrase in flat)
for phrase in ['Facilitator draft', 'add 0 or 1', 'count card', 'quantity card', 'Cards can stand',
               'termination/unbounded length, then parity', '$(2,2,2)$ and $(0,2,0)$']:
    check(f'guide no longer says "{phrase}"', phrase not in flat)

print(f'{len(fails)} failures')
sys.exit(1 if fails else 0)
