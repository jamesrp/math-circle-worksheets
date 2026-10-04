#!/usr/bin/env python3
"""Independently check Week 2 K–1 auxiliary mathematics.

Uses only the Python standard library. Lamp targets are checked by exhaustive
edge-subset enumeration and a separate state-space BFS. Room regions are found
from an exact-rational planar arrangement, rather than using renderer geometry.
Run from any directory; the JSON report is written alongside this script.
"""

from collections import defaultdict, deque
from fractions import Fraction
from functools import cmp_to_key
from itertools import product
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "week-02-k1-aux-data.json").read_text())
OUTPUT = HERE / "week-02-k1-aux-checks.json"


def bitmask(vertices):
    return sum(1 << (v - 1) for v in vertices)


def lit_vertices(state, n):
    return [i + 1 for i in range(n) if state & (1 << i)]


def components(n, edges):
    neighbors = defaultdict(set)
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    unseen, result = set(range(1, n + 1)), []
    while unseen:
        todo, component = [min(unseen)], set()
        while todo:
            vertex = todo.pop()
            if vertex in component:
                continue
            component.add(vertex)
            todo.extend(neighbors[vertex] - component)
        unseen -= component
        result.append(sorted(component))
    return result


def bfs(n, edges, start=0, one_light=False):
    if one_light:
        assert start.bit_count() == 1
    parent = {start: None}
    distance = {start: 0}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        for edge in edges:
            candidate = state ^ bitmask(edge)
            if one_light and candidate.bit_count() != 1:
                continue
            if candidate not in parent:
                parent[candidate] = (state, list(edge))
                distance[candidate] = distance[state] + 1
                queue.append(candidate)
    return parent, distance


def path_to(parent, target):
    if target not in parent:
        return None
    reverse = []
    while parent[target] is not None:
        target, edge = parent[target]
        reverse.append(edge)
    return reverse[::-1]


def graph_checks():
    graph_report = {}
    for name, graph in DATA["graphs"].items():
        n, edges = len(graph["xy"]), graph["edges"]
        assert all(a != b and 1 <= a <= n and 1 <= b <= n for a, b in edges)
        assert len({tuple(sorted(edge)) for edge in edges}) == len(edges)
        comps = components(n, edges)
        expected = {
            state for state in range(1 << n)
            if all((state & bitmask(comp)).bit_count() % 2 == 0 for comp in comps)
        }
        multiplicities, minimum = defaultdict(int), {}
        for selected in range(1 << len(edges)):
            moves = [edge for i, edge in enumerate(edges) if selected & (1 << i)]
            state = 0
            for edge in moves:
                state ^= bitmask(edge)
            multiplicities[state] += 1
            minimum[state] = min(minimum.get(state, len(edges) + 1), len(moves))
            restored = state
            for edge in reversed(moves):
                restored ^= bitmask(edge)
            assert restored == 0, (name, selected, "undo failure")
        parent, distances = bfs(n, edges)
        assert set(multiplicities) == expected == set(parent)
        assert distances == minimum, (name, "BFS disagrees with subset minimum")
        kernel_size = 1 << (len(edges) - n + len(comps))
        assert set(multiplicities.values()) == {kernel_size}
        # Explicitly verify two applications cancel from every possible state.
        assert all((s ^ bitmask(e) ^ bitmask(e)) == s
                   for s in range(1 << n) for e in edges)
        graph_report[name] = {
            "vertices": n,
            "edges": len(edges),
            "components": comps,
            "edge_subsets_enumerated": 1 << len(edges),
            "reachable_states_from_all_off": len(parent),
            "expected_component_even_states": len(expected),
            "reduced_solutions_per_reachable_state": kernel_size,
            "maximum_shortest_length_from_all_off": max(distances.values()),
            "every_subset_undo_verified": True,
            "repeat_move_cancels_from_every_state": True,
            "BFS_and_edge_subset_minima_agree": True,
        }

    examples = []
    for task in DATA["checks"]:
        graph = DATA["graphs"][task["graph"]]
        edges = graph["edges"] + task.get("extra_edges", [])
        n, start = len(graph["xy"]), bitmask(task["start"])
        one_light = task.get("one_light", False)
        parent, distances = bfs(n, edges, start, one_light)
        for target_vertices in task["targets"]:
            target = bitmask(target_vertices)
            sequence = path_to(parent, target)
            expected_possible = not task.get("impossible", False)
            assert (sequence is not None) == expected_possible, task
            states = None
            if sequence is not None:
                state, states = start, [lit_vertices(start, n)]
                for edge in sequence:
                    state ^= bitmask(edge)
                    assert not one_light or state.bit_count() == 1
                    states.append(lit_vertices(state, n))
                assert state == target
                for edge in reversed(sequence):
                    state ^= bitmask(edge)
                assert state == start
            examples.append({
                "problem": task["problem"],
                "graph": task["graph"],
                "extra_edges": task.get("extra_edges", []),
                "start": task["start"],
                "target": target_vertices,
                "one_light_at_every_stage": one_light,
                "reachable": sequence is not None,
                "shortest_length": distances.get(target),
                "sample_shortest_edge_sequence": sequence,
                "states_during_sample": states,
            })
    return graph_report, examples


