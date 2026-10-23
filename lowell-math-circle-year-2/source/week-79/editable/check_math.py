#!/usr/bin/env python3
"""Independent Week 79 arithmetic and diagram checks; author code is not imported.

Finite replay checks are evidence for the handwritten induction in review-math.md,
not a computational assertion about an actually completed infinite process.
"""
import os
import hashlib
import json
import re
from pathlib import Path

RUN = Path(__file__).resolve().parent
GUIDE = RUN / 'guide/facilitator.tex'


def replay(days, changed=False):
    a, b = set(), set()
    snapshots = [(set(), set())]
    births, moves = {}, {}
    for day in range(1, days + 1):
        new = (2 * day - 1, 2 * day)
        a.update(new)
        births.update({label: day for label in new})
        moved = max(new) if changed else min(a)
        a.remove(moved)
        b.add(moved)
        moves[moved] = day
        snapshots.append((a.copy(), b.copy()))
    return snapshots, births, moves


def reachable_targets(days):
    """Every B a chooser can reach after `days` days, by exhaustive search over the moves."""
    found = set()

    def go(day, a, b):
        if day > days:
            found.add(b)
            return
        a = a | {2 * day - 1, 2 * day}
        for card in a:
            go(day + 1, a - {card}, b | {card})

    go(1, frozenset(), frozenset())
    return found


def short_days(target):
    """Days d by which fewer than d of the target's cards have entered A (cards 1 to 2d)."""
    return [d for d in range(1, len(target) + 1) if sum(c <= 2 * d for c in target) < d]


def greedy(target):
    """Each day move the smallest target card in A, if there is one; return the moves or None."""
    a, moves = set(), []
    for day in range(1, len(target) + 1):
        a.update((2 * day - 1, 2 * day))
        wanted = sorted(a & set(target))
        if not wanted:
            return None
        a.remove(wanted[0])
        moves.append(wanted[0])
    return moves


def catalan(n):
    from math import comb
    return comb(2 * n, n) // (n + 1)


