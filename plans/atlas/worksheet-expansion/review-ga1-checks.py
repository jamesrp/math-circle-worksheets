"""Independent reviewer calculations for GA1; does not import author checker."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
R={}
# Apply quarter-turns directly to coordinates, rather than reading author's matrices.
def turn(v,name):
 x,y,z=v
 return {'X':(x,-z,y),'x':(x,z,-y),'Y':(z,y,-x),'y':(-z,y,x)}[name]
def apply(v,w):
 for name in w:v=turn(v,name)
 return v
wins={n:[''.join(w)for w in product('XxYy',repeat=n)if apply((0,0,1),w)==(0,0,1)and apply((1,0,0),w)!=(1,0,0)]for n in range(1,4)}
assert not wins[1]and not wins[2]and len(wins[3])==8
comm=[]
for a,b in product(range(4),repeat=2):
 if all(apply(v,'X'*a+'Y'*b)==apply(v,'Y'*b+'X'*a)for v in [(1,0,0),(0,1,0),(0,0,1)]):comm.append([a,b])
assert len(comm)==8
R['GA-01']={'minimum':3,'shortest_words':wins[3],'commuting_power_pairs':comm}
# Interpolate the actual cyclic profile and verify all roots explicitly.
h=[0,5,1,4,2,3]
def height(x):
 x=x%6;i=x.numerator//x.denominator;t=x-i
 return h[i]+t*(h[(i+1)%6]-h[i])
roots=[]
for i in range(3):
 d0=height(Q(i))-height(Q(i+3));d1=height(Q(i+1))-height(Q(i+4))
 r=i-d0/(d1-d0);assert height(r)==height(r+3);roots.append([r,height(r)])
assert roots==[[Q(4,7),Q(20,7)],[Q(8,5),Q(13,5)],[Q(7,3),Q(2)]]
R['GA-02']={'roots_and_heights':roots}
# Independent enumeration indices and strict budget partial sum.
flat=[(p,q)for q in range(1,102)for p in range(q+1)]
assert [flat.index(z)+1 for z in [(2,3),(4,7),(37,101)]]==[8,32,5188]
for n in range(1,31):assert sum(Q(1,100*2**(k+1))for k in range(1,n+1))+Q(1,100*2**(n+1))==Q(1,200)
R['GA-03']={'indices':[8,32,5188],'total_budget':'1/200'}
# Continuous root choice proof is separate; inspect explicit signed endpoint arithmetic.
for k in range(-20,21):assert ((Q(360*k,2)%360)==0)==(k%2==0)
assert [(120+360*j)/3 for j in range(3)]==[40,160,280]
R['GA-04']={'tested_net_turns':41,'triple_roots':[40,160,280]}
# Derive shortcut using b=(a+c)/2 and a+c=R; substitute both endpoints.
for right in [12,16]:
 a=Q(3*right,8);b=Q(right,2);c=Q(5*right,8)
 assert a==(b+c)/3 and b==(a+c)/2 and c==(a+b+right)/3
R['GA-05']={'shortcut12':['9/2','6','15/2'],'shortcut16':['6','8','10']}
# Exact printed complex examples (binary-exact quarter fractions).
for z in [1+1j,2-1j]:
 for w in [1j*z,-1j*z]:assert z*z+w*w==0
for u,z,w in [(2,0.75j,1.25),(1j,-1,0)]:
 assert w-1j*z==u and w+1j*z==1/u and z*z+w*w==1
R['GA-06']={'printed_complex_examples':6,'inverse_formulas_checked':True}
# Polynomial evaluation at rational points independently checks expanded composition.
for x in [Q(i,7)for i in range(-28,29)]:
 double=lambda z:2*z*z-1;triple=lambda z:4*z**3-3*z
 expected=32*x**6-48*x**4+18*x*x-1
 assert double(triple(x))==triple(double(x))==expected
for x in [Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)]:assert x*(x*x-1)*(x*x-Q(1,4))==0
assert Q(1,4)*(Q(1,16)-1)*(Q(1,16)-Q(1,4))!=0
R['GA-07']={'rational_composition_points':57,'fake_fit_roots':5}
# Join quotients and unbounded Lipschitz quotient; continuum arguments in review.
for c in [Q(3,2),Q(2)]:
 for n in range(1,30):
  h=Q(1,2**n)
  y=lambda t:max(t-c,0)**2
  assert (y(c+h)-y(c))/h==h and(y(c-h)-y(c))/(-h)==0
for n in range(1,50):assert (2*Q(1,n))/Q(1,n*n)==2*n
R['GA-08']={'exact_join_checks':58,'lipschitz_ratios':'2n for h=1/n²','proofs':'Monotonic zero set; derivative of sqrt(y)=1 on positive region; continuity fixes intercept.'}
Path(__file__).with_name('review-ga1-checks-results.json').write_text(json.dumps(R,indent=2,default=str)+'\n')
print('Independent GA1 calculations passed: all eight families.')
