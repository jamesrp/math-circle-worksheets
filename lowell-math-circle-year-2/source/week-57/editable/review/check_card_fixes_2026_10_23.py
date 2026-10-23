#!/usr/bin/env python3
"""Checks for the October 23, 2026 review-card fixes to Week 57 (plans/review/week-57.md).

Standard library only. Dots are classified by exact integer tests (on a side, or inside by
a crossing count); area is the shoelace area, so no claim below uses Pick's rule.

1. K-1 route key (fix 1, guide p. 3): every shape of four squares joined edge to edge has
   10 outline dots and none inside, except the 2 x 2 square (8 and 1); five squares give
   12, or 10 with one inside dot, and the 10 is exactly "a 2 x 2 square with one more
   square". Each inside dot means two fewer outline dots: B = 2n + 2 - 2I, and B is also
   the perimeter (the guide's bridge to Week 26). All fit the
   7 x 7-dot p. 4 grid, and two children's five squares fit a younger kit's 10 squares.
2. Joining limits (fix 3, guide p. 1, student README): a seam of several consecutive sides
   obeys I = I1 + I2 + k - 2, B = B1 + B2 - 2k + 2, Q = Q1 + Q2 (the P8 pentagon and its
   notch make the 4 x 3 rectangle, k = 3; a three-side staircase seam, k = 6); contact in
   two separate places does not (a U and a bar enclose a hole).
3. P5's (5, 4) witness (fix 10, guide p. 5): the triangle (0,0), (2,0), (1,6) has I = 5,
   B = 4, area 6 = base 2 x height 6 / 2, and fits the 0..6 board; the slender
   parallelogram kept as an alternative is also (5, 4) with area 3/5 + 24/5 + 3/5.
4. Materials (fix 6, guide p. 2): a 6 x 10 sheet of 20 mm squares and a 6 x 10 sheet with
   diagonals give 60 squares and 120 halves, the kits' 5 x 10 + 10 and 5 x 20 + 20, and the
   120 x 200 mm sheet fits inside the page's 185.9 x 242.4 mm text area.
"""
from fractions import Fraction as F
from itertools import product

FAILS = []


def check(cond, msg):
    print(('ok   ' if cond else 'FAIL ') + msg)
    if not cond:
        FAILS.append(msg)


def on_segment(p, a, b):
    (x, y), (ax, ay), (bx, by) = p, a, b
    return (bx - ax) * (y - ay) == (by - ay) * (x - ax) and min(ax, bx) <= x <= max(ax, bx) and min(ay, by) <= y <= max(ay, by)


def edges(poly):
    return list(zip(poly, poly[1:] + poly[:1]))


def inside(p, poly):
    # crossing count of a ray to the right, with half-open edges; p is not on the outline
    x, y = p
    c = False
    for (ax, ay), (bx, by) in edges(poly):
        if (ay > y) != (by > y):
            if F(x) < ax + F(y - ay) * (bx - ax) / (by - ay):
                c = not c
    return c


def area(poly):
    return abs(F(sum(a[0] * b[1] - b[0] * a[1] for a, b in edges(poly)), 2))


def record(poly):
    xs = [x for x, _ in poly]
    ys = [y for _, y in poly]
    I = B = 0
    for p in product(range(min(xs), max(xs) + 1), range(min(ys), max(ys) + 1)):
        if any(on_segment(p, a, b) for a, b in edges(poly)):
            B += 1
        elif inside(p, poly):
            I += 1
    a = area(poly)
    return I, B, (int(a) if a.denominator == 1 else a)


# 1. K-1 route: polyominoes of four and five squares
def normalise(cells):
    mx = min(x for x, _ in cells)
    my = min(y for _, y in cells)
    return frozenset((x - mx, y - my) for x, y in cells)


def free(cells):
    forms = []
    for _ in range(4):
        cells = {(-y, x) for x, y in cells}
        forms += [normalise(cells), normalise({(-x, y) for x, y in cells})]
    return min(forms, key=sorted)


def polyominoes(n):
    shapes = {frozenset({(0, 0)})}
    for _ in range(n - 1):
        shapes = {normalise(s | {c}) for s in shapes for x, y in s
                  for c in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)) if c not in s}
    return shapes


def dot_counts(cells):
    I = B = 0
    pinch = False
    xs = [x for x, _ in cells]
    ys = [y for _, y in cells]
    for x, y in product(range(min(xs), max(xs) + 2), range(min(ys), max(ys) + 2)):
        around = [(x - 1, y - 1) in cells, (x, y - 1) in cells, (x - 1, y) in cells, (x, y) in cells]
        if all(around):
            I += 1
        elif any(around):
            B += 1
            pinch |= around in ([True, False, False, True], [False, True, True, False])
    return I, B, pinch