def run():
    ordinary, births, moves = replay(500)
    changed, births_changed, moves_changed = replay(500, changed=True)
    for day, ((a, b), (ca, cb)) in enumerate(zip(ordinary, changed)):
        assert a == set(range(day + 1, 2 * day + 1))
        assert b == set(range(1, day + 1))
        assert ca == set(range(1, 2 * day, 2))
        assert cb == set(range(2, 2 * day + 1, 2))
        assert len(a) == len(b) == len(ca) == len(cb) == day
        assert not a.intersection(b)
        assert a.union(b) == set(range(1, 2 * day + 1))
        if day > 0:
            assert day + 1 in a  # Counterexample to a single finishing day.
            assert max(1 if k in a else 0 for k in range(1, 2 * day + 1)) == 1
    assert ordinary[0] == (set(), set())
    assert 1 not in ordinary[0][0]  # Located day-0 witness defect in guide.
    assert not any(ordinary[0][0])  # Supremum of its indicator is 0, not 1.
    for label in range(1, 1001):
        assert births[label] == (label + 1) // 2
        assert births_changed[label] == (label + 1) // 2
        if label <= 500:
            assert moves[label] == label
            for day in range(label, 501):
                assert label in ordinary[day][1]
        if label % 2 == 0:
            assert moves_changed[label] == label // 2
        else:
            assert label not in moves_changed
    assert ordinary[10] == (set(range(11, 21)), set(range(1, 11)))
    assert births[8] == 4 and moves[8] == 8
    assert all(8 in ordinary[day][0] for day in range(4, 8))
    # Problem 4 (chosen moves): exhaustive search over every sequence of choices.
    tex_path = RUN / 'student/students.tex'
    tex = tex_path.read_text()
    rows = re.findall(r'\\foreach \\row/\\cards in \{(.*)\} \{', tex)
    assert len(rows) == 1
    targets = [tuple(int(c) for c in grp.split(',')) for grp in re.findall(r'\d/\{([0-9,]+)\}', rows[0])]
    assert targets == [(1, 3, 5, 7, 9, 11), (2, 3, 5, 7, 8, 11), (1, 4, 6, 9, 11, 12)]
    reach = {n: reachable_targets(n) for n in range(1, 8)}
    for n, sets in reach.items():
        assert len(sets) == catalan(n + 1)  # 2, 5, 14, 42, 132, 429, 1430
        for t in sets:
            assert not short_days(sorted(t)) and greedy(sorted(t)) is not None
    from itertools import combinations
    for n in range(1, 8):  # The counting criterion is exact: no unreachable set passes it.
        for t in combinations(range(1, 2 * n + 1), n):
            assert (frozenset(t) in reach[n]) == (not short_days(t))
    problem_4 = {}
    for t in targets:
        ok = frozenset(t) in reach[6]
        problem_4[' '.join(map(str, t))] = {'reachable': ok, 'moves_days_1_to_6': greedy(t),
                                             'first_short_day': (short_days(t) or [None])[0]}
    assert [v['reachable'] for v in problem_4.values()] == [True, True, False]
    assert problem_4['1 3 5 7 9 11']['moves_days_1_to_6'] == [1, 3, 5, 7, 9, 11]
    assert problem_4['2 3 5 7 8 11']['moves_days_1_to_6'] == [2, 3, 5, 7, 8, 11]
    assert problem_4['1 4 6 9 11 12']['first_short_day'] == 4
    assert all(c in reach[6] for c in (frozenset(range(1, 7)), frozenset(range(2, 13, 2))))
    # Problem 2 now asks for both days under each printed card.
    p2 = re.findall(r'\\foreach \\x/\\v in \{([^}]*)\}', tex)
    assert [int(pair.split('/')[1]) for pair in p2[0].split(',')] == [3, 6, 10, 20]
    assert tex.count('{Enters day}') == 1 and tex.count('{Moves day}') == 1
    answers = {
        'problem_1': 'Both bowls have n cards after each completed day; no unequal counts.',
        'problem_2': {str(k): {'enters': births[k], 'moves': moves[k]} for k in (3, 6, 10, 20)},
        'problem_3': 'Identical counts; distinct memberships, e.g. after day 1 A={2} versus A={1}.',
        'problem_4': problem_4,
        'problem_5': 'Ordinary rule: empty A/all positive labels B. Changed rule: odds A/evens B. Neither complete limiting configuration is any finite-day configuration; under the changed rule every card present on a finite day already sits where it settles.',
    }
    for day in range(1, 301):  # Problem 5, changed rule: present cards already sit where they settle.
        ca, cb = changed[day]
        assert all(k % 2 == 1 for k in ca) and all(k % 2 == 0 for k in cb)
        a, b = ordinary[day]
        assert a and all(k <= 2 * day for k in a)  # Smallest rule: A is never empty on a day N >= 1.
    # The actual source's first legal attempt and print materials.
    cards = re.findall(r'\\card\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}', tex)
    assert cards == [('8.45', '1.9', '1'), ('9.65', '1.9', '2'), ('15.3', '1.9', '2'), ('15.3', '0', '1')]
    assert '\\foreach \\r in {0,...,5}' in tex
    assert '\\foreach \\c in {0,...,3}' in tex
    labels = [4 * row + col + 1 for row in range(6) for col in range(4)]
    assert labels == list(range(1, 25))
    assert '(3*\\c,-3*\\r) rectangle (3*\\c+3,-3*\\r-3)' in tex
    assert 'x=1cm,y=1cm' in tex  # Equal scaling: cards are 30 mm squares.
    mat_width_mm, mat_height_mm, card_side_mm = 180, 96, 30
    assert (mat_width_mm // card_side_mm) * (mat_height_mm // card_side_mm) >= 12
    reviewed_files = [tex_path, GUIDE]
    result = {
        'status': 'PASS',
        'finite_replay_days_per_rule': 500,
        'problem_4_exhaustive_days': 7,
        'labels_birth_checked': 1000,
        'answers': answers,
        'materials': {'labels': labels, 'card_side_mm': 30, 'each_mat_capacity_without_overlap': 18},
        'reviewed_sha256': {str(p.relative_to(RUN)): hashlib.sha256(p.read_bytes()).hexdigest() for p in reviewed_files},
        'limits': 'Proof of the formulas and quantifier distinctions is by induction/explicit witnesses in the review; finite replays do not complete infinitely many days. Physical print fit and classroom procedure are untested.',
    }
    Path(os.environ.get('INFINITY_CHECK_OUT', 'math-check-results.json')).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
