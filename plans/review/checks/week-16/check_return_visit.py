"""Independent check of the Week 16 return-visit companion
(week-16-return-visit.pdf, 4 pp., Problems 1-4) and its adult guide
(week-16-return-visit-facilitator.pdf, 5 pp.).

Mathematics: enumerates every filling of the star, the three-step mesh with a
fourth interior label G, both diagonals of the square for every corner
labelling, and the signed (oriented) rainbow counts; tests the general
statements on random triangulations.  Diagrams: reads the student PDF's
content streams (dots, lines, squares, diagonals, sign-example arrows and
letters) and checks them against the text.  The companion's own
independent_checks.py and JSON are not used.
Run: python3 check_return_visit.py   (writes out_check_return_visit.txt)
"""
import collections
import itertools
import math
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfgeom16 as G  # noqa: E402
from sperner16 import Board, lattice, from_code, random_triangulation, random_label  # noqa: E402

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


GT = re.sub(r'\s+', ' ', G.text(G.PDF['RVguide']))


def in_guide(s):
    return re.sub(r'\s+', ' ', s) in GT


def three_diff(lab, c):
    return len({lab[v] for v in c}) == 3


def rbY(lab, c):
    return {lab[v] for v in c} == set('RBY')


# ===================================================================== P1 star
say('== Problem 1: star (one interior dot joined to the three corners)')
star = Board({'R': (0, 0), 'B': (1, 0), 'Y': (0.5, math.sqrt(3) / 2), 'c': (0.5, math.sqrt(3) / 6)},
             [('R', 'B', 'c'), ('B', 'Y', 'c'), ('Y', 'R', 'c')], {'R': 'R', 'B': 'B', 'Y': 'Y'})
good = []
for x in 'RBYG':
    lab = {'R': 'R', 'B': 'B', 'Y': 'Y', 'c': x}
    n_rby = sum(rbY(lab, c) for c in star.cells)
    n3 = sum(three_diff(lab, c) for c in star.cells)
    say('   centre %s: %d RBY cells, %d cells with three different letters' % (x, n_rby, n3))
    if n_rby == 0:
        good.append(x)
check(good == ['G'], 'only G leaves no RBY triangle (answer to "Find every choice": G alone)')

# ===================================================================== P2 mesh
say('')
say('== Problem 2: three-step mesh, G allowed only at the interior dot')
b3 = lattice(3)
allf = list(b3.labelings(inside='RBYG'))
check(len(allf) == 256, '256 legal four-label fillings (2^6 boundary x 4 interior)')
norby = [l for l in allf if not any(rbY(l, c) for c in b3.cells)]
d = collections.Counter(sum(three_diff(l, c) for c in b3.cells) for l in norby)
say('   %d fillings with no RBY; any-three counts among them: %s' % (len(norby), dict(sorted(d.items()))))
check(len(norby) == 27 and dict(d) == {3: 18, 5: 9}, 'guide: 27 with no RBY, 18 with three any-three, nine with five')
check(all(l[(1, 1)] == 'G' for l in norby), 'every no-RBY filling has G at the single interior dot')
check(in_guide('All 256 legal four-label fillings include 27 with no RBY: 18 have three any-three cells and nine have five'), 'that sentence is in the guide overview')
n, lab = from_code('RRBB/RGB/YY/Y')
types = collections.Counter(''.join(sorted({lab[v] for v in c}, key='RBYG'.index)) for c in b3.cells)
say('   witness RRBB/RGB/YY/Y cell label sets: %s' % dict(types))
mono = sum(1 for c in b3.cells if len({lab[v] for v in c}) == 1)
two = sum(1 for c in b3.cells if len({lab[v] for v in c}) == 2)
check(all(lab[v] in b3.allowed(v, inside='RBYG') for v in b3.xy) and types['RBY'] == 0 and types['RBG'] == types['RYG'] == types['BYG'] == 1
      and mono == 3 and two == 3, 'witness legal; three monochrome, three two-label, one each RBG, RYG, BYG, no RBY')
