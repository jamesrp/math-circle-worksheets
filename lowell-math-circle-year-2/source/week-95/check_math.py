#!/usr/bin/env python3
"""Independent Week 95 finite checks; Python standard library only.

Run: python3 independent_check.py
No writer verification code, local dependencies, random draws, or PDF parsing.
Exact enumeration checks finite examples; general arguments are in
math-answer-key.md and are not replaced by these finite checks.
"""
from collections import Counter
from fractions import Fraction as F
from functools import reduce
from itertools import combinations
from math import comb
import json


def product(values):
    return reduce(lambda x, y: x*y, values, F(1))


def support(N, M, n):
    assert 0 <= M <= N and 0 <= n <= N
    return tuple(range(max(0, M+n-N), min(M, n)+1))


def law(N, M, n):
    return {r: F(comb(M, r)*comb(N-M, n-r), comb(N, n))
            for r in support(N, M, n)}


def enumerated_law(N, M, n):
    # Hold marked identities fixed. Enumerate actual distinct second catches.
    marked = set(range(M))
    counts = Counter(len(marked.intersection(catch))
                     for catch in combinations(range(N), n))
    return {r: F(count, comb(N, n)) for r, count in counts.items()}


def witness(N, M, n, r):
    assert r in support(N, M, n)
    first = set(range(M))
    second = set(range(r)) | set(range(M, M+n-r))
    assert len(first) == M and len(second) == n
    assert len(first & second) == r and len(first | second) == M+n-r
    assert first | second <= set(range(N))
    return sorted(first), sorted(second)


def ratio(M, n, r):
    return F(M*n, r) if r else None


def expected(dist):
    return sum((r*p for r, p in dist.items()), F(0))


def likelihood(N, M, n, records):
    dist = law(N, M, n)
    return product(dist.get(r, F(0)) for r in records)


def optimal_splits(N, budget):
    options = {(M, budget-M): F(M*(budget-M), N)
               for M in range(budget+1)
               if M <= N and budget-M <= N}
    best = max(options.values())
    return sorted(pair for pair, value in options.items() if value == best), best


