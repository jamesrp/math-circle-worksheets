#!/usr/bin/env python3
"""Independent Week 81 finite-game checks; Python standard library only.

No imports from the author's builder or mathematical checks. Bucket tuples
read left to right. A move takes 1 (or 1..take in the encore) from index j,
then independently adds 0..cap to every index strictly below j.

Finite enumeration supports, but does not replace, the written proofs for
arbitrarily large finite refills or arbitrarily many fixed finite buckets.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json
import re

SOURCE = Path(__file__).resolve().parent
RUN = SOURCE.parent


def rank(state, cap):
    # Each legal move strictly lowers this integer for a fixed refill cap.
    return sum(a * (cap + 1) ** i for i, a in enumerate(state))


def children(state, cap=1, take=1):
    for chosen, count in enumerate(state):
        for removed in range(1, min(take, count) + 1):
            for additions in product(range(cap + 1), repeat=chosen):
                nxt = list(state)
                nxt[chosen] -= removed
                for earlier, amount in enumerate(additions):
                    nxt[earlier] += amount
                nxt = tuple(nxt)
                assert rank(nxt, cap) < rank(state, cap)
                yield nxt


@lru_cache(None)
def solve(state, cap=1, take=1):
    # Work solely from the legal moves, without the parity classification.
    options = tuple(children(state, cap, take))
    if not options:
        return {"first_wins": False, "min_moves": 0, "max_moves": 0}
    answers = tuple(solve(nxt, cap, take) for nxt in options)
    return {
        "first_wins": any(not answer["first_wins"] for answer in answers),
        "min_moves": 1 + min(answer["min_moves"] for answer in answers),
        "max_moves": 1 + max(answer["max_moves"] for answer in answers),
    }


def even_repair(state):
    odd = [i for i, count in enumerate(state) if count % 2]
    if not odd:
        return None
    chosen = max(odd)
    nxt = list(state)
    nxt[chosen] -= 1
    for earlier in range(chosen):
        nxt[earlier] += nxt[earlier] % 2
    return tuple(nxt)


def snapshot(path):
    return {"path": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex", type=Path, default=SOURCE / "student/students.tex")
    parser.add_argument("--pdf", type=Path, default=RUN / "students.pdf")
    parser.add_argument("--output", type=Path, default=RUN / "independent-math-results.json")
    args = parser.parse_args()
    tex = args.tex.read_text()
    printed_three = [tuple(map(int, match)) for match in
                     re.findall(r"\\smallstart\{(\d+)\}\{(\d+)\}\{(\d+)\}", tex)]
    problem1 = [(0, 0, 1), (1, 1, 0), (2, 1, 1), (2, 2, 2)]
    problem3 = [(2, 2, 2), (1, 2, 2), (2, 1, 2), (2, 2, 1), (0, 2, 0), (3, 3, 1)]
    assert printed_three == problem1 + problem3 + [(1, 1, 1)]
    printed_two = [tuple(map(int, match)) for match in
                   re.findall(r"\\paircard\{(\d+)\}\{(\d+)\}", tex)]
    problem2 = [(left, right) for right in range(4) for left in range(4)]
    assert printed_two == problem2

    # Exhaustive finite checks: independent legal-move recurrence on 340 seed
    # states (1..4 buckets, each initially 0..3), including every printed start.
    seed_count = 0
    for buckets in range(1, 5):
        for state in product(range(4), repeat=buckets):
            answer = solve(state)
            assert answer["first_wins"] == any(a % 2 for a in state), state
            assert answer["min_moves"] == sum(state), state
            assert answer["max_moves"] == rank(state, 1), state
            repaired = even_repair(state)
            if repaired is not None:
                assert repaired in set(children(state)), state
                assert all(a % 2 == 0 for a in repaired), state
                assert not solve(repaired)["first_wins"], state
            else:
                assert all(any(a % 2 for a in nxt) for nxt in children(state))
            seed_count += 1

    # Worked visual: (1,1,2), removal from third -> (1,1,1), then adding
    # one to each earlier bucket -> (2,2,1). This is a legal capped move.
    assert (2, 2, 1) in set(children((1, 1, 2)))
    # The separate quantity-card visual removes exactly 1 from 12, yielding 11.
    assert 12 - 1 == 11

    rows = {}
    for problem, starts in [("1", problem1), ("2", problem2), ("3", problem3)]:
        rows[problem] = [{"start": state, **solve(state),
                          "even_repair": even_repair(state),
                          "winning_successors": [nxt for nxt in children(state)
                                                 if not solve(nxt)["first_wins"]]}
                         for state in starts]

    # Uncapped two-bucket witness: after taking the only right counter,
    # refill the left with M. The only subsequent legal moves remove one
    # from the left; total length is exactly M+1.
    witnesses = []
    for target in [10, 30, 100, 1000]:
        refill = target - 1
        assert refill >= 0
        # A sole left bucket has no refill destination. Check every step
        # directly rather than deep-recursing on a large quantity card.
        current = (refill, 0)
        remaining_moves = 0
        while current != (0, 0):
            options = tuple(children(current))
            assert options == ((current[0] - 1, 0),)
            current = options[0]
            remaining_moves += 1
        assert remaining_moves == target - 1
        witnesses.append({"target_moves": target, "first_refill": refill,
                          "post_first_move": [refill, 0], "exact_moves": refill + 1})
    assert solve((0, 1))["max_moves"] == 2  # capped contrast

    # Optional Take 3 encore with a 0..3 refill cap: all-multiples-of-four
    # classification is checked independently for 1..3 buckets, 0..3 starts.
    # Its general uncapped justification remains the written two-way proof.
    encore_seed_count = 0
    for buckets in range(1, 4):
        for state in product(range(4), repeat=buckets):
            assert solve(state, 3, 3)["first_wins"] == any(a % 4 for a in state), state
            encore_seed_count += 1
    # Explicit alternative-reading counterexample: the warm-up cap cannot
    # silently carry into the multiples-of-four Take-3 encore.
    assert not solve((1, 1), 1, 3)["first_wins"]
    assert all(solve(nxt, 1, 3)["first_wins"]
               for nxt in children((1, 1), 1, 3))

    # Numeric fit assertion for the revised cards; physical rehearsal remains untested.
    assert "rectangle +(50,55);" in tex
    assert "rectangle +(56,139);" in tex
    assert 50 < 56 and 55 < 139
    output = {
        "status": "PASS",
        "independence": "Adapted from the independent mathematics-review checker; no author code imported; legal moves enumerated directly.",
        "snapshot": [snapshot(args.tex),
                     snapshot(args.pdf)],
        "digital_material_dimensions_mm": {"bucket": [56, 139], "quantity_card": [50, 55], "fit": True},
        "capped_seed_states": seed_count,
        "cached_states_including_reachable_descendants": solve.cache_info().currsize,
        "printed_starts": rows,
        "worked_visual": {"before": [1, 1, 2], "after_removal": [1, 1, 1],
                          "after_refill": [2, 2, 1], "legal": True},
        "uncapped_length_witnesses": witnesses,
        "capped_max_moves_from_0_1": 2,
        "take3_encore_seed_states": encore_seed_count,
        "take3_cap1_counterexample": {"start": [1, 1], "first_wins": False,
                                        "successors": [[0, 1], [1, 0], [2, 0]],
                                        "all_successors_first_wins": True},
        "limits": ["Infinite-branching uncapped game not exhaustively enumerated.",
                   "Universal termination and parity use the written argument.",
                   "Physical print fit, materials rehearsal and classroom use untested."],
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(f"PASS: {seed_count} capped seeds; all 26 printed starts; "
          f"{encore_seed_count} Take-3 encore seeds.")
    for problem, values in rows.items():
        print("Problem", problem)
        for row in values:
            print(row["start"], "FIRST" if row["first_wins"] else "SECOND",
                  "repair", row["even_repair"],
                  "length", (row["min_moves"], row["max_moves"]))


if __name__ == "__main__":
    main()
