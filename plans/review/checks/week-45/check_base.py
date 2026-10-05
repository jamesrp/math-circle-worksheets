"""Independent check of the Week 45 base packet (K-1, 2-3, 4-5) and its adult
guide by exact enumeration.

The card catalogue (face colours and which faces share a card) is read from
pdf_geometry.json, i.e. from the diagrams in the delivered PDFs (run
pdf_extract.py first).  Every answer is computed here and then compared with
the statements printed in the delivered guide.  Output saved as
check_base.out.
"""
import json
import os
import random
import re
import sys
from fractions import Fraction as F
from itertools import combinations, product

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, PDFS, Log  # noqa: E402

log = Log()
geo = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))
cat = geo['catalogue']['k-1']
COL = {int(k): v for k, v in cat['colour'].items()}
PART = {int(k): v for k, v in cat['partner'].items()}
T = sorted(COL)
SHOW = COL
HIDE = {t: COL[PART[t]] for t in T}
CARDS = sorted({tuple(sorted((t, PART[t]))) for t in T})
CARDNAME = {c: ''.join(sorted(COL[t] for t in c)[::-1]) for c in CARDS}  # RR, RB, BB
log.note(f'model from PDF diagrams: show {SHOW}; hide {HIDE}; cards {CARDNAME}')

guide = ''.join(p.get_text() for p in pymupdf.open(PDFS['guide']))
g = re.sub(r'\s+', ' ', guide)


def section(start, end):
    i = g.find(start)
    j = g.find(end, i + len(start)) if end else len(g)
    return g[i:j]


def counts(cup, shown):
    """Number of equally likely tickets in the cup giving `shown`, split by hidden colour."""
    r = sum(1 for t in cup if SHOW[t] == shown and HIDE[t] == 'R')
    b = sum(1 for t in cup if SHOW[t] == shown and HIDE[t] == 'B')
    return r, b


def cond(cup, shown):
    r, b = counts(cup, shown)
    if r + b == 0:
        return None
    return F(r, r + b), F(b, r + b)


def tie(cup, shown):
    r, b = counts(cup, shown)
    return r == b and r > 0


def fs(s):
    return '{' + ','.join(map(str, sorted(s))) + '}'


ALL = set(T)

# ------------------------------------------------------------------ guide overview
log.check(CARDNAME == {(1, 2): 'RR', (3, 4): 'RB', (5, 6): 'BB'}, 'guide: "RR has faces 1 and 2; RB has faces 3 and 4; BB has faces 5 and 6"')
tab = re.search(r'Ticket Showing color Hidden color (.*?) If the only', g).group(1)
rows = re.findall(r'(1 or 2|3|4|5 or 6) ([RB]) ([RB])', tab)
ok = True
for lab, s, h in rows:
    for t in map(int, re.findall(r'\d', lab)):
        ok &= SHOW[t] == s and HIDE[t] == h
log.check(ok and len(rows) == 4, f'guide overview table {rows} matches the diagram model')
log.check(cond(ALL, 'R') == (F(2, 3), F(1, 3)) and 'P(hidden red | showing red) = 2/3' in g,
          'guide: P(hidden red | red showing) = 2/3')
log.check(cond(ALL, 'B') == (F(1, 3), F(2, 3)), 'guide: given blue showing, hidden blue 2/3')
# card weights after a red clue
w = {CARDNAME[c]: sum(1 for t in c if SHOW[t] == 'R') for c in CARDS}
log.check(w == {'RR': 2, 'RB': 1, 'BB': 0}, f'guide: after a red clue RR has two eligible faces, RB one {w}')
log.check(cond({1, 3}, 'R') == (F(1, 2), F(1, 2)), 'guide: chooser {1,3} gives 1/2 each')

# exact design condition over ALL 64 subsets
fair = [set(s) for k in range(1, 7) for s in combinations(T, k) if tie(set(s), 'R')]
charac = [s for s in (set(c) for k in range(1, 7) for c in combinations(T, k))
          if 3 in s and len(s & {1, 2}) == 1]
log.check(sorted(map(sorted, fair)) == sorted(map(sorted, charac)),
          'guide: fair red clue <=> 3 present and exactly one of 1,2 (checked over all 63 non-empty subsets)')
log.check(len(fair) == 16 and '2 × 2³ = 16' in g, f'guide: 16 fair subsets ({len(fair)})')
two = [s for s in fair if len(s) == 2]
log.check(len(two) == 2, f'guide: only two fair subsets are two-ticket cups {list(map(fs, two))}')
card_sets = [set().union(*cs) for k in range(1, 4) for cs in combinations(CARDS, k)]
log.check(not any(tie(s, 'R') for s in card_sets), 'guide: no whole-card selection is fair')
log.check(all(cond(s, 'R') is not None or s == {5, 6} for s in card_sets),
          'only the BB-only card selection never shows red')

