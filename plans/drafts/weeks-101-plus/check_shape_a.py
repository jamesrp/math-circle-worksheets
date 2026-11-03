#!/usr/bin/env python3
"""Checks for the draft plans of weeks 120-124 (shape group A).

Standard library only. Run: python3 plans/drafts/weeks-101-plus/check_shape_a.py
Each check_week_1NN() asserts the small numbers its draft quotes.
"""

import itertools
import math
from collections import deque


# ---------------------------------------------------------------------------
# Week 120: deltahedra
# ---------------------------------------------------------------------------

def _rotation(tris, v):
    """Cyclic neighbour order at v from oriented triangles."""
    nxt = {}
    for t in tris:
        for i in range(3):
            if t[i] == v:
                nxt[t[(i + 1) % 3]] = t[(i + 2) % 3]
    return nxt


def _canon(tris, nverts):
    rots = [_rotation(tris, v) for v in range(nverts)]
    best = None
    for orient in (0, 1):
        if orient:
            rr = []
            for nxt in rots:
                rr.append({b: a for a, b in nxt.items()})
        else:
            rr = rots
        for a in range(nverts):
            for b in rr[a]:
                label = {a: 0}
                start = {a: b}
                order = [a]
                q = deque([a])
                code = []
                while q:
                    v = q.popleft()
                    s = start[v]
                    w = s
                    row = []
                    while True:
                        if w not in label:
                            label[w] = len(label)
                            start[w] = v
                            order.append(w)
                            q.append(w)
                        row.append(label[w])
                        w = rr[v][w]
                        if w == s:
                            break
                    code.append(tuple(row))
                code = tuple(code)
                if best is None or code < best:
                    best = code
    return best


def deltahedral_triangulations(max_verts=12, max_deg=5):
    """All triangulations of the sphere with every vertex degree <= max_deg."""
    found = {}

    def link_closed(tris_at_v_arcs):
        # arcs: dict p->q ; closed if one cycle containing all arcs
        if not tris_at_v_arcs:
            return False
        p0 = next(iter(tris_at_v_arcs))
        p = p0
        steps = 0
        while p in tris_at_v_arcs:
            p = tris_at_v_arcs[p]
            steps += 1
            if p == p0:
                return steps == len(tris_at_v_arcs)
            if steps > len(tris_at_v_arcs):
                return False
        return False

    def has_cycle_not_all(arcs):
        # True if arcs contain a cycle but not every arc is on it (pinch)
        seen = set()
        for p0 in arcs:
            if p0 in seen:
                continue
            p = p0
            path = []
            while p in arcs and p not in path:
                path.append(p)
                p = arcs[p]
            seen.update(path)
            if p == p0 and len(path) < len(arcs):
                return True
        return False

    def search(tris, used, arcs, nverts):
        open_edges = [(a, b) for (a, b) in used if (b, a) not in used]
        if not open_edges:
            if all(link_closed(arcs[v]) for v in range(nverts)):
                E = len(used) // 2
                if nverts - E + len(tris) != 2:
                    found.setdefault('not sphere', 0)
                    found['not sphere'] += 1
                    return
                key = _canon(tris, nverts)
                found.setdefault(nverts, {})[key] = sorted(len(arcs[v]) for v in range(nverts))
            return
        # most constrained open edge
        a, b = max(open_edges, key=lambda e: (len(arcs[e[0]]) + len(arcs[e[1]]), -e[0], -e[1]))
        cands = list(range(nverts))
        if nverts < max_verts:
            cands.append(nverts)
        tri_sets = {frozenset(t) for t in tris}
        for x in cands:
            if x in (a, b):
                continue
            t = (b, a, x)
            new_edges = [(b, a), (a, x), (x, b)]
            if any(e in used for e in new_edges):
                continue
            if frozenset(t) in tri_sets:
                continue
            nv = nverts + (1 if x == nverts else 0)
            arcs2 = [dict(d) for d in arcs] + ([{}] if x == nverts else [])
            ok = True
            for i in range(3):
                v, p, q = t[i], t[(i + 1) % 3], t[(i + 2) % 3]
                if len(arcs2[v]) >= max_deg or link_closed(arcs2[v]):
                    ok = False
                    break
                arcs2[v][p] = q
                if has_cycle_not_all(arcs2[v]):
                    ok = False
                    break
            if not ok:
                continue
            search(tris + [t], used | set(new_edges), arcs2, nv)

    t0 = (0, 1, 2)
    arcs0 = [{1: 2}, {2: 0}, {0: 1}]
    search([t0], {(0, 1), (1, 2), (2, 0)}, arcs0, 3)
    return found


