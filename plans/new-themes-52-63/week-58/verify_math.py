"""Independent small-instance audit for Week 58's research kernels.

Run with Python 3; no third-party libraries. This checks research examples,
not future writer-selected tasks or physical classroom procedures.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def allocations(values):
    """All complete allocations; rows are observers, columns distinct goods."""
    n, m = len(values), len(values[0])
    for owners in product(range(n), repeat=m):
        seen = [[sum(row[g] for g in range(m) if owners[g] == j)
                 for j in range(n)] for row in values]
        proportional = all(n * seen[i][i] >= sum(values[i]) for i in range(n))
        envy_free = all(seen[i][i] >= seen[i][j] for i in range(n) for j in range(n))
        yield owners, seen, proportional, envy_free


def audit():
    # R1, R2, B1, B2. Labeling avoids hiding case coverage behind identical icons.
    taste_rows = [[3, 3, 1, 1], [1, 1, 3, 3]]
    checked = list(allocations(taste_rows))
    assert len(checked) == 16
    assert all(p == e for _, _, p, e in checked)
    good = [list(o) for o, _, _, e in checked if e]
    assert len(good) == 5
    bad_equal_count = next(s for o, s, _, _ in checked if o == (1, 1, 0, 0))
    good_by_color = next(s for o, s, _, _ in checked if o == (0, 0, 1, 1))
    assert bad_equal_count == [[2, 6], [6, 2]]
    assert good_by_color == [[6, 2], [2, 6]]

    discrete = list(allocations([[1, 1, 1], [1, 1, 1]]))
    assert not any(e for _, _, _, e in discrete)
    assert not any(p for _, _, p, _ in discrete)

    # Three equal-length divisible panels; each person values each full panel as below.
    three = [[4, 8, 0], [0, 4, 8], [8, 0, 4]]
    identity = next(s for o, s, _, _ in allocations(three) if o == (0, 1, 2))
    assert identity == three
    assert all(sum(r) == 12 for r in three)
    assert all(3 * three[i][i] >= sum(three[i]) for i in range(3))
    assert all(any(three[i][j] > three[i][i] for j in range(3)) for i in range(3))

    # Two length-one panels. Cutter values density 3 then 1; chooser 1 then 3.
    cut = F(2, 3)
    cutter = [3 * cut, 3 * (1 - cut) + 1]
    chooser = [cut, 1 - cut + 3]
    assert cutter == [F(2), F(2)]
    assert chooser == [F(2, 3), F(10, 3)]
    assert max(chooser) >= sum(chooser) / 2

    # Exhaust all two-agent profiles on three goods with per-good values 0..2.
    profiles = 0
    for flat in product(range(3), repeat=6):
        profiles += 1
        for _, _, p, e in allocations([flat[:3], flat[3:]]):
            assert p == e

    return {
        "scope": "Research examples only; future worksheet instances need their own audit.",
        "distinct_four_goods_complete_allocations": len(checked),
        "envy_free_allocations_for_different_tastes": good,
        "equal_counts_can_fail_observer_rows": bad_equal_count,
        "color_split_passes_observer_rows": good_by_color,
        "three_identical_indivisible_goods_two_agents_envy_free_count": 0,
        "three_agent_proportional_but_envious_observer_rows": three,
        "divisible_cut_in_first_length_one_panel": str(cut),
        "cutter_piece_values": [str(x) for x in cutter],
        "chooser_piece_values": [str(x) for x in chooser],
        "two_agent_profile_count_checked": profiles,
        "two_agent_allocations_checked": profiles * 8,
        "physical_pretest": "unperformed",
    }


if __name__ == "__main__":
    result = audit()
    out = Path(__file__).with_name("math-checks.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
