#!/usr/bin/env python3
"""Independent finite checks for the Week 1 back-pocket ribbon extensions.

Only the Python standard library is needed. Run this file directly to verify
the claims and write week-01-extension-checks.json next to it. It does not
import the earlier lesson's enumerator or change any existing lesson data.

H(1,a,b) has sides 1,a,b,1,a,b. Its tilings correspond to words containing a R's
and b L's; a local flip swaps adjacent unequal letters. We verify that geometry
for 1 <= a,b <= 4, as well as the distance formula and shortest-route counts.
The finite checks support, but do not replace, the general arguments below.

Distance proof: label the L's from left to right, with starting positions p_i
and target positions q_i. They can never pass one another, and each flip moves
one L by one position, so at least sum(abs(p_i-q_i)) flips are necessary.
First move every left-moving L to its target, in increasing label order; then
move every right-moving L to its target, in decreasing label order. In the
first phase earlier L's lie strictly left of the next target; in the second
phase later L's lie strictly right of the next target. Thus no L blocks a move,
and every move contributes to the necessary total. The lower bound is attained.

For RRRLLL -> LLLRRR, each L crosses three R's, so every shortest route has nine
moves. If x_i counts crossings made by the i-th L, the legal states satisfy
3 >= x_1 >= x_2 >= x_3 >= 0. Add the route counts of all immediate predecessors
to get the route count of each state. This produces 42 at (3,3,3).
"""

from collections import deque
from itertools import combinations, product
from math import atan2, comb, sqrt
import json
from pathlib import Path


def region(a, b):
    """Unit triangles in H(1,a,b), using exact integer centroid tests."""
    polygon = ((0, 0), (1, 0), (1, a), (1-b, a+b), (-b, a+b), (-b, b))

    def inside(vertices):
        sx = sum(x for x, _ in vertices)
        sy = sum(y for _, y in vertices)
        return all((y[0]-x[0])*(sy-3*x[1]) -
                   (y[1]-x[1])*(sx-3*x[0]) >= 0
                   for x, y in zip(polygon, polygon[1:]+polygon[:1]))

    cells = []
    for u in range(-b-1, 2):
        for v in range(-1, a+b+1):
            for triangle in (((u, v), (u+1, v), (u, v+1)),
                             ((u+1, v), (u+1, v+1), (u, v+1))):
                if inside(triangle):
                    cells.append(frozenset(triangle))
    return cells


def tilings(cells):
    """Exact-cover enumeration by pairing triangles across shared edges."""
    neighbors = {i: {j for j in range(len(cells))
                     if len(cells[i] & cells[j]) == 2}
                 for i in range(len(cells))}

    def visit(remaining, pairs):
        if not remaining:
            yield frozenset(pairs)
            return
        i = min(remaining, key=lambda k: len(neighbors[k] & remaining))
        for j in sorted(neighbors[i] & remaining):
            yield from visit(remaining-{i, j}, pairs+[tuple(sorted((i, j)))])

    return list(visit(set(neighbors), []))


def ribbon_details(cells, tiling):
    """Follow opposite horizontal rhombus edges from the unique bottom edge."""
    tile_edges = []
    for i, j in tiling:
        boundary = cells[i] | cells[j]
        horizontal = [frozenset((p, q)) for p, q in combinations(boundary, 2)
                      if p[1] == q[1] and abs(p[0]-q[0]) == 1
                      and frozenset((p, q)) != cells[i] & cells[j]]
        if horizontal:
            assert len(horizontal) == 2
            tile_edges.append(horizontal)

    edge = frozenset(((0, 0), (1, 0)))
    visited = set()
    word = ""
    path = [(0.5, 0)]
    while True:
        options = [(i, pair) for i, pair in enumerate(tile_edges)
                   if edge in pair and i not in visited]
        if not options:
            break
        assert len(options) == 1
        i, pair = options[0]
        next_edge = next(e for e in pair if e != edge)
        # Midpoints doubled in the axial basis; the physical x coordinate is
        # u+v/2, so deltas (0,2) and (-2,2) mean up-right and up-left.
        delta = tuple(sum(p[k] for p in next_edge)-sum(p[k] for p in edge)
                      for k in (0, 1))
        assert delta in ((0, 2), (-2, 2))
        word += "R" if delta == (0, 2) else "L"
        path.append(tuple(sum(p[k] for p in next_edge)/2 for k in (0, 1)))
        visited.add(i)
        edge = next_edge
    assert len(visited) == len(tile_edges)
    return {"word": word, "path_midpoints": path}


def ribbon(cells, tiling):
    return ribbon_details(cells, tiling)["word"]


def word_neighbors(word):
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            yield word[:i]+word[i+1]+word[i]+word[i+2:]


def l_positions(word):
    return [i+1 for i, letter in enumerate(word) if letter == "L"]


def rank(word):
    return sum(left == "L" and right == "R"
               for i, left in enumerate(word) for right in word[i+1:])


def distances_and_counts(start):
    distances = {start: 0}
    counts = {start: 1}
    queue = deque([start])
    while queue:
        word = queue.popleft()
        for nxt in word_neighbors(word):
            if nxt not in distances:
                distances[nxt] = distances[word]+1
                counts[nxt] = 0
                queue.append(nxt)
            if distances[nxt] == distances[word]+1:
                counts[nxt] += counts[word]
    return distances, counts