def check_week_120():
    # Euler: 3F = 2E, V - E + F = 2, so F = 2V - 4 is even and E = 3V - 6.
    for V in range(4, 13):
        F, E = 2 * V - 4, 3 * V - 6
        assert 3 * F == 2 * E and V - E + F == 2 and F % 2 == 0
    # Angle gap at a corner of k equilateral triangles: 360 - 60k > 0 needs k <= 5.
    assert [k for k in range(3, 7) if 360 - 60 * k > 0] == [3, 4, 5]
    # Sum over vertices of (6 - degree) = 12, i.e. total gap 720 degrees.
    known = {  # Kaufman's table: faces -> sorted degrees
        4: [3] * 4, 6: [3, 3, 4, 4, 4], 8: [4] * 6, 10: [4] * 5 + [5] * 2,
        12: [4] * 4 + [5] * 4, 14: [4] * 3 + [5] * 6, 16: [4] * 2 + [5] * 8, 20: [5] * 12,
    }
    for F, degs in known.items():
        V = (F + 4) // 2
        assert len(degs) == V and sum(degs) == 3 * F and sum(6 - d for d in degs) == 12
        assert sum(60 * (6 - d) for d in degs) == 720
    # 11 vertices (18 faces): 3a + 2b + c = 12 and a + b + c = 11 force one degree-4 corner.
    sols = [(a, b, 11 - a - b) for a in range(12) for b in range(12 - a)
            if 3 * a + 2 * b + (11 - a - b) == 12]
    assert sols == [(0, 1, 10)]
    # Combinatorial search: sphere triangulations with all degrees <= 5.
    found = deltahedral_triangulations()
    assert 'not sphere' not in found     # degree <= 5 forces a sphere (sum of 6 - d = 6 * chi > 0)
    counts = {n: len(found.get(n, {})) for n in range(4, 13)}
    assert counts[11] == 0, counts            # no 18-face pattern even on paper
    for F, degs in known.items():          # every convex deltahedron's pattern occurs
        assert degs in found[(F + 4) // 2].values()
    # Combinatorics alone allows extra patterns (e.g. octahedron with two opposite caps,
    # degrees 3,3,5,5,5,5,5,5), which equilateral faces make flat or dented.
    assert [3, 3, 5, 5, 5, 5, 5, 5] in found[8].values()
    assert counts == {4: 1, 5: 1, 6: 2, 7: 2, 8: 2, 9: 1, 10: 1, 11: 0, 12: 1}, counts
    assert sum(counts.values()) == 11   # 11 patterns on paper, 8 convex deltahedra
    check_week_120.counts = counts


# ---------------------------------------------------------------------------
# Week 121: cube nets
# ---------------------------------------------------------------------------

def _normalize(cells):
    mx = min(x for x, y in cells)
    my = min(y for x, y in cells)
    return tuple(sorted((x - mx, y - my) for x, y in cells))


def _free_key(cells):
    forms = []
    for sx, sy, swap in itertools.product((1, -1), (1, -1), (False, True)):
        t = [((y if swap else x) * sx, (x if swap else y) * sy) for x, y in cells]
        forms.append(_normalize(t))
    return min(forms)


def polyominoes(n):
    shapes = {((0, 0),)}
    for _ in range(n - 1):
        new = set()
        for s in shapes:
            ss = set(s)
            for x, y in s:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    c = (x + dx, y + dy)
                    if c not in ss:
                        new.add(_normalize(ss | {c}))
        shapes = new
    return shapes


def folds_to_cube(cells):
    """Roll a cube over the cells; a net covers six different faces."""
    cells = set(cells)
    start = next(iter(cells))
    # cube state: (bottom, top, north, south, east, west)
    state = {start: ('D', 'U', 'N', 'S', 'E', 'W')}
    q = deque([start])
    while q:
        c = q.popleft()
        d, u, n, s, e, w = state[c]
        moves = {
            (1, 0): (e, w, n, s, u, d),
            (-1, 0): (w, e, n, s, d, u),
            (0, 1): (n, s, u, d, e, w),
            (0, -1): (s, n, d, u, e, w),
        }
        for (dx, dy), ns in moves.items():
            c2 = (c[0] + dx, c[1] + dy)
            if c2 in cells and c2 not in state:
                state[c2] = ns
                q.append(c2)
    bottoms = [st[0] for st in state.values()]
    return len(set(bottoms)) == 6


def check_week_121():
    fixed = polyominoes(6)
    assert len(fixed) == 216
    free = {_free_key(s) for s in fixed}
    assert len(free) == 35
    nets = [s for s in free if folds_to_cube(s)]
    assert len(nets) == 11
    # Edge unfoldings: the cut edges form a spanning tree of the cube's 8 corners and 12 edges.
    verts = range(8)
    edges = [(a, a ^ (1 << i)) for a in verts for i in range(3) if a < a ^ (1 << i)]
    assert len(edges) == 12

    def is_tree(es):
        parent = list(range(8))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for a, b in es:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[ra] = rb
        return True
    trees = [es for es in itertools.combinations(edges, 7) if is_tree(es)]
    assert len(trees) == 384                 # 7 cuts, 5 hinges kept
    syms = []
    for perm in itertools.permutations(range(3)):
        for flip in range(8):
            def f(v, perm=perm, flip=flip):
                bits = [(v >> i) & 1 for i in range(3)]
                w = sum(bits[perm[i]] << i for i in range(3))
                return w ^ flip
            syms.append(f)
    assert len(syms) == 48

    def key(es):
        best = None
        for f in syms:
            img = tuple(sorted(tuple(sorted((f(a), f(b)))) for a, b in es))
            if best is None or img < best:
                best = img
        return best
    assert len({key(t) for t in trees}) == 11  # the same 11 nets, counted as cut trees
    # Each net: 6 squares, 5 hinges, 14 outer sides (6*4 - 2*5).
    assert 6 * 4 - 2 * 5 == 14


# ---------------------------------------------------------------------------
# Week 122: convex tangrams
# ---------------------------------------------------------------------------

DIRS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


def _poly_from_sides(sides):
    pts = [(0, 0)]
    x = y = 0
    for k, a in enumerate(sides):
        if a:
            x += a * DIRS[k][0]
            y += a * DIRS[k][1]
            pts.append((x, y))
    assert (x, y) == (0, 0)
    return pts[:-1]


def _area2(pts):
    return abs(sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1]
                   for i in range(len(pts))))


