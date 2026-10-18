#!/usr/bin/env python3
"""Independent, standard-library-only check of Week 99 student mathematics.

Run: python3 check_math.py
No arguments, input files, package dependencies, network requests, or writes.
The printed JSON contains reproducible answers and exhaustive verification totals.
Inputs below were transcribed independently from the rendered student diagrams.
Breadth-first search on legal single-counter moves supplies the reference metric;
the line and star formulas are checked against it, not assumed in its computation.
"""

from collections import deque
from functools import lru_cache
from itertools import combinations_with_replacement, permutations
import json


def states(sites, mass):
    return tuple(combinations_with_replacement(range(sites), mass))


def neighbors(state, adjacency):
    result = set()
    for i, old in enumerate(state):
        for new in adjacency[old]:
            result.add(tuple(sorted(state[:i] + (new,) + state[i + 1:])))
    return tuple(sorted(result))


def all_distances(sites, mass, adjacency):
    arrangements = states(sites, mass)
    edge = {a: neighbors(a, adjacency) for a in arrangements}
    matrix = {}
    for source in arrangements:
        distances = {source: 0}
        queue = deque([source])
        while queue:
            a = queue.popleft()
            for b in edge[a]:
                if b not in distances:
                    distances[b] = distances[a] + 1
                    queue.append(b)
        assert len(distances) == len(arrangements)
        matrix[source] = distances
    return arrangements, edge, matrix


def line_adjacency(sites):
    return tuple(tuple(j for j in (i - 1, i + 1) if 0 <= j < sites)
                 for i in range(sites))


def gap_imbalances(a, b, sites=6):
    return tuple(sum(x <= gap for x in a) - sum(x <= gap for x in b)
                 for gap in range(sites - 1))


