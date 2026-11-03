#!/usr/bin/env python3
"""Checks for draft plans weeks 125-129 (shape group B).

Standard library only. Run: python3 check_shape_b.py
Each check_week_1NN() asserts the small numbers its draft quotes.
"""

import math
from fractions import Fraction
from itertools import combinations, product

S3 = math.sqrt(3)


# ---------------------------------------------------------------- week 125
def hex_pt(x, y):
    """Point of the triangular lattice used for the hat outline."""
    return (x + 0.5 * y, S3 / 2 * y)


HAT = [(0, 0), (-1, -1), (0, -2), (2, -2), (2, -1), (4, -2), (5, -1),
       (4, 0), (3, 0), (2, 2), (0, 3), (0, 2), (-1, 2)]


def shoelace(pts):
    n = len(pts)
    return sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1]
               for i in range(n)) / 2


def inside(pt, poly):
    x, y = pt
    c = False
    n = len(poly)
    for i in range(n):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            if x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
                c = not c
    return c


def kites_of_hexagon(cx, cy):
    """Split a regular hexagon of side 2 (apothem sqrt3) into 6 kites:
    centre, edge midpoint, vertex, next edge midpoint."""
    verts = [(cx + 2 * math.cos(math.pi / 3 * k), cy + 2 * math.sin(math.pi / 3 * k))
             for k in range(6)]
    mids = [((verts[k][0] + verts[(k + 1) % 6][0]) / 2,
             (verts[k][1] + verts[(k + 1) % 6][1]) / 2) for k in range(6)]
    return [[(cx, cy), mids[k - 1], verts[k], mids[k]] for k in range(6)]


def check_week_125():
    poly = [hex_pt(*p) for p in HAT]
    area = abs(shoelace(poly))
    # Kite with sides 1, 1, sqrt3, sqrt3 and angles 60, 90, 120, 90 has area sqrt3.
    kite = kites_of_hexagon(0, 0)[0]
    kite_area = abs(shoelace(kite))
    assert abs(kite_area - S3) < 1e-9
    assert abs(area - 8 * kite_area) < 1e-9          # hat = 8 kites by area
    # Kite angles 60 + 90 + 120 + 90 = 360.
    assert 60 + 90 + 120 + 90 == 360
    # The hat is a union of exactly 8 whole kites of the hexagon-kite grid.
    a, b = hex_pt(2, 2), hex_pt(-2, 4)               # hexagon centre lattice
    count = 0
    for i in range(-4, 5):
        for j in range(-4, 5):
            cx, cy = i * a[0] + j * b[0], i * a[1] + j * b[1]
            for k in kites_of_hexagon(cx, cy):
                cen = (sum(p[0] for p in k) / 4, sum(p[1] for p in k) / 4)
                if inside(cen, poly):
                    count += 1
                    assert all(inside((cen[0] + 0.98 * (p[0] - cen[0]),
                                       cen[1] + 0.98 * (p[1] - cen[1])), poly)
                               for p in k)
    assert count == 8
    # Side count: 13 straight sides (one of length 2 = two collinear unit edges).
    lengths = [round(math.dist(poly[i], poly[(i + 1) % 13]), 6) for i in range(13)]
    assert len(lengths) == 13
    assert sorted(set(lengths)) == [1.0, round(S3, 6), 2.0]
    assert lengths.count(2.0) == 1
    # Bridges 2024 group build: 49 patches of 8 tiles, one reflected in each.
    assert 49 * 8 == 392 and 343 + 49 == 392 and Fraction(49, 392) == Fraction(1, 8)
    # Squares and regular hexagons tile with translations (period vectors).
    assert 3 * 120 == 360 and 4 * 90 == 360           # angles meeting at a vertex


# ---------------------------------------------------------------- week 126
def rect_cells(w, h, x0=0, y0=0):
    return {(x0 + x, y0 + y) for x in range(w) for y in range(h)}


SYMS = [lambda x, y: (x, y), lambda x, y: (-y, x), lambda x, y: (-x, -y),
        lambda x, y: (y, -x), lambda x, y: (-x, y), lambda x, y: (y, x),
        lambda x, y: (x, -y), lambda x, y: (-y, -x)]


def normalize(cells):
    mx = min(c[0] for c in cells)
    my = min(c[1] for c in cells)
    return frozenset((x - mx, y - my) for x, y in cells)


def placements(piece, region):
    out = set()
    for f in SYMS:
        shape = normalize({f(x, y) for x, y in piece})
        for rx, ry in region:
            for sx, sy in shape:
                dx, dy = rx - sx, ry - sy
                placed = frozenset((x + dx, y + dy) for x, y in shape)
                if placed <= region:
                    out.add(placed)
    return out


