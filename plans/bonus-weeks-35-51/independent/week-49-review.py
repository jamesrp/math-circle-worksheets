"""Independent cyclic-difference catalog and dynamics; no author imports."""
from itertools import product
from collections import Counter
from pathlib import Path
import json
def gap(v):return tuple(abs(v[(i+1)%len(v)]-v[i]) for i in range(len(v)))
def signed(v):return tuple(v[(i+1)%len(v)]-v[i] for i in range(len(v)))
def trajectory(v,n,op=gap):
    out=[tuple(v)]
    for _ in range(n):out.append(op(out[-1]))
    return out
targets=[(1,1,1,1),(1,2,1,2)]
catalog={str(g):[v for v in product(range(4),repeat=4) if min(v)==0 and gap(v)==g] for g in targets}
assert len(catalog[str(targets[0])])==6 and len(catalog[str(targets[1])])==4
signed_catalog={}
for g in targets:
    outputs=[]
    for signs in product([-1,1],repeat=4):
        changes=[a*b for a,b in zip(g,signs)]
        if sum(changes):continue
        v=[0]
        for change in changes[:-1]:v.append(v[-1]+change)
        m=min(v);v=tuple(x-m for x in v)
        if max(v)<=3:outputs.append(v)
    assert sorted(set(outputs))==catalog[str(g)];signed_catalog[str(g)]=outputs
assert gap((1,3,2,0))==(2,1,2,1)
assert signed((1,3,3,1))==(2,0,-2,0)
for v in product(range(4),repeat=4):
    assert gap(tuple(x+7 for x in v))==gap(v)==gap(tuple(3-x for x in v))
six=trajectory((1,0,0,1,0,0),7)
assert six[1:4]==[(1,0,1,1,0,1),(1,1,0,1,1,0),(0,1,1,0,1,1)] and six[4]==six[1]
eight_single=trajectory((1,0,0,0,0,0,0,0),8)
assert eight_single[7]==(1,)*8 and eight_single[8]==(0,)*8
zero_times=Counter()
for v in product(range(2),repeat=8):
    run=trajectory(v,8);assert run[-1]==(0,)*8
    zero_times[next(i for i,x in enumerate(run) if not any(x))]+=1
    for k in [1,2,4,8]:assert run[k]==tuple(v[i]^v[(i+k)%8] for i in range(8))
directed={str(v):trajectory(v,10,signed) for v in [(0,1,0,1),(0,0,1,1)]}
first_over={key:next(i for i,state in enumerate(run) if max(map(abs,state))>10) for key,run in directed.items()}
assert first_over=={'(0, 1, 0, 1)':5,'(0, 0, 1, 1)':9}
assert all(sum(state)==0 for run in directed.values() for state in run[1:])
result={'predecessor_catalog':catalog,'signed_choices':signed_catalog,'six_run':six,'eight_single_run':eight_single,'all_256_eight_zero_times':dict(sorted(zero_times.items())),'directed_runs':directed,'first_round_exceeding_10':first_over,'worked_examples':{'gap':[list((1,3,2,0)),list((2,1,2,1))],'signed':[list((1,3,3,1)),list((2,0,-2,0))]}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
