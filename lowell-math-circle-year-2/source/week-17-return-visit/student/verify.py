#!/usr/bin/env python3
"""Exact mathematical checks for the Week 17 student draft; standard library only."""
import itertools
import json
import sys


def rows(limit):
    for length in range(limit + 1):
        yield from map(''.join, itertools.product('RB', repeat=length))


def run(word, transitions, start=0):
    state = start
    for card in word:
        state = transitions[state]['RB'.index(card)]
    return state


def collision(red_moves):
    seen = {}
    state = 0
    for count in range(len(red_moves) + 1):
        if state in seen:
            return seen[state], count
        seen[state] = count
        state = red_moves[state]
    raise AssertionError('Pigeonhole collision missing')


sample = [(0, 1), (0, 1)]  # X=0, Y=1; R resets to X, B moves to Y.
target_rr = [(1, 0), (2, 0), (2, 2)]
parity = [(1, 2), (0, 3), (3, 0), (2, 1)]  # even/even=0
tested = list(rows(12))
for word in tested:
    assert (run(word, sample) == 1) == word.endswith('B')
    assert (run(word, target_rr) == 2) == ('RR' in word)
    assert (run(word, parity) == 0) == (word.count('R') % 2 == word.count('B') % 2 == 0)

assert [run(word, sample) for word in ['', 'R', 'RB', 'RBB']] == [0, 0, 1, 1]

# Two-state machines cannot meet RR's required behavior, even on these short tests.
two_state_total = two_state_pass = 0
short_rows = list(rows(4))
for transition_flat in itertools.product(range(2), repeat=4):
    transitions = [transition_flat[:2], transition_flat[2:]]
    for outputs in itertools.product([False, True], repeat=2):
        for start in range(2):
            two_state_total += 1
            if all(outputs[run(word, transitions, start)] == ('RR' in word) for word in short_rows):
                two_state_pass += 1
assert two_state_pass == 0

# A shared continuation separates each pair of the four parity histories.
parity_histories = ['', 'R', 'B', 'RB']
parity_witnesses = []
for left, right in itertools.combinations(parity_histories, 2):
    suffix = ('R' if left.count('R') % 2 else '') + ('B' if left.count('B') % 2 else '')
    assert run(left + suffix, parity) == 0
    assert run(right + suffix, parity) != 0
    parity_witnesses.append({'left': left, 'right': right, 'common_ending': suffix})

# Every possible red-transition function of size 1 through 6 has the collision
# used in the all-length argument. Applying any common blue ending then keeps
# the machine states equal, while the required equal-count answers differ.
red_functions = 0
collision_examples = []
for size in range(1, 7):
    for red_moves in itertools.product(range(size), repeat=size):
        i, j = collision(red_moves)
        assert 0 <= i < j <= size
        red_functions += 1
        if len(collision_examples) < 6:
            collision_examples.append({'states': size, 'i': i, 'j': j})
        # The histories finish in exactly the same state.
        transitions = [(red_moves[k], (k + 1) % size) for k in range(size)]
        assert run('R' * i, transitions) == run('R' * j, transitions)
        assert run('R' * i + 'B' * i, transitions) == run('R' * j + 'B' * i, transitions)
        assert i == ('B' * i).count('B')
        assert j != ('B' * i).count('B')

report = {
    'tested_rows_per_constructed_machine': len(tested),
    'maximum_row_length': 12,
    'worked_example': {'input': 'RBB', 'states_in_order': ['X', 'X', 'Y', 'Y'], 'output': 'YES'},
    'RR_detector_minimum_states': 3,
    'two_state_machines_checked': two_state_total,
    'two_state_machines_meeting_RR_tests': two_state_pass,
    'parity_machine_minimum_states': 4,
    'parity_pair_witnesses': parity_witnesses,
    'printed_parity_rows_required_outputs': {
        word or '(empty)': run(word, parity) == 0
        for word in ['', 'R', 'RB', 'RRBB', 'BBR', 'BRBR']
    },
    'red_transition_functions_checked_for_collision': red_functions,
    'equal_count_general_argument': (
        'For m states, the m+1 all-red histories force R^i and R^j to share a state, '
        '0 <= i < j <= m. Appending i blue cards gives equal resulting states but '
        'different required answers. This proves failure for all finite m, '
        'rather than claiming finite enumeration proves the unbounded theorem.'
    ),
    'status': 'All assertions passed. Physical procedures and classroom use untested.'
}
if len(sys.argv) != 2:
    raise SystemExit('Usage: python3 verify.py OUTPUT.json')
with open(sys.argv[1], 'w') as out:
    json.dump(report, out, indent=2)
print(json.dumps({key: report[key] for key in ['tested_rows_per_constructed_machine', 'two_state_machines_checked', 'red_transition_functions_checked_for_collision', 'status']}, indent=2))
