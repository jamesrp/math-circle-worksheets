#!/usr/bin/env python3
"""Independent AP2 review certificates. General arguments live in the review note.
No author files are changed or imported. All numerical tests here are exact.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from collections import Counter
import json
HERE=Path(__file__).resolve().parent
results={}
def record(k,**kw):results[k]=kw

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def plus(A,B):return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def transpose(A):return [list(x) for x in zip(*A)]
def outer(v):return [[a*b for b in v] for a in v]

# Flux: independently solve weighted sections and branch equations by rational grids.
profiles=[]
for i in range(121):
 v=F(i,20);u=12-2*v
 assert u>=0 and (u+2*v)/3==4
 profiles.append((u,v))
assert F(12-9,4)==F(3,4) and F(20-8,12-9)==4
assert F(12,9)==F(4,3)
record('AP-11',weighted_profiles=len(profiles),patch_test_mean='4',arithmetic_mean='7/2',tank_fill_time=4,gas_density='4/3')

# A different global certificate for the crossing: supporting unit vectors.
# sqrt(x^2+4^2) >= (3x+16)/5 and sqrt((7-x)^2+3^2) >= (4(7-x)+9)/5.
# Divide respectively by 3,4: slopes cancel, lower bound is 35/12.
assert F(3,15)-F(4,20)==0
assert F(16,15)+F(37,20)==F(35,12)
assert F(35,12)**2 < 2*F(25,12)**2
assert 3*3+4*4==25 and 4*4+3*3==25
# Equality of the first Cauchy inequality forces the first vector to be (3,4).
record('AP-12',independent_global_lower_bound='35/12',equality_crossing=3,direct_crossing=4,direct_time_squared='625/72',optimal_time_squared='1225/144',proof='Supporting unit vectors give a sharp affine lower bound for every real crossing; equality at x=3.')

# Generate exact rational phase coordinates by the unit-circle parameter.
phasors=set()
for p in range(-12,13):
 for q in range(1,13):
  c=F(q*q-p*p,q*q+p*p);s=F(2*p*q,q*q+p*p)
  phasors.add((c,s))
for c,s in phasors:
 I=(2+c)**2+s*s;J=(2+c)**2+(s+1)**2
 assert I==5+4*c and 1<=I<=9
 assert (I-5)/4==c and (J-I-1)/2==s
 assert ((I-5)/4)**2+((J-I-1)/2)**2==1
assert (F(37,5)-5)/4==F(3,5) and (F(10)-F(37,5)-1)/2==F(4,5)
record('AP-13',distinct_exact_phase_coordinates=len(phasors),coordinate_recovery='all passed',impossible_observation=[5,6],reference_outputs=[8,4])

# Heat ledger across every selection of descending intermediate temperatures.
heat_records=0
for mid1 in range(325,600,25):
 for mid2 in range(300,mid1,25):
  temps=[F(600),F(mid1),F(mid2),F(300)]
  q=F(12);work=0;entropy=0
  for hot,cold in zip(temps,temps[1:]):
   qnext=q*cold/hot
   entropy+=qnext/cold-q/hot;work+=q-qnext;q=qnext
  assert q==6 and work==6 and entropy==0
  heat_records+=1
qout=F(27,4);work=12-qout;S=qout/300-F(12,600)
assert work==F(21,4) and S==F(1,400) and 6-work==300*S==F(3,4)
record('AP-14',reversible_cascade_tests=heat_records,loss_work='3/4',entropy='1/400',fridge_minimum_input=6)

# Independent density-matrix update. This avoids the author's state-history routine.
I2=[[F(1),F(0)],[F(0),F(1)]];rho0=[[F(1),F(0)],[F(0),F(0)]]
Z=[outer([F(1),F(0)]),outer([F(0),F(1)])]
X=[[[F(1,2),F(sign,2)],[F(sign,2),F(1,2)]] for sign in [1,-1]]
def channel(rho,projectors):
 out=[[F(0),F(0)],[F(0),F(0)]]
 for P in projectors:out=plus(out,mm(mm(P,rho),P))
 return out
assert channel(rho0,Z)==rho0
assert channel(channel(rho0,X),Z)==[[F(1,2),F(0)],[F(0),F(1,2)]]
assert channel(channel(rho0,Z),X)==channel(channel(rho0,X),Z) # final mixed state is equal; recorded Z histories are not.
for c,s in phasors:
 P=outer([c,s]);Q=outer([-s,c]);rho=channel(rho0,[P,Q])
 assert rho[1][1]==2*c*c*s*s<=F(1,2)
 assert rho[1][1]==F(1,2)-2*(s*s-F(1,2))**2
assert channel(rho0,[outer([F(3,5),F(4,5)]),outer([F(-4,5),F(3,5)])])[1][1]==F(288,625)
# Bloch-axis calculation for two prescribed questions: final z bias is product
# cos(2alpha) cos(2(beta-alpha)) cos(2beta)=(1/2)(1/2)(-1/2).
z_bias=F(1,2)*F(1,2)*F(-1,2)
assert (1-z_bias)/2==F(9,16)
record('AP-15',exact_projector_bases=len(phasors),single_bound='1/2',rational_target='288/625',two_question_target='9/16',final_unobserved_XZ_and_ZX_states_equal=True)

# Polynomial transfer matrices count agreements, independently of link encoding.
def padd(p,q):return tuple((p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q))))
def pmul(p,q):
 r=[0]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):r[i+j]+=a*b
 return tuple(r)
def mat_poly(A,B):return [[padd(pmul(A[i][0],B[0][j]),pmul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
T=[[(0,1),(1,)],[(1,),(0,1)]];P=[[(1,),(0,)],[(0,),(1,)]]
for n in range(1,13):
 P=mat_poly(P,T)
 if n==3:open_polynomial=padd(padd(P[0][0],P[0][1]),padd(P[1][0],P[1][1]))
 if n==4:ring_polynomial=padd(P[0][0],P[1][1])
assert open_polynomial==(2,6,6,2) and ring_polynomial==(2,0,12,0,2)
assert sum(c*2**a for a,c in enumerate(open_polynomial))==54
assert sum(c*2**a for a,c in enumerate(ring_polynomial))==82
# 3-ticket elementary draws: enumerate all 162 equally likely full proposals.
accepted=Counter()
for first in [-1,1]:
 for tickets in product(['A1','A2','D'],repeat=4):
  spins=[first]
  for ticket in tickets:spins.append(spins[-1] if ticket!='D' else -spins[-1])
  if spins[-1]==first:accepted[tuple(spins[:-1])]+=1
assert sum(accepted.values())==82 and len(accepted)==16
for spins,count in accepted.items():
 a=sum(spins[i]==spins[(i+1)%4] for i in range(4))
 assert count==2**a
record('AP-16',transfer_polynomial_open=open_polynomial,transfer_polynomial_ring=ring_polynomial,elementary_accepted_proposals=82,elementary_all_proposals=162,acceptance='41/81')

# Spacetime: direct form coefficients, future time and exact event differences.
B=[[F(5,4),F(-3,4)],[F(-3,4),F(5,4)]];eta=[[1,0],[0,-1]]
assert mm(mm(transpose(B),eta),B)==eta
def boost(t,x):return ((5*t-3*x)/4,(5*x-3*t)/4)
for ti in range(1,25):
 for xi in range(-ti+1,ti):
  t,x=F(ti,3),F(xi,3);tp,xp=boost(t,x)
  assert tp>0 and tp*tp-xp*xp==t*t-x*x
Tprime=boost(F(5),F(3));Rprime=boost(F(10),F(0))
assert Tprime==(4,0) and Rprime==(F(25,2),F(-15,2))
assert (Rprime[0]-4)**2-Rprime[1]**2==16
record('AP-17',primed_turn=['4','0'],primed_reunion=['25/2','-15/2'],interval_invariance='exact identity and future-timelike tests passed',route_for_six=[5,4],fixed_excursion_infimum_squared=40)

# Orbit inverse: exact endpoint images and independent parameter constructions.
Msets=[(F(4)*F(29,10)**2,F(4)*F(31,10)**2),(F(9)*F(19,10)**2,F(9)*F(21,10)**2)]
assert (max(a for a,b in Msets),min(b for a,b in Msets))==(F(841,25),F(961,25))
assert F(3,2)+F(1,4)==2-F(1,4)==F(7,4)
for denominator in range(1,51):
 for numerator in range(1,denominator+1):
  q=F(numerator,denominator);M=36/q**2
  assert M>=36 and q*q*M==36
v=F(8)/F(4,3);assert v==6 and 4*v*v==144 and 3/v==F(1,2)
record('AP-18',compatible_mass_interval=['841/25','961/25'],strict_error_threshold='1/4',touching_reading='7/4',period_solution={'v':6,'M':144,'q':'1/2'})

D=json.loads((HERE/'ap2-data.json').read_text())
assert len(D['families'])==8
assert sum(len(p['prompts']) for f in D['families'] for p in f['pages'])==48
assert sum(len(f['extensions']) for f in D['families'])==8
report={'status':'PASS','reviewer':'expand_ad1','families':8,'prompts':48,'extensions':8,'checks':results,'scope':'Exact finite/identity corroboration; complete proofs and source hypotheses reviewed separately.'}
(HERE/'review-ap2-checks-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('AP2 independent checks PASS: 8 families, 48 prompts, 8 extensions; density matrices and polynomial transfer matrices independently audited.')
