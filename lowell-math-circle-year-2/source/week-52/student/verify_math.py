#!/usr/bin/env python3
"""Writer-stage mathematical checks; no physical or classroom validation."""
import argparse
import itertools
import json
import math
from pathlib import Path


def components(m, n, edges):
    parent = list(range(m + n))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for r, c in edges:
        a, b = root(r - 1), root(m + c - 1)
        parent[a] = b
    return len({root(i) for i in range(m + n)})


def cells(m, n):
    return set(itertools.product(range(1, m + 1), range(1, n + 1)))


def rigid(m, n, edges):
    return components(m, n, edges) == 1


def covers(m, n, edges):
    return ({r for r, c in edges} == set(range(1, m + 1))
            and {c for r, c in edges} == set(range(1, n + 1)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {"scope": "Ideal complete flat grids, fixed side and cell-diagonal lengths; not material testing."}

    # P1–3: exact model geometry, not strength or pin-friction claims.
    triangle = [(0, 0), (4, 0), (2, 3.4641)]
    lengths = [math.dist(triangle[i], triangle[(i + 1) % 3]) for i in range(3)]
    assert max(lengths) - min(lengths) < 0.000002
    assert math.isclose(math.sqrt(60 ** 2 + 60 ** 2), 84.8528137423857)
    result["P1-3"] = {"triangle_drawn_side_lengths_cm": lengths,
                      "kit_side_hole_centers_mm": 60,
                      "kit_diagonal_hole_centers_mm": 60 * math.sqrt(2),
                      "argument": "Fixed triangle sides give discrete circle intersections; fixed diagonal fixes square angle at 90 degrees on the initial planar branch."}

    p4 = [{(1, 1)}, {(1, 1), (2, 2)}, {(1, 1), (1, 2), (2, 1)}, cells(2, 2)]
    assert [rigid(2, 2, e) for e in p4] == [False, False, True, True]
    result["P4"] = {"A-D_component_counts": [components(2, 2, e) for e in p4]}

    # The source handoff offers a standard upper-table 2-by-3 kit alternative.
    # Both comparisons cover all strips but have two independently turning groups.
    handoff = {}
    for m, n, E in [(2, 2, p4[1]), (2, 3, {(1, 1), (1, 2), (2, 3)})]:
        assert covers(m, n, E) and components(m, n, E) == 2
        additions = cells(m, n) - E
        assert all(rigid(m, n, E | {e}) for e in additions)
        handoff[f"{m}-by-{n}"] = {"braced_cells": sorted(E), "components": 2,
                                 "all_empty_cells_join_groups": sorted(additions)}
    result["physical_to_link_handoff"] = handoff

    for m, n, number, expected in [(2, 2, "P5", 4), (2, 3, "P6", 12)]:
        edge_list = sorted(cells(m, n))
        minimum = m + n - 1
        smaller_rigid = [e for e in itertools.combinations(edge_list, minimum - 1) if rigid(m, n, e)]
        minimum_rigid = [e for e in itertools.combinations(edge_list, minimum) if rigid(m, n, e)]
        assert not smaller_rigid and len(minimum_rigid) == expected
        result[number] = {"fewest": minimum, "minimum_rigid_design_count": len(minimum_rigid)}

    p7a = {(1, 1), (1, 2), (2, 1), (2, 2)}
    p7b = {(1, 1), (1, 2), (1, 3), (2, 1)}
    assert len(p7a) == len(p7b) == 4
    assert not rigid(2, 3, p7a) and rigid(2, 3, p7b)
    result["P7"] = {"A_components": components(2, 3, p7a), "B_components": components(2, 3, p7b)}

    p8a = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}
    p8b = {(1, 1), (1, 2), (1, 3), (2, 1), (3, 1)}
    assert covers(3, 3, p8a) and covers(3, 3, p8b)
    assert len(p8a) == len(p8b) == 5
    assert not rigid(3, 3, p8a) and rigid(3, 3, p8b)
    result["P8"] = {"A_components": components(3, 3, p8a), "B_components": components(3, 3, p8b), "both_cover_all_rows_and_columns": True}

    p9 = {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2)}
    removable = {e for e in p9 if rigid(2, 3, p9 - {e})}
    assert removable == p9 - {(1, 3)}
    result["P9"] = {"single_removable_cells": sorted(removable), "essential_cell": (1, 3)}

    p10 = cells(2, 3)
    working, failing = [], []
    for pair in itertools.combinations(sorted(p10), 2):
        (working if rigid(2, 3, p10 - set(pair)) else failing).append(pair)
    assert len(working) == 12 and len(failing) == 3
    assert all(a[1] == b[1] for a, b in failing)
    result["P10"] = {"working_pair_count": len(working), "failing_pairs": failing}

    p11a = {(1, 1), (1, 2), (2, 1), (2, 2)}
    p11b = {(1, 1), (1, 2), (2, 2), (3, 3)}
    helps_a = {e for e in cells(3, 3) - p11a if rigid(3, 3, p11a | {e})}
    helps_b = {e for e in cells(3, 3) - p11b if rigid(3, 3, p11b | {e})}
    assert not helps_a
    assert helps_b == {(1, 3), (2, 3), (3, 1), (3, 2)}
    result["P11"] = {"A_helping_cells": sorted(helps_a), "B_helping_cells": sorted(helps_b)}

    p12 = {(1, c) for c in range(1, 6)} | {(r, 1) for r in range(2, 5)}
    assert len(p12) == 8 and rigid(4, 5, p12)
    result["P12"] = {"fewest": 8, "one_witness": sorted(p12), "lower_bound": "Nine strip vertices start separate; each brace joins at most two groups, reducing the component count by at most one."}

    p13_sets = [set(e) for e in itertools.combinations(sorted(cells(3, 3)), 6) if covers(3, 3, e)]
    assert len(p13_sets) == 78 and all(rigid(3, 3, e) for e in p13_sets)
    result["P13"] = {"covering_six_brace_design_count": len(p13_sets), "all_rigid": True,
                     "explanation": "If disconnected while covering every strip, both sides are split into nonempty parts. For 3+3 strips at most 1*1 + 2*2 = 5 braces fit in separate components."}

    p14_witness = {(1, 1)} | (set(itertools.product(range(2, 5), repeat=2)) - {(4, 4)})
    assert len(p14_witness) == 9 and covers(4, 4, p14_witness) and components(4, 4, p14_witness) == 2
    covering = disconnected = 0
    for e in itertools.combinations(sorted(cells(4, 4)), 9):
        if covers(4, 4, e):
            covering += 1
            disconnected += not rigid(4, 4, e)
    assert (covering, disconnected) == (9696, 144)
    result["P14"] = {"must_hold_shape": False, "one_counterexample": sorted(p14_witness),
                     "covering_nine_brace_design_count": covering, "disconnected_covering_design_count": disconnected}

    # A concrete finite flex of P8 A, independent of merely first-order counting.
    # Top two horizontal/vertical strips share turn 0. Bottom/right pair share turn 0.08.
    angles_h, angles_v = [0, 0, 0.08], [0, 0, 0.08]
    h = [(math.cos(a), math.sin(a)) for a in angles_h]
    v = [(-math.sin(a), math.cos(a)) for a in angles_v]
    def joint(i, j):
        return (sum(x for x, y in h[:j]) + sum(x for x, y in v[:i]),
                sum(y for x, y in h[:j]) + sum(y for x, y in v[:i]))
    side_lengths = [math.dist(joint(i, j), joint(i, j + 1)) for i in range(4) for j in range(3)]
    side_lengths += [math.dist(joint(i, j), joint(i + 1, j)) for i in range(3) for j in range(4)]
    # Diagonals in the PDF rise from the lower-left to the upper-right.
    diagonal_lengths = [math.dist(joint(r - 1, c), joint(r, c - 1)) for r, c in p8a]
    assert all(math.isclose(d, 1, abs_tol=1e-12) for d in side_lengths)
    assert all(math.isclose(d, math.sqrt(2), abs_tol=1e-12) for d in diagonal_lengths)
    assert not math.isclose(math.dist(joint(0, 3), joint(1, 2)), math.sqrt(2), abs_tol=1e-5)
    result["finite_flex_P8_A"] = {"turn_radians": 0.08, "maximum_side_error": max(abs(d-1) for d in side_lengths), "maximum_brace_error": max(abs(d-math.sqrt(2)) for d in diagonal_lengths), "unbraced_cell_changes_angle": True}

    output = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
    print(output)


if __name__ == "__main__":
    main()
