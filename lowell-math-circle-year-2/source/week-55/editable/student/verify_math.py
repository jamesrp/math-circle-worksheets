#!/usr/bin/env python3
"""Finite checks for every Week 55 student task and array."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import argparse
import json

def totals(a, b):
    return sorted(set(x+y for x in a for y in b))

def spacing(a):
    differences = [a[i+1]-a[i] for i in range(len(a)-1)]
    return differences[0] if differences and len(set(differences)) == 1 else None

def record(a, b):
    result = totals(a, b)
    return {'A': list(a), 'B': list(b), 'totals': result,
            'count': len(result), 'lower': len(a)+len(b)-1,
            'upper': len(a)*len(b)}

fixed = {
    1: [((0,2),(1,3)), ((0,2),(1,4))],
    2: [((0,1,2),(0,1,2)), ((0,1,3),(0,1,3)), ((0,1,2),(0,3,6))],
    6: [((1,3,5),(2,4)), ((0,2,4),(0,3)), ((0,2,4),(1,3)), ((0,3,6),(1,4))],
    7: [((4,),(0,1,3)), ((2,),(0,2,4)), ((0,),(1,4,6,9))],
}
expected_counts = {1:[3,4], 2:[5,6,9], 6:[4,6,4,4], 7:[3,3,4]}
count_example = {'A':[1,4], 'B':[0,2,5,8]}
count_example.update(m=len(count_example['A']), n=len(count_example['B']))
assert (count_example['m'], count_example['n']) == (2,4)
assert count_example['m']+count_example['n']-1 == 5
assert count_example['m']*count_example['n'] == 8
fixed_results = {str(k): [record(a,b) for a,b in pairs] for k,pairs in fixed.items()}
for k, rows in fixed_results.items():
    assert [r['count'] for r in rows] == expected_counts[int(k)]

# Design space is exactly the printed reusable 0--9 kit. Exhaust every legal trial.
design = {}
for m,n in [(3,3),(2,3),(2,4),(3,4)]:
    counts = Counter()
    witnesses = {}
    for a in combinations(range(10), m):
        for b in combinations(range(10), n):
            count = len(totals(a,b))
            counts[count] += 1
            witnesses.setdefault(count, record(a,b))
    assert min(counts) == m+n-1
    assert max(counts) <= m*n
    if (m,n) == (3,3):
        assert max(counts) == 9
    design[f'{m}+{n}'] = {'trials':sum(counts.values()),
                         'count_histogram':dict(sorted(counts.items())),
                         'minimum_witness':witnesses[min(counts)],
                         'maximum_witness':witnesses[max(counts)]}

catalog = [record((0,3,6),b) for b in combinations(range(10),2)
           if len(totals((0,3,6),b)) == 4]
assert [r['B'] for r in catalog] == [[i,i+3] for i in range(7)]

def routes(rows, columns, i=0, j=0):
    if (i,j) == (rows-1,columns-1):
        yield [(i,j)]
    else:
        if i+1 < rows:
            for tail in routes(rows,columns,i+1,j):
                yield [(i,j)] + tail
        if j+1 < columns:
            for tail in routes(rows,columns,i,j+1):
                yield [(i,j)] + tail

arrays = []
for a,b in [((1,5),(0,2,6)), ((0,2,5),(1,3,4)), ((1,3,5),(0,2,4,6))]:
    values = [[x+y for y in b] for x in a]
    paths = []
    for path in routes(len(a),len(b)):
        result = [values[i][j] for i,j in path]
        assert len(result) == len(a)+len(b)-1
        assert all(x<y for x,y in zip(result,result[1:]))
        paths.append(result)
    arrays.append({'A_bottom_to_top':a, 'B_left_to_right':b,
                   'rows_bottom_to_top':values, 'route_totals':paths})
assert arrays[0]['rows_bottom_to_top'] == [[1,3,7],[5,7,11]]
assert [1,3,7,11] in arrays[0]['route_totals']

# All integer subsets of this finite universe, generated independently as masks.
sets = [tuple(i for i in range(9) if mask & (1 << i)) for mask in range(1,512)]
equality = singleton = 0
for a in sets:
    for b in sets:
        result = totals(a,b)
        lower = len(a)+len(b)-1
        assert lower <= len(result) <= len(a)*len(b)
        if min(len(a),len(b)) == 1:
            assert len(result) == lower
            singleton += 1
        else:
            common = spacing(a) is not None and spacing(a) == spacing(b)
            assert (len(result) == lower) == common
            equality += len(result) == lower
            if common:
                # Every local alternative has equal intermediate sums.
                for i in range(len(a)-1):
                    for j in range(len(b)-1):
                        assert a[i+1]+b[j] == a[i]+b[j+1]

result = {'status':'pass', 'count_conversion_example':count_example,
          'fixed_tasks':fixed_results, 'design_tasks':design,
          'problem_5_complete_catalog':catalog, 'arrays_all_routes':arrays,
          'general_finite_check':{'universe':list(range(9)),
              'ordered_set_pairs':len(sets)**2,
              'nonsingleton_equality_pairs':equality,
              'singleton_pairs':singleton},
          'scope':'Finite checks verify printed examples and choices. General proof is in MATH-NOTES.md. Physical handling and classroom piloting are unperformed.'}
parser = argparse.ArgumentParser()
parser.add_argument('--out', type=Path, required=True)
args = parser.parse_args()
args.out.parent.mkdir(parents=True,exist_ok=True)
args.out.write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS: {len(sets)**2} finite pairs; all card-design trials; 45 catalog candidates; every printed route')