# minimum-three argument and odd-occurrence claim on random triangulations
rng = random.Random(1616)
ok_min = ok_odd = True
tested = 0
for t in range(600):
    b = random_triangulation(rng, steps=rng.randint(3, 30))
    for _ in range(60):
        l = random_label(b, rng, inside='RBYG')
        if any(rbY(l, c) for c in b.cells):
            continue
        tested += 1
        cnt = collections.Counter(frozenset(l[v] for v in c) for c in b.cells if three_diff(l, c))
        if cnt[frozenset('RBG')] % 2 != 1 or cnt[frozenset('RYG')] % 2 != 1 or cnt[frozenset('BYG')] % 2 != 1:
            ok_odd = False
        if sum(cnt.values()) < 3:
            ok_min = False
        # the recolouring step: G->R creates an RBY cell that was originally GBY, etc.
        for g, wantt in (('R', 'BYG'), ('B', 'RYG'), ('Y', 'RBG')):
            l2 = {v: (g if x == 'G' else x) for v, x in l.items()}
            hit = [c for c in b.cells if rbY(l2, c)]
            if not hit or not all({l[v] for v in c} == set(wantt) for c in hit):
                ok_min = False
check(tested > 500 and ok_min, 'recolouring argument and the bound "at least three" hold in %d random no-RBY labelings' % tested)
check(ok_odd, 'each of RBG, RYG, BYG occurs an odd number of times whenever RBY is absent')

# ===================================================================== P3 squares
say('')
say('== Problem 3: square split by a diagonal; corners 1 LL, 2 LR, 3 UR, 4 UL')


def rainbows(word, diag):
    lab = dict(zip((1, 2, 3, 4), word))
    cells = [(1, 2, 3), (1, 3, 4)] if diag == '13' else [(1, 2, 4), (2, 3, 4)]
    return sum({lab[v] for v in c} == set('RBY') for c in cells)


def bdoors(word):
    return sum({word[k], word[(k + 1) % 4]} == {'R', 'B'} for k in range(4))


changes = parity_ok = 0
parity_ok = True
for word in itertools.product('RBY', repeat=4):
    a, b_ = rainbows(word, '13'), rainbows(word, '24')
    if a != b_:
        changes += 1
    if a % 2 != bdoors(word) % 2 or b_ % 2 != bdoors(word) % 2:
        parity_ok = False
check(changes > 0, 'switching the diagonal changes the rainbow count for %d of 81 corner labellings' % changes)
check(parity_ok, 'for all 81 labellings and both diagonals, rainbow count has the parity of the number of R-B sides')
for word, d_, r13, r24 in [('RBRB', 4, 0, 0), ('RBYY', 1, 1, 1), ('RBRY', 2, 0, 2)]:
    check(bdoors(word) == d_ and rainbows(word, '13') == r13 and rainbows(word, '24') == r24,
          'guide example %s: %d doors, diagonal 1-3 gives %d, diagonal 2-4 gives %d' % (word, d_, r13, r24))

# ===================================================================== P4 signs
say('')
say('== Problem 4: signed rainbows (counterclockwise reading from R)')


def sign(b, lab, c):
    c = b.ccw(c)
    if {lab[v] for v in c} != set('RBY'):
        return 0
    k = [lab[v] for v in c].index('R')
    order = ''.join(lab[c[(k + t) % 3]] for t in range(3))
    return 1 if order == 'RBY' else -1


pairs = collections.Counter()
for lab in b3.labelings():
    s = [sign(b3, lab, c) for c in b3.cells]
    pairs[(s.count(1), s.count(-1))] += 1
say('   (positive, negative) over the 192 legal fillings: %s' % dict(sorted(pairs.items())))
check(dict(pairs) == {(1, 0): 108, (2, 1): 72, (3, 2): 12}, 'guide: (1,0), (2,1), (3,2) in 108, 72, 12 fillings')
ok_sig = ok_rev = True
for t in range(300):
    b = random_triangulation(rng, steps=rng.randint(5, 40))
    for _ in range(10):
        lab = random_label(b, rng)
        if sum(sign(b, lab, c) for c in b.cells) != 1:
            ok_sig = False
        # reverse orientation: mirror the picture (x -> -x)
        bm = Board({v: (-x, y) for v, (x, y) in b.xy.items()}, b.cells, b.corners)
        if sum(sign(bm, lab, c) for c in bm.cells) != -1:
            ok_rev = False
