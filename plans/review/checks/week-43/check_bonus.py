"""Independent checks of the Week 43 bonus companion (picture rows, cuts and
reversals, random insertion) and every claim in its adult guide.

Reads printed card words from extracted.json (run extract.py first) and the
guide text from the delivered PDF. Writes check_bonus.out.
"""
import json
import os
import re
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import factorial, prod

from common import HERE, PDFS, Report, flat, pdf_text

R = Report('check_bonus')
X = json.load(open(os.path.join(HERE, 'extracted.json')))['bonus']
G = ' '.join(flat(t) for t in pdf_text(PDFS['bonus-guide']))
S = [flat(t) for t in pdf_text(PDFS['bonus'])]


def picture(labeled):
    return ''.join(c[0] for c in labeled)


def rot(w, k):
    return w[k:] + w[:k]


def closure(start, ops):
    seen, todo = {start}, [start]
    while todo:
        w = todo.pop()
        for op in ops:
            v = op(w)
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return seen


# ---------------------------------------------------------------- Problem 1
R.head('Problem 1: repeated pictures')
lab = ['A1', 'A2', 'B1', 'B2']
orders = list(permutations(lab))
pic = Counter(picture(o) for o in orders)
R.note(f'24 labeled orders -> {dict(pic)}')
R.check(len(orders) == 24 and len(pic) == 6 and set(pic.values()) == {4}, 'six picture rows, four labeled orders each')
R.check(all(Fraction(v, 24) == Fraction(1, 6) for v in pic.values()), 'each picture row has chance 1/6')
words = re.search(r'All picture words: ([A-Z,]+)\.', G).group(1).split(',')
R.check(sorted(words) == sorted(pic), f'guide picture words {words}')
aabb = sorted(''.join(o) for o in orders if picture(o) == 'AABB')
R.check(aabb == ['A1A2B1B2', 'A1A2B2B1', 'A2A1B1B2', 'A2A1B2B1'] and all(w in G for w in aabb), f'guide AABB labelings {aabb}')
blank_rows = sum(1 for r in X[0]['rects'] if abs(r['x1'] - r['x0'] - 44) < .5) // 4
R.check(blank_rows >= len(pic), f'page 1 prints {blank_rows} record rows for {len(pic)} picture rows')
for multis in [(3, 1), (3, 2), (2, 2, 1), (2, 1, 1)]:
    letters = ''.join(chr(65 + i) * m for i, m in enumerate(multis))
    labeled = [f'{ch}{k}' for i, m in enumerate(multis) for ch in [chr(65 + i)] for k in range(1, m + 1)]
    c = Counter(picture(o) for o in permutations(labeled))
    n = sum(multis)
    R.check(len(c) == factorial(n) // prod(factorial(m) for m in multis) and set(c.values()) == {prod(factorial(m) for m in multis)},
            f'multiplicities {multis}: {len(c)} words x {set(c.values())} labelings (n!/prod m!)')
R.check('four picture rows with six labelings each' in G, 'guide extension A1,A2,A3,B1: 4 rows x 6 (checked above)')

# ---------------------------------------------------------------- Problem 2
R.head('Problem 2: cuts and reversals')
cut_ex = [w['word'] for w in X[1]['words']]
R.check(cut_ex[:3] == ['WXYZ', 'YZWX', 'ABCD'] and rot('WXYZ', 2) == 'YZWX', f'printed cut example and start {cut_ex}')
cuts = [lambda w, k=k: rot(w, k) for k in range(4)]
rev = [lambda w: w[::-1]]
C1 = closure('ABCD', cuts)
C2 = closure('ABCD', cuts + rev)
R.note(f'cuts only: {sorted(C1)}; cuts + reversal: {sorted(C2)}')
R.check(C1 == {'ABCD', 'BCDA', 'CDAB', 'DABC'}, 'cuts only: exactly the four rotations')
R.check(C2 - C1 == {'DCBA', 'CBAD', 'BADC', 'ADCB'}, 'reversal adds exactly DCBA, CBAD, BADC, ADCB')
R.check('ABDC' not in C2, 'ABDC impossible under both rules')
for w in ['ADBC', 'ABDC', 'ACBD']:
    R.check(w not in C2, f'guide: {w} never appears')
m = re.search(r'Cuts only: ([A-Z,]+)\. Cuts plus reversal add ([A-Z,]+)\.', G)
R.check(set(m.group(1).split(',')) == C1 and set(m.group(2).split(',')) == C2 - C1, 'guide catalogs match')


def nbrs(w, x):
    i = w.index(x)
    return {w[(i - 1) % len(w)], w[(i + 1) % len(w)]}


R.check(all(nbrs(w, x) == nbrs('ABCD', x) for w in C2 for x in 'ABCD'), 'invariant: every card keeps its two cyclic neighbours')
R.check(nbrs('ABDC', 'A') == {'B', 'C'} and nbrs('ABCD', 'A') == {'B', 'D'}, 'guide: A has cyclic neighbours B,D vs B,C in ABDC')
R.check(len(closure('ABCDE', [lambda w, k=k: rot(w, k) for k in range(5)])) == 5 and
        len(closure('ABCDE', [lambda w, k=k: rot(w, k) for k in range(5)] + rev)) == 10, 'guide extension: 5 cards -> 5 and 10 rows')
