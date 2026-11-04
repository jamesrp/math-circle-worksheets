#!/usr/bin/env python3
"""Checks for the draft plans of weeks 164-170 (shape group 2).

Standard library only. Run: python3 plans/drafts/weeks-101-plus/check_shape_2.py
Each check_week_1NN() asserts the small numbers its draft quotes.
"""

import cmath
import itertools
import math
import random
from fractions import Fraction
from math import gcd

PHI = (1 + 5 ** 0.5) / 2


# ---------------------------------------------------------------------------
# Week 164: Borromean rings
# ---------------------------------------------------------------------------

def _ellipse_rings(a=2.0, b=1.0, n=400):
    """Three ellipses in the three coordinate planes (the standard model)."""
    ts = [2 * math.pi * k / n for k in range(n)]
    r1 = [(a * math.cos(t), b * math.sin(t), 0.0) for t in ts]   # xy-plane
    r2 = [(0.0, a * math.cos(t), b * math.sin(t)) for t in ts]   # yz-plane
    r3 = [(b * math.sin(t), 0.0, a * math.cos(t)) for t in ts]   # zx-plane
    return r1, r2, r3


def _rect_ring(axis, long, short, n_per_side=50):
    """Boundary of a long-by-short rectangle centred at 0, as a closed polygon.
    axis 0: rectangle in the xy-plane, long along x;
    axis 1: in the yz-plane, long along y; axis 2: in the zx-plane, long along z."""
    corners = [(long, short), (-long, short), (-long, -short), (long, -short)]
    pts = []
    for i in range(4):
        (u1, v1), (u2, v2) = corners[i], corners[(i + 1) % 4]
        for k in range(n_per_side):
            s = k / n_per_side
            u, v = u1 + s * (u2 - u1), v1 + s * (v2 - v1)
            if axis == 0:
                pts.append((u, v, 0.0))
            elif axis == 1:
                pts.append((0.0, u, v))
            else:
                pts.append((v, 0.0, u))
    return pts


def _signed_disk_crossings(curve, plane_axis, inside):
    """Signed crossings of a closed polygon through the flat disk bounded by a
    planar ring lying in the coordinate plane {coordinate plane_axis = 0};
    inside(p) tests whether a point of that plane is in the ring's disk.
    Returns (number of piercings, signed sum) = (geometric, linking number up to sign)."""
    count, signed = 0, 0
    n = len(curve)
    for i in range(n):
        p, q = curve[i], curve[(i + 1) % n]
        zp, zq = p[plane_axis], q[plane_axis]
        if (zp > 0) != (zq > 0):
            s = zp / (zp - zq)
            x = [p[k] + s * (q[k] - p[k]) for k in range(3)]
            if inside(x):
                count += 1
                signed += 1 if zq > zp else -1
    return count, signed


def check_week_164():
    a, b = 2.0, 1.0
    r1, r2, r3 = _ellipse_rings(a, b)

    def in_disk1(p):            # ellipse x^2/a^2 + y^2/b^2 <= 1 in the xy-plane
        return (p[0] / a) ** 2 + (p[1] / b) ** 2 < 1

    # Ring 2 misses ring 1's flat disk entirely; ring 3 pierces it twice,
    # once each way: both pairs have linking number 0.
    assert _signed_disk_crossings(r2, 2, in_disk1) == (0, 0)
    assert _signed_disk_crossings(r3, 2, in_disk1) == (2, 0)
    # By the threefold symmetry (x, y, z) -> (y, z, x), which maps ring 1 to
    # ring 2, ring 2 to ring 3 and ring 3 to ring 1, every pair behaves alike.
    cyc = lambda p: (p[2], p[0], p[1])
    assert all(max(abs(u - v) for u, v in zip(cyc(p), q)) < 1e-12 for p, q in zip(r1, r2))
    assert all(max(abs(u - v) for u, v in zip(cyc(p), q)) < 1e-12 for p, q in zip(r2, r3))

    # A Hopf pair for contrast: a unit circle in the xy-plane and a circle in
    # the xz-plane through its centre region: linking number +-1.
    hopf = [(1 + math.cos(t), 0.0, math.sin(t))
            for t in (2 * math.pi * k / 400 for k in range(400))]
    cnt, sgn = _signed_disk_crossings(hopf, 2, lambda p: p[0] ** 2 + p[1] ** 2 < 1)
    assert cnt == 1 and abs(sgn) == 1

    # Three golden (1 by phi half-sides) rectangles: same pattern.
    A = _rect_ring(0, PHI, 1.0)
    B = _rect_ring(1, PHI, 1.0)
    C = _rect_ring(2, PHI, 1.0)
    in_A = lambda p: abs(p[0]) < PHI and abs(p[1]) < 1.0
    assert _signed_disk_crossings(B, 2, in_A) == (0, 0)
    assert _signed_disk_crossings(C, 2, in_A) == (2, 0)
    # Any long/short ratio above 1 gives the same piercing pattern; ratio 1 fails
    # (the corners would touch).
    for long in (1.2, 1.5, 2.0, 3.0):
        Bx, Cx = _rect_ring(1, long, 1.0, 20), _rect_ring(2, long, 1.0, 20)
        ins = lambda p, L=long: abs(p[0]) < L and abs(p[1]) < 1.0
        assert _signed_disk_crossings(Bx, 2, ins) == (0, 0)
        assert _signed_disk_crossings(Cx, 2, ins) == (2, 0)

    # The 12 corners of the golden rectangles form a regular icosahedron:
    # every corner has 5 nearest neighbours at distance 2, 30 edges in all.
    corners = []
    for s1 in (1, -1):
        for s2 in (1, -1):
            corners += [(s1 * PHI, s2 * 1.0, 0.0), (0.0, s1 * PHI, s2 * 1.0),
                        (s2 * 1.0, 0.0, s1 * PHI)]
    assert len(set(corners)) == 12
    d = lambda p, q: math.dist(p, q)
    edges = [(i, j) for i in range(12) for j in range(i + 1, 12)
             if abs(d(corners[i], corners[j]) - 2.0) < 1e-9]
    assert len(edges) == 30
    deg = [sum(1 for e in edges if i in e) for i in range(12)]
    assert deg == [5] * 12
    assert min(d(p, q) for p, q in itertools.combinations(corners, 2)) > 2 - 1e-9

    # Three rings laid as an overlapping three-circle (Venn) picture cross in
    # 6 places, two for each pair: 2^6 = 64 over/under choices. A pair is
    # unhooked exactly when the same ring is on top at both of its crossings,
    # so 2^3 = 8 choices leave every pair unhooked. Each of those says, for each
    # pair, which ring lies on top; 6 are a straight stack (lift the top ring
    # off) and 2 are cycles (red over blue over yellow over red, and its mirror
    # image), which are the Borromean rings.
    pairs = [(0, 1), (1, 2), (0, 2)]
    pairwise_free = []
    for choice in itertools.product((0, 1), repeat=6):
        tops = []
        ok = True
        for k, (i, j) in enumerate(pairs):
            c1, c2 = choice[2 * k], choice[2 * k + 1]   # 0: i on top, 1: j on top
            if c1 != c2:
                ok = False                             # a Hopf hook (linking number +-1)
            tops.append((i, j) if c1 == 0 else (j, i))
        if ok:
            pairwise_free.append(tops)
    assert len(pairwise_free) == 8
    def is_cycle(tops):
        above = {a: b for a, b in tops}               # a lies on top of b
        # a cycle means every ring is on top of exactly one other
        return sorted(above) == [0, 1, 2]
    assert sum(1 for t in pairwise_free if is_cycle(t)) == 2


