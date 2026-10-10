#!/usr/bin/env python3
"""Week 73: read the delivered student PDF and check every diagram against its text.

Uses pymupdf to read stroked/filled paths and text boxes from
lowell-math-circle-year-2/week-73/week-73-students.pdf (found from this file's
location, four folders up). Units: 1 pt = 1/72 in.
Run: python3 check_diagrams.py  (output saved as check_diagrams.py.out)
"""
from pathlib import Path
import pymupdf

REPO = Path(__file__).resolve().parents[4]
PDF = REPO / 'lowell-math-circle-year-2/week-73/week-73-students.pdf'
doc = pymupdf.open(PDF)
fails = checks = 0
TOL = 0.15


def ok(cond, msg):
    global fails, checks
    checks += 1
    fails += 0 if cond else 1
    print(('PASS ' if cond else 'FAIL ') + msg)


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def rects(page, width=0.8):
    """Closed four-segment thick outlines -> (x0, y0, x1, y1)."""
    out = []
    for d in page.get_drawings():
        it = d['items']
        if d['type'] == 's' and len(it) == 4 and all(i[0] == 'l' for i in it) and close(d.get('width') or 0, width, .05):
            xs = [p.x for i in it for p in i[1:]]
            ys = [p.y for i in it for p in i[1:]]
            out.append((min(xs), min(ys), max(xs), max(ys)))
    return out


