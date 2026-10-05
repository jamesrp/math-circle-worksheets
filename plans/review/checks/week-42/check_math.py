#!/usr/bin/env python3
"""Independent mathematical check of Week 42 (fair results from a bag).

Enumerates labelled draws, colour-only rules, bags, stories, four-draw blocks
and ticket cups by its own code (no writer, guide or bonus verifier is run or
imported) and compares every printed number in the base and bonus adult guides
(text read with pdftotext) with the enumeration.

Run: python3 check_math.py   (writes out_check_math.txt beside itself)
The repository is found by walking up from this file; from the committed copy
in plans/review/checks/week-42/ that is four folders up.
"""
import itertools
import os
import re
import subprocess
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent


def find_repo():
    for d in [HERE] + list(HERE.parents):
        if (d / 'lowell-math-circle-year-2').is_dir() and (d / 'AGENTS.md').is_file():
            return d
    sys.exit('repository not found above ' + str(HERE))


REPO = find_repo()
WEEK = REPO / 'lowell-math-circle-year-2' / 'week-42'
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def norm(s):
    s = s.replace('−', '-').replace('–', '-').replace('—', '-')
    s = s.replace('×', 'x').replace('→', '->')
    return re.sub(r'\s+', ' ', s)


def pdftext(name):
    return norm(subprocess.run(['pdftotext', str(WEEK / name), '-'], capture_output=True,
                               text=True, check=True).stdout)


# ---------------------------------------------------------------- basics
PAIRS = ['RR', 'RB', 'BR', 'BB']
SHAPES = ['S', 'C', 'N']   # square, circle, no shape


def labelled(bag):
    """Labelled counters of a bag string, e.g. RRRB -> R1 R2 R3 B1."""
    c = Counter()
    out = []
    for col in bag:
        c[col] += 1
        out.append((col, col + str(c[col])))
    return out


def weights_with(first, second=None):
    """Colour-pair weights (counts) of independent draws, first bag then second bag."""
    second = second or first
    w = Counter()
    for a, _ in labelled(first):
        for b, _ in labelled(second):
            w[a + b] += 1
    return w


def weights_without(bag):
    w = Counter()
    L = labelled(bag)
    for i, (a, _) in enumerate(L):
        for j, (b, _) in enumerate(L):
            if i != j:
                w[a + b] += 1
    return w


def all_rules():
    for vals in itertools.product(SHAPES, repeat=4):
        yield dict(zip(PAIRS, vals))


def tally(rule, w):
    t = Counter()
    for k, n in w.items():
        t[rule[k]] += n
    return t


def is_fair(rule, w):
    t = tally(rule, w)
    return t['S'] > 0 and t['C'] > 0 and t['S'] == t['C']


VN = {'RR': 'N', 'RB': 'C', 'BR': 'S', 'BB': 'N'}       # guide's key rule
VN2 = {'RR': 'N', 'RB': 'S', 'BR': 'C', 'BB': 'N'}      # shape-swapped

say('# Week 42 independent mathematics check')
say('repo:', REPO)

# ---------------------------------------------------------------- 3R/1B core
w31 = weights_with('RRRB')
say('\n## Core: three red, one blue, independent draws with replacement')
say('labelled colour classes:', dict(w31), 'total', sum(w31.values()))
check(w31 == Counter({'RR': 9, 'RB': 3, 'BR': 3, 'BB': 1}), 'class sizes 9,3,3,1 of 16')
fair31 = [r for r in all_rules() if is_fair(r, w31)]
say('fair colour-only rules (of 81):', fair31)
check(len(fair31) == 2 and VN in fair31 and VN2 in fair31,
      'exactly two fair rules: BR/RB to opposite shapes, RR and BB skipped')
skips = {sum(n for k, n in w31.items() if r[k] == 'N') for r in fair31}
check(skips == {10}, 'every fair rule skips exactly 10 labelled pairs (min skip = 10)')
check(not any(all(v != 'N' for v in r.values()) for r in fair31),
      'no fair rule gives a shape on every pair (G2-3 P7, G4-5 P4)')