check(ok_sig, 'positive minus negative = 1 in 3000 random legal labelings of random triangulations')
check(ok_rev, 'mirror image (corners R, B, Y clockwise) gives -1 every time')
# missing-colour refinement creates one + and one -
tri = Board({'a': (0, 0), 'b': (1, 0), 'c': (0.5, 0.8), 'v': (0.5, 0.3)}, [('a', 'b', 'v'), ('b', 'c', 'v'), ('c', 'a', 'v')], {'R': 'a', 'B': 'b', 'Y': 'c'})
ref_ok = True
for word in itertools.product('RBY', repeat=3):
    if len(set(word)) != 2:
        continue
    miss = (set('RBY') - set(word)).pop()
    lab = dict(zip('abc', word))
    lab['v'] = miss
    s = sorted(sign(tri, lab, c) for c in tri.cells)
    if s != [-1, 0, 1]:
        ref_ok = False
check(ref_ok, 'refining any two-label triangle with the missing colour adds one + and one - rainbow')

# ===================================================================== diagrams
say('')
say('== Student PDF diagrams')
pdf = G.PDFFile(G.PDF['RV'])
check(len(pdf.pages) == 4, '4 pages')
# p.1 star
pl = G.paths(pdf, 1)
circ = G.circles(pl, rmin=5, rmax=15)
segs = [s for s in G.segments(pl) if abs(s[2].lw - 0.6) < 0.05]
words = G.words(G.PDF['RV'], 1)
dots = [(c[0], c[1]) for c in circ]
check(len(dots) == 4, 'p.1: four dots')
lab = {}
for d in dots:
    near = [w[0] for w in words if len(w[0]) == 1 and w[0] in 'RBY' and dist((w[1], w[2]), d) < 8]
    lab[d] = near[0] if near else None
corner = {v: d for d, v in lab.items() if v}
mid = [d for d, v in lab.items() if not v][0]
R, B, Y = corner['R'], corner['B'], corner['Y']
cen = ((R[0] + B[0] + Y[0]) / 3, (R[1] + B[1] + Y[1]) / 3)
check(abs(dist(R, B) - dist(B, Y)) < 0.05 and abs(dist(R, B) - dist(R, Y)) < 0.05 and dist(cen, mid) < 0.1,
      'p.1: equilateral R-B-Y (side %.2f mm), blank dot at the centroid' % (dist(R, B) / 72 * 25.4))
pairs_drawn = set()
for a, c, _ in segs:
    ea = [k for k, p in list(corner.items()) + [('c', mid)] if dist(p, a) < 0.5]
    ec = [k for k, p in list(corner.items()) + [('c', mid)] if dist(p, c) < 0.5]
    if ea and ec:
        pairs_drawn.add(frozenset((ea[0], ec[0])))
check(pairs_drawn == {frozenset(e) for e in [('R', 'B'), ('B', 'Y'), ('Y', 'R'), ('R', 'c'), ('B', 'c'), ('Y', 'c')]},
      'p.1: lines are the three sides and the three spokes')
