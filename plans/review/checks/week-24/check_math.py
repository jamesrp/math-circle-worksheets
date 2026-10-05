"""Independent mathematical check of the Week 24 base packet (nontransitive decks):
K-1, Grades 2-3, Grades 4-5 and the adult guide.

Every printed deck is taken from decks.json, i.e. read back out of the delivered PDFs by
extract_decks.py (run that first).  All answers are recomputed here by brute force; the
guide's stated answers are transcribed as CLAIMS, each is located in the guide's text, and
each is compared with the computation.  Output: out_check_math.txt
"""
import json
import os
import re
import sys
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb

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
D = json.load(open(os.path.join(HERE, 'decks.json')))
GUIDE = re.sub(r'\s+', ' ', ''.join(p.get_text() for p in pymupdf.open(os.path.join(WEEK, 'week-24-facilitator.pdf'))))

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def in_guide(snippet):
    """Confirm a transcribed claim really is printed in the guide (whitespace-normalised)."""
    s = re.sub(r'\s+', ' ', snippet)
    found = s in GUIDE
    check(found, f'guide text present: "{snippet[:90]}"')
    return found


def wins(x, y):
    """Number of physical card pairs in which deck x shows the larger card."""
    return sum(1 for a in x for b in y if a > b)


def ties(x, y):
    return sum(1 for a in x for b in y if a == b)


def decks(band, problem):
    pg = [p for p in D[band] if p['problem'] == problem]
    assert len(pg) == 1
    return pg[0]


def named(band, problem, idx=0):
    """Map label -> values for the idx-th set of decks on the page (by order of appearance)."""
    pg = decks(band, problem)
    groups, cur = [], {}
    for d in pg['decks']:
        if d['label'] in cur:
            groups.append(cur); cur = {}
        cur[d['label']] = tuple(d['values'])
    groups.append(cur)
    return groups[idx]


def cyc(A, B, C, need=None):
    """Directed counts A>B, B>C, C>A; with need=None test a strict majority of all pairs."""
    ab, bc, ca = wins(A, B), wins(B, C), wins(C, A)
    if need is None:
        ok = ab > wins(B, A) and bc > wins(C, B) and ca > wins(A, C)
    else:
        ok = ab >= need and bc >= need and ca >= need
    return (ab, bc, ca), ok


A0, B0, C0 = (2, 4, 9), (1, 6, 8), (3, 5, 7)

# ---------------------------------------------------------------- diagrams = intended data
say('=== Printed decks agree with the intended data ===')
k1 = D['k-1']
check([d['values'] for d in k1[0]['decks'][:2]] == [list(A0), list(B0)], 'K-1 P1 deck rows are A=(2,4,9), B=(1,6,8)')
check([d['values'] for d in k1[1]['decks'][:2]] == [list(B0), list(C0)], 'K-1 P2 deck rows are B=(1,6,8), C=(3,5,7)')
check([d['values'] for d in k1[2]['decks'][:2]] == [list(C0), list(A0)], 'K-1 P3 deck rows are C=(3,5,7), A=(2,4,9)')
for i, (l1, X, l2, Y) in enumerate((('A', A0, 'B', B0), ('B', B0, 'C', C0), ('C', C0, 'A', A0))):
    single = k1[i]['decks'][2:]
    pairs = [(single[j]['label'], single[j]['values'][0], single[j + 1]['label'], single[j + 1]['values'][0])
             for j in range(0, len(single), 2)]
    got = sorted((a, b) for (la, a, lb, b) in pairs if la == l1 and lb == l2)
    check(len(pairs) == 9 and got == sorted(product(X, Y)),
          f'K-1 P{i+1}: the nine pictured pairs are labelled {l1} then {l2} and are exactly all 9 pairs, each once')
    say('     pictured pairs:', [(a, b) for (_, a, _, b) in pairs])
for band in ('grades-2-3', 'grades-4-5'):
    g = named(band, 1)
    check(g == {'A': A0, 'B': B0, 'C': C0}, f'{band} P1 decks are A=(2,4,9), B=(1,6,8), C=(3,5,7)')

