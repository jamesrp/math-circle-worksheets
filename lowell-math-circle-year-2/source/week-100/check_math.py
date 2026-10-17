#!/usr/bin/env python3
"""Independent Week 100 math check, standard library only.

Run: python3 check_math.py
No input files are read and no files are written. JSON goes to standard output.
This checks the revised final student snapshot identified below. If visible P1/P3 card
names change, update only VISIBLE_CARD_AT_POSITION and the P3 request constants,
then update the snapshot description. P4/P5 clue data are intentionally separate.
The guide supplies general proofs and final answers; the production record retains the original review inventory and revision changes.
"""
from collections import Counter
from itertools import combinations, product
import json

SNAPSHOT = {
    "description": "integrated final student source and PDF verified 2026-10-17",
    "tex_sha256": "dd3dcb5bf1c1ea09d8b655b6403dfffe14554d5e7ead0e28d23e49455911f5e8",
    "pdf_sha256": "6658ed00dab8bb8ad0b57a8a4258288e5611818c3f886754ea2b86bd1cd9257e",
}
VALUES = (2, 4, 8)
LETTERS = tuple("ABCDEF")
RADII = (0, 1, 2, 3, 4, 7, 8)
# This is the only name assignment used to transcribe the visible P1/P3 world.
# Coordinates are in the world's unscaled TikZ millimetres.
VISIBLE_CARD_AT_POSITION = {
    "upper_left": "A", "upper_middle": "B", "upper_right": "D",
    "lower_left": "C", "lower_middle": "E", "lower_right": "F",
}
VISIBLE_POSITION_CENTERS = {
    "upper_left": (23, 21), "upper_middle": (40, 21),
    "upper_right": (64, 21), "lower_left": (25, 51),
    "lower_middle": (45, 51), "lower_right": (88, 49),
}
VISIBLE_RECTANGLES = (
    ((0, 0, 112, 67), 8), ((6, 7, 76, 33), 4),
    ((12, 12, 50, 28), 2), ((12, 42, 58, 60), 2),
)
P3_RADIUS3_CENTERS = ("A", "C", "D", "F")
P3_CONTAINED_CARD = "B"
# Fixed hidden-world clues: do not derive these from the visible-world diagram.
P4 = {"AB": 2, "AC": 4, "BC": 4, "DE": 2,
      "AD": 8, "AE": 8, "BD": 8, "BE": 8, "CD": 8, "CE": 8}
P2_CASES = ((2, 2, 2), (2, 4, 4), (2, 2, 4),
            (4, 4, 4), (2, 4, 8), (2, 8, 8))


def key(a, b):
    return tuple(sorted((a, b)))


def distance(matrix, a, b):
    return 0 if a == b else matrix[key(a, b)]


def violations(cards, matrix):
    bad = []
    for triple in combinations(cards, 3):
        ds = [distance(matrix, a, b) for a, b in combinations(triple, 2)]
        if ds.count(max(ds)) == 1:
            bad.append({"cards": list(triple), "distances": ds})
    return bad


def ball(cards, matrix, center, radius):
    return frozenset(c for c in cards if distance(matrix, center, c) <= radius)


def partition_at(cards, matrix, radius):
    parts = {ball(cards, matrix, c, radius) for c in cards}
    return sorted((sorted(part) for part in parts), key=lambda part: part[0])


def pair_json(matrix):
    return {"-".join(map(str, pair)): value for pair, value in sorted(matrix.items())}


def inside_rect(point, rect, margin=0):
    x, y = point
    x0, y0, x1, y1 = rect
    return x0 + margin <= x <= x1 - margin and y0 + margin <= y <= y1 - margin


def rect_inside(a, b):
    return b[0] <= a[0] <= a[2] <= b[2] and b[1] <= a[1] <= a[3] <= b[3]


def rect_disjoint(a, b):
    return a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1]


def diagram_groups():
    assert set(VISIBLE_CARD_AT_POSITION.values()) == set(LETTERS)
    groups = []
    for rect, label in VISIBLE_RECTANGLES:
        members = frozenset(VISIBLE_CARD_AT_POSITION[pos]
                            for pos, xy in VISIBLE_POSITION_CENTERS.items()
                            if inside_rect(xy, rect))
        assert len(members) > 1
        # A complete 10 mm diagram card, rather than just its centre, fits.
        for pos, xy in VISIBLE_POSITION_CENTERS.items():
            if VISIBLE_CARD_AT_POSITION[pos] in members:
                assert inside_rect(xy, rect, margin=5)
        groups.append((members, label))
    for (rect_a, label_a), (rect_b, label_b) in combinations(VISIBLE_RECTANGLES, 2):
        if rect_inside(rect_a, rect_b):
            assert label_a < label_b
        elif rect_inside(rect_b, rect_a):
            assert label_b < label_a
        else:
            assert rect_disjoint(rect_a, rect_b)
    return groups


