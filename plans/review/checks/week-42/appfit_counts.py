# Recheck the counts the reconciled Week 42 card's App fit and fixes cite.
from itertools import product
from fractions import Fraction as F

def bag(r, b): return ['R%d' % i for i in range(1, r+1)] + ['B%d' % i for i in range(1, b+1)]
col = lambda c: c[0]
def pairs(b1, b2=None, replace=True):
    b2 = b2 if b2 is not None else b1
    out = []
    for i, x in enumerate(b1):
        for j, y in enumerate(b2):
            if not replace and b2 is b1 and i == j: continue
            out.append(col(x)+col(y))
    return out
WORDS = ['RR','RB','BR','BB']
RULES = list(product(['S','C','-'], repeat=4))   # square, circle, skip
print('colour-only rules:', len(RULES))
def tally(ps, rule):
    m = dict(zip(WORDS, rule)); s = sum(m[p]=='S' for p in ps); c = sum(m[p]=='C' for p in ps)
    return s, c, len(ps)-s-c
def fair(ps, rule):
    s, c, k = tally(ps, rule); return s == c and s > 0
# 3R/1B classes, fair rules, skips
P = pairs(bag(3,1)); print('3R1B classes', {w: P.count(w) for w in WORDS})
fr = [r for r in RULES if fair(P, r)]; print('fair rules 3R1B:', fr, 'skips', [tally(P, r)[2] for r in fr])
# K-1 P4 under BR->S, RB->C
key = ('-','C','S','-')
for rb in [(1,3),(2,2),(4,0),(0,4),(3,1)]:
    print('K-1 kept rule', rb, tally(pairs(bag(*rb)), key))
# mixed pairs only (what counters can build): RB+BR count per four-counter bag
print('mixed pairs per 4-bag', [(r, 2*r*(4-r)) for r in range(5)])
# no-skip fair rule exists exactly when r == b (check up to 10+10)
ok = True
for r in range(1, 11):
    for b in range(1, 11):
        ps = pairs(bag(r, b)); ex = any(fair(ps, x) and tally(ps, x)[2] == 0 for x in RULES)
        if ex != (r == b): ok = False; print('counterexample', r, b)
print('no-skip fair iff r == b (1..10):', ok)
print('no-skip fair rules on 2R2B:', sum(fair(pairs(bag(2,2)), x) and tally(pairs(bag(2,2)), x)[2]==0 for x in RULES))
fd = ('S','S','C','C')  # first colour decides
print('first colour decides on 2R2B:', tally(pairs(bag(2,2)), fd))
# cross bags
X = pairs(bag(3,1), bag(1,3)); print('RRRB then RBBB', {w: X.count(w) for w in WORDS})
print('  RB/BR rule', tally(X, ('-','C','S','-')), ' RR->S BB->C', tally(X, ('S','-','-','C')))
print('  fair rules there:', [r for r in RULES if fair(X, r)])
Y = pairs(bag(2,2), bag(1,1)); print('RRBB then RB', {w: Y.count(w) for w in WORDS}, tally(Y, key))
Z = pairs(bag(3,1), bag(6,2)); print('RRRB then 6R2B', {w: Z.count(w) for w in WORDS}, tally(Z, key), 'reds needed', 3+6)
# no replacement
N = pairs(bag(3,1), replace=False); print('3R1B no replacement', {w: N.count(w) for w in WORDS}, len(N))
print('  both red -> S else C', tally(N, ('S','C','C','C')))
# bonus P1: 3-draw words, six mixed words to three shapes, fair for every p
mixed = [w for w in (''.join(t) for t in product('RB', repeat=3)) if w not in ('RRR','BBB')]
cnt = 0
for a in product(range(3), repeat=6):
    # weight of a word: p^#R (1-p)^#B; fair for all p iff each shape gets one 1-R word and one 2-R word
    ok1 = all(sorted(w.count('R') for w, s in zip(mixed, a) if s == k) == [1, 2] for k in range(3))
    cnt += ok1
print('bonus P1 universal rules', cnt, 'of', 3**6)
# 2-3 P7 / 4-5 P4 certificate
print('RR 9 > 8 =', 9 > 16/2, ' other classes total', 3+3+1)