# ------------------------------------------------------------------ K-1
log.note('--- K-1')
hr = sorted(t for t in T if HIDE[t] == 'R')
hb = sorted(t for t in T if HIDE[t] == 'B')
log.check(hr == [1, 2, 4] and hb == [3, 5, 6], f'K-1 P1: red underneath {hr}, blue underneath {hb}')
pairs = [p for p in combinations(T, 2) if SHOW[p[0]] == SHOW[p[1]] and HIDE[p[0]] != HIDE[p[1]]]
log.check(pairs == [(1, 3), (2, 3), (4, 5), (4, 6)], f'K-1 P1: same shown, different hidden pairs {pairs} (guide: four unordered pairs)')
s = section('K to 1 answer key Problem 1', 'Problem 2')
log.check('Hidden red: tickets 1, 2, 4. Hidden blue: 3, 5, 6.' in s and 'four unordered pairs' in s, 'guide K-1 P1 text agrees')

r, b = counts(ALL, 'R')
rem = [t for t in T if tie(ALL - {t}, 'R')]
log.check((r, b) == (2, 1) and rem == [1, 2], f'K-1 P2: red showing gives hidden R {r} vs B {b}; tie removals {rem}')
eff = {t: counts(ALL - {t}, 'R') for t in T}
log.note(f'K-1 P2: red-clue counts after each removal {eff}')
s = section('Problem 2 Given red', 'Problem 3')
log.check('Removing 1 or 2 makes a tie' in s and 'Removing 3 leaves only hidden red' in s
          and eff[3] == (2, 0) and all(eff[t] == (2, 1) for t in (4, 5, 6)), 'guide K-1 P2 text agrees')
rem = [t for t in T if tie(ALL - {t}, 'B')]
eff = {t: counts(ALL - {t}, 'B') for t in T}
log.check(counts(ALL, 'B') == (1, 2) and rem == [5, 6], f'K-1 P3: blue showing hidden R/B {counts(ALL, "B")}; tie removals {rem}')
s = section('Problem 3 Restore', 'Problem 4')
log.check('Remove 5 or 6 to make a tie' in s and eff[4] == (0, 2) and all(eff[t] == (1, 2) for t in (1, 2, 3)),
          'guide K-1 P3 text agrees')

base = {1, 3}
log.check(all(SHOW[t] == 'R' for t in base), 'K-1 P4: chooser tickets 1 and 3 both name red faces, so the chooser always shows red')
res = {x: counts(base | {x}, 'R') for x in (2, 4, 5, 6)}
log.check(counts(base, 'R') == (1, 1) and res == {2: (2, 1), 4: (1, 1), 5: (1, 1), 6: (1, 1)},
          f'K-1 P4: before tie 1-1; after adding x: {res}')
allr = {x: (sum(HIDE[t] == 'R' for t in base | {x}), sum(HIDE[t] == 'B' for t in base | {x})) for x in (2, 4, 5, 6)}
log.check(allr == {2: (2, 1), 4: (2, 1), 5: (1, 2), 6: (1, 2)},
          f'guide K-1 P4 alternative reading (all rounds): {allr} = "adding 2 or 4 favors red 2-to-1; adding 5 or 6 favors blue 2-to-1"')

sol5 = [set(c) for c in combinations(T, 3) if counts(set(c), 'R')[1] > 0 and counts(set(c), 'R')[0] == 0]
log.check(sorted(map(sorted, sol5)) == [[3, 4, 5], [3, 4, 6], [3, 5, 6]],
          f'K-1 P5: three-ticket cups with red possible and always hiding blue: {list(map(fs, sol5))} (page prints 3 slots)')
log.check('{3,4,5}, {3,4,6}, {3,5,6}' in g, 'guide K-1 P5 list agrees')

out6 = {CARDNAME[c]: counts(ALL - set(c), 'R') for c in CARDS}
log.check(out6 == {'RR': (0, 1), 'RB': (2, 0), 'BB': (2, 1)},
          f'K-1 P6: red-clue (hidden R, hidden B) after removing each card {out6}: RB removal -> always red; RR removal -> always blue')

sol7 = [set(c) for c in combinations(T, 2) if tie(set(c), 'R')]
log.check(sorted(map(sorted, sol7)) == [[1, 3], [2, 3]], f'K-1 P7: fair two-ticket cups {list(map(fs, sol7))} (page prints 2 slots)')
log.check('Exactly {1,3} and {2,3}' in g, 'guide K-1 P7 agrees')

# ------------------------------------------------------------------ 2-3
log.note('--- grades 2-3')
same = [t for t in T if SHOW[t] == HIDE[t]]
log.check(same == [1, 2, 5, 6], f'2-3 P1: tickets with the same colour on both faces {same}')
tab = re.findall(r'(\d) ([RB]) ([RB]) (Yes|No)', section('Grades 2 to 3 answer key', 'Thus tickets'))
log.check(len(tab) == 6 and all(SHOW[int(t)] == s and HIDE[int(t)] == h and (y == 'Yes') == (s == h) for t, s, h, y in tab),
          'guide 2-3 P1 table agrees')
