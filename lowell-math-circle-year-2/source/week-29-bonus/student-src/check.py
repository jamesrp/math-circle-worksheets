#!/usr/bin/env python3
from functools import lru_cache
import json
@lru_cache(None)
def words(n):
 if n==0:return [()]
 if n<0:return []
 return [(r,)+w for r in (3,4) for w in words(n-r)]
W={n:words(n) for n in (7,10,14,18)}
assert [len(W[n]) for n in W]==[2,3,6,11]
for n in range(1,50):assert len(words(n))==len(words(n-3))+len(words(n-4))
finite={3*x+4*y for x in range(5) for y in range(4)}
gaps=sorted(set(range(25))-finite)
assert gaps==[1,2,5,19,22,23] and all((24-n in finite)==(n in finite) for n in range(25))
def reachable(steps,N=100):
 s={0}
 for n in range(1,N+1):
  if any(n-r in s for r in steps):s.add(n)
 return s
def minimum(n,steps):
 dp=[0]+[999]*n
 for k in range(1,n+1):dp[k]=min((1+dp[k-r] for r in steps if r<=k),default=999)
 return dp[n]
base=reachable((3,5));new={r:sorted(reachable((3,5,r))-base) for r in (8,7,4)}
mins={n:{'3_5':minimum(n,(3,5)),'3_5_8':minimum(n,(3,5,8))} for n in (16,24)}
assert new=={8:[],7:[7],4:[4,7]}
assert mins=={16:{'3_5':4,'3_5_8':2},24:{'3_5':6,'3_5_8':3}}
print(json.dumps({'words':W,'finite_reachable':sorted(finite),'finite_gaps':gaps,'third_length_new_targets_through100':new,'minimum_piece_counts':mins},indent=2))
