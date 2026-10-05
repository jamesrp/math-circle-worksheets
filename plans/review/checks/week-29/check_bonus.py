"""Independent check of the Week 29 bonus companion (ordered words, the sealed
box, redundant rods) and its adult guide, by enumeration.  Diagram data come
from pdf_geometry.json (run pdf_geometry.py first).  Output saved as
check_bonus.out.
"""
import json
import os
import re
import sys
from itertools import product
from math import comb

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, PDFS, Log, gaps, multisets, reachable, words  # noqa: E402

log = Log()
geo = json.load(open(HERE / 'pdf_geometry.json'))['bonus']
guide = re.sub(r'\s+', ' ', ''.join(p.get_text() for p in pymupdf.open(PDFS['bonus-guide'])))
stud = re.sub(r'\s+', ' ', ''.join(p.get_text() for p in pymupdf.open(PDFS['bonus'])))


def says(snippet):
    ok = snippet in guide
    if not ok:
        log.check(False, f'guide text not found: {snippet!r}')
    return ok


def code(w):
    return ''.join(map(str, w))


# ---------------- P1-P2: ordered words ----------------
print('== P1-P2 ordered 3/4 words')
W = {n: sorted(code(w) for w in words([3, 4], n)) for n in (7, 10, 11, 14, 18)}
for n in W:
    log.info(f'{n}: {len(W[n])} words {W[n]}')
log.check('434' in W[11], 'launch row 4,3,4 is a word for 11')
log.check(W[7] == ['34', '43'] and W[10] == ['334', '343', '433'] and W[14] == ['3344', '3434', '3443', '4334', '4343', '4433'],
          'P1 word lists match the guide')
says('length 7 has words 34,43; length 10 has 334,343,433; length 14 has 3344,3434,3443,4334,4343,4433')
log.check(max(len(W[n]) for n in (7, 10, 14)) <= 6, 'P1 six answer slots per column suffice (largest count 6, for 14)')
g18 = '33444,34344,34434,34443,43344,43434,43443,44334,44343,44433'.split(',')
log.check(W[18] == sorted(['333333'] + g18) and len(W[18]) == 11, 'P2: 18 has 11 words: 333333 plus the ten listed; page has 12 slots')
says('eighteen has 333333 and ten words with two 3s/three 4s')
f = {}
for n in range(0, 60):
    f[n] = 1 if n == 0 else (f.get(n - 3, 0) if n >= 3 else 0) + (f.get(n - 4, 0) if n >= 4 else 0)
log.check(all(f[n] == len(words([3, 4], n)) for n in range(0, 40)), 'guide recurrence f(n)=f(n-3)+f(n-4), f(0)=1, negatives 0, matches brute force n<40')
log.check([f[n] for n in (7, 10, 14, 18)] == [2, 3, 6, 11], 'overview counts 7,10,14,18 -> 2,3,6,11')
log.check(all(sum(comb(x + y, x) for x, y in multisets([3, 4], n)) == f[n] for n in range(0, 40)), 'binomial alternative sum C(x+y,x) agrees')
log.check(all(len(words([a, b], n)) == (1 if n == 0 else len(words([a, b], n - a)) * (n >= a) + len(words([a, b], n - b)) * (n >= b))
              for a in range(1, 6) for b in range(a + 1, 7) for n in range(0, 25)), 'last-rod rule holds for any distinct a<b (a,b<=6, n<25)')
log.check([len(words([1, 2], n)) for n in range(6)] == [1, 1, 2, 3, 5, 8], 'a=1,b=2 counts 1,1,2,3,5,8 for lengths 0..5')

# ---------------- P3-P4: sealed box ----------------
print('\n== P3-P4 sealed box (four 3s, three 4s)')
box = {3: 4, 4: 3}
log.check(sorted(geo['3'][0]['lengths'] + geo['3'][1]['lengths']) == [3] * 4 + [4] * 3, 'printed used/unused rows together are the box')
subsets = [(x, y) for x in range(5) for y in range(4)]
R = sorted({3 * x + 4 * y for x, y in subsets})
gap = [n for n in range(0, 25) if n not in R]
log.info(f'box totals {R}; gaps in 0..24 {gap}')
says('Reachable lengths are 0,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24; gaps 1,2,5,19,22,23')
log.check(R == [0, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24] and gap == [1, 2, 5, 19, 22, 23], 'guide reachable/gap lists')
for n, used, unused_total in ((6, (2, 0), 18), (9, (3, 0), 15), (10, (2, 1), 14)):
    ways = [(x, y) for x, y in subsets if 3 * x + 4 * y == n]
    log.check(ways == [used] and 24 - n == unused_total, f'P3 {n}: unique stock choice {ways}, unused total {24 - n}')
