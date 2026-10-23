#!/usr/bin/env python3
"""Independent mathematical check of Week 87 (Voting and agendas).

Written for the review; does not import or run the package's own
check_math.py.  The printed data below were read off the rendered student
pages and cross-checked against the PDF text/vectors by check_diagrams.py.

Covers:
  shared  : worked D/E/F example, Problem 1 cycle, Problem 2 agendas,
            Problem 3 (all 3-card profiles, distinct and not).
  line    : launch example, Problems 1-4 on the ticks AND on a fine real grid,
            all 3003 five-favorite multisets (Problem 3), alternative
            readings, guide counts.
  upper   : Problem 1 two profiles, Problem 2 single-peakedness obstruction
            (proof by cases + brute-force search over placements).
  guide   : every numeric claim in the facilitator overview/solutions.
Run: python3 check_math.py   (writes check_math.py.out beside itself)
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, permutations, product
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
OUT = []
FAILS = []


def say(s=''):
    OUT.append(s)
    print(s)


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


# ---------------------------------------------------------------- cards
def pair(cards, a, b):
    """Majority vote between a and b; each card votes for whichever is higher."""
    va = sum(c.index(a) < c.index(b) for c in cards)
    vb = len(cards) - va
    return (a if va > vb else b if vb > va else None), va, vb


def knockout(cards, first, wait):
    w1 = pair(cards, *first)[0]
    if w1 is None:
        return None
    return pair(cards, w1, wait)[0]


def all_agendas(cards, letters='ABC'):
    res = {}
    for wait in letters:
        a, b = [x for x in letters if x != wait]
        res[wait] = (knockout(cards, (a, b), wait), knockout(cards, (b, a), wait))
    return res


def condorcet(cards, letters='ABC'):
    return [x for x in letters if all(pair(cards, x, y)[0] == x for y in letters if y != x)]


say('=== Shared packet ===')
ex = ['DFE', 'EFD', 'FED']
w, va, vb = pair(ex, 'D', 'E')
check((w, va, vb) == ('E', 1, 2), f'worked example D vs E -> {w} {va}-{vb} (page: V1 D, V2 E, V3 E; E wins 2 to 1)')
check([c for c in ex if c.index('D') < c.index('E')] == ['DFE'], 'only V1 chooses D')
w2 = pair(ex, 'E', 'F')
check(w2 == ('F', 1, 2), f'knockout example E vs F -> {w2[0]} {w2[2]}-{w2[1]} (page: F wins; guide: V1/V3 F, V2 E)')
check([i + 1 for i, c in enumerate(ex) if c.index('F') < c.index('E')] == [1, 3], 'V1 and V3 choose F over E')

P1 = ['ABC', 'BCA', 'CAB']
for a, b in [('A', 'B'), ('B', 'C'), ('C', 'A')]:
    r = pair(P1, a, b)
    voters = [i + 1 for i, c in enumerate(P1) if c.index(a) < c.index(b)]
    say(f'     P1 {a} vs {b}: winner {r[0]} {max(r[1:])}-{min(r[1:])}, voters for {a}: V{voters}')
check(condorcet(P1) == [], 'shared P1: no letter beats both others (answer: no)')
check([pair(P1, 'A', 'B')[0], pair(P1, 'B', 'C')[0], pair(P1, 'C', 'A')[0]] == ['A', 'B', 'C'],
      'shared P1 cycle A>B, B>C, C>A, each 2-1 (guide overview)')
ag = all_agendas(P1)
for wait in 'ABC':
    say(f'     P2 waiting {wait}: winner {ag[wait]} (both orders of first pair)')
check(all(ag[x] == (x, x) for x in 'ABC'), 'shared P2: the waiting letter always wins; A, B, C each possible; order within pair irrelevant')
check(knockout(P1, ('B', 'C'), 'A') == 'A' and pair(P1, 'B', 'C')[0] == 'B', 'guide P2: B/C first, B wins, A beats B')
check(knockout(P1, ('C', 'A'), 'B') == 'B' and pair(P1, 'C', 'A')[0] == 'C', 'guide P2: C/A first, C wins, B beats C')
check(knockout(P1, ('A', 'B'), 'C') == 'C' and pair(P1, 'A', 'B')[0] == 'A', 'guide P2: A/B first, A wins, C beats A')

# Problem 3: every profile of three cards
RANKS = [''.join(p) for p in permutations('ABC')]
say('     Problem 3: all sets of three DIFFERENT cards (20 sets):')
same, diff = [], []
for S in combinations(RANKS, 3):
    winners = {ag[0] for ag in all_agendas(list(S)).values()} | {ag[1] for ag in all_agendas(list(S)).values()}
    (same if len(winners) == 1 else diff).append(S)
say(f'       same winner every knockout: {len(same)} sets; waiting letter can change winner: {len(diff)} sets')
say(f'       the agenda-dependent sets: {diff}')
check(len(same) == 18 and len(diff) == 2, '18 sets have one winner for every agenda; exactly 2 sets are agenda-dependent')
check(set(map(frozenset, diff)) == {frozenset(P1), frozenset(['ACB', 'CBA', 'BAC'])},
      'the only agenda-dependent sets are Problem 1\'s cards {ABC,BCA,CAB} and its mirror {ACB,CBA,BAC}')
# with repeats allowed (ordered multisets) -- cyclic profiles are still only those two
cyc_ms = set()
for prof in product(RANKS, repeat=3):
    if not condorcet(list(prof)):
        cyc_ms.add(tuple(sorted(prof)))
check(cyc_ms == {tuple(sorted(P1)), tuple(sorted(['ACB', 'CBA', 'BAC']))},
      'even allowing repeated cards, every 3-voter cycle uses exactly those two card sets')
check(all(len(set(S)) == 3 for S in cyc_ms), 'so the "three different cards" condition is automatic for the agenda-dependent set')
# any Condorcet winner => same winner, any cycle => waiting wins (3 voters, strict)
ok = True
for prof in product(RANKS, repeat=3):
    cw = condorcet(list(prof))
    ag3 = all_agendas(list(prof))
    if cw:
        ok &= all(v == (cw[0], cw[0]) for v in ag3.values())
    else:
        ok &= all(v == (k, k) for k, v in ag3.items())
check(ok, 'all 216 three-voter profiles: Condorcet winner wins every agenda; otherwise the waiting letter wins')
G3 = ['ABC', 'ACB', 'BAC']
check(pair(G3, 'A', 'B')[1:] == (2, 1) and pair(G3, 'A', 'C')[1:] == (3, 0), 'guide P3 example ABC,ACB,BAC: A beats B 2-1 and C 3-0')
check(all(v == ('A', 'A') for v in all_agendas(G3).values()), 'guide P3 example: A wins every agenda')

say()
say('=== Upper packet ===')
U1a = ['ABC', 'ACB', 'BAC']
U1b = ['ACB', 'CBA', 'BAC']
check(condorcet(U1a) == ['A'] and all(v == ('A', 'A') for v in all_agendas(U1a).values()),
      'upper P1 set 1: A beats B and C, waiting letter never changes the winner')
check(pair(U1a, 'B', 'C')[0:3] == ('B', 2, 1), 'guide: in set 1 B beats C 2-1')
check(pair(U1b, 'B', 'A')[0] == 'B' and pair(U1b, 'A', 'C')[0] == 'A' and pair(U1b, 'C', 'B')[0] == 'C'
      and all(max(pair(U1b, x, y)[1:]) == 2 for x, y in [('A', 'B'), ('A', 'C'), ('B', 'C')]),
      'upper P1 set 2: B>A, A>C, C>B, each 2-1 (guide)')
ag = all_agendas(U1b)
check(all(ag[x] == (x, x) for x in 'ABC'), 'upper P1 set 2: waiting letter always wins (guide lists A/C->B, B/C->A, A/B->C)')
check(knockout(U1b, ('A', 'C'), 'B') == 'B' and knockout(U1b, ('B', 'C'), 'A') == 'A' and knockout(U1b, ('A', 'B'), 'C') == 'C',
      'guide agendas for set 2 verified')

# Upper page 2 worked conversion: favorite 1, D=0, E=4, F=9
fav, locs = 1, {'D': 0, 'E': 4, 'F': 9}
dist = {k: abs(v - fav) for k, v in locs.items()}
check(dist == {'D': 1, 'E': 3, 'F': 8}, f'upper p2 example distances {dist} (page: 1, 3, 8 steps)')
check(''.join(sorted(locs, key=dist.get)) == 'DEF', 'upper p2 example card DEF')


def ranking(fav, locs):
    d = {k: abs(v - fav) for k, v in locs.items()}
    if len(set(d.values())) < 3:
        return None  # tie -> no strict ranking
    return ''.join(sorted(d, key=d.get))


# Upper P2: realizable rankings for every placement; brute force
grid = [F(k, 4) for k in range(-8, 49)]   # -2 .. 12 in quarter steps
real_sets = set()
found = False
cand = [F(k, 2) for k in range(0, 21)]   # candidate spots 0..10 in half steps
for a, b, c in permutations(cand, 3):
    locs = {'A': a, 'B': b, 'C': c}
    rs = {ranking(p, locs) for p in grid} - {None}
    real_sets.add(frozenset(rs))
    if set(P1) <= rs:
        found = True
check(not found, f'upper P2 brute force: no placement of distinct A,B,C on half-ticks 0..10 with favorites on quarter grid -2..12 gives all of ABC,BCA,CAB')
check(max(len(s) for s in real_sets) == 4, 'any placement realizes at most 4 of the 6 strict rankings (never the two with the middle letter last)')
ok = True
for order in permutations('ABC'):
    mid = order[1]
    ok &= any(card[-1] == mid for card in P1)
check(ok, 'proof by cases: for each of the 6 orders of A,B,C on the line, the middle letter is last on one of the cards')
# proof of the lemma over exact rationals, wide grid
ok = True
for l, m, r in combinations([F(k, 3) for k in range(-6, 37)], 3):
    for p in grid:
        ok &= (abs(p - m) < max(abs(p - l), abs(p - r)))
check(ok, 'lemma: for l<m<r and any favorite p (incl. outside [l,r]), m is strictly nearer than some extreme')

say()
say('=== Line packet ===')


def votes(favs, x, y):
    vx = sum(abs(p - x) < abs(p - y) for p in favs)
    vy = sum(abs(p - y) < abs(p - x) for p in favs)
    return vx, vy, len(favs) - vx - vy


lv = votes([0, 1, 5, 8, 10], 2, 8)
per = []
for p in [0, 1, 5, 8, 10]:
    dx, dy = abs(p - 2), abs(p - 8)
    per.append((dx, dy, 'X' if dx < dy else 'Y' if dy < dx else 'Tie'))
check(per == [(2, 8, 'X'), (1, 7, 'X'), (3, 3, 'Tie'), (6, 0, 'Y'), (8, 2, 'Y')], f'line launch per-voter table {per}')
check(lv == (2, 2, 1), 'line launch: 2 to 2 with V3 in Tie (tied vote)')

TICKS = list(range(11))
FINE = [F(k, 8) for k in range(-16, 97)]   # -2 .. 12 in eighth steps (off-board too)


def strict_winners(favs, pts):
    return [x for x in pts if all(votes(favs, x, y)[0] > votes(favs, x, y)[1] for y in pts if y != x)]


def weak_winners(favs, pts):
    return [x for x in pts if all(votes(favs, x, y)[0] >= votes(favs, x, y)[1] for y in pts if y != x)]


P1L = [0, 2, 4, 7, 10]
check(strict_winners(P1L, TICKS) == [4], 'line P1 (0,2,4,7,10): 4 is the only tick beating every other tick')
check(strict_winners(P1L, FINE) == [4], 'line P1: 4 is also the only strict winner on a fine real grid -2..12')
tab = {q: votes(P1L, 4, q) for q in TICKS if q != 4}
say(f'     line P1 counts for 4 vs q (for 4, for q, tie): {tab}')
check(tab[0] == (3, 1, 1) and tab[10] == (3, 1, 1), 'guide: vs 0 and vs 10 the count is 3-1 with one Tie')
check(all(tab[q] == (3, 2, 0) for q in [1, 2, 3, 5, 6, 7, 8, 9]), 'guide: vs 1,2,3,5,6,7,8,9 the count is 3-2')
check(abs(2 - 0) == abs(2 - 4) and abs(7 - 4) == abs(7 - 10), 'guide: voter at 2 ties for 0 vs 4; voter at 7 ties for 4 vs 10')

for favs, ans in [([0, 0, 0, 8, 10], 0), ([1, 4, 4, 4, 9], 4), ([0, 1, 6, 9, 10], 6)]:
    check(strict_winners(favs, TICKS) == [ans] and strict_winners(favs, FINE) == [ans],
          f'line P2 {favs}: unique strict winner {ans} (ticks and fine grid)')
check(sum([0, 1, 6, 9, 10]) == 26, 'guide: mean of 0,1,6,9,10 is 26/5 (midpoint 5, median 6)')
check(votes([0, 1, 6, 9, 10], 6, 5)[:2] == (3, 2), '6 beats the board midpoint 5, 3-2')
# Reading "share a favorite" as one voter would change the answer in set 1 and 2
check(strict_winners([0, 8, 10], TICKS) == [8], 'wrong reading check: if the three voters at 0 counted once, the winner would be 8 (page guards against this)')
check(strict_winners([1, 4, 9], TICKS) == [4], '  (set 2 would still give 4)')

# Problem 3: every multiset of five favorites on the ticks
n = bad = 0
other = 0
min_margin = 9
fine_bad = 0
for fs in combinations_with_replacement(TICKS, 5):
    n += 1
    m = fs[2]
    sw = strict_winners(fs, TICKS)
    if sw != [m]:
        bad += 1
    for q in TICKS:
        if q != m:
            vx, vy, _ = votes(fs, m, q)
            min_margin = min(min_margin, vx)
check(n == 3003, f'line P3: {n} five-favorite multisets on 11 ticks (guide says 3,003)')
check(bad == 0, 'line P3: in every multiset the third favorite from the left is the unique strict winner among ticks')
check(min_margin >= 3, f'line P3: the median always gets at least 3 strict votes (min {min_margin})')
# fine grid / off-board opponents, sampled over all multisets with integer favorites
for fs in combinations_with_replacement(TICKS, 5):
    m = fs[2]
    for q in FINE[::3]:
        if q != m and votes(fs, m, q)[0] < 3:
            fine_bad += 1
check(fine_bad == 0, 'line P3: median also beats every non-tick / off-board opponent on a 3/8 grid -2..12')
# Alternative reading: third DISTINCT position
fails = [fs for fs in combinations_with_replacement(TICKS, 5)
         if len(set(fs)) >= 3 and strict_winners(fs, TICKS) != [sorted(set(fs))[2]]]
say(f'     (reading "third favorite" as third distinct place would fail in {len(fails)} sets, e.g. {fails[0]}; the page\'s "Count all five markers" excludes it)')

# Problem 4: four voters 1,3,7,9
P4 = [1, 3, 7, 9]
check(weak_winners(P4, TICKS) == [3, 4, 5, 6, 7], 'line P4: ticks that never lose = 3,4,5,6,7')
check(strict_winners(P4, TICKS) == [], 'line P4: no tick beats every other')
wf = weak_winners(P4, FINE)
check(min(wf) == 3 and max(wf) == 7 and all(F(3) <= x <= 7 for x in wf) and len(wf) == 33,
      'line P4: on the real grid the never-losing set is exactly [3,7] (guide)')
check(all(votes(P4, x, y)[:2] == (2, 2) for x, y in combinations([F(k, 8) for k in range(24, 57)], 2)),
      'guide: any two distinct locations in [3,7] split 2-2')
check(all(votes(P4, 3, q)[0] >= 3 for q in [0, 1, 2]) and all(votes(P4, 7, q)[0] >= 3 for q in [8, 9, 10]),
      'guide: ticks below 3 lose to 3 (voters 3,7,9) and above 7 lose to 7 (voters 1,3,7)')
check(votes(P4, 3, 8) == (2, 2, 0) and votes(P4, 7, 2) == (2, 2, 0), 'example ties: 3 vs 8 and 7 vs 2 are 2-2 (ties elsewhere too)')
check(votes(P4, 7, 8)[0] == 3, 'guide: "there are still winning comparisons elsewhere" (7 beats 8, 3-1)')
check(len(list(combinations(TICKS, 2))) == 55, 'guide: 55 pairs of tick locations')

say()
say('=== Materials geometry claimed in guide (from source coordinates, mm) ===')
targets = [(11, 11), (43, 11), (27, 27), (11, 43), (43, 43)]
r = 9
clear_edge = min(min(x - r, 54 - x - r, y - r, 54 - y - r) for x, y in targets)
gaps = [((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5 - 2 * r for a, b in combinations(targets, 2)]
check(clear_edge == 2, f'tally well: 18 mm targets have 2 mm boundary clearance ({clear_edge})')
check(abs(min(gaps) - 4.627) < 0.001, f'tally well: min gap between placed tokens {min(gaps):.3f} mm (guide: at least 4.6 mm)')

say()
say(f'{len(FAILS)} failures')
(HERE / 'check_math.py.out').write_text('\n'.join(OUT) + '\n')
sys.exit(1 if FAILS else 0)