def convex_lattice_shapes(area2=16, bound=10):
    """Convex polygons, sides in the 8 compass directions on the unit grid, area area2/2."""
    shapes = set()
    rng = range(bound + 1)
    for a1, a2, a3, a5, a7 in itertools.product(rng, repeat=5):
        a6 = a1 + a2 + a3 - a5 - a7
        if not 0 <= a6 <= bound:
            continue
        c = -a1 + a3 + a5 - a7          # a0 - a4
        for a4 in rng:
            a0 = a4 + c
            if not 0 <= a0 <= bound:
                continue
            sides = (a0, a1, a2, a3, a4, a5, a6, a7)
            if sum(1 for s in sides if s) < 3:
                continue
            pts = _poly_from_sides(sides)
            if _area2(pts) != area2:
                continue
            # up to rotation by 90 degrees (shift by 2) and reflection (direction k -> -k)
            forms = []
            for r in range(0, 8, 2):
                rot = sides[r:] + sides[:r]
                forms.append(rot)
                forms.append(tuple(rot[(-k) % 8] for k in range(8)))
            shapes.add(min(forms))
    return shapes


QUARTER_OFF = {'N': (0.5, 5 / 6), 'S': (0.5, 1 / 6), 'E': (5 / 6, 0.5), 'W': (1 / 6, 0.5)}


