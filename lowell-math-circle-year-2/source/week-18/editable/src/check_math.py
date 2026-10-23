#!/usr/bin/env python3
"""Independent finite checks of Week 18's mathematical claims and construction tasks.

Carried over unchanged from the old student builder (archived beside the problem files in
archive-before-problem-files-2026-10-23/build_packets.py); writes mathematical-checks.json.
"""
from pathlib import Path
import itertools, json
SRC=Path(__file__).resolve().parent

# Independent finite checks for the mathematical claims and construction tasks.
def d(a,b):return sum(x!=y for x,y in zip(a,b))
def strings(n):return [''.join(x) for x in itertools.product('01',repeat=n)]
def ball(s,r=1):return {t for t in strings(len(s)) if d(s,t)<=r}
def reliable(code,r=1):return all(d(a,b)>=2*r+1 for a,b in itertools.combinations(code,2))
checks={}
checks['k_decode']={s:[m for m,c in [('triangle','000'),('square','111')] if s in ball(c)] for s in strings(3)}
checks['two_counter_ambiguity']={s:[c for c in ['00','11'] if s in ball(c)] for s in strings(2)}
checks['ordered_three_counter_keys']=[(a,b) for a in strings(3) for b in strings(3) if reliable([a,b])]
checks['mixed_four_counter_completions']={a:[b for b in strings(4) if '0' in b and '1' in b and reliable([a,b])] for a in ['0011','0100']}
assert [len(v) for v in checks['mixed_four_counter_completions'].values()]==[5,4]
assert len(checks['ordered_three_counter_keys'])==8
checks['weight_two_ordered_keys']=[(a,b) for a in strings(4) for b in strings(4) if a.count('1')==b.count('1')==2 and reliable([a,b])]
assert len(checks['weight_two_ordered_keys'])==6
checks['four_picture_five_entry_example']=['01001','01110','10000','10111']
assert reliable(checks['four_picture_five_entry_example'])
checks['three_picture_four_entry_keys']=sum(reliable(c) for c in itertools.combinations(strings(4),3))
assert checks['three_picture_four_entry_keys']==0
checks['four_picture_four_entry_keys']=sum(reliable(c) for c in itertools.combinations(strings(4),4))
assert checks['four_picture_four_entry_keys']==0
checks['five_entry_received_count']=len(set.union(*(ball(c) for c in checks['four_picture_five_entry_example'])))
assert checks['five_entry_received_count']==24
checks['two_change_minimum']=next(n for n in range(1,6) if any(reliable([a,b],2) for a,b in itertools.combinations(strings(n),2)))
assert checks['two_change_minimum']==5
checks['neighborhood_counts']={n:len(ball('0'*n)) for n in [2,3,4,5,10]}
(SRC/'mathematical-checks.json').write_text(json.dumps(checks,indent=2))
print('Finite mathematical checks passed; wrote mathematical-checks.json.')
