"""Independent review checks; no imports from family writer code.

Coordinates are one based, row downward, column rightward.
Finite confluence checks are evidence for these tested cases, not a theorem proof.
"""
from collections import Counter
from functools import lru_cache
import json
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent

def cells(partition):
    assert all(x > 0 for x in partition)
    assert all(a >= b for a, b in zip(partition, partition[1:]))
    return frozenset((r + 1, c + 1) for r, length in enumerate(partition) for c in range(length))

def partition(shape):
    counts = Counter(r for r, c in shape)
    result = tuple(counts.get(r, 0) for r in range(1, max(counts, default=0) + 1))
    assert cells(result) == shape
    return result

def valid(outer, inner, labels):
    partition(outer)
    partition(inner)
    assert inner <= outer
    assert frozenset(labels) == outer - inner
    assert sorted(labels.values()) == list(range(1, len(labels) + 1))
    for p, value in labels.items():
        r, c = p
        for q in ((r, c + 1), (r + 1, c)):
            if q in labels:
                assert value < labels[q], (p, q, labels)
    return True

def corners(shape):
    return tuple(sorted(p for p in shape if (p[0] + 1, p[1]) not in shape and (p[0], p[1] + 1) not in shape))

def slide(outer, inner, labels, corner):
    valid(outer, inner, labels)
    assert corner in corners(inner)
    numbers = dict(labels)
    hole = corner
    trace = []
    while True:
        r, c = hole
        choices = [q for q in ((r, c + 1), (r + 1, c)) if q in numbers]
        if not choices:
            break
        q = min(choices, key=numbers.get)
        value = numbers.pop(q)
        numbers[hole] = value
        trace.append({"from": q, "to": hole, "number": value})
        hole = q
    assert hole in corners(outer)
    new_outer = outer - {hole}
    new_inner = inner - {corner}
    valid(new_outer, new_inner, numbers)
    return new_outer, new_inner, numbers, trace

def frozen(outer, inner, labels):
    return tuple(sorted(outer)), tuple(sorted(inner)), tuple(sorted(labels.items()))

def undo_with_boundaries(labels, exit, original_corner):
    labels = dict(labels)
    hole = exit
    while hole != original_corner:
        r,c = hole
        choices = [q for q in ((r-1,c),(r,c-1)) if q in labels]
        assert choices
        q = max(choices, key=labels.get)
        labels[hole] = labels.pop(q)
        hole = q
    return labels

@lru_cache(None)
def rectifications(state):
    outer, inner, label_items = state
    outer, inner, labels = frozenset(outer), frozenset(inner), dict(label_items)
    if not inner:
        return frozenset((tuple(sorted(labels.items())),))
    results = set()
    for corner in corners(inner):
        o, i, t, trace = slide(outer, inner, labels, corner)
        results.update(rectifications(frozen(o, i, t)))
    return frozenset(results)

def partitions(total, bound=None):
    if total == 0:
        yield ()
    else:
        for first in range(min(total, bound or total), 0, -1):
            for tail in partitions(total - first, first):
                yield (first,) + tail

def standard_fillings(shape):
    """Topological fillings of the right/down comparison poset."""
    def extend(remaining, labeling):
        if not remaining:
            yield dict(labeling)
            return
        for r, c in sorted(remaining):
            if (r - 1, c) not in remaining and (r, c - 1) not in remaining:
                labeling[(r, c)] = len(labeling) + 1
                yield from extend(remaining - {(r, c)}, labeling)
                del labeling[(r, c)]
    yield from extend(set(shape), {})

def difference(row):
    return [b - a for a, b in zip(row, row[1:])]

def difference_table(row):
    answer = [list(row)]
    while len(answer[-1]) > 1:
        answer.append(difference(answer[-1]))
    return answer

def old_snapshot_engine(initial, rounds):
    """Registers a,b,c,... where each adds its old right neighbor."""
    states = [list(initial)]
    for _ in range(rounds):
        old = states[-1]
        states.append([old[i] + old[i+1] for i in range(len(old)-1)] + [old[-1]])
    return states

def running_sum(row, initial=0):
    answer = [initial]
    for value in row:
        answer.append(answer[-1] + value)
    assert difference(answer) == row
    return answer

def main():
    summary = {"independent": True}
    tested = 0
    undo_checks = 0
    shapes = 0
    for size in range(1, 9):
        for outer_part in partitions(size):
            outer = cells(outer_part)
            for inner_size in range(1, min(4, size) + 1):
                if size - inner_size > 6:
                    continue
                for inner_part in partitions(inner_size):
                    inner = cells(inner_part)
                    if not inner <= outer:
                        continue
                    shapes += 1
                    for labels in standard_fillings(outer - inner):
                        valid(outer, inner, labels)
                        outputs = rectifications(frozen(outer, inner, labels))
                        assert len(outputs) == 1, (outer_part, inner_part, labels, outputs)
                        for corner in corners(inner):
                            _,_,new_labels,path = slide(outer,inner,labels,corner)
                            exit = tuple(path[-1]['from']) if path else corner
                            assert undo_with_boundaries(new_labels,exit,corner)==labels
                            undo_checks += 1
                        tested += 1
    summary["tableau_exhaustive"] = {"shapes": shapes, "standard_tableaux": tested, "single_slides_inverted_with_boundary_information":undo_checks,"outer_cells_at_most": 8, "inner_cells_at_most": 4, "labels_at_most": 6, "all_legal_corner_orders_same": True}
    summary["differences"] = {"triangles": difference_table([n*(n+1)//2 for n in range(7)]), "squares": difference_table([n*n for n in range(7)]), "cubes": difference_table([n*n*n for n in range(7)])}
    summary["accumulation"] = {"input_1_to_6": running_sum(list(range(1,7))), "odd_input": running_sum([1,3,5,7,9,11]), "snapshot_0_0_1": old_snapshot_engine([0,0,1],6), "snapshot_0_1_1": old_snapshot_engine([0,1,1],6), "snapshot_0_0_0_1": old_snapshot_engine([0,0,0,1],6)}
    summary["finite_prefix_caveat"] = {"squares": [n*n for n in range(7)], "squares_plus_binomial_n4": [n*n + math.comb(n,4) if n>=4 else n*n for n in range(7)], "same_first_four_terms": True, "different_next_terms": [16,17]}
    summary["equal_outer_disks"] = []
    for central_radius, outer_radius in [(20,20), (20,10), (10,20), (20,5)]:
        gap = 2*math.asin(outer_radius/(central_radius+outer_radius))
        capacity = math.floor((2*math.pi + 1e-12)/gap)
        summary["equal_outer_disks"].append({"central_radius":central_radius,"outer_radius":outer_radius,"minimum_center_angle_degrees":math.degrees(gap),"capacity":capacity})
    (OUT / "independent-kernel-results.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