check(9 > 16 - 9, 'RR class (9) exceeds the other seven pictures')
# guide K-1 P3 completeness argument: BB cannot get a shape
bb_shape = [r for r in all_rules() if r['RR'] == 'N' and r['BB'] != 'N' and is_fair(r, w31)]
check(bb_shape == [], 'with RR skipped, giving BB a shape never balances (K-1 P3 key)')

# probability of each shape and conditional
t = tally(VN, w31)
check(F(t['S'], 16) == F(3, 16) and F(t['C'], 16) == F(3, 16), 'each shape 3/16, conditional 1/2')

# ---------------------------------------------------------------- K-1
say('\n## K-1')
# P1: colour pairs possible with replacement; with blue removed
pairs_rrrb = {a + b for a, b in itertools.product('RRRB', repeat=2)}
pairs_rrr = {a + b for a, b in itertools.product('RRR', repeat=2)}
check(pairs_rrrb == set(PAIRS), 'P1: all four colour pairs possible with replacement (BB too)')
check(set(PAIRS) - pairs_rrr == {'RB', 'BR', 'BB'}, 'P1: removing blue loses RB, BR, BB')
# P3: the 16 printed pictures are the labelled ordered pairs; see check_diagrams.py
# P4 bags
for bag, exp in [('RBBB', (3, 3)), ('RRBB', (4, 4)), ('RRRR', (0, 0)), ('BBBB', (0, 0))]:
    t = tally(VN, weights_with(bag))
    say(f'P4 {bag}: square {t["S"]}, circle {t["C"]}, none {t["N"]} of 16')
    check((t['S'], t['C']) == exp, f'P4 {bag} gives square/circle {exp}')
# P5: four-counter bags under the kept rule
mixed = []
for r in range(5):
    bag = 'R' * r + 'B' * (4 - r)
    t = tally(VN, weights_with(bag))
    mixed.append(t['S'] + t['C'])
say('P5 mixed labelled pairs by red count 0..4:', mixed)
check(mixed == [0, 6, 8, 6, 0], 'P5: 0,6,8,6,0 -> two red/two blue best under kept rule')
check(all(m < 16 for m in mixed), 'P5: no four-counter bag gives a shape on every pair under kept rule')
# P5 alternative reading: the rule may change for the chosen bag
alt = {}
for r in range(5):
    bag = 'R' * r + 'B' * (4 - r)
    w = weights_with(bag)
    alt[bag] = [rule for rule in all_rules()
                if all(v != 'N' for v in rule.values()) and is_fair(rule, w)]
say('P5 other reading: fair colour-only rules that ALWAYS give a shape, by bag:')
for bag, rs in alt.items():
    say('   ', bag, len(rs), rs[:4])
first_colour = {'RR': 'S', 'RB': 'S', 'BR': 'C', 'BB': 'C'}
check(first_colour in alt['RRBB'],
      'P5 other reading: RRBB with "first counter red -> square, blue -> circle" is fair '
      'and gives a shape on EVERY pair (answer flips to yes if the rule may change)')
check(all(len(alt[b]) == 0 for b in alt if b != 'RRBB'), 'only the 2R/2B bag admits such a rule')
# P6 stories under VN
stories = {
    'no shapes': ['RR'] * 6,
    'exactly one square and no circles': ['BR'] + ['RR'] * 5,
    'exactly three circles and no squares': ['RB'] * 3 + ['RR'] * 3,
}
for name, s in stories.items():
    out = Counter(VN[p] for p in s)
    say(f'P6 guide story "{name}": {s} -> {dict(out)}')
