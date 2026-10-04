from itertools import product,combinations
from functools import lru_cache
from collections import Counter
from pathlib import Path
import json
points=list(product(range(3),repeat=2))
triples=[q for q in combinations(range(9),3) if all(len({points[i][a] for i in q}) in [1,3] for a in range(2))]
tm=[sum(1<<i for i in q) for q in triples]
def bad(mask):return any(mask&t==t for t in tm)
caps=[m for m in range(512) if not bad(m)]
@lru_cache(None)
def winning(own,other):
    for i in range(9):
        bit=1<<i
        if (own|other)&bit or bad(own|bit):continue
        if not winning(other,own|bit):return True
    return False
assert winning(0,0) and len(triples)==12
leaves=Counter()
for center in range(9):
    cx,cy=points[center]
    def oppose(i):
        x,y=points[i];return points.index(((2*cx-x)%3,(2*cy-y)%3))
    def strategy(first,second,claim):
        for i in range(9):
            bit=1<<i
            if (first|second)&bit:continue
            s=second|bit
            if bad(s):leaves[claim]+=1;continue
            response=1<<oppose(i)
            assert not (first|s)&response
            f=first|response
            assert not bad(f)
            strategy(f,s,claim+1)
    strategy(1<<center,0,1)
colorcounts={}
for k in [2,3]:
    colorcounts[k]=sum(all(len({colors[i] for i in q})>1 for q in triples) for colors in product(range(k),repeat=9))
colors=[0,0,1,0,0,1,1,1,2]
nums=[1,2,2,2,3,3,2,3,3]
assert all(len({colors[i] for i in q})>1 for q in triples)
assert all(len({nums[i] for i in q})==2 for q in triples)
result={'allowed_triples':triples,'maximum_cap':max(m.bit_count() for m in caps),'cap_histogram':dict(Counter(m.bit_count() for m in caps)),'first_player_wins':winning(0,0),'game_cache_states':winning.cache_info().currsize,'mirror_terminal_leaves_by_second_claim':dict(leaves),'total_mirror_terminal_leaves_all_centers':sum(leaves.values()),'valid_named_color_assignments':colorcounts,'color_witness_passes':True,'number_witness_passes':True,'number_witness_on_each_projected_line':[{'line':q,'numbers':[nums[i] for i in q]} for q in triples]}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
