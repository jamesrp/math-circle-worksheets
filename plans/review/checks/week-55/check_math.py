"""Independent mathematical check of Week 55 (few sums and equal spacing).

Written for this review; imports nothing from the writer's or guide's checkers.
* Reads the printed inputs (pairs, launch example, fixed A of Problem 5, the
  page-9 count example, the page-8 grids and the blank-slot counts) from the
  editable source students.tex, and checks that every printed card value also
  appears in the delivered student PDF text (pdftotext).
* Recomputes every answer for Problems 1-10 by its own enumeration over the
  0-9 kit, and checks the general theorems exhaustively on small ranges:
  m+n-1 <= |A+B| <= mn for all nonempty subsets of {0..10}, and the equality
  characterisation (m,n >= 2 => common-gap progressions) both ways.
* Compares each answer, table row and example the delivered facilitator guide
  prints (pdftotext) against the computation.
Run: python3 check_math.py   (writes out_check_math.txt beside itself)
"""
import itertools
import os
import re
import subprocess
import sys
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
if not os.path.isdir(os.path.join(ROOT, 'lowell-math-circle-year-2')):
    # run-folder layout tmp/review-runs/week-NN/ is three folders deep
    ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
WEEK = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-55')
SRC = os.path.join(ROOT, 'lowell-math-circle-year-2', 'source', 'week-55')
STUDENT_PDF = os.path.join(WEEK, 'week-55-students.pdf')
GUIDE_PDF = os.path.join(WEEK, 'week-55-facilitator.pdf')
TEX = os.path.join(SRC, 'student', 'students.tex')

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def sumset(A, B):
    return sorted({a + b for a in A for b in B})


def is_common_gap_ap(A, B):
    A, B = sorted(A), sorted(B)
    gaps = {y - x for x, y in zip(A, A[1:])} | {y - x for x, y in zip(B, B[1:])}
    return len(gaps) == 1


def fmt(s):
    return ', '.join(str(x) for x in s)


def pdftext(path, page=None):
    cmd = ['pdftotext', '-layout']
    if page:
        cmd += ['-f', str(page), '-l', str(page)]
    return subprocess.run(cmd + [path, '-'], capture_output=True, text=True, check=True).stdout


def norm(t):
    t = t.replace('\u2212', '-').replace('\u2013', '-')
    return re.sub(r'\s+', ' ', t)


# ---------------------------------------------------------------- source data
tex = open(TEX).read()
body = tex.split('\\begin{document}')[1]
pages = body.split('\\newpage')
say('student source pages:', len(pages))
check(len(pages) == 10, 'ten student pages in source')
student_pdf_pages = [norm(pdftext(STUDENT_PDF, i + 1)) for i in range(10)]


def ints(s):
    return [int(x) for x in s.split(',')]


def pairs_on(p):
    return [(ints(a), ints(b)) for _, a, b in re.findall(r'\\pair\{(\d+)\}\{([\d,]+)\}\{([\d,]+)\}', pages[p])]


def cards_on(p):
    return [(lab, ints(v)) for lab, v in re.findall(r'\\cards\{\d+\}\{\d+\}\{([AB])\}\{([\d,]+)\}', pages[p])]


def grids_on(p):
    return [(ints(a), ints(b), int(step)) for a, b, step in
            re.findall(r'\\arraygrid\{\d+\}\{\d+\}\{([\d,]+)\}\{([\d,]+)\}\{(\d+)\}', pages[p])]


def blanks_on(p):
    return [(int(m), int(n)) for _, m, n in re.findall(r'\\blankpair\{(\d+)\}\{(\d+)\}\{(\d+)\}', pages[p])]


def pdf_has_row(pg, A, B):
    """The delivered page has a line 'A a1 a2 ... B b1 b2 ...'."""
    pat = r'A ' + ' '.join(map(str, A)) + r' B ' + ' '.join(map(str, B))
    return re.search(r'(?<![\d])' + pat + r'(?![\d])', student_pdf_pages[pg]) is not None


# ------------------------------------------------------------------ the kit
KIT = range(10)


def subsets(k, universe=KIT):
    return list(itertools.combinations(universe, k))