# ---------------------------------------------------------------- the basic cycle
say('\n=== Original decks: all 27 pairs ===')
for (n1, X), (n2, Y) in ((('A', A0), ('B', B0)), (('B', B0), ('C', C0)), (('C', C0), ('A', A0))):
    w, l, t = wins(X, Y), wins(Y, X), ties(X, Y)
    say(f'{n1} over {n2}: {w}/9, reverse {l}/9, ties {t}; winning pairs {[(a, b) for a in X for b in Y if a > b]}')
    check(w == 5 and l == 4 and t == 0, f'{n1} beats {n2} 5 to 4')
for X in (A0, B0, C0):
    others = [Y for Y in (A0, B0, C0) if Y != X]
    check(not all(wins(X, Y) > wins(Y, X) for Y in others), f'{X} does not beat both others')
check(sum(A0) == sum(B0) == sum(C0) == 15, 'all three totals are 15 (4-5 P1: totals do not settle it)')
# guide matrices on printed p. 3
def matrix(R, Cc, rn, cn):
    return [[rn if r > c else cn for c in Cc] for r in R]
say('K-1 key matrices (row deck / column deck):')
for R, Cc, rn, cn, claim in ((A0, B0, 'A', 'B', 'AAA BBA BBA'), (B0, C0, 'B', 'C', 'CBB CBB CCB'),
                             (C0, A0, 'C', 'A', 'CCC ACC AAA')):
    m = matrix(R, Cc, rn, cn)
    say('   ', rn, 'vs', cn, m)
# columns as printed in the guide, read column by column
check(matrix(A0, B0, 'A', 'B') == [['A', 'B', 'B'], ['A', 'B', 'B'], ['A', 'A', 'A']], 'guide p.3 Problem 1 matrix')
check(matrix(B0, C0, 'B', 'C') == [['C', 'C', 'C'], ['B', 'B', 'C'], ['B', 'B', 'B']], 'guide p.3 Problem 2 matrix')
check(matrix(C0, A0, 'C', 'A') == [['C', 'A', 'A'], ['C', 'C', 'A'], ['C', 'C', 'A']], 'guide p.3 Problem 3 matrix')
in_guide('A wins (2,1),(4,1),(9,1),(9,6),(9,8): five pairs; B wins four.')
in_guide('B wins (6,3),(6,5),(8,3),(8,5),(8,7): five pairs; C wins four.')
in_guide('C wins (3,2),(5,2),(5,4),(7,2),(7,4): five pairs; A wins four.')

# ---------------------------------------------------------------- K-1 P4 and the six-round game
say('\n=== K-1 P4 / 2-3 P2 / extension: short games ===')
choice = {}
for nm, X in (('A', A0), ('B', B0), ('C', C0)):
    better = [m for m, Y in (('A', A0), ('B', B0), ('C', C0)) if wins(Y, X) > wins(X, Y)]
    choice[nm] = better
check(choice == {'A': ['C'], 'B': ['A'], 'C': ['B']}, f'deck that beats each deck: {choice}')
in_guide('Against A choose C; against B choose A; against C choose B.')
p, q = F(5, 9), F(4, 9)
ahead = sum(comb(6, k) * p**k * q**(6 - k) for k in (4, 5, 6))
tie3 = comb(6, 3) * p**3 * q**3
behind = 1 - ahead - tie3
say(f'favoured deck strictly ahead after 6: {ahead} = {float(ahead):.4f}; 3-3 tie {tie3} = {float(tie3):.4f}; behind {float(behind):.4f}')
say(f'lose all six: (4/9)^6 = {q**6} = {float(q**6):.5f}')
check(round(float(ahead) * 100, 1) == 45.3, 'guide: favoured deck ahead "about 45.3%"')
check(round(float(tie3) * 100, 1) == 30.1, 'guide: 3-3 tie "about 30.1%"')
check(ahead < F(1, 2), 'favoured deck is ahead after six rounds with chance below one half')
in_guide('about 45.3%')
in_guide('about 30.1%')
# 2-3 P2: every finite left/right winner sequence has positive probability either way
for n in range(1, 9):
    for seq in product('LR', repeat=n):
        w = seq.count('L'); l = n - w
        assert p**w * q**l > 0 and q**w * p**l > 0
check(all(0 < wins(X, Y) < 9 for X in (A0, B0, C0) for Y in (A0, B0, C0) if X != Y),
      '2-3 P2: in every ordered matchup each bag wins some pairs and loses some, so no finite winner record is impossible under either assignment')

