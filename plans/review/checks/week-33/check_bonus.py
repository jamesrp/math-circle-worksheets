"""Independent check of the Week 33 bonus companion (Necklaces encore) and its
adult guide.  Ring words for Problem 1 come from pdf_geometry.json (read from
the delivered PDF by pdf_extract.py).  Output saved as check_bonus.out.
"""
import json
import os
import re
import sys
from itertools import combinations

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, PDFS, Log, canon, canon_flip, necklaces, proper,  # noqa: E402
                    readouts, rotations, windows, words)

log = Log()
geo = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))
gtext = re.sub(r'\s+', ' ', ''.join(p.get_text() for p in pymupdf.open(PDFS['bonus-guide'])))

print('=== P1: six printed eight-rings ===')
R = {r['label']: r['letters'] for r in geo['bonus']['rings'] if r['label']}
print(R)
assert sorted(R) == list('abcdef')


def groups(key):
    g = {}
    for lab in 'abcdef':
        g.setdefault(key(R[lab]), []).append(lab)
    return sorted(g.values())


turns = groups(canon)
flips = groups(canon_flip)
print('turns only:', turns, ' turns and flips:', flips)
log.check(turns == [['a', 'c'], ['b'], ['d', 'f'], ['e']], 'turns only: {a,c},{b},{d,f},{e} (guide)')
log.check(flips == [['a', 'b', 'c'], ['d', 'e', 'f']], 'turns and flips: {a,b,c},{d,e,f} (guide)')
bits = {lab: ''.join('1' if ch == 'A' else '0' for ch in R[lab]) for lab in R}
for lab, claimed in re.findall(r'\b([a-f])=([01]{8})\b', gtext):
    log.check(bits[lab] == claimed, f'guide word {lab}={claimed} matches the printed ring read clockwise from the top')


def gaps(w):
    pos = [i for i, ch in enumerate(w) if ch == 'A']
    return [(pos[(i + 1) % len(pos)] - pos[i]) % len(w) or len(w) for i in range(len(pos))]


def cyc_eq(x, y):
    return any(x[i:] + x[:i] == y for i in range(len(x)))


for lab in 'abcdef':
    print(f'  {lab}: {R[lab]} A-gaps {gaps(R[lab])}')
log.check(cyc_eq(gaps(R['a']), [1, 2, 5]) and cyc_eq(gaps(R['b']), [5, 2, 1]), 'a has gaps 1,2,5; b has the reversed cyclic order')
log.check(cyc_eq(gaps(R['d']), [1, 3, 4]) and cyc_eq(gaps(R['e']), [4, 3, 1]), 'd has gaps 1,3,4; e reversed')
log.check(R['c'] in readouts(R['a']) and R['f'] in readouts(R['d']), 'c rotates a; f rotates d')
log.check(all(R[l].count('A') == 3 and R[l].count('B') == 5 for l in R), 'every P1 ring uses 3 A and 5 B')
# general claim: three marks with three distinct cyclic gaps -> flip is not a turn; repeated gap -> achiral
ok = True
for n in range(3, 13):
    for w in words('AB', n):
        if w.count('A') != 3:
            continue
        g = gaps(w)
        chiral = canon(w[::-1]) != canon(w)
        ok &= chiral == (len(set(g)) == 3)
log.check(ok, 'n<=12, three A beads: flip differs from every turn exactly when the three gaps are all different')
# depth claim: at most two marked spots -> a reflection survives; binary length <=5 -> no mirror twins
ok = True
for n in range(1, 13):
    for k in (0, 1, 2):
        for S in combinations(range(n), k):
            S = set(S)
            ok &= any({(a - s) % n for s in S} == S for a in range(n))  # reflections s -> a - s
log.check(ok, 'every set of <=2 spots on an n-gon (n<=12) is preserved by some reflection')
log.check(all(canon(w[::-1]) == canon(w) for n in range(1, 6) for w in words('AB', n)), 'no binary ring of length <=5 has a mirror twin')

print('\n=== P2: two kinds, different neighbours ===')
for n in (4, 5, 6):
    sols = sorted({canon(w) for w in words('AB', n) if proper(w)})
    print(f'  n={n}: {sols}')
    log.check(sols == ({4: ['ABAB'], 5: [], 6: ['ABABAB']}[n]), f'n={n}: guide answer')
