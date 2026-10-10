"""Check every task of the Week 28 bonus companion and its adult guide.

Point positions are read from the delivered bonus PDF (pdfplumber) and
converted to the 6x6 diagram units the bonus guide uses; they are compared
with the TikZ source.  The mathematics (perpendicular bisectors, strip layer
orders, reflected punch patterns) is recomputed from scratch.
"""
import math
import re
from fractions import Fraction as Fr
from itertools import permutations

import pdfplumber

from common import PDFS, TEX, Log, norm, pdf_text

log = Log()
BG = norm(' '.join(pdf_text('bonus-guide')))


def in_bg(s):
    return norm(s) in BG


def r1(v):
    return round(v + 0.0, 2)


pdf = pdfplumber.open(str(PDFS['bonus']))

# ------------------------------------------------------------------ P1
log.head('Problem 1: one crease for two alignments')
p = pdf.pages[0]
squares = sorted([r for r in p.rects if r['x1'] - r['x0'] > 100], key=lambda r: (round(r['top']), r['x0']))
words = p.extract_words()
cases = []
for sq in squares:
    side = sq['x1'] - sq['x0']
    u = side / 6
    pts = {}
    for c in p.curves:
        cx, cy = (c['x0'] + c['x1']) / 2, (c['top'] + c['bottom']) / 2
        if c['x1'] - c['x0'] < 6 and sq['x0'] < cx < sq['x1'] and sq['top'] < cy < sq['bottom']:
            # label is the word just above-right of the dot
            lab = min(words, key=lambda w: math.hypot(w['x0'] - cx, w['bottom'] - cy))['text']
            pts[lab] = (r1((cx - sq['x0']) / u), r1((sq['bottom'] - cy) / u))
    cases.append(pts)
    log.info(f'square side {side / (72 / 2.54):.2f} cm: {dict(sorted(pts.items()))}')
exp = [{'P': (1, 1), 'Q': (5, 1), 'R': (2, 4), 'S': (4, 4)},
       {'P': (1, 1), 'Q': (5, 1), 'R': (1, 4), 'S': (4, 4)},
       {'P': (1, 1), 'Q': (5, 1), 'R': (2, 4), 'S': (4, 4), 'T': (3, 5)},
       {'P': (1, 1), 'Q': (5, 1), 'R': (2, 4), 'S': (4, 4), 'T': (2, 5)}]
log.check(cases == exp, 'PDF dot positions equal the guide/source coordinates for all four squares')
src = TEX['bonus'].read_text()
log.check(all(s in src for s in ('P/1/1,Q/5/1,R/2/4,S/4/4}', 'P/1/1,Q/5/1,R/1/4,S/4/4}', 'T/3/5', 'T/2/5')),
          'TikZ source has the same points')


def bisector(a, b):
    """Line {X : n.X = c} equidistant from a and b."""
    n = (Fr(b[0]) - a[0], Fr(b[1]) - a[1])
    mid = ((Fr(a[0]) + b[0]) / 2, (Fr(a[1]) + b[1]) / 2)
    return n, n[0] * mid[0] + n[1] * mid[1]


def same_line(l1, l2):
    (a, b), c = l1
    (d, e), f = l2
    return a * e - b * d == 0 and a * f - d * c == 0 and b * f - e * c == 0


def reflect(pt, line):
    (a, b), c = line
    x, y = Fr(pt[0]), Fr(pt[1])
    t = (a * x + b * y - c) / (a * a + b * b)
    return (x - 2 * a * t, y - 2 * b * t)


def side_of(pt, line):
    (a, b), c = line
    return (a * pt[0] + b * pt[1] - c)


answers = []
for i, pts in enumerate(cases, 1):
    lpq, lrs = bisector(pts['P'], pts['Q']), bisector(pts['R'], pts['S'])
    common = same_line(lpq, lrs)
    xpq = lpq[1] / lpq[0][0]
    xrs = lrs[1] / lrs[0][0]
    note = f'case {i}: P/Q force x={float(xpq)}, R/S force x={float(xrs)}'
    if 'T' in pts and common:
        t = pts['T']
        on = side_of(t, lpq) == 0
        p_side = (side_of(t, lpq) > 0) == (side_of(pts['P'], lpq) > 0)
        moved = reflect(t, lpq)
        note += f'; T={t} on crease: {on}; on P side: {p_side}; image if P side moves: {tuple(float(v) for v in moved)}'
        works_P_moves = on
        works_Q_moves = on or p_side
        answers.append((common, works_P_moves, works_Q_moves))
    else:
        answers.append((common, common, common))
    log.info(note)
