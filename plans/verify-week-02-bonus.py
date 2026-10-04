#!/usr/bin/env python3
"""Exhaustively check the exact Week 2 bonus instances used by the PDF builder."""
from collections import deque
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "week-02-bonus-data.json").read_text())


def press(state, lamps):
    result = set(state)
    for lamp in lamps:
        if lamp in result:
            result.remove(lamp)
        else:
            result.add(lamp)
    return frozenset(result)


def all_sets(moves):
    for mask in range(1 << len(moves)):
        state = frozenset()
        chosen = []
        for i, move in enumerate(moves):
            if mask & (1 << i):
                state = press(state, move)
                chosen.append(i)
        yield chosen, state


def main():
    graphs = DATA["graphs"]
    result = {"do_nothing": {}, "bridge_cases": {}, "solo": {}, "prices": {}}
    for item in DATA["do_nothing"]:
        graph = graphs[item["graph"]]
        answers = [chosen for chosen, state in all_sets(graph["edges"])
                   if chosen and not state]
        assert {tuple(x) for x in answers} == {tuple(x) for x in item["expected_nonempty_sets"]}
        result["do_nothing"][item["label"]] = {
            "nonempty_sets": answers,
            "lines": [[graph["edges"][i] for i in answer] for answer in answers],
        }

    graph = graphs["bridge"]
    for case in DATA["bridge_cases"]:
        changed = set(case["start"]) ^ set(case["target"])
        answers = [chosen for chosen, state in all_sets(graph["edges"])
                   if state == changed]
        side_counts = [len(changed & set(side)) for side in graph["sides"]]
        assert answers and len(answers) == 4
        assert all((graph["bridge_index"] in answer) == case["must_press"] for answer in answers)
        assert all(bool(count % 2) == case["must_press"] for count in side_counts)
        assert case["example_edges"] in answers
        result["bridge_cases"][case["label"]] = {
            "changed_lamps": sorted(changed), "changed_counts_by_side": side_counts,
            "must_press_bridge": case["must_press"], "all_edge_sets": answers,
            "example_lines": [graph["edges"][i] for i in case["example_edges"]],
        }

    graph = graphs["ring6"]
    moves = graph["edges"] + [[graph["special_lamp"]]]
    solutions = {}
    for chosen, state in all_sets(moves):
        solutions.setdefault(state, []).append(chosen)
    assert len(solutions) == 64
    assert all(len(answers) == 2 for answers in solutions.values())
    original = {state for _, state in all_sets(graph["edges"])}
    assert len(original) == 32 and all(len(state) % 2 == 0 for state in original)
    # Check arbitrary repeated-press sequences independently with a state search.
    distance = {frozenset(): 0}
    todo = deque(distance)
    while todo:
        state = todo.popleft()
        for move in moves:
            next_state = press(state, move)
            if next_state not in distance:
                distance[next_state] = distance[state] + 1
                todo.append(next_state)
    assert len(distance) == 64
    result["solo"] = {
        "reachable_without_button": len(original), "reachable_with_button": len(solutions),
        "targets": [{"target": target,
                     "fewest_presses": distance[frozenset(target)],
                     "example_move_indices": min(solutions[frozenset(target)], key=len)}
                    for target in DATA["solo_targets"]],
        "special_button_move_index": len(graph["edges"]),
    }

    graph = graphs["priced_square"]
    answers = [{"edge_indices": chosen, "presses": len(chosen),
                "cost": sum(graph["costs"][i] for i in chosen)}
               for chosen, state in all_sets(graph["edges"])
               if state == set(DATA["priced_target"])]
    assert answers == [{"edge_indices": [0], "presses": 1, "cost": 5},
                       {"edge_indices": [1, 2, 3], "presses": 3, "cost": 3}]
    # All prices are positive. Removing a repeated pair of identical presses
    # preserves every lamp and strictly reduces both price and press count.
    assert all(cost > 0 for cost in graph["costs"])
    result["prices"] = {"all_reduced_solutions": answers,
                        "fewest_presses": min(answers, key=lambda a: a["presses"]),
                        "least_cost": min(answers, key=lambda a: a["cost"])}
    out = HERE / "week-02-bonus-checks.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print("Verified: 0/1/3 nonempty do-nothing sets; both forced bridge decisions;")
    print("all 64 solo-button targets; fewest = 1 press/cost 5, cheapest = 3 presses/cost 3.")
    print(out)


if __name__ == "__main__":
    main()