log.check(all(bool([w for w in words('AB', n) if proper(w)]) == (n % 2 == 0) for n in range(2, 13)),
          'two kinds: a proper ring exists exactly at even lengths (n=2..12)')

print('\n=== P3: three kinds, five beads, different neighbours ===')
fixed = [w for w in words('ABC', 5) if proper(w)]
cls = sorted({canon(w) for w in fixed})
print('  classes:', cls)
log.check(len(fixed) == 30 and len(cls) == 6, f'{len(fixed)} fixed words, {len(cls)} rotation classes')
claimed = 'ABABC, ABACB, ABCAC, ABCBC, ACACB, ACBCB'.split(', ')
log.check(all(proper(w) for w in claimed) and sorted({canon(w) for w in claimed}) == cls and len(claimed) == 6,
          'guide representatives are proper, pairwise different by turning, and cover every class')
log.check(all(sorted(w.count(ch) for ch in 'ABC') == [1, 2, 2] for w in fixed), 'every proper word has multiplicities 2,2,1')
log.check(len({canon_flip(w) for w in fixed}) == 3, 'allowing flips merges them into 3 classes (one per singleton kind)')
log.check(all(len(readouts(w)) == 5 for w in cls), 'five views for each of the six rings')
# chromatic formula and the S/D recurrence
ok = True
for c in range(2, 6):
    alph = 'ABCDE'[:c]
    S, D = 1, 0
    for n in range(2, 10):
        S, D = D, (c - 1) * S + (c - 2) * D
        if n >= 3 and c ** n <= 400000:
            brute = sum(1 for w in words(alph, n) if proper(w))
            ok &= brute == (c - 1) ** n + (-1) ** n * (c - 1) == c * D
log.check(ok, 'proper n-ring count (c-1)^n+(-1)^n(c-1) = c*D_n = brute force (c=2..5, n=3..9 where feasible)')

print('\n=== P4-P7: windows ===')
log.check(windows('BABAA', 3)[0] == 'BAB', 'window example: starting at the marked B, first window is BAB')
for k in (2, 3):
    need = set(words('AB', k))
    for n in range(1, 2 ** k + 1):
        sols = sorted({canon(w) for w in words('AB', n) if sorted(windows(w, k)) == sorted(need)})
        if n < 2 ** k:
            log.check(not sols, f'k={k}: no ring of length {n} has every {k}-letter window exactly once')
        else:
            print(f'  k={k}, n={n}: rotation classes {sols}')
            if k == 2:
                log.check(sols == ['AABB'], 'P4: AABB is the unique shortest ring (up to turning)')
            else:
                log.check(sols == ['AAABABBB', 'AAABBBAB'], 'P6/P7: exactly two shortest rings, AAABABBB and AAABBBAB')
                log.check(canon(sols[0][::-1]) == sols[1] and canon(sols[1][::-1]) == sols[0],
                          'P7: the flip of each is a turn of the other (mirror twins)')
                log.check(len({canon_flip(w) for w in sols}) == 1, 'allowing flips gives one class')
                fixedw = [w for w in words('AB', 8) if sorted(windows(w, 3)) == sorted(need)]
                log.check(len(fixedw) == 16, f'{len(fixedw)} of the 256 indexed eight-words qualify (2 classes x 8 turns)')
log.check(windows('AABB', 2) == ['AA', 'AB', 'BB', 'BA'], 'guide P4: windows of AABB are AA,AB,BB,BA')
log.check(windows('AAABABBB', 3) == 'AAA,AAB,ABA,BAB,ABB,BBB,BBA,BAA'.split(','), 'guide P6: windows of AAABABBB in the listed order')
# "at least eight counters each of kinds A/B": P7's two rings side by side use 8 A and 8 B; two P1 rings use 10 B
log.note(f'P7 pair uses {sum(w.count("A") for w in ["AAABABBB", "AAABBBAB"])} A and '
         f'{sum(w.count("B") for w in ["AAABABBB", "AAABBBAB"])} B; two P1 rings side by side use 6 A and 10 B')

log.summary()
