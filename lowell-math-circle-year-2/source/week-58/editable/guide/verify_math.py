#!/usr/bin/env python3
"""Independent, standard-library check of the final Week 58 guide instances."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sys


def evaluate(values, owners):
    n = len(values)
    grid = [[sum(row[g] for g, owner in enumerate(owners) if owner == j)
             for j in range(n)] for row in values]
    ef = all(grid[i][i] >= max(grid[i]) for i in range(n))
    prop = all(n * grid[i][i] >= sum(grid[i]) for i in range(n))
    return grid, ef, prop


def all_allocations(labels, values):
    cases = []
    for owners in product(range(len(values)), repeat=len(labels)):
        grid, ef, prop = evaluate(values, owners)
        cases.append({"owners": list(owners), "bundles": [
            [labels[g] for g, owner in enumerate(owners) if owner == i]
            for i in range(len(values))], "observer_grid": grid,
            "envy_free": ef, "proportional": prop})
    return cases


def report():
    p1 = all_allocations(["R1", "R2", "R3", "B1"], [[3, 3, 3, 1], [1, 1, 1, 3]])
    p2 = all_allocations(["R1", "R2", "B1", "B2"], [[3, 3, 1, 1], [1, 1, 3, 3]])
    p5 = all_allocations(["R1", "R2", "R3"], [[1, 1, 1], [1, 1, 1]])
    half = all_allocations(["R1", "R2", "H1", "H2"], [[2, 2, 1, 1], [2, 2, 1, 1]])
    p6 = all_allocations(["X", "Y", "Z"], [[4, 8, 0], [0, 4, 8], [8, 0, 4]])
    for cases, count, efs, props in [(p1, 16, 4, 4), (p2, 16, 5, 5),
                                     (p5, 8, 0, 0), (half, 16, 4, 4), (p6, 27, 1, 2)]:
        assert len(cases) == count
        assert sum(c["envy_free"] for c in cases) == efs
        assert sum(c["proportional"] for c in cases) == props
    assert {tuple(c["bundles"][0]) for c in p1 if c["envy_free"]} == {
        ("R1", "R2"), ("R1", "R3"), ("R2", "R3"), ("R1", "R2", "R3")}
    assert next(c for c in p1 if c["bundles"][0] == ["R1", "R2", "R3"])["observer_grid"] == [[9, 1], [3, 3]]
    assert not next(c for c in p1 if c["bundles"][0] == ["B1"])["envy_free"]
    assert next(c for c in p6 if c["owners"] == [0, 1, 2])["observer_grid"] == [[4, 8, 0], [0, 4, 8], [8, 0, 4]]
    assert [c["owners"] for c in p6 if c["envy_free"]] == [[2, 0, 1]]

    def left_value(x, red, blue):
        return F(red) * min(x, F(150)) / 150 + F(blue) * max(F(0), x - 150) / 150

    strip = []
    for cutter, x in [(0, F(100)), (1, F(200))]:
        rows = [(left_value(x, r, b), F(4) - left_value(x, r, b)) for r, b in [(3, 1), (1, 3)]]
        assert rows[cutter] == (F(2), F(2))
        chooser = 1 - cutter
        side = max(range(2), key=lambda j: rows[chooser][j])
        assert side == (1 if cutter == 0 else 0)
        assert rows[chooser][side] == F(10, 3)
        for e in [-5, -1, 0, 1, 5]:
            v = left_value(x + e, *[(3, 1), (1, 3)][cutter])
            assert min(v, 4 - v) == 2 - F(abs(e), 50)
        strip.append({"cutter": "AB"[cutter], "cut_mm": int(x),
                      "observer_values_left_right": [[str(v) for v in row] for row in rows],
                      "chooser_piece": ["left", "right"][side]})
    assert left_value(F(150), 3, 1) == 3  # both use A: chooser 3, cutter 1

    # Exhaustive finite supplements to the general algebraic proofs in the guide.
    two_checks = 0
    for scores in product(range(3), repeat=6):
        values = [scores[:3], scores[3:]]
        for owners in product(range(2), repeat=3):
            _, ef, prop = evaluate(values, owners)
            assert ef == prop
            two_checks += 1
    three_checks = 0
    for scores in product(range(2), repeat=9):
        values = [scores[:3], scores[3:6], scores[6:]]
        for owners in product(range(3), repeat=3):
            _, ef, prop = evaluate(values, owners)
            assert not ef or prop
            three_checks += 1

    def summary(cases):
        return {"complete_count": len(cases),
                "envy_free_count": sum(c["envy_free"] for c in cases),
                "proportional_count": sum(c["proportional"] for c in cases),
                "passing_allocations": [c for c in cases if c["envy_free"] or c["proportional"]]}
    return {"problem_1": summary(p1), "problem_2": summary(p2),
            "problem_3": strip, "problem_4_join": {"chooser": 3, "cutter": 1, "half_total": 2},
            "problem_5_whole": summary(p5), "problem_5_fixed_halves_scaled_by_2": summary(half),
            "problem_6": summary(p6),
            "problem_7_finite_supplements": {"two_person_allocations_checked": two_checks,
                                            "three_person_allocations_checked": three_checks},
            "guide_print_counts": {"full_material_sheets": 5*3 + 2 + 5*5,
                                   "subset_material_sheets": 5*5+2, "route_student_sheets": 2*2+2*4+7},
            "status": "all exact assertions passed; finite checks supplement, not replace, proofs"}


if __name__ == "__main__":
    data = report()
    text = json.dumps(data, indent=2) + "\n"
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(text)
        print("Week 58 guide mathematical assertions passed")
    else:
        print(text)