# ---------------------------------------------------------------------------
# Week 165: inside or outside (Jordan curve theorem, parity of crossings)
# ---------------------------------------------------------------------------

def _ray_crossings(pt, poly, direction):
    """Crossings of the ray from pt in a direction (0 right, 1 up, 2 left, 3 down)
    with the closed polygon poly (points chosen off vertex lines)."""
    x, y = pt
    c = 0
    n = len(poly)
    for i in range(n):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % n]
        if direction in (0, 2):
            if (y1 > y) != (y2 > y):
                xc = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                if (direction == 0 and xc > x) or (direction == 2 and xc < x):
                    c += 1
        else:
            if (x1 > x) != (x2 > x):
                yc = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
                if (direction == 1 and yc > y) or (direction == 3 and yc < y):
                    c += 1
    return c


def _winding(pt, poly):
    total = 0.0
    n = len(poly)
    for i in range(n):
        a = complex(*poly[i]) - complex(*pt)
        b = complex(*poly[(i + 1) % n]) - complex(*pt)
        total += cmath.phase(b / a)
    return round(total / (2 * math.pi))


# A square spiral "snail shell": a simple closed rectilinear loop made of a
# corridor of width 1 that winds in towards the centre (outer box 0..11).
SPIRAL = [(0, 0), (11, 0), (11, 11), (2, 11), (2, 4), (7, 4), (7, 7), (6, 7),
          (6, 5), (3, 5), (3, 10), (10, 10), (10, 1), (1, 1), (1, 12), (0, 12)]


def _is_simple(poly):
    def seg_inter(p1, p2, p3, p4):
        def orient(a, b, c):
            v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
            return (v > 0) - (v < 0)
        o1, o2 = orient(p1, p2, p3), orient(p1, p2, p4)
        o3, o4 = orient(p3, p4, p1), orient(p3, p4, p2)
        if o1 != o2 and o3 != o4:
            return True
        def on(a, b, c):
            return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0])
                    and min(a[1], b[1]) <= c[1] <= max(a[1], b[1]))
        return ((o1 == 0 and on(p1, p2, p3)) or (o2 == 0 and on(p1, p2, p4))
                or (o3 == 0 and on(p3, p4, p1)) or (o4 == 0 and on(p3, p4, p2)))
    n = len(poly)
    for i in range(n):
        for j in range(i + 1, n):
            if j == i + 1 or (i == 0 and j == n - 1):
                continue
            if seg_inter(poly[i], poly[(i + 1) % n], poly[j], poly[(j + 1) % n]):
                return False
    return True


