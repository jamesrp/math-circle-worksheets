"""Independent check of the Week 27 bonus companion (week-27-bonus.pdf) and its
adult guide (week-27-bonus-facilitator.pdf).

Lists are read from the student source (bonus.tex) and confirmed against the
PDF text.  P1 by scoring and testing all six pairings; P2 by testing every
partial pairing of allowed pairs; P3 by testing all three roommate pairings;
P4 (a pairing set that changes the unpaired objects) by exhaustive search on
small incomplete-list markets and random 3x3 markets.  Output: check_bonus.out
"""
import os
import random
import re
import subprocess
import sys
from itertools import permutations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, WEEK, BONUS_SRC, Log, blockers, perfect_matchings, all_matchings, stable_all,  # noqa: E402
                    mname, parse_m, rank)

L = Log()
tex = open(os.path.join(BONUS_SRC, 'bonus.tex')).read()
ptxt = subprocess.run(['pdftotext', '-layout', os.path.join(WEEK, 'week-27-bonus.pdf'), '-'],
                      capture_output=True, text=True).stdout
gtxt = subprocess.run(['pdftotext', os.path.join(WEEK, 'week-27-bonus-facilitator.pdf'), '-'],
                      capture_output=True, text=True).stdout
g1 = ' '.join(gtxt.split())


def lst(s):
    s = s.strip()
    return [] if s in ('--', '–', '-') else [x.strip() for x in s.split(',')]


def pdf_has(row):
    return re.search(r'\s+'.join(re.escape(t) for t in row.split()), ptxt) is not None


# ------------------------------------------------------------- opening example
L.out('=== Opening example')
L.check('U--P' in tex and 'V--Q' in tex and 'V: P, \\fbox{Q}' in tex and 'P: V, \\fbox{U}' in tex,
        'current pairs U-P, V-Q; V lists P then Q (Q boxed); P lists V then U (U boxed)')
L.check(['P', 'Q'].index('P') < ['P', 'Q'].index('Q') and ['V', 'U'].index('V') < ['V', 'U'].index('U'),
        'V prefers P to current Q and P prefers V to current U: V and P block')

# ------------------------------------------------------------- P1
L.out('=== P1: score versus stability')
m = re.search(r'\\strips\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}', tex)
a = [lst(x) for x in m.groups()]
P1 = ({'A': a[0], 'B': a[1], 'C': a[2]}, {'X': a[3], 'Y': a[4], 'Z': a[5]})
L.out(f'  lists {P1}')
for who in 'ABC':
    L.check(pdf_has(f'{who} ' + ', '.join(P1[0][who])), f'PDF shows {who} {P1[0][who]}')
for who in 'XYZ':
    L.check(pdf_has(f'{who} ' + ', '.join(P1[1][who])), f'PDF shows {who} {P1[1][who]}')
rows = {}
for M in perfect_matchings('ABC', 'XYZ'):
    tot = sum(rank(P1[0][x], M[x]) + rank(P1[1][M[x]], x) for x in M)
    b = blockers(P1, M)
    rows[mname(M).replace(' ', '')] = (tot, b)
    L.out(f'    {mname(M):14s} total {tot:2d}  {"stable" if not b else "blockers " + ", ".join(b)}')
mn = min(t for t, _ in rows.values())
argmin = [k for k, (t, _) in rows.items() if t == mn]
stable = [k for k, (t, b) in rows.items() if not b]
L.check(argmin == ['AY/BZ/CX'] and mn == 10 and rows['AY/BZ/CX'][1] == ['BX'],
        f'lowest total {mn} at {argmin} only, blocked by BX')
L.check(stable == ['AY/BX/CZ'] and rows['AY/BX/CZ'][0] == 11, f'only stable pairing {stable}, total 11')
L.check(len(rows) == 6, 'six table rows printed, six pairings')
# guide P1 list "AX/BY/CZ: 15, AY/AZ/CY; ..."
for k, t, bl in re.findall(r'([A-C][X-Z]/[A-C][X-Z]/[A-C][X-Z]): (\d+), ((?:none|[A-C][X-Z](?:/[A-C][X-Z])*))', g1):
    listed = [] if bl == 'none' else bl.split('/')
    L.check(rows[k][0] == int(t) and sorted(listed) == sorted(rows[k][1]),
            f'guide P1 row {k}: total {t}, blockers {listed or "none"} (actual {rows[k][0]}, {rows[k][1] or "none"})')
L.check('pair scores 2,3,6 totaling 11' in g1, 'guide: AY/BX/CZ pair scores 2, 3, 6')
L.check([rank(P1[0]['A'], 'Y') + rank(P1[1]['Y'], 'A'), rank(P1[0]['B'], 'X') + rank(P1[1]['X'], 'B'),
         rank(P1[0]['C'], 'Z') + rank(P1[1]['Z'], 'C')] == [2, 3, 6], 'pair scores are 2, 3, 6')

