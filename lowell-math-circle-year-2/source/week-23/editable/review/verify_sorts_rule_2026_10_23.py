#!/usr/bin/env python3
"""Check the Critic L fix of October 23, 2026: the K-1 rule asks for the whole order again.

    python3 review/verify_sorts_rule_2026_10_23.py [build-folder] [views-folder]

The card's rule "The machine sorts when the fewest dots finish at the top." asks only for the
smallest card on top. This script shows, by exhaustive search, that under that reading three K-1
keys change (Problem 2: 2 bars, Problem 6: 3 bars, Problem 4's second half has no machine), and
that under the restored rule ("the cards finish in order: fewest dots at the top, most dots at the
bottom") every K-1 key in the guide holds. It then checks the printed K-1 rule and footers, the
guide's packet names, footer and overview wording, and the K-1 Problem 5 key line in the problem
file (and in the key view, if a views folder from problem-files/tools/build.py is given).
The build folder (default build/) holds build.sh's PDFs. Needs PyMuPDF.
"""
import sys
from itertools import permutations, product
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
build = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build'
views = Path(sys.argv[2]) if len(sys.argv) > 2 else None
for problems in (ROOT / 'problem-files' / 'problems', ROOT.parent / 'problems'):
    if problems.is_dir():
        break
else:
    sys.exit('Cannot find the Week 23 problem files')

checks = 0
def ok(cond, what):
    global checks
    assert cond, what
    checks += 1


def text(pdf):
    flat = lambda t: ' '.join(t.replace('–', '-').split())
    return [flat(p.get_text()) for p in fitz.open(pdf)]


# ------------------------------------------------------------ the two readings of "sorts"
def run(bars, start):
    v = list(start)
    for i, j in bars:
        if v[i - 1] > v[j - 1]:
            v[i - 1], v[j - 1] = v[j - 1], v[i - 1]
    return v

FULL = lambda v: all(v[k] <= v[k + 1] for k in range(len(v) - 1))   # the restored rule
WEAK = lambda v: v[0] == min(v)                                       # "the fewest dots finish at the top"

def sorts(bars, cards, good):
    return all(good(run(bars, s)) for s in set(permutations(cards)))

def pairs(n):
    return [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]

def fewest(n, good, limit):
    for k in range(limit + 1):
        if any(sorts(m, range(1, n + 1), good) for m in product(pairs(n), repeat=k)):
            return k
    return None

def separate(a, b, good, limit=3):
    """Some machine of up to `limit` bars always sorts set a but sometimes fails set b."""
    return any(sorts(m, a, good) and not sorts(m, b, good)
               for k in range(1, limit + 1) for m in product(pairs(3), repeat=k))

T, R = [(1, 2), (2, 3)], [(2, 3), (1, 2)]
LEFT, RIGHT = [0, 0, 1], [0, 1, 1]
ORD3 = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# The guide's K-1 keys, under the restored rule.
ok([s for s in ORD3 if FULL(run(T, s))] == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (3, 1, 2)], 'P1: T sorts four starts, fails 231 and 321')
ok(fewest(3, FULL, 4) == 3, 'P2: three bars, no two-bar machine')
ok([s for s in ORD3 if not FULL(run([(1, 2), (2, 3), (1, 2)], s))] == [], 'P3 upper machine fails nothing')
ok([s for s in ORD3 if not FULL(run([(1, 2), (1, 2), (2, 3)], s))] == [(2, 3, 1), (3, 2, 1)], 'P3 lower machine fails 231, 321')
ok(sorts(T, LEFT, FULL) and not sorts(T, RIGHT, FULL) and run(T, (1, 1, 0)) == [1, 0, 1], 'P4: T sorts the left set, 110 -> 101')
ok(sorts(R, RIGHT, FULL) and not sorts(R, LEFT, FULL) and run(R, (1, 0, 0)) == [0, 1, 0], 'P4: R sorts the right set, 100 -> 010')
ok([[b for b in pairs(3) if sorts(m + [b], (1, 2, 3), FULL)] for m in (T, R, [(1, 3), (1, 2)])] == [[(1, 2)], [(2, 3)], [(2, 3)]],
   'P5: the unique last bars are (1,2), (2,3) and (2,3)')
ok(fewest(4, FULL, 5) == 5 and sorts([(1, 2), (3, 4), (1, 3), (2, 4), (2, 3)], (1, 2, 3, 4), FULL), 'P6: five bars, S4 sorts')

# The same problems under the card's sentence read literally: three keys change.
ok(fewest(3, WEAK, 4) == 2 and sorts([(2, 3), (1, 2)], (1, 2, 3), WEAK), 'weak reading: P2 needs only 2 bars, e.g. (2,3),(1,2)')
ok(fewest(4, WEAK, 5) == 3 and sorts([(1, 2), (1, 3), (1, 4)], (1, 2, 3, 4), WEAK), 'weak reading: P6 needs only 3 bars')
ok(separate(LEFT, RIGHT, WEAK) and not separate(RIGHT, LEFT, WEAK), 'weak reading: P4 second half impossible')
ok(sorts(R, LEFT, WEAK), "weak reading: the guide's R 'fails' 100 only by finishing 010, blank on top")

# ------------------------------------------------------------ the printed pages
k1 = text(build / 'k-1.pdf')
ok('The machine sorts when the cards finish in order: fewest dots at the top, most dots at the bottom.' in k1[0], 'K-1 p. 1 rule')
ok('fewest dots finish at the top' not in ' '.join(k1), 'old rule gone')
ok(len(k1) == 6 and all('Bellingham Math Circle / Week 23 / F23-K-v4' in t for t in k1), 'K-1 footers v4')
for band, tag, n in (('grades-2-3', '23', 6), ('grades-4-5', '45', 7)):
    t = text(build / f'{band}.pdf')
    ok(len(t) == n and all(f'Bellingham Math Circle / Week 23 / F23-{tag}-v3' in x for x in t), band + ' unchanged at v3')
g = text(build / 'facilitator-guide.pdf')
ok(len(g) == 13, 'guide keeps 13 pages')
ok('F23-K-v4, F23-23-v3 and F23-45-v3 student packets' in g[1], 'guide names the K-1 v4 packet')
ok(all('2026-10-03, revised 2026-10-23 for F23-K-v4' in t for t in g[1:]), 'numbered guide pages carry the new footer')
ok('with the minimum in the upper lane (the lane 1 side).' in g[0] and 'lower-numbered' not in ' '.join(g), 'overview says upper lane')

# ------------------------------------------------------------ the K-1 Problem 5 key line
p5 = (problems / '05-k1-one-more-bar.md').read_text()
ok('(1,2), (2,3) and (2,3) respectively' in p5 and '(1,3) respectively' not in p5, 'P5 kernel names (2,3) for the bottom machine')
if views:
    key = ' '.join(text(views / 'guide-keys.pdf'))
    ok('(1,2), (2,3) and (2,3) respectively' in key, 'key view P5 line')
    ok(all('F23-K-v4' in t for t in text(views / 'k-1.pdf')), 'problem-file K-1 packet v4')

print(f'PASS: {checks} checks of the October 23 sorts-rule fix' + (' (with the views)' if views else ''))