log.check(answers == [(True, True, True), (False, False, False), (True, True, True), (True, False, True)],
          'case 1 x=3 works; case 2 no common crease (3 vs 2.5); case 3 works (T on crease); '
          'case 4 fails only if the P half is the half that moves')
log.check(in_bg('crease x=3 works') and in_bg('force x=2.5') and in_bg('moves it to (4,5)'),
          'bonus guide states x=3, x=2.5 and T->(4,5)')
log.check(in_bg('A mark on the stationary Q half would stay fixed off the crease'),
          'bonus guide itself notes that a stationary-half mark stays fixed (the reading that makes case 4 work)')
stu1 = norm(pdf_text('bonus')[0])
log.check('brings P onto Q' in stu1 and 'stationary' not in stu1 and 'Keep' not in stu1,
          'student P1 text fixes the moving half only through the phrase "brings P onto Q"')

# ------------------------------------------------------------------ P2, P3: strips
log.head('Problems 2-3: strip layer orders')


def legal_strip(order, joins):
    """order: top-to-bottom string; joins: list of (pair, end).  All panels
    occupy the same square; a join at one end may not interleave with
    another join at the same end.  Free panel ends impose no constraint."""
    pos = {c: i for i, c in enumerate(order)}
    by_end = {}
    for (a, b), end in joins:
        lo, hi = sorted((pos[a], pos[b]))
        by_end.setdefault(end, []).append((lo, hi))
    for end, ivs in by_end.items():
        for i in range(len(ivs)):
            for j in range(i + 1, len(ivs)):
                (a, b), (c, d) = ivs[i], ivs[j]
                if (a < c < b) != (a < d < b):
                    return False
    return True