def check_week_165():
    assert _is_simple(SPIRAL)
    rng = random.Random(165)
    # For random points (off the grid lines), all four ray directions give the
    # same parity, and odd parity matches winding number +-1 (inside).
    inside_count = 0
    for _ in range(3000):
        p = (rng.uniform(-1, 13) + 1e-7, rng.uniform(-1, 13) + 1e-7)
        par = [_ray_crossings(p, SPIRAL, d) % 2 for d in range(4)]
        assert len(set(par)) == 1
        w = _winding(p, SPIRAL)
        assert (par[0] == 1) == (abs(w) == 1)
        assert w in (-1, 0, 1)
        inside_count += par[0]
    assert inside_count > 0
    # The toy at the inner end of the corridor, (6.5, 6.5): a ray to the left
    # crosses the loop 5 times (odd: inside); a ray to the right crosses 3 times.
    toy = (6.5, 6.5 + 1e-7)
    assert _ray_crossings(toy, SPIRAL, 2) == 5 and _ray_crossings(toy, SPIRAL, 0) == 3
    assert _winding(toy, SPIRAL) != 0
    # A point in the gap between corridor walls, (4.5, 6.5): 4 to the left, even, outside.
    gap = (4.5, 6.5 + 1e-7)
    assert _ray_crossings(gap, SPIRAL, 2) == 4
    assert _winding(gap, SPIRAL) == 0
    # Area check: the loop encloses 64 of the 144 unit squares of its 12 by 12 box.
    area2 = sum(SPIRAL[i][0] * SPIRAL[(i + 1) % len(SPIRAL)][1]
                - SPIRAL[(i + 1) % len(SPIRAL)][0] * SPIRAL[i][1]
                for i in range(len(SPIRAL)))
    cells_in = sum(1 for i in range(12) for j in range(12)
                   if _ray_crossings((i + 0.5, j + 0.5 + 1e-7), SPIRAL, 0) % 2)
    assert abs(area2) / 2 == cells_in
    check_week_165.cells_in = cells_in

    # A self-crossing loop (a figure eight drawn as a bow tie): crossing parity
    # still two-colours the regions, but the winding numbers are +1 and -1.
    bow = [(0, 0), (4, 4), (4, 0), (0, 4)]
    left, right = (1, 2.01), (3, 2.01)
    assert _ray_crossings(left, bow, 0) % 2 == 1 and _ray_crossings(right, bow, 0) % 2 == 1
    assert {_winding(left, bow), _winding(right, bow)} == {1, -1}
    # A pentagram drawn in one stroke: the centre pentagon has winding 2, so its
    # crossing parity is even ("outside" by the parity rule) though it is enclosed.
    star = [(math.cos(math.pi / 2 + 4 * math.pi * k / 5), math.sin(math.pi / 2 + 4 * math.pi * k / 5))
            for k in range(5)]
    c0 = (0.001, 0.002)
    assert abs(_winding(c0, star)) == 2 and _ray_crossings(c0, star, 0) % 2 == 0
    tip = (0.0, 0.8)
    assert abs(_winding(tip, star)) == 1 and _ray_crossings(tip, star, 0) % 2 == 1


# ---------------------------------------------------------------------------
# Week 166: hairy ball, indices and the Euler characteristic
# ---------------------------------------------------------------------------

def _index(field, r=0.5, n=720):
    """Turns of the arrow field(z) as z goes once round the circle |z| = r."""
    total = 0.0
    prev = field(complex(r, 0))
    for k in range(1, n + 1):
        z = r * cmath.exp(2j * math.pi * k / n)
        cur = field(z)
        total += cmath.phase(cur / prev)
        prev = cur
    return round(total / (2 * math.pi))


def check_week_166():
    fields = {
        'spring (source)': lambda z: z,
        'drain (sink)': lambda z: -z,
        'whirl (vortex)': lambda z: 1j * z,
        'saddle': lambda z: z.conjugate(),
        'dipole': lambda z: z * z,
        'monkey saddle': lambda z: z.conjugate() ** 2,
    }
    idx = {k: _index(f) for k, f in fields.items()}
    assert idx == {'spring (source)': 1, 'drain (sink)': 1, 'whirl (vortex)': 1,
                   'saddle': -1, 'dipole': 2, 'monkey saddle': -2}
    # The steady east wind on the plane, carried to the sphere by w = 1/z,
    # becomes -w^2 near the point at infinity: one calm spot, index 2.
    assert _index(lambda w: -w * w) == 2
    # North-to-south flow on the sphere: a spring and a drain, 1 + 1 = 2.
    assert idx['spring (source)'] + idx['drain (sink)'] == 2
    # Two springs, two drains and two saddles also total 2.
    assert 2 * 1 + 2 * 1 + 2 * (-1) == 2

    # Euler characteristic V - E + F for surfaces children can draw on.
    solids = {'tetrahedron': (4, 6, 4), 'cube': (8, 12, 6), 'octahedron': (6, 12, 8),
              'dodecahedron': (20, 30, 12), 'icosahedron': (12, 30, 20)}
    for v, e, f in solids.values():
        assert v - e + f == 2
    # A torus made from an m by n grid with opposite edges glued: V = mn,
    # E = 2mn, F = mn, so V - E + F = 0.
    for m, n in ((3, 3), (4, 5)):
        assert m * n - 2 * m * n + m * n == 0
    # A sphere-shaped "pillow" (two squares sewn at the edges): V=4, E=4, F=2.
    assert 4 - 4 + 2 == 2

    # The vertex-edge-face field: springs at the 8 corners, saddles at the 12
    # edge midpoints, drains at the 6 face centres of a cube: 8 - 12 + 6 = 2.
    v, e, f = solids['cube']
    assert v * idx['spring (source)'] + e * idx['saddle'] + f * idx['drain (sink)'] == 2
    # On a 3 by 3 torus grid the same recipe gives 9 - 18 + 9 = 0, and the
    # steady wind along one direction has no calm spot at all.
    assert 9 - 18 + 9 == 0


# ---------------------------------------------------------------------------
# Week 167: total turning
# ---------------------------------------------------------------------------