def check_board(a, b):
    cells = region(a, b)
    arrangements = tilings(cells)
    words = [ribbon(cells, tiling) for tiling in arrangements]
    expected = {"".join("L" if i in places else "R" for i in range(a+b))
                for places in combinations(range(a+b), b)}
    assert len(cells) == 2*(a*b+a+b)
    assert len(arrangements) == len(set(words)) == comb(a+b, a)
    assert set(words) == expected

    geometric_edges = set()
    for i, j in combinations(range(len(arrangements)), 2):
        removed = arrangements[i]-arrangements[j]
        added = arrangements[j]-arrangements[i]
        if len(removed) != 3 or len(added) != 3:
            continue
        involved = {k for pair in removed for k in pair}
        if len(involved) == 6 and len(set.intersection(*(set(cells[k])
                                                        for k in involved))) == 1:
            geometric_edges.add(frozenset((words[i], words[j])))
    word_edges = {frozenset((word, neighbor)) for word in words
                  for neighbor in word_neighbors(word)}
    assert geometric_edges == word_edges

    for word in words:
        distances, _ = distances_and_counts(word)
        assert set(distances) == expected
        for other, distance in distances.items():
            assert distance == sum(abs(x-y) for x, y in
                                   zip(l_positions(word), l_positions(other)))
    return len(arrangements), len(word_edges)


def crossing_recurrence(a, b):
    counts = {(0,)*b: 1}
    for total in range(1, a*b+1):
        for state in product(range(a+1), repeat=b):
            if sum(state) != total or any(state[i] < state[i+1]
                                          for i in range(b-1)):
                continue
            counts[state] = sum(counts.get(tuple(value-(i == j)
                                                for i, value in enumerate(state)), 0)
                                for j in range(b) if state[j])
    return counts


def geometry_export():
    """H133 polygons and ribbon paths in the same axial basis as the lesson."""
    a = b = 3
    cells = region(a, b)
    arrangements = tilings(cells)
    records = []
    for arrangement in arrangements:
        record = ribbon_details(cells, arrangement)
        record["rank"] = rank(record["word"])
        record["neighbors"] = sorted(word_neighbors(record["word"]))
        record["pairs"] = sorted(arrangement)
        record["tiles"] = []
        for i, j in sorted(arrangement):
            points = cells[i] | cells[j]
            center = tuple(sum(p[k] for p in points)/4 for k in (0, 1))
            ordered = sorted(points, key=lambda p: atan2(
                (p[1]-center[1])*sqrt(3)/2,
                p[0]-center[0]+(p[1]-center[1])/2))
            record["tiles"].append({"triangles": [i, j], "vertices": ordered})
        records.append(record)
    records.sort(key=lambda item: (item["rank"], item["word"]))
    for i, record in enumerate(records):
        record["label"] = chr(65+i)
        # Crossing counts of the first, second, and third L, from left to right.
        record["crossings"] = [a+i-p for i, p in enumerate(l_positions(record["word"]), 1)]
    recurrence = crossing_recurrence(a, b)
    table = [{"state": state, "rank": sum(state), "routes": count}
             for state, count in sorted(recurrence.items(), key=lambda pair: (sum(pair[0]), pair[0]))]
    return {
        "sides": [1, a, b, 1, a, b],
        "coordinate_basis": "(u+v/2, sqrt(3)*v/2)",
        "polygon": [(0, 0), (1, 0), (1, a), (1-b, a+b), (-b, a+b), (-b, b)],
        "triangles": [{"id": i, "vertices": sorted(cell),
                       "up": sum(p[1] == min(v for _, v in cell) for p in cell) == 2}
                      for i, cell in enumerate(cells)],
        "tilings": records,
        "route_recurrence": table,
        "equal_rank_example": ["LRRRLL", "RLRRLL", "RRLRLL", "RRLLRL", "RRLLLR"],
        "verification": {"rhombi": 15, "tilings": 20, "flip_edges": 30,
                         "diameter": 9, "shortest_extreme_routes": 42},
    }


def main():
    for a, b in product(range(1, 5), repeat=2):
        count, edges = check_board(a, b)
        if (a, b) == (3, 3):
            print(f"H(1,3,3): 15 rhombi, {count} tilings, {edges} flip edges.")

    start, finish = "RRRLLL", "LLLRRR"
    distances, routes = distances_and_counts(start)
    assert distances[finish] == 9
    assert routes[finish] == 42
    recurrence = crossing_recurrence(3, 3)
    assert len(recurrence) == 20
    assert recurrence[(3, 3, 3)] == routes[finish]

    example = ["LRRRLL", "RLRRLL", "RRLRLL", "RRLLRL", "RRLLLR"]
    assert rank(example[0]) == rank(example[-1]) == 3
    assert distances_and_counts(example[0])[0][example[-1]] == 4
    assert all(nxt in set(word_neighbors(word)) for word, nxt in zip(example, example[1:]))
    print("Verified the word/tiling bijection and flip correspondence for all 1 <= a,b <= 4.")
    print("Verified every pairwise distance against the L-position formula on these boards.")
    print("Extreme H(1,3,3) distance: 9; shortest routes: 42.")
    print("Equal rank 3, distance 4: " + " -> ".join(example))
    print("Route-count checkpoints:", {state: recurrence[state] for state in
          ((2, 2, 2), (3, 2, 1), (3, 3, 0), (3, 2, 2), (3, 3, 1), (3, 3, 2), (3, 3, 3))})
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(geometry_export(), indent=2)+"\n")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
