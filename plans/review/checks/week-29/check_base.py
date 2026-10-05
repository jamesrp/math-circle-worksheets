"""Independent check of the Week 29 base packet (K-1, 2-3, 4-5) and its adult
guide by enumeration.  Every answer is recomputed here; the guide's claims are
located in the delivered guide PDF text and compared.  Diagram data (target
boxes, strips) come from pdf_geometry.json (run pdf_geometry.py first).
Output saved as check_base.out.
"""
import json
import os
import re
import sys
from itertools import combinations
from math import gcd

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, PDFS, Log, gaps, multisets, reachable  # noqa: E402

log = Log()
geo = json.load(open(HERE / 'pdf_geometry.json'))['base']
guide = re.sub(r'\s+', ' ', ''.join(p.get_text() for p in pymupdf.open(PDFS['guide'])))
student = {b: [re.sub(r'\s+', ' ', p.get_text()) for p in pymupdf.open(PDFS[b])] for b in ('k-1', 'grades-2-3', 'grades-4-5')}
BIG = 400


def says(snippet):
    ok = snippet in guide
    if not ok:
        log.check(False, f'guide text not found: {snippet!r}')
    return ok


def last_gap(rods):
    g = gaps(rods, BIG)
    return g[-1] if g else None


def infinite_gaps(rods):
    # with gcd > 1 all non-multiples fail; with gcd 1 gaps stop below a*b
    return len([n for n in gaps(rods, BIG) if n > BIG // 2]) > 0


def page_targets(band, page):
    return [int(t[0]) for t in geo[band][page - 1]['targets'] if t]


def page_strips(band, page):
    return [s['n'] for s in geo[band][page - 1]['strips']]


# ---------------- guide arithmetic: every "n=a+b+..." or "n=a×k" ----------------
print('== Guide decompositions')
for m in re.finditer(r'(?<![\d,.])(\d+)\s*=\s*(\d+(?:\s*[+×]\s*\d+)+)', guide):
    lhs, rhs = int(m.group(1)), m.group(2).replace(' ', '')
    val = eval(rhs.replace('×', '*'))
    log.check(val == lhs, f'guide "{m.group(0)}" evaluates to {val}')

# ---------------- K-1 ----------------
print('\n== K-1')
R34 = reachable([3, 4], BIG)
s = page_strips('k-1', 1)
ok = [n for n in s if n in R34]
bad = [n for n in s if n not in R34]
log.check(ok == [6, 8, 9, 10] and bad == [1, 2, 5], f'K P1 strips {s}: buildable {ok}, impossible {bad} (3, 4, 7 shown in the launch)')
says('6=3+3, 8=4+4, 9=3+3+3, 10=3+3+4 work. The targets 1, 2, 5 do not')
log.check(not any(5 - 3 * k in (0, 4) for k in range(2)) and min(3 + 3, 3 + 4, 4 + 4) == 6,
          'K P1 guide reason for 5: one rod too short, any two rods total at least 6')

for n in (12, 15):
    ways = multisets([3, 4], n)
    log.info(f'K P2 {n}: (3s,4s) = {ways}')
log.check(multisets([3, 4], 12) == [(0, 3), (4, 0)] and multisets([3, 4], 15) == [(1, 3), (5, 0)],
          'K P2: 12 has 2 ways, 15 has 2 ways; page prints exactly two strips each ' + str(page_strips('k-1', 2)))
says('For 12: four 3-rods or three 4-rods. For 15: five 3-rods, or one 3-rod and three 4-rods')

R35 = reachable([3, 5], BIG)
s = page_strips('k-1', 3)
log.check([n for n in s if n not in R35] == [4, 7], f'K P3 strips {s}: impossible {[n for n in s if n not in R35]}')
log.info(f'K P3: 1, 2 also impossible and 6 = 3+3 possible but none of 1, 2, 6 has a strip')
says('With 3 and 5, 4 and 7 are impossible')
says('8=3+5, 9=3+3+3, 10=5+5, 11=3+3+5, 12=3+3+3+3')
log.check([7 - 5 * k for k in range(2)] == [7, 2] and all((7 - 5 * k) % 3 for k in range(2)), 'K P3 7: zero/one 5-rod leaves 7, 2; neither a multiple of 3')

t = page_targets('k-1', 4)
log.check(t == list(range(6, 19)) and all(n in R34 for n in t), 'K P4 every target 6..18 buildable with 3/4')
log.check(all(any(n - 3 * k in (6, 7, 8) for k in range(n)) for n in range(6, BIG)), 'K P4 chains 6,7,8 + 3s cover every n >= 6 (checked to 400)')

R24 = reachable([2, 4], BIG)
t = page_targets('k-1', 5)
log.check([n for n in t if n in R24] == [2, 4, 6, 8, 10, 12], 'K P5 2/4 builds exactly the even targets 2..12')

print('\n-- K P6 all pairs from {2,3,4,5}, targets 6..12')
t = page_targets('k-1', 6)
good = []
for a, b in combinations([2, 3, 4, 5], 2):
    R = reachable([a, b], 20)
    miss = [n for n in t if n not in R]
    log.info(f'{{{a},{b}}}: misses {miss}')
    if not miss:
        good.append((a, b))
log.check(good == [(2, 3), (2, 5), (3, 4)], f'K P6 pairs that cover 6..12: {good}')
says('Exactly {2,3}, {2,5}, {3,4} cover every target 6-12')
says('The failures are {2,4}: 7; {3,5}: 7; {4,5}: 6,7,11')
miss24 = [n for n in t if n not in reachable([2, 4], 20)]
log.check(miss24 == [7], f'K P6 guide lists {{2,4}} failures as "7"; actual failures in 6..12 are {miss24} '
          '(the {4,5} entry lists all its failures, so this reads as complete)')

# ---------------- Grades 2-3 ----------------
print('\n== Grades 2-3')
t = page_targets('grades-2-3', 1)
log.check(t == list(range(1, 17)) and [n for n in t if n not in R34] == [1, 2, 5], 'G23 P1: 1..16, only 1, 2, 5 fail')
p2 = {n: sorted(multisets([3, 4], n), reverse=True) for n in (12, 16, 24)}
log.info(f'G23 P2 (3s,4s): {p2}')
log.check(p2 == {12: [(4, 0), (0, 3)], 16: [(4, 1), (0, 4)], 24: [(8, 0), (4, 3), (0, 6)]}, 'G23 P2 matches guide lists')
says('12 has (4,0),(0,3); 16 has (4,1),(0,4); 24 has (8,0),(4,3),(0,6)')
log.check(all(len({y % 3 for x, y in multisets([3, 4], n)}) <= 1 for n in range(1, 200)),
          'G23 P2 guide: the number of 4-rods has one required remainder mod 3 (n < 200)')
t = page_targets('grades-2-3', 3)
log.check([n for n in t if n not in R35] == [1, 2, 4, 7] and last_gap([3, 5]) == 7, 'G23 P3: impossible 1,2,4,7; last impossible 7')


def min_consecutive_start(rods):
    a = min(rods)
    R = reachable(rods, BIG)
    return next(N for N in range(1, BIG) if all(N + i in R for i in range(a)))


log.check(last_gap([3, 4]) == 5 and min_consecutive_start([3, 4]) == 6, 'G23 P4 3/4: gaps stop after 5; first 3-run 6,7,8')
log.check(last_gap([3, 5]) == 7 and min_consecutive_start([3, 5]) == 8, 'G23 P4 3/5: gaps stop after 7; first 3-run 8,9,10')
says('Minimal consecutive certificates are 6,7,8 for 3/4 and 8,9,10 for 3/5')
# Is "covers every remainder and starts beyond the last gap" enough to say where the gaps stop?
c = [6, 10, 11]
cover = {n for n in range(0, 60) if any(n >= x and (n - x) % 3 == 0 for x in c)}
log.info(f'G23 P4 guide "any other finite collection that covers every remainder and starts beyond the last gap": '
         f'e.g. {c} with added 3-rods reaches {sorted(cover)[:6]}... but not 7, 8 (those need separate builds)')

t = page_targets('grades-2-3', 5)
R47 = reachable([4, 7], BIG)
log.check(t == list(range(12, 29)) and [n for n in t if n not in R47] == [13, 17] and last_gap([4, 7]) == 17,
          f'G23 P5: boxes 12..28, impossible {[n for n in t if n not in R47]}; last impossible overall {last_gap([4, 7])}')
says('18=4+7+7, 19=4+4+4+7, 20=4+4+4+4+4, 21=7+7+7')
log.check([17 - 7 * k for k in range(3)] == [17, 10, 3] and all((17 - 7 * k) % 4 for k in range(3)), 'G23 P5 17: 17, 10, 3 none divisible by 4')
log.check(infinite_gaps([2, 4]) and not infinite_gaps([4, 7]), 'G23 P6: 2/4 has infinitely many gaps (odd), 4/7 finitely many; claim false')

# ---------------- Grades 4-5 ----------------
print('\n== Grades 4-5')
log.check(gaps([3, 4], BIG) == [1, 2, 5], 'G45 P1: every impossible positive length for 3/4 is 1, 2, 5 (to 400)')
for rods, lg, cert in (([3, 5], 7, [8, 9, 10]), ([4, 5], 11, [12, 13, 14, 15]), ([4, 7], 17, [18, 19, 20, 21])):
    R = reachable(rods, BIG)
    log.check(last_gap(rods) == lg and all(c in R for c in cert) and len(cert) == min(rods) and cert[0] == lg + 1,
              f'G45 P2 {rods}: last gap {last_gap(rods)}; certificate {cert} is {min(rods)} consecutive builds')
says('12=4+4+4, 13=4+4+5, 14=4+5+5, 15=5+5+5')
log.check([11 - 5 * k for k in range(3)] == [11, 6, 1] and all((11 - 5 * k) % 4 for k in range(3)), 'G45 P2 11: 11, 6, 1 none divisible by 4')
t = page_targets('grades-4-5', 3)
log.check(t == list(range(18, 30)) and all(n in R47 for n in t), 'G45 P3: all twelve targets 18..29 buildable')
log.check(all(any(n - k in (18, 19, 20, 21) for k in (0, 4, 8)) for n in t), 'G45 P3 guide: 18..21 plus one or two 4-rods give 18..29')
log.check(17 not in R47, 'G45 P4: 17 impossible')
p2_47 = (last_gap([4, 7]), [18, 19, 20, 21])
log.info(f'G45 P2 third pair (4 and 7) asks for the last gap {p2_47[0]} and a certificate {p2_47[1]}: that certificate plus one or two '
         '4-rods is the whole of P3, and "17 is the last gap" contains P4; guide P3-4 key cites "the four builds 18-21" and "the three-case argument above"')
says('All twelve targets 18-29 work: use the four builds 18-21 and add 4 once or twice. Target 17 fails by the three-case argument above')

print('\n-- G45 P5')
for rods in ([2, 4], [3, 6], [4, 6], [3, 5], [4, 7]):
    g = gaps(rods, 40)
    log.info(f'{rods}: gcd {gcd(*rods)}, infinite gaps {infinite_gaps(rods)}, gaps to 40: {g}')
    log.check(infinite_gaps(rods) == (gcd(*rods) > 1), f'G45 P5 {rods}: infinitely many gaps iff common divisor > 1')
says('(odd targets, nonmultiples of 3, and odd targets respectively)')
g46 = gaps([4, 6], BIG)
even_gaps = [n for n in g46 if n % 2 == 0]
log.check(even_gaps == [], f'G45 P5 guide calls the 4/6 gaps "odd targets"; even gaps of 4/6: {even_gaps}')
log.check([n for n in gaps([2, 4], BIG) if n % 2 == 0] == [] and all(n % 3 for n in gaps([3, 6], BIG))
          and len(gaps([3, 6], BIG)) == len([n for n in range(1, BIG + 1) if n % 3]),
          'G45 P5 guide: 2/4 gaps are exactly the odd targets, 3/6 gaps exactly the nonmultiples of 3')

w24 = sorted(multisets([3, 4], 24), reverse=True)
log.check(w24 == [(8, 0), (4, 3), (0, 6)], f'G45 P6: all ways for 24 = {w24}')
log.check(all(abs(w24[i][0] - w24[i + 1][0]) == 4 and abs(w24[i][1] - w24[i + 1][1]) == 3 for i in range(2)),
          'G45 P6: neighbouring ways differ by exchanging four 3-rods for three 4-rods')
log.check(all((x1 - x2) % 4 == 0 and (y1 - y2) % 3 == 0 for n in range(1, 120) for (x1, y1) in multisets([3, 4], n)
              for (x2, y2) in multisets([3, 4], n)), 'G45 P6 guide: 3dx = -4dy forces multiples of the exchange (n < 120)')

R57 = reachable([5, 7], BIG)
t = page_targets('grades-4-5', 5)
log.check(last_gap([5, 7]) == 23 and [n for n in t if n not in R57] == [23], f'G45 P7: last gap 23; in boxes 19..31 only {[n for n in t if n not in R57]} fails')
log.check([23 - 7 * k for k in range(4)] == [23, 16, 9, 2] and all((23 - 7 * k) % 5 for k in range(4)), 'G45 P7 23: 23,16,9,2 none divisible by 5')
says('24=5+5+7+7, 25=5×5, 26=5+7+7+7, 27=5+5+5+5+7, 28=7×4')
log.check([last_gap(r) for r in ([3, 4], [3, 5], [4, 5], [4, 7], [5, 7])] == [5, 7, 11, 17, 23]
          and all(last_gap([a, b]) == a * b - a - b for a, b in ([3, 4], [3, 5], [4, 5], [4, 7], [5, 7])),
          'G45 P7 guide: earlier last gaps 5,7,11,17 and 23 fit ab-a-b')
R25 = reachable([2, 5], BIG)
log.check(4 in R25 and 5 in R25 and gaps([2, 5], BIG) == [1, 3], 'G45 P8 guide example: 2/5 builds 4 and 5, so all n >= 4 (gaps 1, 3)')

# ---------------- Overview and proofs ----------------
print('\n== Overview and proof claims')
bad = []
for a in range(1, 16):
    for b in range(1, 16):
        if a == b:
            continue
        g = gaps([a, b], 3 * a * b + 10)
        d = gcd(a, b)
        if d == 1 and a > 1 and b > 1:
            if not g or g[-1] != a * b - a - b:
                bad.append((a, b, 'F'))
        elif d == 1:
            if g:
                bad.append((a, b, 'one-rod'))
        else:
            if not all(n in g for n in range(1, 3 * a * b + 11) if n % d):
                bad.append((a, b, 'gcd'))
log.check(not bad, f'overview: coprime a,b>1 -> last gap ab-a-b; a 1-rod -> no positive gaps; gcd d>1 -> every non-multiple of d is a gap (all a != b <= 15); exceptions {bad}')
ex = [(a, b, [n for n in gaps([a, b], 200) if n % gcd(a, b) == 0]) for a, b in ([4, 6], [6, 9], [4, 10])]
log.info(f'(not claimed by the overview) gcd>1 pairs also miss a few small multiples of d: {ex}')
says('If a consecutive integers N, ..., N+a-1 are reachable, then every integer at least N is reachable')
says('the largest impossible target is ab-a-b, so every target at least (a-1)(b-1) works')
ok = True
for a in range(2, 13):
    for b in range(2, 13):
        if gcd(a, b) != 1:
            continue
        F = a * b - a - b
        for N in range(F + 1, F + 3 * a * b):
            j = next(j for j in range(a) if (j * b - N) % a == 0)
            i = (N - j * b) // a
            ok &= i >= 0 and N - j * b >= 1 - a
        x_ok = all(not (F - b * y >= 0 and (F - b * y) % a == 0) for y in range(F // b + 1))
        ok &= x_ok
log.check(ok, 'guide proof: for N > F the chosen j gives i >= 0, and F has no representation (coprime a,b <= 12)')
ok = all(len({(j * b) % a for j in range(a)}) == a for a in range(1, 20) for b in range(1, 30) if gcd(a, b) == 1)
log.check(ok, 'guide P8: 0, b, ..., (a-1)b have distinct remainders mod a when gcd(a,b)=1')
log.check(last_gap([2, 7]) == 5 and last_gap([3, 4]) == 5, 'extension: 2/7 and 3/4 both have last gap 5')
says('2/7 and 3/4 both have last gap 5')

# ---------------- Text and materials consistency ----------------
print('\n== Ranges in problem text vs boxes; rod kit')
pairs = [('grades-2-3', 1, r'from 1 through 16', list(range(1, 17))), ('grades-2-3', 3, r'from 1 through 20', list(range(1, 21))),
         ('grades-4-5', 3, r'from 18 through 29', list(range(18, 30))), ('k-1', 4, r'from 6 through 18', list(range(6, 19))),
         ('k-1', 5, r'from 1 through 12', list(range(1, 13))), ('k-1', 6, r'from 6 through 12', list(range(6, 13)))]
for band, page, phrase, want in pairs:
    log.check(phrase in student[band][page - 1] and page_targets(band, page) == want, f'{band} p{page} "{phrase}" matches target boxes')

unit_words = re.findall(r'\b\d*\s*(?:cm|centimet\w*|mm|inch\w*)\b', guide)
log.check(bool(unit_words), f'guide states the size of the printed unit (strips and rulers are 1 cm per unit, see pdf_geometry.out); found {unit_words}')
KIT = {2: 10, 3: 10, 4: 10, 5: 10, 7: 10}
needs = {('k-1', 'P1-P4'): [3, 4], ('k-1', 'P3'): [3, 5], ('k-1', 'P5'): [2, 4], ('grades-2-3', 'P5'): [4, 7],
         ('grades-4-5', 'P5'): [2, 4, 3, 6, 4, 6, 3, 5, 4, 7], ('grades-4-5', 'P7'): [5, 7]}
for (band, prob), lens in needs.items():
    missing = sorted({l for l in lens if l not in KIT})
    log.check(not missing, f'{band} {prob}: rod lengths {sorted(set(lens))} all in the guide kit (2,3,4,5,7); missing {missing}')
worst = {}
for rods, top in (([3, 4], 24), ([3, 5], 20), ([2, 4], 12), ([4, 7], 29), ([5, 7], 31), ([2, 3], 12), ([2, 5], 12), ([4, 5], 15)):
    for n in range(1, top + 1):
        ms = multisets(rods, n)
        if ms:
            worst[(tuple(rods), n)] = min(max(m) for m in ms)
mx = max(worst.values())
log.check(mx <= 10, f'every single printed target can be built with at most {mx} copies of one length (kit has 10)')
every = max(max(m) for n in (12, 15, 16, 24) for m in multisets([3, 4], n))
log.check(every <= 10, f'"find every way" builds for 12, 15, 16, 24 with 3/4 need at most {every} copies of one length')

log.done()