def _inside_convex(pt, poly):
    x, y = pt
    n = len(poly)
    sgn = 0
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        cr = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
        if abs(cr) < 1e-12:
            return False
        s = 1 if cr > 0 else -1
        if sgn == 0:
            sgn = s
        elif s != sgn:
            return False
    return True


def _quarters(poly):
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    out = set()
    for i in range(min(xs), max(xs)):
        for j in range(min(ys), max(ys)):
            for q, (ox, oy) in QUARTER_OFF.items():
                if _inside_convex((i + ox, j + oy), poly):
                    out.add((i, j, q))
    return frozenset(out)


TANS = {
    'small': ([(0, 0), (1, 0), (0, 1)], 2),
    'medium': ([(0, 0), (2, 0), (1, 1)], 1),
    'large': ([(0, 0), (2, 0), (0, 2)], 2),
    'square': ([(0, 0), (1, 0), (1, 1), (0, 1)], 1),
    'para': ([(0, 0), (1, 0), (2, 1), (1, 1)], 1),
}


def _placements(piece, target):
    xs = [q[0] for q in target]
    ys = [q[1] for q in target]
    res = set()
    for a, b, c, d in [(1, 0, 0, 1), (0, -1, 1, 0), (-1, 0, 0, -1), (0, 1, -1, 0),
                       (1, 0, 0, -1), (-1, 0, 0, 1), (0, 1, 1, 0), (0, -1, -1, 0)]:
        img = [(a * x + b * y, c * x + d * y) for x, y in piece]
        # keep counterclockwise order for the convexity test
        if _area_signed(img) < 0:
            img = img[::-1]
        for tx in range(min(xs) - 3, max(xs) + 3):
            for ty in range(min(ys) - 3, max(ys) + 3):
                p = [(x + tx, y + ty) for x, y in img]
                qs = _quarters(p)
                if qs and qs <= target:
                    res.add(qs)
    return res


def _area_signed(p):
    return sum(p[i][0] * p[(i + 1) % len(p)][1] - p[(i + 1) % len(p)][0] * p[i][1] for i in range(len(p)))


def tangram_tiles(poly):
    target = _quarters(poly)
    assert len(target) == 32
    order = ['large', 'large', 'medium', 'square', 'para', 'small', 'small']
    places = {k: list(_placements(v[0], target)) for k, v in TANS.items()}

    def rec(i, covered, last_idx):
        if i == len(order):
            return covered == target
        k = order[i]
        start = last_idx if i > 0 and order[i - 1] == k else 0
        for idx in range(start, len(places[k])):
            p = places[k][idx]
            if covered & p:
                continue
            if rec(i + 1, covered | p, idx + 1):
                return True
        return False
    return rec(0, frozenset(), 0)


def check_week_122():
    shapes = convex_lattice_shapes()
    assert len(shapes) == 20, len(shapes)
    assert max(max(s) for s in shapes) == 9   # longest side 9 (a 9-7 trapezoid), inside the bound
    assert (0, 0, 1, 7, 1, 0, 0, 9) in shapes or any(sorted(s) == [0, 0, 0, 0, 1, 1, 7, 9] for s in shapes)
    tileable = [s for s in shapes if tangram_tiles(_poly_from_sides(s))]
    assert len(tileable) == 13
    sides_count = sorted(sum(1 for a in s if a) for s in tileable)
    # one triangle, six quadrilaterals, two pentagons, four hexagons (Wang-Hsiung)
    assert sides_count == [3] + [4] * 6 + [5] * 2 + [6] * 4
    # the seven tans are 16 half-squares: 4+4+2+2+2+1+1
    assert 4 + 4 + 2 + 2 + 2 + 1 + 1 == 16
    check_week_122.untileable = sorted(sum(1 for a in s if a) for s in shapes if s not in tileable)


# ---------------------------------------------------------------------------
# Week 123: art gallery guards
# ---------------------------------------------------------------------------

def _cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def _point_in_poly(p, poly):
    x, y = p
    inside = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xi > x:
                inside = not inside
    return inside


