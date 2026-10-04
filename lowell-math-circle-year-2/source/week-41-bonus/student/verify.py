#!/usr/bin/env python3
"""Exact independent mathematical checks, standard library only."""
from collections import deque,Counter
import json
D={'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}
def displacement(w):return tuple(sum(D[a][k] for a in w) for k in (0,1))
def orbit(w):
    v=displacement(w);p=(0,0);out=[]
    while p not in out:out.append(p);p=tuple((p[k]+v[k])%3 for k in (0,1))
    return out
assert [len(orbit(w)) for w in ['R','RU','RRR','RULD','RRU']]==[3,3,1,1,3]
# All oriented tours rooted at H; final step returns to H, vertices may not repeat before it.
tours=[]
def dfs(p,seen,w):
    if len(seen)==9:
        for a,v in D.items():
            q=((p[0]+v[0])%3,(p[1]+v[1])%3)
            if q==(0,0):tours.append(w+a)
        return
    for a,v in D.items():
        q=((p[0]+v[0])%3,(p[1]+v[1])%3)
        if q not in seen:dfs(q,seen|{q},w+a)
dfs((0,0),{(0,0)},'')
wind=Counter(tuple(k//3 for k in displacement(w)) for w in tours)
assert len(tours)==96
assert len(wind)==12
assert (0,0) not in wind
assert wind==Counter({(-2,-1):3,(-2,1):3,(-1,-2):3,(-1,0):18,(-1,2):3,(0,-1):18,(0,1):18,(1,-2):3,(1,0):18,(1,2):3,(2,-1):3,(2,1):3})
assert displacement('RL')==(0,0) and displacement('RR')==(2,0)
# Unbounded periodic-map BFS, finite search until the three targets are found.
def blocked(p):x,y=p;return (x%3,y%3) in {(1,0),(0,1)}
targets={(3,0),(0,3),(3,3)};q=deque([((0,0),'')]);seen={(0,0)};answers={}
while q and targets-set(answers):
    p,w=q.popleft()
    if p in targets:answers[p]=w
    for a,v in D.items():
        s=(p[0]+v[0],p[1]+v[1])
        if s not in seen and not blocked(s):seen.add(s);q.append((s,w+a))
assert {p:len(w) for p,w in answers.items()}=={(3,0):5,(0,3):5,(3,3):8}
for target,w in {(3,0):'DRRRU',(0,3):'LUURU',(3,3):'LUURRRRU'}.items():
 p=(0,0)
 for a in w:
  p=(p[0]+D[a][0],p[1]+D[a][1]);assert not blocked(p)
 assert p==target and len(w)==len(answers[target])
print(json.dumps({'orbit_lengths':{w:len(orbit(w)) for w in ['R','RU','RRR','RULD','RRU']},'rooted_oriented_tours':len(tours),'winding_counts':{str(k):v for k,v in sorted(wind.items())},'tour_witnesses':{str(k):next(w for w in tours if tuple(t//3 for t in displacement(w))==k) for k in sorted(wind)},'blocked_shortest_routes':{str(k):v for k,v in answers.items()}},indent=2))
