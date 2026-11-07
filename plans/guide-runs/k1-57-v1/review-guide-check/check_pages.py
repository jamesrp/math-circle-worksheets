"""Read the final student PDF's vector drawings: P1 shapes, board sizes, dot spacing,
and the kit capacity the boards invite.  Usage: python3 check_pages.py [k-1.pdf]"""
import os as _os
_REPO = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "..", ".."))
import sys, math, warnings
from collections import Counter
warnings.filterwarnings('ignore')
import fitz

pdf = sys.argv[1] if len(sys.argv) > 1 else _REPO + '/plans/k1-drafts/week-57/k-1.pdf'
U = 20 / 25.4 * 72          # 20 mm in points
doc = fitz.open(pdf)

print('== P1 shapes (light fill), in reading order ==')
shapes = []
for dr in doc[0].get_drawings():
    f = dr.get('fill')
    if f and abs(f[0] - 0.93) < 0.01:
        pts = []
        for it in dr['items']:
            if it[0] == 'l':
                for q in (it[1], it[2]):
                    t = (round(q.x / U * 2) / 2, round(-q.y / U * 2) / 2)
                    if t not in pts:
                        pts.append(t)
        shapes.append((dr['rect'].y0, dr['rect'].x0, pts))
for _, _, pts in sorted(shapes, key=lambda s: (round(s[0] / 20), s[1])):
    x0 = min(p[0] for p in pts); y0 = min(p[1] for p in pts)
    v = [(int(p[0] - x0), int(p[1] - y0)) for p in pts]
    n = len(v)
    area2 = abs(sum(v[i][0] * v[(i + 1) % n][1] - v[(i + 1) % n][0] * v[i][1] for i in range(n)))
    B = sum(math.gcd(abs(v[i][0] - v[(i + 1) % n][0]), abs(v[i][1] - v[(i + 1) % n][1])) for i in range(n))
    sides = [(v[i], v[(i + 1) % n], math.gcd(abs(v[i][0] - v[(i + 1) % n][0]), abs(v[i][1] - v[(i + 1) % n][1])) - 1)
             for i in range(n)]
    between = [(a, b, k) for a, b, k in sides if k > 0]
    print(f'  vertices {v}: halves {area2}, outline dots {B}, dots between corners {between}')

print('\n== working-board dot grids (dots >= 2 mm) ==')
for pno in range(1, len(doc)):
    dots = []
    for dr in doc[pno].get_drawings():
        r = dr['rect']
        if dr.get('fill') == (0.0, 0.0, 0.0) and 5 < r.width < 9 and abs(r.width - r.height) < 0.5:
            dots.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2))
    xs = sorted({round(x, 1) for x, _ in dots}); ys = sorted({round(y, 1) for _, y in dots})
    gx = sorted({round(b - a, 1) for a, b in zip(xs, xs[1:])})
    gy = sorted({round(b - a, 1) for a, b in zip(ys, ys[1:])})
    print(f'  page {pno + 1}: {len(dots)} dots; column gaps (pt) {gx}; row gaps (pt) {gy}; 20 mm = {U:.2f} pt')

print('\n== kit capacity: 10 squares, 20 halves per pair ==')
print('  P2: six boards x 3 halves =', 6 * 3, 'halves')
print('  P3: six boards x 4 halves =', 6 * 4, 'halves (kit 20): at most', 20 // 4, 'shapes built at once')
p5 = {'none': (0, 4), 'one': (1, 3), 'two next door': (2, 2), 'two opposite': (2, 2), 'three': (3, 1), 'four': (4, 0)}
sq = sum(a for a, b in p5.values()); hv = sum(b for a, b in p5.values())
print(f'  P5: all six closers at once need {sq} squares and {hv} half pieces (kit 10 squares)')
print('  P7: one answer needs 8 halves; both at once 16 halves')
