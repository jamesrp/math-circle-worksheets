"""Week 22 bonus (encore) companion: read the dots back out of the delivered
week-22-bonus.pdf and recompute every answer and every guide claim.

Board unit = 16.25 mm (the tikz x/y unit in the source). Positions are read
relative to the first labelled dot and compared with the source coordinates.

Output: out_check_bonus.txt
"""
import math
import os
import sys
from fractions import Fraction as Fr
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from geom import (find_root, P, hull, contains, on_segment, orient, set_partitions, meet,  # noqa: E402
                  shared_set, dist_to_segment, fmt)
from pdfminer.high_level import extract_pages  # noqa: E402
from pdfminer.layout import LTCurve, LTTextContainer, LTTextLine, LTFigure  # noqa: E402

ROOT = find_root()
PDF = os.path.join(ROOT, 'lowell-math-circle-year-2', 'week-22', 'week-22-bonus.pdf')
UNIT = 16.25 / 25.4 * 72          # pt per board unit
LINES = []


def say(s=''):
    LINES.append(s)
    print(s)


def items(layout):
    for x in layout:
        if isinstance(x, LTFigure):
            yield from items(x)
        else:
            yield x


def page_dots(page):
    dots, rings, texts = [], [], []
    for x in items(page):
        if isinstance(x, LTTextContainer):
            for line in x:
                if isinstance(line, LTTextLine):
                    t = line.get_text().strip()
                    b = line.bbox
                    if len(t) == 1 and t.isupper():
                        texts.append((t, b[0], b[1]))
        elif isinstance(x, LTCurve):
            w = x.bbox[2] - x.bbox[0]
            c = ((x.bbox[0] + x.bbox[2]) / 2, (x.bbox[1] + x.bbox[3]) / 2)
            if x.fill and 3.5 < w < 4.5:
                dots.append(c)
            elif not x.fill and 5.5 < w < 6.5:
                rings.append(c)
    # each label sits above-right (or above) its dot: take the nearest dot to the label's lower-left
    lab = {}
    for t, x0, y0 in texts:
        d = min(dots + rings, key=lambda p: (p[0] - x0) ** 2 + (p[1] - y0) ** 2)
        if math.hypot(d[0] - x0, d[1] - y0) < 25:
            lab[t] = d
    return lab


SRC = {
    1: {'A': (1, 0), 'B': (5, 0), 'C': (8, 2), 'D': (7, 6), 'E': (3, 7), 'F': (0, 3), 'T': (4, 3.2)},
    2: {'A': (1, 1), 'B': (7, 1), 'C': (7, 7), 'D': (1, 7)},
    3: {'A': (1, 6), 'B': (2, 6), 'C': (4, 6), 'D': (5, 6), 'E': (7, 6), 'P': (1, 2), 'Q': (3, 2), 'R': (5, 2), 'S': (7, 2)},
    5: {'A': (1, 0), 'B': (5, 0), 'C': (8, 2), 'D': (7, 6), 'E': (3, 7), 'F': (0, 3)},
}
pages = list(extract_pages(PDF))
say('Extraction (board units relative to the first label; max deviation from source):')
for pn, src in SRC.items():
    lab = page_dots(pages[pn - 1])
    ref = sorted(src)[0]
    dev = 0.0
    for k, (sx, sy) in src.items():
        px = src[ref][0] + (lab[k][0] - lab[ref][0]) / UNIT
        py = src[ref][1] + (lab[k][1] - lab[ref][1]) / UNIT
        dev = max(dev, abs(px - sx), abs(py - sy))
    say(f'  p{pn}: labels {"".join(sorted(lab))}; max deviation {dev:.4f} units')
lab = page_dots(pages[3])
c = [sum(v[0] for v in lab.values()) / 6, sum(v[1] for v in lab.values()) / 6]
radii = [math.hypot(v[0] - c[0], v[1] - c[1]) / UNIT for v in lab.values()]
sides = [math.hypot(lab[a][0] - lab[b][0], lab[a][1] - lab[b][1]) / UNIT for a, b in zip('ABCDEF', 'BCDEFA')]
say(f'  p4 hexagon: radii {min(radii):.4f}-{max(radii):.4f}, sides {min(sides):.4f}-{max(sides):.4f} units (regular, equal scaling)')

# ---------------------------------------------------------------- P1, P2
say()
say('P1/P2 (p1): six dots and target T')
pts = {k: P(*v) for k, v in SRC[1].items()}
T = pts.pop('T')
H = hull(list(pts.values()))
names = {v: k for k, v in pts.items()}
say(f"  hull order: {''.join(names[p] for p in H)} (all six are corners: {len(H) == 6}); T inside: {contains(H, T)}")
on = [a + b for a, b in combinations(sorted(pts), 2) if on_segment(T, pts[a], pts[b])]
say(f'  T on a joining segment: {on or "none"}; T equals a dot: {T in pts.values()}')
onl = [a + b for a, b in combinations(sorted(pts), 2) if orient(pts[a], pts[b], T) == 0]
say(f'  T on an infinite joining line: {onl or "none"}')
tri = [''.join(t) for t in combinations(sorted(pts), 3) if contains(hull([pts[x] for x in t]), T)]
say(f'  containing triples ({len(tri)}): {",".join(tri)}')
w = (Fr(11, 25), Fr(4, 25), Fr(2, 5))
comb = tuple(w[0] * pts['C'][i] + w[1] * pts['E'][i] + w[2] * pts['F'][i] for i in (0, 1))
say(f'  guide: T = 11/25 C + 4/25 E + 2/5 F -> {fmt(comb[0])},{fmt(comb[1])}; weights sum {fmt(sum(w))}')
dists = sorted((dist_to_segment(T, pts[a], pts[b]) * 16.25, a + b) for a, b in combinations(sorted(pts), 2))
say('  closest joining segments to T at print size: ' + ', '.join(f'{n} {d:.2f} mm' for d, n in dists[:4]))
say('  (T is drawn as a ring of radius 3 pt = 1.06 mm with a 1.2 pt stroke, outer edge 3.6 pt = 1.27 mm)')
# P2: Caratheodory on a lattice of targets inside the hexagon; how many dots are needed
need = {}
for i in range(0, 81):
    for j in range(0, 71):
        p = (Fr(i, 10), Fr(j, 10))
        if not contains(H, p):
            continue
        k = next(n for n in (1, 2, 3, 4, 5, 6) if any(contains(hull([pts[x] for x in s]), p)
                                                    for s in combinations(pts, n)))
        need[k] = need.get(k, 0) + 1
