"""Turn a one-stroke picture (straight strokes and circles, in cm) into a graph:
corners, crossings and touching points become vertices; the pieces of stroke between
them become edges.  Then count odd points and the fewest strokes."""

import math

TOL = 0.02   # cm: points closer than this are the same point


def seg_point_dist(p, s):
    (ax, ay), (bx, by) = s
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    t = max(0, min(1, ((p[0] - ax) * dx + (p[1] - ay) * dy) / L2))
    return math.hypot(p[0] - ax - t * dx, p[1] - ay - t * dy)


def seg_seg_points(s, t):
    (x1, y1), (x2, y2) = s
    (x3, y3), (x4, y4) = t
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    pts = []
    if abs(d) < 1e-12:
        # parallel: report shared endpoints only; a real overlap would be an error
        for p in (t[0], t[1]):
            if seg_point_dist(p, s) < TOL:
                pts.append(p)
        for p in (s[0], s[1]):
            if seg_point_dist(p, t) < TOL:
                pts.append(p)
        uniq = []
        for p in pts:
            if all(math.dist(p, q) > TOL for q in uniq):
                uniq.append(p)
        if len(uniq) > 1:
            raise ValueError('overlapping collinear strokes')
        return uniq
    a = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    b = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / d
    Ls = math.dist(s[0], s[1]); Lt = math.dist(t[0], t[1])
    if -TOL / Ls <= a <= 1 + TOL / Ls and -TOL / Lt <= b <= 1 + TOL / Lt:
        pts.append((x1 + a * (x2 - x1), y1 + a * (y2 - y1)))
    return pts


def seg_circle_points(s, c):
    (cx, cy), r = c
    (x1, y1), (x2, y2) = s
    dx, dy = x2 - x1, y2 - y1
    fx, fy = x1 - cx, y1 - cy
    A = dx * dx + dy * dy
    B = 2 * (fx * dx + fy * dy)
    C = fx * fx + fy * fy - r * r
    disc = B * B - 4 * A * C
    out = []
    if disc < -1e-9:
        return out
    disc = max(disc, 0)
    for sgn in (-1, 1):
        t = (-B + sgn * math.sqrt(disc)) / (2 * A)
        if -1e-6 <= t <= 1 + 1e-6:
            p = (x1 + t * dx, y1 + t * dy)
            if all(math.dist(p, q) > TOL for q in out):
                out.append(p)
    return out


def circle_circle_points(c1, c2):
    (x1, y1), r1 = c1
    (x2, y2), r2 = c2
    d = math.hypot(x2 - x1, y2 - y1)
    if d > r1 + r2 + TOL or d < abs(r1 - r2) - TOL or d < 1e-9:
        return []
    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h = math.sqrt(max(r1 * r1 - a * a, 0))
    mx, my = x1 + a * (x2 - x1) / d, y1 + a * (y2 - y1) / d
    if h < TOL:
        return [(mx, my)]
    return [(mx + h * (y2 - y1) / d, my - h * (x2 - x1) / d), (mx - h * (y2 - y1) / d, my + h * (x2 - x1) / d)]


def meet_points(e, f):
    (k1, a), (k2, b) = e, f
    if k1 == 's' and k2 == 's':
        return seg_seg_points(a, b)
    if k1 == 's' and k2 == 'c':
        return seg_circle_points(a, b)
    if k1 == 'c' and k2 == 's':
        return seg_circle_points(b, a)
    return circle_circle_points(a, b)


def elements_touch(e, f):
    return bool(meet_points(e, f))


def gap(e, f):
    """Distance between two strokes that do not meet (centre lines, cm)."""
    (k1, a), (k2, b) = e, f
    if k1 == 's' and k2 == 's':
        return min(seg_point_dist(a[0], b), seg_point_dist(a[1], b), seg_point_dist(b[0], a), seg_point_dist(b[1], a))
    if k1 == 'c' and k2 == 'c':
        (c1, r1), (c2, r2) = a, b
        d = math.dist(c1, c2)
        return d - r1 - r2 if d > r1 + r2 else abs(r1 - r2) - d
    s, c = (a, b) if k1 == 's' else (b, a)
    (cc, r) = c
    dmin = seg_point_dist(cc, s)
    dmax = max(math.dist(cc, s[0]), math.dist(cc, s[1]))
    if dmin > r:
        return dmin - r
    return r - dmax


def analyse(pic):
    """Return dict with vertex degrees, number of odd points, components, fewest strokes, closest near miss."""
    els = [('s', s) for s in pic.segs] + [('c', c) for c in pic.circles]
    special = []

    def add(p):
        for q in special:
            if math.dist(p, q) < TOL:
                return q
        special.append(p)
        return p

    for k, e in els:
        if k == 's':
            add(e[0]); add(e[1])
    near = None
    for i in range(len(els)):
        for j in range(i + 1, len(els)):
            pts = meet_points(els[i], els[j])
            for p in pts:
                add(p)
            if not pts:
                g = gap(els[i], els[j])
                near = g if near is None else min(near, g)
    # pieces
    edges = []
    loops = 0
    for k, e in els:
        if k == 's':
            a, b = e
            L = math.dist(a, b)
            on = [p for p in special if seg_point_dist(p, e) < TOL]
            on.sort(key=lambda p: ((p[0] - a[0]) * (b[0] - a[0]) + (p[1] - a[1]) * (b[1] - a[1])) / L)
            for i in range(len(on) - 1):
                edges.append((on[i], on[i + 1]))
        else:
            (cx, cy), r = e
            on = [p for p in special if abs(math.dist(p, (cx, cy)) - r) < TOL]
            if not on:
                loops += 1
                continue
            on.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
            for i in range(len(on)):
                edges.append((on[i], on[(i + 1) % len(on)]))
    deg = {}
    for a, b in edges:
        deg[a] = deg.get(a, 0) + 1
        deg[b] = deg.get(b, 0) + 1
    # components among vertices
    par = {v: v for v in deg}
    def f(x):
        while par[x] != x:
            x = par[x]
        return x
    for a, b in edges:
        par[f(a)] = f(b)
    comps = {}
    for v in deg:
        comps.setdefault(f(v), []).append(v)
    strokes = loops
    for vs in comps.values():
        odd = sum(1 for v in vs if deg[v] % 2)
        strokes += max(1, odd // 2)
    odd_pts = [v for v in deg if deg[v] % 2]
    return {'deg': deg, 'odd': len(odd_pts), 'odd_pts': odd_pts, 'components': len(comps) + loops,
            'strokes': strokes, 'near_miss_cm': near, 'n_vertices': len(deg), 'n_pieces': len(edges)}