def connected(cells):
    cells = set(cells)
    if not cells:
        return False
    stack = [next(iter(cells))]
    seen = set(stack)
    while stack:
        x, y = stack.pop()
        for n in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if n in cells and n not in seen:
                seen.add(n)
                stack.append(n)
    return len(seen) == len(cells)


def check_week_126():
    # Staircase: 5 rows by 8 columns becomes 4 rows by 10 columns, two pieces.
    W, H = 8, 5
    # Cut along a staircase with steps 2 across and 1 up; slide the lower-right
    # piece 2 right and 1 up. Row 0 of the left piece is empty, so the result
    # occupies rows 1 to 4.
    left = {(x, y) for (x, y) in rect_cells(W, H) if x < 2 * y}
    right = rect_cells(W, H) - left
    moved = {(x + 2, y + 1) for x, y in right}
    assert left.isdisjoint(moved)
    assert left | moved == rect_cells(10, 4, 0, 1)
    # Two equal squares (side 1) -> four half-square triangles -> square of side sqrt2.
    assert abs(4 * 0.5 - math.sqrt(2) ** 2) < 1e-12
    # Square cut on a diagonal: two triangles with legs s make a right isosceles
    # triangle with legs s*sqrt2 and the same area s^2.
    s = 1.0
    assert abs(0.5 * (s * math.sqrt(2)) ** 2 - s * s) < 1e-12
    # 3x3 + 4x4 -> 5x5: keep the 4x4 whole; the 3x3 must fill the width-1 L border.
    big = rect_cells(5, 5)
    border = frozenset(big - rect_cells(4, 4))
    assert len(border) == 9
    # Construction with 3 pieces: L(3,3) + two dominoes.
    Lpiece = {(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)}
    rest = rect_cells(3, 3) - Lpiece
    assert rest == {(1, 1), (2, 1), (1, 2), (2, 2)}
    d1, d2 = {(1, 1), (2, 1)}, {(1, 2), (2, 2)}
    ok3 = any(not (pa & pb) and not (pa & pc) and not (pb & pc) and pa | pb | pc == border
              for pa in placements(Lpiece, border)
              for pb in placements(d1, border)
              for pc in placements(d2, border))
    assert ok3
    # No cut of the 3x3 into two connected grid pieces fills the border.
    sq = sorted(rect_cells(3, 3))
    two_ok = False
    for r in range(1, 9):
        for A in combinations(sq, r):
            A = set(A)
            B = set(sq) - A
            if not (connected(A) and connected(B)):
                continue
            for pa in placements(A, border):
                if any(pb == border - pa for pb in placements(B, border)):
                    two_ok = True
    assert not two_ok
    # Dehn: regular tetrahedron dihedral angle arccos(1/3) ~ 70.53 degrees.
    t = math.degrees(math.acos(1 / 3))
    assert abs(t - 70.5288) < 1e-3
    assert abs((360 - 5 * t) - 7.356) < 1e-2        # gap when five meet at an edge
    assert 4 * 90 == 360                             # cubes close up exactly
    # arccos(1/3)/pi is irrational (proved; cited). Here only: no fraction p/q
    # with q <= 1000 is within 1e-9.
    r = math.acos(1 / 3) / math.pi
    assert all(abs(r - round(r * q) / q) > 1e-9 for q in range(1, 1001))


# ---------------------------------------------------------------- week 127
def koch(n):
    pts = [(0.0, 0.0), (1.0, 0.0)]
    for _ in range(n):
        new = [pts[0]]
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            dx, dy = (x2 - x1) / 3, (y2 - y1) / 3
            a = (x1 + dx, y1 + dy)
            b = (x1 + 2 * dx, y1 + 2 * dy)
            c, s_ = math.cos(math.pi / 3), math.sin(math.pi / 3)
            peak = (a[0] + dx * c - dy * s_, a[1] + dx * s_ + dy * c)
            new += [a, peak, b, (x2, y2)]
        pts = new
    return pts


def boxes_hit(pts, size):
    hit = set()
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        samples = max(4, int(8 * math.dist((x1, y1), (x2, y2)) / size))
        for k in range(samples + 1):
            t = k / samples
            x, y = x1 + t * (x2 - x1), y1 + t * (y2 - y1)
            hit.add((math.floor(x / size + 1e-9), math.floor(y / size + 1e-9)))
    return len(hit)


