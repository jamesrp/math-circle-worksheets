"""Check of the Week 85 critic follow-up, October 23, 2026 (W85-M-v3, W85-F-v3).

Critic A's should: the red pencil at P sat in one 5 mm foam layer and could tilt 2-3 mm off
its pivot. v3 glues an 18 by 25 mm offcut on the P end so P, like T, holds its pencil in two
layers, and the rehearsal pushes each pencil sideways. Coulds made: the fastener length, the
O hole made with the pin, the binder clip on the pencil, the pin pushed in after the mat is
down, and the guide's account of what blocks full stretch and collapse.

Models the foam-board build in the plane (strips 18 mm wide, holes 80 mm apart and 11 mm from
each end, 7 mm pencils) and checks every number the new text states. Then checks the wording,
that the student packets did not change, and that unchanged pages kept their text and pixels.
Run: python3 check_critic_fixes.py (writes out_check_critic_fixes.txt beside itself).
"""
import math
import os
import re

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
W = os.path.join(ROOT, 'lowell-math-circle-year-2/week-85')
ARC = os.path.join(W, 'archive-before-critic-fixes-2026-10-23')
OUT = []


def ok(cond, msg):
    if not cond:
        raise SystemExit('FAIL ' + msg)
    OUT.append('ok   ' + msg)


# ---------------------------------------------------------------- the build in the plane
L, HALF, END, PEN = 80.0, 9.0, 11.0, 3.5      # hole spacing, half strip width, hole to strip end, pencil radius


def pose(theta):
    """Rhombus angle theta at X between XQ and XT. Long bar O-X-Q along +x."""
    u = (1.0, 0.0)
    v = (math.cos(theta), math.sin(theta))
    O = (0.0, 0.0)
    X = (L, 0.0)
    Q = (2 * L, 0.0)
    T = (X[0] + L * v[0], X[1] + L * v[1])
    Y = (Q[0] + L * v[0], Q[1] + L * v[1])
    P = (2 * Y[0] - Q[0], 2 * Y[1] - Q[1])
    return dict(O=O, X=X, Q=Q, T=T, Y=Y, P=P)


def strip(a, b, ext_a=END, ext_b=END, half=HALF):
    """Rectangle of a strip whose hole centres are a and b."""
    d = (b[0] - a[0], b[1] - a[1])
    n = math.hypot(*d)
    d = (d[0] / n, d[1] / n)
    p = (-d[1] * half, d[0] * half)
    s = (a[0] - d[0] * ext_a, a[1] - d[1] * ext_a)
    e = (b[0] + d[0] * ext_b, b[1] + d[1] * ext_b)
    return [(s[0] + p[0], s[1] + p[1]), (e[0] + p[0], e[1] + p[1]), (e[0] - p[0], e[1] - p[1]), (s[0] - p[0], s[1] - p[1])]


def seg_dist(p, a, b):
    ax, ay = a
    bx, by = b
    t = max(0, min(1, ((p[0] - ax) * (bx - ax) + (p[1] - ay) * (by - ay)) / ((bx - ax) ** 2 + (by - ay) ** 2)))
    return math.dist(p, (ax + t * (bx - ax), ay + t * (by - ay)))


def inside(p, poly):
    c = False
    for i in range(len(poly)):
        a, b = poly[i], poly[(i + 1) % len(poly)]
        if (a[1] > p[1]) != (b[1] > p[1]) and p[0] < a[0] + (p[1] - a[1]) * (b[0] - a[0]) / (b[1] - a[1]):
            c = not c
    return c


def poly_gap(A, B):
    """Separation of two convex polygons (0 when they overlap)."""
    if any(inside(p, B) for p in A) or any(inside(p, A) for p in B):
        return 0.0
    return min(seg_dist(p, B[i], B[(i + 1) % 4]) for p in A for i in range(4))


def circle_poly_gap(c, r, A):
    if inside(c, A):
        return 0.0
    return max(0.0, min(seg_dist(c, A[i], A[(i + 1) % 4]) for i in range(4)) - r)


