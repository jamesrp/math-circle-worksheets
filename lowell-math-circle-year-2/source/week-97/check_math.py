#!/usr/bin/env python3
"""Independent Week 97 checks. Standard library only; no writer code imported.

Finite checks verify the activity data, not the universal theorem. See
the facilitator guide for proofs of periodicity and the prime collision theorem.
"""
from collections import defaultdict
from itertools import combinations
import json
from pathlib import Path
import re


def leftover(n, bundle):
    assert n >= 0 and bundle > 0
    count = sum(n for _ in range(n))  # square as n rows of n counters
    while count >= bundle:
        count -= bundle
    return count


def inventory(bundle):
    groups = defaultdict(list)
    for n in range(bundle):
        remainder = leftover(n, bundle)
        assert remainder == divmod(n * n, bundle)[1]
        groups[remainder].append(n)
    return dict(sorted(groups.items()))


EXPECTED = {
    3: {0:[0], 1:[1,2]},
    5: {0:[0], 1:[1,4], 4:[2,3]},
    7: {0:[0], 1:[1,6], 2:[3,4], 4:[2,5]},
    8: {0:[0,4], 1:[1,3,5,7], 4:[2,6]},
    9: {0:[0,3,6], 1:[1,8], 4:[2,7], 7:[4,5]},
    11:{0:[0], 1:[1,10], 3:[5,6], 4:[2,9], 5:[4,7], 9:[3,8]},
    15:{0:[0], 1:[1,4,11,14], 4:[2,7,8,13], 6:[6,9], 9:[3,12], 10:[5,10]},
}
FACTS = [0,1,4,9,16,25,36,49,64,81,100,121,144,169,196,225]


def main():
    for n, square in enumerate(FACTS):
        assert sum(n for _ in range(n)) == square
    source_candidates = [
        Path(__file__).parent / 'draft/src/students.tex',
        Path(__file__).parent / 'student/students.tex',
    ]
    source = next((p for p in source_candidates if p.exists()), None)
    printed_fact_count = None
    if source:
        facts = re.findall(r'\\support\{(\d+)\}\{(\d+)\}', source.read_text())
        assert facts, 'No fact cards found in source'
        for n, square in facts:
            assert FACTS[int(n)] == int(square), (n, square)
        printed_fact_count = len(facts)
    actual = {m:inventory(m) for m in EXPECTED}
    assert actual == EXPECTED
    pairs = [(a,b) for a,b in combinations(range(5),2) if leftover(a,5)==leftover(b,5)]
    assert pairs == [(1,4),(2,3)]
    assert sorted(set(range(5))-set(actual[5])) == [2,3]
    assert [r for r,ns in actual[7].items() if len(ns)==1] == [0]
    assert [r for r,ns in actual[7].items() if len(ns)==2] == [1,2,4]
    maxima = {m:max(map(len,groups.values())) for m,groups in actual.items()}
    assert [maxima[m] for m in (7,8,9)] == [2,4,3]
    assert actual[15][1] == [1,4,11,14] and maxima[15] == 4
    assert [r for r,ns in actual[15].items() if len(ns)==4] == [1,4]
    # Every support input on P5 and many beyond it reduce to the same finite set.
    for n in range(701):
        r = n % 7
        q = n // 7
        assert n*n-r*r == 7*q*(7*q+2*r)
        assert n*n % 7 == r*r % 7
    # Check exact prime collision criterion, including equal inputs and zero.
    primes = [p for p in range(3,100,2) if all(p%d for d in range(2,p))]
    for p in primes:
        groups = inventory(p)
        assert len(groups) == (p+1)//2 and groups[0] == [0]
        squares = set(groups) - {0}
        nonsquares = set(range(1,p)) - squares
        assert len(squares) == len(nonsquares)
        for a in range(1,p):
            assert len({a*b % p for b in range(1,p)}) == p-1
            for b in range(1,p):
                assert ((a*b % p) in squares) == ((a in squares) == (b in squares))
        for a in range(p):
            for b in range(p):
                assert (a*a%p==b*b%p) == (a==b or a+b==p)
    assert [len(actual[m]) for m in (3,5,7,11)] == [2,3,4,6]
    assert [len(actual[m]) for m in (8,9,15)] == [3,4,6]
    # Explicit failures of extending the prime collision criterion to composites.
    for m,a,b in [(8,1,3),(9,0,3),(15,1,4)]:
        assert a*a%m == b*b%m and a!=b and a+b!=m
    print(json.dumps({'status':'PASS','inventories':actual,
                      'fact_cards_checked':printed_fact_count,
                      'prime_criteria_tested_through':97,
                      'periodicity_inputs_checked_through':700},indent=2))

if __name__ == '__main__':
    main()