def point(values):
    return tuple(Fraction(str(value)) for value in values)


def subtract(a, b):
    return (a[0] - b[0], a[1] - b[1])


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def on_segment(p, a, b):
    return cross(subtract(p, a), subtract(b, a)) == 0 and all(
        min(a[i], b[i]) <= p[i] <= max(a[i], b[i]) for i in (0, 1)
    )


def intersections(segment1, segment2):
    a, b = segment1
    c, d = segment2
    r, s, delta = subtract(b, a), subtract(d, c), subtract(c, a)
    denominator = cross(r, s)
    if denominator == 0:
        if cross(delta, r) != 0:
            return set()
        return {p for p in (a, b, c, d) if on_segment(p, a, b) and on_segment(p, c, d)}
    t, u = cross(delta, s) / denominator, cross(delta, r) / denominator
    if 0 <= t <= 1 and 0 <= u <= 1:
        return {(a[0] + t * r[0], a[1] + t * r[1])}
    return set()


def twice_area(vertices):
    return sum(cross(a, b) for a, b in zip(vertices, vertices[1:] + vertices[:1]))


def corner_count(vertices):
    return sum(cross(subtract(p, vertices[i - 1]),
                     subtract(vertices[(i + 1) % len(vertices)], p)) != 0
               for i, p in enumerate(vertices))


def angular_comparison(vertex, a, b):
    """Order outgoing rays counterclockwise using rational arithmetic only."""
    first, second = subtract(a, vertex), subtract(b, vertex)
    half1 = 0 if first[1] > 0 or (first[1] == 0 and first[0] > 0) else 1
    half2 = 0 if second[1] > 0 or (second[1] == 0 and second[0] > 0) else 1
    if half1 != half2:
        return half1 - half2
    determinant = cross(first, second)
    return -1 if determinant > 0 else 1 if determinant < 0 else 0


def room_geometry(raw_walls):
    walls = [(point(a), point(b)) for a, b in raw_walls]
    assert all(a != b and all(0 <= coordinate <= 1 for p in (a, b) for coordinate in p)
               for a, b in walls)
    square = [point(p) for p in ([0, 0], [1, 0], [1, 1], [0, 1])]
    segments = walls + list(zip(square, square[1:] + square[:1]))
    split_points = [set(segment) for segment in segments]
    for i, segment1 in enumerate(segments):
        for j, segment2 in enumerate(segments[:i]):
            common = intersections(segment1, segment2)
            split_points[i].update(common)
            split_points[j].update(common)
    undirected = set()
    for (a, b), vertices in zip(segments, split_points):
        axis = 0 if a[0] != b[0] else 1
        ordered = sorted(vertices, key=lambda p: (p[axis] - a[axis]) / (b[axis] - a[axis]))
        for first, second in zip(ordered, ordered[1:]):
            undirected.add(tuple(sorted((first, second))))
    neighbors = defaultdict(set)
    for a, b in undirected:
        neighbors[a].add(b)
        neighbors[b].add(a)
    rotations = {
        vertex: sorted(adjacent, key=cmp_to_key(lambda a, b: angular_comparison(vertex, a, b)))
        for vertex, adjacent in neighbors.items()
    }
    # Traverse each directed edge with its face on the left. A clockwise turn
    # from the reversed incoming edge follows the same face at each vertex.
    face_of, faces = {}, []
    for a, b in sorted(undirected):
        for initial in ((a, b), (b, a)):
            if initial in face_of:
                continue
            cursor, vertices = initial, []
            face_id = len(faces)
            while cursor not in face_of:
                face_of[cursor] = face_id
                u, v = cursor
                vertices.append(u)
                rotation = rotations[v]
                cursor = (v, rotation[(rotation.index(u) - 1) % len(rotation)])
            assert cursor == initial, "face traversal merged into an existing face"
            faces.append(vertices)
    bounded = [i for i, vertices in enumerate(faces) if twice_area(vertices) > 0]
    assert sum(twice_area(faces[i]) for i in bounded) == 2, "room areas do not tile square"
    # Connected square-with-walls has F_bounded = E - V + 1.
    assert len(bounded) == len(undirected) - len(neighbors) + 1
    renumber = {old: new for new, old in enumerate(bounded)}
    adjacency = set()
    for a, b in undirected:
        left, right = face_of[(a, b)], face_of[(b, a)]
        if left in renumber and right in renumber and left != right:
            adjacency.add(tuple(sorted((renumber[left], renumber[right]))))
    assignments = {}
    for k in (2, 3):
        assignments[k] = [list(colors) for colors in product(range(k), repeat=len(bounded))
                          if all(colors[a] != colors[b] for a, b in adjacency)]
    return {
        "rooms": len(bounded),
        "vertices_in_planar_arrangement": len(neighbors),
        "edges_in_planar_arrangement": len(undirected),
        "room_adjacencies_zero_based": [list(edge) for edge in sorted(adjacency)],
        "corner_counts": sorted(corner_count(faces[i]) for i in bounded),
        "room_areas": [str(twice_area(faces[i]) / 2) for i in bounded],
        "two_symbol_assignment_count": len(assignments[2]),
        "three_symbol_assignment_count": len(assignments[3]),
        "sample_two_symbol_assignment": next(iter(assignments[2]), None),
        "sample_three_symbol_assignment": next(iter(assignments[3]), None),
        "area_and_Euler_checks_passed": True,
    }


