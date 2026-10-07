#!/usr/bin/env python3
"""Exact independent checks of the final Week 78 examples and guide answers.

Coordinates below were transcribed from the final PDF and cross-checked against
its plotted source coordinates. No student checker or source module is imported.
Pairwise ray solving uses exact rational arithmetic; it does not prove the
all-real theorem. The guide supplies the separate geometric proof.
"""
from fractions import Fraction as F
from itertools import product

DIRECTIONS = ((1, 0), (0, 1), (-1, -1))
REVERSED = tuple((-x, -y) for x, y in DIRECTIONS)


def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def move(p, t, u):
    return tuple(F(a) + t * b for a, b in zip(p, u))


def on_ray(p, start, direction):
    delta = sub(p, start)
    i = next(i for i, value in enumerate(direction) if value)
    t = F(delta[i]) / direction[i]
    return t >= 0 and move(start, t, direction) == p


def intersection(p, q, directions=DIRECTIONS):
    """Return (isolated points, closed rays), solving all nine arm pairs."""
    points, rays = set(), set()
    for u, v in product(directions, repeat=2):
        delta, determinant = sub(q, p), cross(u, v)
        if determinant:
            t = F(cross(delta, v)) / determinant
            s = F(cross(delta, u)) / determinant
            if t >= 0 and s >= 0:
                points.add(move(p, t, u))
        elif cross(delta, u) == 0:
            # The three directions in either family have no opposite pairs.
            assert u == v
            i = next(i for i, value in enumerate(u) if value)
            k = F(delta[i]) / u[i]
            rays.add((move(p, max(F(0), k), u), u))
    points = {x for x in points if not any(on_ray(x, a, u) for a, u in rays)}
    return points, rays


def point(x, y):
    return ({(F(x), F(y))}, set())


def ray(x, y, u):
    return (set(), {((F(x), F(y)), u)})


def family(j):
    return (set(), {(tuple(map(F, j)), u) for u in DIRECTIONS})


def on_line(p, j):
    scores = (F(p[0]) - j[0], F(p[1]) - j[1], F(0))
    return scores.count(min(scores)) >= 2


def predicted_intersection(a, b):
    """The guide's classification, independently checked by the ray solver."""
    x, y = a
    p, q = sub(b, a)
    if p == q == 0:
        return family(a)
    if p == 0:
        return ray(x, y + max(0, q), (0, 1))
    if q == 0:
        return ray(x + max(0, p), y, (1, 0))
    if p == q:
        return ray(x + min(0, p), y + min(0, p), (-1, -1))
    if 0 < p < q:
        z = (0, q - p)
    elif 0 < q < p:
        z = (p - q, 0)
    elif p < 0 < q:
        z = (0, q)
    elif q < 0 < p:
        z = (p, 0)
    elif p < q < 0:
        z = (q, q)
    else:
        assert q < p < 0
        z = (p, p)
    return point(x + z[0], y + z[1])


def reflect(result):
    points, rays = result
    return ({(-x, -y) for x, y in points},
            {((-x, -y), (-u, -v)) for (x, y), (u, v) in rays})


def main():
    # Opening comparison and translated launch example.
    assert on_line((4, 2), (2, 2))
    assert not on_line((4, 4), (2, 2))
    assert on_line((5, 2), (3, 2))
    print('Opening: (4,2) is on L(2,2); (4,4) is off; launch translation checked.')

    cases = [
        ('P1 top: one point', (4, 4), (6, 5), point(5, 4)),
        ('P1 top: east ray', (4, 4), (6, 4), ray(6, 4, (1, 0))),
        ('P1 top: north ray', (4, 4), (4, 6), ray(4, 6, (0, 1))),
        ('P1 top: southwest ray', (4, 4), (6, 6), ray(4, 4, (-1, -1))),
        ('P1 top: same line', (4, 4), (4, 4), family((4, 4))),
        ('P1 bottom left', (2, 2), (6, 5), point(3, 2)),
        ('P1 bottom right', (2, 2), (5, 6), point(2, 3)),
        ('P2 top left', (2, 5), (6, 2), point(6, 5)),
        ('P2 top right', (3, 2), (3, 6), ray(3, 6, (0, 1))),
        ('P2 bottom left', (2, 4), (6, 4), ray(6, 4, (1, 0))),
        ('P2 bottom right', (2, 2), (6, 6), ray(2, 2, (-1, -1))),
        ('P6 cropped picture', (2, 7), (10, 5), point(10, 7)),
    ]
    for name, a, b, answer in cases:
        actual = intersection(a, b)
        assert actual == answer, (name, actual, answer)
        for p in actual[0]:
            assert on_line(p, a) and on_line(p, b)
        print(f'{name}: {actual}')

    inverse = [
        ('P4 left', (2, 5), (6, 2), point(2, 2)),
        ('P4 right', (2, 2), (6, 5), point(5, 5)),
        ('P5 left', (2, 4), (6, 4), ray(2, 4, (-1, 0))),
        ('P5 middle', (3, 2), (3, 6), ray(3, 2, (0, -1))),
        ('P5 right', (2, 2), (5, 5), ray(5, 5, (1, 1))),
    ]
    for name, p, q, answer in inverse:
        actual = intersection(p, q, REVERSED)
        assert actual == answer, (name, actual, answer)
        for j in actual[0]:
            assert on_line(p, j) and on_line(q, j)
        for start, direction in actual[1]:
            for t in (F(0), F(1, 2), F(3), F(100)):
                j = move(start, t, direction)
                assert on_line(p, j) and on_line(q, j)
        print(f'{name}: junction set {actual}')

    # Fractional and negative examples audit every boundary and all six sectors.
    grid = tuple(product((F(i, 2) for i in range(-4, 5)), repeat=2))
    count = 0
    for a, b in product(grid, repeat=2):
        actual = intersection(a, b)
        assert actual == predicted_intersection(a, b), (a, b, actual)
        inverse_actual = intersection(a, b, REVERSED)
        inverse_expected = reflect(predicted_intersection(
            (-a[0], -a[1]), (-b[0], -b[1])))
        assert inverse_actual == inverse_expected
        if a != b:
            assert len(actual[0]) == 1 if not actual[1] else len(actual[1]) == 1
            assert len(inverse_actual[0]) == 1 if not inverse_actual[1] else len(inverse_actual[1]) == 1
        count += 1
    print(f'PASS: all 17 answer cases and opening examples; {count} line pairs and')
    print(f'{count} inverse pairs checked exactly. Finite audit only; see the geometric proof.')


if __name__ == '__main__':
    main()