def check_week_127():
    # Stage lengths of the Koch curve on a base of length 1: (4/3)^n.
    lens = [Fraction(4, 3) ** n for n in range(4)]
    assert lens == [1, Fraction(4, 3), Fraction(16, 9), Fraction(64, 27)]
    for n in range(4):
        pts = koch(n)
        assert len(pts) - 1 == 4 ** n
        L = sum(math.dist(p, q) for p, q in zip(pts, pts[1:]))
        assert abs(L - float(lens[n])) < 1e-9
    # Ruler of length 3^-k on stage k: exactly 4^k steps; 81 cm base example.
    assert [4 ** k for k in range(4)] == [1, 4, 16, 64]
    assert [81 * Fraction(4, 3) ** k for k in range(5)] == [81, 108, 144, 192, 256]
    assert [27 * Fraction(4, 3) ** k for k in range(4)] == [27, 36, 48, 64]
    # 27 cm base: stage k has 4^k segments of 27/3^k cm (9, 3, 1 cm for k = 1, 2, 3).
    assert [(4 ** k, Fraction(27, 3 ** k)) for k in (1, 2, 3)] == [(4, 9), (16, 3), (64, 1)]
    # Similarity dimension log 4 / log 3.
    D = math.log(4) / math.log(3)
    assert abs(D - 1.26186) < 1e-5
    # Britain, D = 1.25 (Mandelbrot 1967): halving the ruler multiplies length by 2^0.25.
    assert abs(2 ** 0.25 - 1.1892) < 1e-4
    # Halving four times: 2^(0.25*4) = 2 exactly.
    assert 2 ** (0.25 * 4) == 2
    # Box counts: straight segment doubles, filled square quadruples.
    seg = [(0.0, 0.3), (0.999, 0.3)]
    assert boxes_hit(seg, 1 / 8) == 8 and boxes_hit(seg, 1 / 16) == 16
    assert len(rect_cells(8, 8)) * 4 == len(rect_cells(16, 16))
    # Koch stage 5 on grids of 1/9 and 1/27: count ratio near 4 (about 3.5 to 4.5).
    pts = koch(5)
    n9, n27 = boxes_hit(pts, 1 / 9), boxes_hit(pts, 1 / 27)
    ratio = n27 / n9
    assert 3.3 < ratio < 4.6, (n9, n27)
    check_week_127.koch_boxes = (n9, n27)
    assert (n9, n27) == (16, 68)


