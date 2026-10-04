"""Independent root-edge recursion and BFS against the final problem instances."""
from functools import lru_cache
from collections import deque
from pathlib import Path
import json
P=Path(__file__).resolve().parent
@lru_cache(None)
def triangulations(vertices):
    if len(vertices)<3:return (frozenset(),)
    out=[];a=vertices[0];b=vertices[-1]
    for k in range(1,len(vertices)-1):
        c=vertices[k]
        join=set()
        if k>1:join.add(tuple(sorted((a,c))))
        if k<len(vertices)-2:join.add(tuple(sorted((c,b))))
        for left in triangulations(vertices[:k+1]):
            for right in triangulations(vertices[k:]):out.append(frozenset(set(left)|set(right)|join))
    assert len(out)==len(set(out))
    return tuple(out)
def es(text):return frozenset(tuple(sorted((ord(w[0])-65,ord(w[1])-65))) for w in text.split())
def stringify(t):return ' '.join(''.join(chr(65+x) for x in e) for e in sorted(t))
def fan(n,v):return frozenset(tuple(sorted((i,v))) for i in range(n) if i!=v and (i-v)%n not in (1,n-1))
T={n:triangulations(tuple(range(n))) for n in range(3,9)}
G={n:{t:tuple(u for u in ts if len(t^u)==2) for t in ts} for n,ts in T.items()}
def route(n,s,t):
    q=deque([s]);prev={s:None}
    while q:
        a=q.popleft()
        if a==t:
            r=[]
            while a is not None:r.append(a);a=prev[a]
            return list(reversed(r))
        for b in G[n][a]:
            if b not in prev:prev[b]=a;q.append(b)
    raise AssertionError('Disconnected')
def check_route(n,r):
    assert all(t in T[n] for t in r)
    assert all(b in G[n][a] for a,b in zip(r,r[1:]))
def serialize_route(r):return [stringify(t) for t in r]
assert [len(T[n]) for n in T]==[1,2,5,14,42,132]
# Actual final packet examples (letter equivalents of K--1 labels where needed).
A6=es('AC AD AE');B6=es('BD BE BF');C6=es('AC AE CE');D6=es('AD BD DF')
S8=es('AC AD DF DG DH');T8=es('AE BD BE EG EH')
assert S8 in T[8] and T8 in T[8]
R={}
R['middle6_short']=[es(x) for x in ['BD BE BF','AE BD BE','AD AE BD','AC AD AE']]
R['middle6_long']=[es(x) for x in ['BD BE BF','BE BF CE','AE BE CE','AC AE CE','AC AD AE']]
for key,r in R.items():check_route(6,r);assert len(set(r))==len(r)
R['upper4_left']=route(6,B6,A6)
R['upper4_middle']=route(6,C6,A6)
R['upper4_right']=route(6,D6,A6)
R['upper5_A']=route(8,S8,fan(8,0))
R['upper5_E']=route(8,S8,fan(8,4))
R['upper7']=route(8,S8,T8)
for key,r in R.items():check_route(8 if key.startswith('upper5') or key=='upper7' else 6,r)
assert [len(R[f'upper4_{x}'])-1 for x in ['left','middle','right']]==[3,1,2]
assert len(R['upper5_A'])-1==3 and len(R['upper5_E'])-1==5 and len(R['upper7'])-1==5
# Verify optimal-fan formula for all labeled examples through 8 corners.
for n,ts in T.items():
 for target in range(n):
  for t in ts:assert len(route(n,t,fan(n,target)))-1==n-3-sum(target in e for e in t)
fixed5=[t for t in T[5] if (0,2) in t]
fixed6=[t for t in T[6] if (0,3) in t]
assert len(fixed5)==2 and len(fixed6)==4
# Which triangle touches the fixed boundary edge AF?
def root_third(n,t):
    edges=set(t)|{tuple(sorted((i,(i+1)%n))) for i in range(n)}
    ks=[k for k in range(1,n-1) if (0,k) in edges and (k,n-1) in edges]
    assert len(ks)==1
    return ks[0]
hex_groups={chr(65+k):[stringify(t) for t in T[6] if root_third(6,t)==k] for k in range(1,5)}
assert [len(v) for v in hex_groups.values()]==[5,2,2,5]
# Nonfan extension: lower bound 3 is strict, and the supplied four-step route is legal.
extra=[es(x) for x in ['BF CE CF','BF CF DF','BD BF DF','AD BD DF','AD AE BD']]
check_route(6,extra)
assert len(route(6,extra[0],extra[-1]))-1==4
assert {next(iter(t-extra[0])) for t in G[6][extra[0]]}=={(3,5),(1,4),(0,2)}
R['extension_nonfan']=extra
res={'counts':{n:len(t) for n,t in T.items()},'pentagons':[stringify(fan(5,v)) for v in range(5)], 'fixed_pentagon':[stringify(t) for t in fixed5], 'fixed_hexagon':[stringify(t) for t in fixed6], 'hex_fan_neighbors':[stringify(t) for t in G[6][A6]],'hex_center_neighbors':[stringify(t) for t in G[6][C6]],'hex_groups':hex_groups,'routes':{key:serialize_route(r) for key,r in R.items()},'all_fan_distances_checked_through_n':8}
(P/'checks.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
