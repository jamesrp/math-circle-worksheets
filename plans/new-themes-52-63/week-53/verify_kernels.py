"""Enumerate examples independently and audit MST exchange certificates."""
import itertools
import json
from pathlib import Path


def connected(vertices, edges):
    seen = {vertices[0]}
    while True:
        old = len(seen)
        for a, b, _ in edges:
            if a in seen or b in seen:
                seen.update((a, b))
        if len(seen) == old:
            return len(seen) == len(vertices)


def path_prices(tree, start, end):
    todo = [(start, None, [])]
    while todo:
        v, parent, prices = todo.pop()
        if v == end:
            return prices
        for a, b, price in tree:
            if a == v and b != parent:
                todo.append((b, v, prices + [price]))
            elif b == v and a != parent:
                todo.append((a, v, prices + [price]))
    raise AssertionError("Disconnected candidate")


examples = {
    "cheapest_three_trap": ("ABCD", [("A", "B", 1), ("B", "C", 2), ("A", "C", 3),
                                      ("C", "D", 4), ("A", "D", 5)], 7, 1),
    "five_places_tied_triangle": ("ABCDE", [("A", "B", 1), ("B", "C", 1), ("A", "C", 1),
                                             ("C", "D", 2), ("D", "E", 2), ("C", "E", 3),
                                             ("A", "D", 5), ("B", "E", 6)], 6, 3),
    "network_vs_direct_journeys": ("ABCD", [("A", "B", 2), ("A", "C", 2), ("A", "D", 2),
                                             ("B", "C", 1), ("C", "D", 1), ("B", "D", 3)], 4, 3),
    "ties_multiple": ("ABC", [("A", "B", 1), ("B", "C", 2), ("A", "C", 2)], 3, 2),
    "ties_unique": ("ABC", [("A", "B", 1), ("A", "C", 1), ("B", "C", 2)], 2, 1),
    "two_improving_exchanges": ("ABCD", [("A", "B", 1), ("B", "C", 2), ("C", "D", 3),
                                          ("D", "A", 4), ("A", "C", 5)], 6, 1),
}
report = {"status": "research examples checked; not physical rehearsal", "examples": {}}
for name, (vertices, edges, expected_cost, expected_count) in examples.items():
    connected_sets = [t for r in range(len(edges) + 1) for t in itertools.combinations(edges, r)
                      if connected(vertices, t)]
    trees = [t for t in connected_sets if len(t) == len(vertices) - 1]
    minimum = min(sum(e[2] for e in t) for t in connected_sets)
    best = [t for t in connected_sets if sum(e[2] for e in t) == minimum]
    assert (minimum, len(best)) == (expected_cost, expected_count)
    assert all(len(t) == len(vertices) - 1 for t in best)
    for tree in trees:
        certificate = all(max(path_prices(tree, a, b)) <= price
                          for a, b, price in edges if (a, b, price) not in tree)
        assert certificate == (sum(e[2] for e in tree) == minimum)
    # Greedy selection implemented separately from subset enumeration.
    forest = []
    groups = [{v} for v in vertices]
    for a, b, price in sorted(edges, key=lambda e: e[2]):
        ga = next(g for g in groups if a in g)
        gb = next(g for g in groups if b in g)
        if ga is not gb:
            forest.append((a, b, price))
            groups.remove(ga)
            groups.remove(gb)
            groups.append(ga | gb)
    assert connected(vertices, forest)
    assert sum(e[2] for e in forest) == minimum
    report["examples"][name] = {"vertices": vertices, "edges": edges, "minimum_cost": minimum,
                               "number_of_optima": len(best), "optimal_trees": best,
                               "spanning_trees_checked": len(trees), "certificate_checked_for_all_trees": True}
out = Path(__file__).with_name("math-checks.json")
out.write_text(json.dumps(report, indent=2) + "\n")
print(out)
