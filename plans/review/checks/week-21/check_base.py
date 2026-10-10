#!/usr/bin/env python3
"""Independent exact check of every Week 21 base problem and every number in the adult guide.

Board data come from geometry.json (read back out of the delivered student PDFs by
extract_geometry.py) and are rounded to the 0.1 cm grid they lie on, then handled as
exact fractions.  Nothing from the package's own check scripts or audit JSON is used.

Method, per same-side pair: the length of the route through contact t is
    L(t) = |A - (t,h)| + |(t,h) - B|.
The reflection formula is checked against a brute-force scan of L over 400,001
contacts on the marked segment (it never uses the formula), and every square-root
comparison is made exactly by comparing squares or with a 60-digit Decimal.
"""
import json, math
from fractions import Fraction as F
from decimal import Decimal, getcontext
from common import HERE

getcontext().prec = 60
G = json.loads((HERE / 'geometry.json').read_text())
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); out.append(s); print(s)

def fr(v):
    return F(round(v * 10), 10)

def board(band, page):
    g = G[band][page - 1]
    ln = g['line']
    axis = 'h' if abs(ln['from'][1] - ln['to'][1]) < 1e-6 else 'v'
    pts = {k: (fr(v['x']), fr(v['y'])) for k, v in g['named'].items()}
    if axis == 'h':
        h = fr(ln['from'][1]); lo, hi = fr(ln['from'][0]), fr(ln['to'][0])
    else:
        h = fr(ln['from'][0]); lo, hi = fr(ln['from'][1]), fr(ln['to'][1])
    return dict(axis=axis, h=h, lo=min(lo, hi), hi=max(lo, hi), pts=pts)

def coords(b, p):
    """Return (along, height above line) for point p."""
    x, y = p
    return (x, y - b['h']) if b['axis'] == 'h' else (y, x - b['h'])

def sqrtD(q):
    q = F(q); return (Decimal(q.numerator) / Decimal(q.denominator)).sqrt()

def route_len(b, p, q, t):
    """Exact-ish (Decimal) length A->contact t->B."""
    (pa, ph), (qa, qh) = coords(b, p), coords(b, q)
    return sqrtD((pa - t) ** 2 + ph ** 2) + sqrtD((qa - t) ** 2 + qh ** 2)

def route_len_f(b, p, q, t):
    (pa, ph), (qa, qh) = coords(b, p), coords(b, q)
    pa, ph, qa, qh = float(pa), float(ph), float(qa), float(qh)
    return math.hypot(pa - t, ph) + math.hypot(qa - t, qh)

def optimum(b, p, q):
    """Exact optimal contact via reflection, and squared minimum (same side only)."""
    (pa, ph), (qa, qh) = coords(b, p), coords(b, q)
    assert ph * qh > 0
    u, v = abs(ph), abs(qh)
    t = (v * pa + u * qa) / (u + v)
    return t, (qa - pa) ** 2 + (u + v) ** 2

def scan(b, p, q, n=400000):
    lo, hi = float(b['lo']), float(b['hi'])
    best = None
    for i in range(n + 1):
        t = lo + (hi - lo) * i / n
        L = route_len_f(b, p, q, t)
        if best is None or L < best[1]:
            best = (t, L)
    return best

def check_pair(name, b, a, c):
    p, q = b['pts'][a], b['pts'][c]
    t, m2 = optimum(b, p, q)
    st, sL = scan(b, p, q)
    inside = b['lo'] < t < b['hi']
    say(f'  {name} {a}{c}: contact {t} = {float(t):.5f}, min^2 = {m2} (min {float(sqrtD(m2)):.5f}); '
        f'scan contact {st:.4f}, scan min {sL:.5f}; strictly inside marks: {inside}')
    assert abs(st - float(t)) < 1e-3 and abs(sL - float(sqrtD(m2))) < 1e-6 and inside
    # L at the exact contact equals sqrt(m2)
    assert abs(route_len(b, p, q, t) - sqrtD(m2)) < Decimal('1e-40')
    return t, m2

problems = {}
# ---------- equal-height board: K-1 P1
say('K-1 P1 (equal-height board)')
b = board('k-1', 1); A, B = b['pts']['A'], b['pts']['B']
say('  A, B =', A, B, ' line y =', b['h'], ' marks', b['lo'], b['hi'])
t, m2 = check_pair('K-1 P1', b, 'A', 'B')
mid = (A[0] + B[0]) / 2
assert A[1] == B[1] and mid == F(84, 10) and t == mid and m2 == F('213.8')
for d in [F(1), F(2), F(4), F(78, 10)]:
    L1 = route_len(b, A, B, mid - d); L2 = route_len(b, A, B, mid + d)
    assert abs(L1 - L2) < Decimal('1e-50')