say(f'  0.1-unit lattice targets in the hexagon by fewest dots needed: {dict(sorted(need.items()))}')
for name, p in (('A', pts['A']), ('(3,0)', P(3, 0)), ('T', T)):
    k = next(n for n in (1, 2, 3, 4) if any(contains(hull([pts[x] for x in s]), p) for s in combinations(pts, n)))
    say(f'  guide P2 target {name}: needs exactly {k}')

# ---------------------------------------------------------------- P3
say()
say('P3 (p2): square, fixed groupings')
sq = {k: P(*v) for k, v in SRC[2].items()}
for g1, g2 in (('AC', 'BD'), ('AB', 'CD')):
    s = shared_set(hull([sq[x] for x in g1]), hull([sq[x] for x in g2]))
    say(f'  {g1}/{g2}: hulls meet: {s}')
sep = all(p[1] < 4 for p in (sq['A'], sq['B'])) and all(p[1] > 4 for p in (sq['C'], sq['D']))
say(f'  y = 4 strictly separates AB from CD: {sep}')

# ---------------------------------------------------------------- P4
say()
say('P4 (p3): rows on a line, three groups with one common point')
row = {k: P(*v) for k, v in SRC[3].items()}
for labels in ('ABCDE', 'PQRS'):
    parts = set_partitions(labels, 3)
    good = ['/'.join(sorted(p, key=lambda b: (-len(b), b))) for p in parts if meet([[row[x] for x in b] for b in p])]
    say(f'  {labels}: {len(parts)} partitions; successful: {good or "none"}')
# sharp line threshold 2r-1 (guide depth note), all placements on a small line
for r in (2, 3):
    n = 2 * r - 1
    line = [P(x, 0) for x in range(n + 1)]
    from itertools import product
    ok_all = all(any(meet([[dict(zip('abcdefg', t))[x] for x in b] for b in p])
                     for p in set_partitions('abcdefg'[:n], r)) for t in product(line, repeat=n))
    distinct = [P(x, 0) for x in range(2 * r - 2)]
    fails = not any(meet([[dict(zip('abcdefg', distinct))[x] for x in b] for b in p])
                    for p in set_partitions('abcdefg'[:2 * r - 2], r))
    say(f'  r={r}: every placement of {n} labels on {n + 1} line positions works: {ok_all}; '
        f'{2 * r - 2} distinct positions fail: {fails}')

# ---------------------------------------------------------------- P5
say()
say('P5 (p4): regular hexagon. An affine map (x, y) -> (x, (y-4)/(3.5*sqrt(3)/2)) keeps every')
say('  hull incidence and makes the vertices rational:')
hexa = {'A': P(7.5, 0), 'B': P(5.75, 1), 'C': P(2.25, 1), 'D': P(0.5, 0), 'E': P(2.25, -1), 'F': P(5.75, -1)}
parts = set_partitions('ABCDEF', 3)
good = ['/'.join(sorted(p)) for p in parts if meet([[hexa[x] for x in b] for b in p])]
say(f'  {len(parts)} partitions into three groups; successful: {good}')

# ---------------------------------------------------------------- P6
say()
say('P6 (p5): the irregular hexagon of P1')
H6 = hull(list(pts.values()))
strict = all(orient(H6[i], H6[(i + 1) % 6], H6[(i + 2) % 6]) > 0 for i in range(6))
say(f'  strictly convex hexagon with all six as corners: {len(H6) == 6 and strict}')
good = ['/'.join(sorted(p)) for p in parts if meet([[pts[x] for x in b] for b in p])]
say(f'  {len(parts)} partitions into three groups; successful: {good or "none"}')
A, B, C, D, E, F = (pts[x] for x in 'ABCDEF')


def cross_pt(a, b, c, d):
    r = (b[0] - a[0], b[1] - a[1])
    s = (d[0] - c[0], d[1] - c[1])
    den = r[0] * s[1] - r[1] * s[0]
    t = ((c[0] - a[0]) * s[1] - (c[1] - a[1]) * s[0]) / den
    return (a[0] + t * r[0], a[1] + t * r[1])


X = cross_pt(A, D, B, E)
Y = cross_pt(A, D, C, F)
Z = cross_pt(B, E, C, F)
yCF = C[1] + (F[1] - C[1]) * (X[0] - C[0]) / (F[0] - C[0])
say(f'  AD x BE = ({fmt(X[0])}, {fmt(X[1])}); CF at x = {fmt(X[0])} has y = {fmt(yCF)}')
side = max(math.dist(map(float, X), map(float, Y)), math.dist(map(float, Y), map(float, Z)),
           math.dist(map(float, Z), map(float, X)))
say(f'  the three pairwise crossings span up to {side * 16.25:.1f} mm at print size')

open(os.path.join(HERE, 'out_check_bonus.txt'), 'w').write('\n'.join(LINES) + '\n')