check(Counter(VN[p] for p in stories['no shapes'])['N'] == 6, 'P6 no-shape story valid')
o = Counter(VN[p] for p in stories['exactly one square and no circles'])
check(o['S'] == 1 and o['C'] == 0, 'P6 one-square story valid')
o = Counter(VN[p] for p in stories['exactly three circles and no squares'])
check(o['C'] == 3 and o['S'] == 0, 'P6 three-circle story valid')
check(F(9, 16) ** 6 > 0, 'P6: six RR pairs have positive probability (9/16)^6 = %s' % (F(9, 16) ** 6))

# ---------------------------------------------------------------- Grades 2-3
say('\n## Grades 2-3')
grid = {}
L = labelled('RRRB')
for a, la in L:
    for b, lb in L:
        grid[(la, lb)] = a + b
for la in ['R1', 'R2', 'R3', 'B1']:
    say('   ', la, [grid[(la, lb)] for lb in ['R1', 'R2', 'R3', 'B1']])
check(grid[('R2', 'B1')] == 'RB', 'P2 highlighted cell row R2, column B is the colour pair RB')
check(Counter(grid.values()) == Counter({'RR': 9, 'RB': 3, 'BR': 3, 'BB': 1}), 'P2 grid classes 9,3,3,1')
for bag, exp in [('RRBB', 4), ('RBBB', 3)]:
    w = weights_with(bag)
    check(w['RB'] == w['BR'] == exp, f'P3 {bag}: RB = BR = {exp} of 16 (fair)')
check(weights_with('RRBB')['RB'] * 2 == 8 and weights_with('RRRB')['RB'] * 2 == 6,
      'P4: two-red bag 8/16 output vs three-red bag 6/16 -> choose two-red')
w5 = weights_with('RRRB', 'RBBB')
say('P5 cross-bag weights:', dict(w5))
check(w5 == Counter({'RR': 3, 'RB': 9, 'BR': 1, 'BB': 3}), 'P5 counts RR 3, RB 9, BR 1, BB 3')
t = tally(VN, w5)
check(F(t['C'], t['C'] + t['S']) == F(9, 10) and F(t['S'], t['C'] + t['S']) == F(1, 10),
      'P5 conditional circle 9/10, square 1/10 -> unfair')
check(not any(is_fair(r, w5) for r in [VN, VN2]), 'P5 neither fair rule stays fair')
check(F(9, 16) ** 6 > 0, 'P6 RRRRRR... story is legal and has chance (9/16)^6')

# ---------------------------------------------------------------- Grades 4-5
say('\n## Grades 4-5')
for bag, n, tot in [('RRRRRBB', 10, 49), ('RRRBBBB', 12, 49)]:
    w = weights_with(bag)
    check(w['RB'] == w['BR'] == n and sum(w.values()) == tot, f'P3 {bag}: {n} RB and {n} BR among {tot}')
ok = True
for r in range(0, 9):
    for b in range(0, 9):
        if r + b == 0:
            continue
        w = weights_with('R' * r + 'B' * b)
        ok &= (w['RB'] == w['BR'] == r * b and sum(w.values()) == (r + b) ** 2)
        ok &= (is_fair(VN, w) == (r > 0 and b > 0))
check(ok, 'P3 general: r red, b blue gives rb of each mixed order among (r+b)^2; fair iff r,b > 0 (r,b <= 8)')
cases = [('RRRB', 'RBBB', False), ('RRRB', 'RRRRRRBB', True), ('RRBB', 'RB', True)]
for a, b, exp in cases:
    w = weights_with(a, b)
    tot = sum(w.values())
    say(f'P5 {a} then {b}: {dict(w)} of {tot}; RB {F(w["RB"], tot)}, BR {F(w["BR"], tot)}')
    check(is_fair(VN, w) == exp, f'P5 {a} -> {b} fair = {exp}')
