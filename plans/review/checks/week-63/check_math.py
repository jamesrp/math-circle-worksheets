"""Independent mathematical check of Week 63 (cards away from home).

Enumerates every row by its own backtracking (no writer or guide verifier is
imported), computes every printed answer for Problems 1-9, and compares every
row list, intersection, family and count in the delivered facilitator PDF
(text read with pdftotext) against that enumeration.
Run: python3 check_math.py   (writes out_check_math.txt beside itself)
"""
import itertools
import math
import os as _os
import re
import subprocess
import sys

HERE = _os.path.dirname(_os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfgeom63 as G  # noqa: E402  (only for the repository paths)

OUT = []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


FAIL = []


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


from rows63 import rows, matches, derangements, arrows, cycles, row_from_arrows, reduce_row, restore  # noqa: E402


# ---------------------------------------------------------------- guide text
def page_text(pdf, n):
    return subprocess.run(['pdftotext', '-layout', '-f', str(n), '-l', str(n), pdf, '-'],
                          capture_output=True, text=True, check=True).stdout


GUIDE = [page_text(G.GUIDE_PDF, n) for n in range(1, 11)]
STUD = [page_text(G.STUDENT_PDF, n) for n in range(1, 10)]


def words(s):
    return re.findall(r'\b[A-E]{2,5}\b', s)


ABC, ABCD, ABCDE = 'ABC', 'ABCD', 'ABCDE'

# ---------------------------------------------------------------- P1
say('== P1 (student p. 1): home-free A-C rows; exactly two matches?')
d3 = derangements(ABC)
say('home-free A-C rows:', d3)
two = [r for r in rows(ABC) if len(matches(r, ABC)) == 2]
say('rows with exactly two matches:', two)
check(d3 == ['BCA', 'CAB'] and two == [], 'P1: two home-free rows BCA, CAB; no row has exactly two matches')
g = GUIDE[3]
tab = {m[0]: (m[1], m[2]) for m in re.findall(r'^\s*([A-C]{3})\s+(none|[A-C](?:, [A-C])*)\s+(\d)\s*$', g, re.M)}
for r in rows(ABC):
    ms = sorted(matches(r, ABC))
    want = (', '.join(ms) if ms else 'none', str(len(ms)))
    check(tab.get(r) == want, f'guide P1 table row {r}: printed {tab.get(r)} vs {want}')
# Week 43 cross-reference: swap slot 1 with slot 2 or 3, then swap slots 2 and 3
w43 = set()
for j in (1, 2):
    s = list('ABC')
    s[0], s[j] = s[j], s[0]
    s[1], s[2] = s[2], s[1]
    w43.add(''.join(s))
check(w43 == set(d3), f'Week 43 grades 4-5 p. 3 P5 procedure gives {sorted(w43)} = the two home-free rows')

# ---------------------------------------------------------------- P2
say('\n== P2 (student p. 2): outside both A-home and B-home groups (6 cards)')
U3 = rows(ABC)
GA = [r for r in U3 if r[0] == 'A']
GB = [r for r in U3 if r[1] == 'B']
outside = [r for r in U3 if r[0] != 'A' and r[1] != 'B']
say('A-home', GA, 'B-home', GB, 'both', sorted(set(GA) & set(GB)), 'outside', outside)
check(len(outside) == 3 and 6 - 2 - 2 == 2 and 6 - len(GA) - len(GB) + len(set(GA) & set(GB)) == 3,
      'P2: outside both = 3 = 6-2-2+1; printed student count 6-2-2 = 2 is the subtract-only count')
g = GUIDE[3]
check('{ABC, ACB}' in g and '{ABC, CBA}' in g and 'BAC, BCA, CAB' in g and '6 − 2 − 2 + 1 = 3' in g,
      'guide P2 groups/outside/total match')
check('6 − 2 − 2 = 2' in STUD[1], 'student p. 2 prints the count 6 - 2 - 2 = 2')

# ---------------------------------------------------------------- P3
say('\n== P3 (student p. 3): home-free A-D rows')
d4 = derangements(ABCD)
say(len(d4), d4)
check(len(d4) == 9, 'P3: 9 home-free A-D rows')
gt = {}
for m in re.finditer(r'^\s*([BCD])\s+([A-D]{4}(?:, [A-D]{4})+)\s*$', GUIDE[3], re.M):
    gt[m.group(1)] = m.group(2).split(', ')
for f in 'BCD':
    want = [r for r in d4 if r[0] == f]
    check(gt.get(f) == want, f'guide P3 branch {f}: {gt.get(f)} vs {want}')
recip = [r for r in d4 if all(len(c) == 2 for c in cycles(r, ABCD))]
four = [r for r in d4 if len(cycles(r, ABCD)) == 1]
check(recip == ['BADC', 'CDAB', 'DCBA'] and len(four) == 6,
      f'guide: two-pair rows {recip}, four-cycles {len(four)}')

# ---------------------------------------------------------------- P4
say('\n== P4 (student p. 4): A away from A and B away from B')
U4 = rows(ABCD)
p4 = [r for r in U4 if r[0] != 'A' and r[1] != 'B']
say(len(p4), p4)
HA = {r for r in U4 if r[0] == 'A'}
HB = {r for r in U4 if r[1] == 'B'}
check(len(p4) == 14 == 24 - len(HA) - len(HB) + len(HA & HB) and sorted(HA & HB) == ['ABCD', 'ABDC'],
      'P4: 14 = 24-6-6+2 (intersection ABCD, ABDC); student check count 24-6-6 = 12')
gt = {}
for m in re.finditer(r'^\s*([BCD])\s+([A-D]{4}(?:, [A-D]{4})+)\s*$', GUIDE[4], re.M):
    gt.setdefault(m.group(1), m.group(2).split(', '))
for f in 'BCD':
    want = [r for r in p4 if r[0] == f]
    check(gt.get(f) == want, f'guide P4 branch {f}: {gt.get(f)} vs {want}')

# ---------------------------------------------------------------- P5
say('\n== P5 (student p. 5): four home-groups, inclusion-exclusion')
inter = {}
for k in range(0, 5):
    for S in itertools.combinations(ABCD, k):
        inter[''.join(S)] = [r for r in U4 if all(r[ABCD.index(s)] == s for s in S)]
total = sum((-1) ** len(S) * len(v) for S, v in inter.items())
check(total == 9 == len(d4), f'P5: alternating sum = {total} = 9 home-free rows')
check(24 - 4 * 6 + 6 * 2 - 4 * 1 + 1 == 9, 'guide P5 arithmetic 24-24+12-4+1 = 9')
lines = re.findall(r'^\s*([A-D]{1,4})\s{2,}((?:[A-D]{4}, )*[A-D]{4})\s+(\d)\s*$', GUIDE[4], re.M)
printed = {a: (b.split(', '), int(c)) for a, b, c in lines}
for S in ['A', 'B', 'C', 'D', 'AB', 'AC', 'AD', 'BC', 'BD', 'CD', 'ABCD']:
    check(printed.get(S) == (inter[S], len(inter[S])), f'guide P5 intersection {S}: {printed.get(S)}')
for S in ['ABC', 'ABD', 'ACD', 'BCD']:
    check(inter[S] == ['ABCD'], f'triple {S} = [ABCD]')
for kforb, want in [(1, 18), (2, 14), (3, 11), (4, 9)]:
    forb = ABCD[:kforb]
    n = sum(1 for r in U4 if all(r[ABCD.index(h)] != h for h in forb))
    check(n == want, f'forbidding {kforb} specified own homes leaves {n} (guide says {want})')
check(24 - 18 + 6 - 1 == 11 and 24 - 6 == 18, 'guide extension arithmetic')
# per-row weights for four cards
for r in U4:
    M = matches(r, ABCD)
    w = sum((-1) ** k * math.comb(len(M), k) for k in range(len(M) + 1))
    assert w == (1 if not M else 0)
check(True, 'every A-D row has weight 1 if home-free else 0')

# ---------------------------------------------------------------- P6
say('\n== P6 (student p. 6): five groups')
U5 = rows(ABCDE)
check(len(U5) == 120, '120 A-E rows')
tot = 0
sizes = {}
for k in range(6):
    for S in itertools.combinations(ABCDE, k):
        n = sum(1 for r in U5 if all(r[ABCDE.index(s)] == s for s in S))
        sizes.setdefault(k, set()).add(n)
        tot += (-1) ** k * n
say('intersection sizes by k:', sizes)
check(tot == 44 == len(derangements(ABCDE)), f'P6: alternating sum {tot} = 44 home-free rows')
check(sizes == {0: {120}, 1: {24}, 2: {6}, 3: {2}, 4: {1}, 5: {1}}, 'guide P6 table sizes 120,24,6,2,1,1')
check([math.comb(5, k) * s for k, s in zip(range(6), [120, 24, 6, 2, 1, 1])] == [120, 120, 60, 20, 5, 1],
      'guide P6 totals 120,120,60,20,5,1')
acd = [r for r in U5 if r[0] == 'A' and r[2] == 'C' and r[3] == 'D']
check(acd == ['ABCDE', 'AECDB'], f'guide: ACD intersection {acd}')
dist = [sum(1 for r in U5 if len(matches(r, ABCDE)) == m) for m in range(6)]
check(dist == [44, 45, 20, 10, 0, 1], f'guide: match distribution {dist}')
check(sorted(matches('AECDB', ABCDE)) == ['A', 'C', 'D'], 'AECDB has match set {A,C,D}')
for r in U5:
    M = matches(r, ABCDE)
    w = sum((-1) ** len(S) for k in range(len(M) + 1) for S in itertools.combinations(sorted(M), k))
    assert w == (1 if not M else 0)
check(True, 'every A-E row has alternating weight 1 if home-free else 0')
g6 = GUIDE[5]
check('120 − 120 + 60 − 20 + 5 − 1 = 44' in g6, 'guide prints 120-120+60-20+5-1 = 44')
if 'intersections of size k containing that row' in g6.replace('\n', ' '):
    say('note guide p. 6 calls k-group intersections "intersections of size k" right after a '
        'table whose "Each size" column means number of rows (wording only)')

# ---------------------------------------------------------------- p. 7 bridge
say('\n== Student p. 7 bridge example')
a = arrows('QRSTP', 'PQRST')
check(a['P'] == 'T', 'QRSTP: P is in home T')
check(cycles('QRSTP', 'PQRST') == [['P', 'T', 'S', 'R', 'Q']], 'QRSTP arrows form P->T->S->R->Q->P')

# ---------------------------------------------------------------- P7
say('\n== P7 (student p. 7): D in home A')
p7 = [r for r in d4 if r[0] == 'D']
say(p7)
check(p7 == ['DABC', 'DCAB', 'DCBA'], 'P7: three rows DABC, DCAB, DCBA')
fam = {r: reduce_row(r, ABCD, 'D') for r in p7}
say(fam)
check(fam['DCBA'] == ('reciprocal', 'BC', 'CB') and fam['DABC'] == ('longer', 'ABC', 'CAB')
      and fam['DCAB'] == ('longer', 'ABC', 'BCA'), 'guide P7 reductions DCBA->CB, DABC->CAB, DCAB->BCA')
check([r for r in p7 if r[3] == 'A'] == ['DCBA'], 'only DCBA has A in home D')
check(cycles('DABC', ABCD) == [['A', 'B', 'C', 'D']] and cycles('DCAB', ABCD) == [['A', 'C', 'B', 'D']],
      'guide P7 arrows D->A->B->C->D and D->A->C->B->D (same cycles)')
for h in 'ABC':
    check(sum(1 for r in d4 if r[ABCD.index(h)] == 'D') == 3, f'D at home {h}: three rows')

# ---------------------------------------------------------------- p. 8 examples
say('\n== Student p. 8 non-task removal examples')
top = {'P': 'U', 'U': 'P', 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'Q'}
r_top = row_from_arrows(top, 'PQRSTU')
check(r_top == 'UTQRSP', f'top input row {r_top}')
check(reduce_row(r_top, 'PQRSTU', 'U') == ('reciprocal', 'QRST', 'TQRS'), 'top output Q/R/S/T row TQRS (4-cycle)')
bot = {'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'U', 'U': 'P'}
r_bot = row_from_arrows(bot, 'PQRSTU')
check(r_bot == 'UPQRST', f'bottom input row {r_bot}')
check(reduce_row(r_bot, 'PQRSTU', 'U') == ('longer', 'PQRST', 'TPQRS'), 'bottom output row TPQRS')
check(arrows('TPQRS', 'PQRST') == {'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'P'},
      'bottom output arrows P->Q->R->S->T->P')
check(restore('longer', 'PQRST', 'TPQRS', 'PQRSTU', 'U', 'P') == r_bot
      and restore('reciprocal', 'QRST', 'TQRS', 'PQRSTU', 'U', 'P') == r_top, 'both restorations return the input')

# ---------------------------------------------------------------- P8
say('\n== P8 (student p. 8): E in home A')
p8 = [r for r in derangements(ABCDE) if r[0] == 'E']
say(len(p8), p8)
check(len(p8) == 11, 'P8: 11 rows with E at home A')
red = {r: reduce_row(r, ABCDE, 'E') for r in p8}
rec = sorted(r for r in p8 if red[r][0] == 'reciprocal')
lon = sorted(r for r in p8 if red[r][0] == 'longer')
check(rec == ['ECDBA', 'EDBCA'] and len(lon) == 9, f'P8 families: reciprocal {rec}, longer {len(lon)}')
check(sorted(red[r][2] for r in rec) == sorted(derangements('BCD'))
      and sorted(red[r][2] for r in lon) == sorted(d4), 'P8 reductions are bijections onto D(BCD) and D(ABCD)')
for r in p8:
    f, hs, sr = red[r]
    assert restore(f, hs, sr, ABCDE, 'E', 'A') == r
    if f == 'longer':
        assert sr == r[4] + r[1:4]  # guide: "last entry to the first entry"
check(True, 'P8 every reduction restores uniquely; longer reduction = last entry moved to first')
gl = re.findall(r'^\s*(E[A-D]{4})\s+(reciprocal|longer)\s+(A,E removed: B/C/D|E removed: A/B/C/D) / ([A-D]{3,4})\s*$',
                GUIDE[7], re.M)
check(len(gl) == 11, f'guide P8 table has {len(gl)} rows')
for full, f, _, small in gl:
    check(red.get(full, ('?', '', ''))[0] == f and red[full][2] == small, f'guide P8 {full} {f} -> {small}')
check(reduce_row('EADBC', ABCDE, 'E')[2] == 'CADB', 'guide example EADBC -> CADB')

# ---------------------------------------------------------------- P9
say('\n== P9 (student p. 9): pooled catalog and recurrence')
d5 = derangements(ABCDE)
check(len(d5) == 44, '44 home-free A-E rows')
branches = {}
for h in 'ABCD':
    br = [r for r in d5 if r[ABCDE.index(h)] == 'E']
    fams = {r: reduce_row(r, ABCDE, 'E') for r in br}
    branches[h] = br
    nrec = sum(1 for r in br if fams[r][0] == 'reciprocal')
    check(len(br) == 11 and nrec == 2, f'E at {h}: {len(br)} rows, {nrec} reciprocal')
    for r in br:
        f, hs, sr = fams[r]
        assert restore(f, hs, sr, ABCDE, 'E', h) == r
check(sum(len(b) for b in branches.values()) == 44, 'branches disjoint and pool to 44')
g9 = GUIDE[8]
for h in 'ABCD':
    m = re.search(r'^' + h + r'\s+((?:[A-E]{5}, )[A-E]{5})\s+((?:[A-E]{5}, )+[A-E]{5})\s*$', g9, re.M)
    if not m:
        check(False, f'guide P9 row {h} not parsed')
        continue
    gr, gl9 = m.group(1).split(', '), m.group(2).split(', ')
    br = branches[h]
    want_r = sorted(r for r in br if reduce_row(r, ABCDE, 'E')[0] == 'reciprocal')
    want_l = sorted(r for r in br if reduce_row(r, ABCDE, 'E')[0] == 'longer')
    check(gr == want_r and gl9 == want_l, f'guide P9 branch {h}: reciprocal {gr}, longer {len(gl9)} rows')

# recurrence and its bijection for every n, z, h up to 7
D = [sum(1 for r in derangements(''.join(chr(65 + i) for i in range(n)))) if n else 1 for n in range(8)]
say('D_0..D_7 by enumeration:', D)
check(D[:6] == [1, 0, 1, 2, 9, 44], 'D0..D5 = 1,0,1,2,9,44')
check(all(D[n] == (n - 1) * (D[n - 1] + D[n - 2]) for n in range(2, 8)), 'D_n = (n-1)(D_{n-1}+D_{n-2}) for 2<=n<=7')
check(all(D[n] == sum((-1) ** k * math.comb(n, k) * math.factorial(n - k) for k in range(n + 1)) for n in range(8)),
      'inclusion-exclusion formula for 0<=n<=7')
bad = 0
for n in range(2, 7):
    L = ''.join(chr(65 + i) for i in range(n))
    dn = derangements(L)
    for z in L:
        for h in L:
            if h == z:
                continue
            br = [r for r in dn if arrows(r, L)[z] == h]
            imgs = [reduce_row(r, L, z) for r in br]
            nr = sum(1 for f in imgs if f[0] == 'reciprocal')
            if not (nr == D[n - 2] and len(br) - nr == D[n - 1] and len(set(imgs)) == len(imgs)):
                bad += 1
            for r, (f, hs, sr) in zip(br, imgs):
                if restore(f, hs, sr, L, z, h) != r or matches(sr, hs):
                    bad += 1
check(bad == 0, 'two-family deletion is a bijection for every n<=6, card z and destination h')
check('Dn = (n − 1)(Dn−1 + Dn−2 ),     n ≥ 2,   D0 = 1,    D1 = 0.' in GUIDE[0], 'guide overview recurrence and base cases')

# ---------------------------------------------------------------- preparation arithmetic
say('\n== Guide preparation arithmetic (p. 3)')
pieces = 5 * (10 + 2) + 5 * (6 + 5 + 12) + 2 * 24
check(pieces == 223 and 5 + 5 + 2 == 12, f'cut pieces {pieces}, sheets 12')
check(24 * 56 * 27 == 36288 and 173 * 95 < 36288 and 173 * 97 < 36288, 'outcome area 36,288 mm^2 exceeds both boxes')
check(4 * 12 >= 44 and 16 >= 11, '48 blank records for 44 rows; 16 writing rows for an 11-row branch')

say('\nFAILURES:', len(FAIL))
for f in FAIL:
    say('  ' + f)
open(_os.path.join(HERE, 'out_check_math.txt'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
