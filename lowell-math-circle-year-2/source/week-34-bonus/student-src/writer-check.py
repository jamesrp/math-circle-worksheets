#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import math,json
def matches(s,p): return all(s[i]==s[p[i]] for i in range(len(s)))
def motions(s):
    n=len(s)
    return {'turns':[r for r in range(n) if matches(s,[(i+r)%n for i in range(n)])], 'flips':[k for k in range(n) if matches(s,[(k-i)%n for i in range(n)])]}
witnesses={s:motions(s) for s in ['AABBBB','ABBABB','ABABAB']}
assert [witnesses[s]['flips'] for s in witnesses]==[[1],[0,3],[0,2,4]]
counts=sorted({len(motions(''.join(t))['flips']) for t in product('AB',repeat=6)})
assert counts==[0,1,2,3,6]
start='AAABBABB';n=8
perms={'half_turn':[(i+4)%n for i in range(n)],'vertical_flip':[(-i)%n for i in range(n)],'one_spot':[(i+1)%n for i in range(n)],'two_spots':[(i+2)%n for i in range(n)]}
repairs={}
for name,p in perms.items():
    candidates=[(''.join(t),sum(a!=b for a,b in zip(start,t))) for t in product('AB',repeat=n) if matches(t,p)]
    cost=min(k for s,k in candidates)
    repairs[name]={'cost':cost,'minima':[s for s,k in candidates if k==cost]}
assert [repairs[k]['cost'] for k in perms]==[2,3,4,4]
assert sorted(repairs['half_turn']['minima'])==sorted(['AAABAAAB','BABBBABB','AABBAABB','BAABBAAB'])
first='100000';second='010000'
stack=tuple(zip(first,second))
intersection={'turns':sorted(set(motions(first)['turns'])&set(motions(second)['turns'])),'flips':sorted(set(motions(first)['flips'])&set(motions(second)['flips']))}
assert motions(stack)==intersection=={'turns':[0],'flips':[]}
opposite='000100'
assert motions(tuple(zip(first,opposite)))=={'turns':[0],'flips':[0]}
half_first='100100';half_second='010010'
assert 3 in motions(tuple(zip(half_first,half_second)))['turns']
report={'witnesses':witnesses,'six_ring_possible_flip_counts':counts,'minimum_repairs':repairs,'adjacent_layer_stack':intersection,'eight_ring_adjacent_center_mm':2*37*math.sin(math.pi/8),'working_spot_diameter_mm':28}
(Path(__file__).resolve().parent.parent/'writer-check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
