"""Independent finite checks for the Week 62 research outline; standard library only."""
import itertools
import json
from collections import Counter, deque
from pathlib import Path


def colorings(vertices, edges, k):
    return [a for a in itertools.product(range(k), repeat=len(vertices))
            if all(a[vertices.index(u)] != a[vertices.index(v)] for u, v in edges)]


def chromatic(vertices, edges):
    return next(k for k in range(1, len(vertices) + 1) if colorings(vertices, edges, k))


def clique_number(vertices, edges):
    pairs = {frozenset(e) for e in edges}
    return max(len(s) for r in range(1, len(vertices) + 1)
               for s in itertools.combinations(vertices, r)
               if all(frozenset(e) in pairs for e in itertools.combinations(s, 2)))


def first_fit(vertices, edges, order):
    assigned = {}
    for v in order:
        forbidden = {assigned[u] for e in edges if v in e for u in e
                     if u != v and u in assigned}
        assigned[v] = next(c for c in range(1, len(vertices) + 1) if c not in forbidden)
    return assigned


graphs = {
    "P4": (list("ABCD"), ["AB", "BC", "CD"]),
    "C4": (list("ABCD"), ["AB", "BC", "CD", "DA"]),
    "diamond": (list("ABCD"), ["AB", "AC", "BC", "AD", "BD"]),
    "K4": (list("ABCD"), list(itertools.combinations("ABCD", 2))),
    "K2_3": (list("ABCDE"), [u+v for u in "AB" for v in "CDE"]),
    "C5_leaf": (list("ABCDEF"), ["AB", "BC", "CD", "DE", "EA", "AF"]),
    "C4_diagonal": (list("ABCD"), ["AB", "BC", "CD", "DA", "AC"]),
}
expected = {"P4": 2, "C4": 2, "diamond": 3, "K4": 4,
            "K2_3": 2, "C5_leaf": 3, "C4_diagonal": 3}
data = {}
for name, (vertices, edges) in graphs.items():
    chi = chromatic(vertices, edges)
    assert chi == expected[name]
    data[name] = {"vertices": vertices, "edges": [list(e) for e in edges],
                  "chromatic_number": chi, "clique_number": clique_number(vertices, edges),
                  "proper_named_color_counts": {str(k): len(colorings(vertices, edges, k))
                                                 for k in range(1, 5)}}
    if name == "P4":
        bad = first_fit(vertices, edges, list("ADBC"))
        assert bad == {"A": 1, "D": 1, "B": 2, "C": 3}
        data[name]["bad_first_fit_order"] = list("ADBC")
        data[name]["bad_first_fit_assignment"] = bad
        data[name]["all_order_color_counts"] = dict(Counter(
            max(first_fit(vertices, edges, order).values())
            for order in itertools.permutations(vertices)))
        for k in range(1, 5):
            assert len(colorings(vertices, edges, k)) == k * (k-1)**3
    if name == "diamond":
        for k in range(1, 5):
            assert len(colorings(vertices, edges, k)) == k * (k-1) * (k-2)**2


def bfs_bipartite(vertices, edges):
    assigned = {}
    for root in vertices:
        if root in assigned:
            continue
        assigned[root] = 0
        queue = deque([root])
        while queue:
            v = queue.popleft()
            for e in edges:
                if v not in e:
                    continue
                u = e[0] if e[1] == v else e[1]
                if u in assigned and assigned[u] == assigned[v]:
                    return False
                if u not in assigned:
                    assigned[u] = 1 - assigned[v]
                    queue.append(u)
    return True


def has_odd_simple_cycle(vertices, edges):
    pairs = {frozenset(e) for e in edges}
    for length in range(3, len(vertices) + 1, 2):
        for subset in itertools.combinations(vertices, length):
            for tail in itertools.permutations(subset[1:]):
                cyc = (subset[0],) + tail
                if all(frozenset((cyc[i], cyc[(i+1) % length])) in pairs
                       for i in range(length)):
                    return True
    return False


checked = 0
for n in range(1, 6):
    vertices = list(range(n))
    possible = list(itertools.combinations(vertices, 2))
    for mask in range(1 << len(possible)):
        edges = [e for i, e in enumerate(possible) if mask & (1 << i)]
        bfs = bfs_bipartite(vertices, edges)
        brute = bool(colorings(vertices, edges, 2))
        assert bfs == brute == (not has_odd_simple_cycle(vertices, edges))
        checked += 1
data["finite_theorem_check"] = {"all_labeled_simple_graphs_on_1_through_5_vertices": checked,
    "methods": ["BFS alternating labels", "exhaustive two-colorings", "exhaustive odd simple cycles"],
    "limit": "Finite check supports examples; the general theorem has a separate proof."}
path = Path(__file__).with_name("small-instances.json")
path.write_text(json.dumps(data, indent=2) + "\n")
print(f"Verified {len(graphs)} graphs and {checked} finite bipartiteness cases; wrote {path}")
