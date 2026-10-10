"""Week 10 one-stroke pictures (K-1 P5, 2-3 P7, 4-5 P7): read every stroke from the PDFs, build the
drawing's graph (corners, line ends, crossings and touch points as vertices), and decide by search
whether one stroke can draw it, and how many strokes are needed.
Run: python3 check_pictures.py > check_pictures.out
"""
import os
import sys
import math
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfread as R
from graphs import Town

FAILS = []
TOL = 0.6


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + str(detail) if detail != '' else ''))
    if not ok:
        FAILS.append(name)


def strokes(key, pg):
    p, objs, words = R.page_objects(key, pg)
    segs, circles = [], []
    for o in objs:
        if abs((o.get('linewidth') or 0) - 1.4) > 0.1 or o.get('fill'):
            continue
        if str(o.get('stroking_color')) not in ('0.5', '(0.5,)', '[0.5]'):
            continue
        c = R.circle_of(o) if o['object_type'] == 'curve' else None
        if c:
            circles.append(c)
            continue
        path = o['path']
        assert not any(cmd[0] == 'c' for cmd in path)
        pts = [cmd[-1] for cmd in path if cmd[0] in ('m', 'l')]
        for k in range(len(pts) - 1):
            segs.append((pts[k], pts[k + 1]))
        if path[-1][0] == 'h':
            segs.append((pts[-1], pts[0]))
    return segs, circles


def seg_seg(s, t):
    (x1, y1), (x2, y2) = s
    (x3, y3), (x4, y4) = t
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(d) < 1e-9:
        return []
    a = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    b = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / d
    L1 = math.hypot(x2 - x1, y2 - y1)
    L2 = math.hypot(x4 - x3, y4 - y3)
    if -TOL / L1 <= a <= 1 + TOL / L1 and -TOL / L2 <= b <= 1 + TOL / L2:
        return [(x1 + a * (x2 - x1), y1 + a * (y2 - y1))]
    return []


def seg_circ(s, c):
    (x1, y1), (x2, y2) = s
    cx, cy, r = c
    dx, dy = x2 - x1, y2 - y1
    A = dx * dx + dy * dy
    B = 2 * (dx * (x1 - cx) + dy * (y1 - cy))
    C = (x1 - cx) ** 2 + (y1 - cy) ** 2 - r * r
    disc = B * B - 4 * A * C
    out = []
    if disc < 0:
        return out
    L = math.sqrt(A)
    for sgn in (-1, 1):
        t = (-B + sgn * math.sqrt(disc)) / (2 * A)
        if -TOL / L <= t <= 1 + TOL / L:
            out.append((x1 + t * dx, y1 + t * dy))
    return out


