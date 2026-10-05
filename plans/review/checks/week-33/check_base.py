"""Independent check of the Week 33 base packet (K-1, 2-3, 4-5) and its adult
guide, by brute-force enumeration.

Reads card numbering from pdf_geometry.json (run pdf_extract.py first) and the
guide's tables and lists from the delivered guide PDF, then compares every
claim with enumeration done here.  Output saved as check_base.out.
"""
import json
import os
import re
import sys
from itertools import combinations, product
from math import gcd

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HERE, PDFS, Log, canon, canon_flip, families, necklaces,  # noqa: E402
                    period, readouts, rotations, words, is_prime)

log = Log()
geo = json.load(open(os.path.join(HERE, 'pdf_geometry.json')))
guide = ''.join(p.get_text() for p in pymupdf.open(PDFS['guide']))
guide_flat = re.sub(r'\s+', ' ', guide)


def cards(band, length):
    cs = [c for c in geo[band]['cards'] if len(c['letters']) == length]
    return {int(c['num']): c['letters'] for c in cs}


print('=== Three-bead rings (all bands P1-P2) ===')
n3 = necklaces('AB', 3)
print('rings:', n3, 'family sizes:', [len(readouts(w)) for w in n3])
log.check(len(n3) == 4, 'there are 4 three-bead A/B rings (one-colour allowed)')
mixed3 = [w for w in n3 if len(set(w)) == 2]
log.check(len(mixed3) == 2, f'only {len(mixed3)} of them use both A and B: {mixed3}')
for band in ('k-1', 'grades-2-3', 'grades-4-5'):
    boards = [r for r in geo[band]['rings'] if r['page'] == 1 and r['n'] == 3 and set(r['letters']) == {'-'}]
    log.note(f'{band} P1: {len(boards)} blank three-bead boards printed for a 4-ring answer (2 = the mixed-only count)')
# guide table vs 8 cards
tab3 = re.findall(r'\b([AB]{3})\s+((?:[AB]{3}(?:,\s*)?)+)\s+([\d,]+)', guide)
c3 = cards('grades-2-3', 3)
assert c3 == cards('k-1', 3) == cards('grades-4-5', 3)
fam3 = {}
for k, w in c3.items():
    fam3.setdefault(canon(w), []).append(k)
for rep, rd, nums in tab3:
    rds = [x.strip() for x in rd.split(',')]
    log.check(set(rds) == readouts(rep) and len(rds) == len(readouts(rep)),
              f'guide 3-bead row {rep}: readouts {rds} are exactly the rotations')
    log.check(sorted(int(x) for x in nums.split(',')) == sorted(fam3[canon(rep)]),
              f'guide 3-bead row {rep}: card numbers {nums} = printed cards {sorted(fam3[canon(rep)])}')