# ---------------------------------------------------------------- K-1 P5
say('\n=== K-1 P5 ===')
pg = decks('k-1', 5)
check(pg['decks'][0]['values'][:2] == [2, 4] and pg['decks'][0]['values'][2] is None and pg['pool'] == [3, 5, 7, 9],
      'K-1 P5 diagram: A=(2,4,_), B=(1,6,8), candidates 3,5,7,9')
res = {x: (wins((2, 4, x), B0), wins(B0, (2, 4, x))) for x in pg['pool']}
say('A wins / B wins for each candidate:', res)
check([x for x, (a, b) in res.items() if a > b] == [9], 'only 9 makes A win more pairs than B')
check([res[x][0] for x in (3, 5, 7, 9)] == [3, 3, 4, 5], 'guide: A totals 3,3,4,5')
in_guide('Thus A totals 3,3,4,5 out of nine')

# ---------------------------------------------------------------- K-1 P6
say('\n=== K-1 P6: every single swap ===')
table = {}
for i, a in enumerate(A0):
    for j, b in enumerate(B0):
        A = list(A0); B = list(B0); A[i], B[j] = b, a
        table[(a, b)] = (wins(B, A), wins(A, B), tuple(sorted(A)), tuple(sorted(B)))
for k, v in table.items():
    say(f'  swap A{k[0]}/B{k[1]}: B wins {v[0]}, A wins {v[1]}; A={v[2]} B={v[3]}')
claim = {(2, 1): 5, (2, 6): 2, (2, 8): 1, (4, 1): 6, (4, 6): 3, (4, 8): 2, (9, 1): 9, (9, 6): 6, (9, 8): 5}
check(all(table[k][0] == v for k, v in claim.items()), 'guide p.4 swap table entries (B wins) all correct')
works = sorted(k for k, v in table.items() if v[0] > v[1])
check(works == [(2, 1), (4, 1), (9, 1), (9, 6), (9, 8)], f'exactly five swaps work: {works}')

# ---------------------------------------------------------------- K-1 P7
say('\n=== K-1 P7: two three-card decks from 1-6 with equal wins ===')
eq = [A for A in combinations(range(1, 7), 3)
      if wins(A, tuple(sorted(set(range(1, 7)) - set(A)))) == wins(tuple(sorted(set(range(1, 7)) - set(A))), A)]
check(eq == [], f'no split of 1-6 into two decks of three gives equal win counts (all {comb(6,3)} splits tried)')

# ---------------------------------------------------------------- two-card cycles from 1..6
say('\n=== K-1 P8 / 2-3 P7: three two-card decks from 1-6 ===')
count = 0; found = []
for perm in permutations(range(1, 7)):
    A, B, C = tuple(sorted(perm[0:2])), tuple(sorted(perm[2:4])), tuple(sorted(perm[4:6]))
    if A[0] > A[1] or perm[0] > perm[1] or perm[2] > perm[3] or perm[4] > perm[5]:
        continue
    count += 1
    if cyc(A, B, C)[1]:
        found.append((A, B, C))
    # the deck holding 1 has at most two wins against each other deck
    for X, others in ((A, (B, C)), (B, (A, C)), (C, (A, B))):
        if 1 in X:
            assert all(wins(X, Y) <= 2 for Y in others)
check(count == 90 and not found, f'none of the {count} labelled arrangements is a cycle; the deck holding 1 never wins more than 2 of 4')

# ---------------------------------------------------------------- fixed maxima (2-3 P3, 4-5 P2)
say('\n=== 2-3 P3 / 4-5 P2: keep 9 in A, 8 in B, 7 in C ===')
for band, pr in (('grades-2-3', 3), ('grades-4-5', 2)):
    pg = decks(band, pr)
    check([d['values'] for d in pg['decks']] == [[None, None, 9], [None, None, 8], [None, None, 7]]
          and pg['pool'] == [1, 2, 3, 4, 5, 6], f'{band} P{pr} diagram: blanks + 9/8/7, pool 1-6')
sols = []
cases = 0
cert = {}
for a in combinations(range(1, 7), 2):
    rest = [x for x in range(1, 7) if x not in a]
    first_two, all_three = [], []
    for b in combinations(rest, 2):
        c = tuple(x for x in rest if x not in b)
        cases += 1
        A, B, C = a + (9,), b + (8,), c + (7,)
        cnt, ok = cyc(A, B, C)
        # W formulas from the guide, checked against the full count
        assert (wins(A, B) >= 5) == (wins(a, b) >= 2)
        assert (wins(B, C) >= 5) == (wins(b, c) >= 2)
        assert (wins(C, A) >= 5) == (wins(c, a) >= 3)
        if wins(a, b) >= 2 and wins(b, c) >= 2:
            first_two.append(b)
            if wins(c, a) >= 3:
                all_three.append(b)
        if ok:
            sols.append((A, B, C, cnt))
    cert[a] = (first_two, all_three)