def circ_circ(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    d = math.hypot(x2 - x1, y2 - y1)
    if d > r1 + r2 + TOL or d < abs(r1 - r2) - TOL or d < 1e-9:
        return []
    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h = math.sqrt(max(r1 * r1 - a * a, 0))
    xm, ym = x1 + a * (x2 - x1) / d, y1 + a * (y2 - y1) / d
    return [(xm + h * (y2 - y1) / d, ym - h * (x2 - x1) / d), (xm - h * (y2 - y1) / d, ym + h * (x2 - x1) / d)]


def build(segs, circles):
    """Graph of one picture: vertices are points (merged within TOL), edges are stroke pieces."""
    pts = []

    def vid(p):
        for i, q in enumerate(pts):
            if math.hypot(p[0] - q[0], p[1] - q[1]) < TOL:
                return i
        pts.append(p)
        return len(pts) - 1
    on_seg = {i: set() for i in range(len(segs))}
    on_circ = {i: set() for i in range(len(circles))}
    for i, s in enumerate(segs):
        on_seg[i] |= {vid(s[0]), vid(s[1])}
    for i, j in itertools.combinations(range(len(segs)), 2):
        for p in seg_seg(segs[i], segs[j]):
            v = vid(p)
            on_seg[i].add(v)
            on_seg[j].add(v)
    for i, s in enumerate(segs):
        for j, c in enumerate(circles):
            for p in seg_circ(s, c):
                v = vid(p)
                on_seg[i].add(v)
                on_circ[j].add(v)
    for i, j in itertools.combinations(range(len(circles)), 2):
        for p in circ_circ(circles[i], circles[j]):
            v = vid(p)
            on_circ[i].add(v)
            on_circ[j].add(v)
    # any vertex lying on a segment's interior is a split point of that segment
    for i, s in enumerate(segs):
        (x1, y1), (x2, y2) = s
        L = math.hypot(x2 - x1, y2 - y1)
        for v, (px, py) in enumerate(pts):
            cr = abs((x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)) / L
            t = ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / (L * L)
            if cr < TOL and -1e-6 <= t <= 1 + 1e-6:
                on_seg[i].add(v)
    edges = []
    for i, s in enumerate(segs):
        vs = sorted(on_seg[i], key=lambda v: math.hypot(pts[v][0] - s[0][0], pts[v][1] - s[0][1]))
        for a, b in zip(vs, vs[1:]):
            edges.append((a, b))
    for j, (cx, cy, r) in enumerate(circles):
        vs = sorted(on_circ[j], key=lambda v: math.atan2(pts[v][1] - cy, pts[v][0] - cx))
        if not vs:
            v = vid((cx + r, cy))
            edges.append((v, v))
        elif len(vs) == 1:
            edges.append((vs[0], vs[0]))
        else:
            for a, b in zip(vs, vs[1:] + vs[:1]):
                edges.append((a, b))
    # collapse duplicated straight pieces (a segment drawn twice would be one line on paper)
    seen = set()
    uniq = []
    for k, (a, b) in enumerate(edges):
        uniq.append((a, b))
    return pts, uniq


def near_misses(segs, circles):
    """Stroke ends that come within 0.6-4 pt of another stroke without meeting it."""
    out = []
    ends = [p for s in segs for p in s]
    for p in ends:
        for s in segs:
            if p in s:
                continue
            (x1, y1), (x2, y2) = s
            L = math.hypot(x2 - x1, y2 - y1)
            t = max(0, min(1, ((p[0] - x1) * (x2 - x1) + (p[1] - y1) * (y2 - y1)) / (L * L)))
            d = math.hypot(x1 + t * (x2 - x1) - p[0], y1 + t * (y2 - y1) - p[1])
            if TOL <= d < 4:
                out.append((round(p[0], 1), round(p[1], 1), round(d, 2)))
        for (cx, cy, r) in circles:
            d = abs(math.hypot(p[0] - cx, p[1] - cy) - r)
            if TOL <= d < 4:
                out.append((round(p[0], 1), round(p[1], 1), round(d, 2)))
    return out


def clusters(segs, circles):
    items = [('s', s) for s in segs] + [('c', c) for c in circles]

    def bbox(it):
        if it[0] == 's':
            (x1, y1), (x2, y2) = it[1]
            return min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        x, y, r = it[1]
        return x - r, y - r, x + r, y + r
    parent = list(range(len(items)))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i, j in itertools.combinations(range(len(items)), 2):
        a, b = bbox(items[i]), bbox(items[j])
        if a[0] <= b[2] + 2 and b[0] <= a[2] + 2 and a[1] <= b[3] + 2 and b[1] <= a[3] + 2:
            parent[find(i)] = find(j)
    groups = {}
    for i in range(len(items)):
        groups.setdefault(find(i), []).append(items[i])
    out = []
    for g in groups.values():
        bb = [bbox(it) for it in g]
        box = (min(b[0] for b in bb), min(b[1] for b in bb), max(b[2] for b in bb), max(b[3] for b in bb))
        out.append((box, [it[1] for it in g if it[0] == 's'], [it[1] for it in g if it[0] == 'c']))
    out.sort(key=lambda g: (round(g[0][1] / 40), g[0][0]))
    return out


def min_strokes(pts, edges):
    """Lower bound from odd points; upper bound from an explicit decomposition found by search."""
    t = Town(list(range(len(pts))), edges)
    deg = t.degrees()
    odd = [v for v in t.V if deg[v] % 2]
    one = t.has_walk()
    k = max(1, len(odd) // 2)
    # explicit decomposition: join odd points in pairs by k-1 virtual edges, walk, cut at virtual edges
    virt = [(odd[2 * i + 1], odd[2 * i + 2]) for i in range(k - 1)] if odd else []
    aug = Town(t.V, edges + virt)
    se = aug.start_end()
    assert se, 'augmented drawing has no walk'
    s = next(iter(se))
    # recover one walk as an edge sequence
    full = aug.full
    seq = []

    def rec(v, mask):
        if mask == full:
            return True
        for i, w in aug.inc[v]:
            if not mask >> i & 1 and aug.ends_from(w, mask | 1 << i):
                seq.append(i)
                return rec(w, mask | 1 << i)
        return False
    rec(s, 0)
    pieces = [[]]
    for i in seq:
        if i >= len(edges):
            pieces.append([])
        else:
            pieces[-1].append(i)
    pieces = [p for p in pieces if p]
    covered = sorted(i for p in pieces for i in p) == list(range(len(edges)))
    return one, len(odd), len(pieces), covered, t.connected()


CASES = {
    ('k1', 7): ['house', 'house', 'square-diamond', 'square-diamond', 'envelope', 'envelope'],
    ('k1', 8): ['circle-diameter', 'circle-diameter', 'wheel', 'wheel', 'triforce', 'triforce'],
    ('g23', 8): ['house', 'house', 'window', 'window'],
    ('g23', 9): ['star', 'star', 'envelope', 'envelope', 'rings', 'rings', 'square-diamond', 'square-diamond'],
    ('g45', 7): ['house', 'house', 'window', 'window', 'cube', 'cube', 'grid', 'grid'],
    ('g45', 8): ['rings', 'rings', 'star', 'star'],
}
# what the guide says: (one stroke possible, fewest strokes)
GUIDE = {'house': (True, 1), 'square-diamond': (True, 1), 'envelope': (False, 2), 'circle-diameter': (True, 1),
         'wheel': (False, 2), 'triforce': (True, 1), 'window': (False, 2), 'star': (True, 1), 'rings': (True, 1),
         'cube': (False, 4), 'grid': (False, 4)}
# expected odd-point counts from the guide's explanations
GUIDE_ODD = {'house': 2, 'envelope': 4, 'wheel': 4, 'window': 4, 'cube': 8, 'grid': 8, 'rings': 0, 'star': 0,
             'square-diamond': 0, 'triforce': 0, 'circle-diameter': 2}

shapes = {}
for (key, pg), names in CASES.items():
    segs, circles = strokes(key, pg)
    cl = clusters(segs, circles)
    check(f'{key} p{pg}: {len(names)} pictures found', len(cl) == len(names), len(cl))
    nm = near_misses(segs, circles)
    check(f'{key} p{pg}: no stroke end stops just short of, or just past, another stroke', not nm, nm[:6])
    for (box, s, c), name in zip(cl, names):
        pts, edges = build(s, c)
        one, nodd, k, covered, conn = min_strokes(pts, edges)
        degs = sorted(Town(list(range(len(pts))), edges).degrees().values())
        w, h = box[2] - box[0], box[3] - box[1]
        print(f'  {key} p{pg} {name}: box {w:.0f}x{h:.0f} pt, {len(pts)} points, {len(edges)} pieces, degrees {degs}, '
              f'odd {nodd}, one stroke {one}, strokes found {k}')
        check(f'{key} p{pg} {name}: connected, odd points = {GUIDE_ODD[name]}', conn and nodd == GUIDE_ODD[name])
        check(f'{key} p{pg} {name}: one stroke possible = {GUIDE[name][0]}, fewest strokes = {GUIDE[name][1]} '
              f'(lower bound odd/2, decomposition found)', one == GUIDE[name][0] and k == GUIDE[name][1] and covered
              and k == max(1, nodd // 2))
        # shape signature, to compare the two copies and the same picture across bands
        sig = (len(pts), len(edges), tuple(degs))
        shapes.setdefault(name, set()).add(sig)
for name, sigs in shapes.items():
    check(f'every copy of {name} in every band has the same graph', len(sigs) == 1, sigs)

# regular figures: the star-in-pentagon and the triforce picture must have equal x/y scaling
for key, pg, idx in [('g23', 9, 0), ('g45', 8, 2), ('k1', 8, 4)]:
    segs, circles = strokes(key, pg)
    box, s, c = clusters(segs, circles)[idx]
    P = sorted({(round(x, 2), round(y, 2)) for seg in s for (x, y) in seg})
    cx = sum(p[0] for p in P) / len(P)
    if key == 'k1':
        corners = [p for p in P if all(math.hypot(p[0] - q[0], p[1] - q[1]) > 1 for q in [])]
        # triforce: the three outer corners
        far = sorted(P, key=lambda p: -math.hypot(p[0] - cx, p[1] - sum(q[1] for q in P) / len(P)))[:3]
        d = [math.hypot(a[0] - b[0], a[1] - b[1]) for a, b in itertools.combinations(far, 2)]
        check(f'{key} p{pg} triforce: outer triangle equilateral', max(d) - min(d) < 0.5, [round(x, 2) for x in d])
    else:
        cy = sum(p[1] for p in P) / len(P)
        rr = [math.hypot(p[0] - cx, p[1] - cy) for p in P]
        sides = sorted(math.hypot(a[0] - b[0], a[1] - b[1]) for a, b in itertools.combinations(P, 2))
        check(f'{key} p{pg} star in pentagon: 5 vertices on one circle, sides equal', len(P) == 5 and max(rr) - min(rr) < 0.5
              and sides[4] - sides[0] < 0.5 and sides[9] - sides[5] < 0.5, [round(x, 2) for x in sides])

print()
print('FAILURES:', FAILS if FAILS else 'none')