# ------------------------------------------------------------- page 1 launch
say('\n== Page 1 launch example')
c = cards_on(0)
launchA = [v for lab, v in c if lab == 'A'][0]
launchB = [v for lab, v in c if lab == 'B'][0]
say('launch A', launchA, 'B', launchB, 'sumset', sumset(launchA, launchB))
check(re.search(r'A 1 4 ', student_pdf_pages[0]) is not None and re.search(r'B 0 3 ', student_pdf_pages[0]) is not None,
      'launch inputs A 1 4 and B 0 3 printed in PDF')
for a, b, t in [(1, 3, 4), (4, 0, 4), (1, 0, 1)]:
    check(a in launchA and b in launchB and a + b == t, f'launch try {a}+{b}={t} is a legal pair with that total')
check(sumset(launchA, launchB) == [1, 4, 7], 'complete launch sumset is {1,4,7} (guide: picture partial, 7 untried)')
# the launch example is not one of the task trials
alltrials = [p for pg in range(10) for p in pairs_on(pg)]
check((launchA, launchB) not in alltrials, 'launch example is not a task trial')

# --------------------------------------------------------------- Problems 1-2
say('\n== Problems 1-2')
P1 = pairs_on(0)
P2 = pairs_on(1)
check(len(P1) == 2 and len(P2) == 3, 'P1 has 2 trials, P2 has 3 trials')
for pg, plist in [(0, P1), (1, P2)]:
    for A, B in plist:
        check(pdf_has_row(pg, A, B), f'p{pg+1}: delivered PDF shows A {A} B {B}')
c1 = [len(sumset(A, B)) for A, B in P1]
c2 = [len(sumset(A, B)) for A, B in P2]
for (A, B), k in zip(P1 + P2, c1 + c2):
    say(f'  {A} + {B} = {sumset(A, B)}  ({k})')
check(c1[0] < c1[1], 'P1: first trial has fewer')
check(c2.index(min(c2)) == 0 and c2.count(min(c2)) == 1, 'P2: first has strictly the fewest')
check(c2.index(max(c2)) == 2 and c2.count(max(c2)) == 1, 'P2: third has strictly the most')
for (A, B) in P1 + P2:
    check(max(sumset(A, B)) <= 18, f'{A}+{B} fits the 0-18 lane')

# ------------------------------------------------------------- Problem 3
say('\n== Problem 3: three cards each from 0-9')
check(blanks_on(2) == [(3, 3)] * 4, 'P3: four blank 3+3 records')
counts = {}
mins, maxs = [], []
for A in subsets(3):
    for B in subsets(3):
        k = len(sumset(A, B))
        counts[k] = counts.get(k, 0) + 1
lo, hi = min(counts), max(counts)
say('  distribution of |A+B| over all ordered (A,B):', dict(sorted(counts.items())))
check((lo, hi) == (5, 9), f'P3 min {lo}, max {hi} (expected 5 and 9)')
minimal = [(A, B) for A in subsets(3) for B in subsets(3) if len(sumset(A, B)) == 5]
check(all(is_common_gap_ap(A, B) for A, B in minimal),
      f'all {len(minimal)} minimal 3+3 designs are common-gap progressions (guide adult key)')
check(len(sumset([0, 1, 2], [0, 1, 2])) == 5 and len(sumset([0, 1, 2], [0, 3, 6])) == 9,
      'guide witnesses 2a (5) and 2c (9)')

# ------------------------------------------------------------- Problem 4
say('\n== Problem 4')
sizes = blanks_on(3)
check(sizes == [(2, 3), (2, 4), (3, 4)], f'P4 sizes {sizes}')
guide_min = {(2, 3): 4, (2, 4): 5, (3, 4): 6}
for m, n in sizes:
    best = min(len(sumset(A, B)) for A in subsets(m) for B in subsets(n))
    mins_mn = [(A, B) for A in subsets(m) for B in subsets(n) if len(sumset(A, B)) == best]
    say(f'  {m}+{n}: minimum {best}, {len(mins_mn)} minimal designs in 0-9')
    check(best == m + n - 1 == guide_min[(m, n)], f'P4 {m}+{n} minimum = m+n-1 = {m+n-1} (guide {guide_min[(m, n)]})')
    check(all(is_common_gap_ap(A, B) for A, B in mins_mn), f'P4 {m}+{n}: every minimum is common-gap')
