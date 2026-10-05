"""Independent check of the Week 24 bonus companion ("Three random decks encore",
W24-BON-v1) and its adult bonus guide (W24-BON-FAC-v1).

The decks are read from the delivered student PDF's text; every guide claim is transcribed,
located in the guide text, and compared with an exhaustive computation here.
Output: out_check_bonus.txt
"""
import os
import re
import sys
from collections import Counter
from fractions import Fraction as F
from itertools import product

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))  # plans/review/checks/week-24 -> repo
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):  # still in the tmp run folder
    ROOT = HERE
    while not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
        parent = os.path.dirname(ROOT)
        if parent == ROOT:
            sys.exit('repository not found above ' + HERE)
        ROOT = parent
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-24')
stu = pymupdf.open(os.path.join(WEEK, 'week-24-bonus.pdf'))
GUIDE = re.sub(r'\s+', ' ', ''.join(p.get_text() for p in pymupdf.open(os.path.join(WEEK, 'week-24-bonus-facilitator.pdf'))))

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def in_guide(s):
    s = re.sub(r'\s+', ' ', s)
    check(s in GUIDE, f'guide text present: "{s[:90]}"')


# decks as printed at the top of pages 1 and 2
for pno in (0, 1):
    t = re.sub(r'\s+', ' ', stu[pno].get_text())
    m = re.search(r'A 2 4 9 B 1 6 8 C 3 5 7', t)
    check(bool(m), f'bonus page {pno+1} prints A=(2,4,9), B=(1,6,8), C=(3,5,7)')
A, B, C = (2, 4, 9), (1, 6, 8), (3, 5, 7)
DECK = {'A': A, 'B': B, 'C': C}

# ---------------------------------------------------------------- P1
say('\n=== P1: largest of one draw from each bag ===')
triples = list(product(A, B, C))
win = Counter()
per_card = Counter()
for t in triples:
    m = max(t)
    assert list(t).count(m) == 1
    win['ABC'[t.index(m)]] += 1
    per_card[m] += 1
say('wins by bag:', dict(win), ' wins by card:', dict(sorted(per_card.items())))
check(len(triples) == 27 and dict(win) == {'A': 10, 'B': 10, 'C': 7}, 'A 10, B 10, C 7 of 27 (A and B tie)')
check([per_card[x] for x in A] == [0, 1, 9] and [per_card[x] for x in B] == [0, 4, 6]
      and [per_card[x] for x in C] == [1, 2, 4], 'guide per-card counts 0,1,9 / 0,4,6 / 1,2,4')
in_guide("A's cards 2,4,9 win 0,1,9 triples; B's 1,6,8 win 0,4,6; C's 3,5,7 win 1,2,4.")

# ---------------------------------------------------------------- P2
say('\n=== P2: two draws with replacement, totals ===')
rows = {k: [[x + y for y in v] for x in v] for k, v in DECK.items()}
say('totals by first card:', rows)
check(rows == {'A': [[4, 6, 11], [6, 8, 13], [11, 13, 18]], 'B': [[2, 7, 9], [7, 12, 14], [9, 14, 16]],
               'C': [[6, 8, 10], [8, 10, 12], [10, 12, 14]]}, 'guide P2 rows of totals')
freq = {k: Counter(x + y for x in v for y in v) for k, v in DECK.items()}
say('frequencies:', {k: dict(sorted(f.items())) for k, f in freq.items()})
check(dict(freq['A']) == {4: 1, 6: 2, 8: 1, 11: 2, 13: 2, 18: 1} and dict(freq['B']) == {2: 1, 7: 2, 9: 2, 12: 1, 14: 2, 16: 1}
      and dict(freq['C']) == {6: 1, 8: 2, 10: 3, 12: 2, 14: 1}, 'guide total frequencies')

# ---------------------------------------------------------------- P3
say('\n=== P3: sums of two draws, 2 points for higher, 1 each for a tie ===')
def comp(X, Y):
    sx = [a + b for a in X for b in X]; sy = [a + b for a in Y for b in Y]
    w = sum(1 for a in sx for b in sy if a > b); l = sum(1 for a in sx for b in sy if a < b)
    t = sum(1 for a in sx for b in sy if a == b)
    return w, l, t, 2 * w + t, 2 * l + t
res = {k: comp(DECK[k[0]], DECK[k[1]]) for k in ('AB', 'BC', 'CA')}
say(res)
check(res['AB'] == (37, 44, 0, 74, 88), 'A/B: 37 wins, 44 losses, 0 ties; points 74 and 88 (B better)')
check(res['BC'] == (39, 38, 4, 82, 80), 'B/C: 39, 38, 4 ties; points 82 and 80 (B better)')
check(res['CA'] == (39, 38, 4, 82, 80), 'C/A: 39, 38, 4 ties; points 82 and 80 (C better)')
check(all(v[3] + v[4] == 162 for v in res.values()), 'every pairing totals 162 points over 81 outcomes')
in_guide('A/B has wins 37/44 with no ties; B/C and C/A each have wins 39/38 with four ties.')

# ---------------------------------------------------------------- P4-P5
say('\n=== P4-P5: hidden label bags ===')
def pts(X, Y):  # expected points of X against Y for one card each, separate copies
    return F(sum(2 if a > b else 1 if a == b else 0 for a in X for b in Y), len(X) * len(Y))
M = {(x, y): pts(DECK[x], DECK[y]) for x in 'ABC' for y in 'ABC'}
say({k: str(v) for k, v in M.items()})
check([M['A', y] for y in 'ABC'] == [1, F(10, 9), F(8, 9)] and [M['B', y] for y in 'ABC'] == [F(8, 9), 1, F(10, 9)]
      and [M['C', y] for y in 'ABC'] == [F(10, 9), F(8, 9), 1], 'pure rows (1,10/9,8/9), (8/9,1,10/9), (10/9,8/9,1)')
check(all(sum(1 for a in DECK[x] for b in DECK[x] if a > b) == 3 and sum(1 for a in DECK[x] for b in DECK[x] if a == b) == 3
          for x in 'ABC'), 'self-comparison: 3 wins, 3 losses, 3 ties')
# mixture formula over a grid of proportions
ok = True; best = None
N = 12
for i in range(N + 1):
    for j in range(N + 1 - i):
        a, b = F(i, N), F(j, N); c = 1 - a - b
        vals = [a * M['A', y] + b * M['B', y] + c * M['C', y] for y in 'ABC']
        if vals != [1 + (c - b) / 9, 1 + (a - c) / 9, 1 + (b - a) / 9]:
            ok = False
        if sum(vals) != 3:
            ok = False
        if all(v > 1 for v in vals):
            ok = False
        if min(vals) == 1 and not (a == b == c):
            ok = False
check(ok, 'mixture averages 1+(c-b)/9, 1+(a-c)/9, 1+(b-a)/9; they sum to 3; none beats 1 against all three; min=1 only at a=b=c (grid of 91 bags)')
check(all(min(M[x, y] for y in 'ABC') == F(8, 9) for x in 'ABC'), 'a revealed label lets the opponent hold the chooser to 8/9')
in_guide('pure A averages (1,10/9,8/9) points, B (8/9,1,10/9), C (10/9,8/9,1).')

say('\nFAILURES:', len(FAIL))
for m in FAIL:
    say('  ', m)
open(os.path.join(HERE, 'out_check_bonus.txt'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