def _turtle(program):
    """program: list of ('F', d) or ('T', degrees left). Returns path and turning."""
    x = y = 0.0
    h = 0.0
    pts = [(0.0, 0.0)]
    turn = 0
    for op, v in program:
        if op == 'F':
            x += v * math.cos(math.radians(h))
            y += v * math.sin(math.radians(h))
            pts.append((round(x, 9), round(y, 9)))
        else:
            h += v
            turn += v
    return pts, turn


def _poly(step_angle):
    """Repeat FORWARD 1, LEFT A until heading and position return."""
    k = 360 // gcd(step_angle, 360)
    prog = [('F', 1), ('T', step_angle)] * k
    pts, turn = _turtle(prog)
    return k, turn, pts


def _grid_turning(moves):
    """moves: string over E N W S for a closed grid walk; returns L - R in quarter turns
    counted at every step including the closing corner."""
    dirs = 'ENWS'
    total = 0
    n = len(moves)
    for i in range(n):
        a, b = dirs.index(moves[i]), dirs.index(moves[(i + 1) % n])
        d = (b - a) % 4
        assert d != 2, 'no U-turns on a smooth walk'
        total += {0: 0, 1: 1, 3: -1}[d]
    return total


def _self_avoiding_polygons(max_len):
    """Closed self-avoiding grid walks from the origin (as move strings)."""
    step = {'E': (1, 0), 'N': (0, 1), 'W': (-1, 0), 'S': (0, -1)}
    found = []

    def go(pos, visited, path):
        if len(path) == max_len:
            return
        for m, (dx, dy) in step.items():
            nxt = (pos[0] + dx, pos[1] + dy)
            if nxt == (0, 0) and len(path) >= 3:
                found.append(path + m)
            elif nxt not in visited:
                visited.add(nxt)
                go(nxt, visited, path + m)
                visited.remove(nxt)

    go((0, 0), {(0, 0)}, '')
    return found


def check_week_167():
    # Regular polygons and stars: steps to close and total turning.
    table = {}
    for a in (90, 120, 72, 60, 144, 135, 150, 160):
        k, turn, pts = _poly(a)
        assert abs(pts[-1][0]) < 1e-6 and abs(pts[-1][1]) < 1e-6   # back home
        # It is not home earlier with the starting heading.
        table[a] = (k, turn // 360)
    assert table == {90: (4, 1), 120: (3, 1), 72: (5, 1), 60: (6, 1),
                     144: (5, 2), 135: (8, 3), 150: (12, 5), 160: (9, 4)}
    # The closing rule: steps = 360 / gcd(A, 360), full turns = A / gcd(A, 360).
    for a in range(1, 360):
        k = 360 // gcd(a, 360)
        assert k * a == math.lcm(a, 360)
        s = sum(cmath.exp(1j * math.radians(a * j)) for j in range(k))
        assert abs(s) < 1e-9

    # Every simple closed grid loop up to length 14 turns exactly once
    # (L - R = +4 or -4 quarter turns).
    loops = _self_avoiding_polygons(14)
    assert len(loops) == 20144   # walks from a fixed start, each loop counted per start and direction
    assert {_grid_turning(m) for m in loops} == {4, -4}
    # A figure eight on the grid (two unit squares, one walked each way,
    # crossing at the shared corner region) turns 0 in all.
    fig8 = 'ENNESWWS'   # up through the middle point, round the top square, back across it
    assert _grid_turning(fig8) == 0
    # A loop walked twice around turns twice.
    assert _grid_turning('ENWS' * 2) == 8
    # Tape-path example: a 3-by-2 rectangle with a notch: L - R = 4 with L = 5, R = 1.
    notch = 'EEENNWSWWS'  # check it is closed
    x = y = 0
    for m in notch:
        x += {'E': 1, 'W': -1}.get(m, 0)
        y += {'N': 1, 'S': -1}.get(m, 0)
    assert (x, y) == (0, 0)
    dirs = 'ENWS'
    lefts = sum(1 for i in range(len(notch))
                if (dirs.index(notch[(i + 1) % len(notch)]) - dirs.index(notch[i])) % 4 == 1)
    rights = sum(1 for i in range(len(notch))
                 if (dirs.index(notch[(i + 1) % len(notch)]) - dirs.index(notch[i])) % 4 == 3)
    assert (lefts, rights) == (5, 1) and _grid_turning(notch) == 4


# ---------------------------------------------------------------------------
# Week 168: folding beats the compass
# ---------------------------------------------------------------------------

def _reflect(p, a, b):
    """Reflect point p in the line through a and b."""
    ax, ay = a
    dx, dy = b[0] - ax, b[1] - ay
    t = ((p[0] - ax) * dx + (p[1] - ay) * dy) / (dx * dx + dy * dy)
    fx, fy = ax + t * dx, ay + t * dy
    return (2 * fx - p[0], 2 * fy - p[1])


def _line_inter(p1, p2, p3, p4):
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3; x4, y4 = p4
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))


def _haga(q):
    """Unit square, corners (0,0),(1,0),(1,1),(0,1). Fold the bottom-left corner
    (0,0) up onto the point (q,1) of the top edge. The crease is the perpendicular
    bisector of the corner and its landing point. The folded bottom edge runs
    from (q,1) down to the right edge x = 1; return how far below the top-right
    corner it meets that edge."""
    mid = (q / 2, 0.5)
    direction = (1.0, -q)              # perpendicular to (q, 1)
    a, b = mid, (mid[0] + direction[0], mid[1] + direction[1])
    img0 = _reflect((0, 0), a, b)      # = (q, 1)
    img1 = _reflect((1, 0), a, b)
    return 1 - _line_inter(img0, img1, (1, 0), (1, 1))[1]


