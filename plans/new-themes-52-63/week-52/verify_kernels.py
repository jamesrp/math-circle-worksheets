"""Independent finite checks of the research examples; no student tasks fixed."""
import itertools
import json
import math
from pathlib import Path


def components(m, n, braces):
    adj = [set() for _ in range(m + n)]
    for i, j in braces:
        adj[i].add(m + j)
        adj[m + j].add(i)
    labels = [-1] * (m + n)
    k = 0
    for start in range(m + n):
        if labels[start] >= 0:
            continue
        labels[start] = k
        todo = [start]
        while todo:
            v = todo.pop()
            for w in adj[v]:
                if labels[w] < 0:
                    labels[w] = k
                    todo.append(w)
        k += 1
    return k, labels


def all_subsets(items):
    for size in range(len(items) + 1):
        yield from itertools.combinations(items, size)


def rotated(v, angle):
    x, y = v
    return (x * math.cos(angle) - y * math.sin(angle),
            x * math.sin(angle) + y * math.cos(angle))


def placement(m, n, labels, angles):
    h = [rotated((1, 0), angles[labels[m + j]]) for j in range(n)]
    v = [rotated((0, 1), angles[labels[i]]) for i in range(m)]
    return {(i, j): (sum(w[0] for w in h[:j]) + sum(w[0] for w in v[:i]),
                     sum(w[1] for w in h[:j]) + sum(w[1] for w in v[:i]))
            for i in range(m + 1) for j in range(n + 1)}


def distance(p, q):
    return math.dist(p, q)


report = {"status": "research examples checked; not physical rehearsal", "grids": []}
for m, n in [(2, 2), (2, 3), (3, 3)]:
    cells = list(itertools.product(range(m), range(n)))
    rigid = [b for b in all_subsets(cells) if components(m, n, b)[0] == 1]
    minimum = min(map(len, rigid))
    count = sum(len(b) == minimum for b in rigid)
    assert minimum == m + n - 1
    assert count == m ** (n - 1) * n ** (m - 1)
    report["grids"].append({"rows": m, "columns": n, "minimum": minimum,
                            "minimum_rigid_sets": count,
                            "all_sets_at_minimum_size": math.comb(m * n, minimum),
                            "all_rigid_sets": len(rigid)})

braces = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)]
k, labels = components(3, 3, braces)
assert k == 2
assert {i for i, _ in braces} == {0, 1, 2}
assert {j for _, j in braces} == {0, 1, 2}
p0 = placement(3, 3, labels, [0, 0])
p1 = placement(3, 3, labels, [0, 0.2])
bars = ([((i, j), (i, j + 1)) for i in range(4) for j in range(3)] +
        [((i, j), (i + 1, j)) for i in range(3) for j in range(4)] +
        [((i, j), (i + 1, j + 1)) for i, j in braces])
err = max(abs(distance(p0[a], p0[b]) - distance(p1[a], p1[b])) for a, b in bars)
assert err < 1e-12
changed = abs(distance(p0[0, 2], p0[1, 3]) - distance(p1[0, 2], p1[1, 3]))
assert changed > 0.01
report["covered_but_flexible_3x3"] = {"braces_zero_based": braces, "components": k,
                                      "nontrivial_first_order_modes": k - 1,
                                      "finite_bar_length_max_error": err,
                                      "unbraced_diagonal_length_change": changed}
out = Path(__file__).with_name("math-checks.json")
out.write_text(json.dumps(report, indent=2) + "\n")
print(out)