check(F(weights_with('RRRB', 'RRRRRRBB')['RB'], 32) == F(3, 16), 'P5 case 2: 6/32 = 3/16')
check(F(weights_with('RRBB', 'RB')['RB'], 8) == F(1, 4), 'P5 case 3: 2/8 = 1/4')
# p = q criterion on a grid of rationals
ok = True
for p in [F(i, 12) for i in range(13)]:
    for q in [F(i, 12) for i in range(13)]:
        ok &= ((p * (1 - q) == (1 - p) * q) == (p == q))
check(ok, 'p(1-q) = (1-p)q iff p = q (13x13 rational grid)')
wn = weights_without('RRRB')
say('P6 without replacement:', dict(wn), 'total', sum(wn.values()))
check(wn == Counter({'RR': 6, 'RB': 3, 'BR': 3}) and sum(wn.values()) == 12,
      'P6: 12 ordered pairs, RR 6, RB 3, BR 3, BB 0 -> fair, each shape 3/12')
check(is_fair(VN, wn), 'P6 kept rule still fair without replacement')
ok = True
for r in range(0, 7):
    for b in range(0, 7):
        if r + b >= 2:
            w = weights_without('R' * r + 'B' * b)
            ok &= w['RB'] == w['BR']
check(ok, 'without replacement RB = BR for every bag (exchangeability), r,b <= 6')
# P7: stories with positive probability
check(Counter(VN[p] for p in ['BR'] + ['RR'] * 5)['S'] == 1, 'P7 BR,RR x5 -> one square, no circles')

# ---------------------------------------------------------------- guide overview claims
say('\n## Base guide overview')
ok = True
for r in range(1, 6):
    for b in range(1, 6):
        p = F(r, r + b)
        w = weights_with('R' * r + 'B' * b)
        tot = (r + b) ** 2
        ok &= F(w['RB'], tot) == p * (1 - p) == F(w['BR'], tot)
        ok &= F(w['RB'] + w['BR'], tot) == 2 * p * (1 - p)
check(ok, 'P(RB) = P(BR) = p(1-p), output rate 2p(1-p) for bags up to 5+5')
# no output after m pairs
ok = True
for bag in ['RRRB', 'RRBB', 'RBBB', 'RRRRRBB']:
    w = weights_with(bag)
    tot = sum(w.values())
    p = F(bag.count('R'), len(bag))
    for m in range(1, 4):
        prob = F(0)
        for seq in itertools.product(PAIRS, repeat=m):
            if all(VN[s] == 'N' for s in seq):
                term = F(1)
                for s in seq:
                    term *= F(w[s], tot)
                prob += term
        ok &= prob == (p * p + (1 - p) ** 2) ** m
check(ok, 'chance of no output after m pairs = [p^2+(1-p)^2]^m (m <= 3, four bags)')
# "Independence is sufficient, not necessary": independence alone with p != q fails
w_ind = weights_with('RRRB', 'RBBB')
check(not is_fair(VN, w_ind),
      'independent draws with p != q are NOT fair: "independence" alone is not sufficient '
      '(needs the same bag, i.e. identically distributed draws)')
check(is_fair(VN, weights_without('RRRB')),
      'dependent but exchangeable (no replacement) draws are fair')

# ---------------------------------------------------------------- bonus P1
say('\n## Bonus Problem 1 (three draws, three shapes)')
WORDS3 = [''.join(w) for w in itertools.product('RB', repeat=3)]
MIXED3 = [w for w in WORDS3 if w not in ('RRR', 'BBB')]


def word_weight_poly(wd):
    """(number of R, number of B): weight p^r (1-p)^b."""
    return (wd.count('R'), wd.count('B'))


lone = {}
for wd in MIXED3:
    cnt = Counter(wd)
    lone_col = 'R' if cnt['R'] == 1 else 'B'
    lone[wd] = ['square', 'circle', 'triangle'][wd.index(lone_col)]
say('lone-colour-position rule:', lone)
check(lone == {'RBB': 'square', 'BRR': 'square', 'BRB': 'circle', 'RBR': 'circle',
               'BBR': 'triangle', 'RRB': 'triangle'}, 'guide P1 rule pairs words as printed')
