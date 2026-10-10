#!/usr/bin/env python3
"""Week 64 math check: exact dynamics for every student problem and every
numerical / combinatorial claim in the adult guide.

Independent of the packet's generate.py and verify.py.  Gluings, start dots and
directions are read from the delivered student PDF by geom64.py (same folder);
the dynamics here use exact arithmetic: Q(sqrt 2) for the octagon, Fractions for
the L.  The guide is read from the delivered facilitator PDF with pdftotext.

Run:  python3 math64.py      (writes math64.out beside itself)
"""
import io
import math
import subprocess
import sys
from contextlib import redirect_stdout
from fractions import Fraction as F
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
import geom64  # noqa: E402

GUIDE = REPO / 'lowell-math-circle-year-2/week-64/week-64-facilitator.pdf'
OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


# ------------------------------------------------------------ Q(sqrt 2)
class Q2:
    """p + q*sqrt(2) with Fraction p, q."""
    __slots__ = ('p', 'q')

    def __init__(self, p=0, q=0):
        self.p, self.q = F(p), F(q)

    @staticmethod
    def c(x):
        return x if isinstance(x, Q2) else Q2(x)

    def __add__(s, o):
        o = Q2.c(o); return Q2(s.p + o.p, s.q + o.q)
    __radd__ = __add__

    def __neg__(s):
        return Q2(-s.p, -s.q)

    def __sub__(s, o):
        return s + (-Q2.c(o))

    def __rsub__(s, o):
        return Q2.c(o) - s

    def __mul__(s, o):
        o = Q2.c(o); return Q2(s.p * o.p + 2 * s.q * o.q, s.p * o.q + s.q * o.p)
    __rmul__ = __mul__

    def inv(s):
        n = s.p * s.p - 2 * s.q * s.q
        return Q2(s.p / n, -s.q / n)

    def __truediv__(s, o):
        return s * Q2.c(o).inv()

    def sign(s):
        p, q = s.p, s.q
        if q == 0:
            return (p > 0) - (p < 0)
        if p == 0:
            return (q > 0) - (q < 0)
        if p > 0 and q > 0:
            return 1
        if p < 0 and q < 0:
            return -1
        # opposite signs: compare p^2 with 2 q^2
        d = p * p - 2 * q * q
        return (1 if p > 0 else -1) if d > 0 else (1 if q > 0 else -1)

    def __eq__(s, o):
        return (s - Q2.c(o)).sign() == 0

    def __lt__(s, o):
        return (s - Q2.c(o)).sign() < 0

    def __le__(s, o):
        return (s - Q2.c(o)).sign() <= 0

    def __gt__(s, o):
        return (s - Q2.c(o)).sign() > 0

    def __ge__(s, o):
        return (s - Q2.c(o)).sign() >= 0

    def __abs__(s):
        return -s if s.sign() < 0 else s

    def __hash__(s):
        return hash((s.p, s.q))

    def f(s):
        return float(s.p) + float(s.q) * math.sqrt(2)

    def __repr__(s):
        if s.q == 0:
            return str(s.p)
        return f'{s.p}{"+" if s.q >= 0 else "-"}{abs(s.q)}r2'


a = Q2(1, 1)          # 1 + sqrt2
b = Q2(2, 1)          # 2 + sqrt2
V = [(Q2(1), a), (a, Q2(1)), (a, Q2(-1)), (Q2(1), -a), (Q2(-1), -a), (-a, Q2(-1)), (-a, Q2(1)), (Q2(-1), a)]


def octagon_edges_from_pdf(data):
    """Edges of the p2 octagon as printed: letter -> [(tail, head), (tail, head)]
    with vertex indices 0..7 of V (V[i] is printed corner i+1)."""
    P, W = data['prims'], data['words']
    poly = [p for p in P[1]['poly'] if len(p['v']) == 8][0]
    info = geom64.octagon_info(poly, P[1], W[1])
    U = info['U']
    idx = {}
    for i, p in enumerate(info['v']):
        u = U(p)
        idx[i] = min(range(8), key=lambda j: (V[j][0].f() - u[0]) ** 2 + (V[j][1].f() - u[1]) ** 2)
    edges = {}
    for e in info['edges']:
        edges.setdefault(e['letter'], []).append((idx[e['tail']], idx[e['head']]))
    return edges


