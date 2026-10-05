"""Independent finite checks for Week 18 (hidden changes / error-correcting keys).

Own code only: no packet builder, checker or answer file is imported.
Printed data come from pdf_strips.json (written by extract_pdf.py from the
delivered PDFs); guide claims are quoted from the delivered guide PDF and each
quote is first confirmed to appear in its text.

Conventions (from the 4-5 shared rules): 0 = empty circle, 1 = filled circle.
A "change" flips one entry. A key works for t changes when no received row is
reachable from two different key rows with at most t flips each.
"""
import itertools
import json
import re
import pymupdf
from repo import WEEK, HERE

FAILS = []


def ok(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def words(n):
    return [''.join(w) for w in itertools.product('01', repeat=n)]


def flip(w, i):
    return w[:i] + ('1' if w[i] == '0' else '0') + w[i + 1:]


def received(w, t=1):
    """All rows obtainable by flipping at most t distinct positions (built by flipping, not by distance)."""
    out = {w}
    for k in range(1, t + 1):
        for pos in itertools.combinations(range(len(w)), k):
            x = w
            for i in pos:
                x = flip(x, i)
            out.add(x)
    return out


def works(key, t=1):
    if len(set(key)) < len(key):
        return False
    return all(not (received(a, t) & received(b, t)) for a, b in itertools.combinations(key, 2))


def dist(a, b):
    return sum(x != y for x, y in zip(a, b))


def fmt(s):
    return '{' + ','.join(sorted(s)) + '}'


# ---------------------------------------------------------------- data
strips = json.loads((HERE / 'pdf_strips.json').read_text())
guide_doc = pymupdf.open(WEEK / 'week-18-facilitator.pdf')
GUIDE = ' '.join(' '.join(p.get_text().split()) for p in guide_doc)


def quote(q):
    """Confirm a quoted guide claim exists verbatim (whitespace-normalised)."""
    q2 = ' '.join(q.split())
    ok(q2 in GUIDE, 'guide quote present: "' + (q2[:70] + '...' if len(q2) > 70 else q2) + '"')
    return q2


def page(band, n):
    return strips[band][n - 1]['strips']


def printed(band, n, icon=None):
    return [s['contents'] for s in page(band, n) if icon is None or s['icon'] == icon]


print('=== Printed data read from the PDFs')
# training page, all bands
for band in strips:
    tr = printed(band, 1)
    ok(tr == ['0101', '0111', '0111'], f'{band} p1 training: start 0101, final 0111, receiver 0111')
    ok([i for i in range(4) if tr[0][i] != tr[1][i]] == [2], f'{band} p1 training: only the third entry changes')

# ================================================================ K-1
print('\n=== K-1')
k = 'k-1'
# P1
tri, sq = printed(k, 2, 'triangle'), printed(k, 2, 'square')
ok(tri == ['000'] and sq == ['111'], 'K-1 P1 key is triangle 000 / square 111')
ok(works(['000', '111']), 'K-1 P1: 000/111 always works -> the changer cannot fool the receiver')
print('   triangle outcomes', fmt(received('000')), ' square outcomes', fmt(received('111')))

# P2
p2 = page(k, 3)
keys3 = [s['contents'] for s in p2 if s['icon'] and s['cells'] == 3]
keys2 = [s['contents'] for s in p2 if s['icon'] and s['cells'] == 2]
rows3 = [s['contents'] for s in p2 if not s['icon'] and s['cells'] == 3]
rows2 = [s['contents'] for s in p2 if not s['icon'] and s['cells'] == 2]
ok(keys3 == ['000', '111'] and keys2 == ['00', '11'], 'K-1 P2 keys 000/111 and 00/11')
ok(rows3 == ['000', '101', '010', '111'] and rows2 == ['00', '01', '10', '11'], 'K-1 P2 final rows as transcribed')
dec = {}
for r in rows3:
    dec[r] = [n for n, w in [('triangle', '000'), ('square', '111')] if r in received(w)]
for r in rows2:
    dec[r] = [n for n, w in [('triangle', '00'), ('square', '11')] if r in received(w)]
print('   decodes:', dec)
q = quote('000 triangle; 101 square; 010 triangle; 111 square')
q = quote('00 triangle; 01 both pictures; 10 both pictures; 11 square')
ok(dec['000'] == ['triangle'] and dec['101'] == ['square'] and dec['010'] == ['triangle'] and dec['111'] == ['square'],
   'K-1 P2 guide decodes for the three-counter rows')
ok(dec['00'] == ['triangle'] and dec['01'] == dec['10'] == ['triangle', 'square'] and dec['11'] == ['square'],
   'K-1 P2 guide decodes for the two-counter rows; the two-counter key is the one that fails')

# P3
pairs2 = [(a, b) for a in words(2) for b in words(2)]
ok(not any(works([a, b]) for a, b in pairs2), 'K-1 P3: no ordered pair of two-counter rows works (16 pairs incl. equal rows)')

# P4
ok(len([s for s in page(k, 5) if s['icon'] == 'triangle']) == 6, 'K-1 P4 prints 6 key slots')
k4 = [(a, b) for a in words(3) for b in words(3) if works([a, b])]
print('   working ordered keys:', k4)
ok(len(k4) == 8 and all(dist(a, b) == 3 for a, b in k4), 'K-1 P4: exactly 8 ordered keys, each a row and its opposite')
quote('000/111, 001/110, 010/101, 011/100, 100/011, 101/010, 110/001, 111/000')
ok(sorted(k4) == sorted([tuple(x.split('/')) for x in '000/111, 001/110, 010/101, 011/100, 100/011, 101/010, 110/001, 111/000'.split(', ')]),
   'K-1 P4 guide list equals the computed list')

# P5
t5 = printed(k, 6, 'triangle')
ok(t5 == ['0011', '0100'] and printed(k, 6, 'square') == ['----', '----'], 'K-1 P5 triangles 0011, 0100 with blank square rows')
comp = {}
for a in t5:
    comp[a] = sorted(b for b in words(4) if '0' in b and '1' in b and works([a, b]))
    allp = sorted(b for b in words(4) if works([a, b]))
    print(f'   {a}: mixed partners {comp[a]}; all partners {allp}')
quote('For triangle 0011, the square may be 0100, 1000, 1100, 1101, or 1110')
quote('For triangle 0100, the square may be 0011, 1001, 1010, or 1011')
ok(comp['0011'] == ['0100', '1000', '1100', '1101', '1110'], 'K-1 P5 guide list for 0011 (5 rows) is complete and correct')
ok(comp['0100'] == ['0011', '1001', '1010', '1011'], 'K-1 P5 guide list for 0100 (4 rows) is complete and correct')
ok(flip('1011', 1) == '1111', 'K-1 P5 guide: changing 1011 in its second position gives 1111')
# Extension: every length-4 row has exactly 5 partners
ok(all(len([b for b in words(4) if works([a, b])]) == 5 for a in words(4)),
   'K-1 extension: every fixed length-4 row has exactly 5 reliable partners (complement and its 4 neighbours)')

# P6
k6 = [c for c in itertools.combinations(words(3), 3) if works(list(c))]
ok(k6 == [], 'K-1 P6: no three distinct three-counter rows work (all 56 triples fail)')
ok(all(b == ''.join('1' if x == '0' else '0' for x in a) for a, b in k4), 'K-1 P6 guide: two reliable three-counter rows are opposites')

# ================================================================ Grades 2-3
print('\n=== Grades 2-3')
g = 'grades-2-3'
p = page(g, 2)
key_strips = [s for s in p if s['icon']]
left = [s['contents'] for s in key_strips if s['x_cm'] < 10]
right = [s['contents'] for s in key_strips if s['x_cm'] > 10]
ok(left == ['000', '111'] and right == ['001', '101'], '2-3 P1 keys 000/111 and 001/101')
ok(works(['000', '111']) and not works(['001', '101']), '2-3 P1: 000/111 works, 001/101 fails')
print('   001/101 shared rows:', fmt(received('001') & received('101')))
ok(received('001') & received('101') == {'001', '101'}, '2-3 P1 guide witness: 001 is unchanged triangle or square 101 flipped at position 1')

p = page(g, 3)
lefts = [s['contents'] for s in p if s['x_cm'] < 10]
rights = [s['contents'] for s in p if s['x_cm'] > 10]
pairs = [(lefts[0], lefts[1]), (rights[0], rights[1]), (lefts[2], lefts[3]), (rights[2], rights[3])]
ok(pairs == [('0000', '0001'), ('0101', '0110'), ('0001', '1111'), ('0011', '1100')], '2-3 P2 four keys as transcribed')
for a, b in pairs:
    print(f'   {a}/{b}: distance {dist(a, b)}, common rows {fmt(received(a) & received(b))}')
quote('For 0000/0001, use 0000 (also 0001). For 0101/0110, use 0100 (also 0111). For 0001/1111, no common row. For 0011/1100, no common row.')
ok([received(a) & received(b) for a, b in pairs] == [{'0000', '0001'}, {'0100', '0111'}, set(), set()], '2-3 P2 guide answers (complete common sets)')
ok([dist(a, b) for a, b in pairs] == [1, 2, 3, 4], '2-3 P2 guide: the pairs differ in 1, 2, 3, 4 positions')

ok([s['cells'] for s in page(g, 4)] == [1, 1, 2, 2, 3, 3], '2-3 P3 prints length-1, -2, -3 slots')
mins = {}
for n in range(1, 6):
    if any(works([a, b]) for a, b in itertools.combinations(words(n), 2)):
        mins.setdefault('2pics_t1', n)
ok(mins['2pics_t1'] == 3, '2-3 P3: shortest two-picture key is length 3')

ok(len([s for s in page(g, 5) if s['icon'] == 'triangle']) == 4, '2-3 P4 prints 4 key slots')
bal = [(a, b) for a in words(4) for b in words(4) if a.count('1') == b.count('1') == 2 and works([a, b])]
print('   balanced working keys:', bal)
quote('0011/1100, 0101/1010, 0110/1001, 1001/0110, 1010/0101, 1100/0011')
ok(sorted(bal) == sorted(tuple(x.split('/')) for x in '0011/1100, 0101/1010, 0110/1001, 1001/0110, 1010/0101, 1100/0011'.split(', ')),
   '2-3 P4: exactly the guide\'s 6 ordered keys')
ok(all(dist(a, b) % 2 == 0 for a in words(4) for b in words(4) if a.count('1') == b.count('1') == 2),
   '2-3 P4 guide parity claim: two weight-2 rows differ in an even number of positions')

# P5 (also 4-5 P2)
ok([s['icon'] for s in page(g, 6)] == ['triangle', 'square', 'star', 'diamond'] and all(s['cells'] == 5 for s in page(g, 6)),
   '2-3 P5 prints four five-cell slots')
gk = ['00000', '00111', '11001', '11110']
ok(works(gk), '2-3 P5 / 4-5 P2 guide key 00000, 00111, 11001, 11110 works')
ds = [dist(a, b) for a, b in itertools.combinations(gk, 2)]
ok(ds == [3, 3, 4, 4, 3, 3], f'guide pairwise distances 3,3,4,4,3,3 (computed {ds})')
table = {
    '00000': '00000, 00001, 00010, 00100, 01000, 10000',
    '00111': '00011, 00101, 00110, 00111, 01111, 10111',
    '11001': '01001, 10001, 11000, 11001, 11011, 11101',
    '11110': '01110, 10110, 11010, 11100, 11110, 11111',
}
for w, lst in table.items():
    quote(lst)
    ok(set(lst.split(', ')) == received(w), f'guide p7 table row for {w} equals its received set')
allrec = set().union(*(received(w) for w in gk))
ok(len(allrec) == 24, 'the 24 received rows are distinct')
outside = sorted(set(words(5)) - allrec)
print('   rows outside the promise:', outside)
quote('01010, 01011, 01100, 01101, 10010, 10011, 10100, 10101')
ok(outside == '01010, 01011, 01100, 01101, 10010, 10011, 10100, 10101'.split(', '), 'guide p10: the 8 rows outside all outcome sets')
nkeys = sum(1 for c in itertools.permutations(words(5), 4) if works(list(c)))
nsets = sum(1 for c in itertools.combinations(words(5), 4) if works(list(c)))
print(f'   working four-picture length-5 keys: {nsets} unordered sets, {nkeys} ordered keys')

# P6 two changes
s6 = strips[g][6]['standalone_icons']
ok([s['icon'] for s in s6] == ['triangle', 'square', 'triangle', 'square'], '2-3 P6 prints two triangle/square answer-line pairs')
two = next(n for n in range(1, 8) if any(works([a, b], 2) for a, b in itertools.combinations(words(n), 2)))
ok(two == 5, '2-3 P6: shortest two-picture key for up to two changes is 5 (within the "at most five" limit)')
ok(works(['00000', '11111'], 2), '2-3 P6 guide key 00000/11111 works for two changes')
ok(all((w.count('1') >= 3) == (src == '11111') for src in ['00000', '11111'] for w in received(src, 2)),
   '2-3 P6 guide: majority decodes; triangle outcomes have <=2 filled, square outcomes >=3')
ok('0011' in received('0000', 2) & received('1111', 2), '2-3 P6 guide hint: 0011 comes from 0000 and 1111 with two changes')
ok(all(received(a, 2) & received(b, 2) for n in range(1, 5) for a, b in itertools.combinations(words(n), 2)),
   '2-3 P6 guide: every pair with d<=4 has a common row (halfway construction)')

# ================================================================ Grades 4-5
print('\n=== Grades 4-5')
h = 'grades-4-5'
p = page(h, 2)
lk = [s['contents'] for s in p if s['icon'] == 'triangle']
rk = [s['contents'] for s in p if s['icon'] == 'square']
ok(list(zip(lk, rk)) == [('00', '11'), ('000', '111'), ('0010', '0100')], '4-5 P1 keys 00/11, 000/111, 0010/0100')
claims = {
    '00': '00,01,10', '11': '01,10,11', '000': '000,001,010,100', '111': '011,101,110,111',
    '0010': '0000,0010,0011,0110,1010', '0100': '0000,0100,0101,0110,1100'}
for w, lst in claims.items():
    quote('{' + lst + '}')
    ok(set(lst.split(',')) == received(w), f'4-5 P1 guide set for {w}')
for a, b in zip(lk, rk):
    print(f'   {a}/{b}: shared {fmt(received(a) & received(b))} -> {"works" if works([a, b]) else "fails"}')
ok([works([a, b]) for a, b in zip(lk, rk)] == [False, True, False], '4-5 P1: only 000/111 works; 0010/0100 shares 0000 and 0110')

ok([s['icon'] for s in page(h, 3)] == ['triangle', 'square', 'star', 'diamond'] and all(s['cells'] == 5 for s in page(h, 3)),
   '4-5 P2 prints four five-cell slots (key checked under 2-3 P5)')

p = page(h, 4)
pa = sorted([s for s in p], key=lambda s: (s['x_cm'], s['y_cm']))
pairs = [(pa[0]['contents'], pa[1]['contents']), (pa[2]['contents'], pa[3]['contents'])]
ok(pairs == [('000000', '110000'), ('010010', '101010')], '4-5 P3 pairs as transcribed')
for a, b in pairs:
    print(f'   {a}/{b}: distance {dist(a, b)}, differing positions {[i + 1 for i in range(6) if a[i] != b[i]]}, common {fmt(received(a) & received(b))}')
ok(received('000000') & received('110000') == {'100000', '010000'}, '4-5 P3 guide: common observations 100000 and 010000')
ok(not (received('010010') & received('101010')) and [i for i in range(6) if '010010'[i] != '101010'[i]] == [0, 1, 2],
   '4-5 P3 guide: 010010/101010 differ in exactly the first three positions; no common row')
thr = all((not (received(a) & received(b))) == (dist(a, b) >= 3) for n in range(1, 8) for a in [ '0' * n] for b in words(n) if a != b)
ok(thr, '4-5 P3: for lengths 1..7, two rows are separable after one change iff they differ in >= 3 positions')
# General overview criterion, all pairs, n<=6, t<=3
gen = all((not (received(a, t) & received(b, t))) == (dist(a, b) >= 2 * t + 1)
          for n in range(1, 7) for t in range(0, 4) for a, b in itertools.combinations(words(n), 2))
ok(gen, 'overview: disjoint t-change outcome sets iff distance >= 2t+1 (all pairs, n<=6, t<=3)')

p = page(h, 5)
ok([s['contents'] for s in p] == ['010', '0110', '00111'], '4-5 P4 rows 010, 0110, 00111')
for lst, w in [('{000,010,011,110}', '010'), ('{0010,0100,0110,0111,1110}', '0110'),
               ('{00011,00101,00110,00111,01111,10111}', '00111')]:
    quote(lst)
    ok(set(lst.strip('{}').split(',')) == received(w), f'4-5 P4 guide set for {w}')
ok(all(len(received(w)) == n + 1 for n in range(1, 11) for w in [words(n)[0], words(n)[-1]]) and len(received('0' * 10)) == 11,
   '4-5 P4: a length-10 row has 11 received rows (n+1 for n=1..10)')

four = next(n for n in range(1, 7) if any(works(list(c)) for c in itertools.combinations(words(n), 4)))
ok(four == 5, '4-5 P5: shortest length for four pictures is 5')
ok(all(4 * (n + 1) > 2 ** n for n in range(1, 5)) and 4 * 6 <= 32, '4-5 P5 guide counting: 4(n+1) > 2^n for n=1..4')

ok([s['cells'] for s in page(h, 7)] == [4, 4, 4], '4-5 P6 prints three four-entry slots')
c34 = [c for c in itertools.combinations(words(4), 3) if works(list(c))]
ok(c34 == [] and 3 * 5 <= 16, '4-5 P6: no three-row length-4 key works, although 3*5 <= 16')
# guide argument for P6 and overview pairwise-sum argument
ok(all(sum(dist(a, b) for a, b in itertools.combinations(c, 2)) <= 2 * 4 for c in itertools.combinations(words(4), 3)),
   'overview: sum of the three pairwise distances among three length-4 rows is at most 8')
ok(all({i for i in range(4) if B[i] != C[i]} == {i for i in range(4) if (B[i] == A[i]) != (C[i] == A[i])}
       for A in words(4) for B in words(4) for C in words(4)),
   '4-5 P6 guide: B and C disagree exactly where exactly one of them agrees with A')

# guide p8 decoding example
ok([w for w in gk if dist('00101', w) <= 1] == ['00111'], 'guide p8: 00101 decodes to square 00111 only')
# guide p3 diagram
ok(flip('00', 1) == '01' and flip('11', 0) == '01', 'guide p3 diagram: 00 flip right and 11 flip left both give 01')

# packing bound: necessary, not sufficient
print('\n=== Packing bound vs actual maximum (one change)')
for n in range(1, 7):
    best = 0
    W = words(n)
    # greedy-free exact search for max code size with d>=3 (small n)
    def extend(code, start):
        global best
        best = max(best, len(code))
        for i in range(start, len(W)):
            if all(dist(W[i], c) >= 3 for c in code):
                extend(code + [W[i]], i + 1)
    extend([], 0)
    print(f'   n={n}: max pictures {best}, packing bound floor(2^n/(n+1)) = {2 ** n // (n + 1)}')

print('\nFAILURES:', len(FAILS))
for f in FAILS:
    print('  ', f)
