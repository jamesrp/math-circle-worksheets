#!/usr/bin/env python3
"""Exhaustive edge subsets vs independent state-space BFS for the upper catalog."""
from collections import deque
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "week-02-catalog-upper-data.json").read_text())


def structure(spec):
    if "cycle" in spec:
        n = spec["cycle"]
        return n, [(v, (v + 1) % n) for v in range(n)]
    return len(spec["xy"]), [(a - 1, b - 1) for a, b in spec["edges"]]


def mask(vertices):
    assert len(set(vertices)) == len(vertices)
    return sum(1 << (v - 1) for v in vertices)


def check_graph(spec):
    n, edges = structure(spec)
    assert all(0 <= a < n and 0 <= b < n and a != b for a, b in edges)
    assert len({tuple(sorted(e)) for e in edges}) == len(edges)
    moves = [(1 << a) | (1 << b) for a, b in edges]
    answers = {}
    for selection in range(1 << len(edges)):
        state = 0
        for i, move in enumerate(moves):
            if selection & (1 << i):
                state ^= move
        answers.setdefault(state, []).append(selection)
    distance = {0: 0}
    queue = deque([0])
    while queue:
        state = queue.popleft()
        for move in moves:
            nxt = state ^ move
            if nxt not in distance:
                distance[nxt] = distance[state] + 1
                queue.append(nxt)
    assert set(distance) == set(answers)
    assert all(distance[s] == min(a.bit_count() for a in choices)
               for s, choices in answers.items())
    # Independent connected-component test, including isolated vertices.
    unseen = set(range(n))
    components = []
    while unseen:
        component = {unseen.pop()}
        todo = list(component)
        while todo:
            v = todo.pop()
            for a, b in edges:
                w = b if a == v else a if b == v else None
                if w in unseen:
                    unseen.remove(w)
                    component.add(w)
                    todo.append(w)
        components.append(component)
    for delta in range(1 << n):
        possible = all(sum(bool(delta & (1 << v)) for v in comp) % 2 == 0
                       for comp in components)
        assert possible == (delta in answers)
    if "cycle" in spec:
        full = (1 << len(edges)) - 1
        assert all(len(choices) == 2 and choices[0] ^ choices[1] == full
                   for choices in answers.values())
        assert max(distance.values()) == n // 2
    if len(components) == 1 and len(edges) == n - 1:
        assert all(len(choices) == 1 for choices in answers.values())
    return n, edges, answers, distance


def main():
    verified = {name: check_graph(spec) for name, spec in DATA["graphs"].items()}
    report = {"cases": [], "hardest_rings": {}, "graph_count": len(verified)}
    for problem in DATA["problems"]:
        for index, case in enumerate(problem.get("cases", [])):
            n, edges, answers, distance = verified[case["graph"]]
            assert all(1 <= v <= n for v in case["start"] + case["target"])
            delta = mask(case["start"]) ^ mask(case["target"])
            solutions = answers.get(delta, [])
            if "reachable" in case:
                assert bool(solutions) == case["reachable"], (problem, case)
            if "solution_count" in case:
                assert len(solutions) == case["solution_count"], (problem, case)
            if "minimum" in case:
                assert distance[delta] == case["minimum"], (problem, case)
            report["cases"].append({
                "case": f"{problem['number']}{chr(65 + index)}",
                "graph": case["graph"], "start": case["start"], "target": case["target"],
                "changed_vertices": [v + 1 for v in range(n) if delta & (1 << v)],
                "solution_count": len(solutions), "minimum": distance.get(delta),
                "solutions": [[[a + 1, b + 1] for i, (a, b) in enumerate(edges)
                               if selection & (1 << i)] for selection in solutions],
            })
        for n in problem.get("rings", []):
            _, _, _, distance = verified[f"ring{n}"]
            maximum = max(distance.values())
            example = next(s for s, d in distance.items() if d == maximum)
            report["hardest_rings"][n] = {
                "minimum_moves": maximum,
                "example_target": [v + 1 for v in range(n) if example & (1 << v)],
            }
    (HERE / "week-02-catalog-upper-checks.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Checked {len(verified)} graphs and {len(report['cases'])} pictured puzzles.")
    for item in report["cases"]:
        print(item["case"], "solutions", item["solution_count"], "minimum", item["minimum"])
    print("Hardest rings:", report["hardest_rings"])


if __name__ == "__main__":
    main()