def oct_flow_right(edges, x0, y0, start_on_edge=False, maxsteps=20):
    """Exact rightward flow on the glued octagon.  Returns (status, total,
    pieces, crossings)."""
    seg = []
    for L, pair in edges.items():
        for k, (t, h) in enumerate(pair):
            other = pair[1 - k]
            trans = (V[other[0]][0] - V[t][0], V[other[0]][1] - V[t][1])
            seg.append((L, V[t], V[h], trans))
    x, y = x0, y0
    total = Q2(0)
    pieces, cross = [], []
    first = True
    for _ in range(maxsteps):
        # vertex on this horizontal line, to the right?
        hits = []
        for L, p, q, tr in seg:
            lo, hi = (p[1], q[1]) if p[1] <= q[1] else (q[1], p[1])
            if p[1] == q[1]:
                continue  # horizontal edge: only on the boundary line y = +-a
            if lo < y < hi:
                xi = p[0] + (y - p[1]) * (q[0] - p[0]) / (q[1] - p[1])
                if xi > x:
                    hits.append((xi, L, tr))
        verts = [v for v in V if v[1] == y and v[0] > x]
        if not hits and not verts:
            return ('stuck', total, pieces, cross)
        xh = min(h[0] for h in hits) if hits else None
        xv = min(v[0] for v in verts) if verts else None
        if xv is not None and (xh is None or xv <= xh):
            # corner reached first (unless the start lies before it)
            if not first and y == y0 and x <= x0 < xv:
                pieces.append(x0 - x); total = total + (x0 - x)
                return ('closed', total, pieces, cross)
            return ('corner', total + (xv - x), pieces + [xv - x], cross)
        # closed before the exit?
        if not first and y == y0 and x <= x0 < xh:
            pieces.append(x0 - x); total = total + (x0 - x)
            return ('closed', total, pieces, cross)
        if not first and start_on_edge and y == y0 and x0 == xh:
            pieces.append(x0 - x); total = total + (x0 - x)
            return ('closed', total, pieces, cross)
        hit = min(hits, key=lambda h: h[0])
        xi, L, tr = hit
        pieces.append(xi - x)
        total = total + (xi - x)
        cross.append(L)
        x, y = xi + tr[0], y + tr[1]
        first = False
        if start_on_edge and x == x0 and y == y0:
            return ('closed', total, pieces, cross)
    return ('unfinished', total, pieces, cross)


def inside(x, y):
    return abs(x) < a and abs(y) < a and (abs(x) + abs(y)) < b


# ------------------------------------------------------------ L surface
def l_flow(R, U, sq, x, y, p, q, dots=(), maxt=10):
    """Exact flow on the 3-square surface.  Local coordinates in [0,1).
    Returns (status, time, events, dot visits, event times)."""
    s0, x0, y0 = sq, F(x), F(y)
    x, y = F(x), F(y)
    t = F(0)
    ev, evt, visits = [], [], [sq]
    while t <= maxt:
        tx = (1 - x) / p if p > 0 else None
        ty = (1 - y) / q if q > 0 else None
        tn = min(v for v in (tx, ty) if v is not None)
        # dots on the open segment (t, t+tn]
        hits = []
        for (ds, dx, dy) in dots:
            if ds != sq:
                continue
            # solve x + p s = dx, y + q s = dy for 0 < s <= tn
            cand = None
            if p > 0:
                cand = (F(dx) - x) / p
            elif q > 0:
                cand = (F(dy) - y) / q
            if cand is not None and 0 < cand < tn and x + p * cand == dx and y + q * cand == dy:
                hits.append((cand, ds))
        for cand, ds in sorted(hits):
            visits.append(ds)
        # return to start strictly inside this piece?
        if t > 0 or True:
            if sq == s0:
                if p > 0:
                    sret = (x0 - x) / p
                else:
                    sret = (y0 - y) / q
                if 0 < sret < tn and x + p * sret == x0 and y + q * sret == y0 and t + sret > 0:
                    return ('closed', t + sret, ''.join(ev), visits, evt)
        if tx is not None and ty is not None and tx == ty:
            return ('corner', t + tn, ''.join(ev), visits, evt)
        t += tn
        x, y = x + p * tn, y + q * tn
        if tx is not None and tx == tn:
            sq = R[sq]; x = F(0); ev.append('r'); evt.append((t, 'r', sq))
        else:
            sq = U[sq]; y = F(0); ev.append('u'); evt.append((t, 'u', sq))
    return ('unfinished', t, ''.join(ev), visits, evt)


