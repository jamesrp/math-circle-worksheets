from itertools import product
from collections import Counter,deque
from pathlib import Path
import json
def legal(a,edges):return all(abs(a[i]-a[j])<=1 for i,j in edges)
def catalog(n,edges,clues,maxh):return [a for a in product(range(maxh+1),repeat=n) if all(a[i]==h for i,h in clues.items()) and legal(a,edges)]
e5=[(i,i+1) for i in range(4)];r5=e5+[(4,0)]
open5=catalog(5,e5,{0:0,3:3},4);bad5=catalog(5,r5,{0:0,3:3},4);fixed5=catalog(5,r5,{0:0,3:2},4)
e7=[(i,i+1) for i in range(6)];rows=catalog(7,e7,{0:1,6:1},4);rowset=set(rows)
def adjacent(a):
    for i in range(1,6):
        for delta in [-1,1]:
            b=list(a);b[i]+=delta;b=tuple(b)
            if b in rowset:yield b
all_pair_l1=True
for start in rows:
    d={start:0};q=deque([start])
    while q:
        a=q.popleft()
        for b in adjacent(a):
            if b not in d:d[b]=d[a]+1;q.append(b)
    all_pair_l1 &= len(d)==len(rows) and all(d[b]==sum(abs(x-y) for x,y in zip(start,b)) for b in rows)
start=(1,2,3,2,1,0,1);end=(1,0,1,2,3,2,1)
printed=[start,(1,2,2,2,1,0,1),(1,1,2,2,1,0,1),(1,1,1,2,1,0,1),(1,0,1,2,1,0,1),(1,0,1,2,1,1,1),(1,0,1,2,2,1,1),(1,0,1,2,2,2,1),end]
assert all(a in rowset for a in printed) and all(sum(abs(x-y) for x,y in zip(a,b))==1 for a,b in zip(printed,printed[1:]))
r6=[(i,(i+1)%6) for i in range(6)];rings=catalog(6,r6,{0:1,3:1},2)
budget_hist=Counter(map(sum,rings))
assert len(rows)==120 and len(rings)==49 and all_pair_l1
assert (1,0,0,1,1,2) in rings and (1,1,1,1,2,2) in rings
result={'open_row_completions':open5,'inconsistent_ring_completions':bad5,'repaired_ring_completions':fixed5,'transition_state_count':len(rows),'all_14400_ordered_row_pairs_shortest_distance_equals_l1':all_pair_l1,'printed_route_legal':True,'printed_route_length':len(printed)-1,'budget_ring_count':len(rings),'budget_histogram':dict(sorted(budget_hist.items()))}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
