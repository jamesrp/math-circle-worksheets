#!/usr/bin/env python3
"""Finite checks of writer-selected rings, independent of rendering."""
from itertools import product
from pathlib import Path
import json
def rotations(s): return [s[i:]+s[:i] for i in range(len(s))]
def canon(s): return min(rotations(s))
def flipcanon(s): return min(canon(s),canon(s[::-1]))
patterns={'a':'AABABBBB','b':'ABBBBABA','c':'BAABABBB','d':'AABBABBB','e':'ABBBABBA','f':'BBAABBAB'}
turn_groups={}
flip_groups={}
for label,s in patterns.items():
    turn_groups.setdefault(canon(s),[]).append(label)
    flip_groups.setdefault(flipcanon(s),[]).append(label)
assert sorted(map(sorted,turn_groups.values()))==[['a','c'],['b'],['d','f'],['e']]
assert sorted(map(sorted,flip_groups.values()))==[['a','b','c'],['d','e','f']]
proper=[''.join(t) for t in product('ABC',repeat=5) if all(t[i]!=t[(i+1)%5] for i in range(5))]
proper_classes=sorted({canon(s) for s in proper})
assert proper_classes==['ABABC','ABACB','ABCAC','ABCBC','ACACB','ACBCB']
def windows(s,k): return [''.join(s[(i+j)%len(s)] for j in range(k)) for i in range(len(s))]
codes3={''.join(t) for t in product('AB',repeat=3)}
solutions=sorted({canon(''.join(t)) for t in product('AB',repeat=8) if set(windows(''.join(t),3))==codes3})
assert solutions==['AAABABBB','AAABBBAB']
assert canon(solutions[0][::-1])==solutions[1]
assert set(windows('AABB',2))=={'AA','AB','BA','BB'}
report={'turn_groups':list(turn_groups.values()),'turn_flip_groups':list(flip_groups.values()),'proper_fixed_words':len(proper),'proper_rotation_classes':proper_classes,'shortest_three_window_classes':solutions,'example_wrap_window':windows('ABAAB',3)[4],'working_spot_diameter_mm':24,'eight_ring_adjacent_center_mm':2*33*__import__('math').sin(__import__('math').pi/8)}
assert report['example_wrap_window']=='BAB'
(Path(__file__).resolve().parent.parent/'writer-check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