def main():
    buf = io.StringIO()
    with redirect_stdout(buf):
        doc, data = geom64.extract()
    edges = octagon_edges_from_pdf(data)
    say('Octagon gluing read from student p. 2 (vertex index i = printed corner i+1):', edges)

    # ------------------------------------------------ octagon basics
    sides = [(V[i][0] - V[(i + 1) % 8][0]) * (V[i][0] - V[(i + 1) % 8][0]) +
             (V[i][1] - V[(i + 1) % 8][1]) * (V[i][1] - V[(i + 1) % 8][1]) for i in range(8)]
    check(all(s == 4 for s in sides), 'octagon (+-1,+-a),(+-a,+-1): every squared side is exactly 4 (side 2)')
    # guide: side v_i -> v_{i+1} matches opposite side by v_i<->v_{i+5}, v_{i+1}<->v_{i+4}
    ok = True
    for L, ((t1, h1), (t2, h2)) in edges.items():
        for (t, h), (tt, hh) in (((t1, h1), (t2, h2)), ((t2, h2), (t1, h1))):
            i = min(t, h) if abs(t - h) == 1 else max(t, h)  # side from v_i to v_{i+1}
            j = (i + 1) % 8
            m = {i: (i + 5) % 8, j: (i + 4) % 8}
            if not (m[t] == tt and m[h] == hh):
                ok = False
    check(ok, 'guide p. 8: side v_i v_{i+1} matches the opposite side by v_i<->v_{i+5}, v_{i+1}<->v_{i+4}')
    # guide translation table
    def trans(L):
        (t1, h1), (t2, h2) = edges[L]
        return (V[t2][0] - V[t1][0], V[t2][1] - V[t1][1])
    # which letter is which side
    side_of = {}
    for L, ((t1, h1), _) in edges.items():
        mx = (V[t1][0] + V[h1][0]) / 2
        my = (V[t1][1] + V[h1][1]) / 2
        side_of[L] = (mx.f(), my.f())
    say('     first-listed edge midpoint per letter:', {k: (round(v[0], 3), round(v[1], 3)) for k, v in side_of.items()})
    y = Q2(F(3, 2))
    # Right -> left (-2a,0); NE -> SW (-b,-b); SE -> NW (-b,b); top -> bottom (0,-2a)
    tC = trans('C'); tB = trans('B'); tD = trans('D'); tA = trans('A')
    tabs = {}
    for L, t in (('A', tA), ('B', tB), ('C', tC), ('D', tD)):
        tabs[L] = (t, (-t[0], -t[1]))
    def has(L, vec):
        return any(tt[0] == vec[0] and tt[1] == vec[1] for tt in tabs[L])
    check(has('C', (-2 * a, Q2(0))) and has('B', (-b, -b)) and has('D', (-b, b)) and has('A', (Q2(0), -2 * a)),
          'guide p. 8 table: right->left (-2a,0), NE->SW (-b,-b), SE->NW (-b,b), top->bottom (0,-2a) are the printed gluings')
    yv = Q2(F(3, 2))
    check((b - yv) + (yv) == b and (-yv) + (yv - b) == -b, 'guide p. 8: (b-y,y) on x+y=b maps to (-y,y-b) on x+y=-b')
    check((yv - (yv - b)) == b and ((yv - b) - yv) == -b, 'guide p. 8: (y,y-b) on x-y=b maps to (y-b,y) on x-y=-b')

    # vertex classes and cone angle
    par = list(range(8))
    def fnd(x):
        while par[x] != x:
            x = par[x]
        return x
    for L, ((t1, h1), (t2, h2)) in edges.items():
        par[fnd(t1)] = fnd(t2); par[fnd(h1)] = fnd(h2)
    ncls = len(set(fnd(i) for i in range(8)))
    check(ncls == 1, 'all eight octagon corners are one point')
    check(8 * 135 == 1080 and 1080 / 360 == 3, 'cone angle 8 x 135 = 1080 deg = 3 full turns')
    chi = 1 - 4 + 1
    check(chi == -2 and (2 - chi) // 2 == 2, 'octagon: V-E+F = 1-4+1 = -2, genus 2')
    # guide chain v0~v5~v2~v7~v4~v1~v6~v3~v0 (0-based) -- every step a single endpoint match
    pairs = set()
    for L, ((t1, h1), (t2, h2)) in edges.items():
        pairs |= {frozenset((t1, t2)), frozenset((h1, h2))}
    chain = [0, 5, 2, 7, 4, 1, 6, 3, 0]
    check(all(frozenset((chain[i], chain[i + 1])) in pairs for i in range(8)),
          'guide p. 9 chain v0~v5~v2~v7~v4~v1~v6~v3~v0: each step is an endpoint match')
    tour = [1, 6, 3, 8, 5, 2, 7, 4, 1]
    check(all(frozenset((tour[i] - 1, tour[i + 1] - 1)) in pairs for i in range(8)),
          'guide p. 5 tour 1->6->3->8->5->2->7->4->1: each step is an endpoint match')
    pl = {L: (sorted((t1 + 1, t2 + 1)), sorted((h1 + 1, h2 + 1))) for L, ((t1, h1), (t2, h2)) in edges.items()}
    check(pl == {'A': ([5, 8], [1, 4]), 'B': ([1, 6], [2, 5]), 'C': ([3, 6], [2, 7]), 'D': ([4, 7], [3, 8])},
          'guide p. 5 endpoint table A 8~5,1~4; B 1~6,2~5; C 3~6,2~7; D 4~7,3~8')

    # ------------------------------------------------ P1
    starts = {'P': (Q2(F(-13, 20)), Q2(0)), 'Q': (Q2(F(-3, 10)), Q2(F(8, 5))), 'R': (Q2(F(1, 5)), Q2(F(-29, 20)))}
    res1 = {}
    for k, (x0, y0) in starts.items():
        st, tot, pcs, cr = oct_flow_right(edges, x0, y0)
        res1[k] = (st, tot, cr)
        say(f'     P1 {k}: {st}, length {tot} = {tot.f():.4f}, crossings {cr}, pieces {[round(p.f(), 3) for p in pcs]}')
    check(res1['P'][0] == 'closed' and res1['P'][1] == 2 * a and res1['P'][2] == ['C'], 'P1 P closes, length 2a = 2+2r2, crossing C')
    check(res1['Q'][0] == 'closed' and res1['Q'][1] == 2 * b and res1['Q'][2] == ['B', 'D'], 'P1 Q closes, length 2b = 4+2r2, crossings B, D')
    check(res1['R'][0] == 'closed' and res1['R'][1] == 2 * b and res1['R'][2] == ['D', 'B'], 'P1 R closes, length 2b, crossings D, B')
    check(Q2(F(8, 5)) - b < -1 and b - Q2(F(29, 20)) > 1 and Q2(F(8, 5)) - b != Q2(F(-29, 20)),
          'P1 Q and R are distinct loops of the outer family (guide heights 1.60-b and b-1.45)')

    # ------------------------------------------------ P2: classify interior starts
    lengths = {}
    corner_heights = set()
    bad = []
    for ky in range(-120, 121):
        yy = Q2(F(ky, 50))
        for kx in range(-120, 121, 7):
            xx = Q2(F(kx, 50))
            if not inside(xx, yy):
                continue
            st, tot, pcs, cr = oct_flow_right(edges, xx, yy)
            if st == 'closed':
                lengths.setdefault(tot, set()).add(ky)
            elif st == 'corner':
                corner_heights.add(ky)
            else:
                bad.append((kx, ky, st))
    say('     P2 sampled lengths:', {str(k): (min(v) / 50, max(v) / 50, len(v)) for k, v in lengths.items()},
        ' corner heights:', sorted(h / 50 for h in corner_heights))
    check(not bad, 'P2: every sampled interior start closes or hits a corner')
    check(set(lengths) == {2 * a, 2 * b}, 'P2: exactly two closed-trip lengths, 2a and 2b')
    check(all(abs(k) < 50 for k in lengths[2 * a]) and all(abs(k) > 50 for k in lengths[2 * b]),
          'P2: |y|<1 gives 2a; 1<|y|<a gives 2b')
    check(corner_heights == {-50, 50}, 'P2: only the heights y = +-1 hit a corner')
    # irrational heights too: y = 1 + r2/3, y = r2/5
    for yy in (Q2(1, F(1, 3)), Q2(0, F(1, 5)), Q2(-1, F(-7, 10))):
        st, tot, _, _ = oct_flow_right(edges, Q2(0), yy)
        check(st == 'closed' and tot == (2 * a if abs(yy.f()) < 1 else 2 * b), f'P2 irrational height {yy}: length {tot}')
    s2 = 5.35 / (2 * a.f())
    check(abs(2 * a.f() * s2 - 5.35) < 1e-9 and abs(2 * b.f() * s2 - 7.566) < 1e-3 and abs(b.f() / a.f() - math.sqrt(2)) < 1e-12,
          f'P2 printed lengths 5.35 in and {2 * b.f() * s2:.3f} in = 5.35 r2 (guide p. 3)')
    check(2 * b - 2 * a == 2, 'guide: outer minus middle length = 2 = one side')

    # ------------------------------------------------ P3
    # equal stretches: 2(b-y) = 2y
    yb = b / 2
    check(2 * (b - yb) == 2 * yb and yb > 1 and yb < a, 'P3: equal chords exactly at y = b/2 (inside the outer band)')
    mid_nw = ((V[6][0] + V[7][0]) / 2, (V[6][1] + V[7][1]) / 2)
    check(mid_nw[1] == yb and mid_nw[0] == -b / 2, 'P3: y = b/2 meets the NW (D) edge at its midpoint (-b/2, b/2)')
    st, tot, pcs, cr = oct_flow_right(edges, mid_nw[0], mid_nw[1], start_on_edge=True)
    say(f'     P3 from NW midpoint: {st}, pieces {pcs}, crossings {cr}')
    check(st == 'closed' and len(pcs) == 2 and pcs[0] == b and pcs[1] == b, 'P3: from the D midpoint the trip closes with two chords of length b each')
    # uniqueness: other heights give unequal chords
    unequal = all(oct_flow_right(edges, (Q2(F(k, 40)) - b), Q2(F(k, 40)), start_on_edge=True)[2][0] !=
                  oct_flow_right(edges, (Q2(F(k, 40)) - b), Q2(F(k, 40)), start_on_edge=True)[2][1]
                  for k in range(41, 96) if Q2(F(k, 40)) != yb)
    check(unequal, 'P3: every other D-edge start height gives two unequal chords')
    # development: copy 2 = copy 1 + (b,b); copy 3 = copy 1 + (2b, 0)
    def shifted(dx, dy):
        return [(v[0] + dx, v[1] + dy) for v in V]
    C1, C2, C3 = shifted(Q2(0), Q2(0)), shifted(b, b), shifted(2 * b, Q2(0))
    ne = {(C1[0][0], C1[0][1]), (C1[1][0], C1[1][1])}
    sw2 = {(C2[4][0], C2[4][1]), (C2[5][0], C2[5][1])}
    check(ne == sw2, 'P3 development: copy 2 at (b,b) puts its SW B edge exactly on copy 1 NE B edge')
    se2 = {(C2[2][0], C2[2][1]), (C2[3][0], C2[3][1])}
    nw3 = {(C3[6][0], C3[6][1]), (C3[7][0], C3[7][1])}
    check(se2 == nw3, 'P3 optional: copy 3 at (2b,0) puts its NW D edge on copy 2 SE D edge')

    def disjoint_interiors(P1, P2):
        for poly in (P1, P2):
            n = len(poly)
            for i in range(n):
                ex = poly[(i + 1) % n][0].f() - poly[i][0].f()
                ey = poly[(i + 1) % n][1].f() - poly[i][1].f()
                nx, ny = -ey, ex
                pr1 = [v[0].f() * nx + v[1].f() * ny for v in P1]
                pr2 = [v[0].f() * nx + v[1].f() * ny for v in P2]
                if max(pr1) <= min(pr2) + 1e-9 or max(pr2) <= min(pr1) + 1e-9:
                    return True
        return False
    check(disjoint_interiors(C1, C2) and disjoint_interiors(C2, C3) and disjoint_interiors(C1, C3),
          'P3 development copies 1, 2, 3 do not overlap')
    endpt = (Q2(3) * b / 2, b / 2)
    check(endpt[0] - b == b / 2 and endpt[1] - b == -b / 2 and (b / 2) - (-b / 2) == b,
          'P3 line (-b/2,b/2)->(3b/2,b/2) ends at copy 2 SE D midpoint (b/2,-b/2) after length 2b')
    s3 = 4.65 / (2 * a.f())
    w3 = (2 * b.f() + 2 * a.f()) * s3
    h3 = (b.f() + 2 * a.f()) * s3
    check(11 < w3 < 12 and 7.5 < h3 < 8.1, f'guide p. 2: three-copy p. 3 layout {w3:.2f} x {h3:.2f} in ("about 12 by 8")')
    check(abs(2 * b.f() * s3 - 6.576) < 1e-3, f'P3 full trip at p. 3 size {2 * b.f() * s3:.3f} in')

    # ------------------------------------------------ P4/P5 (geometry from geom64)
    with redirect_stdout(buf):
        geom64.OUT.clear(); geom64.FAIL.clear()
        Pp, Ww, corners, secs, lres = geom64.main()
    check(not geom64.FAIL, f'geom64 diagram checks pass ({len(geom64.FAIL)} failures)')
    # guide p. 5 sector order and seams
    sec = {s['num']: s for s in secs}
    order = [1, 6, 3, 8, 5, 2, 7, 4]
    seams = []
    ok = True
    for i in range(8):
        x, y_ = sec[order[i]], sec[order[(i + 1) % 8]]
        common = {x['left'][0], x['right'][0]} & {y_['left'][0], y_['right'][0]}
        # the shared ray must be on opposite sides with the same arrow sense
        found = None
        for side in ('left', 'right'):
            other = 'right' if side == 'left' else 'left'
            if x[side] == y_[other]:
                found = x[side][0]
        if found is None:
            ok = False
        seams.append(found)
    say('     P5 seams along 1,6,3,8,5,2,7,4:', seams)
    check(ok and seams == ['B', 'C', 'D', 'A', 'B', 'C', 'D', 'A'], 'guide p. 5: order 1,6,3,8,5,2,7,4 joins rays B,C,D,A,B,C,D,A with matching arrows, no flips')
    sorder = [9, 10, 11, 12]
    sseams = []
    for i in range(4):
        x, y_ = sec[sorder[i]], sec[sorder[(i + 1) % 4]]
        f_ = None
        for side in ('left', 'right'):
            other = 'right' if side == 'left' else 'left'
            if x[side] == y_[other]:
                f_ = x[side][0]
        sseams.append(f_)
    check(sseams == ['E', 'F', 'E', 'F'], f'guide p. 5: square order 9,10,11,12 joins rays {sseams}')

    # ------------------------------------------------ L surface
    R, U = lres[6]['R'], lres[6]['U']
    dots_p6 = [(s, F(1, 2), F(1, 4)) for s in 'ABC']
    res6 = {}
    for s in 'ABC':
        for nm, (p, q) in (('right', (1, 0)), ('up', (0, 1))):
            st, t, ev, vis, _ = l_flow(R, U, s, F(1, 2), F(1, 4), p, q, dots_p6)
            res6[(s, nm)] = (st, t)
            say(f'     P6 {s} {nm}: {st} length {t}, events {ev}, dots {vis}')
    check(res6 == {('A', 'right'): ('closed', 2), ('A', 'up'): ('closed', 2), ('B', 'right'): ('closed', 2),
                   ('B', 'up'): ('closed', 1), ('C', 'right'): ('closed', 1), ('C', 'up'): ('closed', 2)},
          'P6: length 2 for A-right, B-right, A-up, C-up; length 1 for B-up, C-right (guide table)')

    res7 = {}
    for s in 'ABC':
        st, t, ev, vis, evt = l_flow(R, U, s, F(1, 2), F(1, 4), 1, 1, dots_p6)
        res7[s] = (st, t, vis)
        say(f'     P7 {s}: {st} block-time {t}, events {ev}, dot order {vis}')
        if s == 'A':
            say('       events (time, edge, square after):', [(str(tt), e, sq) for tt, e, sq in evt])
            check([(str(tt), e, sq) for tt, e, sq in evt] ==
                  [('1/2', 'r', 'B'), ('3/4', 'u', 'B'), ('3/2', 'r', 'A'), ('7/4', 'u', 'C'), ('5/2', 'r', 'C'), ('11/4', 'u', 'A')],
                  'guide p. 10 table for one-right/one-up from A: times 1/2..11/4 and squares B,B,A,C,C,A')
    check(res7 == {'A': ('closed', 3, ['A', 'B', 'C', 'A']), 'B': ('closed', 3, ['B', 'C', 'A', 'B']),
                   'C': ('closed', 3, ['C', 'A', 'B', 'C'])},
          'P7: every trip closes after 3 blocks (length 3r2) visiting A->B->C->A cyclically')
    st, t, *_ = l_flow(R, U, 'A', F(1, 2), F(1, 2), 1, 1)
    check(st == 'corner' and t == F(1, 2), 'guide: from the square centre, direction (1,1) hits a corner')

    dots_p8 = [(s, F(1, 4), F(1, 2)) for s in 'ABC']
    res8 = {}
    for s in 'ABC':
        st, t, ev, vis, evt = l_flow(R, U, s, F(1, 4), F(1, 2), 2, 1, dots_p8)
        res8[s] = (st, t, vis, ev)
        say(f'     P8 {s}: {st} block-time {t}, events {ev}, dot order {vis}, first-block times {[str(e[0]) for e in evt[:3]]}')
    check(res8['A'][:3] == ('closed', 1, ['A', 'A']) and res8['B'][:3] == ('closed', 2, ['B', 'C', 'B'])
          and res8['C'][:3] == ('closed', 2, ['C', 'B', 'C']),
          'P8: A alone is shortest (1 block, r5); B and C take 2 blocks, exactly twice as long')
    check(res8['A'][3] == 'rur' and res8['B'][3] == 'rurrur', 'guide pp. 7, 10: block = right, up, right at 3/8, 1/2, 7/8')

    res9 = {}
    for (p, q) in ((1, 2), (2, 3), (3, 1), (3, 2)):
        st, t, ev, vis, evt = l_flow(R, U, 'A', F(1, 2), F(1, 4), p, q)
        # block-end labels
        labels = ['A']
        sq = 'A'
        for k in range(1, int(t) + 1 if st == 'closed' else 0):
            last = [e for e in evt if e[0] <= k]
            labels.append(last[-1][2] if last else 'A')
        first_block = ''.join(e[1] for e in evt if e[0] < 1)
        res9[(p, q)] = (st, t)
        length = f'{t} x sqrt({p * p + q * q})'
        say(f'     P9 ({p},{q}): {st} at block-time {t} (length {length}), first-block events {first_block}, block-end labels {labels}')
    check(res9 == {(1, 2): ('closed', 1), (2, 3): ('corner', F(1, 4)), (3, 1): ('closed', 3), (3, 2): ('closed', 2)},
          'P9: (1,2) closes after 1 block, (2,3) hits a corner at 1/4, (3,1) closes after 3, (3,2) after 2 (guide table)')

    # universal claim: every rational direction from every sampled start closes within 3 blocks or hits a corner,
    # and first returns only at whole blocks
    bad = []
    nst = 0
    for p, q in product(range(0, 9), range(0, 9)):
        if (p, q) == (0, 0) or math.gcd(p, q) != 1:
            continue
        for s in 'ABC':
            for kx in range(1, 16, 2):
                for ky in range(1, 16, 3):
                    x0, y0 = F(kx, 16) + F(1, 97), F(ky, 16)
                    st, t, *_ = l_flow(R, U, s, x0, y0, p, q, maxt=4)
                    nst += 1
                    if st == 'closed':
                        if t.denominator != 1 or t > 3:
                            bad.append((p, q, s, x0, y0, t))
                    elif st != 'corner':
                        bad.append((p, q, s, x0, y0, st))
    check(not bad, f'P9 universal answer: {nst} (direction, start) pairs all close within <=3 whole blocks or hit a corner')

    # L corner sectors: one class of 12
    sect = [(s, c) for s in 'ABC' for c in ('BL', 'BR', 'TR', 'TL')]
    par = {x: x for x in sect}
    def fd(x):
        while par[x] != x:
            x = par[x]
        return x
    rel = set()
    for s in 'ABC':
        for u_, v_ in (((s, 'TR'), (R[s], 'TL')), ((s, 'BR'), (R[s], 'BL')), ((s, 'TR'), (U[s], 'BR')), ((s, 'TL'), (U[s], 'BL'))):
            par[fd(u_)] = fd(v_)
            rel.add(frozenset((u_, v_)))
    check(len(set(fd(x) for x in sect)) == 1, 'L: all 12 square-corner sectors form one point, 12 x 90 = 1080 deg')
    ch = ['A_BL', 'B_BR', 'B_TR', 'A_TL', 'C_BL', 'C_BR', 'A_TR', 'B_TL', 'B_BL', 'A_BR', 'C_TR', 'C_TL', 'A_BL']
    ch = [tuple(c.split('_')) for c in ch]
    check(all(frozenset((ch[i], ch[i + 1])) in rel for i in range(12)), 'guide p. 10 L corner chain: every step is a single edge match')
    check(1 - 6 + 3 == -2, 'L: V-E+F = 1-6+3 = -2, genus 2')

    # ------------------------------------------------ guide p. 4 figure (optional three-copy development)
    import pymupdf
    gp = pymupdf.open(str(GUIDE))[3]
    octs, dots, path = [], [], None
    for d in gp.get_drawings():
        it = d['items']
        if len(it) == 8 and all(i[0] == 'l' for i in it):
            pts = [(i[1].x, -i[1].y) for i in it]
            octs.append(pts)
        elif len(it) == 4 and all(i[0] == 'c' for i in it):
            r = d['rect']; dots.append(((r.x0 + r.x1) / 2, -(r.y0 + r.y1) / 2))
        elif len(it) == 1 and round(d.get('width') or 0, 2) == 1.39:
            path = ((it[0][1].x, -it[0][1].y), (it[0][2].x, -it[0][2].y))
    cen = sorted([(sum(p[0] for p in o) / 8, sum(p[1] for p in o) / 8) for o in octs])
    side = math.hypot(octs[0][0][0] - octs[0][1][0], octs[0][0][1] - octs[0][1][1])
    u = side / 2
    rel = [((c[0] - cen[0][0]) / u, (c[1] - cen[0][1]) / u) for c in cen]
    say('     guide p. 4 figure copy centres (side-2 units, copy 1 at 0):', [(round(x, 3), round(y, 3)) for x, y in rel])
    bf, af = b.f(), a.f()
    check(abs(rel[1][0] - bf) < .01 and abs(rel[1][1] - bf) < .01 and abs(rel[2][0] - 2 * bf) < .01 and abs(rel[2][1]) < .01,
          'guide p. 4 figure: copies at (0,0), (b,b), (2b,0)')
    dx = sorted(round((p[0] - cen[0][0]) / u, 3) for p in dots)
    dy = set(round((p[1] - cen[0][1]) / u, 3) for p in dots)
    check(dy == {round(bf / 2, 3)} and all(abs(x - y) < .01 for x, y in zip(dx, [0, bf / 2, 3 * bf / 2, 2 * bf])),
          f'guide p. 4 figure: path at y=b/2 with marks at x = 0, b/2 (B), 3b/2 (D), 2b (return S): {dx}')
    check(path is not None and abs((path[0][1] - cen[0][1]) / u - bf / 2) < .01 and abs(path[0][1] - path[1][1]) < .01,
          'guide p. 4 figure: the drawn path is horizontal at height b/2')

    # ------------------------------------------------ guide text: printed values present
    txt = subprocess.run(['pdftotext', '-layout', str(GUIDE), '-'], capture_output=True, text=True).stdout
    flat = ' '.join(txt.split())
    for frag in ['4+2', '1080', '5.35', '7.57', '1, 6, 3, 8, 5, 2, 7, 4', '9, 10, 11, 12', 'three full turns',
                 'about 12 by 8 inches', 'twice as long']:
        check(frag.replace(' ', '') in flat.replace(' ', ''), f'guide PDF text contains "{frag}"')
    check(abs(2 + 2 * math.sqrt(2) - 4.828) < 1e-3 and abs(4 + 2 * math.sqrt(2) - 6.828) < 1e-3, 'guide p. 8: 4.828 and 6.828')

    say('')
    n = sum(1 for o in OUT if o.startswith('ok') or o.startswith('FAIL'))
    say(f'{n} checks, {len(FAIL)} failures')


if __name__ == '__main__':
    main()
    (HERE / 'math64.out').write_text('\n'.join(OUT) + '\n')
    print('\n'.join(OUT))
    sys.exit(1 if FAIL else 0)