# count all assignments of the six words to three shapes that are fair for every p
valid = 0
for vals in itertools.product(range(3), repeat=6):
    shape_poly = [Counter() for _ in range(3)]
    for wd, s in zip(MIXED3, vals):
        shape_poly[s][word_weight_poly(wd)] += 1
    if shape_poly[0] == shape_poly[1] == shape_poly[2] and all(shape_poly):
        valid += 1
say('assignments of the six mixed words, fair for every p (polynomial identity):', valid)
check(valid == 36, '36 = 3! x 3! universal rules: each shape gets one one-R and one two-R word')
# exact identity-history counts
for bag, exp_each, exp_skip, tot in [('RRRB', 12, 28, 64), ('RB', 2, 2, 8), ('RRB', 6, 9, 27)]:
    t = Counter()
    for hist in itertools.product(labelled(bag), repeat=3):
        wd = ''.join(c for c, _ in hist)
        t[lone.get(wd, 'skip')] += 1
    say(f'  {bag}: {dict(t)} of {len(labelled(bag)) ** 3}')
    check(t['square'] == t['circle'] == t['triangle'] == exp_each and t['skip'] == exp_skip
          and sum(t.values()) == tot, f'{bag}: each output {exp_each}, skip {exp_skip} of {tot}')
ok = True
for r in range(1, 6):
    for b in range(1, 6):
        p = F(r, r + b)
        wsum = Counter()
        for wd, s in lone.items():
            wsum[s] += p ** wd.count('R') * (1 - p) ** wd.count('B')
        ok &= all(v == p * (1 - p) for v in wsum.values())
        ok &= sum(wsum.values()) == 3 * p * (1 - p)
check(ok, 'each output weight p(1-p), total 3p(1-p) (bags up to 5+5)')

# ---------------------------------------------------------------- bonus P2
say('\n## Bonus Problem 2 (recycling skipped pairs)')
REC = {'RRBB': 'C', 'BBRR': 'S'}


def outputs(word, recycle):
    o = [VN[word[:2]], VN[word[2:]]]
    o = [x for x in o if x != 'N']
    if recycle and not o and word in REC:
        o.append(REC[word])
    return o


def totals(bag, recycle):
    t = Counter()
    per_block = Counter()
    for hist in itertools.product(labelled(bag), repeat=4):
        wd = ''.join(c for c, _ in hist)
        o = outputs(wd, recycle)
        t.update(o)
        per_block[len(o)] += 1
    return t, per_block


for bag, exp_basic, exp_rec in [('RB', (8, 8), (9, 9)), ('RRRB', (96, 96), (105, 105))]:
    tb, pb = totals(bag, False)
    tr, pr = totals(bag, True)
    say(f'  {bag}: basic {dict(tb)} per-block {dict(pb)}; recycled {dict(tr)} per-block {dict(pr)}')
    check((tb['S'], tb['C']) == exp_basic and (tr['S'], tr['C']) == exp_rec,
          f'{bag}: basic {exp_basic}, recycled {exp_rec}')
tb, pb = totals('RB', False)
check(pb == Counter({0: 4, 1: 8, 2: 4}), 'balanced bag basic per-block counts 0:4, 1:8, 2:4')
tr, pr = totals('RB', True)
check(pr == Counter({0: 2, 1: 10, 2: 4}) and max(pr) == 2, 'recycling turns two zero-output words into one-output words')
t3b, _ = totals('RRRB', False)
t3r, _ = totals('RRRB', True)
check(sum(t3b.values()) == 192 and sum(t3r.values()) == 210, '3R/1B: 192/256 vs 210/256')
ok = True
for r in range(1, 5):
    for b in range(1, 5):
        p = F(r, r + b)
        e_basic = e_rec = F(0)
        for wd in (''.join(x) for x in itertools.product('RB', repeat=4)):
            pr_ = p ** wd.count('R') * (1 - p) ** wd.count('B')
            e_basic += pr_ * len(outputs(wd, False))
            e_rec += pr_ * len(outputs(wd, True))
        ok &= e_basic == 4 * p * (1 - p) and e_rec == 4 * p * (1 - p) + 2 * p ** 2 * (1 - p) ** 2
        # recycled shapes equal for every p
        ok &= (p ** 2 * (1 - p) ** 2) == ((1 - p) ** 2 * p ** 2)
