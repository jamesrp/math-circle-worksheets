#!/usr/bin/env python3
"""Independent three-step four-label audit after the Week16 novelty correction."""
from collections import Counter
from itertools import product
from pathlib import Path
import json

vertices = [(i, j) for j in range(4) for i in range(4-j)]
cells = []
for i, j in vertices:
    if i+j < 3:
        cells.append(((i,j), (i+1,j), (i,j+1)))
    if i+j < 2:
        cells.append(((i+1,j), (i+1,j+1), (i,j+1)))
choices = []
for p in vertices:
    i, j = p
    if p == (0,0): allowed = 'R'
    elif p == (3,0): allowed = 'B'
    elif p == (0,3): allowed = 'Y'
    elif j == 0: allowed = 'RB'
    elif i == 0: allowed = 'RY'
    elif i+j == 3: allowed = 'BY'
    else: allowed = 'RBYG'
    choices.append(allowed)

def triple_counts(labels):
    return Counter(''.join(sorted({labels[p] for p in cell}))
                   for cell in cells if len({labels[p] for p in cell}) == 3)

histogram = Counter()
for labels in product(*choices):
    counts = triple_counts(dict(zip(vertices, labels)))
    # Each endpoint-restricted outer side has an odd number of its label-pair doors.
    for types in [('BRY','BGR'), ('BRY','GRY'), ('BRY','BGY')]:
        assert sum(counts[t] for t in types) % 2 == 1
    if not counts['BRY']:
        assert counts['BGR'] % 2 == counts['GRY'] % 2 == counts['BGY'] % 2 == 1
        assert sum(counts.values()) >= 3
    histogram[(counts['BRY'], sum(counts.values()))] += 1

witness = {(0,0):'R', (1,0):'R', (2,0):'B', (3,0):'B',
           (0,1):'R', (1,1):'G', (2,1):'B',
           (0,2):'Y', (1,2):'Y', (0,3):'Y'}
assert triple_counts(witness) == {'BGR':1, 'GRY':1, 'BGY':1}
result = {
    'assumptions': 'Usual endpoint-restricted R/B/Y outer sides; interior may also use G; count distinct three-label cells by unordered label triple.',
    'legal_fillings': sum(histogram.values()),
    'histogram_RBY_then_all_three_distinct': {f'{a},{b}': n for (a,b),n in sorted(histogram.items())},
    'zero_RBY_histogram_all_three_distinct': {str(b):n for (a,b),n in sorted(histogram.items()) if a == 0},
    'minimum_zero_RBY': 3,
    'witness_rows_bottom_to_top': ['RRBB', 'RGB', 'YY', 'Y'],
    'witness_cells': [{'vertices': cell, 'labels': ''.join(witness[p] for p in cell)} for cell in cells],
    'general_proof': 'Count incidences of RB doors: RBY+RBG has the parity of the odd RB boundary count. Similarly RBY+RYG and RBY+BYG are odd. If RBY=0, all three G-containing types are odd and each occurs. Thus at least three distinct-three-label cells remain. The witness attains three.',
    'limit': 'Finite audit supplements the incidence proof; no classroom or physical rehearsal is claimed.',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(f"{result['legal_fillings']} legal fillings; zero-RBY counts {result['zero_RBY_histogram_all_three_distinct']}; minimum3 witness checked")
