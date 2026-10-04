#!/usr/bin/env python3
from itertools import permutations,product
import json

def run(values,bars):
    values=list(values)
    for a,b in bars:
        if values[a][0]>values[b][0]:values[a],values[b]=values[b],values[a]
    return tuple(values)
def plain(p):return tuple((x,str(x)) for x in p)
selector=((0,1),(0,2),(0,3))
half=((0,1),(2,3),(0,3),(1,2))
merger=((0,2),(1,3),(1,2))
X=((0,2),(0,1),(1,2));Y=((0,1),(1,2),(0,1))
all_inputs=list(permutations(range(1,5)))
assert all(run(plain(p),selector)[0][0]==1 for p in all_inputs)
assert all(max(x[0] for x in run(plain(p),half)[:2])<=min(x[0] for x in run(plain(p),half)[2:]) for p in all_inputs)
for p in product(range(3),repeat=4):
    out=run(plain(p),half)
    assert max(x[0] for x in out[:2])<=min(x[0] for x in out[2:])
merge_inputs=[p for p in all_inputs if p[0]<p[1] and p[2]<p[3]]
assert len(merge_inputs)==6
assert all(tuple(v[0] for v in run(plain(p),merger))==(1,2,3,4) for p in merge_inputs)
for p in product(range(3),repeat=4):
    if p[0]<=p[1] and p[2]<=p[3]:assert tuple(v[0] for v in run(plain(p),merger))==tuple(sorted(p))
merge_failure=next(p for p in all_inputs if tuple(v[0] for v in run(plain(p),merger))!=(1,2,3,4))
tagged=((2,'A'),(2,'B'),(1,'C'))
rows=[]
for p in permutations(tagged):
    x,y=run(p,X),run(p,Y)
    order=[tag for val,tag in p if val==2]
    assert [tag for val,tag in y if val==2]==order
    rows.append({'input':p,'X':x,'Y':y,'X_preserves':[tag for val,tag in x if val==2]==order})
assert any(not r['X_preserves'] for r in rows)
print(json.dumps({'selector_permutations_checked':24,'lower_half_repeated_inputs_checked':81,'half_trace_3412':run(plain((3,4,1,2)),half),'legal_merge_inputs':merge_inputs,'merge_failure':merge_failure,'tagged_outputs':rows},indent=2))