for A, B, S in [([0, 1], [0, 1, 2], [0, 1, 2, 3]), ([0, 1], [0, 1, 2, 3], [0, 1, 2, 3, 4]),
                ([0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4, 5])]:
    check(sumset(A, B) == S, f'guide P4 witness {A}+{B}={S}')

# ------------------------------------------------------------- Problem 5
say('\n== Problem 5')
c5 = cards_on(4)
A5 = [v for lab, v in c5 if lab == 'A'][0]
check(A5 == [0, 3, 6], f'P5 fixed A = {A5}')
check('A 0 3 6' in student_pdf_pages[4], 'P5 A printed in PDF')
nslots = len(re.findall(r'\\cards\{\d+\}\{\\y\}\{B\}', pages[4])) * len(re.search(r'\\foreach \\y in \{([\d,]+)\}', pages[4]).group(1).split(','))
allB = subsets(2)
check(len(allB) == 45 == comb(10, 2), '45 two-card B from 0-9')
sol5 = [B for B in allB if len(sumset(A5, B)) == 4]
say('  solutions:', sol5)
check(sol5 == [(t, t + 3) for t in range(7)], 'P5 catalog is exactly B={t,t+3}, t=0..6 (seven)')
say(f'  printed B slots: {nslots}; solutions: {len(sol5)}')
check(nslots >= len(sol5), 'P5 has room for every solution')
for B in sol5:
    check(max(sumset(A5, B)) <= 18, f'{B} totals fit lane')
# guide continuations
s024 = [B for B in allB if len(sumset((0, 2, 4), B)) == 4]
check(s024 == [(t, t + 2) for t in range(8)], f'guide: A={{0,2,4}} gives eight B={{t,t+2}}, 0<=t<=7 -> {s024}')
s013 = [B for B in allB if len(sumset((0, 1, 3), B)) == 4]
check(s013 == [], 'guide: A={0,1,3} has no two-card B with four totals')
# shift-overlap argument in the guide
for s in range(1, 10):
    ov = len({0, 3, 6} & {s, s + 3, s + 6})
    check(ov == {3: 2, 6: 1}.get(s, 0), f'guide shift argument: shift {s} -> {ov} coincidences')

# ------------------------------------------------------------- Problem 6
say('\n== Problem 6')
P6 = pairs_on(5)
for A, B in P6:
    check(pdf_has_row(5, A, B), f'p6: PDF shows A {A} B {B}')
c6 = [len(sumset(A, B)) for A, B in P6]
for (A, B), k in zip(P6, c6):
    ga = {y - x for x, y in zip(A, A[1:])}
    gb = {y - x for x, y in zip(B, B[1:])}
    check(len(ga) == 1 and len(gb) == 1, f'{A},{B} each equally spaced (gaps {ga},{gb})')
    say(f'  {A} + {B} = {sumset(A, B)} ({k})')
check(all((len(A), len(B)) == (3, 2) for A, B in P6), 'all P6 sizes are 3+2')
best32 = min(len(sumset(A, B)) for A in subsets(3) for B in subsets(2))
check(best32 == 4, 'fewest possible for 3+2 is 4')
check(any(k > best32 for k in c6), 'P6 answer is "no": some equally spaced pair exceeds the minimum')
check(c6 == [4, 6, 4, 4], f'guide P6 counts 4,6,4,4 -> {c6}')

# ------------------------------------------------------------- Problem 7
say('\n== Problem 7')
P7 = pairs_on(6)
for A, B in P7:
    check(pdf_has_row(6, A, B), f'p7: PDF shows A {A} B {B}')
    check(len(A) == 1 and len(sumset(A, B)) == len(B), f'{A}+{B}={sumset(A, B)}: count equals |B|={len(B)}')
check(any(len({y - x for x, y in zip(B, B[1:])}) > 1 for A, B in P7), 'P7 includes an unequally spaced B')
# rule holds for every singleton and every nonempty B in the kit
ok = all(len(sumset([a], B)) == len(B) for a in KIT for k in range(1, 11) for B in subsets(k))
check(ok, 'singleton rule |{a}+B| = |B| for every a and every nonempty B in 0-9')

