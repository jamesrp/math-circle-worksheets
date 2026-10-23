#!/usr/bin/env python3
"""Numerical and order checks for every start printed on the Week 11 student pages.

Moved unchanged from the old student builder (build_packets.py) when the pages became
problem files. Every assigned start is stabilised in 20 random legal orders and by a
memoised search over all legal choices; repeated additions and staged batches are
checked too. Writes checks.json and prints a one-line summary.
"""
from pathlib import Path
import json, random
ROOT=Path(__file__).resolve().parent

# Verify all authored numerical cases and independent legal orders.
GRAPHS={'triangle':[[1,None],[0,None]],'square':[[1,None],[0,2],[1,None]],'diagonal':[[1,2,None],[0,2],[0,1,None]]}
def stabilize(g,start,rng=None):
    x=list(start); cnt=[0]*len(x); sink=0
    while True:
        active=[i for i,e in enumerate(g) if x[i]>=len(e)]
        if not active:return {'finish':x,'shares':cnt,'sink':sink}
        i=active[0] if rng is None else rng.choice(active)
        x[i]-=len(g[i]); cnt[i]+=1
        for j in g[i]:
            if j is None:sink+=1
            else:x[j]+=1
        assert sum(cnt)<100000
cases={'triangle':[(2,2),(3,2),(2,3),(3,3),(4,0),(5,4),(3,3),(2,4)]+[(i,6-i) for i in range(7)],'square':[(0,4,0),(2,2,0),(0,2,2),(2,0,2),(2,1,2),(2,4,2),(2,4,0),(3,0,3),(0,12,0),(6,0,6),(4,4,4),(0,8,0)],'diagonal':[(3,0,3),(0,6,0),(2,2,2),(4,1,2)]}
checks={}
for name,starts in cases.items():
    g=GRAPHS[name]; result=[]
    for start in starts:
        expected=stabilize(g,start)
        for seed in range(20): assert stabilize(g,start,random.Random(seed))==expected
        result.append({'start':start,**expected})
    checks[name]=result
# All legal choices via memoization, not just sampled orders, on the assigned starts.
from functools import lru_cache
for name,starts in cases.items():
    g=GRAPHS[name]
    @lru_cache(None)
    def outcomes(state):
        active=[i for i,e in enumerate(g) if state[i]>=len(e)]
        if not active:return frozenset([(state,tuple([0]*len(g)))])
        result=set()
        for i in active:
            n=list(state);n[i]-=len(g[i])
            for j in g[i]:
                if j is not None:n[j]+=1
            for fin,cnt in outcomes(tuple(n)):
                c=list(cnt);c[i]+=1;result.add((fin,tuple(c)))
        return frozenset(result)
    for start in starts:assert len(outcomes(tuple(start)))==1
checks['repeated_A']={}
for start in [(0,0),(1,0),(0,1),(1,1)]:
    x=list(start);seq=[]
    for _ in range(12):
        x[0]+=1;x=stabilize(GRAPHS['triangle'],x)['finish'];seq.append(x[:])
    checks['repeated_A'][str(start)]=seq
for x,y in [((0,4,0),(2,0,0)),((3,0,0),(0,0,3))]:
    g=GRAPHS['square'];both=stabilize(g,[a+b for a,b in zip(x,y)])['finish']
    for p,q in [(x,y),(y,x)]:
        z=stabilize(g,p)['finish']; assert stabilize(g,[a+b for a,b in zip(z,q)])['finish']==both
(ROOT/'checks.json').write_text(json.dumps(checks,indent=2))
print('All numerical and order checks of the student pages passed.')