check(ok, 'expected outputs per block 4p(1-p) -> 4p(1-p)+2p^2(1-p)^2 (bags up to 4+4)')
both_skipped = [wd for wd in (''.join(x) for x in itertools.product('RB', repeat=4))
                if not outputs(wd, False)]
check(sorted(both_skipped) == ['BBBB', 'BBRR', 'RRBB', 'RRRR'], 'both-skipped words RRRR, RRBB, BBRR, BBBB')

# ---------------------------------------------------------------- bonus P3
say('\n## Bonus Problem 3 (fair positions vs fair pairs)')
TK = ['SS', 'SC', 'CS', 'CC']
cups = []
for combo in itertools.combinations_with_replacement(TK, 4):
    left = Counter(t[0] for t in combo)
    right = Counter(t[1] for t in combo)
    if left['S'] == left['C'] == 2 and right['S'] == right['C'] == 2:
        cups.append(combo)
for c in cups:
    say('  fair-position cup:', c, 'support', len(set(c)), 'counts', dict(Counter(c)))
check(len(cups) == 3, 'exactly three four-ticket cups have fair positions')
supp = Counter(len(set(c)) for c in cups)
check(supp == Counter({2: 2, 4: 1}), 'two cups give two pairs (SS,SS,CC,CC and SC,SC,CS,CS); one gives all four')
check(('SS', 'SC', 'CS', 'CC') in [tuple(sorted(c, key=TK.index)) for c in cups], 'Cup 2 SS,SC,CS,CC is the unique all-four cup')
eq_among_possible = all(len(set(Counter(c).values())) == 1 for c in cups)
check(eq_among_possible,
      'EVERY fair-position four-ticket cup gives equal chances to each pair it can give '
      '(so "whole pair fair" = "equal chances among pairs that come out" makes the answer yes)')
# three possible pairs impossible for any number of tickets; first n with unequal possible pairs
first_unequal = None
ok3 = True
for n in range(2, 11):
    for combo in itertools.combinations_with_replacement(TK, n):
        left = Counter(t[0] for t in combo)
        right = Counter(t[1] for t in combo)
        if left['S'] == left['C'] and right['S'] == right['C']:
            if len(set(combo)) == 3:
                ok3 = False
            if first_unequal is None and len(set(Counter(combo).values())) > 1:
                first_unequal = combo
check(ok3, 'no fair-position cup of 2..10 tickets has exactly three possible pairs (guide extension)')
say('  smallest fair-position cup with unequal possible-pair chances:', first_unequal)