def _abe(theta_deg, h=0.2):
    """Abe's trisection in a unit square with corner B=(0,0), bottom edge on the
    x-axis, left edge on the y-axis. Line BP at angle theta. Horizontal creases
    y = h and y = 2h; E=(0,2h). Find the fold sending B onto y = h and E onto BP;
    return angles (degrees) of B->image(B) and B->image(F), F=(0,h)."""
    th = math.radians(theta_deg)
    u = (math.cos(th), math.sin(th))

    def residual(x):
        Bp = (x, h)                            # image of B on the line y = h
        mid = (x / 2, h / 2)
        d = (h, -x)                            # crease direction, perpendicular to B->B'
        a, b = mid, (mid[0] + d[0], mid[1] + d[1])
        Ep = _reflect((0, 2 * h), a, b)
        return Ep[0] * u[1] - Ep[1] * u[0], (a, b)   # cross product: zero when E' on BP

    # Scan for the root at which E lands on the ray BP itself (not its extension
    # behind B), then refine by bisection.
    lo = hi = None
    prev_x, prev_r = None, None
    for k in range(1, 2000):
        xx = k * 0.002
        r, (a, b) = residual(xx)
        Ep = _reflect((0, 2 * h), a, b)
        if prev_r is not None and (r > 0) != (prev_r > 0) and Ep[0] * u[0] + Ep[1] * u[1] > 0:
            lo, hi = prev_x, xx
            break
        prev_x, prev_r = xx, r
    flo = residual(lo)[0]
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = residual(mid)[0]
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    x = (lo + hi) / 2
    a, b = residual(x)[1]
    Bp = _reflect((0, 0), a, b)
    Fp = _reflect((0, h), a, b)
    ang = lambda p: math.degrees(math.atan2(p[1], p[0]))
    return ang(Bp), ang(Fp)


def check_week_168():
    # Haga: fold a corner up to the midpoint of the top edge; the folded bottom
    # edge meets the right edge 2/3 of the way down, i.e. 1/3 up from the bottom.
    assert abs(_haga(0.5) - 2 / 3) < 1e-12
    # Folding to the 1/3 mark instead gives 1/2 (general rule 2q/(1+q)).
    for q in (0.5, 1 / 3, 0.25, 0.2):
        assert abs(_haga(q) - 2 * q / (1 + q)) < 1e-12
    assert abs(_haga(1 / 3) - 0.5) < 1e-12
    # Landing at the 1/4 mark gives 2/5: Haga's fold makes fifths from quarters.
    assert abs(_haga(0.25) - 0.4) < 1e-12

    # Equilateral triangle from a square: crease the vertical centre line, then
    # fold the bottom-left corner's edge so the corner lands on the centre line
    # with the crease through the bottom-right corner: the landing point is at
    # height sqrt(3)/2, and the three points form an equilateral triangle.
    land = (0.5, math.sqrt(1 - 0.25))
    for p, q in (((0, 0), (1, 0)), ((0, 0), land), ((1, 0), land)):
        assert abs(math.dist(p, q) - 1) < 1e-12
    assert abs(land[1] - math.sqrt(3) / 2) < 1e-12 and land[1] < 1

    # Abe's trisection works for acute angles of the corner.
    for th in (30, 45, 60, 75, 80):
        a1, a2 = _abe(th)
        assert abs(a1 - th / 3) < 1e-6 and abs(a2 - 2 * th / 3) < 1e-6

    # Fujimoto-style pinch folding: start anywhere, fold the right part in half,
    # then the left part in half; the error from 1/3 shrinks by 4 each round.
    x = Fraction(1, 2)
    errs = []
    for _ in range(5):
        x = (x + 1) / 2      # pinch midway between the mark and the right edge
        x = x / 2            # then midway between the left edge and that pinch
        errs.append(abs(x - Fraction(1, 3)))
    assert errs[0] == Fraction(1, 24)
    assert all(errs[i + 1] * 4 == errs[i] for i in range(4))

    # The cube root of 2 is a root of x^3 - 2 with no rational root, so it has
    # degree 3, not a power of 2: no compass construction (Wantzel 1837).
    assert all(Fraction(p, q) ** 3 != 2 for p in range(1, 30) for q in range(1, 30))


# ---------------------------------------------------------------------------
# Week 169: stacking oranges
# ---------------------------------------------------------------------------