check(cases == 90, f'{cases} cases (15 x 6)')
for s in sols:
    say('   cycle:', s)
check(sorted(s[:3] for s in sols) == sorted([((1, 5, 9), (3, 4, 8), (2, 6, 7)), ((2, 3, 9), (1, 6, 8), (4, 5, 7)),
                                              ((2, 4, 9), (1, 6, 8), (3, 5, 7))]),
      'exactly three arrangements, the guide\'s three rows (so two besides Problem 1)')
check({s[:3]: s[3] for s in sols}[((1, 5, 9), (3, 4, 8), (2, 6, 7))] == (5, 5, 5)
      and {s[:3]: s[3] for s in sols}[((2, 3, 9), (1, 6, 8), (4, 5, 7))] == (5, 5, 6), 'directed counts 5,5,5 and 5,5,6')
check(all((wins(a, b) >= 2) == (wins(a + (9,), b + (8,)) >= 5) for a in combinations(range(1, 7), 2)
          for b in combinations([x for x in range(1, 7) if x not in a], 2)), 'guide W(a,b)>=2 / W(b,c)>=2 / W(c,a)>=3 formulas exact (asserted for all 90)')
CERT = {(1, 2): ([], []), (1, 3): ([], []), (1, 4): ([], []), (1, 5): ([(3, 4)], [(3, 4)]),
        (1, 6): ([(2, 5), (3, 4), (3, 5), (4, 5)], []), (2, 3): ([(1, 6)], [(1, 6)]), (2, 4): ([(1, 6)], [(1, 6)]),
        (2, 5): ([(1, 6), (3, 4)], []), (2, 6): ([(1, 5), (3, 4), (3, 5), (4, 5)], []),
        (3, 4): ([(1, 6), (2, 5), (2, 6)], []), (3, 5): ([(1, 6), (2, 4), (2, 6)], []),
        (3, 6): ([(1, 5), (2, 4), (2, 5), (4, 5)], []), (4, 5): ([(1, 6), (2, 3), (2, 6), (3, 6)], []),
        (4, 6): ([(1, 5), (2, 3), (2, 5), (3, 5)], []), (5, 6): ([(1, 4), (2, 3), (2, 4), (3, 4)], [])}
for a in cert:
    if cert[a] != CERT[a]:
        say('   computed', a, cert[a], 'guide', CERT[a])
check(cert == CERT, 'guide p.9 certificate table: all 15 rows, both columns, match the computation')
in_guide('(1,6) (2,5), (3,4), (3,5), (4,5) None')
in_guide('(5,6) (1,4), (2,3), (2,4), (3,4) None')
# worked row (1,5)
check(all(wins((1, 5), b) <= 1 for b in ((2, 6), (3, 6), (4, 6))), 'guide p.9: (1,5) against a B pair containing 6 wins at most 1')
check(wins((2, 3), (4, 6)) == 0 and wins((2, 4), (3, 6)) == 1, 'guide p.9: B=(2,3)/C=(4,6) gives 0, B=(2,4)/C=(3,6) gives 1')
check((wins((1, 5), (3, 4)), wins((3, 4), (2, 6)), wins((2, 6), (1, 5))) == (2, 2, 3), 'guide p.9: low counts 2,2,3')

# ---------------------------------------------------------------- 2-3 P4
say('\n=== 2-3 P4: A=(2,x,9) ===')
pg = decks('grades-2-3', 4)
check(pg['decks'][0]['values'] == [2, None, 9] and pg['pool'] == [0, 2, 4, 9, 10], '2-3 P4 diagram: A=(2,_,9), choices 0,2,4,9,10')
rows = {}
for x in pg['pool']:
    A = (2, x, 9)
    assert not (set(A) & set(B0)) and not (set(A) & set(C0))
    rows[x] = cyc(A, B0, C0)
    say(f'  x={x}: A>B {rows[x][0][0]}, B>C {rows[x][0][1]}, C>A {rows[x][0][2]}; cycle {rows[x][1]}')