def _segments_cross(p, q, a, b):
    d1, d2 = _cross(p, q, a), _cross(p, q, b)
    d3, d4 = _cross(a, b, p), _cross(a, b, q)
    return (d1 * d2 < 0) and (d3 * d4 < 0)


def _sees(p, q, poly):
    n = len(poly)
    for i in range(n):
        a, b = poly[i], poly[(i + 1) % n]
        if _segments_cross(p, q, a, b):
            return False
        # passing exactly through a boundary vertex: test both sides via midpoints
    for t in (0.25, 0.5, 0.75):
        m = (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))
        if not _point_in_poly(m, poly):
            return False
    return True


def comb(k, H=10.0):
    """Triangular-tooth comb with k teeth and 3k + 2 corners."""
    pts = [(0.0, 0.0), (3 * k - 1.0, 0.0)]
    for j in range(k - 1, -1, -1):
        pts += [(3 * j + 2.0, 1.0), (3 * j + 1.0, H), (3 * j + 0.0, 1.1)]
    # left feet sit a little higher so no three corners are collinear
    return pts


def rect_comb(k, H=10.0):
    """Orthogonal comb with k rectangular teeth and 4k corners."""
    L = 3 * k - 2
    pts = [(0.0, 0.0), (float(L), 0.0)]
    for j in range(k - 1, -1, -1):
        x0, x1 = 3 * j, 3 * j + 1
        if j == k - 1:
            pts += [(x1, H), (x0, H), (x0, 1.0)]
        elif j == 0:
            pts += [(x1, 1.0), (x1, H), (x0, H)]
        else:
            pts += [(x1, 1.0), (x1, H), (x0, H), (x0, 1.0)]
    return [(float(a), float(b)) for a, b in pts]


def _samples(poly, step=0.25):
    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    out = []
    x = min(xs) + step / 2
    while x < max(xs):
        y = min(ys) + step / 2
        while y < max(ys):
            if _point_in_poly((x, y), poly):
                out.append((x, y))
            y += step
        x += step
    return out


def _ear_clip(poly):
    idx = list(range(len(poly)))
    if _area_signed(poly) < 0:
        idx.reverse()
    tris = []
    while len(idx) > 3:
        for i in range(len(idx)):
            a, b, c = idx[i - 1], idx[i], idx[(i + 1) % len(idx)]
            if _cross(poly[a], poly[b], poly[c]) <= 0:
                continue
            if any(_inside_convex(poly[m], [poly[a], poly[b], poly[c]]) for m in idx if m not in (a, b, c)):
                continue
            tris.append((a, b, c))
            idx.pop(i)
            break
        else:
            raise AssertionError('no ear')
    tris.append(tuple(idx))
    return tris


def _fisk_colour(n, tris):
    colour = {}
    t0 = tris[0]
    for i, v in enumerate(t0):
        colour[v] = i
    remaining = list(tris[1:])
    while remaining:
        for t in remaining:
            known = [v for v in t if v in colour]
            if len(known) >= 2:
                for v in t:
                    if v not in colour:
                        colour[v] = ({0, 1, 2} - {colour[u] for u in known}).pop()
                remaining.remove(t)
                break
        else:
            raise AssertionError('disconnected')
    return colour