# ------------------------------------------------------------- Problem 8
say('\n== Problem 8 grids')
G = grids_on(7)
check(len(G) == 3, 'three grids on page 8 (demo + two tasks)')


def routes(m, n):
    """All monotone routes from (0,0) to (m-1,n-1) as move strings (R = B index +1, U = A index +1)."""
    for pos in itertools.combinations(range(m + n - 2), m - 1):
        yield ''.join('U' if k in pos else 'R' for k in range(m + n - 2))


def walk(A, B, w):
    i = j = 0
    out = [A[0] + B[0]]
    for ch in w:
        if ch == 'R':
            j += 1
        else:
            i += 1
        out.append(A[i] + B[j])
    return out


names = ['demonstration', 'left task', 'right task']
guide_routes = {
    'demonstration': 'RRU, RUR, URR',
    'left task': 'RRUU, RURU, RUUR, URRU, URUR, UURR',
    'right task': 'RRRUU, RRURU, RRUUR, RURRU, RURUR, RUURR, URRRU, URRUR, URURR, UURRR',
}
for name, (A, B, step) in zip(names, G):
    check(A == sorted(A) and B == sorted(B), f'{name}: rows/columns increasing')
    m, n = len(A), len(B)
    rs = list(routes(m, n))
    vals = [walk(A, B, w) for w in rs]
    S = sumset(A, B)
    say(f'  {name}: A={A} B={B} grid rows (top->bottom):', [[a + b for b in B] for a in reversed(A)])
    say(f'    sumset {S} ({len(S)}); routes {len(rs)}; each route visits {m+n-1} dots')
    check(all(all(x < y for x, y in zip(v, v[1:])) for v in vals), f'{name}: every route strictly increasing, no repeat')
    check(all(len(set(v)) == m + n - 1 for v in vals), f'{name}: every route has {m+n-1} different totals')
    check(sorted(rs) == sorted(guide_routes[name].split(', ')), f'{name}: guide route catalog matches ({len(rs)})')
    covers = all(set(v) == set(S) for v in vals)
    say(f'    every route covers whole sumset: {covers}')
    if name == 'demonstration':
        check(walk(A, B, 'RUR') == [1, 3, 7, 11], 'demo bold route R,U,R gives 1,3,7,11')
        check(S == [1, 3, 5, 7, 11], 'guide: demo grid totals {1,3,5,7,11}, five')
        check(A[0] + B[1] == 3, 'demo: A row 1 + B column 2 = 3')
    if name == 'left task':
        check(S == [1, 3, 4, 5, 6, 8, 9] and not covers, 'guide: left sumset seven values; a route need not cover it')
        check(walk(A, B, 'RRUU') == [1, 3, 4, 6, 9] and walk(A, B, 'UURR') == [1, 3, 6, 8, 9], 'guide left examples RRUU, UURR')
    if name == 'right task':
        check(S == [1, 3, 5, 7, 9, 11] and covers, 'guide: right sumset six values; every route covers it')
        check(walk(A, B, 'RRRUU') == [1, 3, 5, 7, 9, 11], 'guide right example RRRUU')
    # every pair of equal grid values is incomparable (cannot both lie on a route)
    cells = [(i, j, A[i] + B[j]) for i in range(m) for j in range(n)]
    clash = [(c1, c2) for c1, c2 in itertools.combinations(cells, 2)
             if c1[2] == c2[2] and ((c1[0] <= c2[0] and c1[1] <= c2[1]) or (c1[0] >= c2[0] and c1[1] >= c2[1]))]
    check(not clash, f'{name}: equal values never lie on one route')