check([x for x in rows if rows[x][1]] == [2, 4], 'only x=2 and x=4 keep the cycle')
check({x: rows[x][0] for x in rows} == {0: (4, 5, 6), 2: (5, 5, 6), 4: (5, 5, 5), 9: (7, 5, 3), 10: (7, 5, 3)}, 'guide p.7 table counts')

# ---------------------------------------------------------------- 6-card and 4-card decks
say('\n=== 2-3 P5 / 4-5 P4: duplicated decks ===')
A6, B6, C6 = named('grades-2-3', 5).values()
check((A6, B6, C6) == ((2, 2, 4, 4, 9, 9), (1, 1, 6, 6, 8, 8), (3, 3, 5, 5, 7, 7)), '2-3 P5 six-card decks as intended')
check(tuple(named('grades-4-5', 4, 0).values()) == (A6, B6, C6), '4-5 P4 six-card decks as intended')
A4, B4, C4 = named('grades-4-5', 4, 1).values()
check((A4, B4, C4) == ((2, 2, 4, 9), (1, 1, 6, 8), (3, 3, 5, 7)), '4-5 P4 four-card decks copy each smallest value once')
six = {('A', 'B'): wins(A6, B6), ('B', 'A'): wins(B6, A6), ('B', 'C'): wins(B6, C6), ('C', 'B'): wins(C6, B6),
       ('C', 'A'): wins(C6, A6), ('A', 'C'): wins(A6, C6)}
four = {('A', 'B'): wins(A4, B4), ('B', 'A'): wins(B4, A4), ('B', 'C'): wins(B4, C4), ('C', 'B'): wins(C4, B4),
        ('C', 'A'): wins(C4, A4), ('A', 'C'): wins(A4, C4)}
say('six-card wins /36:', six)
say('four-card wins /16:', four)
check(six == {('A', 'B'): 20, ('B', 'A'): 16, ('B', 'C'): 20, ('C', 'B'): 16, ('C', 'A'): 20, ('A', 'C'): 16}, 'six-card: 20 to 16 out of 36 each way, same winners')
check(four == {('A', 'B'): 10, ('B', 'A'): 6, ('B', 'C'): 7, ('C', 'B'): 9, ('C', 'A'): 10, ('A', 'C'): 6}, 'guide p.10 four-card table: 10/6, 7/9, 10/6 out of 16')
orig = {('A', 'B'): 5, ('B', 'A'): 4, ('B', 'C'): 5, ('C', 'B'): 4, ('C', 'A'): 5, ('A', 'C'): 4}
check(all(F(four[k], 16) != F(orig[k], 9) for k in orig), 'every four-card chance differs from the original')
check(all(F(six[k], 36) == F(orig[k], 9) for k in orig), 'every six-card chance equals the original')
check(four[('C', 'A')] > 8 and four[('A', 'B')] > 8 and four[('C', 'B')] > 8, 'four-card relation: C over A, A over B, C over B (no cycle)')
# guide p.10 gate: "Counting distinct printed number-pairs as equally likely gives the wrong answer."
in_guide('Counting distinct printed number-pairs as equally likely gives the wrong answer.')
from collections import Counter
for nm, (X, Y) in (('six-card A/B', (A6, B6)), ('six-card B/C', (B6, C6)), ('four-card A/B', (A4, B4)), ('four-card B/C', (B4, C4))):
    mult = Counter((a, b) for a in X for b in Y)
    uniform = len(set(mult.values())) == 1
    distinct = F(sum(1 for (a, b) in mult if a > b), len(mult))
    true = F(wins(X, Y), len(X) * len(Y))
    say(f'   {nm}: distinct number-pairs equally likely? {uniform}; distinct-pair count gives {distinct}, true chance {true}')
six_ok = all(F(sum(1 for (a, b) in set(product(X, Y)) if a > b), 9) == F(wins(X, Y), 36) for X, Y in ((A6, B6), (B6, C6), (C6, A6)))
check(not six_ok, 'guide gate sentence holds for the six-card decks too (expected FAIL: there the 9 distinct number-pairs are '
      'equally likely, 4 physical copies each, and give the right 5/9)')
check(F(sum(1 for (a, b) in set(product(B4, C4)) if a > b), 9) == F(5, 9) and F(wins(B4, C4), 16) == F(7, 16),
      'four-card decks: distinct-pair counting gives B over C 5/9, true 7/16 (wrong winner) -- the gate is right here')
