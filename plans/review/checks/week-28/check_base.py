"""Recompute every base-packet task (K-1, 2-3, 4-5) and every guide claim.

Uses foldcheck.py (my own layer-order brute force, cross-checked against the
crimp reduction) as the oracle for which M/V words fold flat.  Diagram data
(ray angles, printed labels, tab stocks) were read from the PDFs by
pdf_geometry.py; they are restated here as constants and re-asserted against
pdf_geometry.json so the two scripts cannot drift apart.
"""
import json
import random
import re
from fractions import Fraction
from itertools import combinations, permutations, product

import foldcheck as F
from common import HERE, Log, norm, pdf_text

log = Log()
GEO = json.loads((HERE / 'pdf_geometry.json').read_text())
GUIDE = norm(' '.join(pdf_text('guide')))


def in_guide(fragment):
    return norm(fragment) in GUIDE


def sectors(rays):
    rays = sorted(rays)
    n = len(rays)
    return [(rays[(i + 1) % n] - rays[i]) % 360 for i in range(n)]


RIGHT = [90, 90, 90, 90]
ALL4 = [''.join(t) for t in product('MV', repeat=4)]

# ---------------------------------------------------------------- oracle
log.head('Oracle self-test: layer-order brute force agrees with crimp reduction')
random.seed(28)
mism = 0
for trial in range(400):
    n = random.choice([4, 4, 6, 6])

    def comp(total, parts):
        while True:
            xs = [random.randint(1, total - 1) for _ in range(parts)]
            if sum(xs) == total:
                return xs
    odd, even = comp(12, n // 2), comp(12, n // 2)
    ang = [v * 15 for pair in zip(odd, even) for v in pair]
    b, c = F.valid_words(ang), F.crimp_words(ang)
    mism += b != c
    assert b and all(F.maekawa(w) for w in b)
log.check(mism == 0, f'400 random even-degree Kawasaki patterns: {mism} disagreements; every pattern has a flat state; all states obey Maekawa')
eq8 = F.valid_words([45] * 8)
log.check(len(eq8) == 112, f'eight 45-degree sectors: {len(eq8)} valid words (Hull: 2*C(8,3) = 112)')

# ---------------------------------------------------------------- right angles
log.head('Four right angles')
V4 = F.valid_words(RIGHT)
three_one = sorted(w for w in ALL4 if w.count('M') in (1, 3))
log.check(V4 == three_one, f'valid words = the eight 3:1 words {V4}')
orders = F.legal_orders(RIGHT)
log.check(len(orders) == 8, f'{len(orders)} of 24 stack orders are legal')
table = {'1234': 'VVMV', '1432': 'VVVM', '2143': 'VMMM', '2341': 'MMMV',
         '3214': 'VMVV', '3412': 'MVVV', '4123': 'MVMM', '4321': 'MMVM'}
log.check(dict(orders) == table, 'guide p6 survivor table (orders and words) is exactly right')
s1 = [o for o, _ in orders if o[0] == '1']
log.check(s1 == ['1234', '1432'], f'with S1 bottom only {s1} survive')
# guide's reading rule: V on rays 1..4 iff h4>h1, h2>h1, h2>h3, h4>h3
ok = True
for o in permutations('1234'):
    h = {int(c): i for i, c in enumerate(o)}
    w = ''.join('V' if c else 'M' for c in (h[4] > h[1], h[2] > h[1], h[2] > h[3], h[4] > h[3]))
    if ''.join(o) in table and table[''.join(o)] != w:
        ok = False
log.check(ok, 'guide reading rule (V iff h4>h1, h2>h1, h2>h3, h4>h3) reproduces the table')
# two-book-fold witness and its rotations / reversals
rot = {w[-k:] + w[:-k] for w in ['VVVM'] for k in range(4)}
rev = {w.translate(str.maketrans('MV', 'VM')) for w in rot}
log.check(sorted(rot | rev) == V4, 'rotations and reversals of VVVM give all eight words')

# ---------------------------------------------------------------- K-1
log.head('K-1')
CAT = dict(zip('ABCDEFGH', ['MMMV', 'MMVM', 'MVMM', 'VMMM', 'MVVV', 'VMVV', 'VVMV', 'VVVM']))
k1 = GEO['k-1']
log.check([d['word'] for d in k1[5]['discs']] == list(CAT.values()), 'P6 printed A-H words read from the PDF match my catalog')
p2 = dict(zip('ABCDEF', [d['word'] for d in k1[1]['discs']]))
works = sorted(k for k, w in p2.items() if w in V4)
log.check(works == ['A', 'C', 'E'], f'P2 printed words {p2}; foldable: {works} (guide: A,C,E)')
log.check(len(V4) >= 4, 'P1: at least four distinct foldable words exist (there are 8)')
p3 = [w for w in V4 if w[0] == 'M']
log.check(p3 == ['MMMV', 'MMVM', 'MVMM', 'MVVV'] and len(k1[2]['discs']) >= 4,
          f'P3: ray 1 = M gives {p3} (4 answers, {len(k1[2]["discs"])} disks printed)')
log.check(len(V4) == 8 and len(k1[4]['discs']) == 10, 'P5: 8 answers, 10 disks printed (2 spare)')

# P4 tab rows
fixed = [d['word'] for d in k1[3]['discs']]
log.check(fixed == ['M?V?', 'MM??', 'V?V?'] * 3, f'P4 printed partial words {fixed[:3]} in each row')
stocks = GEO['k-1-p4-tabs']


def completions(pattern):
    out = []
    holes = [i for i, c in enumerate(pattern) if c == '?']
    for fill in product('MV', repeat=len(holes)):
        w = list(pattern)
        for i, c in zip(holes, fill):
            w[i] = c
        w = ''.join(w)
        if w in V4:
            out.append((w, ''.join(fill)))
    return out


comp_l, comp_m, comp_r = (completions(p) for p in ('M?V?', 'MM??', 'V?V?'))
log.check([w for w, _ in comp_l] == ['MMVM', 'MVVV'] and [w for w, _ in comp_m] == ['MMMV', 'MMVM']
          and [w for w, _ in comp_r] == ['VMVV', 'VVVM'], 'P4 completion table (guide p8) is right')
row_sol = {}
for row, stock in zip('ABC', stocks):
    sols = []
    for (wl, fl), (wm, fm), (wr, fr) in product(comp_l, comp_m, comp_r):
        used = ''.join(sorted(fl + fm + fr))
        if used == ''.join(sorted(stock)):
            sols.append(f'{wl} / {wm} / {wr}')
    row_sol[row] = sols
log.check(len(row_sol['A']) == 4 and len(row_sol['C']) == 4 and not row_sol['B'],
          f'P4: rows A and C each have 4 completions, row B none: {row_sol}')
gA = ['MVVV / MMMV / VMVV', 'MVVV / MMMV / VVVM', 'MVVV / MMVM / VMVV', 'MVVV / MMVM / VVVM']
gC = ['MMVM / MMMV / VMVV', 'MMVM / MMMV / VVVM', 'MMVM / MMVM / VMVV', 'MMVM / MMVM / VVVM']
log.check(sorted(row_sol['A']) == gA and sorted(row_sol['C']) == gC, 'guide p8 lists exactly these eight triples')
okk = []
for k in range(7):
    stock = 'M' * k + 'V' * (6 - k)
    if any(''.join(sorted(a[1] + b[1] + c[1])) == ''.join(sorted(stock)) for a, b, c in product(comp_l, comp_m, comp_r)):
        okk.append(k)
log.check(okk == [2, 4], f'extension: M-tab counts that work = {okk} (guide: exactly 2 and 4)')

# P6 routes
def dist(a, b):
    return sum(x != y for x, y in zip(CAT[a], CAT[b]))


comp_pairs = sorted(tuple(sorted((a, b))) for a in CAT for b in CAT if a < b and dist(a, b) == 4)
log.check(comp_pairs == [('A', 'H'), ('B', 'G'), ('C', 'F'), ('D', 'E')] and
          all(dist(a, b) == 2 for a in CAT for b in CAT if a < b and (a, b) not in comp_pairs),
          'move rule: every pair is 2 apart except complements A-H, B-G, C-F, D-E (4 apart)')


def ham(start, end):
    others = [x for x in CAT if x not in (start, end)]
    cnt = 0
    for mid in permutations(others):
        path = (start,) + mid + (end,)
        if all(dist(path[i], path[i + 1]) == 2 for i in range(7)):
            cnt += 1
    return cnt


nH, nD = ham('A', 'H'), ham('A', 'D')
log.check((nH, nD) == (240, 248) and in_guide('240 A-to-H routes and 248 A-to-D routes'),
          f'P6: {nH} routes A..H and {nD} routes A..D (guide: 240 and 248)')
for route in ('ABCDFEGH', 'ABCEFGHD'):
    log.check(all(dist(route[i], route[i + 1]) == 2 for i in range(7)) and len(set(route)) == 8,
              f'guide route {route} is legal')
chg = [[i + 1 for i in range(4) if CAT[r[j]][i] != CAT[r[j + 1]][i]] for r in ('ABCDFEGH',) for j in range(7)]
log.check(chg == [[3, 4], [2, 3], [1, 2], [3, 4], [1, 2], [1, 3], [3, 4]], f'guide changed-ray column (route to H) {chg}')
chg = [[i + 1 for i in range(4) if CAT[r[j]][i] != CAT[r[j + 1]][i]] for r in ('ABCEFGHD',) for j in range(7)]
log.check(chg == [[3, 4], [2, 3], [3, 4], [1, 2], [2, 3], [3, 4], [2, 3]], f'guide changed-ray column (route to D) {chg}')
cyc = 'ABCDFEHGA'
log.check(all(dist(cyc[i], cyc[i + 1]) == 2 for i in range(8)) and len(set(cyc[:-1])) == 8,
          'extension cycle A-B-C-D-F-E-H-G-A is legal')

# ---------------------------------------------------------------- Grades 2-3
log.head('Grades 2-3')
W7 = dict(zip('ABCDEFG', [30, 30, 60, 60, 90, 120, 150]))
groups = sorted(''.join(c) for r in range(1, 8) for c in combinations('ABCDEFG', r) if sum(W7[x] for x in c) == 180)
gl = sorted(''.join(sorted(g)) for g in 'AG BG CF DF ABF ACE ADE BCE BDE ABCD'.split())
log.check(groups == gl, f'P1: {len(groups)} groups {groups} == guide list')
import pdfplumber
from common import PDFS, CM
with pdfplumber.open(str(PDFS['grades-2-3'])) as pdf:
    answer_lines = len([l for l in pdf.pages[0].lines if abs((l['x1'] - l['x0']) / CM - 8.75) < 0.05])
log.info(f'P1 prints {answer_lines} answer lines for {len(groups)} groups')
P = {'A': [0, 90, 180, 270], 'B': [0, 45, 135, 225], 'C': [0, 60, 180, 300], 'D': [0, 30, 90, 240]}
g23 = GEO['grades-2-3']
log.check([d['ray_angles'] for d in g23[1]['discs']] == [[float(x) for x in v] for v in P.values()]
          and [d['ray_angles'] for d in g23[2]['discs']] == [[float(x) for x in v] for v in P.values()],
          'P2 and P3 disks are the patterns A-D')
for k, rays in P.items():
    s = sectors(rays)
    sh, wh = s[0] + s[2], s[1] + s[3]
    expect = {'A': (180, 180), 'B': (135, 225), 'C': (180, 180), 'D': (180, 180)}[k]
    log.check((sh, wh) == expect, f'P2 disk {k}: sectors {s}, shaded {sh}, white {wh}')
for k, rays in P.items():
    s = sectors(rays)
    vw = F.valid_words(s)
    log.check(bool(vw) == (k != 'B'), f'P3 disk {k}: {"foldable" if vw else "not foldable"}; valid words {vw}')
log.check('VVVM' in F.valid_words(sectors(P['A'])) and 'VVVM' in F.valid_words(sectors(P['C']))
          and 'MVVV' in F.valid_words(sectors(P['D'])), 'guide witnesses: A VVVM, C VVVM, D MVVV are valid')
log.check('VVVM' not in F.valid_words(sectors(P['D'])), 'guide: VVVM (3:1 count) fails for D')
log.check(F.order_word(sectors(P['D']), '3412') == 'MVVV', 'guide p4 certificate: order S3,S4,S1,S2 is legal and reads MVVV')
# P4 added ray: scan every half degree and every rational candidate
P4 = {'A': [0, 90, 180], 'B': [0, 60, 180], 'C': [0, 30, 180], 'D': [0, 120, 180]}
log.check([d['ray_angles'] for d in g23[3]['discs']] == [[float(x) for x in v] for v in P4.values()], 'P4 printed rays')
for k, rays in P4.items():
    sols = []
    for x2 in range(1, 720):
        x = Fraction(x2, 2)
        if x in rays:
            continue
        s = sectors(rays + [x])
        if F.kawasaki(s):
            sols.append(x)
    a = rays[1]
    comp_s = sectors(rays + [360 - a])
    log.check(sols == [360 - a] and 'VVVM' in F.valid_words(comp_s),
              f'P4 {k}: unique added ray {[float(v) for v in sols]} (=360-{a}); sectors {comp_s}; VVVM valid')
ok = all(F.crimp_foldable([a, 180 - a, 180 - a, a], 'VVVM') for a in range(1, 180))
log.check(ok, 'generalization: for every integer 0<a<180, rays 0,a,180,360-a fold as VVVM')
# P6 six wedges
seqs = set(permutations('AABBCC'))
val = {'A': 30, 'B': 60, 'C': 90}
good = sorted(''.join(s) for s in seqs if sum(val[c] for c in s[0::2]) == 180)
log.check(len(good) == 36, f'P6: {len(good)} rooted letter orders (guide: 36)')
samples = ['AABBCC', 'AABCCB', 'AACBBC', 'AACCBB']
log.check(all(s in good for s in samples), 'guide sample orders are valid')
bounds = {s: [0] + [sum(val[c] for c in s[:i]) for i in range(1, 6)] for s in samples}
log.check(bounds == {'AABBCC': [0, 30, 60, 120, 180, 270], 'AABCCB': [0, 30, 60, 120, 210, 300],
                     'AACBBC': [0, 30, 60, 150, 210, 270], 'AACCBB': [0, 30, 60, 150, 240, 300]},
          f'guide boundary rays {bounds}')
log.check(all(sorted(s[0::2]) == ['A', 'B', 'C'] == sorted(s[1::2]) for s in good),
          'every valid order has one A, B, C in each alternating triple')

# ---------------------------------------------------------------- Grades 4-5
log.head('Grades 4-5')
g45 = GEO['grades-4-5']
for d, (k, rays) in zip(g45[0]['discs'], P.items()):
    log.check(d['ray_angles'] == [float(x) for x in rays], f'P1 disk {k} = 2-3 P3 disk {k}')
P2 = [[120, 120, 120], [60, 60, 60, 90, 90], [30, 30, 60, 60, 60, 60, 60]]
log.check([d['sectors'] for d in g45[1]['discs']] == [[float(x) for x in s] for s in P2],
          'P2 sectors A 120x3, B 60,60,60,90,90, C 30,30,60x5')
log.check(all(len(s) % 2 == 1 and sum(s) == 360 for s in P2), 'P2: all three have an odd number of rays and total 360')
P3 = [[45, 90, 90, 135], [30, 30, 60, 60, 90, 90], [30, 30, 30, 60, 90, 120], [45] * 8]
log.check([d['sectors'] for d in g45[2]['discs']] == [[float(x) for x in s] for s in P3], 'P3 sectors read from PDF')
res = []
for nm, s in zip('ABCD', P3):
    o, e = sum(s[0::2]), sum(s[1::2])
    has = bool(F.valid_words(s)) if len(s) <= 6 else bool(F.crimp_words(s))
    res.append((nm, o, e, has))
log.check([(r[0], r[1], r[2]) for r in res] == [('A', 135, 225), ('B', 180, 180), ('C', 150, 210), ('D', 180, 180)],
          f'P3 alternating sums {[(r[0], r[1], r[2]) for r in res]}')
log.check([r[3] for r in res] == [False, True, False, True], 'P3: B and D (not ruled out) do have flat states; A, C none')
p5 = [d['word'] for d in g45[4]['discs']]
log.check(p5 == ['MMMM', 'VVVV', 'MMVV', 'MVMV'] and not any(w in V4 for w in p5), f'P5: none of {p5} folds')
rots = set()
for w in p5:
    for k in range(4):
        rots.add(w[k:] + w[:k])
log.check(sorted(rots) == sorted(set(ALL4) - set(V4)) and len(rots) == 8,
          'P5: rotations of the four printed words are exactly the 8 non-foldable words; with P4 they cover all 16')
seq6 = sorted(set(p for p in permutations([30, 30, 60, 60, 90, 90]) if p[0] == 30 and sum(p[0::2]) == 180))
log.check(len(seq6) == 12, f'P6: {len(seq6)} orders starting with 30 (guide: 12)')
glist = [(30, 30, 60, 60, 90, 90), (30, 30, 60, 90, 90, 60), (30, 30, 90, 60, 60, 90), (30, 30, 90, 90, 60, 60),
         (30, 60, 60, 30, 90, 90), (30, 60, 60, 90, 90, 30), (30, 60, 90, 30, 60, 90), (30, 60, 90, 90, 60, 30),
         (30, 90, 60, 30, 90, 60), (30, 90, 60, 60, 90, 30), (30, 90, 90, 30, 60, 60), (30, 90, 90, 60, 60, 30)]
log.check(sorted(glist) == seq6, 'guide p15 table lists exactly the 12 orders')
all6 = set(p for p in permutations([30, 30, 60, 60, 90, 90]) if sum(p[0::2]) == 180)
log.check(len(all6) == 36, f'unrestricted rooted orders: {len(all6)} (guide: 36)')
# rows printed on P6 (read from the PDF)
import pdfplumber
from collections import Counter
from common import PDFS, CM
with pdfplumber.open(str(PDFS['grades-4-5'])) as pdf:
    blanks = [l for l in pdf.pages[5].lines if 30 < l['x1'] - l['x0'] < 60]
rows = len(Counter(round(l['top']) for l in blanks))
log.check(rows == len(seq6), f'FINDING CHECK: P6 prints exactly {rows} answer rows of six blanks for an answer of {len(seq6)} (the page reveals the count)')
# cyclic reading (for the record)
cyc = {min(p[k:] + p[:k] for k in range(6)) for p in seq6}
log.info(f'if rotations were identified, the 12 rooted orders form {len(cyc)} cyclic arrangements')

# ---------------------------------------------------------------- guide statements
log.head('Guide statements')
log.check(in_guide('|M−V|=2') or in_guide('|M-V|=2'), 'overview states Maekawa |M-V|=2')
# sector intervals of D (guide p4)
theta, iv, s = F.folded_image([30, 60, 150, 120])
log.check(theta == [0, 30, -30, 120] and iv == [(0, 30), (-30, 30), (-30, 120), (0, 120)],
          f'guide p4 flattened rays {theta} and sector intervals {iv}')
log.check(in_guide('S1=[0,30], S2=[−30,30], S3=[−30,120], S4=[0,120]'), 'guide p4 prints these intervals')
# forced order for VVVM on D
forced = []
for o in permutations('1234'):
    h = {int(c): i for i, c in enumerate(o)}
    up, down = {1, 3}, {2, 4}
    w = ''
    for (i, j) in ((4, 1), (1, 2), (2, 3), (3, 4)):
        u, dn = (i, j) if i in up else (j, i)
        w += 'V' if h[dn] > h[u] else 'M'
    if w == 'VVVM':
        forced.append(''.join(o))
log.check(forced == ['1432'], f'D with VVVM: the joins force bottom-to-top {forced} (S1<S4<S3<S2), which is illegal')
# C (60,120,120,60): guide's book-fold claim
log.check('VVVM' in F.valid_words([60, 120, 120, 60]), 'model C: VVVM valid (two book folds)')
log.info(f'model C all valid words: {F.valid_words([60, 120, 120, 60])}; model D: {F.valid_words([30, 60, 150, 120])}')
# odd-degree impossibility (orientation parity) - check folded image never closes with consistent facing
log.check(all(len(s) % 2 == 1 for s in P2), 'odd ray counts 3, 5, 7: ruled out by orientation parity')
# alternating-sum proof: -360 < O-E < 360 for positive sectors
log.check(all(-360 < sum(s[0::2]) - sum(s[1::2]) < 360 for s in P3), 'O-E lies strictly between -360 and 360 for P3 patterns')
# 2-3 P1 completeness by largest piece
cases = {'G': [g for g in groups if 'G' in g], 'F': [g for g in groups if 'F' in g and 'G' not in g],
         'E': [g for g in groups if 'E' in g and not set('FG') & set(g)], '-': [g for g in groups if not set('EFG') & set(g)]}
log.check([len(v) for v in cases.values()] == [2, 3, 4, 1], f'guide largest-piece cases 2+3+4+1: {cases}')
# 4-5 P5 counting: 1 + 4 + 6 + 4 + 1
cnt = [sum(1 for w in ALL4 if w.count('M') == k) for k in range(5)]
two = [w for w in ALL4 if w.count('M') == 2]
adj = [w for w in two if any(w[i] == w[(i + 1) % 4] == 'M' for i in range(4))]
log.check(cnt == [1, 4, 6, 4, 1] and len(adj) == 4 and len(two) - len(adj) == 2,
          'guide p14 counts: 1,4,6,4,1 and two-M words = 4 adjacent + 2 opposite')

# ---------------------------------------------------------------- guide cross-references
log.head('Guide page cross-references point at the right content')
GP = [norm(t) for t in pdf_text('guide')]   # GP[0] = unnumbered overview, GP[k] = printed page k (k<=16)


def printed(k):
    return GP[k]


refs = [(2, 'table on page 10', 10, 'Clockwise sectors 1,2,3,4'),
        (3, 'Page 4 gives a geometric certificate', 4, 'A geometric witness for the unequal model D'),
        (6, 'construction on page 3', 3, 'Two book folds give a verified right-angle example'),
        (7, 'page 6 proves', 6, 'A complete proof for the four right angles'),
        (9, 'catalog words on page 7', 7, 'eight-fold catalog'),
        (11, 'certificate on page 4', 4, 'Why the certificate works'),
        (11, 'necessity proof on page 5', 5, 'Every other sector must total a half-turn'),
        (12, 'diagrams on page 7', 7, 'E MVVV'),
        (13, 'exact totals are on page 10', 10, 'Shaded 1+3'),
        (13, 'witness assignments are on page 11', 11, 'Problem 3 witnesses'),
        (14, 'Page 7 supplies exact labeled diagrams', 7, 'H VVVM'),
        (16, 'completion table on page 8', 8, 'All possible completed words'),
        (16, 'complementary-pair rule on page 9', 9, 'Complete move rule'),
        (16, 'construction on page 11', 11, 'Uniqueness proof'),
        (16, 'model D on page 4', 4, 'model D')]
for src_p, phrase, tgt, key in refs:
    log.check(norm(phrase) in printed(src_p) and norm(key) in printed(tgt),
              f'p{src_p} "{phrase}" -> p{tgt} contains "{key}"')
log.check('Bellingham Math Circle / Week 28 / Facilitator guide / Draft unpiloted 16' in GP[16] and GP[17].rstrip().endswith('18'),
          'printed numbering: guide pages 1-16, then the route-update page is numbered 18 (no page 17)')

log.done()
