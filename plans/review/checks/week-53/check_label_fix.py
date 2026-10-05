"""Test candidate price-label placements for links CD and DE on the six-place map
(student pp. 6 and 8). Vertex positions are re-read from the delivered PDF
(page 6, converted to map units); label boxes use the printed white-box size.
A placement passes when its own link is clearly nearest (other links >= 1.5x
farther) and the white box crosses no other link, at both printed scales.
Run: python3 check_label_fix.py  (writes out_check_label_fix.txt)
"""
import math
import os as _os
import sys

HERE = _os.path.dirname(_os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pdfgeom  # noqa: E402
from check_diagrams import seg_dist, seg_hits_rect  # noqa: E402

CM = 72 / 2.54
page6 = pdfgeom.read(pdfgeom.STUDENT_PDF)[5]
verts = [c for c in page6['curves'] if c['op'] == 'B' and c['rx'] > 5]
letters = [t for t in page6['texts'] if len(t['s']) == 1 and t['s'].isupper()]
P = {}
for c in verts:
    t = min(letters, key=lambda t: math.hypot(t['x'] + 4 - c['cx'], t['y'] + 4 - c['cy']))
    P[t['s']] = (c['cx'], c['cy'])
ax, ay = P['B']
S6 = 1.7 * CM  # page-6 points per map unit
M = {k: ((x - ax) / S6, (y - ay) / S6) for k, (x, y) in P.items()}
EDGES = ['AB', 'AC', 'BC', 'CD', 'BD', 'CE', 'DE', 'EF', 'DF']
BOX_W, BOX_H = 9.44 / CM, 11.31 / CM  # printed white label box, cm
OFF = 0.32  # printed perpendicular offset, cm

out = []


def place(edge, frac, side, scale, off=OFF):
    (x0, y0), (x1, y1) = M[edge[0]], M[edge[1]]
    mx, my = x0 + (x1 - x0) * frac, y0 + (y1 - y0) * frac
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    nx, ny = -dy / L * side, dx / L * side
    return mx + nx * off / scale, my + ny * off / scale


def judge(edge, frac, side, scale, off=OFF):
    px, py = place(edge, frac, side, scale, off)
    d = {e: seg_dist(px, py, *M[e[0]], *M[e[1]]) * scale * 10 for e in EDGES}  # mm
    own = d[edge]
    other = min((v, e) for e, v in d.items() if e != edge)
    box = {'x0': px - BOX_W / 2 / scale, 'x1': px + BOX_W / 2 / scale,
           'y0': py - BOX_H / 2 / scale, 'y1': py + BOX_H / 2 / scale}
    crossed = [e for e in EDGES if e != edge and seg_hits_rect(*M[e[0]], *M[e[1]], box)]
    if off == 0:
        own = 0.0  # label sits on its own link
    circle = [v for v in M if math.hypot(M[v][0] - px, M[v][1] - py) * scale < 0.52 + 0.25]
    ok = other[0] >= max(1.5 * own, 2.5) and not crossed and not circle
    return ok, own, other, crossed, circle


for edge in ('CD', 'DE'):
    out.append('--- %s ---' % edge)
    for side in (1, -1):
        for frac in (0.25, 0.3, 0.5, 0.7, 0.75):
            res = [judge(edge, frac, side, s) for s in (1.7, 1.25)]
            tag = 'PASS' if all(r[0] for r in res) else 'fail'
            desc = '; '.join('scale %.2f: own %.1f mm, nearest other %s %.1f mm%s%s' % (
                s, r[1], r[2][1], r[2][0], (' crosses ' + ','.join(r[3])) if r[3] else '',
                (' near circle ' + ','.join(r[4])) if r[4] else '') for s, r in zip((1.7, 1.25), res))
            out.append('%s side %+d frac %.2f: %s  [%s]' % (tag, side, frac, desc,
                                                           'printed placement' if (frac == 0.5 and side == 1) else ''))
out.append('--- CD alternatives (offset in cm) ---')
for frac, side, off in ((0.5, 1, 0.0), (0.75, 1, 0.2), (0.25, -1, 0.2), (0.7, 1, 0.22)):
    res = [judge('CD', frac, side, s, off) for s in (1.7, 1.25)]
    tag = 'PASS' if all(r[0] for r in res) else 'fail'
    out.append('%s CD frac %.2f side %+d offset %.2f cm: %s' % (tag, frac, side, off, '; '.join(
        'scale %.2f: own %.1f mm, nearest other %s %.1f mm%s' % (s, r[1], r[2][1], r[2][0],
        (' crosses ' + ','.join(r[3])) if r[3] else '') for s, r in zip((1.7, 1.25), res))))
out.append('--- BD (printed above at midpoint, under circle C on p. 8) ---')
for frac, side in ((0.5, 1), (0.5, -1)):
    res = [judge('BD', frac, side, s) for s in (1.7, 1.25)]
    tag = 'PASS' if all(r[0] for r in res) else 'fail'
    out.append('%s BD frac %.2f side %+d: %s' % (tag, frac, side, '; '.join(
        'scale %.2f: own %.1f mm, nearest other %s %.1f mm%s%s' % (s, r[1], r[2][1], r[2][0],
        (' crosses ' + ','.join(r[3])) if r[3] else '', (' near circle ' + ','.join(r[4])) if r[4] else '')
        for s, r in zip((1.7, 1.25), res))))
txt = '\n'.join(out)
print(txt)
open(_os.path.join(HERE, 'out_check_label_fix.txt'), 'w').write(txt + '\n')