log.check(cond(ALL, 'R') == (F(2, 3), F(1, 3)), '2-3 P2: red showing -> red is better guess, 2/3')
log.check(cond(ALL, 'B') == (F(1, 3), F(2, 3)), '2-3 P3: blue showing -> blue is better guess, 2/3 (the guess changes colour; "guess the showing colour" is the same rule)')
log.check(cond(base, 'R')[0] == F(1, 2) != cond(ALL, 'R')[0], '2-3 P4: two-ticket chooser 1/2 vs six-ticket 2/3: not the same')
res = {CARDNAME[c]: cond(ALL - set(c), 'R') for c in CARDS}
log.check(res == {'RR': (0, 1), 'RB': (1, 0), 'BB': (F(2, 3), F(1, 3))},
          f'2-3 P5: certain red (remove RB) yes; certain blue (remove RR) yes; equal chance: no {res}')
log.check(sorted(map(sorted, sol7)) == [[1, 3], [2, 3]], '2-3 P6: same as K-1 P7, {1,3} and {2,3}')
log.check('The only pairs are {1,3} and {2,3}' in g, 'guide 2-3 P6 agrees')

# ------------------------------------------------------------------ 4-5
log.note('--- grades 4-5')
log.check(cond(ALL, 'R') == (F(2, 3), F(1, 3)) and cond(ALL, 'B') == (F(1, 3), F(2, 3)), '4-5 P1: 2/3,1/3 and 1/3,2/3')
pc = {CARDNAME[c]: F(sum(1 for t in c if SHOW[t] == 'R'), sum(1 for t in T if SHOW[t] == 'R')) for c in CARDS}
log.check(pc == {'RR': F(2, 3), 'RB': F(1, 3), 'BB': 0}, f'4-5 P2: P(card | red) = {pc}; friend\'s 1/2-1/2 is wrong')
log.check(all(len({HIDE[t]}) == 1 for t in T) and [t for t in T if HIDE[t] == 'R'] == [1, 2, 4],
          '4-5 P3: a revealed mark determines the hidden colour (1,2,4 red; 3,5,6 blue)')
log.check(cond(base, 'R')[0] == F(1, 2) and cond(ALL, 'R')[0] == F(2, 3), '4-5 P4: 1/2 vs 2/3')
pa, pb = cond(ALL, 'R')[0], cond(base, 'R')[0]
seqs = list(product('RB', repeat=6))
both = all((pa ** s.count('R')) * ((1 - pa) ** s.count('B')) > 0 and (pb ** s.count('R')) * ((1 - pb) ** s.count('B')) > 0 for s in seqs)
log.check(both, '4-5 P5: all 64 six-round hidden-colour sequences have positive probability under both rules -> no proof possible')
log.check(pa ** 6 == F(64, 729) and pb ** 6 == F(1, 64) and '(2/3)6 and (1/2)6' in g,
          f'guide 4-5 P5: six hidden reds have probabilities (2/3)^6={float(pa**6):.4f} and (1/2)^6={float(pb**6):.4f}')
log.check(len(fair) == 16, '4-5 P6: 16 fair subsets')
Tlist = re.search(r'Explicitly T may be (.*?)\. These', g).group(1)
Ts = [set(map(int, re.findall(r'\d', x))) for x in re.findall(r'∅|\{[\d,]+\}', Tlist)]
fam = [set(a) | t for a in ({1, 3}, {2, 3}) for t in Ts]
log.check(len(Ts) == 8 and len({frozenset(x) for x in Ts}) == 8 and all(t <= {4, 5, 6} for t in Ts),
          f'guide 4-5 P6: T list has the 8 subsets of {{4,5,6}}')
log.check(sorted(map(sorted, fam)) == sorted(map(sorted, fair)), 'guide 4-5 P6: the two families give exactly the 16 fair subsets, without repeats')
log.check(not any(tie(s, 'R') for s in card_sets), '4-5 P7: no whole-card selection (1, 2 or 3 cards) gives a fair red clue')
for s in card_sets:
    log.note(f'  4-5 P7 keep {sorted(CARDNAME[c] for c in CARDS if set(c) <= s)}: red-clue (hidden R, hidden B) = {counts(s, "R")}')

# ------------------------------------------------------------------ physical-protocol simulation
log.note('--- simulation of the printed protocol (draw ticket, set named face up, read the other face)')
rng = random.Random(45)


def simulate(cup, n=60000):
    cup = sorted(cup)
    shown_r = hid_r = 0
    for _ in range(n):
        t = rng.choice(cup)
        if COL[t] == 'R':
            shown_r += 1
            hid_r += COL[PART[t]] == 'R'
    return hid_r / shown_r


s6, s2 = simulate(ALL), simulate(base)
log.check(abs(s6 - 2 / 3) < 0.01 and abs(s2 - 0.5) < 0.01, f'simulation: six-ticket {s6:.3f} (~2/3), chooser {{1,3}} {s2:.3f} (~1/2)')

log.summary()