def matrix_from_groups(cards, groups):
    return {key(a, b): min(label for members, label in groups if {a, b} <= members)
            for a, b in combinations(cards, 2)}


def partitions(items):
    """Every set partition once, in restricted-growth canonical order."""
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for part in partitions(rest):
        yield ((first,),) + part
        for i in range(len(part)):
            yield part[:i] + ((first,) + part[i],) + part[i + 1:]


def all_worlds(cards):
    """All distances in {2,4,8}: a partition at 2 refining a partition at 4.

    At threshold 8 everything merges. This also permits an actual outermost
    merger below 8; unused labels do not force extra groups.
    """
    for p4 in partitions(cards):
        for refinements in product(*(tuple(partitions(block)) for block in p4)):
            p2 = tuple(block for refinement in refinements for block in refinement)
            at4 = {card: i for i, block in enumerate(p4) for card in block}
            at2 = {card: i for i, block in enumerate(p2) for card in block}
            yield {key(a, b): (2 if at2[a] == at2[b] else
                               4 if at4[a] == at4[b] else 8)
                   for a, b in combinations(cards, 2)}


def check_ball_theorems(cards, matrix):
    unique_balls = set()
    for center, radius in product(cards, RADII):
        current = ball(cards, matrix, center, radius)
        unique_balls.add(current)
        for member in current:
            assert ball(cards, matrix, member, radius) == current
    for a, b in combinations(unique_balls, 2):
        assert not (a & b) or a <= b or b <= a
    return len(unique_balls)