log.check(sorted(len(v) for v in fam3.values()) == [1, 1, 3, 3], 'family sizes 1,3,3,1 (not all equal)')
log.check(2 + (8 - 2) // 3 == 4 and (8 - 2) % 3 == 0 and 8 % 3 != 0, '2+(8-2)/3 = 4; 8/3 is not a whole number')

print('\n=== K-1 P3: four beads, two A and two B ===')
r = [w for w in necklaces('AB', 4) if w.count('A') == 2]
print(r)
log.check(r == ['AABB', 'ABAB'], 'exactly two rings: AABB, ABAB (guide P3)')
log.note('K-1 P3 page prints 4 boards for this 2-ring answer')

print('\n=== Four-bead readout counts (K-1 P4, 2-3 P3, 4-5 P3) ===')
n4 = necklaces('AB', 4)
sizes4 = {w: len(readouts(w)) for w in n4}
print(sizes4)
log.check(set(sizes4.values()) == {1, 2, 4}, 'possible numbers of readouts: 1, 2, 4; 3 impossible')
log.check(len(n4) == 6 and sizes4 == {'AAAA': 1, 'AAAB': 4, 'AABB': 4, 'ABAB': 2, 'ABBB': 4, 'BBBB': 1},
          'guide 4-5 P3: six rings AAAA,BBBB (1), ABAB (2), AAAB,AABB,ABBB (4)')
log.check(rotations('AAAB') == ['AAAB', 'AABA', 'ABAA', 'BAAA'], 'guide K-1 P4: AAAB readouts AAAB,AABA,ABAA,BAAA')
log.check(readouts('ABAB') == {'ABAB', 'BABA'}, 'guide K-1 P4: ABAB readouts ABAB,BABA')
# The guide's 2-3 P3 "physical alternative": which coincidences R_i = R_j occur on 4-bead rings?
print('  coincidences between readouts at starts i<j, by step j-i, for mixed 4-bead words:')
steps = {}
for w in words('AB', 4):
    if len(set(w)) < 2:
        continue
    R = rotations(w)
    for i, j in combinations(range(4), 2):
        if R[i] == R[j]:
            steps.setdefault(j - i, set()).add(canon(w))
print('   ', {k: sorted(v) for k, v in steps.items()})
log.check(set(steps) == {2}, 'mixed 4-bead rings repeat only after 2 steps (ABAB); a 1- or 3-step repeat forces one colour')
log.note('guide 2-3 P3 "physical alternative" treats only the 3-step repeat; the 2-step repeat (ABAB, 2 readouts) '
         'must also be excluded for "exactly three" - see report')

print('\n=== K-1 P5: five beads, two A and three B ===')
r = [w for w in necklaces('AB', 5) if w.count('A') == 2]
log.check(r == ['AABBB', 'ABABB'], f'exactly two rings: {r}')
log.check(all(len(readouts(w)) == 5 for w in r), 'each has five readouts')
log.check(rotations('AABBB') == 'AABBB,ABBBA,BBBAA,BBAAB,BAABB'.split(','), 'guide list for AABBB = its rotations in order')
log.check(rotations('ABABB') == 'ABABB,BABBA,ABBAB,BBABA,BABAB'.split(','), 'guide list for ABABB = its rotations in order')
log.note('K-1 P5 page prints 4 boards for this 2-ring answer')

print('\n=== K-1 P6: six beads, both colours ===')
by = {}
for w in necklaces('AB', 6):
    if len(set(w)) == 2:
        by.setdefault(len(readouts(w)), []).append(w)
print({k: v for k, v in sorted(by.items())})
log.check(set(by) == {2, 3, 6}, 'two, three and six readouts all occur; nothing else (1,4,5) occurs')
log.check(len(readouts('ABABAB')) == 2 and len(readouts('AABAAB')) == 3 and len(readouts('AAAAAB')) == 6,
          'guide examples ABABAB=2, AABAAB=3, AAAAAB=6')
log.check(max('ABABAB'.count('A'), 'AABAAB'.count('A'), 'AAAAAB'.count('A')) <= 6, 'each example fits a pair-kit of six A and six B')

print('\n=== Five-bead cards (2-3 P4, 4-5 P4) ===')
c5 = cards('grades-2-3', 5)
assert c5 == cards('grades-4-5', 5)
fam5 = {}
for k, w in c5.items():
    fam5.setdefault(canon(w), []).append(k)
for rep in sorted(fam5):
    print(f'  {rep}: cards {sorted(fam5[rep])}')
tab5 = re.findall(r'\b([AB]{5})\s+([\d,]+)\s+(\d)\b', guide)
log.check(len(tab5) == 8 == len(fam5), f'8 rings; guide table has {len(tab5)} rows')
for rep, nums, size in tab5:
    got = sorted(fam5[canon(rep)])
    log.check(sorted(int(x) for x in nums.split(',')) == got and int(size) == len(got),
              f'guide row {rep}: cards {nums}, size {size}')
log.check(sorted(len(v) for v in fam5.values()) == [1, 1, 5, 5, 5, 5, 5, 5], 'two singletons and six families of five')
log.check(2 + (32 - 2) // 5 == 8 and 32 % 5 != 0, '2-3 P6: 32/5 is not whole; 2+(32-2)/5 = 8')
log.check(all(len(readouts(w)) == 5 for w in words('AB', 5) if len(set(w)) == 2),
          '2-3 P5: every mixed five-bead ring has exactly five readouts (no counterexample exists)')
seq2 = [(2 * i) % 5 for i in range(6)]
seq3 = [(3 * i) % 5 for i in range(6)]
log.check(seq2 == [0, 2, 4, 1, 3, 0] and seq3 == seq2[::-1], f'guide 2-3 P5: steps of 2 visit {seq2}; steps of 3 visit {seq3} (reverse)')

print('\n=== Theory: prime lengths, period, counting (4-5 P5, P6, overview) ===')
for c in (2, 3):
    for n in range(1, 13 if c == 2 else 9):
        for w in words('ABC'[:c], n):
            d = period(w)
            assert n % d == 0, (w, d)
            assert len(readouts(w)) == d, (w, d)
            if is_prime(n) and len(set(w)) > 1:
                assert len(readouts(w)) == n, w
log.check(True, 'all binary words n<=12 and ternary n<=8: least period d divides n and equals the number of readouts; '
                'prime n: every mixed word has n readouts')
comp_early = {n: any(len(set(w)) > 1 and len(readouts(w)) < n for w in words('AB', n)) for n in range(2, 13)}
log.check(all(comp_early[n] == (not is_prime(n)) for n in comp_early),
          'a mixed binary ring repeats early exactly when the length is composite (n=2..12)')
for c in range(1, 5):
    for p in (2, 3, 5, 7):
        if c ** p > 20000:
            continue
        cnt = len(necklaces('ABCD'[:c], p))
        log.check(cnt == c + (c ** p - c) // p and (c ** p - c) % p == 0, f'c={c}, p={p}: {cnt} rings = c+(c^p-c)/p')
log.check(len(necklaces('ABC', 5)) == 51 and 3 ** 5 == 243 and (243 - 3) // 5 == 48, '4-5 P6: 243 readouts, 3 constant, 48 families of five, 51 rings')
log.check(all((c ** p - c) % p == 0 for c in range(0, 60) for p in range(2, 40) if is_prime(p)), 'p | c^p - c for c<60, primes p<40')
# composite lengths: formula fails
for n, c in ((4, 2), (6, 2), (4, 3)):
    true = len(necklaces('ABC'[:c], n))
    log.check((c ** n - c) % n != 0 or c + (c ** n - c) // n != true,
              f'n={n}, c={c}: prime formula fails ((c^n-c)/n = {(c ** n - c) / n:.2f}, true count {true})')
log.check(pow(2, 341, 341) == 2 and 341 == 11 * 31, 'converse fails: 341 = 11*31 divides 2^341 - 2 (guide "not a converse primality test")')
# guide 4-5 P5 step: p | m*k with 0<m,k<p impossible
log.check(all((m * k) % p for p in range(2, 60) if is_prime(p) for m in range(1, p) for k in range(1, p)),
          'guide 4-5 P5: for prime p and 0<m,k<p, p does not divide mk')

print('\n=== Guide optional extension: AABABB vs AABBAB ===')
log.check(rotations('AABABB') == 'AABABB,ABABBA,BABBAA,ABBAAB,BBAABA,BAABAB'.split(','), 'listed rotations of AABABB are correct and in order')
log.check('AABBAB' not in readouts('AABABB') and canon('AABBAB') == canon('AABABB'[::-1]),
          'AABBAB is a flip of AABABB but not a turn of it')
chiral = {n: [w for w in necklaces('AB', n) if canon(w[::-1]) != w and canon(w[::-1]) != canon(w)] for n in range(1, 8)}
log.check(all(not chiral[n] for n in range(1, 6)) and chiral[6], f'smallest binary length with a flip-only pair is 6: {chiral[6]}')

print('\n=== Guide period proof: n = q d + r restores r ===')
ok = True
for n in range(1, 11):
    for w in words('AB', n):
        rs = {s for s in range(1, n + 1) if w[s:] + w[:s] == w}
        d = min(rs)
        ok &= all(s % d == 0 for s in rs)
        # starts with different remainders mod d differ; starts congruent mod d agree
        R = rotations(w)
        ok &= all((R[i] == R[j]) == ((i - j) % d == 0) for i in range(n) for j in range(n))
log.check(ok, 'restoring rotations are exactly the multiples of d; R_i = R_j iff i = j (mod d), n<=10')

log.summary()