first = Counter(rot('ABCD', k)[0] for k in range(4))
R.check(set(first.values()) == {1} and len(first) == 4, 'one uniform cut: each card first with chance 1/4')
# any number of independent uniform cuts: distribution over rotations stays uniform
dist = {'ABCD': Fraction(1)}
for _ in range(3):
    nd = Counter()
    for w, p in dist.items():
        for k in range(4):
            nd[rot(w, k)] += p / 4
    dist = nd
R.check(len(dist) == 4 and set(dist.values()) == {Fraction(1, 4)}, 'repeated random cuts: 4 rows at 1/4, 20 orders at 0')
# a random cut after a uniform shuffle preserves uniformity
u = Counter()
for p in permutations('ABCD'):
    for k in range(4):
        u[rot(''.join(p), k)] += Fraction(1, 24 * 4)
R.check(len(u) == 24 and set(u.values()) == {Fraction(1, 24)}, 'guide: random cut after a uniform shuffle stays uniform')
R.check(rot(rot('ABCD', 1), 2) == rot('ABCD', 3) and rot('ABCD', 1)[::-1] == rot('DCBA', 3),
        'guide closure argument: rotation of rotation is a rotation; reversed rotation is rotation of reversal')

# ---------------------------------------------------------------- Problem 3
R.head('Problem 3: random insertion')
ins_ex = [w['word'] for w in X[2]['words']]
R.check(ins_ex[:3] == ['XY', 'Z', 'XZY'], f'printed insertion example {ins_ex[:3]}')


def insert(old, g, new='D'):
    return old[:g - 1] + new + old[g - 1:]


R.check(insert('XY', 2, 'Z') == 'XZY', 'gap 2 of XY is between X and Y')
hist = {(''.join(p), g): insert(''.join(p), g) for p in permutations('ABC') for g in range(1, 5)}
R.check(len(hist) == 24 and len(set(hist.values())) == 24, '6 old rows x 4 gaps = 24 stories, all different final orders')
inv = {v: k for k, v in hist.items()}
targets = ins_ex[3:]
R.check(targets == ['ABCD', 'DACB', 'BDCA', 'CBAD'], f'printed targets {targets}')
exp = {'ABCD': ('ABC', 4), 'DACB': ('ACB', 1), 'BDCA': ('BCA', 2), 'CBAD': ('CBA', 4)}
for t in targets:
    R.check(inv[t] == exp[t], f'target {t}: old row {inv[t][0]}, gap {inv[t][1]}')
    R.check(f'{t} comes from {exp[t][0]}, gap {exp[t][1]}' in G.replace('Targets: ', '') or
            f'{t} from {exp[t][0]}, gap {exp[t][1]}' in G, f'guide states {t} <- {exp[t]}')
R.check(all(Fraction(1, 6) * Fraction(1, 4) == Fraction(1, 24) for _ in hist), 'each final order has chance 1/24')
# biased old shuffle is not repaired
bias = {'ABC': Fraction(1, 2)}
bias.update({''.join(p): Fraction(1, 10) for p in permutations('ABC') if ''.join(p) != 'ABC'})
out = Counter()
for (o, g), w in hist.items():
    out[w] += bias[o] / 4
R.check(len(set(out.values())) > 1, 'guide: fair gaps cannot repair a biased old shuffle (example: ABC at 1/2)')
# independence matters: a dependent gap rule with uniform marginal gap is not uniform
dep = {}
olds = [''.join(p) for p in permutations('ABC')]
# old rows 1..6; gap rule: rows 1,2 -> gaps {1,2}; rows 3,4 -> gaps {3,4}; rows 5,6 -> {1,2,3,4} half/half...
# simplest: gap = 1 + (index mod 4) cycling, with weight spreading to make marginal uniform
pairs = Counter()
for i, o in enumerate(olds):
    for g in range(1, 5):
        if (i + g) % 2 == 0:
            pairs[(o, g)] += Fraction(1, 12)
marg = Counter()
for (o, g), p in pairs.items():
    marg[g] += p
outd = Counter()
for (o, g), p in pairs.items():
    outd[insert(o, g)] += p
R.check(set(marg.values()) == {Fraction(1, 4)} and len(outd) == 12,
        'a gap draw that depends on the old row can have uniform gap marginal yet reach only 12 orders')
# general: insert into n+1 gaps after uniform n-shuffle -> uniform; E extension
for n in (4, 5):
    letters = 'ABCDEF'[:n]
    new = 'ABCDEF'[n]
    res = Counter(insert(''.join(p), g, new) for p in permutations(letters) for g in range(1, n + 2))
    R.check(len(res) == factorial(n + 1) and set(res.values()) == {1}, f'insertion of card {n + 1}: {factorial(n)}*{n + 1}={factorial(n + 1)} stories, bijective')
R.check('24*5=120' in G, 'guide E extension count 120')

# ---------------------------------------------------------------- student text
R.head('Student text')
R.check('Choose 0, 1, 2, or 3 front cards with equal chances' in S[1], 'P2 shared rule: uniform cut size 0..3')
R.check('Independently draw one of four equal-chance gap tickets' in S[2], 'P3 states independence and four gaps')
R.check('Number gaps from left to right' in S[2], 'P3 gap numbering convention stated')

R.finish()