check(wins((2, 2, 4, 9), (1, 1, 6, 8)) == 2 + 2 + 2 + 4 and wins((1, 1, 6, 8), (3, 3, 5, 7)) == 0 + 0 + 3 + 4
      and wins((3, 3, 5, 7), (2, 2, 4, 9)) == 2 + 2 + 3 + 3, 'guide row sums 2+2+2+4, 0+0+3+4, 2+2+3+3')

# ---------------------------------------------------------------- 2-3 P6
say('\n=== 2-3 P6: nine different cards from 1-12, totals 15/18/21 ===')
check(decks('grades-2-3', 6)['pool'] == list(range(1, 13)), '2-3 P6 pool is 1-12')
sol6 = []
for A in combinations(range(1, 13), 3):
    if sum(A) != 15:
        continue
    for B in combinations([x for x in range(1, 13) if x not in A], 3):
        if sum(B) != 18:
            continue
        for C in combinations([x for x in range(1, 13) if x not in A and x not in B], 3):
            if sum(C) != 21:
                continue
            cnt, ok = cyc(A, B, C)
            if ok:
                sol6.append((A, B, C, cnt))
for s in sol6:
    say('   solution:', s)
check(((3, 5, 7), (2, 4, 12), (1, 9, 11), (5, 5, 6)) in sol6, 'guide example A=(3,5,7), B=(2,4,12), C=(1,9,11) works with counts 5,5,6')
check(len(sol6) == 1, f'guide p.13 "exactly one solution to the revised 15,18,21 construction": found {len(sol6)}')
space = sum(1 for A in combinations(range(1, 13), 3) if sum(A) == 15
            for B in combinations([x for x in range(1, 13) if x not in A], 3) if sum(B) == 18
            for C in combinations([x for x in range(1, 13) if x not in A + B], 3) if sum(C) == 21)
say(f'   context: {space} labelled assignments meet all three totals; {len(sol6)} of them is a cycle')

# ---------------------------------------------------------------- 4-5 P3
say('\n=== 4-5 P3: values 1-6, repeats only within a deck ===')
ms = list(combinations_with_replacement(range(1, 7), 3))
sol3 = []
for A in ms:
    for B in ms:
        if set(A) & set(B):
            continue
        for C in ms:
            if set(C) & (set(A) | set(B)):
                continue
            if cyc(A, B, C)[1]:
                sol3.append((A, B, C))
say(f'   {len(sol3)} labelled multiset solutions; e.g. {sol3[:4]}')
check(len(sol3) > 0, 'a cycle exists using only values 1-6')
check(((1, 4, 4), (3, 3, 3), (2, 2, 5)) in sol3 and cyc((1, 4, 4), (3, 3, 3), (2, 2, 5))[0] == (6, 6, 5),
      'guide example A=(1,4,4), B=(3,3,3), C=(2,2,5) works: 6, 6, 5 out of 9')
with_triple = [s for s in sol3 if any(len(set(X)) == 1 for X in s)]
say(f'   solutions containing a deck of three equal cards: {len(with_triple)}')
uses_all = [s for s in sol3 if set(s[0]) | set(s[1]) | set(s[2]) == set(range(1, 7))]
say(f'   solutions that use every value 1-6 at least once: {len(uses_all)}; e.g. {uses_all[:2]}')

# ---------------------------------------------------------------- 4-5 P5: the two-card rule
say('\n=== 4-5 P5: two-card decks ===')
pg = decks('grades-4-5', 5)
P = {d['label']: tuple(d['values']) for d in pg['decks']}
check(P == {'A': (1, 5), 'B': (2, 4), 'C': (2, 6), 'D': (1, 5), 'E': (4, 6), 'F': (2, 3), 'G': (1, 3), 'H': (2, 6)},
      '4-5 P5 printed pairs')
res5 = {(x, y): (wins(P[x], P[y]), wins(P[y], P[x])) for x, y in (('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'))}
say('   ', res5)
check(res5 == {('A', 'B'): (2, 2), ('C', 'D'): (3, 1), ('E', 'F'): (4, 0), ('G', 'H'): (1, 3)}, 'guide p.11 table: 2-2 neither, 3-1 C, 4-0 E, 1-3 H')
bad = 0; tested = 0
for X in combinations_with_replacement(range(1, 9), 2):
    for Y in combinations_with_replacement(range(1, 9), 2):
        if set(X) & set(Y):
            continue
        tested += 1
        rule = X[0] > Y[0] and X[1] > Y[1]
        if rule != (wins(X, Y) > 2):
            bad += 1