def check_week_123():
    # Chvatal comb: k teeth, n = 3k + 2 corners, floor(n/3) = k guards, and k are needed.
    for k in (2, 3):
        P = comb(k)
        n = len(P)
        assert n == 3 * k + 2 and n // 3 == k
        tips = [(3 * j + 1.0, 10.0) for j in range(k)]
        pts = _samples(P, 0.25)
        for p in pts:   # no sample point sees two tips (sampled check)
            assert sum(_sees(p, t, P) for t in tips) <= 1
        guards = [(3 * j + 1.0, 0.5) for j in range(k)]
        for p in pts:   # k guards below the teeth see every sample point
            assert any(_sees(g, p, P) for g in guards)
    # Fisk: triangulate, 3-colour, least colour class has at most floor(n/3) corners.
    shapes = [comb(3), rect_comb(3),
              [(0, 0), (6, 0), (6, 4), (4, 4), (4, 2), (2, 2), (2, 5), (0, 5)],
              [(0, 0), (4, 1), (8, 0), (7, 4), (8, 8), (4, 6), (0, 8), (1, 4)]]
    for P in shapes:
        n = len(P)
        tris = _ear_clip(P)
        assert len(tris) == n - 2
        col = _fisk_colour(n, tris)
        assert all({col[a], col[b], col[c]} == {0, 1, 2} for a, b, c in tris)
        sizes = [sum(1 for v in range(n) if col[v] == c) for c in range(3)]
        assert sum(sizes) == n and min(sizes) <= n // 3
    # Convex 9-gon: the least colour depends on the triangulation. A fan from one corner gives
    # that corner its own colour (1 guard); a zigzag gives classes 3, 3, 3.
    fan = [(0, i, i + 1) for i in range(1, 8)]
    col = _fisk_colour(9, fan)
    assert sorted(sum(1 for v in range(9) if col[v] == c) for c in range(3)) == [1, 4, 4]
    zig = [(0, 1, 8), (1, 7, 8), (1, 2, 7), (2, 6, 7), (2, 3, 6), (3, 5, 6), (3, 4, 5)]
    col = _fisk_colour(9, zig)
    assert sorted(sum(1 for v in range(9) if col[v] == c) for c in range(3)) == [3, 3, 3]
    # Orthogonal comb: n = 4k corners, k = floor(n/4) guards needed and enough.
    for k in (2, 3):
        P = rect_comb(k)
        n = len(P)
        assert n == 4 * k and n % 2 == 0
        reflex = sum(1 for i in range(n) if _cross(P[i - 1], P[i], P[(i + 1) % n]) < 0)
        assert n == 2 * reflex + 4
        tops = [(3 * j + 0.5, 9.9) for j in range(k)]
        pts = _samples(P, 0.25)
        for p in pts:
            assert sum(_sees(p, t, P) for t in tops) <= 1
        guards = [(3 * j + 0.5, 0.5) for j in range(k)]
        for p in pts:
            assert any(_sees(g, p, P) for g in guards)
    # Table of floor(n/3) and floor(n/4).
    assert [n // 3 for n in range(3, 13)] == [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
    assert [n // 4 for n in range(4, 17, 2)] == [1, 1, 2, 2, 3, 3, 4]


# ---------------------------------------------------------------------------
# Week 124: fold and cut
# ---------------------------------------------------------------------------

def _reflect(p, a, b):
    ax, ay = a
    dx, dy = b[0] - a[0], b[1] - a[1]
    L2 = dx * dx + dy * dy
    t = ((p[0] - ax) * dx + (p[1] - ay) * dy) / L2
    fx, fy = ax + t * dx, ay + t * dy
    return (2 * fx - p[0], 2 * fy - p[1])


def _fold_map(p, folds):
    """Apply simple folds: each fold (a, b) reflects points left of a->b onto the right."""
    signs = []
    for a, b in folds:
        if _cross(a, b, p) > 1e-12:
            p = _reflect(p, a, b)
            signs.append(1)
        else:
            signs.append(0)
    return p, tuple(signs)


def _dist_line(p, a, b):
    return abs(_cross(a, b, p)) / math.hypot(b[0] - a[0], b[1] - a[1])


def _on_boundary(p, poly, eps=1e-7):
    n = len(poly)
    for i in range(n):
        a, b = poly[i], poly[(i + 1) % n]
        L = math.hypot(b[0] - a[0], b[1] - a[1])
        t = ((p[0] - a[0]) * (b[0] - a[0]) + (p[1] - a[1]) * (b[1] - a[1])) / (L * L)
        if -eps <= t <= 1 + eps and _dist_line(p, a, b) < eps:
            return True
    return False


def _inverse_line(signs, folds, cut):
    a, b = cut
    for s, (fa, fb) in reversed(list(zip(signs, folds))):
        if s:
            a, b = _reflect(a, fa, fb), _reflect(b, fa, fb)
    return a, b


def fold_and_cut_ok(poly, folds, cut, half=4.0):
    # every boundary point lands on the cut line
    n = len(poly)
    for i in range(n):
        a, b = poly[i], poly[(i + 1) % n]
        for t in [j / 50 for j in range(51)]:
            p = (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))
            q, _ = _fold_map(p, folds)
            if _dist_line(q, *cut) > 1e-7:
                return False
    # every paper point landing on the cut line is on the boundary
    for signs in itertools.product((0, 1), repeat=len(folds)):
        la, lb = _inverse_line(signs, folds, cut)
        dx, dy = lb[0] - la[0], lb[1] - la[1]
        L = math.hypot(dx, dy)
        for s in range(-4000, 4001):
            t = s / 500.0
            p = (la[0] + t * dx / L, la[1] + t * dy / L)
            if abs(p[0]) > half or abs(p[1]) > half:
                continue
            q, sg = _fold_map(p, folds)
            if sg != signs:
                continue
            if _dist_line(q, *cut) < 1e-9 and not _on_boundary(p, poly):
                return False
    return True


def mirror_folds(n):
    """Fewest folds along the regular n-gon's mirror lines that stack every edge on one line.

    Rays from the centre at multiples of 180/n degrees; vertices at even multiples.
    State = folded wedge [lo, hi] in those units. Returns None if not reachable.
    """
    def inside(lo, hi):
        m = lo // 2
        return lo >= 2 * m and hi <= 2 * m + 2
    start = [(r, r + n) for r in range(2 * n)]
    frontier = set(start)
    seen = set(frontier)
    depth = 1
    while frontier:
        if any(inside(lo, hi) for lo, hi in frontier):
            return depth
        nxt = set()
        for lo, hi in frontier:
            for r in range(lo + 1, hi):
                w = (lo, r) if r - lo >= hi - r else (r, hi)
                if w not in seen:
                    seen.add(w)
                    nxt.add(w)
        frontier = nxt
        depth += 1
    return None


def check_week_124():
    # Square: two diagonal folds then one cut.
    sq = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    assert fold_and_cut_ok(sq, [((1, 1), (-1, -1)), ((-1, 1), (1, -1))], ((-1, -1), (-1, 1)))
    # Equilateral triangle: two folds along mirror lines.
    v = [(math.cos(math.radians(a)), math.sin(math.radians(a))) for a in (90, 210, 330)]
    tri = v
    f1 = ((0, -1), (0, 1))                       # move x < 0 onto x > 0
    d = (math.cos(math.radians(-30)), math.sin(math.radians(-30)))
    f2 = (d, (-d[0], -d[1]))                     # line through centre and the 330-degree corner
    assert fold_and_cut_ok(tri, [f1, f2], (v[2], v[0]))
    # Non-square rectangle: halve twice, then fold the corner's bisector: three folds.
    rect = [(-2, -1), (2, -1), (2, 1), (-2, 1)]
    folds = [((0, -1), (0, 1)), ((1, 0), (-1, 0)), ((0, -1), (3, 2))]
    assert fold_and_cut_ok(rect, folds, ((2, -3), (2, 3)))
    # The rectangle's two halvings alone do not stack its edges on one line.
    assert not fold_and_cut_ok(rect, folds[:2], ((2, -3), (2, 3)))
    # A single fold makes mirror shapes: one fold along x = 0 and a cut cuts a symmetric pair.
    # Mirror-line folds for regular n-gons (an upper bound; the model allows only symmetry folds).
    table = {n: mirror_folds(n) for n in range(3, 11)}
    assert table == {n: math.ceil(math.log2(n)) for n in range(3, 11)}, table
    assert table == {3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4}
    check_week_124.table = table


def main():
    for name in ('check_week_120', 'check_week_121', 'check_week_122',
                 'check_week_123', 'check_week_124'):
        globals()[name]()
        print(name, 'ok')
    print('week 120 degree-<=5 sphere triangulations by vertex count:', check_week_120.counts)
    print('week 122 untileable convex 16-triangle shapes, side counts:', check_week_122.untileable)
    print('week 124 mirror-line folds for regular n-gons:', check_week_124.table)


if __name__ == '__main__':
    main()