# ---------------------------------------------------------------- week 128
def fair_with_cuts(beads, cuts, alternate):
    """Can the string be cut at the given positions into pieces that two
    people share equally in every colour?"""
    bounds = [0] + list(cuts) + [len(beads)]
    pieces = [beads[a:b] for a, b in zip(bounds, bounds[1:])]
    colours = set(beads)
    need = {c: beads.count(c) // 2 for c in colours}
    owners = [tuple(i % 2 for i in range(len(pieces)))] if alternate else \
        product((0, 1), repeat=len(pieces))
    for own in owners:
        got = {c: 0 for c in colours}
        for o, p in zip(own, pieces):
            if o == 0:
                for c in p:
                    got[c] += 1
        if got == need:
            return True
    return False


def min_cuts(beads, alternate=False):
    n = len(beads)
    for k in range(0, n):
        for cuts in combinations(range(1, n), k):
            if fair_with_cuts(beads, cuts, alternate):
                return k
    return None


def strings(counts):
    """All distinct strings with the given colour counts."""
    letters = ''.join(c * m for c, m in counts.items())
    out = set()

    def rec(prefix, left):
        if not any(left.values()):
            out.add(prefix)
            return
        for c in left:
            if left[c]:
                left[c] -= 1
                rec(prefix + c, left)
                left[c] += 1
    rec('', dict(counts))
    assert all(sorted(s) == sorted(letters) for s in out)
    return out


def check_week_128():
    # Two colours, 4 red and 4 blue: 70 strings, every one splits with <= 2 cuts.
    S = strings({'R': 4, 'B': 4})
    assert len(S) == 70
    m = {s: min_cuts(s) for s in S}
    assert max(m.values()) == 2
    one_or_less = sum(1 for v in m.values() if v <= 1)
    check_week_128.one_cut_share = (one_or_less, len(S))
    # One cut works exactly when the first 4 beads hold 2 red: C(4,2)^2 = 36.
    assert one_or_less == math.comb(4, 2) ** 2 == 36
    assert m['RRRRBBBB'] == 2 and m['RBRBRBRB'] == 1
    # Sliding window: some run of exactly half the beads holds exactly half
    # of each colour, for every two-colour string with even counts (small sizes).
    for r, b in [(2, 2), (4, 2), (4, 4), (6, 4), (2, 6)]:
        for s in strings({'R': r, 'B': b}):
            n = len(s)
            assert any(s[i:i + n // 2].count('R') == r // 2 for i in range(n // 2 + 1))
    # Three colours: k = 3 cuts always enough, even with alternate sharing,
    # and blocks RRBBGG-style need all 3.
    for counts in [{'R': 2, 'B': 2, 'G': 2}, {'R': 4, 'B': 2, 'G': 2}]:
        worst = 0
        for s in strings(counts):
            assert min_cuts(s, alternate=True) <= 3
            worst = max(worst, min_cuts(s))
        assert worst == 3
    assert min_cuts('RRBBGG') == 3 and min_cuts('RRRRBBGG') == 3
    assert len(strings({'R': 2, 'B': 2, 'G': 2})) == 90


# ---------------------------------------------------------------- week 129
def check_week_129():
    import random
    rng = random.Random(129)
    # Square table, feet at angles th, th+90, th+180, th+270 on a circle of radius 1.
    # Feet lie in one plane exactly when h1 + h3 = h2 + h4 (diagonal midpoints agree).
    # g(th) = h1 + h3 - h2 - h4 satisfies g(th + 90) = -g(th), so g has a zero in [0, 90].
    for trial in range(200):
        terms = [(rng.uniform(-1, 1), rng.uniform(0, 3), rng.uniform(0, 3),
                  rng.uniform(0, 6.3)) for _ in range(6)]

        def ground(x, y):
            return sum(a * math.sin(p * x + q * y + ph) for a, p, q, ph in terms)

        def g(th):
            h = [ground(math.cos(th + k * math.pi / 2), math.sin(th + k * math.pi / 2))
                 for k in range(4)]
            return h[0] + h[2] - h[1] - h[3]

        for th in (0.0, 0.3, 1.1):
            assert abs(g(th + math.pi / 2) + g(th)) < 1e-9
        a, b = 0.0, math.pi / 2
        ga = g(a)
        if ga == 0:
            continue
        for _ in range(60):
            mid = (a + b) / 2
            if (g(mid) > 0) == (ga > 0):
                a = mid
            else:
                b = mid
        assert abs(g(a)) < 1e-6 and 0 <= a <= math.pi / 2
    # Planarity test: corners of a tilted plane satisfy h1 + h3 = h2 + h4.
    plane = lambda x, y: 0.2 * x - 0.1 * y + 3
    hs = [plane(math.cos(k * math.pi / 2), math.sin(k * math.pi / 2)) for k in range(4)]
    assert abs(hs[0] + hs[2] - hs[1] - hs[3]) < 1e-12
    # Map on map: a 28 x 21.6 cm map and a half-size copy turned a quarter turn
    # counterclockwise, placed so the copy's image of the map's lower-left corner
    # sits at c = (16, 4) cm. Copy point of map point p is c + R(p/2), with
    # R(x, y) = (-y, x). The copy then covers x in [5.2, 16], y in [4, 18]: on the map.
    cx, cy = Fraction(16), Fraction(4)
    W, H = Fraction(28), Fraction(216, 10)
    corners = [(cx - y / 2, cy + x / 2) for x in (0, W) for y in (0, H)]
    assert min(c[0] for c in corners) == Fraction(26, 5) and max(c[0] for c in corners) == 16
    assert min(c[1] for c in corners) == 4 and max(c[1] for c in corners) == 18
    # Fixed point: x = cx - y/2, y = cy + x/2  ->  x (1 + 1/4) = cx - cy/2.
    x = (cx - cy / 2) / Fraction(5, 4)
    y = cy + x / 2
    assert (x, y) == (Fraction(56, 5), Fraction(48, 5))      # (11.2, 9.6) cm
    assert (cx - y / 2, cy + x / 2) == (x, y)
    # Iterating "find where this spot is shown on the copy" converges (scale 1/2).
    px, py = Fraction(0), Fraction(0)
    for _ in range(30):
        px, py = cx - py / 2, cy + px / 2
    assert abs(px - x) < Fraction(1, 10 ** 6) and abs(py - y) < Fraction(1, 10 ** 6)
    # Monk: up 6:00-18:00 and down 6:00-18:00 next day; any up and down schedules
    # cross. Discrete check with random monotone height lists.
    for _ in range(200):
        up = sorted(rng.uniform(0, 1) for _ in range(11))
        up[0], up[-1] = 0.0, 1.0
        down = sorted((rng.uniform(0, 1) for _ in range(11)), reverse=True)
        down[0], down[-1] = 1.0, 0.0
        diffs = [u - d for u, d in zip(up, down)]
        assert diffs[0] < 0 < diffs[-1]
        assert any(d1 <= 0 <= d2 for d1, d2 in zip(diffs, diffs[1:]))


def main():
    for f in (check_week_125, check_week_126, check_week_127,
              check_week_128, check_week_129):
        f()
        print(f.__name__.replace('check_', ''), 'ok')
    print('week 127 Koch boxes at 1/9 and 1/27:', check_week_127.koch_boxes)
    print('week 128 strings of RRRRBBBB splittable with <= 1 cut:',
          check_week_128.one_cut_share)


if __name__ == '__main__':
    main()
