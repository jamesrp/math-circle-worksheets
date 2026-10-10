#!/usr/bin/env python3
"""Independent exact arithmetic for the midnight example; standard library only.

Adapted from the separate mathematical review's exact-prefix checker.
Finite replay corroborates examples; general proofs are in the adult guide.
Page geometry and every-page visual review are separate release checks.
"""
from fractions import Fraction
from pathlib import Path
import json
import os

time = position = Fraction(0)
state = 0
records = []
for n in range(1,129):
    previous = time
    time = (time + 1) / 2
    position = (position + 1) / 2
    state = 1 - state
    assert previous < time < 1
    assert time == position == 1 - Fraction(1,2**n)
    assert 1-position == Fraction(1,2**n)
    assert state == n % 2
    if n <= 4:
        records.append({'n':n,'time':str(time),'post_switch':'ON' if state else 'OFF',
                        'remaining_mm':str(Fraction(180,2**n))})
prefix = {1-Fraction(1,2**n): n % 2 for n in range(1,129)}
on, off = {**prefix,Fraction(1):1}, {**prefix,Fraction(1):0}
assert all(on[t] == off[t] for t in prefix)
assert on[1] != off[1]
assert Fraction(180,2**4) == Fraction(45,4)
result = {'status':'PASS','first_four_actions':records,'exact_prefix_checked':128,
          'limits':'General subsequence and convergence proofs are in the guide; physical and classroom rehearsal untested.'}
Path(os.environ.get('INFINITY_CHECK_OUT','math-check-results.json')).write_text(json.dumps(result,indent=2)+'\n')
print('PASS: exact halvings, alternating states and two endpoint extensions.')
