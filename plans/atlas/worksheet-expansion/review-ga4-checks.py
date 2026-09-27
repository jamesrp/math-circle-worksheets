#!/usr/bin/env python3
"""Independent structural checks; the all-family proof review is in the report."""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch
import hashlib
import json
import runpy

HERE = Path(__file__).resolve().parent


def add(*polys):
    result = defaultdict(F)
    for poly in polys:
        for monomial, coefficient in poly.items():
            result[monomial] += coefficient
    return {m: c for m, c in result.items() if c}


def mul(p, q):
    result = defaultdict(F)
    for pm, pc in p.items():
        for qm, qc in q.items():
            result[tuple(x + y for x, y in zip(pm, qm))] += pc * qc
    return {m: c for m, c in result.items() if c}


def scale(p, c):
    return {m: coefficient * c for m, coefficient in p.items() if coefficient * c}


def cycles(domain, successor):
    unseen = set(domain)
    answer = []
    while unseen:
        start = next(iter(unseen))
        cycle = []
        point = start
        while point in unseen:
            unseen.remove(point)
            cycle.append(point)
            point = successor(point)
        assert point == start
        answer.append(cycle)
    return answer


one = {(0, 0, 0, 0): F(1)}
a, b, u, v = [
    {tuple(int(j == i) for j in range(4)): F(1)} for i in range(4)
]
points = [
    (add(a, u), add(b, v)),
    (add(a, scale(v, -1)), add(b, u)),
    (add(a, scale(u, -1)), add(b, scale(v, -1))),
    (add(a, v), add(b, scale(u, -1))),
]
bases = [lambda x, y: mul(x, x), lambda x, y: mul(x, y),
         lambda x, y: mul(y, y), lambda x, y: x, lambda x, y: y,
         lambda x, y: one]
radius_squared = add(mul(u, u), mul(v, v))
for i, basis in enumerate(bases):
    mean = scale(add(*(basis(x, y) for x, y in points)), F(1, 4))
    difference = add(mean, scale(basis(a, b), -1))
    expected = scale(radius_squared, F(1, 2)) if i in (0, 2) else {}
    assert difference == expected

# Constant Laurent coefficient gives the circle average, with z=e^(it).
# cos^2=(z^2+2+z^-2)/4; sin^2=(-z^2+2-z^-2)/4.
cos2 = {2: F(1, 4), 0: F(1, 2), -2: F(1, 4)}
sin2 = {2: -F(1, 4), 0: F(1, 2), -2: -F(1, 4)}
circle_average = sum(c * sin2.get(-power, 0) for power, c in cos2.items())
assert circle_average == F(1, 8)

# Independently trace actual long-edge identifications, not 2*annuli+Mobius.
topology = []
for lane_count in range(1, 65):
    components = cycles(range(lane_count), lambda i: lane_count - 1 - i)
    boundaries = cycles(
        [(i, e) for i in range(lane_count) for e in (0, 1)],
        lambda point: (lane_count - 1 - point[0], 1 - point[1]),
    )
    assert len(components) == (lane_count + 1) // 2
    assert len(boundaries) == lane_count
    for component in components:
        boundary_count = sum(any(i in component for i, e in boundary)
                             for boundary in boundaries)
        assert boundary_count == (2 if len(component) == 2 else 1)
    topology.append([lane_count, len(components), len(boundaries)])

data = json.loads((HERE / 'ga4-data.json').read_text())
assert [family['id'] for family in data['families']] == [
    'GA-28', 'GA-30', 'GA-31', 'GA-32', 'GA-33', 'GA-34', 'GA-35', 'GA-36'
]
assert sum(len(f['pages']) for f in data['families']) == 24
assert sum(len(p['prompts']) for f in data['families'] for p in f['pages']) == 48
assert sum(len(f['extensions']) for f in data['families']) == 8
assert 'may delay choosing r' in data['families'][0]['pages'][0]['intro']
assert 'without overlapping' in data['families'][1]['pages'][0]['intro']
assert 'called an annulus' in data['families'][3]['pages'][1]['prompts'][1]['text']

# Run the author's finite audits without changing author-owned results.
with patch.object(Path, 'write_text', return_value=0):
    author = runpy.run_path(str(HERE / 'ga4-checks.py'), run_name='__main__')
assert set(author['out']) == {f['id'] for f in data['families']}
out = {
    'data_sha256': hashlib.sha256((HERE / 'ga4-data.json').read_bytes()).hexdigest(),
    'scope': 'Symbolic quadratic identity and independent boundary cycles; general all-family arguments reviewed separately.',
    'GA-35': {'formal_polynomial_bases_proved': 6,
              'variables': ['a', 'b', 'u', 'v'],
              'quadratic_mean_shift': '(A+C)(u^2+v^2)/2',
              'quartic_circle_mean_on_unit_circle': str(circle_average)},
    'GA-32': {'rows_are': ['lanes', 'connected_components', 'boundary_circuits'],
              'independent_edge_cycle_counts': topology},
    'coverage': {'families': 8, 'student_pages': 24, 'prompts': 48, 'extensions': 8},
    'author_finite_audits_passed': sorted(author['out']),
    'status': 'passed',
}
(HERE / 'review-ga4-checks-results.json').write_text(json.dumps(out, indent=2) + '\n')
print('Independent GA4 checks passed: symbolic identity, edge cycles, coverage; author audits passed read-only.')
