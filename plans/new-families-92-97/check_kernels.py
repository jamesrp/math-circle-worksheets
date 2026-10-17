#!/usr/bin/env python3
"""Independent exact checks of the six design kernels, not page coverage.

Run with Python 3. The finite checks support the examples; general arguments
remain in the facilitator guides. No classroom or physical readiness claim.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json


def tent(x):
    return 2 * min(x, 16 - x)


def interval_image(a, b):
    values = [tent(a), tent(b)]
    if a <= 8 <= b:
        values.append(F(16))
    return min(values), max(values)


def divisor_count(n):
    return sum(n % d == 0 for d in range(1, n + 1))


def main():
    results = {}
    route = [(F(7), F(9))]
    for _ in range(4):
        route.append(interval_image(*route[-1]))
    assert route == [(7, 9), (14, 16), (0, 4), (0, 8), (0, 16)]
    branches = 0
    for n in range(1, 10):
        width = F(16, 2 ** n)
        for k in range(2 ** n):
            span = (k * width, (k + 1) * width)
            for _ in range(n):
                span = interval_image(*span)
            assert span == (0, 16)
            branches += 1
    assert tent(F(799, 100)) == tent(F(801, 100))
    for aa, bb in combinations(range(65), 2):
        a, b = F(aa, 4), F(bb, 4)
        low, high = interval_image(a, b)
        assert high-low >= b-a
    results['92'] = {'dyadic_branch_intervals': branches,
                     'worked_route': [[str(x) for x in pair] for pair in route],
                     'nearby_merging_pair': ['7.99', '8.01'],
                     'interval_width_note': 'Whole interval widths never shrink, although particular pairs may merge.'}

    rectangle_count = 0
    for denominator in range(1, 8):
        for aa in range(1, 30):
            for bb in range(aa, 30):
                a, b = F(aa, denominator), F(bb, denominator)
                area = a*b
                m = (a+b)/2
                h = area/m
                assert a <= h <= m <= b and h*m == area
                assert h*h <= area <= m*m
                assert m-h == (b-a)**2/(2*(a+b))
                assert (m-h < (b-a)/2) if a < b else m == h
                rectangle_count += 1
    results['93'] = {'positive_rational_rectangles': rectangle_count}

    calibration_count = 0
    for x1, x2 in combinations(range(-4, 9), 2):
        for error in [F(0), F(1, 2), F(1), F(3, 2)]:
            y1, y2 = F(3)+F(5, 4)*x1, F(3)+F(5, 4)*x2
            lo = (y2-y1-2*error)/(x2-x1)
            hi = (y2-y1+2*error)/(x2-x1)
            assert hi-lo == 4*error/(x2-x1)
            for slope in (lo, hi):
                intercept_lo = max(y1-error-slope*x1, y2-error-slope*x2)
                intercept_hi = min(y1+error-slope*x1, y2+error-slope*x2)
                assert intercept_lo <= intercept_hi
            calibration_count += 1
    results['94'] = {'affine_bounded_error_cases': calibration_count,
                     'qualification': 'Unrestricted real offset and slope; extra constraints may narrow the interval.'}

    recapture_count = 0
    for N in range(1, 19):
        for M in range(1, N+1):
            for n in range(1, N+1):
                outcomes = []
                for r in range(max(0, M+n-N), min(M,n)+1):
                    weight = comb(M,r)*comb(N-M,n-r)
                    outcomes.append((r, weight))
                    assert N >= M+n-r
                assert sum(w for _,w in outcomes) == comb(N,n)
                expectation = sum(F(r*w, comb(N,n)) for r,w in outcomes)
                assert expectation == F(M*n,N)
                recapture_count += 1
    for budget in range(2, 30):
        values = {M: M*(budget-M) for M in range(1,budget)}
        assert max(values.values()) == (budget//2)*(budget-budget//2)
    results['95'] = {'exact_hypergeometric_cases': recapture_count,
                     'warning': 'Expected overlap identity does not imply an unbiased inverse estimate.'}

    minima = {count: next(n for n in range(1,1000) if divisor_count(n)==count)
              for count in (6,8,12)}
    assert minima == {6:12,8:24,12:60}
    results['96'] = {'least_number_by_divisor_count': minima}

    primes = [p for p in range(3,100) if all(p%d for d in range(2,p))]
    for p in primes:
        outputs = {}
        for x in range(p):
            outputs.setdefault(x*x%p, []).append(x)
        assert outputs[0] == [0]
        assert len(outputs)-1 == (p-1)//2
        assert all(len(v)==2 and sum(v)==p for k,v in outputs.items() if k)
    composites = {}
    for m, residue, expected in [(8,1,[1,3,5,7]),(9,0,[0,3,6]),(15,1,[1,4,11,14])]:
        roots = [x for x in range(m) if x*x%m == residue]
        assert roots == expected
        composites[str(m)] = {'residue':residue,'roots':roots}
    results['97'] = {'odd_primes_tested':len(primes),'composite_contrasts':composites}
    print(json.dumps({'scope':'Design kernels only; see per-week records for final problem coverage.',
                      'status':'pass','results':results}, indent=2))


if __name__ == '__main__':
    main()