rows = []
for k in range(1, 3600):
    th = math.radians(k / 20)
    q = pose(th)
    OT = math.dist(q['O'], q['T'])
    xt_qy = poly_gap(strip(q['X'], q['T']), strip(q['Q'], q['Y']))          # same (middle) layer
    tpen_long = circle_poly_gap(q['T'], PEN, strip(q['O'], q['Q']))        # T pencil against the bottom bar
    off = strip(q['P'], q['Y'], 0.0, 0.0)                                    # placeholder, replaced below
    # The offcut: 18 by 25 mm, flush with the P end of Q-Y-P, on top (the T-Y layer).
    d = (q['P'][0] - q['Y'][0], q['P'][1] - q['Y'][1])
    n = math.hypot(*d)
    d = (d[0] / n, d[1] / n)
    end = (q['P'][0] + d[0] * END, q['P'][1] + d[1] * END)
    start = (end[0] - d[0] * 25, end[1] - d[1] * 25)
    off = strip(start, end, 0.0, 0.0)
    off_ty = poly_gap(off, strip(q['T'], q['Y']))                          # same (top) layer
    off_tpen = circle_poly_gap(q['T'], PEN, off)
    rows.append((OT, xt_qy, tpen_long, off_ty, off_tpen))
rows.sort()


def threshold(col, lo=True):
    """Largest OT (collapse side) or smallest OT (stretch side) at which the contact column is 0."""
    hits = [r[0] for r in rows if r[col] == 0.0]
    if lo:
        return max([h for h in hits if h < 80], default=None)
    return min([h for h in hits if h > 80], default=None)


c1, s1 = threshold(1), threshold(1, False)
ok(17.5 < c1 < 18.6 and 158.5 < s1 < 159.6, f'X-T meets Q-Y (one layer) when OT < {c1:.1f} mm or OT > {s1:.1f} mm (the rhombus 18 mm high): "above about 159 mm"')
c3 = threshold(3)
ok(c3 is not None and 21 < c3 < 22.5 and c3 > c1 and threshold(3, False) is None,
   f'the P offcut (top layer) meets T-Y when OT < {c3:.1f} mm, before X-T meets Q-Y on the collapse side, and never near full stretch: "below about 22 mm"')
c2, s2 = threshold(2), threshold(2, False)
ok(c2 < c3 and s2 > s1, f'the T pencil would meet the long bar O-X-Q only beyond both stops: OT < {c2:.1f} or > {s2:.1f} mm')
c4 = threshold(4)
ok(c4 is None or c4 < c3, 'the P offcut meets the T pencil only beyond the stop' if c4 else 'the P offcut never meets the T pencil')
zone = [r for r in rows if 70 <= r[0] <= 123]
ok(min(min(r[1:]) for r in zone) > 30, f'T zone (OT 70-123 mm): every listed pair clears by at least {min(min(r[1:]) for r in zone):.0f} mm, "well clear"')
# The offcut covers the P hole with board on every side.
ok(25 - END > PEN and HALF > PEN, 'an 18 by 25 mm offcut flush with the P end covers the P hole: 11 mm to the end, 14 mm toward Y, 9 mm each side')
# The tilt the critic described: a 7 mm pencil in one 5 mm layer, its point 7-10 mm below the strip.
lo, hi = 7 * math.tan(math.radians(15)), 10 * math.tan(math.radians(15))
ok(1.8 < lo < 2.0 and 2.6 < hi < 2.8, f'a 15 degree tilt moves a point 7-10 mm below the strip by {lo:.1f}-{hi:.1f} mm: "2-3 mm"')
stack = 2 * 5 + 1  # two foam layers and a washer, mm
ok(20 - stack >= 9, f'fasteners 20-25 mm long pass the {stack} mm stack (two 5 mm layers and a washer) and leave {20 - stack}-{25 - stack} mm of leg to fold')

# ---------------------------------------------------------------- wording and unchanged pages


