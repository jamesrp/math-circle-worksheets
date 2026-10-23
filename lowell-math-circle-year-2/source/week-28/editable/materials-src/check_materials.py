#!/usr/bin/env python3
"""Independent check of build/materials.pdf (the Week 28 print-and-cut kit).

Reads only the finished PDF. Every dimension, angle, label and count is measured
from the vector drawing and compared with what the student problems need. The
crease patterns are then tested against the flat-folding conditions:

* Kawasaki: an even number of rays, and alternating sector sums of 180 degrees;
* Maekawa: |M - V| = 2 in every flat labelling;
* the crimp reduction (Bern-Hayes, Hull), which decides whether a given
  mountain/valley labelling of one vertex folds flat;
* a brute force over bottom-to-top layer orders with the noncrossing rules,
  as a second, separate decision of the same question.

Usage: python3 materials-src/check_materials.py [path/to/materials.pdf]
Writes build/materials-checks.json and exits non-zero on any failure.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
import json
import math
import sys

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
PDF = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'build' / 'materials.pdf'
MM = 72 / 25.4
H = 792
results = []


def check(ok, what):
    results.append({'check': what, 'pass': bool(ok)})
    if not ok:
        print('FAIL:', what)


# ---------------------------------------------------------------- folding theory
def kawasaki(sectors):
    return len(sectors) % 2 == 0 and sum(sectors[0::2]) == sum(sectors[1::2]) == 180


def crimp_flat(sectors, word):
    """Hull's crimp reduction: a labelled single vertex folds flat iff repeated
    crimps of a locally smallest sector between unequal labels end at two equal labels."""
    a, w = list(sectors), list(word)
    if len(a) % 2 or not kawasaki(a):
        return False
    while len(a) > 2:
        n = len(a)
        for i in range(n):
            # sector i lies between ray i and ray i+1
            if a[i] <= a[i - 1] and a[i] <= a[(i + 1) % n] and w[i] != w[(i + 1) % n]:
                # Rotate so ray i-1 comes first: a2 = [sector i-1, sector i, sector i+1, ...],
                # w2 = [ray i-1, ray i, ray i+1, ...]. Crimping drops rays i and i+1 and
                # merges the three sectors into one between rays i-1 and i+2.
                r = (i - 1) % n
                a2, w2 = a[r:] + a[:r], w[r:] + w[:r]
                a = [a2[0] - a2[1] + a2[2]] + a2[3:]
                w = [w2[0]] + w2[3:]
                break
        else:
            return False
    return w[0] == w[1]


def layer_flat_words(sectors):
    """Brute force: labellings realised by a noncrossing bottom-to-top layer order."""
    n = len(sectors)
    if n % 2:
        return set()
    theta = [0]
    face = [1 if k % 2 == 0 else -1 for k in range(n)]
    for k in range(n):
        theta.append(theta[-1] + face[k] * sectors[k])
    if theta[-1] != 0:
        return set()
    theta = theta[:n]
    iv = [tuple(sorted((theta[k], theta[(k + 1) % n]))) for k in range(n)]
    words = set()
    for perm in permutations(range(n)):
        h = [0] * n
        for pos, sec in enumerate(perm):
            h[sec] = pos
        creases, ok = [], True
        for k in range(n):                      # ray k joins sectors k-1 and k
            i, j, x = (k - 1) % n, k, theta[k]
            lo, hi = sorted((h[i], h[j]))
            for m in range(n):
                if m not in (i, j) and iv[m][0] < x < iv[m][1] and lo < h[m] < hi:
                    ok = False
            creases.append((x, face[k], lo, hi))
        for p, q in combinations(creases, 2):
            if p[0] != q[0]:
                continue
            if p[1] == q[1]:
                if ((p[2] < q[2] < p[3]) + (p[2] < q[3] < p[3])) == 1:
                    ok = False
            elif not (p[3] < q[2] or q[3] < p[2]):
                ok = False
        if ok:
            w = ''
            for k in range(n):
                i, j = (k - 1) % n, k
                up, down = (i, j) if face[i] == 1 else (j, i)
                w += 'V' if h[down] > h[up] else 'M'
            words.add(w)
    return words


def flat_words(sectors):
    a = sorted(''.join(t) for t in product('MV', repeat=len(sectors)) if crimp_flat(sectors, ''.join(t)))
    b = sorted(layer_flat_words(sectors))
    check(a == b, f'crimp reduction and layer-order brute force agree on sectors {sectors}')
    return a


def sectors_of(rays):
    r = sorted(rays)
    return [Fraction(round(((r[(i + 1) % len(r)] - r[i]) % 360) * 2), 2) for i in range(len(r))]


# ---------------------------------------------------------------- PDF reading
def up(p):
    return (p.x, H - p.y)


def angle_cw(cx, cy, x, y):
    return round(math.degrees(math.atan2(x - cx, y - cy)) % 360, 3)


def words_up(page):
    return [(w[4], (w[0] + w[2]) / 2, H - (w[1] + w[3]) / 2) for w in page.get_text('words')]


def circles(page, min_r=0.0):
    """Closed four-curve paths, as (cx, cy, r, drawing)."""
    out = []
    for d in page.get_drawings():
        it = d['items']
        if len(it) == 4 and all(x[0] == 'c' for x in it):
            r = d['rect']
            if abs(r.width - r.height) < .01 and r.width / 2 >= min_r:
                out.append(((r.x0 + r.x1) / 2, H - (r.y0 + r.y1) / 2, r.width / 2, d))
    return out


def lines(page):
    out = []
    for d in page.get_drawings():
        for it in d['items']:
            if it[0] == 'l':
                out.append((up(it[1]), up(it[2]), d))
    return out


def scale_line(page):
    found = [l for l in lines(page) if abs(l[0][1] - l[1][1]) < .01 and abs(abs(l[0][0] - l[1][0]) - 100 * MM) < .05]
    return found


def wedges(page):
    """Filled-and-stroked sectors: apex, radius, clockwise start and span, gray, label."""
    out = []
    for d in page.get_drawings():
        it = d['items']
        if d.get('fill') is None or d.get('color') is None:
            continue
        ls = [x for x in it if x[0] == 'l']
        cs = [x for x in it if x[0] == 'c']
        if not cs:
            continue
        if not ls:                                     # a full disk drawn as a circle
            continue
        ends = [up(p) for x in ls for p in (x[1], x[2])]
        apex = max(set((round(x, 3), round(y, 3)) for x, y in ends), key=lambda q: sum(
            1 for e in ends if abs(e[0] - q[0]) < .01 and abs(e[1] - q[1]) < .01))
        arc = [up(p) for x in cs for p in (x[1], x[4])]
        radii = [math.dist(apex, q) for q in arc]
        a = [angle_cw(*apex, *q) for q in arc]
        first, last = up(cs[0][1]), up(cs[-1][4])
        a_first, a_last = angle_cw(*apex, *first), angle_cw(*apex, *last)
        # ReportLab draws the arc counterclockwise, so it runs from the clockwise end to the start.
        start, end = a_last, a_first
        span = round((end - start) % 360, 2) or 360.0
        out.append({'apex': apex, 'r_mm': round(sum(radii) / len(radii) / MM, 3),
                    'r_spread_mm': round((max(radii) - min(radii)) / MM, 4),
                    'start': round(start, 2), 'span': span, 'gray': round(d['fill'][0], 2)})
    return out


def label_in(w, texts):
    cx, cy = w['apex']
    best = []
    for t, x, y in texts:
        dist = math.hypot(x - cx, y - cy)
        if dist < w['r_mm'] * MM * .95 and dist > 2:
            ang = angle_cw(cx, cy, x, y)
            if (ang - w['start']) % 360 < w['span']:
                best.append(t)
    return best


# ---------------------------------------------------------------- the checks
doc = pymupdf.open(PDF)
check(len(doc) == 15, f'15 pages (found {len(doc)})')
for i, page in enumerate(doc, 1):
    check(page.rect == pymupdf.Rect(0, 0, 612, 792), f'p{i}: US Letter')
    t = page.get_text()
    check('Week 28 / Flat folds / Materials' in t, f'p{i}: header')
    check(f'Bellingham Math Circle / Week 28 / W28-M-v1 / physically unrehearsed' in t, f'p{i}: footer with id and status')
    check(len(scale_line(page)) == 1 and '10 cm check' in t, f'p{i}: one 10 cm scale line (100.00 mm)')
    if i > 1:
        check('at 100%:' in t and ('copy paper' in t or 'card stock' in t), f'p{i}: heading states paper and print counts')
    for b in page.get_text('dict')['blocks']:
        for line in b.get('lines', []):
            for s in line['spans']:
                x0, y0, x1, y1 = s['bbox']
                check(x0 >= 28 and x1 <= 584 and y0 >= 20 and y1 <= 772, f'p{i}: text inside printable margins')
        break

summary = {}

# Disks: pages 2-10.
EXPECT = {  # page: (rays the problem needs, letter, numbered, tick spacing)
    2: ([0, 90, 180, 270], None, True, None),
    3: ([0, 45, 135, 225], 'B', True, None),       # 2-3 P3 B / 4-5 P1 B: 45, 90, 90, 135
    4: ([0, 60, 180, 300], 'C', True, None),       # 60, 120, 120, 60
    5: ([0, 30, 90, 240], 'D', True, None),        # 30, 60, 150, 120
    6: ([0, 90, 180], 'A', False, 30),             # 2-3 P4 starts
    7: ([0, 60, 180], 'B', False, 30),
    8: ([0, 30, 180], 'C', False, 30),
    9: ([0, 120, 180], 'D', False, 30),
    10: ([], None, False, 15),
}
for pno, (rays_needed, letter, numbered, tick) in EXPECT.items():
    page = doc[pno - 1]
    big = [c for c in circles(page, 50 * MM) if c[3].get('color') is not None]
    check(len(big) == 1, f'p{pno}: one disk outline')
    cx, cy, R, _ = big[0]
    check(abs(2 * R / MM - 180) < .05, f'p{pno}: disk diameter {2 * R / MM:.3f} mm = 180 mm')
    tint = [c for c in circles(page, 50 * MM) if c[3].get('color') is None and c[3].get('fill')]
    check(len(tint) == 1 and tint[0][3]['fill'][0] < .95, f'p{pno}: tinted front')
    check(cx - R > 12 * MM and 612 - (cx + R) > 12 * MM and cy - R > 40 * MM and H - (cy + R) > 45 * MM,
          f'p{pno}: disk clear of page edges, header and scale line')
    rays, ticks = [], []
    for a, b, d in lines(page):
        if math.dist(a, (cx, cy)) < .01 and abs(math.dist(b, (cx, cy)) - R) < .01:
            rays.append(angle_cw(cx, cy, *b))
        elif abs(math.dist(b, (cx, cy)) - R) < .01 and math.dist(a, (cx, cy)) > R - 7 * MM:
            ticks.append((angle_cw(cx, cy, *b), round((R - math.dist(a, (cx, cy))) / MM, 2)))
    rays.sort()
    check(rays == sorted(float(x) for x in rays_needed), f'p{pno}: rays {rays} match the problem {rays_needed}')
    texts = words_up(page)
    inside = [(t, x, y) for t, x, y in texts if math.hypot(x - cx, y - cy) < R]
    check(any(t == 'front' for t, _, _ in inside), f'p{pno}: front mark inside the disk')
    if letter:
        check(any(t == letter for t, _, _ in inside), f'p{pno}: letter {letter} inside the disk')
    if numbered:
        for k, a in enumerate(rays_needed, 1):
            near = [t for t, x, y in inside if t == str(k) and abs(((angle_cw(cx, cy, x, y) - a + 180) % 360) - 180) < 3
                    and math.hypot(x - cx, y - cy) > R - 12 * MM]
            check(near, f'p{pno}: number {k} at the rim end of the ray at {a} degrees')
    if tick:
        check(sorted(t[0] for t in ticks) == [float(k * tick) for k in range(360 // tick)],
              f'p{pno}: rim ticks every {tick} degrees')
    # corner marks for the optional 18 cm square lie outside the square
    marks = [l for l in lines(page) if l[2]['width'] and abs(l[2]['width'] - .5) < .01]
    check(len(marks) == 8 and all(max(abs(p[0] - cx), abs(p[1] - cy)) >= R + 2.9 for l in marks for p in l[:2]),
          f'p{pno}: eight square-trim marks, all outside the 18 cm square')
    if rays_needed:
        sec = sectors_of(rays)
        summary[f'page {pno}'] = {'rays': rays, 'sectors': [float(s) for s in sec]}

# Folding conditions where the problems need them.
right = sectors_of(EXPECT[2][0])
fw = flat_words(right)
eight = ['MMMV', 'MMVM', 'MVMM', 'MVVV', 'VMMM', 'VMVV', 'VVMV', 'VVVM']
check(kawasaki(right) and fw == eight, 'right-angle disk: Kawasaki holds; exactly the eight 3:1 labellings fold (K-1 P1-P5, 2-3 P5, 4-5 P4)')
check(all(abs(w.count('M') - w.count('V')) == 2 for w in fw), 'right-angle disk: every flat labelling obeys Maekawa')
check(set(fw) >= {'MMMV', 'MVVV', 'MMVM'} and not set(fw) & {'MMMM', 'MMVV', 'MVMV', 'VVVV'},
      'K-1 P2 A, C, E fold and B, D, F do not; 4-5 P5 A-D do not')
check(sorted(w for w in fw if w[0] == 'M') == ['MMMV', 'MMVM', 'MVMM', 'MVVV'], 'K-1 P3: four flat folds with ray 1 = M')
b = sectors_of(EXPECT[3][0])
check(b == [45, 90, 90, 135] and not kawasaki(b) and flat_words(b) == [],
      'disk B (45, 90, 90, 135): alternating sums 135 and 225, so no labelling folds')
cc = sectors_of(EXPECT[4][0])
wc = flat_words(cc)
check(cc == [60, 120, 120, 60] and kawasaki(cc) and wc == ['MMMV', 'MVMM', 'MVVV', 'VMMM', 'VMVV', 'VVVM'],
      'disk C (60, 120, 120, 60): Kawasaki holds; six labellings fold, including the guide witness VVVM')
dd = sectors_of(EXPECT[5][0])
wd = flat_words(dd)
check(dd == [30, 60, 150, 120] and kawasaki(dd) and wd == ['MVMM', 'MVVV', 'VMMM', 'VMVV'] and 'VVVM' not in wd,
      'disk D (30, 60, 150, 120): Kawasaki holds; four labellings fold, MVVV among them, VVVM not')
check(all(abs(w.count('M') - w.count('V')) == 2 for w in wc + wd), 'disks C and D: every flat labelling obeys Maekawa')
summary['flat labellings'] = {'right angles': fw, 'B': [], 'C': wc, 'D': wd}
added = {}
for pno in (6, 7, 8, 9):
    given = EXPECT[pno][0]
    check(len(given) == 3 and not kawasaki(sectors_of(given)), f'p{pno}: three printed rays cannot fold (odd number)')
    a = given[1]
    good_ticks = [t for t in range(0, 360, 30) if t not in given and kawasaki(sectors_of(given + [t]))]
    good_half = [x / 2 for x in range(720) if x / 2 not in given and kawasaki(sectors_of(given + [x / 2]))]
    check(good_ticks == [360 - a] and good_half == [360 - a],
          f'p{pno}: the only added ray that balances is {360 - a} degrees, on a tick (scanned every 0.5 degree)')
    words = flat_words(sectors_of(given + [360 - a]))
    check('VVVM' in words, f'p{pno}: completed pattern folds, for example as VVVM')
    added[f'page {pno}'] = {'given': given, 'added': 360 - a, 'flat labellings': words}
summary['add-a-ray'] = added
p10 = doc[9]
cx, cy, R, _ = [c for c in circles(p10, 50 * MM) if c[3].get('color') is not None][0]
lt = []
for a_, b_, d in lines(p10):
    if abs(math.dist(b_, (cx, cy)) - R) < .01 and math.dist(a_, (cx, cy)) > R - 7 * MM:
        lt.append((angle_cw(cx, cy, *b_), round((R - math.dist(a_, (cx, cy))) / MM, 1)))
check(sorted(t for t, l in lt if l == 6.5) == [float(x) for x in range(0, 360, 45)] and
      all(l == 4 for t, l in lt if t % 45), 'p10: blank disk has long ticks every 45 and short every 15 degrees')

# Seven lettered wedges, page 11: three sets of A-G at radius 2.25 cm.
ws = wedges(doc[10])
texts = words_up(doc[10])
for w in ws:
    w['label'] = label_in(w, texts)
check(all(len(w['label']) == 1 for w in ws), 'p11: one letter inside every wedge')
check(all(abs(w['r_mm'] - 22.5) < .05 and w['r_spread_mm'] < .05 for w in ws), 'p11: every wedge has radius 22.5 mm')
spans = sorted((w['label'][0], w['span']) for w in ws)
want7 = {'A': 30, 'B': 30, 'C': 60, 'D': 60, 'E': 90, 'F': 120, 'G': 150}
check(spans == sorted((k, float(v)) for k, v in want7.items() for _ in range(3)), 'p11: three sets of A30 B30 C60 D60 E90 F120 G150')
groups = [''.join(g) for n in range(1, 8) for g in combinations('ABCDEFG', n) if sum(want7[x] for x in g) == 180]
check(sorted(groups) == sorted(['AG', 'BG', 'CF', 'DF', 'ABF', 'ACE', 'ADE', 'BCE', 'BDE', 'ABCD']),
      'p11: exactly the ten half-turn groups of the guide (2-3 P1)')
summary['seven wedges'] = {'radius_mm': 22.5, 'half-turn groups': groups}

# Sixteen matching wedges, page 12: one set at 2.5 cm, sectors 1 and 3 shaded; two boards.
ws = wedges(doc[11])
texts = words_up(doc[11])
want16 = {'A': [90, 90, 90, 90], 'B': [45, 90, 90, 135], 'C': [60, 120, 120, 60], 'D': [30, 60, 150, 120]}
found = {}
for w in ws:
    lab = label_in(w, texts)
    check(len(lab) == 1, f'p12: one label in wedge at {w["start"]}')
    found[lab[0]] = w
check(sorted(found) == sorted(f'{k}{i}' for k in want16 for i in range(1, 5)), 'p12: pieces A1-A4, B1-B4, C1-C4, D1-D4')
for k, secs in want16.items():
    a = 0
    for i, s in enumerate(secs, 1):
        w = found[f'{k}{i}']
        check(abs(w['span'] - s) < .01 and abs((w['start'] - a + 180) % 360 - 180) < .01 and abs(w['r_mm'] - 25) < .05,
              f'p12: {k}{i} spans {s} degrees from {a}, radius 25 mm, as on the Problem 2 page')
        check((w['gray'] < .9) == (i % 2 == 1), f'p12: {k}{i} shading matches the page (sectors 1 and 3 shaded)')
        a += s
    odd, even = secs[0] + secs[2], secs[1] + secs[3]
    check((odd == even == 180) == (k != 'B'), f'p12: disk {k} shaded pair {odd}, white pair {even}')
semis = [d for d in doc[11].get_drawings() if d.get('fill') is None and len([x for x in d['items'] if x[0] == 'c']) == 2]
check(len(semis) == 2 and all(abs(d['rect'].width / 2 / MM - 25) < .05 and abs(d['rect'].height / MM - 25) < .05 for d in semis),
      'p12: two half-turn boards, semicircles of radius 25 mm')

# Six wedges, page 13: three sets of A30 A30 B60 B60 C90 C90 at 2.4 cm.
ws = wedges(doc[12])
texts = words_up(doc[12])
by_disk = {}
for w in ws:
    lab = label_in(w, texts)
    check(len(lab) == 1 and abs(w['r_mm'] - 24) < .05, 'p13: labelled wedge of radius 24 mm')
    by_disk.setdefault(round(w['apex'][0]), []).append((w['start'], lab[0], w['span']))
check(len(by_disk) == 3, 'p13: three sets')
val = {'A': 30, 'B': 60, 'C': 90}
orders = set(permutations('AABBCC'))
good = sorted(''.join(o) for o in orders if sum(val[x] for x in o[0::2]) == 180)
check(len(good) == 36 and sum(o[0] == 'A' for o in good) == 12, 'p13: 36 rooted orders, 12 starting with 30 degrees (2-3 P6, 4-5 P6)')
for x, ps in by_disk.items():
    ps.sort()
    word = ''.join(l for _, l, _ in ps)
    check(sorted(word) == list('AABBCC') and all(abs(s - val[l]) < .01 for _, l, s in ps),
          f'p13: set at x={x} is A, A, B, B, C, C with spans 30, 30, 60, 60, 90, 90')
    check(word not in good, f'p13: printed order {word} is not an answer')
starts = [c for c in circles(doc[12], 20 * MM) if c[3].get('fill') is None]
check(len(starts) == 3 and all(abs(c[2] / MM - 24) < .05 for c in starts), 'p13: three start disks of radius 24 mm')

# K-1 tabs, page 14: 54 squares of 10 mm, 27 M and 27 V.
page = doc[13]
sq = [d for d in page.get_drawings() if any(x[0] == 're' for x in d['items'])]
rects = [x[1] for d in sq for x in d['items'] if x[0] == 're']
check(len(rects) == 54 and all(abs(r.width / MM - 10) < .02 and abs(r.height / MM - 10) < .02 for r in rects),
      'p14: 54 tabs of 10 mm')
gx0, gx1 = min(r.x0 for r in rects), max(r.x1 for r in rects)
gy0, gy1 = H - max(r.y1 for r in rects), H - min(r.y0 for r in rects)
letters = [t for t, x, y in words_up(page) if t in ('M', 'V') and gx0 < x < gx1 and gy0 < y < gy1]
check(letters.count('M') == 27 and letters.count('V') == 27, 'p14: 27 M and 27 V')
stock = {'A': (2, 4), 'B': (3, 3), 'C': (4, 2)}       # K-1 P4 row stocks (M, V)
need = (sum(m for m, v in stock.values()), sum(v for m, v in stock.values()))
check(need == (9, 9) and 3 * need[0] <= 27 and 3 * need[1] <= 27, 'p14: three full K-1 P4 stocks (9 M and 9 V each)')

# K-1 route cards, page 15: 16 cards of 46 mm, words as on the Problem 6 page.
page = doc[14]
rects = [x[1] for d in page.get_drawings() for x in d['items'] if x[0] == 're' and x[1].width > 100]
check(len(rects) == 16 and all(abs(r.width / MM - 46) < .02 and abs(r.height / MM - 46) < .02 for r in rects),
      'p15: 16 cards of 46 mm')
page6 = {'A': 'MMMV', 'B': 'MMVM', 'C': 'MVMM', 'D': 'VMMM', 'E': 'MVVV', 'F': 'VMVV', 'G': 'VVMV', 'H': 'VVVM'}
texts = words_up(page)
cards = []
for r in rects:
    x0, y0, x1, y1 = r.x0, H - r.y1, r.x1, H - r.y0
    inside = [(t, x, y) for t, x, y in texts if x0 < x < x1 and y0 < y < y1]
    letter = [t for t, x, y in inside if t in page6 and y > y1 - 10 * MM and x < x0 + 10 * MM]
    disk = [c for c in circles(page, 10 * MM) if x0 < c[0] < x1 and y0 < c[1] < y1]
    check(len(letter) == 1 and len(disk) == 1, 'p15: each card has one letter and one disk')
    cx, cy, rr, _ = disk[0]
    labs = sorted((round(angle_cw(cx, cy, x, y) / 90) % 4, t) for t, x, y in inside
                  if t in ('M', 'V') and math.hypot(x - cx, y - cy) < rr)
    word = ''.join(t for _, t in labs)
    check([k for k, _ in labs] == [0, 1, 2, 3], 'p15: one label on each of rays 1-4')
    cards.append((letter[0], word))
check(sorted(cards) == sorted(list(page6.items()) * 2), 'p15: two sets of A-H with the Problem 6 words')
check(sorted(page6.values()) == eight, 'p15: the eight cards are exactly the eight flat folds')

failed = [r for r in results if not r['pass']]
out = {'pdf': PDF.name, 'pages': len(doc), 'checks': len(results), 'failures': len(failed),
       'physically_rehearsed': False, 'summary': summary}
(ROOT / 'build').mkdir(exist_ok=True)
(ROOT / 'build' / 'materials-checks.json').write_text(json.dumps(out, indent=2, default=str) + '\n')
print(f'{len(results)} checks, {len(failed)} failures')
sys.exit(1 if failed else 0)