for n in (4, 5):
    fixed = polyominoes(n)
    shapes = {free(s) for s in fixed}
    counts = {}
    for s in shapes:
        I, B, pinch = dot_counts(s)
        perimeter = sum((x + dx, y + dy) not in s for x, y in s for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        check(not pinch and B == 2 * n + 2 - 2 * I == perimeter, f'{n} squares {sorted(s)}: I = {I}, B = {B} = 2*{n} + 2 - 2I = perimeter, no pinch')
        counts.setdefault((I, B), []).append(s)
        w = max(x for x, _ in s) + 1
        h = max(y for _, y in s) + 1
        check(max(w, h) <= 6, f'{n} squares fit the 6 x 6-square p. 4 grid ({w} x {h})')
    print(f'{n} squares: {len(shapes)} free shapes, {len(fixed)} placements; records {sorted((k, len(v)) for k, v in counts.items())}')
    square = frozenset(product(range(2), range(2)))
    if n == 4:
        check(sorted(counts) == [(0, 10), (1, 8)] and counts[(1, 8)] == [free(square)],
              'four squares: B = 10 with I = 0, except only the 2 x 2 square, B = 8 with I = 1')
    else:
        with_square = {free(square | {c}) for c in ((2, 0), (2, 1), (0, 2), (1, 2), (-1, 0), (-1, 1), (0, -1), (1, -1))}
        check(sorted(counts) == [(0, 12), (1, 10)] and set(counts[(1, 10)]) == with_square and len(with_square) == 1,
              'five squares: B = 12 with I = 0, or B = 10 with I = 1 exactly for a 2 x 2 square with one more square')
check(2 * 5 <= 10, 'two children with five squares each use at most a younger kit\'s 10 intact squares')

# 2. Joining limits
def seam_dots(path):
    # every lattice dot on a path of consecutive sides
    xs = [x for x, _ in path]
    ys = [y for _, y in path]
    return [p for p in product(range(min(xs), max(xs) + 1), range(min(ys), max(ys) + 1))
            if any(on_segment(p, a, b) for a, b in zip(path, path[1:]))]


def join_check(name, p1, p2, whole, path):
    (i1, b1, a1), (i2, b2, a2), (i, b, a) = record(p1), record(p2), record(whole)
    k = len(seam_dots(path))
    q = lambda I, B: I + F(B, 2) - 1
    ok = (i == i1 + i2 + k - 2 and b == b1 + b2 - 2 * k + 2 and q(i, b) == q(i1, b1) + q(i2, b2) and a == a1 + a2)
    check(ok, f'{name}: {(i1, b1, a1)} + {(i2, b2, a2)} -> {(i, b, a)}, k = {k}; the joining formulas hold')


pentagon = [(0, 0), (4, 0), (4, 3), (2, 2), (0, 3)]
notch = [(0, 3), (2, 2), (4, 3)]
rect43 = [(0, 0), (4, 0), (4, 3), (0, 3)]
check(record(pentagon) == (5, 12, 10) and record(notch) == (0, 6, 2) and record(rect43) == (6, 14, 12),
      'P8 pentagon (5, 12, 10), notch (0, 6, 2), rectangle (6, 14, 12)')
join_check('pentagon + notch along two sides (0,3)-(2,2)-(4,3)', pentagon, notch, rect43, [(0, 3), (2, 2), (4, 3)])
lower = [(0, 0), (4, 0), (4, 2), (2, 2), (2, 1), (0, 1)]
upper = [(0, 1), (2, 1), (2, 2), (4, 2), (4, 3), (0, 3)]
stair = [(0, 1), (2, 1), (2, 2), (4, 2)]
join_check('4 x 3 rectangle cut along a three-side staircase seam', lower, upper, rect43, stair)
# contact in two separate places: a U and a bar enclose a hole
U = [(0, 0), (3, 0), (3, 2), (2, 2), (2, 1), (1, 1), (1, 2), (0, 2)]
bar = [(0, 2), (3, 2), (3, 3), (0, 3)]
(iu, bu, au), (ib, bb, ab) = record(U), record(bar)
# the union is the 3 x 3 square with the unit hole [1,2] x [1,2]: no dot strictly inside,
# 12 outer and 4 hole dots on the outline
outer = [(0, 0), (3, 0), (3, 3), (0, 3)]
hole = [(1, 1), (2, 1), (2, 2), (1, 2)]
I_union = sum(1 for p in product(range(4), repeat=2) if inside(p, outer) and not any(on_segment(p, a, b) for a, b in edges(outer))
              and not inside(p, hole) and not any(on_segment(p, a, b) for a, b in edges(hole)))
B_union = sum(1 for p in product(range(4), repeat=2) if any(on_segment(p, a, b) for a, b in edges(outer) + edges(hole)))
q_union = I_union + F(B_union, 2) - 1
check((I_union, B_union) == (0, 16) and au + ab == area(outer) - area(hole) == 8 and q_union == 7 and (iu + F(bu, 2) - 1) + (ib + F(bb, 2) - 1) == 8,
      f'U {(iu, bu, au)} and bar {(ib, bb, ab)} meet in two separate places: the union (0, 16, 8) has Q = {q_union}, not Q1 + Q2 = 8')

# 3. P5's (5, 4) witnesses
tri = [(0, 0), (2, 0), (1, 6)]
check(record(tri) == (5, 4, 6) and area(tri) == F(2 * 6, 2) and all(0 <= c <= 6 for v in tri for c in v),
      '(5, 4) triangle (0,0), (2,0), (1,6): I = 5, B = 4, area 6 = base 2 x height 6 / 2, on the 0..6 board')
par = [(0, 0), (2, 1), (6, 6), (4, 5)]
check(record(par) == (5, 4, 6) and F(3, 5) + F(24, 5) + F(3, 5) == 6, 'slender parallelogram also (5, 4), area 3/5 + 24/5 + 3/5 = 6')

# 4. Materials
squares, halves = 6 * 10, 2 * 6 * 10
check(squares == 5 * 10 + 10 and halves == 5 * 20 + 20, f'materials: {squares} squares and {halves} halves = five kits plus spares')
text_w, text_h = 215.9 - 2 * 15, 279.4 - 19 - 18
check(6 * 20 <= text_w and 10 * 20 + 25 <= text_h, f'a 120 x 200 mm sheet plus two text lines and the bar fit {text_w:.1f} x {text_h:.1f} mm')

print('PASS: all Week 57 card-fix checks' if not FAILS else f'FAIL: {len(FAILS)} checks failed')
raise SystemExit(1 if FAILS else 0)