three = [''.join(o) for o in permutations('ABC') if legal_strip(o, [('AB', 'L'), ('BC', 'R')])]
log.check(sorted(three) == ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'], f'P2: all six orders are legal {three}')
# directions relative to B's original front (B face up): an outer panel folded toward the front lies above B
dirs = {}
for o in three:
    pos = {c: i for i, c in enumerate(o)}  # 0 = top
    da = 'front' if pos['A'] < pos['B'] else 'back'
    dc = 'front' if pos['C'] < pos['B'] else 'back'
    dirs.setdefault((da, dc), []).append(o)
log.check(dirs == {('front', 'front'): ['ACB', 'CAB'], ('back', 'back'): ['BAC', 'BCA'],
                   ('front', 'back'): ['ABC'], ('back', 'front'): ['CBA']},
          f'P2: direction pairs -> orders {dirs}; same directions give two orders')
log.check(in_bg("both outer panels toward B's front give ACB/CAB") and in_bg('A toward front and C toward back gives ABC'),
          'bonus guide P2 mapping matches')
four = sorted(''.join(o) for o in permutations('ABCD') if legal_strip(o, [('AB', 'L'), ('CD', 'L'), ('BC', 'R')]))
gv = 'ABCD, ABDC, ACDB, ADCB, BACD, BADC, BCDA, BDCA, CABD, CBAD, CDAB, CDBA, DABC, DBAC, DCAB, DCBA'.split(', ')
gx = 'ACBD, ADBC, BCAD, BDAC, CADB, CBDA, DACB, DBCA'.split(', ')
log.check(four == gv, f'P3: {len(four)} legal orders, exactly the guide list')
log.check(sorted(set(''.join(o) for o in permutations('ABCD')) - set(four)) == sorted(gx), 'P3: guide excluded list is the other 8')
rev = all((o[::-1] in four) == (o in four) for o in (''.join(x) for x in permutations('ABCD')))
log.check(rev, 'turning the stack over (reversing a word) preserves legality, as the guide says')
# 3-panel table rows
p2 = pdf.pages[1]
log.info(f'P2 table has {len([t for t in p2.find_tables()])} table(s); rows: {[len(t.rows) for t in p2.find_tables()]}')

# ------------------------------------------------------------------ P4, P5: punches
log.head('Problems 4-5: punch patterns')


def holes(page_no):
    pg = pdf.pages[page_no]
    sqs = sorted([r for r in pg.rects if abs((r['x1'] - r['x0']) - 132.7) < 1], key=lambda r: r['x0'])
    out = []
    for sq in sqs:
        u = (sq['x1'] - sq['x0']) / 6
        cx0, cy0 = (sq['x0'] + sq['x1']) / 2, (sq['top'] + sq['bottom']) / 2
        hs = []
        for c in pg.curves:
            if 3 < c['x1'] - c['x0'] < 5:
                x, y = (c['x0'] + c['x1']) / 2, (c['top'] + c['bottom']) / 2
                if sq['x0'] < x < sq['x1'] and sq['top'] < y < sq['bottom']:
                    hs.append((round((x - cx0) / u, 2), round((cy0 - y) / u, 2)))
        out.append(sorted(hs))
    return out


def orbit(p, q, diag=False):
    pts = {(sx * p, sy * q) for sx in (1, -1) for sy in (1, -1)}
    if diag:
        pts |= {(y, x) for x, y in pts}
    return sorted((round(x, 2), round(y, 2)) for x, y in pts)


def single_punch(hs, diag):
    """Return (p, q) with p, q > 0 (and p > q if diag) whose orbit is hs, else None."""
    for x, y in hs:
        if x > 0 and y > 0 and (not diag or x > y):
            if orbit(x, y, diag) == sorted(hs):
                return (x, y)
    return None


h4 = holes(3)
log.info(f'P4 hole centres (units, square [-3,3]^2): {h4}')
r4 = [single_punch(h, False) for h in h4]
log.check(r4 == [(1.7, 0.9), (1.2, 1.2), None], f'P4: patterns 1, 2 come from punches {r4[:2]}; pattern 3 from none')
log.check(in_bg('Patterns 1/2 are possible at (1.7,0.9) and (1.2,1.2)'), 'bonus guide P4 positions match')
h5 = holes(4)
log.info(f'P5 hole centres: {h5}')
r5 = [single_punch(h, True) for h in h5]
log.check(r5 == [(1.7, 0.9), (1.8, 0.7), None], f'P5: patterns 1, 2 from punches {r5[:2]}; pattern 3 from none')
log.check(sorted(h5[2]) == sorted(orbit(1.7, 0.8) + orbit(0.7, 1.4)) and (0.8, 1.7) not in h5[2],
          'P5 pattern 3 = midline orbits of (1.7,0.8) and (0.7,1.4); diagonal image (0.8,1.7) missing')
log.check(all(len(h) == 8 for h in h5) and all(len(h) == 4 for h in h4), 'hole counts: 4 per P4 target, 8 per P5 target')
log.check(in_bg('Patterns 1/2 work at (1.7,0.9) and (1.8,0.7)'), 'bonus guide P5 positions match')
# clearance on a 15 cm square (2.5 cm per unit)
cm = 2.5
clear = []
for (pp, qq), diag in ((r4[0], False), (r4[1], False), (r5[0], True), (r5[1], True)):
    d = [pp * cm, qq * cm, (3 - pp) * cm, (3 - qq) * cm]
    if diag:
        d.append(abs(pp - qq) / math.sqrt(2) * cm)
    clear.append(round(min(d), 2))
log.check(all(c > 1.0 for c in clear), f'punch clearance to nearest fold/edge on a 15 cm square: {clear} cm (> 1 cm)')
seps = []
for h in (h4[0], h4[1], h5[0], h5[1]):
    seps.append(round(min(math.dist(a, b) for i, a in enumerate(h) for b in h[i + 1:]) * cm, 2))
log.check(all(s > 1.0 for s in seps), f'smallest separation between unfolded hole centres: {seps} cm')
# folded-quarter record: thick L on left and bottom edges
pg4 = pdf.pages[3]
ls = [c for c in pg4.curves if abs((c['x1'] - c['x0']) - 51.02) < 0.1 and len(c['pts']) == 3]
okL = all(abs(c['pts'][1][0] - c['x0']) < 0.1 and abs(c['pts'][1][1] - c['bottom']) < 0.1 for c in ls)
log.check(len(ls) == 3 and okL, 'P4 folded-quarter records mark the left and bottom edges (the two midline folds)')
pg5 = pdf.pages[4]
tri = [c for c in pg5.curves if abs((c['x1'] - c['x0']) - 51.02) < 0.1 and len(c['pts']) == 4]
log.check(len(tri) == 3, 'P5 has three triangle records (right angle at bottom right, hypotenuse = diagonal fold)')
diag_src = '\\draw[dashed] (0,0)--(3,3)' in src and '(6,0)--(9,0)--(9,3)--cycle' in src
log.check(diag_src, 'P5 picture folds along the diagonal through the folded corner (the original centre), giving 0<=q<=p')

log.done()