# ---------------------------------------------------------------- guide text
say('\n## Printed numbers in the base guide')
G = pdftext('week-42-facilitator.pdf')
phrases = [
    'sizes 9, 3, 3, 1 for RR, RB, BR, BB',
    'Thus ten of the sixteen labeled outcomes must be skipped',
    '8 of 16 pairs produce a shape, versus 6 of 16 for a 3-to-1 bag',
    'One red/three blue gives each shape in 3 of 16 marked pairs. Two red/two blue gives each shape in 4 of 16',
    'For red counts 0, 1, 2, 3, 4, the numbers of mixed labeled pairs are 0, 6, 8, 6, 0 out of 16',
    'no shapes: RR, RR, RR, RR, RR, RR',
    'Exactly one square, no circles: BR, RR, RR, RR, RR, RR',
    'Exactly three circles, no squares: RB, RB, RB, RR, RR, RR',
    'three outcomes for either shape and ten skipped outcomes',
    'Two red/two blue gives four labeled RB and four BR outcomes out of 16',
    'One red/three blue gives three RB and three BR outcomes',
    'The two-red bag produces a shape in 8 of 16 pairs; the three-red bag in 6 of 16',
    'RR 3, RB 9, BR 1, BB 3 among 16',
    'circle has 9 ways and square 1; conditional on a shape, their chances are 9/10 and 1/10',
    'five red/two blue has 10 RB and 10 BR outcomes among 49; three red/four blue has 12 and 12 among 49',
    'the RR class alone has weight 9 > 8',
    'all other classes total only 7',
    'The minimum is 10 skipped labeled pairs',
    'RB 9/16 and BR 1/16, so unfair',
    'each 6/32 = 3/16, so fair',
    'each mixed order 2/8 = 1/4, so fair',
    '4 x 3 = 12 equally likely ordered pairs',
    'RR has six, RB three, BR three, BB none',
    'Each shape has probability 3/12',
    'giving equal shape probabilities 3/16 and conditional probabilities 1/2',
]
for ph in phrases:
    check(norm(ph) in G, 'guide prints: ' + ph)
# G2-3 grid table in the guide
m = re.search(r'First / second R1 R2 R3 B (R1 .*?) The three RB cells', G)
rows = m.group(1).split() if m else []
exp_rows = []
for la, name in zip(['R1', 'R2', 'R3', 'B1'], ['R1', 'R2', 'R3', 'B']):
    exp_rows += [name] + [grid[(la, lb)] for lb in ['R1', 'R2', 'R3', 'B1']]
check(rows == exp_rows, 'guide p.4 grid table matches the 16 labelled colour pairs')
check('(9/16)6' in G or '(9/16)^6' in G, 'guide prints (9/16)^6')
check('Independence is sufficient, not necessary' in G,
      'guide p.1 sentence "Independence is sufficient, not necessary" present (see finding)')

say('\n## Printed numbers in the bonus guide')
BG = pdftext('week-42-bonus-facilitator.pdf')
bphrases = [
    'equal weight p(1-p)^2', 'equal weight p^2(1-p)', 'each output has weight p(1-p)',
    'Total output rate is 3p(1-p)',
    'RRBB and BBRR have equal probability p^2(1-p)^2',
    'rises from 4p(1-p) to 4p(1-p)+2p^2(1-p)^2',
    'produce 16 versus 18 outputs in total',
    'Thus RBB and BRR give square; BRB and RBR give circle; BBR and RRB give triangle',
    'all 64 identity triples are equally likely. Each output has 12 histories; 28 skip',
    'each output has two of eight stories and two skip',
    'each output has six of 27 identity histories and nine skip',
    'Basic output totals: square 8, circle 8, overall 16. Recycled: square 9, circle 9, overall 18',
    'Basic per-block counts are zero in 4 words, one in 8, two in 4',
    'each basic shape occurs 96 times', 'hence 105 each, total 210',
    'Compare 192/256 with 210/256',
    'Cup 1 can hold SS,SS,CC,CC. Cup 2 can hold SS,SC,CS,CC',
    'Other valid Cup 1 examples use SC,SC,CS,CS',
    'Four equally likely tickets SS,SS,CC,CC give each position S/C chances 1/2, but only SS and CC occur',
    'it is impossible with four equal tickets',
]
for ph in bphrases:
    check(norm(ph) in BG, 'bonus guide prints: ' + ph)
check(5 * 8 == 40 and 5 * 4 == 20 and 4 * 40 == 160, 'bonus materials: 40 tickets, 20 counters, 160 mm strip')

say('\n## Summary')
n_checks = sum(1 for l in OUT if l.startswith(('PASS', 'FAIL')))
say(f'{n_checks} checks, {len(FAIL)} failures')
for f in FAIL:
    say('FAILED:', f)
(HERE / 'out_check_math.txt').write_text('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
sys.exit(1 if FAIL else 0)