say('  mirror contacts 8.4 -/+ d give equal totals for d = 1, 2, 4, 7.8 (d = 7.8 puts both contacts on the end marks)')
l1 = (F('6.4') - A[0]) ** 2 + (A[1] - b['h']) ** 2; l2 = (B[0] - F('6.4')) ** 2 + (B[1] - b['h']) ** 2
say(f'  guide M1 = 6.4: legs^2 = {float(l1)}, {float(l2)}  (guide: 35.05, 79.85)')
assert l1 == F('35.05') and l2 == F('79.85')
assert b['lo'] == mid - F('7.8') and b['hi'] == mid + F('7.8')

# ---------- guesses board: K-1 P2
say('K-1 P2 (two drawn guesses)')
b = board('k-1', 2); A, B = b['pts']['A'], b['pts']['B']
t, m2 = check_pair('K-1 P2', b, 'A', 'B')
assert t == F(3473, 525) and m2 == F('259.09')
for g in G['k-1'][1]['routes']:
    gx = fr(g['pts'][1][0])
    L = route_len(b, A, B, gx)
    say(f'  drawn guess via x = {gx}: length {L:.5f} (> min by {L - sqrtD(m2):.3f} cm)')
    assert L > sqrtD(m2)
Bp = (B[0], 2 * b['h'] - B[1]); say('  B\' =', Bp, ' on sheet:', 0 <= Bp[1] <= F('18.2'))

# ---------- mirror board: K-1 P3, 2-3 P2, 4-5 P2
say('Mirror board (K-1 P3, 2-3 P2, 4-5 P2)')
for band, pg in [('k-1', 3), ('grades-2-3', 2), ('grades-4-5', 2)]:
    b = board(band, pg); A, B, C = (b['pts'][k] for k in 'ABC')
    assert B[0] == C[0] and B[1] - b['h'] == b['h'] - C[1]
    # every contact: MB^2 == MC^2 exactly
    for k in range(0, 157):
        tt = b['lo'] + (b['hi'] - b['lo']) * F(k, 156)
        assert (B[0] - tt) ** 2 + (B[1] - b['h']) ** 2 == (C[0] - tt) ** 2 + (C[1] - b['h']) ** 2
say('  B and C are mirror images in y = 8.7 on all three pages; MB = MC exactly at 157 rational contacts and by symmetry at all')
b = board('k-1', 3); A, B, C = (b['pts'][k] for k in 'ABC')
s = (A[1] - b['h']) / (A[1] - C[1]); xc = A[0] + s * (C[0] - A[0])
say(f'  straight AC crosses at x = {xc} = {float(xc):.5f}; |AC|^2 = {(C[0]-A[0])**2 + (C[1]-A[1])**2}')
assert xc == F(8751, 1010) and (C[0]-A[0])**2 + (C[1]-A[1])**2 == F('225.22')
t, m2 = check_pair('mirror', b, 'A', 'B'); assert t == xc and m2 == F('225.22')

# ---------- unequal board: K-1 P4, 2-3 P3, 4-5 P3
say('Unequal-height board (K-1 P4, 2-3 P3, 4-5 P3)')
for band, pg in [('k-1', 4), ('grades-2-3', 3), ('grades-4-5', 3)]:
    b = board(band, pg); t, m2 = check_pair(band, b, 'A', 'B')
    assert t == F('6.3') and m2 == F('248.04')
A, B = b['pts']['A'], b['pts']['B']
leg1 = (t - A[0]) ** 2 + (A[1] - b['h']) ** 2; leg2 = (B[0] - t) ** 2 + (B[1] - b['h']) ** 2
say(f'  legs^2 {leg1}, {leg2}; leg2 = 4*leg1: {leg2 == 4 * leg1}; midpoint of feet {(A[0]+B[0])/2}; heights {A[1]-b["h"]}:{B[1]-b["h"]}, runs {t-A[0]}:{B[0]-t}')
assert leg1 == F('27.56') and leg2 == 4 * leg1 and (A[0] + B[0]) / 2 == F('8.3')