# ------------------------------------------------------------- P2
L.out('=== P2: omitted choices')
t2a = re.search(r'A&X&X&A, B\\\\\[8pt\]B&X&Y&--', tex)
L.check(t2a is not None, 'first lists: A: X; B: X; X: A, B; Y: none')
P2a = ({'A': ['X'], 'B': ['X']}, {'X': ['A', 'B'], 'Y': []})
m = list(re.finditer(r'\\strips\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}', tex))[1]
a = [lst(x) for x in m.groups()]
P2b = ({'A': a[0], 'B': a[1], 'C': a[2]}, {'X': a[3], 'Y': a[4], 'Z': a[5]})
L.out(f'  second lists {P2b}')
for P, nrows, tag in ((P2a, 2, 'first'), (P2b, 3, 'second')):
    st = stable_all(P)
    objs = set(P[0]) | set(P[1])
    un = [sorted(objs - set(M) - set(M.values())) for M in st]
    L.out(f'  {tag}: stable {[mname(M) for M in st]}, unpaired {un}')
    for M in all_matchings(P):
        b = blockers(P, M)
        L.out(f'      {mname(M) or "(none)":10s} {"stable" if not b else "blockers " + ", ".join(b)}')
    L.check(len(st) <= nrows and all(u == un[0] for u in un), f'{tag}: {len(st)} stable, {nrows} table rows; same unpaired set every time')
L.check([mname(M) for M in stable_all(P2a)] == ['AX'], 'guide: first profile AX uniquely stable, B and Y unpaired')
L.check(sorted(mname(M) for M in stable_all(P2b)) == ['AX / BY', 'AY / BX'], 'guide: second profile exactly AX/BY and AY/BX, C and Z unpaired')
# guide "Depth": remove A-X from both lists of the first profile
P2c = ({'A': [], 'B': ['X']}, {'X': ['B'], 'Y': []})
L.check([mname(M) for M in stable_all(P2c)] == ['BX'], 'guide depth: without A-X, BX uniquely stable, A and Y unpaired')

# ------------------------------------------------------------- P3
L.out('=== P3: one group (roommates)')
rows3 = re.findall(r'([A-D])&([A-D], [A-D], [A-D])&([A-D])&([A-D], [A-D], [A-D])', tex)
left = {r[0]: lst(r[1]) for r in rows3}
right = {r[2]: lst(r[3]) for r in rows3}


def rm_block(pref, pairs):
    part = {}
    for p, q in pairs:
        part[p], part[q] = q, p
    out = []
    for p in sorted(pref):
        for q in sorted(pref):
            if p < q and part[p] != q and pref[p].index(q) < pref[p].index(part[p]) and pref[q].index(p) < pref[q].index(part[q]):
                out.append(p + q)
    return out


pairings = [(('A', 'B'), ('C', 'D')), (('A', 'C'), ('B', 'D')), (('A', 'D'), ('B', 'C'))]
res = {}
for tag, pref in (('left', left), ('right', right)):
    L.out(f'  {tag}: {pref}')
    for pr in pairings:
        b = rm_block(pref, pr)
        nm = '/'.join(p + q for p, q in pr)
        res[(tag, nm)] = b
        L.out(f'    {nm}: {"stable" if not b else "blockers " + ", ".join(b)}')
L.check(all(res[('left', n)] for n in ('AB/CD', 'AC/BD', 'AD/BC')), 'left: no stable pairing')
L.check('BC' in res[('left', 'AB/CD')] and 'AB' in res[('left', 'AC/BD')] and 'AC' in res[('left', 'AD/BC')],
        'guide left witnesses BC, AB, AC are blockers')
L.check(res[('right', 'AB/CD')] == [] and res[('right', 'AC/BD')] == ['AB', 'CD'] and res[('right', 'AD/BC')] == ['AB', 'AC', 'CD'],
        'guide right: AB/CD stable; AC/BD blocked by AB, CD; AD/BC by AB, AC, CD')
L.check(len(re.findall(r'\\roommateboard', tex)) - 1 == 6, 'six roommate boards (3 pairings x 2 lists)')

# ------------------------------------------------------------- P4 (rural hospitals)
L.out('=== P4: can two stable pairings leave different objects unpaired?')


def ordered_subsets(items):
    out = [[]]
    for k in range(1, len(items) + 1):
        for c in permutations(items, k):
            out.append(list(c))
    return out


def same_unpaired(P):
    st = stable_all(P)
    if not st:
        return False, 0
    sets = {frozenset(set(P[0]) | set(P[1])) - frozenset(M) - frozenset(M.values()) for M in st}
    return len(sets) == 1, len(st)


def exhaust(left, right):
    lo, ro = ordered_subsets(right), ordered_subsets(left)
    n = bad = 0
    multi = 0

    def rec_l(i, Ld):
        nonlocal n, bad, multi
        if i == len(left):
            def rec_r(j, Rd):
                nonlocal n, bad, multi
                if j == len(right):
                    ok, k = same_unpaired((Ld, Rd))
                    n += 1
                    bad += not ok
                    multi += k > 1
                    return
                for o in ro:
                    Rd[right[j]] = o
                    rec_r(j + 1, Rd)
            rec_r(0, {})
            return
        for o in lo:
            Ld[left[i]] = o
            rec_l(i + 1, Ld)
    rec_l(0, {})
    return n, bad, multi


for lft, rgt in (('AB', 'XY'), ('AB', 'XYZ'), ('ABC', 'XY')):
    n, bad, multi = exhaust(lft, rgt)
    L.check(bad == 0, f'{len(lft)}x{len(rgt)} exhaustive: {n} profiles, {multi} with several stable pairings, {bad} change the unpaired set')
rng = random.Random(27)
n = bad = 0
for _ in range(100000):
    Ld = {x: rng.sample('XYZ', rng.randint(0, 3)) for x in 'ABC'}
    Rd = {x: rng.sample('ABC', rng.randint(0, 3)) for x in 'XYZ'}
    ok, k = same_unpaired((Ld, Rd))
    n += 1
    bad += not ok
L.check(bad == 0, f'3x3 random: {n} incomplete-list profiles, {bad} change the unpaired set (the guide: impossible)')

L.save(os.path.join(HERE, 'check_bonus.out'))
