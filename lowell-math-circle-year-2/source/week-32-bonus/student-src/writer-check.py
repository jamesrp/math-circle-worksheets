#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations_with_replacement
from pathlib import Path
import json
area30={str(k):[list(s) for s in combinations_with_replacement(range(1,6),k) if sum(a*a for a in s)==30] for k in range(1,5)}
assert area30=={'1':[],'2':[],'3':[[1,2,5]],'4':[[1,2,3,4]]}
def tiling(w,h,sizes):
    full=(1<<(w*h))-1
    @lru_cache(None)
    def solve(mask):
        if mask==full:return ()
        first=next(i for i in range(w*h) if not mask>>i&1)
        x,y=first%w,first//w
        for s in sizes:
            if x+s>w or y+s>h:continue
            block=sum(1<<(yy*w+xx) for yy in range(y,y+s) for xx in range(x,x+s))
            if mask&block:continue
            rest=solve(mask|block)
            if rest is not None:return ((x,y,s),)+rest
        return None
    return solve(0)
restricted={f'{w}x5':tiling(w,5,(3,2)) for w in (5,6,7)}
assert restricted['5x5'] is None and restricted['6x5'] and restricted['7x5'] is None
cells=[]
construction=[(0,0,3),(3,0,3),(0,3,2),(2,3,2),(4,3,2)]
for x,y,s in construction:cells.extend((xx,yy) for xx in range(x,x+s) for yy in range(y,y+s))
assert len(cells)==len(set(cells))==30 and set(cells)=={(x,y) for x in range(6) for y in range(5)}
def recipe(a,b):
    a,b=max(a,b),min(a,b);counts=[];sizes=[]
    while b:
        q,r=divmod(a,b);counts.append(q);sizes.extend([b]*q);a,b=b,r
    return counts,sizes
recipes={f'{a}x{b}':recipe(a,b) for a,b in ((5,2),(3,2),(8,3),(7,4))}
assert recipes['5x2'][0]==[2,2]
assert [recipes[k][0] for k in ['3x2','8x3','7x4']]==[[1,2],[2,1,2],[1,1,3]]
assert all(recipe(a*2,b*2)[0]==recipe(a,b)[0] for a,b in ((3,2),(8,3),(7,4)))
report={'area30_decompositions_by_piece_count':area30,'restricted_tilings':restricted,'five_piece_construction':construction,'recipes':recipes}
(Path(__file__).resolve().parent.parent/'writer-check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