def room_checks():
    report = {name: room_geometry(walls) for name, walls in DATA["room_maps"].items()}
    counts = {"parallel3": 4, "concurrent3": 6, "general3": 7, "five3": 5,
              "stripes": 3, "cross": 4, "tee": 3}
    for name, expected in counts.items():
        assert report[name]["rooms"] == expected, (name, report[name])
    for name in ("parallel3", "concurrent3", "general3", "five3", "stripes", "cross"):
        assert report[name]["two_symbol_assignment_count"] > 0, name
    assert report["tee"]["two_symbol_assignment_count"] == 0
    assert report["tee"]["three_symbol_assignment_count"] == 6
    assert len(report["tee"]["room_adjacencies_zero_based"]) == 3
    assert len(report["cross"]["room_adjacencies_zero_based"]) == 4, "corner-only contact became adjacency"
    one_wall_examples = {
        "two_triangles": ([[[0, 0], [1, 1]]], [3, 3]),
        "two_quadrilaterals": ([[[0, 0.5], [1, 0.5]]], [4, 4]),
        "triangle_and_pentagon": ([[[0, 0.5], [0.5, 1]]], [3, 5]),
    }
    for name, (walls, corners) in one_wall_examples.items():
        result = room_geometry(walls)
        assert result["rooms"] == 2 and result["corner_counts"] == corners
        report[name] = {"walls": walls, **result}
    return report


def main():
    graphs, examples = graph_checks()
    rooms = room_checks()
    report = {
        "id": DATA["id"],
        "date": DATA["date"],
        "status": "All mathematical assertions passed; classroom use remains unpiloted",
        "data_source": "plans/week-02-k1-aux-data.json",
        "method": {
            "graphs": "Every edge subset enumerated; independent BFS confirms reachability and minimum moves. Walk BFS retains only states with exactly one ON lamp.",
            "rooms": "Exact Fraction segment intersections, planar face traversal, area and Euler checks; adjacency requires a shared wall segment. All 2- and 3-symbol assignments enumerated.",
        },
        "graph_classifications": graphs,
        "student_targets": examples,
        "room_maps": rooms,
        "bounds_and_interpretation": {
            "one_complete_straight_wall": "Two regions when endpoints lie on boundary and the wall crosses the interior; the supplied examples have corner counts 3+3, 4+4, and 3+5.",
            "two_complete_straight_walls_maximum": 4,
            "two_wall_bound_reason": "The first wall adds one room. The second meets it at most once, hence has at most two interior pieces and adds at most two rooms. Crossing example attains 4.",
            "three_complete_straight_walls_maximum": 7,
            "three_wall_bound_reason": "The third wall meets the first two at at most two distinct points, so adds at most three rooms: 1+1+2+3=7. General3 attains 7; all totals 4 through 7 have checked examples.",
            "room_symbol_rule": "Regions sharing a nonzero-length wall have different symbols. Meeting at a point does not force different symbols.",
            "two_symbol_full_line_proof": "Give each room the parity of the number of supporting lines separating it from a fixed reference point. Crossing one wall changes exactly one sign, hence changes parity.",
            "tee_requires_three_symbols": "Its three rooms are pairwise adjacent; exhaustive enumeration gives no 2-symbol assignments and 6 assignments with three labeled symbols.",
        },
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"PASS: {len(graphs)} graph classifications, {len(examples)} target checks, {len(rooms)} room constructions")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