# ---------------------------------------------------------- Problem 9 example
say('\n== Page 9 count example and Problem 9')
c9 = cards_on(8)
A9 = [v for lab, v in c9 if lab == 'A'][0]
B9 = [v for lab, v in c9 if lab == 'B'][0]
m9, n9 = len(A9), len(B9)
check((A9, B9) == ([1, 4], [0, 2, 5, 8]), f'p9 example A={A9} B={B9}')
check('m+n-1=2+4-1=5' in student_pdf_pages[8].replace(' ', ''), 'p9 prints m+n-1=2+4-1=5')
check(re.search(r'm\s*×\s*n\s*=\s*2\s*×\s*4\s*=\s*8', student_pdf_pages[8]) is not None, 'p9 prints m×n=2×4=8')
check((m9, n9, m9 + n9 - 1, m9 * n9) == (2, 4, 5, 8), 'p9 count substitution correct')
check(sumset(A9, B9) == [1, 3, 4, 6, 9, 12], f'guide: example full result set {{1,3,4,6,9,12}} -> {sumset(A9, B9)}')

# exhaustive bound and equality check on {0..10} with bit masks
say('\n== General theorems (exhaustive over nonempty subsets of {0..10})')
N = 11
sets = []
for mask in range(1, 1 << N):
    els = [i for i in range(N) if mask >> i & 1]
    sets.append((mask, els))
viol_lo = viol_hi = 0
eq_nonsingle = eq_ap = ap_not_eq = eq_single = 0
for ma, A in sets:
    m = len(A)
    gapA = {y - x for x, y in zip(A, A[1:])}
    for mb, B in sets:
        n = len(B)
        s = 0
        for a in A:
            s |= mb << a
        k = bin(s).count('1')
        if k < m + n - 1:
            viol_lo += 1
        if k > m * n:
            viol_hi += 1
        if m >= 2 and n >= 2:
            gapB = {y - x for x, y in zip(B, B[1:])}
            common = len(gapA) == 1 and gapA == gapB
            if k == m + n - 1:
                eq_nonsingle += 1
                if common:
                    eq_ap += 1
            elif common:
                ap_not_eq += 1
        elif k == m + n - 1:
            eq_single += 1
total_pairs = len(sets) ** 2
say(f'  ordered pairs checked: {total_pairs}')
check(viol_lo == 0, 'no pair has fewer than m+n-1 totals')
check(viol_hi == 0, 'no pair has more than mn totals')
check(eq_nonsingle == eq_ap, f'm,n>=2 equality cases {eq_nonsingle}: all common-gap progressions')
check(ap_not_eq == 0, 'every common-gap pair with m,n>=2 attains m+n-1')
singles = sum(1 for ma, A in sets for mb, B in sets if len(A) == 1 or len(B) == 1)
check(eq_single == singles, f'every pair with a singleton attains the bound ({eq_single} of {singles})')

# sharpness constructions from the guide
for m in range(1, 13):
    for n in range(1, 13):
        A = list(range(m))
        check_lo = len(sumset(A, list(range(n)))) == m + n - 1
        check_hi = len(sumset(A, [j * m for j in range(n)])) == m * n
        if not (check_lo and check_hi):
            check(False, f'guide sharpness constructions fail at m={m}, n={n}')
check(True, 'guide sharpness constructions attain m+n-1 and mn for all 1<=m,n<=12')
check(sumset([0, 1, 2], [0, 3, 6, 9]) == list(range(12)), 'guide 3+4 maximum example {0,1,2}+{0,3,6,9} = {0..11}')
check(sumset([-2, 0, 2], [-3, -1, 1]) == [-5, -3, -1, 1, 3], 'guide signed example')
check(len({(a + b) % 3 for a in range(3) for b in range(3)}) == 3 < 5, 'guide: bound fails mod 3 (Z3+Z3 has 3 < 5)')

# guide index formula i=min(k,m-1), j=k-i
okidx = all(0 <= k - min(k, m - 1) < n for m in range(1, 15) for n in range(1, 15) for k in range(m + n - 1))
check(okidx, 'guide index choice i=min(k,m-1), j=k-i stays in range')

# local square swap: in an equality case both middle values agree
okswap = True
for A in itertools.chain.from_iterable(subsets(k, range(9)) for k in (2, 3, 4)):
    for B in itertools.chain.from_iterable(subsets(k, range(9)) for k in (2, 3)):
        if len(sumset(A, B)) == len(A) + len(B) - 1:
            for i in range(len(A) - 1):
                for j in range(len(B) - 1):
                    if A[i + 1] + B[j] != A[i] + B[j + 1]:
                        okswap = False