ring = 2 * circ[0][2] / 72 * 25.4
say('     dot ring diameter %.2f mm (guide: about 7.1 mm)' % ring)
check(abs(ring - 7.1) < 0.1, 'p.1 dot rings about 7.1 mm across')
# p.2 and p.4 meshes
for pg in (2, 4):
    pl = G.paths(pdf, pg)
    circ = G.circles(pl, rmin=5, rmax=15)
    segs = [s for s in G.segments(pl) if abs(s[2].lw - 0.6) < 0.05]
    words = G.words(G.PDF['RV'], pg)
    dots = [(c[0], c[1]) for c in circ]
    ys = sorted(d[1] for d in dots)
    bottom = sorted(d for d in dots if abs(d[1] - ys[0]) < 0.5)
    Rp, Bp = bottom[0], bottom[-1]
    side = Bp[0] - Rp[0]
    match = {}
    for v, (x, y) in b3.xy.items():
        near = [d for d in dots if dist(d, (Rp[0] + x * side, Rp[1] + y * side)) < 0.5]
        if len(near) == 1:
            match[v] = near[0]
    check(len(match) == 10 == len(dots), 'p.%d: ten dots exactly on a side-3 lattice, spacing %.1f mm' % (pg, side / 3 / 72 * 25.4))
    drawn = set()
    for a, c, _ in segs:
        ea = [v for v, p in match.items() if dist(p, a) < 0.5]
        ec = [v for v, p in match.items() if dist(p, c) < 0.5]
        if ea and ec and ea != ec:
            drawn.add(frozenset((ea[0], ec[0])))
    check(drawn == set(b3.edge_cells), 'p.%d: the 18 mesh edges are drawn' % pg)
    lab = {}
    for v, p in match.items():
        near = [w[0] for w in words if len(w[0]) == 1 and w[0] in 'RBY' and dist((w[1], w[2]), p) < 8]
        if near:
            lab[v] = near[0]
    check(lab == {(0, 0): 'R', (3, 0): 'B', (0, 3): 'Y'}, 'p.%d: only the corners are lettered, R bottom left, B bottom right, Y top' % pg)
    fr = [w for w in words if w[0] in ('Ro', 'rY', 'Bo', 'or', 'Y', 'R', 'B') and not any(dist((w[1], w[2]), p) < 12 for p in match.values())]
    Yp = match[(0, 3)]
    midL = ((Rp[0] + Yp[0]) / 2, (Rp[1] + Yp[1]) / 2)
    midR = ((Bp[0] + Yp[0]) / 2, (Bp[1] + Yp[1]) / 2)
    lt = ''.join(sorted(''.join(w[0] for w in fr if dist((w[1], w[2]), midL) < 50 and w[1] < midL[0])))
    rt = ''.join(sorted(''.join(w[0] for w in fr if dist((w[1], w[2]), midR) < 50 and w[1] > midR[0])))
    bt = ' '.join(w[0] for w in sorted(words, key=lambda w: w[1]) if Rp[1] - 40 < w[2] < Rp[1] - 5 and Rp[0] < w[1] < Bp[0])
    check(lt == ''.join(sorted('RorY')) and rt == ''.join(sorted('BorY')) and bt == 'R or B',
          'p.%d: side rules "R or Y" left, "B or Y" right, "R or B" below (%r %r %r)' % (pg, lt, rt, bt))
# p.3 squares
pl = G.paths(pdf, 3)
circ = G.circles(pl, rmin=5, rmax=15)
segs = [s for s in G.segments(pl) if abs(s[2].lw - 0.65) < 0.05]
dots = [(c[0], c[1]) for c in circ]
rects = [s for p in pl for s in p.subpaths if s[2] and len(s[0]) == 4 and not s[1]]
check(len(dots) == 16 and len(rects) == 4, 'p.3: four squares with sixteen corner dots')
diag_ok = True
desc = []
for pts, _, _ in sorted(rects, key=lambda s: (-s[0][0][1], s[0][0][0])):
    xs = sorted({round(p[0], 2) for p in pts})
    ys = sorted({round(p[1], 2) for p in pts})
    if abs((xs[-1] - xs[0]) - (ys[-1] - ys[0])) > 0.05:
        diag_ok = False
    LL, LR, UR, UL = (xs[0], ys[0]), (xs[-1], ys[0]), (xs[-1], ys[-1]), (xs[0], ys[-1])
    ds = [s for s in segs if all(xs[0] - 0.5 <= q[0] <= xs[-1] + 0.5 and ys[0] - 0.5 <= q[1] <= ys[-1] + 0.5 for q in s[:2])
          and abs(s[0][0] - s[1][0]) > 1 and abs(s[0][1] - s[1][1]) > 1]
    kinds = []
    for a, c, _ in ds:
        if {tuple(round(v, 1) for v in a), tuple(round(v, 1) for v in c)} == {tuple(round(v, 1) for v in LL), tuple(round(v, 1) for v in UR)}:
            kinds.append('13')
        elif {tuple(round(v, 1) for v in a), tuple(round(v, 1) for v in c)} == {tuple(round(v, 1) for v in LR), tuple(round(v, 1) for v in UL)}:
            kinds.append('24')
    desc.append(''.join(kinds))
    corners_have_dots = all(any(dist(q, d) < 0.3 for d in dots) for q in (LL, LR, UR, UL))
    diag_ok = diag_ok and corners_have_dots and len(kinds) == 1