def flat(p):
    return re.sub(r'\s+', ' ', p.get_text()).replace('’', "'")


M, MO = pymupdf.open(os.path.join(W, 'week-85-materials.pdf')), pymupdf.open(os.path.join(ARC, 'week-85-materials.pdf'))
G, GO = pymupdf.open(os.path.join(W, 'week-85-facilitator.pdf')), pymupdf.open(os.path.join(ARC, 'week-85-facilitator.pdf'))
ok(len(M) == len(MO) == 10 and len(G) == len(GO) == 6, 'materials still 10 pages, guide still 6')
m1, m2 = flat(M[0]), flat(M[1])
ok('Make the X, Q and Y holes with a skewer and the O hole with the pushpin itself' in m1 and 'Glue an 18 by 25 mm offcut' in m1
   and 'both T holes and both P layers' in m1, 'materials p. 1: O hole with the pin; the P offcut; pencils through both layers')
ok('three brass fasteners about 20–25 mm (3/4 to 1 inch) long' in m2, 'materials p. 2: fastener length')
ok('the red pencil through both P layers' in m2 and 'Once the mat is on the base (below), push the pin through O' in m2
   and 'clip the binder clip to that pencil just above the bar' in m2, 'materials p. 2: P in two layers, pin after the mat, clip on the pencil')
ok('push each pencil sideways, and its point should move no more than about 1 mm' in m2, 'materials p. 2: the sideways-push rehearsal check')
for i in range(2, 10):
    ok(flat(MO[i]).replace('W85-M-v2', 'W85-M-v3') == flat(M[i]), f'materials p. {i + 1}: text unchanged apart from the footer')
    a = MO[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, 612, 740)).samples
    b = M[i].get_pixmap(dpi=100, clip=pymupdf.Rect(0, 0, 612, 740)).samples
    ok(a == b, f'materials p. {i + 1}: pixels above the footer unchanged')
g2, g4 = flat(G[1]), flat(G[3])
ok('three brass fasteners 20–25 mm long' in g2 and 'the O hole with the pushpin itself' in g2 and 'offcut on top of the P end' in g2
   and 'a tilt moves the point 2–3 mm' in g2, 'guide p. 2: fastener length, O hole, P offcut and the tilt')
ok('Once the mat is on the base, pin O through it' in g2 and 'clip the binder clip onto a pencil that marks faintly, just above the bar' in g2,
   'guide p. 2: pin after the mat; clip on the pencil')
ok('each pencil point moves no more than about 1 mm when the pencil is pushed sideways' in g2 and 'fastener at Q and the pin at O stop' not in g2,
   'guide p. 2: the rehearsal pushes each pencil sideways')
ok('X–T and Q–Y share a layer and meet when OT rises above about 159 mm' in g4 and 'meets T–Y , the top strip, when OT falls below about 22 mm' in g4
   and 'fastener at Q and the pin at O should block' not in g4, 'guide p. 4: what blocks full stretch and collapse, as computed above')
for i in (0, 2, 4, 5):
    ok(flat(GO[i]).replace('W85-F-v2', 'W85-F-v3') == flat(G[i]), f'guide p. {i + 1}: text unchanged apart from the footer')
for name in ('shared', 'upper'):
    a = open(os.path.join(W, f'week-85-{name}.pdf'), 'rb').read()
    b = open(os.path.join(ROOT, f'lowell-math-circle-year-2/source/week-85/editable/reference-pdfs/week-85-{name}.pdf'), 'rb').read()
    ok(a == b and 'W85-' in flat(pymupdf.open(os.path.join(W, f'week-85-{name}.pdf'))[0]), f'student {name} packet unchanged (v2), reference copy identical')

print('\n'.join(OUT))
print(f'{len(OUT)} checks passed')
with open(os.path.join(HERE, 'out_check_critic_fixes.txt'), 'w') as f:
    f.write('\n'.join(OUT) + f'\n{len(OUT)} checks passed\n')