def main():
    # An independently enumerated broad finite grid, including empty/full catches.
    finite_models = 0
    for N in range(1, 13):
        for M in range(N+1):
            for n in range(N+1):
                dist = enumerated_law(N, M, n)
                assert dist == law(N, M, n)
                assert sum(dist.values(), F(0)) == 1
                assert tuple(sorted(dist)) == support(N, M, n)
                mean = expected(dist)
                assert mean == F(M*n, N)
                variance = sum(((r-mean)**2*p for r, p in dist.items()), F(0))
                if N > 1:
                    assert variance == F(n*M*(N-M)*(N-n), N*N*(N-1))
                for r in dist:
                    witness(N, M, n, r)
                finite_models += 1

    # Shared visual, independent explicit identities/marks.
    population = set('ABCDEF')
    first, second = set('AC'), set('CDF')
    assert population-first == set('BDEF')
    assert population-second == set('ABE')
    assert first & second == set('C')
    assert len(first | second) == 4
    assert first & (population-second) == set('A')

    # Grades 2-3, Problem 1: all printed populations feasible; no fixed outcome.
    assert all(support(N, 4, 4) == (0, 1, 2, 3, 4) for N in range(8, 21))
    # Problems 2-3 exact identities, candidate totals, and adding unseen objects.
    a, b = set('ABCDE'), set('BDEFG')
    assert len(a & b) == 3 and len(a | b) == 7
    candidates = [N for N in (6, 7, 8, 12, 20) if 3 in support(N, 5, 5)]
    assert candidates == [7, 8, 12, 20]
    assert len(set('ABCDE') | set('FGHIJ')) == 10
    for N in (10, 12, 20, 100, 10000):
        witness(N, 5, 5, 0)
    # Problems 4-5: same series possible at BOTH totals, including zero overlap.
    younger_series = [2, 1, 3, 1, 2, 0]
    for N in (8, 16):
        assert likelihood(N, 4, 4, younger_series) > 0
        witness(N, 4, 4, 0)
        witness(N, 4, 4, 3)
    per_round = [8 if law(8, 4, 4)[r] > law(16, 4, 4)[r] else 16
                 for r in younger_series]
    assert per_round == [8, 16, 8, 16, 8, 16]
    lr = likelihood(8, 4, 4, younger_series)/likelihood(16, 4, 4, younger_series)
    assert lr == F(308915776, 543547125) < 1
    # Problems 6-7 all overlaps, including impossible plausible-range records.
    assert support(6, 5, 4) == (3, 4)
    assert support(7, 5, 4) == (2, 3, 4)
    assert support(8, 5, 4) == (1, 2, 3, 4)
    assert support(12, 5, 4) == (0, 1, 2, 3, 4)
    for N in (6, 7, 8):
        witness(N, 5, 4, 4)
        assert 0 not in support(N, 5, 4)

    # Grades 4-5 P1 through P5.
    assert all(support(N, 6, 6) == tuple(range(7)) for N in range(12, 25))
    assert 2 not in support(9, 6, 6) and 2 in support(10, 6, 6)
    assert 0 not in support(11, 6, 6) and 0 in support(12, 6, 6)
    assert ratio(6, 6, 2) == 18
    witness(10, 6, 6, 2)
    older_series = [1, 2, 3, 2, 0]
    assert [ratio(6, 6, r) for r in older_series] == [36, 18, 12, 18, None]
    assert all(likelihood(N, 6, 6, older_series) > 0 for N in (12, 18, 24, 36, 100))
    assert all(likelihood(N, 6, 6, older_series) == 0 for N in range(6, 12))
    assert F(sum(older_series), len(older_series)) == F(8, 5)
    assert F(36, 1)/F(8, 5) == F(45, 2)
    witness(12, 6, 6, 0)
    witness(18, 6, 6, 0)

    # Exact ratio limitation examples, not claims about all estimator quality.
    d18 = law(18, 6, 6)
    assert expected(d18) == 2 and d18[0] == F(11, 221)
    conditional_ratio_mean = sum((ratio(6, 6, r)*p for r, p in d18.items() if r), F(0))/(1-d18[0])
    assert conditional_ratio_mean == F(305797, 14700) != 18
    # A positive overlap can yield a noninteger or even an impossible total.
    assert ratio(6, 6, 5) == F(36, 5)
    assert ratio(6, 6, 5) != int(ratio(6, 6, 5))
    assert ratio(4, 4, 3) == F(16, 3)  # noninteger estimate; lower bound is 5

    # P6-P7 exact fixed-budget optima for every printed budget.
    assert optimal_splits(24, 12) == ([(6, 6)], F(3, 2))
    assert optimal_splits(24, 13) == ([(6, 7), (7, 6)], F(7, 4))
    assert optimal_splits(24, 20) == ([(10, 10)], F(25, 6))
    for budget in range(2, 25):
        actual, best = optimal_splits(24, budget)
        low, high = budget//2, (budget+1)//2
        assert actual == sorted(set([(low, high), (high, low)]))
        assert best == F(low*high, 24)
    # Fixed finite sampling expectation confirms budget 12 comparisons directly
    # via combinatorial counts, avoiding 24-choose-12 physical enumeration.
    assert all(expected(law(24, M, 12-M)) == F(M*(12-M), 24) for M in range(13))

    # P8 lost marks: independent retention with q=1/2 on M=3, N=8, n=3.
    # Enumerate ALL second subsets and ALL 2**M equiprobable retained-mark sets.
    N, M, n = 8, 3, 3
    first = set(range(M))
    outcomes = []
    for mask in range(2**M):
        retained = {i for i in first if mask & (1 << i)}
        for catch_tuple in combinations(range(N), n):
            catch = set(catch_tuple)
            true_R, observed_R = len(first & catch), len(retained & catch)
            assert observed_R <= true_R
            if observed_R:
                assert ratio(M, n, observed_R) >= ratio(M, n, true_R)
            outcomes.append(observed_R)
    assert F(sum(outcomes), len(outcomes)) == F(1, 2)*F(M*n, N)

    report = {
        'status': 'PASS', 'independently_enumerated_finite_models': finite_models,
        'shared_visual': {'population': 'ABCDEF', 'first': 'AC', 'second': 'CDF', 'overlap': 'C'},
        'grades_2_3': {
            'P1': 'variable live outcomes; possible R=0..4',
            'P2_min': 7, 'P2_possible_listed_totals': candidates,
            'P3_min': 10, 'P3_max': 'none; add any number of unseen identities',
            'P4_single_round_likelihood_choices': per_round,
            'P4_series_likelihood_ratio_8_over_16': str(lr),
            'P4_series': 'both compatible; weak model evidence for 16, no forced total',
            'P5': 'both N=8 and N=16 permit R=0 and R=3',
            'P6': {str(N): support(N, 5, 4) for N in (6, 8, 12)},
            'P7': {str(N): {'possible': support(N, 5, 4), 'impossible_in_0_to_4': sorted(set(range(5))-set(support(N, 5, 4)))} for N in (6, 7, 8)},
        },
        'grades_4_5': {
            'P1': 'variable live outcomes; possible R=0..6',
            'P2_min_A_B': [10, 12], 'P2_max': 'none',
            'P3_guess': 18, 'P3_counterexample_total': 10,
            'P4_guesses': [36, 18, 12, 18, None], 'P4_compatible_populations': 'every integer N>=12',
            'P4_series_probability_at_18': str(likelihood(18, 6, 6, older_series)),
            'P4_pooled_ratio_if_used': '22.5, only an estimate',
            'P5_example_totals': [12, 18],
            'P6_optimum': [6, 6], 'P6_expected_overlap': '3/2',
            'P7_budget_13': [[6, 7], [7, 6]], 'P7_budget_20': [10, 10],
            'P7_rule': 'floor(s/2), ceil(s/2)',
            'P8': 'lost marks weakly lower detected overlap; inflate positive ratio or make it undefined',
        },
        'ratio_warning': {'N': 18, 'M': 6, 'n': 6, 'probability_zero': str(d18[0]),
                          'conditional_mean_ratio_given_positive': str(conditional_ratio_mean)},
        'not_established': ['infinite-case proof by finite enumeration alone', 'physical uniformity', 'classroom piloting'],
    }
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