def main():
    out = {"snapshot": SNAPSHOT}
    # Convention visual, independently transcribed from its rectangles.
    example_cards = tuple("XYZ")
    example = matrix_from_groups(example_cards,
                                 ((frozenset("XY"), 3), (frozenset("XYZ"), 6)))
    assert pair_json(example) == {"X-Y": 3, "X-Z": 6, "Y-Z": 6}
    assert ball(example_cards, example, "X", 1) == frozenset("X")
    assert ball(example_cards, example, "X", 4) == frozenset("XY")
    out["convention_example"] = pair_json(example)

    groups = diagram_groups()
    visible = matrix_from_groups(LETTERS, groups)
    assert not violations(LETTERS, visible)
    out["P1_visible_world"] = {
        "card_at_position": VISIBLE_CARD_AT_POSITION,
        "groups": [{"cards": sorted(members), "label": label} for members, label in groups],
        "all_15_distances": pair_json(visible),
        "diagram_containment_and_strict_labels": "passed",
    }
    out["P2"] = [{"AB_AC_BC": list(ds),
                    "possible": not violations(tuple("ABC"), dict(zip(combinations("ABC", 2), ds)))}
                   for ds in P2_CASES]
    assert [item["possible"] for item in out["P2"]] == [True, True, False, True, False, True]

    balls_containing = {}
    for radius in RADII:
        # Use every possible center; do not assume the center theorem here.
        collections = {ball(LETTERS, visible, center, radius) for center in LETTERS
                       if P3_CONTAINED_CARD in ball(LETTERS, visible, center, radius)}
        assert len(collections) == 1
        collection = next(iter(collections))
        balls_containing.setdefault("".join(sorted(collection)), []).append(radius)
    out["P3"] = {
        "radius3": {center: sorted(ball(LETTERS, visible, center, 3))
                    for center in P3_RADIUS3_CENTERS},
        "balls_containing": P3_CONTAINED_CARD,
        "collections_with_radii": balls_containing,
    }

    five = tuple("ABCDE")
    original = {tuple(pair): value for pair, value in P4.items()}
    assert len(original) == 10 and not violations(five, original)
    out["P4"] = {str(radius): partition_at(five, original, radius) for radius in VALUES}
    visible_restriction = {pair: visible[pair] for pair in combinations(five, 2)}
    leak = visible_restriction == original
    assert not leak, "The visible world must not supply the later reconstruction answer."
    out["located_issue"] = {
        "visible_world_restricted_to_ABCDE_exactly_solves_P4": leak,
        "explanation": "If true, deleting F from P1/P3 supplies P4's complete solution.",
    }

    broken = dict(original)
    broken[tuple("AC")] = 2
    bad = violations(five, broken)
    assert bad == [{"cards": list("ABC"), "distances": [2, 2, 4]}]
    repairs = []
    for pair in sorted(broken):
        for value in VALUES:
            if value == broken[pair]:
                continue
            candidate = dict(broken)
            candidate[pair] = value
            if not violations(five, candidate):
                repairs.append({"pair": "".join(pair), "new_value": value,
                                "partitions": {str(r): partition_at(five, candidate, r)
                                               for r in VALUES}})
    assert [(r["pair"], r["new_value"]) for r in repairs] == [("AB", 4), ("AC", 4), ("BC", 2)]
    out["P5"] = {"initial_violations": bad, "candidates_checked": 20, "repairs": repairs}

    # Cross-check the partition construction against ALL 3^10 assignments on 5 cards.
    pairs5 = tuple(combinations(five, 2))
    brute5 = set()
    for values in product(VALUES, repeat=len(pairs5)):
        matrix = dict(zip(pairs5, values))
        if not violations(five, matrix):
            brute5.add(values)
    constructed5 = {tuple(matrix[pair] for pair in pairs5) for matrix in all_worlds(five)}
    assert brute5 == constructed5
    pairs6 = tuple(combinations(LETTERS, 2))
    worlds6 = tuple(all_worlds(LETTERS))
    assert len(worlds6) == len({tuple(w[p] for p in pairs6) for w in worlds6})
    ball_count_histogram = Counter()
    for matrix in worlds6:
        assert not violations(LETTERS, matrix)
        ball_count_histogram[check_ball_theorems(LETTERS, matrix)] += 1
    out["P6_P7_finite_checks"] = {
        "all_five_card_distance_assignments_checked": len(VALUES) ** len(pairs5),
        "valid_five_card_worlds": len(brute5),
        "all_six_card_worlds_checked": len(worlds6),
        "six_card_triples_checked": len(worlds6) * 20,
        "radii_checked": list(RADII),
        "distinct_ball_count_histogram": dict(sorted(ball_count_histogram.items())),
        "general_proofs": "See the facilitator guide; finite checks alone are not the proof.",
    }

    numbers = tuple(range(8))
    number_matrix = {}
    for a, b in combinations(numbers, 2):
        value = 8 if a % 2 != b % 2 else 4 if a % 4 != b % 4 else 2
        number_matrix[(a, b)] = value
        difference = abs(a - b)
        valuation = 0
        while difference % 2 == 0:
            valuation += 1
            difference //= 2
        assert value == 8 // (2 ** valuation)
    assert 1 % 4 == 5 % 4 == 1 and number_matrix[(1, 5)] == 2
    assert not violations(numbers, number_matrix)
    out["P8"] = {"distance_counts": dict(sorted(Counter(number_matrix.values()).items())),
                 "radius3_balls": partition_at(numbers, number_matrix, 3),
                 "radius5_balls": partition_at(numbers, number_matrix, 5),
                 "group_partitions": {str(r): partition_at(numbers, number_matrix, r) for r in VALUES}}
    number_triples = Counter(tuple(sorted(number_matrix[key(a, b)] for a, b in combinations(t, 2)))
                             for t in combinations(numbers, 3))
    assert sum(number_triples.values()) == 56
    out["P9"] = {",".join(map(str, ds)): count for ds, count in sorted(number_triples.items())}

    # Adversarial path: every answer so far is 8. Each unasked pair separately
    # remains compatible with a valid world in which JUST that pair is 2.
    all8 = {pair: 8 for pair in pairs6}
    assert not violations(LETTERS, all8)
    alternatives = {}
    for unasked in pairs6:
        alternative = dict(all8)
        alternative[unasked] = 2
        assert not violations(LETTERS, alternative)
        assert all(alternative[pair] == all8[pair] for pair in pairs6 if pair != unasked)
        alternatives["".join(unasked)] = "valid single-2 counterexample; every other answer is 8"
    out["P10"] = {
        "number_of_unordered_distinct_pairs": len(pairs6),
        "universal_query_upper_bound": 15,
        "worst_case_required": 15,
        "all8_compatible_single2_counterexamples": alternatives,
        "reason": "After fewer than 15 distinct queries on the all-8 answer path, an unasked pair remains. The all-8 world and a world with that pair at 2 require different output distances but give the same answers to every query so far.",
    }
    out["mathematical_checks_passed"] = True
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