def dots(page):
    """Filled circles (4 Bezier curves) -> centre."""
    out = []
    for d in page.get_drawings():
        it = d['items']
        if d['type'] == 'f' and len(it) == 4 and all(i[0] == 'c' for i in it):
            xs = [p.x for i in it for p in i[1:]]
            ys = [p.y for i in it for p in i[1:]]
            out.append(((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2))
    return out


def segs(page, width=None, dashed=None):
    out = []
    for d in page.get_drawings():
        if d['type'] != 's':
            continue
        if width is not None and not close(d.get('width') or 0, width, .05):
            continue
        isdash = d.get('dashes') not in (None, '[] 0')
        if dashed is not None and isdash != dashed:
            continue
        for i in d['items']:
            if i[0] == 'l':
                out.append((i[1].x, i[1].y, i[2].x, i[2].y))
    return out


def labels(page):
    out = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            t = ''.join(s['text'] for s in l['spans']).strip()
            out.append((t, l['bbox'], l['dir']))
    return out


def find(page, text):
    return [bb for t, bb, _ in labels(page) if t == text]


U = 0.94 * 72  # one drawn unit on pages 1-3


def board_checks(pn):
    page = doc[pn]
    print(f'\n-- page {pn + 1}: fan board --')
    R = rects(page)
    rect = [r for r in R if close(r[2] - r[0], 4 * U, .2)]
    sq = [r for r in R if close(r[2] - r[0], 2 * U, .2)]
    ok(len(rect) == 1 and close(rect[0][3] - rect[0][1], U, .2), f'old sheet is 4 x 1 units of 0.94 in: {rect}')
    ok(len(sq) == 1 and close(sq[0][3] - sq[0][1], 2 * U, .2), f'square is 2 x 2 units at the same scale (equal axes): {sq}')
    r, s = rect[0], sq[0]
    cx, cy = (r[0] + r[2]) / 2, (r[1] + r[3]) / 2
    D = dots(page)
    ok(any(close(x, cx) and close(y, cy) for x, y in D), 'O dot at the centre of the old sheet')
    corners_r = [(r[0], r[3]), (r[2], r[3]), (r[2], r[1]), (r[0], r[1])]
    corners_s = [(s[0], s[3]), (s[2], s[3]), (s[2], s[1]), (s[0], s[1])]
    ok(all(any(close(x, a) and close(y, b) for x, y in D) for a, b in corners_r + corners_s), 'corner dots on both sheets')
    ok(not any(s[0] + .5 < x < s[2] - .5 and s[1] + .5 < y < s[3] - .5 for x, y in D), 'no O printed in the square (children place it)')
    spokes = [g for g in segs(page, .4) if any(close(g[2], cx) and close(g[3], cy) for _ in [0])]
    ends = sorted((round(g[0], 1), round(g[1], 1)) for g in spokes)
    ok(len(spokes) == 4 and all(any(close(e[0], a, .3) and close(e[1], b, .3) for a, b in corners_r) for e in ends),
       'four spokes join O to A, B, C, D in the old sheet')
    # labels: corners
    for name, (a, b) in zip('ABCD', corners_r):
        bb = find(page, name)
        ok(any(abs((q[0] + q[2]) / 2 - a) < 14 and abs((q[1] + q[3]) / 2 - b) < 14 for q in bb), f'old {name} label beside its corner')
    for name, (a, b) in zip('ABCD', corners_s):
        bb = find(page, name)
        ok(any(abs((q[0] + q[2]) / 2 - a) < 14 and abs((q[1] + q[3]) / 2 - b) < 14 for q in bb), f'new {name} label beside its corner')
    side_label_report(page, r, s)


def side_label_report(page, r, s):
    right = find(page, 'right')[0]
    left = find(page, 'left')[0]
    gap = left[0] - right[2]
    print(f'   gap between the two sheets: {s[0] - r[2]:.1f} pt; old "right" box x={right[0]:.1f}-{right[2]:.1f}, '
          f'new "left" box x={left[0]:.1f}-{left[2]:.1f}; space between the two words {gap:.1f} pt = {gap / 72 * 25.4:.1f} mm')
    print(f'   old "right": {right[0] - r[2]:.1f} pt from old right edge, {s[0] - right[2]:.1f} pt from square left edge')
    print(f'   new "left":  {s[0] - left[2]:.1f} pt from square left edge, {left[0] - r[2]:.1f} pt from old right edge')
    ok(right[0] > r[2] and left[2] < s[0], 'inner "right"/"left" labels both sit in the gap on their own sides (correct attribution)')
    ok(gap > 10, f'inner "right" and "left" labels are clearly separated (> 10 pt apart); measured {gap:.1f} pt')


page = doc[0]
print('-- page 1: stretch example --')
S = [g for g in segs(page, .8) if close(g[1], g[3]) and g[1] < 150]
lens = sorted(abs(g[2] - g[0]) for g in S)
cm = 72 / 2.54
ok(len(lens) == 2 and close(lens[0], 2 * cm, .1) and close(lens[1], 3 * cm, .1),
   f'example segments print at 2 cm and 3 cm: {[round(x / cm, 3) for x in lens]} cm')

board_checks(0)
board_checks(1)

# grid on pp. 1-2
for pn in (0, 1):
    page = doc[pn]
    for d in page.get_drawings():
        col = d.get('color')
        if d['type'] == 's' and col and col[0] > .8 and len(d['items']) > 10:
            for axis in ('x', 'y'):
                v = sorted({round(getattr(q, axis), 2) for i in d['items'] for q in i[1:]})
                steps = {round(b - a, 2) for a, b in zip(v, v[1:])}
                ok(all(close(st, U / 4, .05) for st in steps),
                   f'p.{pn + 1} grid ({len(v)} {axis}-lines, {v[0]:.1f}-{v[-1]:.1f}) step = quarter unit ({U / 4:.2f} pt): {steps}')

# page 2 example triangles
page = doc[1]
print('\n-- page 2: halfway example --')
D = dots(page)
tri = [g for g in segs(page, .4, False) if g[1] < 260]
pts = {}
for t, bb, _ in labels(page):
    if t in 'PQRMN' and len(t) == 1 and bb[1] < 240:
        pts.setdefault(t, []).append(((bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2))
top = sorted([d for d in D if d[1] < 260])
left_pts, right_pts = [d for d in top if d[0] < 300], [d for d in top if d[0] > 300]


def nearest(lbl, side):
    c = [q for q in pts[lbl] if (q[0] < 300) == (side == 'L')][0]
    return min((d for d in (left_pts if side == 'L' else right_pts)), key=lambda d: (d[0] - c[0]) ** 2 + (d[1] - c[1]) ** 2)


for side in 'LR':
    P, Q, R, M, N = (nearest(k, side) for k in 'PQRMN')
    ok(close(M[0], (P[0] + Q[0]) / 2) and close(M[1], (P[1] + Q[1]) / 2), f'{side}: M is the midpoint of PQ')
    ok(close(N[0], (P[0] + R[0]) / 2) and close(N[1], (P[1] + R[1]) / 2), f'{side}: N is the midpoint of PR')
dash = segs(page, .4, True)
ok(len(dash) == 2, 'one dashed MN segment in each triangle')

# page 3
page = doc[2]
print('\n-- page 3: rule board --')
R = rects(page)
rect = [r for r in R if close(r[2] - r[0], 4 * U, .2)][0]
sq = [r for r in R if close(r[2] - r[0], 2 * U, .2)][0]
ok(close(rect[3] - rect[1], U, .2) and close(sq[3] - sq[1], 2 * U, .2), 'p.3 sheets are 4 x 1 and 2 x 2 at 0.94 in per unit')
dot = segs(page, .8, True)
vx = sorted({round(g[0], 2) for g in dot if close(g[0], g[2])})
hy = sorted({round(g[1], 2) for g in dot if close(g[1], g[3])})
inner_v = [x for x in vx if rect[0] + 1 < x < rect[2] - 1]
inner_h = [y for y in hy if rect[1] + 1 < y < rect[3] - 1]
ok(len(inner_v) == 7 and all(close(b - a, U / 2, .05) for a, b in zip([rect[0]] + inner_v, inner_v + [rect[2]])),
   f'7 interior dotted verticals at half-unit spacing ({len(inner_v)} found)')
ok(len(inner_h) == 1 and close(inner_h[0], (rect[1] + rect[3]) / 2, .1), 'one dotted horizontal at mid-height')
ok(not any(sq[0] < g[0] < sq[2] for g in dot), 'square left blank for children to draw the images')
side_label_report(page, rect, sq)

# page 4
page = doc[3]
print('\n-- page 4: other targets --')
u4 = 0.6 * 72
R = sorted(rects(page), key=lambda r: (r[1] > 300, r[0]))
dims = [(round((r[2] - r[0]) / u4, 3), round((r[3] - r[1]) / u4, 3)) for r in R]
print('   rectangles in units of 0.6 in:', dims)
ok(dims == [(4, 1), (6, 2), (4, 1), (2, 3)], 'p.4 pairs: 4x1 -> 6x2 and 4x1 -> 2x3 at one shared scale')
for (t, bb, dr) in labels(page):
    if t == 'left':
        y = (bb[1] + bb[3]) / 2
        owner = min(R, key=lambda r: abs(r[0] - bb[2]) + (0 if r[1] <= y <= r[3] else 999))
        ok(owner[0] - bb[2] > 0 and owner[1] <= y <= owner[3], f'"left" label at x={bb[0]:.0f} sits left of a rectangle spanning its height')
    if t == 'top':
        x = (bb[0] + bb[2]) / 2
        owner = min(R, key=lambda r: abs(r[1] - bb[3]) + (0 if r[0] <= x <= r[2] else 999))
        ok(owner[1] - bb[3] > 0 and close(x, (owner[0] + owner[2]) / 2, 1.5), f'"top" label at y={bb[1]:.0f} centred above a rectangle')
margin = 612 - 46.8
over = max(r[2] for r in R) - margin
print(f'   (info) widest p.4 figure ends {over:+.1f} pt relative to the right text margin (page edge at 612 pt)')

print(f'\n{checks} checks, {fails} failures')
