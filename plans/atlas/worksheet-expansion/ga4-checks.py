#!/usr/bin/env python3
"""Exact finite checks supporting, not replacing, the GA4 written arguments."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
D=Path(__file__).resolve().parent
out={}
# GA-28: exact midpoint signs, cubic cycle and all four-reply histories.
a,b=F(1),F(2);tests=[]
for _ in range(4):
 m=(a+b)/2;tests.append([str(m),str(m*m)])
 if m*m<2:a=m
 else:b=m
assert (a,b)==(F(11,8),F(23,16))
f=lambda x:x**3-2*x+2
N=lambda x:x-f(x)/(3*x*x-2)
assert N(F(0))==1 and N(F(1))==0
assert f(F(-3,2))==F(13,8) and f(F(-7,4))==F(9,64)
for replies in product([0,1],repeat=4):
 l,u=F(1),F(2)
 for reply in replies:
  m=(l+u)/2
  if reply:l=m
  else:u=m
 assert u-l==F(1,16)
for q in [F(k,100) for k in range(1,100)]:assert max(q,1-q)>=F(1,2)
out['GA-28']={'midpoints_and_squares':tests,'retained_bracket':[str(a),str(b)],'all_16_reply_histories_width':'1/16','min_width_tests_for_1/100':next(n for n in range(10) if F(1,2**n)<F(1,100))}
# GA-30: all displayed lifts and a rational-offset sweep, plus closed proof in key.
dist2=lambda d,k:(d+6*k)**2+16
assert [k for k in range(-100,101) if dist2(3,k)==25]==[-1,0]
for j in range(600):
 d=F(j,100);best=min(dist2(d,k) for k in range(-3,4))
 assert best==16+min(d,6-d)**2
 winners=[k for k in range(-3,4) if dist2(d,k)==best]
 assert winners==([0] if d<3 else [-1,0] if d==3 else [-1])
out['GA-30']={'squared_lengths':{str(k):dist2(3,k) for k in range(-2,2)},'rational_offsets_checked':600,'scope':'Written integer-lift bound covers all offsets and windings.'}
# GA-31: all finite interval families on a six-point endpoint grid.
ints=[(a,b) for a in range(6) for b in range(a,6)];count=0
for n in range(1,5):
 for fam in combinations(ints,n):
  pairwise=all(max(a[0],b[0])<=min(a[1],b[1]) for a,b in combinations(fam,2))
  common=max(a for a,b in fam)<=min(b for a,b in fam)
  assert pairwise==common;count+=1
sets=[{0,1},{1,2},{0,2}]
assert all(a&b for a,b in combinations(sets,2)) and not set.intersection(*sets)
A=lambda p:p[0]>=0;B=lambda p:p[1]>=0;C=lambda p:sum(p)<=-1
assert A((0,0)) and B((0,0)) and A((0,-1)) and C((0,-1)) and B((-1,0)) and C((-1,0))
out['GA-31']={'finite_endpoint_families_checked':count,'pair_witnesses':[[0,0],[0,-1],[-1,0]],'scope':'General finite proof is the L/U extremal argument; grid enumeration is only support.'}
# GA-32: cycles of the reversing seam; parity counts intrinsic surface types.
lanes=[]
for m in range(1,33):
 seen=set();cycles=[]
 for i in range(m):
  if i in seen:continue
  cyc=[];j=i
  while j not in seen:seen.add(j);cyc.append(j);j=m-1-j
  cycles.append(cyc)
 ann=sum(len(c)%2==0 for c in cycles);mob=sum(len(c)%2==1 for c in cycles)
 assert ann==m//2 and mob==m%2 and 2*ann+mob==m
 lanes.append({'lanes':m,'annuli':ann,'mobius_bands':mob,'boundary_loops':2*ann+mob})
out['GA-32']={'lane_classifications':lanes,'scope':'Cycle parity models the specified seam; it does not calculate knotting or linking.'}
# GA-33: coefficient-exact ODE and rational-transform identities.
for a in [F(-5),F(-1),F(0),F(1),F(2),F(7,3)]:
 # y=1+(a-1)e^-t; derivative coefficients (0,1-a).
 assert (1-a)+(a-1)==0 and 1+(a-1)==a
 for s in [F(1,10),F(1),F(2),F(7,3)]:
  Y=1/s+(a-1)/(s+1)
  assert (s+1)*Y-a==1/s
  Z=1/(s+1)**2
  assert (s+1)*Z==1/(s+1)
# (te^-t)' + te^-t = (1-t+t)e^-t.
assert [1,-1+1]==[1,0]
out['GA-33']={'starts_tested':6,'positive_transform_parameters':4,'identity':'Boundary/IBP proof and integrating-factor uniqueness are written in the key; checks confirm coefficient and rational identities.'}
# GA-34: exact arrivals, reciprocal law and all chosen starts.
for n in range(21):
 t=1-F(1,2**n);assert 1/(1-t)==2**n
 if n:assert t-(1-F(1,2**(n-1)))==F(1,2**n)
for a in [F(1),F(1,2),F(0),F(-1),F(-3,2)]:
 for t in [F(0),F(1,10),F(1,3)]:
  if 1-a*t==0:continue
  y=a/(1-a*t);der=a*a/(1-a*t)**2
  assert der==y*y
  if a:assert -der/(y*y)==-1
out['GA-34']={'doubling_arrivals_checked':21,'initial_values_checked':['1','1/2','0','-1','-3/2'],'scope':'Rational derivative identity and limiting blow-up argument are analytic proofs in the key.'}
# GA-35: polynomial expansion of a four-sample mean for many exact inputs.
count=0
for A,B,C in product(range(-2,3),repeat=3):
 for a,b,u,v in product(range(-1,2),repeat=4):
  Dc,Ec,Kc=2,-3,5
  q=lambda x,y:A*x*x+B*x*y+C*y*y+Dc*x+Ec*y+Kc
  ds=[(u,v),(-v,u),(-u,-v),(v,-u)]
  mean=sum(F(q(a+x,b+y),4) for x,y in ds)
  assert mean==q(a,b)+F((A+C)*(u*u+v*v),2);count+=1
assert sum([5,-3,-15,1])/4==-3
# cos² sin²=(1-cos4θ)/8 gives circle mean r⁴/8; finite samples at axes zero and 45° 1/4.
out['GA-35']={'exact_quadratic_cases':count,'unit_circle_quartic_means':{'cardinal':'0','rotated_45_degrees':'1/4','continuous':'1/8'},'scope':'Trigonometric integral identity is proved in the key, not inferred from samples.'}
# GA-36: entire finite parameter grid and exact iterate identity.
count=0
for q in [F(j,10) for j in range(-10,11)]:
 for x0 in [F(j,10) for j in range(11)]:
  x=x0
  for n in range(9):
   assert 0<=x<=1 and x-F(1,2)==q**n*(x0-F(1,2));count+=1
   x=F(1,2)+q*(x-F(1,2))
assert F(1,2*3**4)<F(1,100)<F(1,2*3**3)
out['GA-36']={'exact_iterate_cases':count,'worst_error_after_four':'1/162','scope':'Geometric limit and IVT arguments establish the continuous claims.'}
(D/'ga4-checks-results.json').write_text(json.dumps({'status':'pass','families':out},indent=2)+'\n')
print('GA4 exact checks pass:',len(out),'families')
