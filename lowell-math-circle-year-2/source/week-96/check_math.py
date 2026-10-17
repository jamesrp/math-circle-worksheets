#!/usr/bin/env python3
"""Independent Week 96 audit; Python 3 standard library only.

Run anywhere: python3 independent-check_math.py [--json answers.json]
Data were transcribed from the rendered drafts, not the writer's verifier.
Routes are sorted-multiset state paths: exchanging equal cards or reversing
factor order is not a new route. This convention is for this audit only.
"""
import argparse
import itertools
import json
import math
from collections import Counter
from functools import lru_cache
from pathlib import Path


def divisors(n):
    assert n > 0
    return [d for d in range(1, n + 1) if n % d == 0]


def prime_factors(n):
    result = []
    candidate = 2
    while candidate * candidate <= n:
        while n % candidate == 0:
            result.append(candidate)
            n //= candidate
        candidate += 1
    if n > 1:
        result.append(n)
    return tuple(result)


def successors(state):
    result = set()
    for i, value in enumerate(state):
        for a in range(2, math.isqrt(value) + 1):
            if value % a == 0:
                nxt = tuple(sorted(state[:i] + state[i + 1:] + (a, value // a)))
                assert math.prod(nxt) == math.prod(state)
                assert len(nxt) == len(state) + 1
                result.add(nxt)
    return sorted(result)


@lru_cache(None)
def routes(state):
    next_states = successors(state)
    if not next_states:
        return ((state,),)
    return tuple((state,) + route for nxt in next_states for route in routes(nxt))


def subbags(tokens):
    counts = Counter(tokens)
    primes = sorted(counts)
    results = []
    for exponents in itertools.product(*(range(counts[p] + 1) for p in primes)):
        chosen = tuple(p for p, e in zip(primes, exponents) for _ in range(e))
        results.append({'tokens': chosen, 'value': math.prod(chosen)})
    # Independently enumerate subsets of the physical tokens, then forget labels.
    physical_values = {math.prod(tokens[i] for i in range(len(tokens)) if mask >> i & 1)
                       for mask in range(1 << len(tokens))}
    values = [entry['value'] for entry in results]
    assert len(values) == len(set(values))
    assert sorted(values) == sorted(physical_values) == divisors(math.prod(tokens))
    assert len(values) == math.prod(e + 1 for e in counts.values())
    return sorted(results, key=lambda row: row['value'])


def multiplicative_partitions(n, least=2):
    """Nondecreasing factors >1 whose product is n, including the one-factor case."""
    if n >= least:
        yield (n,)
    for first in range(least, math.isqrt(n) + 1):
        if n % first == 0:
            for tail in multiplicative_partitions(n // first, first):
                yield (first,) + tail


def patterns(count):
    return sorted({tuple(sorted((f - 1 for f in factors), reverse=True))
                   for factors in multiplicative_partitions(count)})


def check():
    answer = {'route_convention': 'sorted multiset states; no swapping identical cards',
              'routes': {}, 'subbags': {}, 'patterns': {}, 'minimum_by_pattern': {},
              'least_numbers': {}}
    for n in (12, 18, 20, 24, 36, 48, 60):
        all_routes = routes((n,))
        assert len(all_routes) >= 2
        terminal = {route[-1] for route in all_routes}
        assert terminal == {prime_factors(n)}
        answer['routes'][n] = {'prime_bag': prime_factors(n), 'count': len(all_routes),
                                'all_state_routes': all_routes}
    for tokens in ((2,2,3), (2,3,3), (2,2,5), (2,2,2,3), (2,3,5),
                   (2,2,3,3), (2,2,3,5), (2,2,2,3,3), (2,)*7+(3,)*4, ()):
        answer['subbags'][math.prod(tokens)] = subbags(tokens)
    assert math.prod((2,2,5)) == 20
    assert math.prod((2,5)) == 10 and 20 // 10 == 2
    expected_counts = {12:6, 18:6, 20:6, 24:8, 30:8, 36:9, 60:12, 72:12, 10368:40, 1:1}
    for n, count in expected_counts.items():
        assert len(answer['subbags'][n]) == count
    primes = (2,3,5,7,11,13)
    for count in (4,6,8,9,10,12):
        pp = patterns(count)
        # Complete independent bounded search: each exponent + 1 divides count,
        # so each exponent is at most count - 1. Three slots suffice for these targets.
        brute = {tuple(sorted((e for e in exps if e), reverse=True))
                 for exps in itertools.product(range(count), repeat=3)
                 if math.prod(e+1 for e in exps) == count}
        assert set(pp) == brute
        candidates = [(pattern, math.prod(p**e for p,e in zip(primes,pattern)))
                      for pattern in pp]
        minimum = min(value for pattern,value in candidates)
        assert len(divisors(minimum)) == count
        assert all(len(divisors(n)) != count for n in range(1, minimum))
        answer['patterns'][count] = pp
        answer['minimum_by_pattern'][count] = candidates
        answer['least_numbers'][count] = minimum
    assert answer['least_numbers'] == {4:6, 6:12, 8:24, 9:36, 10:48, 12:60}
    return answer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path, help='Write complete machine-readable enumeration')
    args = parser.parse_args()
    result = check()
    for n, row in result['routes'].items():
        print('Routes', n, row['count'], 'terminal', row['prime_bag'])
    for n, rows in result['subbags'].items():
        print('Divisors', n, len(rows), [row['value'] for row in rows])
    for d, pp in result['patterns'].items():
        print('Patterns', d, pp, 'least', result['least_numbers'][d])
    if args.json:
        args.json.write_text(json.dumps(result, indent=2) + '\n')
    print('PASS: exhaustive routes, physical-token subsets, divisor lists, patterns and minima.')


if __name__ == '__main__':
    main()