for n in (19, 22):
    log.check(not [(x, y) for x, y in subsets if 3 * x + 4 * y == n] and 24 - n not in R,
              f'P3 {n}: impossible from the box; complement {24 - n} is not a box total either')
log.check(all((3 * x + 4 * y in R) == (24 - 3 * x - 4 * y in R) for x, y in subsets) and all((n in R) == (24 - n in R) for n in range(25)),
          'P4 complement symmetry n <-> 24-n')
twelve = [(x, y) for x, y in subsets if 3 * x + 4 * y == 12]
log.check(twelve == [(0, 3), (4, 0)], f'P4 equal rows: subsets of total 12 are {twelve} (all 3s vs all 4s)')
log.check(all(n in reachable([3, 4], 30) for n in (19, 22)), 'with unlimited rods 19 and 22 would be possible: the box matters')

# ---------------- P5-P6: redundant rods ----------------
print('\n== P5-P6 added rods')
base = reachable([3, 5], 300)
log.check(gaps([3, 5], 300) == [1, 2, 4, 7], '3/5 gaps 1,2,4,7')
for c, want in ((8, []), (7, [7]), (4, [4, 7])):
    new = sorted(reachable([3, 5, c], 300) - base)
    log.check(new == want, f'P5 added {c}: new targets {new}')
says('For 3/5, adding 8 adds none, 7 adds only 7, and 4 adds 4 and 7')
ok = all((reachable([a, b, c], 200) == reachable([a, b], 200)) == (c in reachable([a, b], 200))
         for a in range(2, 7) for b in range(a + 1, 9) for c in range(1, 25))
log.check(ok, 'theorem: new c adds no target iff c already reachable (a<b<=8, c<25)')


def fewest(rods, n):
    best = None
    for ms in multisets(rods, n):
        k = sum(ms)
        best = k if best is None or k < best else best
    return best


res = {(n, tuple(r)): fewest(r, n) for n in (16, 24) for r in ([3, 5], [3, 5, 8])}
log.info(f'fewest rods {res}')
log.check(res == {(16, (3, 5)): 4, (16, (3, 5, 8)): 2, (24, (3, 5)): 6, (24, (3, 5, 8)): 3}, 'P6 minima 4,2,6,3 as in guide')
log.check(multisets([3, 5], 16) == [(2, 2)] and (3, 3) in multisets([3, 5], 24), 'P6 builds 3+3+5+5 and 3+3+3+5+5+5')
log.check(all((15 + 2 * y) % 2 == 1 for y in range(6)) and 4 * 5 < 24, 'P6 guide: five 3/5 rods sum to 15+2y (odd); four rods at most 20')
log.check(3 + 5 + 8 == 16, 'finite counterexample: one 3, one 5, one 8 make 16')
log.check(not any(3 * x + 5 * y == 16 for x in range(2) for y in range(2)), 'finite stock {3,5} alone cannot make 16')

# ---------------- materials ----------------
print('\n== Kit sufficiency (ten 3s, ten 4s, six 5s, three 7s, three 8s)')
kit = {3: 10, 4: 10, 5: 6, 7: 3, 8: 3}
for rods, n in (([3, 4], 18), ([3, 5], 16), ([3, 5, 8], 16), ([3, 5], 24), ([3, 5, 8], 24)):
    best = [m for m in multisets(rods, n) if sum(m) == fewest(rods, n)]
    fits = any(all(k <= kit[r] for k, r in zip(m, rods)) for m in best)
    log.check(fits, f'{rods} target {n}: a fewest-rod build fits the kit: {best}')
log.check(all(max(m) <= 10 for m in multisets([3, 4], 18)), 'every multiset for 18 (P2) fits ten 3s/ten 4s')

log.done()
