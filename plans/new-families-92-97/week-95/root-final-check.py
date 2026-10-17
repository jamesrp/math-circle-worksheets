from fractions import Fraction as F
from itertools import combinations
from math import comb
import json
cases=0
for N in range(1,13):
 for M in range(1,min(6,N)+1):
  first=set(range(M))
  for n in range(1,min(6,N)+1):
   hist={}
   for second in combinations(range(N),n):
    overlap=len(first.intersection(second));hist[overlap]=hist.get(overlap,0)+1
   assert sorted(hist)==list(range(max(0,M+n-N),min(M,n)+1))
   assert F(sum(r*c for r,c in hist.items()),sum(hist.values()))==F(M*n,N)
   cases+=1
# Every printed fixed record, with explicit set witnesses for arbitrary unseen extras.
for M,n,rs in [(5,5,[3,0]),(4,4,[0,1,2,3]),(5,4,list(range(5))),(6,6,[0,1,2,3])]:
 for r in rs:
  first=set(range(M)); second=set(range(r))|set(range(M,M+n-r))
  assert len(first)==M and len(second)==n and len(first&second)==r and len(first|second)==M+n-r
assert 5+5-3==7 and [N for N in [6,7,8,12,20] if N>=7]==[7,8,12,20]
assert 5+5==10
assert {N:list(range(max(0,9-N),5)) for N in [6,8,12]}=={6:[3,4],8:[1,2,3,4],12:[0,1,2,3,4]}
assert 6+6-2==10 and 6+6==12
assert F(2,6)==F(1,3) and 6*6//2==18
assert [F(36,r) for r in [1,2,3,2]]==[36,18,12,18]
assert all(max(0,12-18)<=r<=6 for r in [1,2,3,2,0])
# Hypergeometric record likelihoods confirm lower packet does not yield certainty.
def prob(N,M,n,r):
 if not max(0,M+n-N)<=r<=min(M,n):return F(0)
 return F(comb(M,r)*comb(N-M,n-r),comb(N,n))
like={}
for N in [8,16]:
 p=F(1)
 for r in [2,1,3,1,2,0]:p*=prob(N,4,4,r)
 assert p>0;like[N]=str(p)
# Balanced integer split maximizes only the stated expected overlap objective.
budgets={}
for s in range(2,25):
 products={M:M*(s-M) for M in range(1,s)};best=max(products.values())
 winners=[M for M,v in products.items() if v==best]
 assert winners==sorted(set([s//2,(s+1)//2]))
 if s in [12,13,20]:budgets[s]={'first_sizes':winners,'expected_overlap':str(F(best,24))}
# A strictly positive-overlap example demonstrates bias without undefined outcomes.
bias=sum(prob(6,4,3,r)*F(12,r) for r in [1,2,3]);assert bias==F(34,5)!=6
print(json.dumps({'status':'pass','direct_subset_models':cases,'printed_lower_repeat_likelihoods':like,'budget_checks':budgets,'biased_estimate_mean':str(bias),'limits':'Finite enumeration checks data; report supplies general proofs. Physical handling untested.'},indent=2))