# ---------- compare board: K-1 P5, 2-3 P1, 4-5 P1
say('Compare board (K-1 P5, 2-3 P1, 4-5 P1)')
for band, pg in [('k-1', 5), ('grades-2-3', 1), ('grades-4-5', 1)]:
    b = board(band, pg)
    tab, mab = check_pair(band, b, 'A', 'B'); tac, mac = check_pair(band, b, 'A', 'C')
    assert (tab, mab, tac, mac) == (F(658, 71), F('175.85'), F(1646, 295), F('203.24'))
A, B, C = (b['pts'][k] for k in 'ABC')
dab = (B[0]-A[0])**2 + (B[1]-A[1])**2; dac = (C[0]-A[0])**2 + (C[1]-A[1])**2
say(f'  AB route shorter (175.85 < 203.24); difference {float(sqrtD(mac)-sqrtD(mab)):.3f} cm. Direct |AB|^2 = {float(dab)}, |AC|^2 = {float(dac)} (direct distance points the other way)')
worst_ab = max(route_len(b, A, B, b['lo']), route_len(b, A, B, b['hi']))
say(f'  longest legal AB route {worst_ab:.3f} > shortest AC {sqrtD(mac):.3f}: {worst_ab > sqrtD(mac)}')

# ---------- vertical board: K-1 P6, 2-3 P4
say('Vertical board (K-1 P6, 2-3 P4)')
for band, pg in [('k-1', 6), ('grades-2-3', 4)]:
    b = board(band, pg); res = {}
    for a, c in ['AB', 'AC', 'BC']:
        res[a + c] = check_pair(band, b, a, c)
    assert res['AB'] == (F(2788, 405), F('110.5')) and res['AC'] == (F(9977, 1150), F('311.81')) and res['BC'] == (F(2539, 225), F('125.89'))
    assert res['AB'][0] < res['AC'][0] < res['BC'][0]
say('  contact order bottom to top AB, AC, BC')

# ---------- inverse board: K-1 P7, 2-3 P5, 4-5 P5
say('Inverse board (K-1 P7, 2-3 P5, 4-5 P5)')
b = board('grades-4-5', 5); B = b['pts']['B']; P = b['pts']['P']; h = b['h']
Bp = (B[0], 2 * h - B[1])
say('  B =', B, ' P =', P, ' B\' =', Bp)
# grid search: which start points (0.05 cm grid, above the line, inside the board) have best allowed contact exactly P?
hits = []; n = 0
for i in range(0, 337):
    for j in range(1, 191):
        S = (F(i, 20), h + F(j, 20)); n += 1
        u = S[1] - h; v = B[1] - h
        t = (v * S[0] + u * B[0]) / (u + v)
        t = min(max(t, b['lo']), b['hi'])
        if t == P[0]:
            hits.append(S)
on_ray = all((S[0] - P[0]) * (Bp[1] - P[1]) == (S[1] - P[1]) * (Bp[0] - P[0]) and S[0] < P[0] for S in hits)
say(f'  {n} grid starts above the line: {len(hits)} have best contact exactly P, all on the ray from P away from B\': {on_ray}; e.g. {hits[:3]}')
for tt in [F(1, 2), F(1)]:
    S = (P[0] - F('6.3') * tt, h + F('5.6') * tt)
    t, m2 = optimum(b, S, B)
    say(f'  t = {tt}: S = ({S[0]}, {S[1]}), best contact {t}, min {float(sqrtD(m2)):.4f}')
    assert t == P[0]
xedge = F(0); tt = (P[0] - xedge) / F('6.3')
say(f'  ray leaves the 16.8 x 18.2 board frame at x = 0, y = {float(h + F("5.6")*tt):.3f}; visible length {float(tt)*float(sqrtD(F("6.3")**2 + F("5.6")**2)):.2f} cm')

# ---------- lengthtie: 2-3 P6
say('Equal-minimum board (2-3 P6)')
b = board('grades-2-3', 6)
tab, mab = check_pair('2-3 P6', b, 'A', 'B'); tac, mac = check_pair('2-3 P6', b, 'A', 'C')
assert mab == mac == 164 and tab == 8 and tac == F('6.2')

# ---------- matching: 4-5 P4
say('Shared-contact board (4-5 P4)')
b = board('grades-4-5', 4)
tab, mab = check_pair('4-5 P4', b, 'A', 'B'); tcd, mcd = check_pair('4-5 P4', b, 'C', 'D')
assert tab == tcd == F('6.2') and mab == F('260.64') and mcd == 225
# do the two optimal routes cross elsewhere or pass through the other dots?
A, B, C, D = (b['pts'][k] for k in 'ABCD')
def seg_dist(p, a, c):
    ax, ay = float(a[0]), float(a[1]); cx, cy = float(c[0]), float(c[1]); px, py = float(p[0]), float(p[1])
    dx, dy = cx - ax, cy - ay; s = max(0, min(1, ((px-ax)*dx + (py-ay)*dy) / (dx*dx + dy*dy)))
    return math.hypot(px - ax - s*dx, py - ay - s*dy)
