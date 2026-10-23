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


def replies(public, world, n):
    """Each doll's reply in `world` against the unchanged shared set `public`."""
    out = []
    for doll in range(n):
        view = {w for w in public if w[:doll] + w[doll + 1:] == world[:doll] + world[doll + 1:]}
        out.append("PROVE BLUE" if all(w[doll] == "B" for w in view) else "NOT YET")
    return tuple(out)


def play(actual, n, announcement=True, rounds=6):
    """Rounds of simultaneous replies: the cards left after each round, and the round
    in which each doll first proves blue."""
    public = {"".join(w) for w in product("BR", repeat=n)}
    if announcement:
        public.discard("R" * n)
    left, first_proof = [], {}
    for r in range(1, rounds + 1):
        said = replies(public, actual, n)
        for doll, reply in enumerate(said):
            if reply == "PROVE BLUE":
                first_proof.setdefault(doll, r)
        public = {w for w in public if replies(public, w, n) == said}
        left.append(sorted(public))
    return left, first_proof


def card_fixes():
    """Checks for the October 23 review-card revision."""
    evidence = {}
    # Page 2's worked round: two dolls, deal RB, shared cards BB, BR, RB.
    two = {"BB", "BR", "RB"}
    assert replies(two, "RB", 2) == ("NOT YET", "PROVE BLUE")
    assert replies(two, "BB", 2) == ("NOT YET", "NOT YET")
    assert replies(two, "BR", 2) == ("PROVE BLUE", "NOT YET")
    assert {w for w in two if w[1] == "B"} == {"BB", "RB"} and {w for w in two if w[0] == "R"} == {"RB"}
    assert {w for w in two if replies(two, w, 2) == replies(two, "RB", 2)} == {"RB"}
    # Problem 2: the cards left after each round (guide p. 3).
    left = {deal: play(deal, 3)[0][:2] for deal in ("BRR", "BBR", "BBB")}
    assert left["BRR"][0] == ["BRR"]
    assert left["BBR"][0] == left["BBB"][0] == ["BBB", "BBR", "BRB", "RBB"]
    assert left["BBR"][1] == ["BBR"] and left["BBB"][1] == ["BBB"]
    evidence["problem_2_cards_left"] = left
    # Problem 3, the printed reading: group deals by each doll's reply.
    deals = sorted({"".join(w) for w in product("BR", repeat=3)} - {"RRR"})
    def histories(key):
        out = {}
        for d in deals:
            cards = set(deals)
            h = []
            for _ in range(2):
                said = replies(cards, d, 3)
                h.append(key(said))
                cards = {w for w in cards if replies(cards, w, 3) == said}
            out[d] = h
        return out
    by_doll = histories(lambda said: said)
    groups_1 = sorted(sorted(d for d in deals if by_doll[d][0] == by_doll[e][0]) for e in deals)
    assert sorted(set(map(tuple, groups_1))) == sorted([("BRR",), ("RBR",), ("RRB",), ("BBB", "BBR", "BRB", "RBB")])
    assert len({tuple(h) for h in by_doll.values()}) == 7          # yes: all separated by round 2
    # The other reading the card warned about: which replies appear, not who gave them.
    by_count = histories(lambda said: tuple(sorted(said)))
    assert by_count["BRR"] == by_count["RBR"] == by_count["RRB"]   # never separated: the answer would be no
    assert by_count["BBR"] == by_count["BRB"] == by_count["RBB"]
    evidence["problem_3_round_1_groups"] = sorted(set(map(tuple, groups_1)))
    # Problem 4 and the overview: without the announcement nothing is removed; the BBB chain.
    left_none, proofs_none = play("BBB", 3, announcement=False)
    assert all(len(cards) == 8 for cards in left_none) and not proofs_none
    everything = {"".join(w) for w in product("BR", repeat=3)}
    assert {w for w in everything if w[1:] == "BB"} == {"BBB", "RBB"}       # doll 1 in BBB allows RBB
    assert {w for w in everything if w[0] + w[2] == "RB"} == {"RBB", "RRB"}  # doll 2 in RBB allows RRB
    assert {w for w in everything if w[:2] == "RR"} == {"RRB", "RRR"}        # doll 3 in RRB allows RRR
    # Return visit: four dolls, 15 cards; k blue dolls prove together in round k.
    for world in sorted({"".join(w) for w in product("BR", repeat=4)} - {"RRRR"}):
        _, proofs = play(world, 4)
        k = world.count("B")
        assert proofs == {i: k for i, c in enumerate(world) if c == "B"}, (world, proofs)
    assert play("BBBB", 4)[1] == {0: 4, 1: 4, 2: 4, 3: 4} and play("BBBR", 4)[1] == {0: 3, 1: 3, 2: 3}
    # K-1 route: the two-person café; deals sorted by conversation.
    def cafe2(deal):
        first = "NOT YET" if deal[0] == "Y" else "NO"
        second = "NO" if first == "NO" else ("YES" if deal[1] == "Y" else "NO")
        return (first, second)
    convo = {d: cafe2(d) for d in ("YY", "YN", "NY", "NN")}
    assert convo == {"YY": ("NOT YET", "YES"), "YN": ("NOT YET", "NO"), "NY": ("NO", "NO"), "NN": ("NO", "NO")}
    evidence["k1_two_person_cafe"] = {d: list(c) for d, c in convo.items()}
    return evidence


if __name__ == "__main__":
    check_examples()
    evidence = {"status": "PASS", "cafe": cafe_tree(),
                "hats_with_announcement": hat_tree(True, 4),
                "hats_without_announcement": hat_tree(False, 4), "grid": grid(),
                "card_fixes_2026_10_23": card_fixes()}
    output = Path(os.environ.get("INFINITY_CHECK_OUT", "math-check-results.json"))
    output.write_text(json.dumps(evidence, indent=2) + "\n")
    print("PASS: café all 8 worlds; hats all 7/8 worlds, synchronized rounds and fixed point; grid 42→30→12→2.")
    print("PASS: two-doll RB example, Problem 2 cards per round, Problem 3 by doll (and the rejected reading), four dolls, K-1 café.")
    print(output)
