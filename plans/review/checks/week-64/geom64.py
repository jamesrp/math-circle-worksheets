#!/usr/bin/env python3
"""Week 64 math check: read the diagrams of the delivered student PDF back from
its drawing primitives (PyMuPDF) and check them against the mathematics.

Independent of the packet's own generate.py / verify.py.  The repository is
found four folders up from this script (plans/review/checks/week-64/).

Run:  python3 geom64.py      (writes geom64.out beside itself)

Also importable: extract() returns the data read from the PDF (octagon edge
gluings, numbered corners, sector pieces, L gluings, start dots and travel
directions), which math64.py uses for its exact dynamics.
"""
import math
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
STUDENT = REPO / 'lowell-math-circle-year-2/week-64/week-64-students.pdf'
A = 1 + math.sqrt(2)
PT = 72.0

OUT, FAIL = [], []


def say(*a):
    OUT.append(' '.join(str(x) for x in a))


def check(cond, msg):
    say(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------- primitives
def up(p, H=792.0):
    """PDF point (y down) -> (x, y) with y up."""
    return (p.x, H - p.y)


def prims(page):
    """Classify drawings: polygons, open heads (edge arrows), filled heads
    (travel arrows), dots, sectors, single lines."""
    res = dict(poly=[], ehead=[], thead=[], dot=[], sector=[], line=[])
    for d in page.get_drawings():
        it = d['items']
        w = round(d.get('width') or 0, 2)
        if all(i[0] == 'c' for i in it) and len(it) == 4:
            r = d['rect']
            res['dot'].append(dict(c=((r.x0 + r.x1) / 2, 792 - (r.y0 + r.y1) / 2),
                                   r=(r.x1 - r.x0) / 2,
                                   black=d.get('fill') == (0.0, 0.0, 0.0)))
            continue
        if not all(i[0] == 'l' for i in it):
            continue
        pts = [up(i[1]) for i in it] + [up(it[-1][2])]
        if len(it) == 4 and w in (0.65, 1.34, 1.35):
            tip = pts[0]
            back = ((pts[1][0] + pts[3][0]) / 2, (pts[1][1] + pts[3][1]) / 2)
            dvec = (tip[0] - back[0], tip[1] - back[1])
            n = math.hypot(*dvec)
            res['thead' if d['type'] == 'fs' else 'ehead'].append(
                dict(tip=tip, dir=(dvec[0] / n, dvec[1] / n)))
        elif len(it) == 50:
            res['sector'].append(pts)
        elif len(it) == 1:
            res['line'].append(dict(a=pts[0], b=pts[1], w=w))
        else:
            res['poly'].append(dict(v=pts[:-1], w=w))
    return res


def words(page):
    out = []
    for w in page.get_text('words'):
        out.append(dict(t=w[4], c=((w[0] + w[2]) / 2, 792 - (w[1] + w[3]) / 2)))
    return out


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def seg_dist(p, a, b):
    ax, ay = a
    bx, by = b
    t = ((p[0] - ax) * (bx - ax) + (p[1] - ay) * (by - ay)) / ((bx - ax) ** 2 + (by - ay) ** 2)
    t = max(0, min(1, t))
    return dist(p, (ax + t * (bx - ax), ay + t * (by - ay)))


def nearest(lbls, p, allowed):
    c = [w for w in lbls if w['t'] in allowed]
    return min(c, key=lambda w: dist(w['c'], p))


def angle_deg(v):
    return math.degrees(math.atan2(v[1], v[0]))


# ---------------------------------------------------------------- octagons
def octagon_info(poly, page_prims, lbls, letters='ABCD'):
    """Return regularity data, octagon-unit map and the edge gluing as printed."""
    v = poly['v']
    n = len(v)
    sides = [dist(v[i], v[(i + 1) % n]) for i in range(n)]
    angs = []
    for i in range(n):
        p0, p1, p2 = v[i - 1], v[i], v[(i + 1) % n]
        a1 = math.atan2(p0[1] - p1[1], p0[0] - p1[0])
        a2 = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
        angs.append(math.degrees(abs((a1 - a2 + math.pi) % (2 * math.pi) - math.pi)))
    c = (sum(p[0] for p in v) / n, sum(p[1] for p in v) / n)
    s = sides[0] / 2  # points per octagon unit (side = 2 units)
    U = lambda p: ((p[0] - c[0]) / s, (p[1] - c[1]) / s)
    # Edge arrows lying on this polygon's edges.
    edges = []
    for i in range(n):
        a, b = v[i], v[(i + 1) % n]
        hs = [h for h in page_prims['ehead'] if seg_dist(h['tip'], a, b) < 0.6]
        if not hs or any(hh['dir'][0] * hs[0]['dir'][0] + hh['dir'][1] * hs[0]['dir'][1] < 0.99 for hh in hs):
            edges.append(None)  # no arrow, or conflicting arrows on a shared edge
            continue
        h = hs[0]
        mid = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        lab = nearest(lbls, mid, letters)['t']
        # arrow points from tail vertex to head vertex
        e = (b[0] - a[0], b[1] - a[1])
        forward = h['dir'][0] * e[0] + h['dir'][1] * e[1] > 0
        tail, head = (i, (i + 1) % n) if forward else ((i + 1) % n, i)
        edges.append(dict(i=i, letter=lab, tail=tail, head=head,
                          vec=(v[head][0] - v[tail][0], v[head][1] - v[tail][1]),
                          lab_dist=dist(nearest(lbls, mid, letters)['c'], mid)))
    return dict(v=v, sides=sides, angles=angs, c=c, s=s, U=U, edges=edges,
                width=(max(p[0] for p in v) - min(p[0] for p in v)))


def check_gluing(info, name):
    E = info['edges']
    check(all(e is not None for e in E), f'{name}: every edge carries exactly one arrow')
    by = {}
    for e in E:
        by.setdefault(e['letter'], []).append(e)
    check(all(len(x) == 2 for x in by.values()), f'{name}: each letter labels exactly two edges {sorted(by)}')
    ok = True
    for L, (e1, e2) in by.items():
        if dist(e1['vec'], e2['vec']) > 0.05 * math.hypot(*e1['vec']):
            ok = False
            say('     mismatch', L, e1['vec'], e2['vec'])
    check(ok, f'{name}: each letter pair is glued by a translation (arrows agree as vectors)')
    # Opposite sides?
    n = len(info['v'])
    opp = all(((e1['i'] - e2['i']) % n) == n // 2 for e1, e2 in by.values())
    check(opp, f'{name}: paired edges are opposite sides')
    return by


def vertex_classes(n, by):
    par = list(range(n))

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for e1, e2 in by.values():
        par[f(e1['tail'])] = f(e2['tail'])
        par[f(e1['head'])] = f(e2['head'])
    cl = {}
    for i in range(n):
        cl.setdefault(f(i), []).append(i)
    return list(cl.values())


def corner_signature(info, by, vi):
    """For polygon vertex vi: (letter on the right-hand side when facing into
    the interior, arrow toward?), (left-hand letter, toward?), interior angle."""
    v = info['v']
    n = len(v)
    inc = []
    for e in info['edges']:
        if vi in (e['tail'], e['head']):
            other = e['head'] if e['tail'] == vi else e['tail']
            d = (v[other][0] - v[vi][0], v[other][1] - v[vi][1])
            inc.append((e['letter'], e['head'] == vi, d))
    (l1, t1, d1), (l2, t2, d2) = inc
    # Polygon is convex; bisector points inward.
    bis = (d1[0] / math.hypot(*d1) + d2[0] / math.hypot(*d2),
           d1[1] / math.hypot(*d1) + d2[1] / math.hypot(*d2))
    cross1 = bis[0] * d1[1] - bis[1] * d1[0]  # >0: d1 is counterclockwise (left)
    if cross1 > 0:
        left, right = (l1, t1), (l2, t2)
    else:
        left, right = (l2, t2), (l1, t1)
    return dict(right=right, left=left, angle=info['angles'][vi])


# ---------------------------------------------------------------- sectors
def sector_info(pts, page_prims, lbls, letters):
    apex = pts[0]
    e1 = pts[1]
    e2 = pts[-2]  # last arc point before closing back to apex
    r1, r2 = dist(apex, e1), dist(apex, e2)
    d1 = (e1[0] - apex[0], e1[1] - apex[1])
    d2 = (e2[0] - apex[0], e2[1] - apex[1])
    ang = math.degrees(math.acos((d1[0] * d2[0] + d1[1] * d2[1]) / (r1 * r2)))
    arcmid = pts[len(pts) // 2]
    bis = (arcmid[0] - apex[0], arcmid[1] - apex[1])
    rays = []
    for d, e in ((d1, e1), (d2, e2)):
        hs = [h for h in page_prims['ehead'] if seg_dist(h['tip'], apex, e) < 0.6]
        assert len(hs) == 1, hs
        h = hs[0]
        toward = h['dir'][0] * d[0] + h['dir'][1] * d[1] < 0
        # label: nearest allowed letter to the ray's 0.74 point
        p = (apex[0] + 0.74 * d[0], apex[1] + 0.74 * d[1])
        lab = nearest(lbls, p, letters)
        side = 'left' if bis[0] * d[1] - bis[1] * d[0] > 0 else 'right'
        rays.append(dict(side=side, letter=lab['t'], toward=toward))
    num = nearest(lbls, (apex[0] + 0.58 * bis[0] / math.hypot(*bis) * r1,
                         apex[1] + 0.58 * bis[1] / math.hypot(*bis) * r1),
                  [str(k) for k in range(1, 13)])
    sig = {r['side']: (r['letter'], r['toward']) for r in rays}
    return dict(apex=apex, radius=(r1 + r2) / 2, angle=ang, num=int(num['t']),
                right=sig['right'], left=sig['left'])


# ---------------------------------------------------------------- L shapes
def lshape_info(page_prims, lbls):
    polys = [p for p in page_prims['poly'] if len(p['v']) == 6]
    assert len(polys) == 1
    v = polys[0]['v']
    xs = sorted(set(round(p[0], 2) for p in v))
    ys = sorted(set(round(p[1], 2) for p in v))
    x0, x2 = xs[0], xs[-1]
    y0, y2 = ys[0], ys[-1]
    side_x = (x2 - x0) / 2
    side_y = (y2 - y0) / 2
    L = lambda p: ((p[0] - x0) / side_x, (p[1] - y0) / side_y)
    shape = sorted((round(L(p)[0], 4), round(L(p)[1], 4)) for p in v)
    # square names from labels A, B, C
    names = {}
    for w in lbls:
        if w['t'] in 'ABC' and len(w['t']) == 1:
            q = L(w['c'])
            if 0 <= q[0] <= 2 and 0 <= q[1] <= 2:
                names[(int(q[0]), int(q[1]))] = w['t']
    # outer boundary unit edges with arrows and letters
    bedges = []
    for h in page_prims['ehead']:
        q = L(h['tip'])
        # which unit boundary edge?
        if abs(q[1] - round(q[1])) < 0.02:  # horizontal edge
            yy = round(q[1])
            xx = math.floor(q[0])
            seg = ((xx, yy), (xx + 1, yy))
        else:
            xx = round(q[0])
            yy = math.floor(q[1])
            seg = ((xx, yy), (xx, yy + 1))
        mid = ((seg[0][0] + seg[1][0]) / 2, (seg[0][1] + seg[1][1]) / 2)
        midpt = (x0 + mid[0] * side_x, y0 + mid[1] * side_y)
        lab = nearest(lbls, midpt, 'pqrs')['t']
        bedges.append(dict(seg=seg, letter=lab, dir=(round(h['dir'][0], 3), round(h['dir'][1], 3))))
    dots = [dict(q=L(d['c']), black=d['black']) for d in page_prims['dot']
            if 0 <= L(d['c'])[0] <= 2 and 0 <= L(d['c'])[1] <= 2]
    travel = []
    for h in page_prims['thead']:
        q = L(h['tip'])
        if 0 <= q[0] <= 2.2 and 0 <= q[1] <= 2.2:
            travel.append(dict(tip=q, dir=h['dir']))
    grid = [l for l in page_prims['line'] if l['w'] in (0.25, 0.35)
            and all(-0.01 <= c <= 2.01 for c in L(l['a']) + L(l['b']))]
    return dict(shape=shape, side=(side_x, side_y), names=names, bedges=bedges,
                dots=dots, travel=travel, L=L, grid=grid)


def l_permutations(info):
    """Right/up square maps read from the L's outer letters and seams."""
    names = info['names']
    sqs = list(names)
    by = {}
    for e in info['bedges']:
        by.setdefault(e['letter'], []).append(e)
    R, U = {}, {}
    for (i, j) in sqs:
        # right neighbour
        if (i + 1, j) in names:
            R[names[(i, j)]] = names[(i + 1, j)]
        else:
            seg = ((i + 1, j), (i + 1, j + 1))
            e = [x for x in info['bedges'] if x['seg'] == seg][0]
            partner = [x for x in by[e['letter']] if x is not e][0]
            (px, py), _ = partner['seg']
            R[names[(i, j)]] = names[(px, py)]  # partner is a left side at x=px
        if (i, j + 1) in names:
            U[names[(i, j)]] = names[(i, j + 1)]
        else:
            seg = ((i, j + 1), (i + 1, j + 1))
            e = [x for x in info['bedges'] if x['seg'] == seg][0]
            partner = [x for x in by[e['letter']] if x is not e][0]
            (px, py), _ = partner['seg']
            U[names[(i, j)]] = names[(px, py)]
    return R, U, by


# ---------------------------------------------------------------- main
def extract():
    doc = pymupdf.open(str(STUDENT))
    data = dict(pages=len(doc))
    P = [prims(doc[i]) for i in range(len(doc))]
    W = [words(doc[i]) for i in range(len(doc))]
    data['prims'] = P
    data['words'] = W
    return doc, data


def main():
    doc, data = extract()
    P, W = data['prims'], data['words']
    say('Student PDF:', STUDENT.relative_to(REPO), 'pages', data['pages'])
    check(data['pages'] == 9, 'student packet has 9 pages')

    # ------------------------------------------------------------ octagons
    oct_infos = {}
    for pn in (1, 2, 3, 4):
        polys = [p for p in P[pn - 1]['poly'] if len(p['v']) == 8]
        for k, poly in enumerate(polys):
            info = octagon_info(poly, P[pn - 1], W[pn - 1])
            nm = f'p{pn} octagon {k + 1} (width {info["width"] / PT:.3f} in)'
            sd = info['sides']
            check(max(sd) - min(sd) < 0.02 and all(abs(a - 135) < 0.05 for a in info['angles']),
                  f'{nm}: regular (sides {min(sd):.2f}-{max(sd):.2f} pt, angles 135 deg)')
            # standard orientation: horizontal top/bottom sides
            U = info['U']
            uv = [U(p) for p in info['v']]
            std = [(1, A), (A, 1), (A, -1), (1, -A), (-1, -A), (-A, -1), (-A, 1), (-1, A)]
            okstd = all(min(dist(q, s) for s in std) < 0.01 for q in uv)
            check(okstd, f'{nm}: vertices are (+-1,+-a),(+-a,+-1) in side-2 units')
            by = check_gluing(info, nm)
            oct_infos[(pn, k)] = (info, by)
    # widths stated in the source README
    widths = {pn: sorted(round(i['width'] / PT, 2) for (p, k), (i, b) in oct_infos.items() if p == pn)
              for pn in (1, 2, 3, 4)}
    say('     octagon widths (in):', widths)
    check(widths[2] == [5.35] and widths[3] == [1.4, 1.4, 4.65] and widths[1] == [1.63, 1.63, 3.94],
          'octagon widths p1 3.94 (+1.63 examples), p2 5.35, p3 4.65 (+1.40 examples)')

    # same letter -> same geometric side on every octagon (consistent convention)
    def letter_sides(info):
        out = {}
        for e in info['edges']:
            U = info['U']
            a, b = U(info['v'][e['tail']]), U(info['v'][e['head']])
            out.setdefault(e['letter'], []).append(
                (round((a[0] + b[0]) / 2, 2), round((a[1] + b[1]) / 2, 2),
                 round(b[0] - a[0], 2), round(b[1] - a[1], 2)))
        return {k: sorted(v) for k, v in out.items()}
    sigs = [letter_sides(i) for (i, b) in oct_infos.values()]
    check(all(s == sigs[0] for s in sigs), 'all eight printed octagons use the same letters and arrows')
    say('     octagon convention (midpoint x, y, arrow dx, dy in side-2 units):')
    for L in sorted(sigs[0]):
        say('       ', L, sigs[0][L])

    # ------------------------------------------------------------ page 1
    big = [(i, b) for (p, k), (i, b) in oct_infos.items() if p == 1 and i['width'] > 200][0][0]
    U = big['U']
    starts = {}
    for d in P[0]['dot']:
        q = U(d['c'])
        if max(abs(q[0]), abs(q[1])) < A + 0.1 and d['black']:
            lab = nearest(W[0], d['c'], 'PQR')['t']
            starts[lab] = q
    say('     p1 start dots (octagon units):', {k: (round(v[0], 3), round(v[1], 3)) for k, v in starts.items()})
    exp = {'P': (-.65, 0), 'Q': (-.3, 1.6), 'R': (.2, -1.45)}
    check(all(dist(starts[k], exp[k]) < 0.01 for k in exp), 'p1 P, Q, R at (-.65,0), (-.3,1.6), (.2,-1.45)')
    # travel arrows from each start: heads whose tail lines start at the dot
    heads = [h for h in P[0]['thead'] if max(abs(U(h['tip'])[0]), abs(U(h['tip'])[1])) < A]
    for k, q in starts.items():
        hs = [h for h in heads if abs(U(h['tip'])[1] - q[1]) < 0.02 and U(h['tip'])[0] > q[0]]
        check(len(hs) == 1 and abs(hs[0]['dir'][1]) < 1e-3 and hs[0]['dir'][0] > 0,
              f'p1 {k}: one travel arrow, pointing straight right')
    # convention example: S, X (hollow) on the right C edge of example 1, X on left C edge of example 2
    small = sorted([i for (p, k), (i, b) in oct_infos.items() if p == 1 and i['width'] < 200], key=lambda i: i['c'][0])
    o1, o2 = small
    S = [d for d in P[0]['dot'] if d['black'] and dist(d['c'], o1['c']) < o1['width'] / 2][0]
    Xs = [d for d in P[0]['dot'] if not d['black']]
    X1 = [d for d in Xs if dist(d['c'], o1['c']) < o1['width']][0]
    X2 = [d for d in Xs if dist(d['c'], o2['c']) < o2['width']][0]
    s1, x1 = o1['U'](S['c']), o1['U'](X1['c'])
    x2 = o2['U'](X2['c'])
    say(f'     p1 example: S={tuple(round(t, 3) for t in s1)}, X(right)={tuple(round(t, 3) for t in x1)}, X(left)={tuple(round(t, 3) for t in x2)}')
    check(abs(x1[0] - A) < 0.01 and abs(x1[1]) < 1, 'p1 example: first X is on the right vertical (C) edge, away from its corners')
    check(abs(x2[0] + A) < 0.01 and abs(x2[1] - x1[1]) < 0.01, 'p1 example: second X is the translated mate on the left C edge')
    tl = [l for l in P[0]['line'] if l['w'] in (1.34, 1.35)]
    seg1 = [l for l in tl if dist(l['a'], S['c']) < 0.5][0]
    seg2 = [l for l in tl if dist(l['a'], X2['c']) < 0.5][0]
    d1 = angle_deg((X1['c'][0] - S['c'][0], X1['c'][1] - S['c'][1]))
    d2 = angle_deg((seg2['b'][0] - seg2['a'][0], seg2['b'][1] - seg2['a'][1]))
    check(abs(d1 - d2) < 0.3, f'p1 example: resumed segment parallel to arrival ({d1:.2f} vs {d2:.2f} deg)')
    e2 = o2['U'](seg2['b'])
    check(abs(e2[1] - e2[0]) < A + 1 and abs(e2[0]) < A and abs(e2[1]) < A and e2[1] - e2[0] < A + 1,
          'p1 example: resumed segment stays inside the second octagon')

    # ------------------------------------------------------------ page 3 example
    sm = sorted([i for (p, k), (i, b) in oct_infos.items() if p == 3 and i['width'] < 200], key=lambda i: i['c'][0])
    c1, c2 = sm
    check(abs((c2['c'][0] - c1['c'][0]) - 2 * A * c1['s']) < 0.05 and abs(c2['c'][1] - c1['c'][1]) < 0.05,
          'p3 example: copy 2 is copy 1 translated by one octagon width (left C on right C)')
    tl = [l for l in P[2]['line'] if l['w'] in (1.34, 1.35)]
    th = P[2]['thead']
    pts = [tl[0]['a'], tl[0]['b'], tl[1]['b'], th[0]['tip']]
    angs = [angle_deg((pts[i + 1][0] - pts[0][0], pts[i + 1][1] - pts[0][1])) for i in range(3)]
    check(max(angs) - min(angs) < 0.3, f'p3 example: the two pieces are one straight line (angles {[round(a, 2) for a in angs]})')
    j = c1['U'](tl[0]['b'])
    check(abs(j[0] - A) < 0.01 and abs(j[1]) < 1, 'p3 example: the join is on copy 1 right C edge = copy 2 left C edge')
    lbl12 = [w for w in W[2] if w['t'] in ('1', '2') and w['c'][1] > 500]
    check(len(lbl12) == 2, 'p3 example: copies numbered 1 and 2')

    # ------------------------------------------------------------ page 4
    o4, by4 = oct_infos[(4, 0)]
    nums = {}
    for vi, p in enumerate(o4['v']):
        w = nearest(W[3], p, [str(k) for k in range(1, 9)])
        nums[vi] = int(w['t'])
        check(dist(w['c'], p) < 20, f'p4 corner label {w["t"]} is next to its corner ({dist(w["c"], p):.1f} pt)')
    cls = vertex_classes(8, by4)
    cls_n = [sorted(nums[i] for i in c) for c in cls]
    say('     p4 octagon corner classes (from printed letters/arrows):', cls_n)
    check(cls_n == [[1, 2, 3, 4, 5, 6, 7, 8]], 'p4 octagon: all eight corners form one group')
    endpoint_pairs = {L: (sorted((nums[e1['tail']], nums[e2['tail']])), sorted((nums[e1['head']], nums[e2['head']])))
                      for L, (e1, e2) in by4.items()}
    say('     p4 octagon endpoint matches (tails, heads):', endpoint_pairs)
    sq = [p for p in P[3]['poly'] if len(p['v']) == 4][0]
    sqi = octagon_info(sq, P[3], W[3], letters='EF')
    sd = sqi['sides']
    check(max(sd) - min(sd) < 0.02 and all(abs(a - 90) < 0.05 for a in sqi['angles']), 'p4 square is a square')
    bysq = check_gluing(sqi, 'p4 square')
    sqnums = {}
    for vi, p in enumerate(sqi['v']):
        w = nearest(W[3], p, ['9', '10', '11', '12'])
        sqnums[vi] = int(w['t'])
    clsq = [sorted(sqnums[i] for i in c) for c in vertex_classes(4, bysq)]
    say('     p4 square corner classes:', clsq)
    check(clsq == [[9, 10, 11, 12]], 'p4 square: all four corners form one group')
    say('     p4 square endpoint matches:', {L: (sorted((sqnums[e1['tail']], sqnums[e2['tail']])),
                                               sorted((sqnums[e1['head']], sqnums[e2['head']])))
                                           for L, (e1, e2) in bysq.items()})
    corners = {}
    for vi in range(8):
        corners[nums[vi]] = corner_signature(o4, by4, vi)
    for vi in range(4):
        corners[sqnums[vi]] = corner_signature(sqi, bysq, vi)

    # ------------------------------------------------------------ page 5
    secs = [sector_info(p, P[4], W[4], 'ABCDEF') for p in P[4]['sector']]
    check(sorted(s['num'] for s in secs) == list(range(1, 13)), 'p5 has twelve sectors numbered 1-12')
    bar = [l for l in P[4]['line'] if l['w'] == 0.8 and abs(l['a'][1] - l['b'][1]) < 0.01]
    barlen = max(abs(l['a'][0] - l['b'][0]) for l in bar)
    check(abs(barlen - 72) < 0.05, f'p5 scale bar is 1 inch ({barlen:.2f} pt)')
    turns = {'oct': 0.0, 'sq': 0.0}
    for s in sorted(secs, key=lambda s: s['num']):
        c = corners[s['num']]
        good = (s['right'] == c['right'] and s['left'] == c['left'] and abs(s['angle'] - c['angle']) < 0.3)
        say(f"     piece {s['num']:2d}: angle {s['angle']:.2f} radius {s['radius'] / PT:.3f} in; "
            f"piece R/L {s['right']}/{s['left']}  corner R/L {c['right']}/{c['left']} (letter, arrow toward corner)")
        check(good, f"p5 piece {s['num']} is an orientation-preserving copy of corner {s['num']}: same angle, letters and arrow directions")
        turns['oct' if s['num'] <= 8 else 'sq'] += s['angle'] / 360
    check(abs(turns['oct'] - 3) < 0.01 and abs(turns['sq'] - 1) < 0.01,
          f"p5 sector angles total {turns['oct']:.3f} turns (octagon) and {turns['sq']:.3f} (square)")
    # cyclic ordering: each piece's right ray glues to the next piece's left ray?
    def cycle(nums_):
        # From a piece, cross its left ray: find the other piece having that ray letter+arrow on its right.
        ps = {s['num']: s for s in secs if s['num'] in nums_}
        start = min(ps)
        order = [start]
        cur = start
        for _ in range(len(ps)):
            lt = ps[cur]['left']
            nxt = [k for k, s in ps.items() if s['right'] == lt and k != cur]
            if len(nxt) != 1:
                return None
            cur = nxt[0]
            if cur == start:
                break
            order.append(cur)
        return order
    co = cycle(range(1, 9))
    cs = cycle(range(9, 13))
    say('     p5 octagon cyclic order (crossing left rays):', co, ' square:', cs)
    check(co is not None and len(co) == 8, 'p5 octagon pieces close up in a single cycle of all eight pieces')
    check(cs is not None and len(cs) == 4, 'p5 square pieces close up in a single cycle of all four pieces')

    # ------------------------------------------------------------ pages 6-9
    lres = {}
    for pn in (6, 7, 8, 9):
        info = lshape_info(P[pn - 1], W[pn - 1])
        sx, sy = info['side']
        check(abs(sx - sy) < 0.01, f'p{pn} L: equal x/y scale (side {sx / PT:.3f} in)')
        check(info['shape'] == sorted([(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)]), f'p{pn} L outline is the three-square L')
        check(info['names'] == {(0, 0): 'A', (1, 0): 'B', (0, 1): 'C'}, f'p{pn} L squares named A (lower left), B (lower right), C (upper)')
        # grid: 7 interior lines each way per square at k/8
        gl = info['grid']
        L = info['L']
        fr_ok = True
        cnt = 0
        for l in gl:
            a, b = L(l['a']), L(l['b'])
            for t in (a[0], a[1], b[0], b[1]):
                if abs(t * 8 - round(t * 8)) > 0.01:
                    fr_ok = False
            cnt += 1
        check(cnt == 42 and fr_ok, f'p{pn} L: 42 grid lines, all on eighth-grid positions')
        R, U_, by = l_permutations(info)
        lres[pn] = dict(R=R, U=U_, info=info)
        say(f'     p{pn} L gluing read from letters/arrows: right {R}, up {U_}')
        ok = all(len(v) == 2 for v in by.values()) and len(by) == 4
        # translations: paired unit edges parallel with same arrow direction
        for Lt, es in by.items():
            if es[0]['dir'] != es[1]['dir']:
                ok = False
        check(ok, f'p{pn} L: letters p,q,r,s each mark two outer edges with arrows agreeing (translations)')
        check(R == {'A': 'B', 'B': 'A', 'C': 'C'} and U_ == {'A': 'C', 'C': 'A', 'B': 'B'},
              f'p{pn} L: right crossing swaps A/B and fixes C; up crossing swaps A/C and fixes B')
        dots = []
        for d in info['dots']:
            q = d['q']
            sqn = info['names'][(int(q[0]), int(q[1]))]
            loc = (round(q[0] - int(q[0]), 4), round(q[1] - int(q[1]), 4))
            dots.append((sqn, loc))
        say(f'     p{pn} dots (square, local coords):', sorted(dots))
        lres[pn]['dots'] = sorted(dots)
        dirs = sorted(set((round(h['dir'][0], 3), round(h['dir'][1], 3)) for h in info['travel']))
        say(f'     p{pn} travel arrow unit directions:', dirs)
        lres[pn]['dirs'] = dirs
        # travel arrows start at dots and have length about one grid cell step
    check(lres[6]['dots'] == [('A', (0.5, 0.25)), ('B', (0.5, 0.25)), ('C', (0.5, 0.25))], 'p6 dots at local (1/2,1/4) in A, B, C')
    check(lres[6]['dirs'] == [(0.0, 1.0), (1.0, 0.0)], 'p6 arrows: right and straight up from every dot')
    check(len(lres[6]['info']['travel']) == 6, 'p6 has six travel arrows (two per dot)')
    check(lres[7]['dots'] == [('A', (0.5, 0.25)), ('B', (0.5, 0.25)), ('C', (0.5, 0.25))], 'p7 dots at local (1/2,1/4)')
    r2 = round(1 / math.sqrt(2), 3)
    check(lres[7]['dirs'] == [(r2, r2)], 'p7 arrows: direction (1,1)')
    check(lres[8]['dots'] == [('A', (0.25, 0.5)), ('B', (0.25, 0.5)), ('C', (0.25, 0.5))], 'p8 dots at local (1/4,1/2)')
    check(lres[8]['dirs'] == [(round(2 / math.sqrt(5), 3), round(1 / math.sqrt(5), 3))], 'p8 arrows: direction (2,1)')
    check(lres[9]['dots'] == [('A', (0.5, 0.25))], 'p9: single dot S at local (1/2,1/4) of A')
    Sdot = [d for d in P[8]['dot'] if d['c'][1] < 560][0]
    check(dist(nearest(W[8], Sdot['c'], ['S'])['c'], Sdot['c']) < 15, 'p9 dot labelled S')
    # page 9 direction diagrams: arrows and labels
    mini = []
    for d in P[8]['dot']:
        if d['c'][1] > 560:  # top of page (y up)
            h = min(P[8]['thead'], key=lambda h: dist(h['tip'], d['c']))
            v = (h['tip'][0] - d['c'][0], h['tip'][1] - d['c'][1])
            mini.append((d['c'][0], v))
    mini.sort()
    labels = []
    txt = doc[8].get_text()
    for k in ('1 right, 2 up', '2 right, 3 up', '3 right, 1 up', '3 right, 2 up'):
        labels.append(k in txt)
    check(all(labels), 'p9 labels "1 right, 2 up", "2 right, 3 up", "3 right, 1 up", "3 right, 2 up" present')
    exp_v = [(1, 2), (2, 3), (3, 1), (3, 2)]
    for (x, v), (p_, q_) in zip(mini, exp_v):
        ratio_ok = abs(v[0] * q_ - v[1] * p_) < 0.03 * math.hypot(*v)
        check(ratio_ok and v[0] > 0 and v[1] > 0, f'p9 mini arrow at x={x:.0f} has direction {p_}:{q_} (drawn {v[0]:.2f},{v[1]:.2f} pt)')
    # p9 word positions under each mini arrow
    rowy = [w for w in W[8] if w['t'] == 'right,']
    xs = sorted(w['c'][0] for w in rowy)
    check(len(xs) == 4 and all(abs(xs[i] - mini[i][0]) < 40 for i in range(4)), 'p9 each label sits under its own arrow')

    say('')
    say(f'{len(OUT) - OUT.count("") - sum(1 for o in OUT if o.startswith("     ") or o.startswith("Student"))} checks, {len(FAIL)} failures')
    return P, W, corners, secs, lres


if __name__ == '__main__':
    main()
    (HERE / 'geom64.out').write_text('\n'.join(OUT) + '\n')
    print('\n'.join(OUT))
    sys.exit(1 if FAIL else 0)