check(okswap, 'local-square swap: at equality a_{i+1}+b_j = a_i+b_{j+1} for every square')
# demo grid is nonminimal and the alternatives differ
check(5 + 0 != 1 + 2, 'guide: demonstration square alternatives differ (5 vs 3)')

# ------------------------------------------------------------- Problem 10 text
say('\n== Problem 10 statement')
t10 = student_pdf_pages[9]
check('at least two cards' in t10, 'P10 states each input has at least two cards')
check('whole-number' in t10, 'P10 restricts to whole numbers')

# --------------------------------- other reading of "Each input has different numbers"
say('\n== Other reading: A and B share no number (page-1 rule read as "the inputs differ")')
t1 = student_pdf_pages[0]
check('Each input has different numbers' in t1, 'page-1 rule text "Each input has different numbers."')
shared = [(pg + 1, A, B) for pg in range(10) for A, B in pairs_on(pg) if set(A) & set(B)]
say('  printed trials whose A and B share a number:', shared)
d3 = [len(sumset(A, B)) for A in subsets(3) for B in subsets(3) if not set(A) & set(B)]
say(f'  P3 under disjoint reading: min {min(d3)}, max {max(d3)} (unchanged 5, 9)')
for m, n in sizes:
    best = min(len(sumset(A, B)) for A in subsets(m) for B in subsets(n) if not set(A) & set(B))
    say(f'  P4 {m}+{n} under disjoint reading: minimum {best}')
sol5d = [B for B in sol5 if not set(B) & set(A5)]
say(f'  P5 under disjoint reading: {len(sol5d)} answers {sol5d} instead of {len(sol5)}')
say(f'  note: the P5 "find every" count depends on the reading ({len(sol5)} vs {len(sol5d)})')

# ---------------------------------------------------- guide text cross-check
say('\n== Guide text cross-check')
g = norm(pdftext(GUIDE_PDF))
rows_guide = [('1a', P1[0]), ('1b', P1[1]), ('2a', P2[0]), ('2b', P2[1]), ('2c', P2[2])]
for lab, (A, B) in rows_guide:
    S = sumset(A, B)
    pat = f'{lab} {fmt(A)} {fmt(B)} {fmt(S)} {len(S)}'
    check(pat in g, f'guide row "{pat}"')
for A, B in P6:
    S = sumset(A, B)
    pat = f'{fmt(A)} {fmt(B)} {fmt(S)} {len(S)}'
    check(pat in g, f'guide P6 row "{pat}"')
for B in sol5:
    pat = '{' + fmt(B) + '} {' + fmt(sumset(A5, B)) + '}'
    check(pat in g, f'guide P5 row "{pat}"')
for A, B in P7:
    pat = '{' + fmt(A) + '} + {' + fmt(B) + '} = {' + fmt(sumset(A, B)) + '} (' + str(len(sumset(A, B))) + ')'
    check(pat in g, f'guide P7 "{pat}"')
check('The minimum is 5 and the maximum 9' in g, 'guide P3 min/max sentence')
check('There are seven choices' in g, 'guide P5 count sentence')
check('{1, 3, 4, 6, 9, 12}' in g, 'guide P9 example result set')
check('The complete example has {1, 4, 7}' in g, 'guide launch complete example')
check('Pages 7-8 give the complete argument' in g, 'guide overview cites its pages 7-8 for the proof')
gp = [norm(pdftext(GUIDE_PDF, i)) for i in (7, 8)]
check('Lower bound' in gp[0] and 'Necessity' in gp[1], 'guide pages 7-8 hold the lower bound and the inverse proof')
check('separate prior tiling option is specified on page 2' in g and 'K-1 option' in norm(pdftext(GUIDE_PDF, 2)),
      'guide K-1 tiling option is on its page 2')

say('\nSUMMARY:', 'all checks passed' if not FAIL else f'{len(FAIL)} FAIL(s)')
for f in FAIL:
    say('  FAIL:', f)
open(os.path.join(HERE, 'out_check_math.txt'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
sys.exit(1 if FAIL else 0)
