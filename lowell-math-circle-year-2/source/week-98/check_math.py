#!/usr/bin/env python3
"""Independent Week 98 bootstrap-percolation checks.

Standard-library Python only. Run `python3 check_math.py` from any
working directory. All data are embedded: no input files are read, no files
are created or changed, and the JSON result goes to stdout. Assertions fail
on a disagreement. Coordinates are 1-based (row, column), top left first.
This checker was written independently of the packet author's checker.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
import json


class Board:
    def __init__(self, rows, columns=None):
        self.rows = rows
        self.columns = columns if columns is not None else rows
        self.size = self.rows * self.columns
        self.full = (1 << self.size) - 1
        self.cells = tuple(range(self.size))
        self.neighbors = []
        for i in self.cells:
            r, c = divmod(i, self.columns)
            mask = 0
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.columns:
                    mask |= 1 << (nr * self.columns + nc)
            self.neighbors.append(mask)

    def mask(self, coordinates):
        answer = 0
        for r, c in coordinates:
            assert 1 <= r <= self.rows and 1 <= c <= self.columns
            bit = 1 << ((r - 1) * self.columns + c - 1)
            assert not answer & bit, 'Repeated seed'
            answer |= bit
        return answer

    def coordinates(self, state):
        return [[i // self.columns + 1, i % self.columns + 1]
                for i in self.cells if state & (1 << i)]

    def legal(self, state):
        return tuple(i for i in self.cells
                     if not state & (1 << i)
                     and (state & self.neighbors[i]).bit_count() >= 2)

    def sequential(self, seeds, reverse=False):
        state = seeds
        sequence = []
        while moves := self.legal(state):
            chosen = moves[-1] if reverse else moves[0]
            state |= 1 << chosen
            sequence += self.coordinates(1 << chosen)
        return state, sequence

    def parallel(self, seeds):
        state = seeds
        layers = []
        while moves := self.legal(state):
            addition = sum(1 << i for i in moves)
            layers.append(self.coordinates(addition))
            state |= addition
        return state, layers

    def perimeter(self, state):
        # Each filled square starts with four unit sides. Each occupied
        # side-neighbor removes the one directed side from that square.
        # Counting both directions removes two for each shared edge.
        return sum(4 - (state & self.neighbors[i]).bit_count()
                   for i in self.cells if state & (1 << i))


def outcome(board, coordinates):
    seeds = board.mask(coordinates)
    final, sequence = board.sequential(seeds)
    parallel_final, layers = board.parallel(seeds)
    assert final == parallel_final
    assert board.sequential(seeds, reverse=True)[0] == final
    return {'seeds': board.coordinates(seeds),
            'final_count': final.bit_count(),
            'final_cells': board.coordinates(final),
            'legal_sequential_additions': sequence,
            'reverse_priority_legal_additions': board.sequential(seeds, reverse=True)[1],
            'parallel_layers': layers,
            'initial_perimeter': board.perimeter(seeds),
            'final_perimeter': board.perimeter(final)}


def removal_test(board, coordinates):
    record = outcome(board, coordinates)
    assert record['final_count'] == board.size
    trials = []
    for seed in coordinates:
        remaining = [s for s in coordinates if s != seed]
        after = outcome(board, remaining)
        assert after['final_count'] < board.size
        trials.append({'removed_seed': list(seed),
                       'final_count': after['final_count'],
                       'final_cells': after['final_cells']})
    record['one_seed_removals'] = trials
    return record


def main():
    b3, b4, b5 = Board(3), Board(4), Board(5)
    result = {}

    # Exact pictured non-task example: two rows and three columns.
    demo = outcome(Board(2, 3), [(1, 1), (2, 1), (2, 2)])
    assert demo['legal_sequential_additions'] == [[1, 2]]
    assert demo['final_count'] == 4
    result['opening_demo_both_bands'] = demo

    # Enumerate every placement of exactly three seeds on the 3x3 board.
    hist, examples, starts_by_order_count = Counter(), {}, Counter()
    @lru_cache(maxsize=None)
    def terminals_and_order_count(state):
        moves = b3.legal(state)
        if not moves:
            return frozenset([state]), 1
        ends, count = set(), 0
        for move in moves:
            child_ends, child_count = terminals_and_order_count(state | (1 << move))
            ends.update(child_ends)
            count += child_count
        return frozenset(ends), count

    for positions in combinations(b3.cells, 3):
        seeds = sum(1 << i for i in positions)
        ends, order_count = terminals_and_order_count(seeds)
        assert len(ends) == 1
        final = next(iter(ends))
        assert final == b3.parallel(seeds)[0]
        hist[final.bit_count()] += 1
        examples.setdefault(final.bit_count(), outcome(b3, b3.coordinates(seeds)))
        starts_by_order_count['multiple' if order_count > 1 else 'only_one'] += 1
    assert sum(hist.values()) == 84
    assert sorted(hist) == [3, 4, 6, 9]
    result['three_seeds_on_3x3'] = {
        'placements_checked': 84,
        'closure_size_histogram': dict(sorted(hist.items())),
        'witness_for_each_size': dict(sorted(examples.items())),
        'number_of_complete_orders': dict(starts_by_order_count)}

    # Stronger order-independence check: every subset, not just 3 seeds.
    for state in range(1 << b3.size):
        ends, _ = terminals_and_order_count(state)
        assert ends == frozenset([b3.parallel(state)[0]])
    result['all_3x3_states_order_independent'] = 512

    # Counterexamples to an unconditional requirement of two growth orders.
    no_moves = [(1, 1), (1, 2), (1, 3)]
    one_move = [(1, 1), (1, 2), (2, 1)]
    result['order_wording_edge_cases'] = {
        'zero_additions': outcome(b3, no_moves),
        'only_one_addition': outcome(b3, one_move)}
    assert len(result['order_wording_edge_cases']['zero_additions']['legal_sequential_additions']) == 0
    assert len(result['order_wording_edge_cases']['only_one_addition']['legal_sequential_additions']) == 1

    # All sets of <=4 seeds on 4x4. This establishes min=4 by enumeration.
    counts4 = {}
    for count in range(5):
        total = percolating = 0
        for positions in combinations(b4.cells, count):
            total += 1
            state = sum(1 << i for i in positions)
            percolating += b4.parallel(state)[0] == b4.full
        counts4[count] = {'checked': total, 'fill_board': percolating}
    assert all(counts4[k]['fill_board'] == 0 for k in range(4))
    assert counts4[4]['fill_board'] >= 3
    result['4x4_by_seed_count'] = counts4
    examples4 = [
        [(1, 1), (2, 2), (3, 3), (4, 4)],
        [(1, 4), (2, 3), (3, 2), (4, 1)],
        [(1, 1), (1, 3), (2, 4), (4, 1)],
    ]
    result['three_optimal_4x4_examples'] = [outcome(b4, s) for s in examples4]
    assert all(x['final_count'] == 16 for x in result['three_optimal_4x4_examples'])
    result['explicit_adult_4x4_example_verified'] = True

    # All 12,650 four-seed starts on 5x5, plus the smaller sizes.
    counts5 = {}
    for count in range(5):
        total = percolating = 0
        for positions in combinations(b5.cells, count):
            total += 1
            state = sum(1 << i for i in positions)
            percolating += b5.parallel(state)[0] == b5.full
        counts5[count] = {'checked': total, 'fill_board': percolating}
    assert all(record['fill_board'] == 0 for record in counts5.values())
    result['5x5_impossible_seed_counts'] = counts5

    # Construct optimal diagonal starts. The lower bound for arbitrary n
    # is supplied in math-answers.md; no finite enumeration proves it.
    diagonals = {}
    for n in (3, 4, 5, 10):
        answer = outcome(Board(n), [(i, i) for i in range(1, n + 1)])
        assert answer['final_count'] == n * n
        assert len(answer['parallel_layers']) == n - 1
        diagonals[n] = answer
    result['diagonal_constructions'] = diagonals

    # Exact pictured perimeter cases, immediately after filling the circle.
    center = (2, 2)
    perimeter_cases = []
    for seeds in ([(1, 2), (2, 1)],
                  [(1, 2), (2, 1), (2, 3)],
                  [(1, 2), (2, 1), (2, 3), (3, 2)]):
        before = b3.mask(seeds)
        k = (before & b3.neighbors[4]).bit_count()
        after = before | b3.mask([center])
        perimeter_cases.append({'seeds': seeds,
                                'filled_neighbors_of_circle': k,
                                'before': b3.perimeter(before),
                                'after_one_addition': b3.perimeter(after)})
    assert [(x['before'], x['after_one_addition']) for x in perimeter_cases] == [(8, 8), (12, 10), (16, 12)]
    result['pictured_perimeter_cases'] = perimeter_cases

    # Exhaust every empty-cell addition on every 3x3 state, including
    # boundary and corner cells, to test the local formula and legality.
    additions = legal_additions = 0
    for state in range(1 << b3.size):
        for cell in b3.cells:
            if state & (1 << cell):
                continue
            additions += 1
            k = (state & b3.neighbors[cell]).bit_count()
            delta = b3.perimeter(state | (1 << cell)) - b3.perimeter(state)
            assert delta == 4 - 2 * k
            if k >= 2:
                legal_additions += 1
                assert delta <= 0
    result['perimeter_formula_exhaustive_check'] = {
        'all_empty_cell_additions': additions,
        'legal_additions': legal_additions,
        'all_deltas_equal_4_minus_2k': True}

    # Exact four-seed diagram and the specifically requested rotation.
    four = [(1, 1), (1, 2), (2, 3), (3, 3)]
    rotated = [(1, 3), (2, 3), (3, 1), (3, 2)]
    result['printed_indispensable_four'] = removal_test(b3, four)
    result['rotated_indispensable_four'] = removal_test(b3, rotated)
    assert [x['final_count'] for x in result['printed_indispensable_four']['one_seed_removals']] == [6, 3, 3, 6]
    assert [x['final_count'] for x in result['rotated_indispensable_four']['one_seed_removals']] == [6, 3, 6, 3]

    minimal_fours = []
    for positions in combinations(b3.cells, 4):
        state = sum(1 << i for i in positions)
        if b3.parallel(state)[0] != b3.full:
            continue
        if all(b3.parallel(state ^ (1 << i))[0] != b3.full for i in positions):
            minimal_fours.append(b3.coordinates(state))
    assert b3.coordinates(b3.mask(four)) in minimal_fours
    assert b3.coordinates(b3.mask(rotated)) in minimal_fours
    result['all_indispensable_percolating_four_seed_starts_3x3'] = minimal_fours

    # Check the alternate reading "each seed is needed for this closure."
    # On this particular 3x3 four-seed task, it yields no extra examples:
    # every four-seed set minimal for its closure actually fills the board.
    nonpercolating_irredundant_fours = []
    for positions in combinations(b3.cells, 4):
        state = sum(1 << i for i in positions)
        final = b3.parallel(state)[0]
        if final != b3.full and all(
                b3.parallel(state ^ (1 << i))[0] != final for i in positions):
            nonpercolating_irredundant_fours.append(b3.coordinates(state))
    assert nonpercolating_irredundant_fours == []
    result['nonpercolating_irredundant_four_seed_starts_3x3'] = []

    result['status'] = 'PASS: all embedded mathematical assertions verified'
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