check(bad == 0, f'rule "sorted, both coordinates larger" <=> majority, all {tested} disjoint two-card deck pairs over 1-8 (repeats allowed)')

# ---------------------------------------------------------------- 4-5 P6: fewest cards
say('\n=== 4-5 P6: fewest cards per deck ===')
one = [(a, b, c) for a, b, c in permutations(range(1, 7), 3) if a > b > c > a]
check(not one, 'no one-card cycle')
two = 0
vals = range(1, 9)
for A in combinations_with_replacement(vals, 2):
    for B in combinations_with_replacement(vals, 2):
        if set(A) & set(B):
            continue
        for C in combinations_with_replacement(vals, 2):
            if set(C) & (set(A) | set(B)):
                continue
            if cyc(A, B, C)[1]:
                two += 1
check(two == 0, 'no two-card cycle over values 1-8 with repeats inside decks (exhaustive)')
check(cyc(A0, B0, C0) == ((5, 5, 5), True), 'three cards suffice (5,5,5)')
# transitivity of the two-card relation even when A and C may share a value
viol = 0
for A in combinations_with_replacement(vals, 2):
    for B in combinations_with_replacement(vals, 2):
        for C in combinations_with_replacement(vals, 2):
            if set(A) & set(B) or set(B) & set(C):
                continue
            if wins(A, B) > 2 and wins(B, C) > 2 and not wins(A, C) > 2:
                viol += 1
check(viol == 0, 'two-card majority relation is transitive (overview claim)')

# ---------------------------------------------------------------- 4-5 P7 and the 1,680 partitions
say('\n=== 4-5 P7 / guide audit: all labelled partitions of 1-9 ===')
check(decks('grades-4-5', 7)['pool'] == list(range(1, 10)), '4-5 P7 pool is 1-9')
nparts = 0; strict = []; six_all = []; best_min = 0
for A in combinations(range(1, 10), 3):
    r1 = [x for x in range(1, 10) if x not in A]
    for B in combinations(r1, 3):
        C = tuple(x for x in r1 if x not in B)
        nparts += 1
        cnt, ok = cyc(A, B, C)
        if ok:
            strict.append((A, B, C, cnt))
            best_min = max(best_min, min(cnt))
        if min(cnt) >= 6:
            six_all.append((A, B, C))
check(nparts == 1680, f'{nparts} labelled partitions (84 x 20)')
check(len(strict) == 15, f'guide: 15 labelled strict cycles -> found {len(strict)}')
unl = {frozenset(s[:3]) for s in strict}
say(f'   {len(unl)} unlabelled nontransitive partitions:', sorted(sorted(u) for u in unl))
check(not six_all, 'no partition has all three cyclic counts >= 6 (best cycle minimum is %d)' % best_min)
# the guide's proof step 3, as a general statement for distinct values
viol = 0
for vals9 in [range(1, 10)]:
    for A in combinations(vals9, 3):
        if 9 not in A:
            continue
        a, b = sorted(A)[:2]
        r1 = [x for x in vals9 if x not in A]
        for B in combinations(r1, 3):
            if wins(A, B) >= 6 and sum(1 for x in B if x < b) < 2:
                viol += 1
check(viol == 0, 'guide step 3: if A=(a,b,9) wins >= 6 against B then at least two B cards are below b')

# ---------------------------------------------------------------- extensions
say('\n=== Extensions ===')
f = lambda x: 3 * x + 100
check(all(wins(tuple(map(f, X)), tuple(map(f, Y))) == wins(X, Y) for X in (A0, B0, C0) for Y in (A0, B0, C0)),
      'strictly increasing relabelling keeps every count')
check(all(F(wins(X * r, Y * s), 9 * r * s) == F(wins(X, Y), 9) for r in (1, 2, 3) for s in (1, 2, 3)
          for X in (A0, B0, C0) for Y in (A0, B0, C0)), 'r and s copies keep every fraction')
in_guide('Replacement restores the same probabilities in each round.')

say('\nFAILURES:', len(FAIL))
for m in FAIL:
    say('  ', m)
open(os.path.join(HERE, 'out_check_math.txt'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