def check_week_169():
    sq = [sum(k * k for k in range(1, n + 1)) for n in range(1, 8)]
    tri = [sum(k * (k + 1) // 2 for k in range(1, n + 1)) for n in range(1, 8)]
    assert sq == [1, 5, 14, 30, 55, 91, 140]
    assert tri == [1, 4, 10, 20, 35, 56, 84]
    for n in range(1, 50):
        assert sum(k * k for k in range(1, n + 1)) == n * (n + 1) * (2 * n + 1) // 6
    # Cannonball problem: 1^2 + ... + 24^2 = 4900 = 70^2; no other n up to 10^6.
    hits = []
    for n in range(1, 10 ** 6 + 1):
        s = n * (n + 1) * (2 * n + 1) // 6
        r = math.isqrt(s)
        if r * r == s:
            hits.append(n)
    assert hits == [1, 24] and 24 * 25 * 49 // 6 == 4900 == 70 ** 2

    # Densities: grocer's stack (fcc) pi/sqrt(18), cube stacking pi/6.
    fcc = math.pi / math.sqrt(18)
    assert abs(fcc - 0.74048) < 1e-5
    assert abs(math.pi / 6 - 0.5236) < 1e-4
    # Hexagonal layers stacked straight up (each ball on top of one below):
    # density pi/(3 sqrt 3) ~ 0.6046.
    assert abs(math.pi / (3 * math.sqrt(3)) - 0.6046) < 1e-4

    # Square-pyramid layers: k by k square grid of unit balls, next layer in the
    # hollows at height 1/sqrt2. Each ball touches 4 below, 4 beside, 4 above
    # (12) inside a big stack, and the stack is the same lattice as the
    # triangular-pyramid stack (the fcc lattice).
    def square_stack(n):
        pts = []
        for layer in range(n):
            k = n - layer
            off = layer * 0.5
            for i in range(k):
                for j in range(k):
                    pts.append((i + off, j + off, layer / math.sqrt(2)))
        return pts
    pts = square_stack(6)
    assert len(pts) == 91
    for p, q in itertools.combinations(pts, 2):
        assert math.dist(p, q) > 1 - 1e-9          # no overlaps
    # Contact numbers: an interior ball of a huge slab of this packing has 12.
    big = []
    for layer in range(-2, 3):
        off = (layer % 2) * 0.5
        for i in range(-3, 4):
            for j in range(-3, 4):
                big.append((i + off, j + off, layer / math.sqrt(2)))
    centre = (0.0, 0.0, 0.0)
    touching = [p for p in big if abs(math.dist(p, centre) - 1) < 1e-9]
    assert len(touching) == 12
    # The same 12 neighbours as the fcc lattice {integer points with even sum}
    # scaled by 1/sqrt2: rotate by 45 degrees about the vertical axis.
    fcc_nb = [p for p in itertools.product(range(-1, 2), repeat=3)
              if sum(p) % 2 == 0 and p != (0, 0, 0)]
    assert len(fcc_nb) == 12

    # Balls of diameter 1 in a box 4 wide, 4 deep: straight stacking puts 16 in
    # every layer one unit apart; offset stacking alternates 16 and 9 at
    # spacing 1/sqrt2. Box height 4: 64 against 66; height 6: 96 against 100.
    def straight(H):
        return 16 * int(H)               # layers at z = 0, 1, ..., H - 1
    def offset(H):
        layers = int((H - 1) * math.sqrt(2) + 1e-9) + 1
        return sum(16 if k % 2 == 0 else 9 for k in range(layers))
    assert (straight(4), offset(4)) == (64, 66)
    assert (straight(6), offset(6)) == (96, 100)

    def to_fcc(p):
        x, y, z = p
        return (round(x + y, 9), round(x - y, 9), round(z * math.sqrt(2), 9))
    mapped = {to_fcc(p) for p in touching}
    assert mapped == {tuple(float(c) for c in t) for t in fcc_nb}
    # Number of balls touching a ball resting on a flat table in a square layer: 4
    # beside; in a triangular layer: 6 beside.
    assert sum(1 for p in big if p[2] == 0 and abs(math.dist(p, centre) - 1) < 1e-9) == 4


# ---------------------------------------------------------------------------
# Week 170: rep-tiles
# ---------------------------------------------------------------------------

def _orientations(cells):
    out = set()
    pts = list(cells)
    for flip in (False, True):
        for r in range(4):
            q = []
            for x, y in pts:
                if flip:
                    x = -x
                for _ in range(r):
                    x, y = -y, x
                q.append((x, y))
            mx, my = min(a for a, _ in q), min(b for _, b in q)
            out.add(frozenset((a - mx, b - my) for a, b in q))
    return out


def _count_tilings(region, piece, limit=10 ** 6):
    """Count tilings of a set of square cells by copies of a polyomino."""
    shapes = _orientations(piece)
    region = frozenset(region)
    placements = {}
    for s in shapes:
        for ax, ay in region:
            for (px, py) in s:
                dx, dy = ax - px, ay - py
                cells = frozenset((x + dx, y + dy) for x, y in s)
                if cells <= region:
                    for c in cells:
                        placements.setdefault(c, set()).add(cells)
    count = 0

    def go(empty):
        nonlocal count
        if count >= limit:
            return
        if not empty:
            count += 1
            return
        c = min(empty)
        for pl in placements.get(c, ()):
            if pl <= empty:
                go(empty - pl)

    go(region)
    return count


def _scale(cells, k):
    return {(k * x + i, k * y + j) for x, y in cells for i in range(k) for j in range(k)}


L_TROMINO = {(0, 0), (1, 0), (0, 1)}
L_TETROMINO = {(0, 0), (0, 1), (0, 2), (1, 0)}
T_TETROMINO = {(0, 0), (1, 0), (2, 0), (1, 1)}
S_TETROMINO = {(0, 0), (1, 0), (1, 1), (2, 1)}


def _chair_substitution(level):
    """Split an L of side n = 2^level (three n-by-n squares in a 2n-by-2n box)
    into 4 Ls of side n/2, repeatedly, down to unit L-trominoes (the chair rule).
    Returns the region and the list of unit tiles."""
    n = 2 ** level
    region = {(x, y) for x in range(2 * n) for y in range(2 * n)
              if not (x >= n and y >= n)}

    def split(cells, n):
        if n == 1:
            assert len(cells) == 3
            return [cells]
        xs = [x for x, _ in cells]; ys = [y for _, y in cells]
        x0, y0 = min(xs), min(ys)
        cx, cy = x0 + n, y0 + n                    # centre of the 2n box
        quads = {}
        for x, y in cells:
            quads.setdefault(((x - x0) // n, (y - y0) // n), set()).add((x, y))
        assert len(quads) == 3
        middle = set()
        pieces = []
        for sq in quads.values():
            near = {(x, y) for x, y in sq
                    if abs(x + 0.5 - cx) < n / 2 and abs(y + 0.5 - cy) < n / 2}
            middle |= near
            pieces.append(sq - near)
        pieces.append(middle)
        out = []
        for p in pieces:
            assert len(p) == 3 * (n // 2) ** 2
            out += split(p, n // 2)
        return out

    return region, split(region, n)


def _sphinx_cells():
    """Unit triangles of the sphinx hexiamond on the triangular lattice, as
    frozensets of 3 lattice vertices in axial coordinates."""
    h = math.sqrt(3) / 2
    poly = [(0, 0), (3, 0), (2.5, h), (1.5, h), (1, 2 * h)]

    def cart(a, b):
        return (a + b / 2, b * h)

    def inside(pt):
        x, y = pt
        c = False
        for i in range(len(poly)):
            (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % len(poly)]
            if (y1 > y) != (y2 > y):
                if x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
                    c = not c
        return c

    cells = set()
    for i in range(-2, 5):
        for j in range(-2, 4):
            for tri in (((i, j), (i + 1, j), (i, j + 1)),
                        ((i + 1, j), (i, j + 1), (i + 1, j + 1))):
                cx = sum(cart(*v)[0] for v in tri) / 3
                cy = sum(cart(*v)[1] for v in tri) / 3
                if inside((cx, cy)):
                    cells.add(frozenset(tri))
    return cells


def _tri_transforms(cells):
    out = set()
    for flip in (False, True):
        for r in range(6):
            new = []
            for tri in cells:
                vs = []
                for a, b in tri:
                    if flip:
                        a, b = b, a
                    for _ in range(r):
                        a, b = -b, a + b
                    vs.append((a, b))
                new.append(vs)
            ma = min(a for t in new for a, _ in t)
            mb = min(b for t in new for _, b in t)
            out.add(frozenset(frozenset((a - ma, b - mb) for a, b in t) for t in new))
    return out


def _tri_scale2(cells):
    """Split each unit triangle into 4 after doubling coordinates."""
    out = set()
    for tri in cells:
        p, q, r = [(2 * a, 2 * b) for a, b in tri]
        m = lambda u, v: ((u[0] + v[0]) // 2, (u[1] + v[1]) // 2)
        pq, qr, rp = m(p, q), m(q, r), m(r, p)
        for t in ((p, pq, rp), (pq, q, qr), (rp, qr, r), (pq, qr, rp)):
            out.add(frozenset(t))
    return out


def _tri_scale(cells, k):
    """Scale a set of lattice triangles by k and split each into k*k unit triangles."""
    out = set()
    for tri in cells:
        p0, p1, p2 = [(k * a, k * b) for a, b in tri]
        e1 = ((p1[0] - p0[0]) // k, (p1[1] - p0[1]) // k)
        e2 = ((p2[0] - p0[0]) // k, (p2[1] - p0[1]) // k)
        for i in range(k):
            for j in range(k - i):
                A = (p0[0] + i * e1[0] + j * e2[0], p0[1] + i * e1[1] + j * e2[1])
                B = (A[0] + e1[0], A[1] + e1[1])
                C = (A[0] + e2[0], A[1] + e2[1])
                out.add(frozenset([A, B, C]))
                if j < k - i - 1:
                    D = (B[0] + e2[0], B[1] + e2[1])
                    out.add(frozenset([B, C, D]))
    return out


def _count_tri_tilings(region, piece):
    shapes = _tri_transforms(piece)
    region = frozenset(region)
    verts = {v for t in region for v in t}
    placements = {}
    for s in shapes:
        sv = {v for t in s for v in t}
        for (ax, ay) in verts:
            for (px, py) in sv:
                da, db = ax - px, ay - py
                pl = frozenset(frozenset((a + da, b + db) for a, b in t) for t in s)
                if pl <= region:
                    for c in pl:
                        placements.setdefault(c, set()).add(pl)
    order = sorted(region, key=lambda t: sorted(t))
    count = 0

    def go(empty):
        nonlocal count
        if not empty:
            count += 1
            return
        c = min(empty, key=lambda t: sorted(t))
        for pl in placements.get(c, ()):
            if pl <= empty:
                go(empty - pl)

    go(region)
    return count


def _sphinx_handedness():
    """In the tiling of the double sphinx, how many of the 4 pieces have the
    same handedness as the big sphinx, and how many are mirror images."""
    sph = _sphinx_cells()
    big = frozenset(_tri_scale2(sph))

    def norm(cells, flip, r):
        new = []
        for tri in cells:
            vs = []
            for a, b in tri:
                if flip:
                    a, b = b, a
                for _ in range(r):
                    a, b = -b, a + b
                vs.append((a, b))
            new.append(vs)
        ma = min(a for t in new for a, _ in t)
        mb = min(b for t in new for _, b in t)
        return frozenset(frozenset((a - ma, b - mb) for a, b in t) for t in new)

    same = {norm(sph, False, r) for r in range(6)}
    shapes = _tri_transforms(sph)
    verts = {v for t in big for v in t}
    pls = set()
    for s in shapes:
        sv = {v for t in s for v in t}
        for ax, ay in verts:
            for px, py in sv:
                pl = frozenset(frozenset((a + ax - px, b + ay - py) for a, b in t) for t in s)
                if pl <= big:
                    pls.add(pl)
    for combo in itertools.combinations(pls, 4):
        if frozenset().union(*combo) == big:
            k = sum(1 for p in combo if norm(p, False, 0) in same)
            return k, 4 - k
    return None


def check_week_170():
    # L-tromino: rep-4 (exactly one way to tile its double), and rep-9 (4 ways).
    assert _count_tilings(_scale(L_TROMINO, 2), L_TROMINO) == 1
    assert _count_tilings(_scale(L_TROMINO, 3), L_TROMINO) == 4
    # Repeating the split: 4, 16, 64 small Ls fill Ls of side 2, 4, 8.
    for lev, want in ((1, 4), (2, 16), (3, 64)):
        region, tiles = _chair_substitution(lev)
        assert len(tiles) == want == 4 ** lev
        assert all(len(t) == 3 for t in tiles)
        assert set().union(*tiles) == region and sum(len(t) for t in tiles) == len(region)
        # every piece is an L-tromino
        shapes = _orientations(L_TROMINO)
        for t in tiles:
            mx, my = min(x for x, _ in t), min(y for _, y in t)
            assert frozenset((x - mx, y - my) for x, y in t) in shapes
    # L-tetromino doubles with 4 copies (4 ways); T- and S-tetromino doubles cannot be tiled.
    assert _count_tilings(_scale(L_TETROMINO, 2), L_TETROMINO) == 4
    assert _count_tilings(_scale(T_TETROMINO, 2), T_TETROMINO) == 0
    assert _count_tilings(_scale(S_TETROMINO, 2), S_TETROMINO) == 0
    # The square tetromino (2 by 2) doubles trivially; the straight one too.
    assert _count_tilings(_scale({(0, 0), (1, 0), (0, 1), (1, 1)}, 2),
                          {(0, 0), (1, 0), (0, 1), (1, 1)}) == 1

    # Sphinx: six unit triangles; its double (24 triangles) is tiled by 4 sphinxes.
    sph = _sphinx_cells()
    assert len(sph) == 6
    big = _tri_scale2(sph)
    assert len(big) == 24
    n_tilings = _count_tri_tilings(big, sph)
    assert n_tilings >= 1
    check_week_170.sphinx_tilings = n_tilings
    assert n_tilings == 1
    assert _sphinx_handedness() == (1, 3)   # one piece as the big one, three mirrored

    # Sphinx is also rep-9: 4 ways to tile its triple with 9 sphinxes.
    assert _tri_scale(sph, 2) == big
    assert _count_tri_tilings(_tri_scale(sph, 3), sph) == 4
    # Pattern blocks on the triangle grid: the red trapezoid (3 triangles)
    # doubles in exactly one way; the yellow hexagon (6 triangles round a point)
    # cannot make a double of itself.
    trap = {frozenset([(0, 0), (1, 0), (0, 1)]), frozenset([(1, 0), (0, 1), (1, 1)]),
            frozenset([(1, 0), (2, 0), (1, 1)])}
    hexa = set()
    for i in range(-1, 3):
        for j in range(-1, 3):
            for tri in (((i, j), (i + 1, j), (i, j + 1)), ((i + 1, j), (i, j + 1), (i + 1, j + 1))):
                if (1, 1) in tri:
                    hexa.add(frozenset(tri))
    assert len(trap) == 3 and len(hexa) == 6
    assert _count_tri_tilings(_tri_scale(trap, 2), trap) == 1
    assert _count_tri_tilings(_tri_scale(hexa, 2), hexa) == 0
    # Green triangle and blue rhombus double trivially (4 copies).
    tri1 = {frozenset([(0, 0), (1, 0), (0, 1)])}
    rh = {frozenset([(0, 0), (1, 0), (0, 1)]), frozenset([(1, 0), (0, 1), (1, 1)])}
    assert _count_tri_tilings(_tri_scale(tri1, 2), tri1) == 1
    assert _count_tri_tilings(_tri_scale(rh, 2), rh) == 1

    # Paper: a 1 by sqrt2 rectangle cut in half gives two copies of itself
    # (rep-2); US letter (8.5 by 11) does not.
    r = math.sqrt(2)
    assert abs(r / (1 / 1) - (1 / (r / 2))) < 1e-12        # long/short kept
    letter = 11 / 8.5
    half = 8.5 / 5.5
    assert abs(letter - 1.294) < 1e-3 and abs(half - 1.545) < 1e-3
    # A right isosceles triangle is rep-2 (area halves, scale 1/sqrt2).
    assert abs((1 / math.sqrt(2)) ** 2 * 2 - 1) < 1e-12


def main():
    for f in (check_week_164, check_week_165, check_week_166, check_week_167,
              check_week_168, check_week_169, check_week_170):
        f()
        print(f.__name__.replace('check_', ''), 'ok')
    print('week 165 spiral cells inside:', check_week_165.cells_in)
    print('week 170 tilings of the double sphinx:', check_week_170.sphinx_tilings)


if __name__ == '__main__':
    main()
