#!/usr/bin/env python3
"""Numerical and order checks for every start printed on the Week 11 student pages.

Moved unchanged from the old student builder (build_packets.py) when the pages became
problem files. Every assigned start is stabilised in 20 random legal orders and by a
memoised search over all legal choices; repeated additions and staged batches are
checked too. Writes checks.json and prints a one-line summary.

The October 23, 2026 card fixes added the checks at the end: they read the printed
starts and row counts from the problem files' figures.py and check the claims the
revised pages rely on (two orders for each start printed twice, more K-1 P4 rows than
stable placements, both triangle circles never empty again, one finish for every
timing in grades 2-3 P5).
"""
from pathlib import Path
import json, random, sys
ROOT=Path(__file__).resolve().parent
for week in (ROOT.parent/'problem-files', ROOT.parent.parent):
    if (week/'figures.py').exists(): break
else: sys.exit('Cannot find the Week 11 problem files (figures.py); see README.md.')
sys.path.insert(0,str(week)); sys.dont_write_bytecode=True
import figures as F  # noqa: E402

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
# Card fixes, October 23, 2026: the revised pages' claims, from the printed starts.
from itertools import product
def words(g,start):
    """Every complete legal sharing word from start."""
    out=[]
    def go(x,w):
        active=[i for i,e in enumerate(g) if x[i]>=len(e)]
        if not active: out.append(w); return
        for i in active:
            y=list(x); y[i]-=len(g[i])
            for j in g[i]:
                if j is not None: y[j]+=1
            go(y,w+'ABC'[i])
    go(list(start),''); return out
printed={'triangle':F.K1_ORDER_TRIANGLE+F.ORDER_TRIANGLE_23+F.ORDER_TRIANGLE_45,
         'square':F.K1_ORDER_SQUARE+F.ORDER_SQUARE_23,'diagonal':F.EXTRA_LINE_23+F.EXTRA_LINE_45}
for name,starts in printed.items():
    assert set(starts)<=set(cases[name]),(name,'printed start not in the checked cases')
# Unhedged "two different orders" (K-1 P1, P3; grades 2-3 P2) and "another order wherever a choice is possible" (P4).
for name,starts in (('triangle',F.K1_ORDER_TRIANGLE),('square',F.K1_ORDER_SQUARE),('square',F.ORDER_SQUARE_23),('diagonal',F.EXTRA_LINE_23),('diagonal',F.EXTRA_LINE_45)):
    for s in starts: assert len(set(words(GRAPHS[name],s)))>=2,(name,s,'only one order')
# "If possible" is needed in grades 2-3 and 4-5 P1: (4,0) has the single word AAB.
assert words(GRAPHS['triangle'],(4,0))==['AAB']
# K-1 P4: 8 stable placements (7 with chips), none with 4 chips; the page has more rows than answers.
stable=[s for s in product(range(4),repeat=3) if all(s[i]<len(GRAPHS['square'][i]) for i in range(3))]
assert len(stable)==8 and sum(1 for s in stable if sum(s))==7 and max(map(sum,stable))==3
assert F.K1_STABLE_ROWS>len(stable)
# K-1 P6: after any number of additions at A, both circles are never empty again; one circle often is.
x=[0,0]; seen=[]
for k in range(1,F.K1_ADD_ONE_ROWS+1):
    x[0]+=1; x=stabilize(GRAPHS['triangle'],x)['finish']; seen.append(tuple(x))
assert (0,0) not in seen and sum(1 for s in seen if 0 in s)==8
# Grades 2-3 P5: together, A's batch first and B's batch first all finish at (1,1,1).
a,b=F.BATCHES_23; g=GRAPHS['square']
together=stabilize(g,[p+q for p,q in zip(a,b)])['finish']
for p,q in ((a,b),(b,a)):
    assert stabilize(g,[u+v for u,v in zip(stabilize(g,p)['finish'],q)])['finish']==together==[1,1,1]
(ROOT/'checks.json').write_text(json.dumps(checks,indent=2))
print('All numerical and order checks of the student pages passed.')