M = (tab, b['h'])
say(f'  distance of C from leg AM {seg_dist(C, A, M):.2f} cm, of A from leg CM {seg_dist(A, C, M):.2f} cm, of D from leg MB {seg_dist(D, M, B):.2f} cm, of B from leg MD {seg_dist(B, M, D):.2f} cm')
# other same-side pairs on this board (in case a child pairs differently)
for a, c in ['AC', 'AD', 'BC', 'BD']:
    t, m2 = optimum(b, b['pts'][a], b['pts'][c]); say(f'  (other pair {a}{c}: contact {float(t):.3f})')

# ---------- restricted: 2-3 P7, 4-5 P6
say('Restricted board (2-3 P7, 4-5 P6)')
for band, pg in [('grades-2-3', 7), ('grades-4-5', 6)]:
    b = board(band, pg); t, m2 = check_pair(band, b, 'A', 'B')
    assert t == F('6.5') and m2 == 288
    Cx, Dx, Ex, Fx = (b['pts'][k][0] for k in 'CDEF')
    dec = {'CD': Cx < t < Dx, 'EF': Ex < t < Fx, 'CF': Cx < t < Fx}
    say(f'  {band}: C {Cx}, D {Dx}, E {Ex}, F {Fx}; strict membership {dec}; margins to C, D: {t - Cx}, {Dx - t}; distance to E: {Ex - t}')
    assert dec == {'CD': True, 'EF': False, 'CF': True}
    assert b['lo'] <= Cx and Fx <= b['hi']
    A, B = b['pts']['A'], b['pts']['B']
    # E-F optimum (not asked): scan
    best = min((route_len_f(b, A, B, float(Ex) + (float(Fx) - float(Ex)) * k / 20000), float(Ex) + (float(Fx) - float(Ex)) * k / 20000) for k in range(20001))
    say(f'  (not asked) best E-F contact {best[1]:.4f}, length {best[0]:.4f} vs unrestricted {float(sqrtD(m2)):.4f}')

# ---------- unique: 4-5 P7
say('Uniqueness board (4-5 P7)')
b = board('grades-4-5', 7); t, m2 = check_pair('4-5 P7', b, 'A', 'B')
assert t == F(1157, 110) and m2 == F('208.26')
A, B = b['pts']['A'], b['pts']['B']
# strict convexity check: second differences positive along a fine grid
vals = [route_len_f(b, A, B, float(b['lo']) + (float(b['hi'] - b['lo'])) * k / 4000) for k in range(4001)]
assert all(vals[k-1] + vals[k+1] - 2 * vals[k] > 0 for k in range(1, 4000))
say('  route length strictly convex along the marked segment (positive second differences at 4001 points): unique contact')

# ---------- every same-side pair on every page has its optimum inside the marks
say('All same-side pairs on all 21 pages')
cnt = 0
for band in G:
    for pg in range(1, 8):
        b = board(band, pg); names = sorted(b['pts'])  # marks on the line have height 0 and are skipped below
        for i, a in enumerate(names):
            for c in names[i+1:]:
                pa, pc = coords(b, b['pts'][a]), coords(b, b['pts'][c])
                if pa[1] * pc[1] <= 0: continue
                t, m2 = optimum(b, b['pts'][a], b['pts'][c]); cnt += 1
                assert b['lo'] < t < b['hi'], (band, pg, a, c, t)
                # reflected point inside the 16.8 x 18.2 working region
                p = b['pts'][c]; r = (p[0], 2*b['h'] - p[1]) if b['axis'] == 'h' else (2*b['h'] - p[0], p[1])
                assert 0 <= r[0] <= F('16.8') and 0 <= r[1] <= F('18.2'), (band, pg, c, r)
say(f'  {cnt} same-side pairs: every optimum strictly inside the end marks and every reflected finish on the working region')

# ---------- guide general formula
say('Guide p. 3 formula x = (va+ub)/(u+v), squared minimum (b-a)^2+(u+v)^2: used above and matched by the brute-force scans')
(HERE / 'check_base.out').write_text('\n'.join(out) + '\n')
