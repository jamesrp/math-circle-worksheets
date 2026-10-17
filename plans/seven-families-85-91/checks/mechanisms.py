"""Verify the two mechanism plans' finite examples; no PDFs or hardware tested."""

from itertools import product
from math import cos, hypot, isclose, pi, sin


def tree(initial, depth, count):
    """Each bool is the next exit; False=L, True=R, followed by a flip."""
    state = list(initial)
    outputs = []
    for _ in range(count):
        node = 0
        leaf = 0
        for _ in range(depth):
            right = state[node]
            state[node] = not right
            leaf = 2 * leaf + int(right)
            node = 2 * node + 1 + int(right)
        outputs.append(leaf)
    return outputs, state


def road(initial, m, entrance, count):
    state = list(initial)
    outputs, paths = [], []
    initial_score = sum(state)
    for chip in range(count):
        x = entrance
        path = [x]
        step_score = x + sum(state)
        while 0 < x < m:
            right = state[x - 1]
            state[x - 1] = not right
            x += 1 if right else -1
            path.append(x)
            assert x + sum(state) == step_score
            assert len(path) < 1000, "Unexpected nontermination"
        outputs.append(x == m)
        paths.append(path)
        assert m * sum(outputs) + sum(state) == (chip + 1) * entrance + initial_score
    return outputs, state, paths


def polygon_area(points):
    twice = sum(x * v - y * u for (x, y), (u, v) in zip(points, points[1:] + points[:1]))
    return abs(twice) / 2


def main():
    tree_starts = 0
    for depth in (1, 2, 3):
        count = 2 ** depth
        for initial in product((False, True), repeat=count - 1):
            outputs, final = tree(initial, depth, count)
            assert sorted(outputs) == list(range(count))
            assert tuple(final) == initial
            outputs, _ = tree(initial, depth, 30)
            for start in range(31 - count):
                assert sorted(outputs[start:start + count]) == list(range(count))
            tree_starts += 1
    assert tree([False] * 3, 2, 4)[0] == [0, 2, 1, 3]
    assert tree([False] * 7, 3, 8)[0] == [0, 4, 2, 6, 1, 5, 3, 7]
    assert all(tree(initial, 2, 2)[0] != [0, 1] for initial in product((False, True), repeat=3))
    assert all(tree(initial, 3, 2)[0] != [0, 1] for initial in product((False, True), repeat=7))

    road_starts = 0
    for m in (4, 5):
        for entrance in range(1, m):
            for initial in product((False, True), repeat=m - 1):
                outputs, _, _ = road(initial, m, entrance, 30)
                for start in range(31 - m):
                    assert sum(outputs[start:start + m]) == entrance
                road_starts += 1
    outputs, state, paths = road([False] * 3, 4, 2, 8)
    assert outputs == [False, True] * 4
    assert paths[0] == [2, 1, 0]
    assert paths[1] == [2, 3, 2, 1, 2, 3, 4]
    for entrance, expected in [(1, "LLLLR"), (2, "LLRLR"), (3, "LRLRR"), (4, "LRRRR")]:
        outputs, _, _ = road([False] * 4, 5, entrance, 5)
        assert "".join("R" if result else "L" for result in outputs) == expected
    outputs, state, _ = road([False, False, True], 4, 1, 4)
    assert outputs == [False, False, True, False]
    assert state == [True, False, False]  # block balance need not return the full state
    _, state, paths = road([True, False], 3, 2, 1)
    assert paths[0] == [2, 1, 2, 3] and state == [False, False]

    poses = 0
    half_bar = 80
    for a in range(12):
        for b in range(12):
            if a == b or (a - b) % 12 == 6:
                continue  # exclude collapsed/collinear configurations
            u = [half_bar * cos(a * pi / 6), half_bar * sin(a * pi / 6)]
            v = [half_bar * cos(b * pi / 6), half_bar * sin(b * pi / 6)]
            x, q = u, [2 * z for z in u]
            y = [2 * z + w for z, w in zip(u, v)]
            t = [z + w for z, w in zip(u, v)]
            p = [2 * z + 2 * w for z, w in zip(u, v)]
            assert all(isclose(z, 2 * w, abs_tol=1e-9) for z, w in zip(p, t))
            for start, end in [(x, q), (q, y), (y, t), (t, x)]:
                assert isclose(hypot(*(end[i] - start[i] for i in (0, 1))), half_bar)
            poses += 1
    shapes = [
        [(0, 0), (20, 0), (20, 20), (0, 20)],
        [(0, 0), (20, 0), (20, 10), (10, 10), (10, 20), (0, 20)],
        [(0, 0), (20, 0), (0, 20)],
    ]
    for shape, expected in zip(shapes, (4, 3, 2)):
        assert polygon_area(shape) / 100 == expected
        copied = [(2 * x, 2 * y) for x, y in shape]
        assert polygon_area(copied) / 100 == 4 * expected
    for point in [(140, -20), (180, -20), (180, 20), (160, 35), (140, 20)]:
        tracer = [z / 2 for z in point]
        assert 70 <= tracer[0] <= 120 and -25 <= tracer[1] <= 25
        assert 0 < hypot(*tracer) < 160
    for x, y in [(140, 130), (160, 130), (150, 150)]:
        for ox in (40, 70):
            assert 0 < hypot(x - ox, y - 140) < 160
        p = (2 * x - 40, 2 * y - 140)
        pp = (2 * x - 70, 2 * y - 140)
        assert pp[0] - p[0] == -30 and pp[1] == p[1]

    print(f"PASS: {tree_starts} complete-tree starting states, {road_starts} road/entrance starting states, {poses} ideal pantograph poses, area/coordinate examples.")
    print("Limits: finite digital examples and algebraic proofs only; hardware, print fit, PDF rendering and classroom use untested.")


if __name__ == "__main__":
    main()
