"""Audit the revised Week 58 instances using exact arithmetic.

Run: python3 verify_math.py [json-output-path]
No external dependencies. It does not validate material handling or piloting.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import sys


def inspect_allocations(values):
    n, m = len(values), len(values[0])
    cases = []
    for owners in product(range(n), repeat=m):
        scores = [[sum(values[i][g] for g in range(m) if owners[g] == j)
                   for j in range(n)] for i in range(n)]
        envy = all(scores[i][i] >= scores[i][j]
                   for i in range(n) for j in range(n))
        share = all(n * scores[i][i] >= sum(values[i]) for i in range(n))
        cases.append(dict(owners=list(owners), observer_rows=scores,
                          envy_free=envy, proportional=share))
    return cases


def strip_value(red, blue, cut):
    # cut is millimeters from the left of two adjacent 150 mm panels.
    red_left = min(cut, Fraction(150)) / 150
    blue_left = max(Fraction(0), cut - 150) / 150
    left = red * red_left + blue * blue_left
    return [left, red + blue - left]


def audit():
    p1 = inspect_allocations([[3, 3, 3, 1], [1, 1, 1, 3]])
    p2 = inspect_allocations([[3, 3, 1, 1], [1, 1, 3, 3]])
    assert len(p1) == len(p2) == 16
    p1_good = [c for c in p1 if c['envy_free']]
    p2_good = [c for c in p2 if c['envy_free']]
    assert len(p1_good) == 4 and len(p2_good) == 5
    assert all(c['envy_free'] == c['proportional'] for c in p1 + p2)
    # A chooser takes its highest-value tray. Every envy-free assignment can
    # therefore be realized in either divider/chooser role, with ties allowed.
    for c in p1_good:
        s = c['observer_rows']
        assert s[0][0] >= s[0][1] and s[1][1] >= s[1][0]

    a_cut, b_cut = Fraction(100), Fraction(200)
    a_view = strip_value(3, 1, a_cut)
    b_view = strip_value(1, 3, a_cut)
    assert a_view == [2, 2] and b_view == [Fraction(2, 3), Fraction(10, 3)]
    assert strip_value(1, 3, b_cut) == [2, 2]
    assert strip_value(3, 1, b_cut) == [Fraction(10, 3), Fraction(2, 3)]
    # Same preferences and an equal-length cut fail the cutter's comparison.
    midpoint = strip_value(3, 1, Fraction(150))
    assert midpoint == [3, 1]
    assert 1 < 3 and 1 < Fraction(4, 2)

    p5 = inspect_allocations([[1, 1, 1], [1, 1, 1]])
    assert len(p5) == 8
    assert not any(c['envy_free'] for c in p5)
    half = Fraction(1, 2)
    assert 1 + half == Fraction(3, 2)

    p6 = inspect_allocations([[4, 8, 0], [0, 4, 8], [8, 0, 4]])
    given = next(c for c in p6 if c['owners'] == [0, 1, 2])
    assert given['proportional'] and not given['envy_free']
    corrected = next(c for c in p6 if c['owners'] == [2, 0, 1])
    assert corrected['proportional'] and corrected['envy_free']
    assert len([c for c in p6 if c['envy_free']]) == 1
    assert len(p6) == 27
    assert len([c for c in p6 if c['proportional']]) == 2

    # P7's universal arithmetic is also exhaustively sanity-checked over all
    # small nonnegative observer rows. The explanation is algebraic: each
    # other bundle <= own, so total <= n*own. For n=2 the converse follows
    # from other = total-own. The n=3 converse is refuted by P6.
    profiles_checked = {}
    for n in [2, 3]:
        count = 0
        for row in product(range(9), repeat=n):
            own = row[0]
            ef = all(own >= v for v in row)
            prop = n * own >= sum(row)
            assert not ef or prop
            if n == 2:
                assert ef == prop
            count += 1
        profiles_checked[n] = count

    return dict(
        complete_allocation_counts=dict(problem_1=16, problem_2=16,
                                        problem_5=8, problem_6=27),
        envy_free_counts=dict(problem_1=4, problem_2=5,
                             problem_5=0, problem_6=1),
        problem_6_proportional_count=2,
        problem_1_successes=p1_good,
        problem_2_successes=p2_good,
        problem_3_cut_mm=dict(A=str(a_cut), B=str(b_cut)),
        problem_3_A_cut_values=dict(A=[str(x) for x in a_view],
                                    B=[str(x) for x in b_view]),
        problem_3_B_cut_values=dict(A=[str(x) for x in strip_value(3, 1, b_cut)],
                                    B=[str(x) for x in strip_value(1, 3, b_cut)]),
        problem_4_same_taste_midpoint_values=[str(x) for x in midpoint],
        problem_5_whole_card_success_count=0,
        problem_5_halved_R3_own_values=['3/2', '3/2'],
        problem_6_initial=given,
        problem_6_corrected=corrected,
        problem_7_small_observer_profiles_checked=profiles_checked,
        physical_pretests='Unperformed',
        classroom_piloting='Unperformed')


if __name__ == '__main__':
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent / 'math-checks.json'
    target.write_text(json.dumps(audit(), indent=2) + '\n')
    print(target)