check(diag_ok and desc == ['13', '24', '13', '24'], 'p.3: squares are square; diagonals by row are left 1-3, right 2-4 (%s), as the guide says' % desc)
# p.4 sign examples
pl = G.paths(pdf, 4)
words = G.words(G.PDF['RV'], 4)
heads = []
for p in pl:
    if p.filled:
        for pts, cu, cl in p.subpaths:
            if cl and not cu and len(pts) == 4 and max(dist(pts[0], q) for q in pts) < 8:
                heads.append(pts)   # TikZ Stealth head: first point is the tip
shafts = [s for s in G.segments(pl) if abs(s[2].lw - 0.7) < 0.05 and s[2].op == 'S' and dist(s[0], s[1]) > 15]
tris = []
for p in pl:
    for pts, cu, cl in p.subpaths:
        if cl and not cu and len(pts) == 3 and abs(p.lw - 0.4) < 0.05:
            tris.append(pts)
check(len(tris) == 2, 'p.4: two small example triangles')
for t in sorted(tris, key=lambda t: t[0][0]):
    labs = {}
    for v in t:
        near = sorted([w for w in words if w[0] in ('R', 'B', 'Y')], key=lambda w: dist((w[1], w[2]), v))
        labs[v] = near[0][0]
    cx = sum(v[0] for v in t) / 3
    cy = sum(v[1] for v in t) / 3
    # arrows inside this triangle: shaft start -> end
    turn = 0
    arrows = []
    for a, c, _ in shafts:
        if min(v[0] for v in t) - 2 < (a[0] + c[0]) / 2 < max(v[0] for v in t) + 2 and min(v[1] for v in t) - 2 < (a[1] + c[1]) / 2 < max(v[1] for v in t) + 2:
            # which end carries the arrowhead?
            hd = min(heads, key=lambda h: min(dist(h[0], a), dist(h[0], c)))
            tip = c if dist(hd[0], c) < dist(hd[0], a) else a
            tail = a if tip is c else c
            arrows.append((tail, tip))
            turn += (tail[0] - cx) * (tip[1] - cy) - (tail[1] - cy) * (tip[0] - cx)
    order = sorted(t, key=lambda v: math.atan2(v[1] - cy, v[0] - cx))     # counterclockwise
    k = [labs[v] for v in order].index('R')
    read = ''.join(labs[order[(k + s) % 3]] for s in range(3))
    sgn = '+' if read == 'RBY' else '-'
    caption = [w for w in words if abs(w[1] - cx) < 60 and cy - 70 < w[2] < cy - 45]
    captxt = ' '.join(w[0] for w in sorted(caption, key=lambda w: w[1]))
    check(len(arrows) == 3 and turn > 0, 'p.4 example %s: three arrows, all counterclockwise' % read)
    check(captxt.replace('→', '>').replace(' ', '').startswith(read[0] + '>' + read[1] + '>' + read[2]) and captxt.strip().endswith(sgn) or
          captxt.strip().endswith({'+': '+', '-': '−'}[sgn]),
          'p.4 example: counterclockwise reading from R is %s, caption "%s" gives %s' % (read, captxt, sgn))

say('')
say('%d failures' % len(FAIL))
for f in FAIL:
    say('FAILED: ' + f)
open(os.path.join(HERE, 'out_check_return_visit.txt'), 'w').write('\n'.join(OUT) + '\n')
print('\n'.join(OUT))
