#!/usr/bin/env python3
"""Owned independent finite information-partition checks for Week 84.

No worksheet implementation is imported. Worlds are strings/cells; updates
come from partitions by the information visible to each ideal reasoner.
"""
import os
import json
from collections import defaultdict
from itertools import product
from pathlib import Path


def partition(worlds, observation):
    cells = defaultdict(set)
    for world in worlds:
        cells[observation(world)].add(world)
    return cells


def determine(cell, proposition, yes, no):
    answers = {proposition(world) for world in cell}
    assert answers
    if len(answers) == 2:
        return "NOT YET"
    return yes if answers.pop() else no


def cafe_tree():
    """Branch on each public answer, never on the actual hidden card."""
    worlds = {"".join(w) for w in product("YN", repeat=3)}
    frontier = {(): worlds}
    for speaker in range(3):
        children = {}
        for history, public in frontier.items():
            private_cells = partition(public, lambda w: w[speaker])
            response_groups = defaultdict(set)
            for cell in private_cells.values():
                response = determine(cell, lambda w: w == "YYY", "YES", "NO")
                response_groups[response].update(cell)
            for response, group in response_groups.items():
                children[history + (response,)] = group
        frontier = children
    expected = {
        ("NOT YET", "NOT YET", "NO"): {"YYN"},
        ("NO", "NO", "NO"): {"NYY", "NYN", "NNY", "NNN"},
        ("NOT YET", "NO", "NO"): {"YNY", "YNN"},
        ("NOT YET", "NOT YET", "YES"): {"YYY"},
    }
    assert frontier == expected, frontier
    return {" / ".join(k): sorted(v) for k, v in frontier.items()}


def hat_response_map(public):
    per_doll = []
    for doll in range(3):
        # The doll sees exactly the other two coordinates.
        cells = partition(public, lambda w: w[:doll] + w[doll + 1:])
        by_world = {}
        for cell in cells.values():
            response = "PROVE BLUE" if all(w[doll] == "B" for w in cell) else "NOT YET"
            for world in cell:
                by_world[world] = response
        per_doll.append(by_world)
    return {w: tuple(d[w] for d in per_doll) for w in public}


def hat_tree(announcement, rounds):
    worlds = {"".join(w) for w in product("BR", repeat=3)}
    initial = worlds - {"RRR"} if announcement else worlds
    frontier = {(): initial}
    history_for_world = {}
    frontier_sizes = [sorted(len(p) for p in frontier.values())]
    for _ in range(rounds):
        children = {}
        for history, public in frontier.items():
            # Calculate ALL replies from the same public state first.
            mapping = hat_response_map(public)
            for reply, cell in partition(public, lambda w: mapping[w]).items():
                new_history = history + (reply,)
                children[new_history] = cell
                for world in cell:
                    history_for_world[world] = new_history
        frontier = children
        frontier_sizes.append(sorted(len(p) for p in frontier.values()))
    if announcement:
        for world, history in history_for_world.items():
            blue_count = world.count("B")
            assert history[:blue_count-1] == (("NOT YET",)*3,)*(blue_count-1)
            assert history[blue_count-1] == tuple("PROVE BLUE" if c == "B" else "NOT YET" for c in world)
        # All seven deals already separate after two public rounds; the
        # all-blue dolls still need the third round to publicly declare.
        assert frontier_sizes[1] == [1, 1, 1, 4]
        assert frontier_sizes[2] == [1]*7
    else:
        assert len(frontier) == 1
        only_public = next(iter(frontier.values()))
        assert only_public == initial
        assert set(hat_response_map(initial).values()) == {("NOT YET",)*3}
        # Exact fixed point: this argument extends to every later round.
    return {"world_histories": history_for_world, "public_cell_sizes": frontier_sizes}


def grid():
    public = {(a, b) for a in range(7) for b in range(7) if a != b}
    stages = [sorted(public)]
    for speaker in (0, 1, 0):
        private_cells = partition(public, lambda w: w[speaker])
        response = {key: determine(cell, lambda w: w[0] > w[1], "ALICE LARGER", "BOB LARGER") for key, cell in private_cells.items()}
        assert response[(3, 2)[speaker]] == "NOT YET"
        public = {w for w in public if response[w[speaker]] == "NOT YET"}
        stages.append(sorted(public))
    assert [len(s) for s in stages] == [42, 30, 12, 2]
    assert public == {(3, 2), (3, 4)}
    bob_private = {w for w in public if w[1] == 2}
    assert bob_private == {(3, 2)}
    # Audience still has both worlds; Bob's private filtering did not update it.
    assert len(public) == 2
    comparison_response = {w: "ALICE LARGER" if w[0] > w[1] else "BOB LARGER" for w in public}
    assert {w for w in public if comparison_response[w] == "ALICE LARGER"} == {(3, 2)}
    return {"stage_sizes": [len(s) for s in stages], "stages": stages,
            "bob_private_at_2": sorted(bob_private), "audience_after_three_ignorance_reports": sorted(public)}


def check_examples():
    cafe = {"YY", "YN", "NY", "NN"}
    cells = partition(cafe, lambda w: w[0])
    answers = {key: determine(cell, lambda w: w == "YY", "YES", "NO") for key, cell in cells.items()}
    assert {w for w in cafe if answers[w[0]] == "NO"} == {"NY", "NN"}
    hats = {"BB", "BR", "RB"}
    assert {w for w in hats if w[1] == "R"} == {"BR"}


if __name__ == "__main__":
    check_examples()
    evidence = {"status": "PASS", "cafe": cafe_tree(),
                "hats_with_announcement": hat_tree(True, 4),
                "hats_without_announcement": hat_tree(False, 4), "grid": grid()}
    output = Path(os.environ.get("INFINITY_CHECK_OUT", "math-check-results.json"))
    output.write_text(json.dumps(evidence, indent=2) + "\n")
    print("PASS: café all 8 worlds; hats all 7/8 worlds, synchronized rounds and fixed point; grid 42→30→12→2.")
    print(output)