def matching_cost(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def brute_assignment_cost(a, b):
    return min(sum(abs(x - y) for x, y in zip(a, order))
               for order in set(permutations(b)))


def move_between(a, b):
    old = list(a)
    new = list(b)
    for x in a:
        if x in new:
            new.remove(x)
            old.remove(x)
    assert len(old) == len(new) == 1
    return [old[0], new[0]]


def two_shortest_plans(a, b, edge, matrix):
    def visit(current):
        if current == b:
            return [[]]
        result = []
        for following in edge[current]:
            if matrix[following][b] == matrix[current][b] - 1:
                for tail in visit(following):
                    result.append([move_between(current, following)] + tail)
                    if len(result) == 2:
                        return result
        return result
    plans = visit(a)
    assert len(plans) == 2 and plans[0] != plans[1]
    assert all(len(plan) == matrix[a][b] for plan in plans)
    return plans


@lru_cache(None)
def greedy_plans(a, b):
    """Committed complete deliveries; enumerate every permitted tie choice."""
    if not a:
        return ((0, ()),)
    shortest = min(abs(x - y) for x in a for y in b)
    result = set()
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if abs(x - y) == shortest:
                for tail_cost, tail in greedy_plans(a[:i] + a[i + 1:],
                                                    b[:j] + b[j + 1:]):
                    result.add((shortest + tail_cost, ((x, y),) + tail))
    return tuple(sorted(result))


def row_name(row):
    return ''.join(str(i) for i in row)


def main():
    line = {mass: all_distances(6, mass, line_adjacency(6)) for mass in (2, 4)}
    five = all_distances(5, 4, line_adjacency(5))
    checked_line_pairs = 0
    for mass, (arrangements, edge, matrix) in line.items():
        for a in arrangements:
            for b in arrangements:
                assert matrix[a][b] == matching_cost(a, b)
                assert matrix[a][b] == sum(map(abs, gap_imbalances(a, b)))
                checked_line_pairs += 1

    # Tuples list counter positions, not bin occupancies.
    fixed = {
        '2-3 P1 first': ((0, 0), (2, 4), 6),
        '2-3 P1 second': ((0, 3), (1, 2), 2),
        '2-3 P2 first / 4-5 P1 first': ((0, 0, 0, 5), (1, 2, 3, 4), 7),
        '2-3 P2 second / 4-5 P1 second': ((1, 1, 4, 4), (0, 2, 2, 5), 5),
        '2-3 P2 third': ((2, 2, 2, 2), (0, 1, 3, 4), 6),
        'both P3 first': ((0, 3), (2, 5), 4),
        '2-3 P3 second': ((0, 4), (2, 5), 3),
        '4-5 P2 first': ((0, 0, 5, 5), (2, 2, 3, 3), 8),
        '4-5 P2 second': ((1, 1, 1, 4), (0, 2, 3, 5), 5),
        '4-5 P2 third': ((0, 2, 3, 5), (1, 1, 4, 4), 4),
        '4-5 P3 second': ((0, 4), (3, 5), 4),
    }
    fixed_results = {}
    for label, (a, b, answer) in fixed.items():
        arrangements, edge, matrix = line[len(a)]
        assert matrix[a][b] == answer == brute_assignment_cost(a, b)
        fixed_results[label] = {
            'start_positions': a, 'target_positions': b, 'minimum_work': answer,
            'signed_gap_imbalances': gap_imbalances(a, b),
            'sorted_complete_deliveries': list(zip(a, b)),
            'two_distinct_best_adjacent_move_plans': two_shortest_plans(a, b, edge, matrix)
        }

    greedy_results = {}
    for a, b, expect in [((0, 3), (2, 5), {6}),
                         ((0, 4), (2, 5), {3}),
                         ((0, 4), (3, 5), {4, 6})]:
        plans = greedy_plans(a, b)
        assert {cost for cost, _ in plans} == expect
        greedy_results[f'{row_name(a)} to {row_name(b)}'] = {
            'optimum': line[2][2][a][b], 'all_greedy_plans': plans}

    arrangements, edge, matrix = line[4]
    target = (2, 2, 2, 2)
    starts_by_work = {str(work): [row_name(a) for a in arrangements
                                if matrix[a][target] == work] for work in (4, 7)}
    assert all(len(rows) >= 2 for rows in starts_by_work.values())
    work5_witnesses = {}
    for target in arrangements:
        candidates = [a for a in arrangements if matrix[a][target] == 5]
        assert candidates
        # Construct five units of one-way motion toward a far endpoint.
        direction = 1 if sum(target) <= 10 else -1
        monotone = target
        for _ in range(5):
            candidates_for_step = [i for i, x in enumerate(monotone)
                                   if 0 <= x + direction <= 5]
            assert candidates_for_step
            i = candidates_for_step[0]
            monotone = tuple(sorted(monotone[:i] + (monotone[i] + direction,)
                                    + monotone[i + 1:]))
        assert matrix[monotone][target] == 5
        work5_witnesses[row_name(target)] = {
            'number_of_work5_starts': len(candidates),
            'constructive_work5_start': row_name(monotone)}

    catalog = tuple(a for a in five[0] if sum(a) == 8)
    printed_catalog = ((0, 0, 4, 4), (0, 1, 3, 4), (0, 2, 2, 4), (0, 2, 3, 3),
                       (1, 1, 2, 4), (1, 1, 3, 3), (1, 2, 2, 3), (2, 2, 2, 2))
    assert catalog == printed_catalog
    catalog_matrix = [[five[2][a][b] for b in catalog] for a in catalog]
    maximum = max(map(max, catalog_matrix))
    maximizers = [[row_name(a), row_name(b)] for i, a in enumerate(catalog)
                 for b in catalog[i + 1:] if five[2][a][b] == maximum]
    assert maximum == 8 and maximizers == [['0044', '2222']]

    star_adj = ((3,), (3,), (3,), (0, 1, 2))  # A, B, C, O
    star = {mass: all_distances(4, mass, star_adj) for mass in (3, 4)}
    star_pairs = 0
    for mass, (arrs, _, distance) in star.items():
        for a in arrs:
            for b in arrs:
                formula = sum(abs(a.count(leaf) - b.count(leaf)) for leaf in range(3))
                assert distance[a][b] == formula
                star_pairs += 1
    fixed_star = {
        'both P5 first': ((0, 0, 2), (1, 1, 3), 5),
        '2-3 P5 second': ((0, 0, 1), (0, 2, 2), 4),
        '4-5 P5 second': ((0, 0, 0, 1), (0, 2, 2, 3), 5),
        '2-3 P5 work6 example': ((0, 0, 0), (1, 1, 1), 6),
        '4-5 P5 four-counter example': ((0, 0, 0, 0), (1, 1, 1, 1), 8),
    }
    star_results = {}
    for label, (a, b, expected) in fixed_star.items():
        actual = star[len(a)][2][a][b]
        assert actual == expected
        star_results[label] = {
            'start_positions': ['ABCO'[x] for x in a],
            'target_positions': ['ABCO'[x] for x in b],
            'leaf_edge_imbalances': [a.count(i) - b.count(i) for i in range(3)],
            'minimum_work': actual}

    triangle_checked = 0
    for a in arrangements:
        for b in arrangements:
            ab = matrix[a][b]
            for c in arrangements:
                assert matrix[a][c] <= ab + matrix[b][c]
                triangle_checked += 1
    triple_examples = {
        'equality': ((0, 0, 0, 0), (2, 2, 2, 2), (5, 5, 5, 5)),
        'strict_inequality': ((0, 0, 0, 0), (5, 5, 5, 5), (1, 1, 1, 1))}
    triple_results = {}
    for label, (a, b, c) in triple_examples.items():
        via = matrix[a][b] + matrix[b][c]
        direct = matrix[a][c]
        assert (via == direct) if label == 'equality' else (via > direct)
        triple_results[label] = {'A': a, 'B': b, 'C': c,
                                 'AB': matrix[a][b], 'BC': matrix[b][c],
                                 'AC': direct, 'via_B': via}

    result = {
        'status': 'PASS',
        'scope': 'Grades 2-3 and grades 4-5 only; six problems and six pages each.',
        'method': 'Exhaustive BFS on legal adjacent/road moves, independently transcribed inputs.',
        'line_formula_ordered_pairs_checked': checked_line_pairs,
        'line_fixed_cases': fixed_results,
        'committed_greedy_delivery_cases': greedy_results,
        'middle_P4_all_starts_by_work': starts_by_work,
        'middle_P6_targets_checked': len(arrangements),
        'middle_P6_impossible_targets': [],
        'middle_P6_minimum_solution_count': min(x['number_of_work5_starts'] for x in work5_witnesses.values()),
        'middle_P6_maximum_solution_count': max(x['number_of_work5_starts'] for x in work5_witnesses.values()),
        'middle_P6_constructive_witness_for_every_target': work5_witnesses,
        'upper_P4_catalog': [row_name(a) for a in catalog],
        'upper_P4_distance_matrix': catalog_matrix,
        'upper_P4_maximum': maximum,
        'upper_P4_all_maximizing_unordered_pairs': maximizers,
        'star_formula_ordered_pairs_checked': star_pairs,
        'star_fixed_cases': star_results,
        'triangle_ordered_triples_checked': triangle_checked,
        'triangle_examples': triple_results,
        'scope_caveat': 'Upper P5 universal star claim requires equal total counter counts.'}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
