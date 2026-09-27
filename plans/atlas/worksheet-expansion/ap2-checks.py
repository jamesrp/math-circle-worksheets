#!/usr/bin/env python3
"""Exact finite checks for AP11–18. General proofs remain in the keyed text.

Fractions and exhaustive finite histories verify the actual printed instances.
Polynomial arithmetic independently audits identities used by the proofs.
No numeric sampling is presented as a proof over a continuum.
"""
import json, math
from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
DATA=json.loads((HERE/'ap2-data.json').read_text())
FAMS={f['id']:f for f in DATA['families']}
assert list(FAMS)==[f'AP-{n:02d}' for n in range(11,19)]
required=['id','title','core_gate','index_gate','extension_gate','reading','materials','prep_minutes','timing','launch','satisfying_stop','prior_use','assessment','mathematical_connection','sources','pages','extensions','figures']
for f in FAMS.values():
 assert all(k in f for k in required)
 assert len(f['pages'])==3 and len(f['extensions'])==1
 prompts=[p for pg in f['pages'] for p in pg['prompts']]
 assert [p['id'] for p in prompts]==list(map(str,range(1,7)))
 assert all(p['solution'] and p['hints'] for p in prompts)
 assert all(s['checked'] and s['locator'] for s in f['sources'])
RESULT={'batch':'ap2','status':'PASS','student_pages':24,'student_prompts':48,'guide_extensions':8,'checks':{}}
def record(family,details):RESULT['checks'][family]=details

def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def mv(a,x):return [sum(ai*xi for ai,xi in zip(row,x)) for row in a]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def norm2(x):return dot(x,x)

# AP11: profiles and splits are checked exactly, including zero endpoints.
q=F(6)*2; assert q==12 and q/3==4
profiles=[(0,6),(8,2),(4,4),(2,5)]
assert all(F(u)+2*F(v)==q for u,v in profiles)
assert (F(2)+5)/2==F(7,2) and (F(2)+2*5)/3==4
splits=[(F(k,12),12-2*F(k,12)) for k in range(73)]
assert all(2*u+v==12 and u>=0 and v>=0 for u,v in splits)
assert splits[0]==(0,12) and splits[-1]==(6,0)
assert 2*2+8==12 and 2*5+2==12 and 2*4+4==12
assert (20-8)/F(12-9)==4 and F(12-9,4)==F(3,4)
assert F(4,3)*3*3==12
# All four boundary fluxes of (ax,by) on 2x1: 0,2a,0,2b.
for a,b in product(range(-3,4),repeat=2): assert (2*a+2*b==0)==(a+b==0)
record('AP-11',dict(Q=12,narrow_mean=4,profiles=profiles,branch_nonnegative_fraction_grid=len(splits),tank_overflow_time=4,tank_height_rate='3/4',gas_outlet_density='4/3',divergence_boundary_identity='2a+2b=2(a+b)'))

# AP12: exact candidate and time comparison. Positivity proof is in the guide.
assert 3**2+4**2==5**2 and 4**2+3**2==5**2
assert F(3,3*5)-F(4,4*5)==0
assert F(5,3)+F(5,4)==F(35,12)
assert 35**2 < 25**2*2 # exact T(3)<T(4)
assert F(1,3)-F(1,4)==F(1,12) # T'(4) coefficient of 1/sqrt(2)
# Check the inverse-speed derivative balance on varied exact target choices
# with float square roots only as regression support, not a continuum proof.
inverse=[]
for s in [F(1,2),F(1),F(2),F(3),F(4),F(5),F(13,2)]:
 x=float(s); l1=math.sqrt(x*x+16);l2=math.sqrt((7-x)**2+9)
 w=3*(7-x)*l1/(x*l2)
 derivative=x/(3*l1)-(7-x)/(w*l2)
 assert abs(derivative)<1e-14 and w>0
 inverse.append({'target':str(s),'lower_speed':w,'derivative_residual':derivative})
assert abs(inverse[3]['lower_speed']-4)<1e-14 and abs(inverse[4]['lower_speed']-3)<1e-14
record('AP-12',dict(exact_stationary_x=3,optimal_time='35/12',direct_crossing_x=4,direct_time='25sqrt(2)/12',constrained_gate=[4,6],constrained_minimizer=4,inverse_design_regressions=inverse,proof_scope='T second derivative strictly positive in key; finite evaluations do not prove global minimum.'))

# AP13: work in exact coefficient pairs P sin t+Q cos t; I=P^2+Q^2.
assert norm2([F(2),0])==4 and norm2([F(3),0])==9 and norm2([F(1),0])==1
assert norm2([F(2)-2,0])==0
for c,s in [(1,0),(-1,0),(0,1),(0,-1),(F(3,5),F(4,5)),(F(3,5),F(-4,5))]:
 c,s=F(c),F(s); assert c*c+s*s==1
 P,Q=2+c,s; I=P*P+Q*Q; J=P*P+(Q+1)**2
 assert I==5+4*c and J==I+1+2*s
 assert (I-5)/4==c and (J-I-1)/2==s
assert norm2([2,2])==8 and norm2([2,0])==4
assert norm2([3,1])==norm2([3,-1])==10
I,J=F(37,5),F(10);assert (I-5)/4==F(3,5) and (J-I-1)/2==F(4,5)
assert ((F(5)-5)/4)**2+((F(6)-5-1)/2)**2==0
record('AP-13',dict(original_brightness=4,aligned=9,opposed=1,range=[1,9],reference_cos_outputs=[8,4],reference_sin_outputs=[10,10],decoded_coordinates=['3/5','4/5'],inconsistent_pair=[5,6],exact_unit_circle_instances=6))

# AP14: all small rational candidate splits; reversible cascades and loss identity.
for k in range(49):
 Qc=F(k,4);W=12-Qc;S=Qc/300-F(12,600)
 assert (S>=0)==(W<=6)
 assert 6-W==300*S
for mid in [F(301),F(350),F(400),F(450),F(599)]:
 qm=12*mid/600; qc=qm*300/mid
 assert qc==6 and (12-qm)+(qm-qc)==6
for temps in [[600,500,400,300],[600,450,375,300],[600,300]]:
 heat=F(12);work=F(0)
 for a,b in zip(temps,temps[1:]):
  new=heat*F(b,a);work+=heat-new;heat=new
 assert heat==6 and work==6
qm=F(9);qc=qm*F(300,400);w=12-qm+qm-qc;s=qc/300-F(12,600)
assert qc==F(27,4) and w==F(21,4) and s==F(1,400) and 6-w==F(3,4)==300*s
qc=F(6);win=qc*(F(600,300)-1); assert win==6 and qc/win==1
record('AP-14',dict(audited_quarter_unit_splits=49,maximum_work=6,intermediate_temperatures_checked=5,multistage_cascades_checked=3,loss_example={'W':'21/4','Qc':'27/4','Sgen':'1/400','lost_work':'3/4'},refrigerator_min_work=6))

# AP15: projector algebra (exact rational), all four-state histories and arbitrary p.
P0=[[F(1),F(0)],[F(0),F(0)]];Pplus=[[F(1,2)]*2,[F(1,2)]*2]
a=mm(P0,Pplus);b=mm(Pplus,P0)
assert a!=b and norm2(mv(a,[1,0]))==F(1,4) and norm2(mv(b,[1,0]))==F(1,2)
# Four named states: cross-basis probabilities 1/2, within-basis Kronecker delta.
bases={'Z':['0','1'],'X':['+','-']}
def probability(out,old):
 return (F(1) if out==old else F(0)) if any(out in v and old in v for v in bases.values()) else F(1,2)
def tree(seq):
 histories=[((), '0',F(1))]
 for name in seq:
  histories=[(hist+((name,out),),out,p*probability(out,state)) for hist,state,p in histories for out in bases[name]]
 assert sum(p for _,_,p in histories)==1
 return histories
for seq,expected in [('XZ',F(1,2)),('ZX',F(0)),('ZZ',F(0)),('ZXZ',F(1,2))]:
 histories=tree(seq)
 observed=sum(p for h,_,p in histories if [o for n,o in h if n=='Z'][-1]=='1')
 assert observed==expected
p=F(16,25);assert 2*p*(1-p)==F(288,625)<F(1,2)
for k in range(101):
 p=F(k,100);assert 2*p*(1-p)==F(1,2)-2*(p-F(1,2))**2 <= F(1,2)
# Two intermediate angles: exact transitions 3/4 and 1/4, then final probabilities.
plus=F(3,4)**2+F(1,4)**2
assert plus==F(5,8) and plus*F(3,4)+(1-plus)*F(1,4)==F(9,16)
record('AP-15',dict(projector_forward=a,projector_reverse=b,selected_joint_probabilities=['1/4','1/2'],recorded_Z1={'XZ':'1/2','ZX':'0','ZZ':'0','ZXZ':'1/2'},rational_basis_target='288/625',single_basis_bound='1/2',two_intermediate_target='9/16'))

# AP16: every actual spin configuration; sampler laws checked individually.
open_counts=Counter();ring_counts=Counter();open_weights=Counter();ring_weights=Counter()
open_total=ring_total=F(0)
all_spins=list(product([-1,1],repeat=4))
for spins in all_spins:
 ao=sum(spins[i]==spins[i+1] for i in range(3))
 ar=sum(spins[i]==spins[(i+1)%4] for i in range(4))
 open_counts[ao]+=1;ring_counts[ar]+=1;open_weights[ao]+=2**ao;ring_weights[ar]+=2**ar
 po=F(1,2)*F(2,3)**ao*F(1,3)**(3-ao)
 assert po==F(2**ao,54);open_total+=po
 pr=F(1,2)*F(2,3)**ar*F(1,3)**(4-ar)
 assert pr/F(41,81)==F(2**ar,82);ring_total+=pr
 # Encoding/decoding all finite records, with closure condition.
 bonds=[spins[i]==spins[i+1] for i in range(3)]
 decoded=[spins[0]]
 for agree in bonds:decoded.append(decoded[-1] if agree else -decoded[-1])
 assert tuple(decoded)==spins and (4-ar)%2==0
assert [open_counts[i] for i in range(4)]==[2,6,6,2]
assert [ring_counts[i] for i in range(5)]==[2,0,12,0,2]
assert open_total==1 and ring_total==F(41,81)
assert sum(open_weights.values())==54 and sum(ring_weights.values())==82
# Exact general partition sums for n>=3, including b<1 (abstract antialignment weights).
for n in range(3,9):
 for b in [F(1,2),F(1),F(2),F(3)]:
  zo=zr=F(0)
  for spins in product([-1,1],repeat=n):
   ao=sum(spins[i]==spins[i+1] for i in range(n-1));ar=sum(spins[i]==spins[(i+1)%n] for i in range(n))
   zo+=b**ao;zr+=b**ar
  assert zo==2*(1+b)**(n-1)
  assert zr==(b+1)**n+(b-1)**n
record('AP-16',dict(configurations=16,open_counts=dict(open_counts),ring_counts=dict(ring_counts),open_weight=54,ring_weight=82,open_alignment='8/27',ring_alignment='16/41',rejection_acceptance='41/81',general_formula_enumerations=24))

# AP17: exact boost, interval invariance and event differences.
boost=[[F(5,4),F(-3,4)],[F(-3,4),F(5,4)]]
eta=[[F(1),F(0)],[F(0),F(-1)]]
assert mm(mm(boost,eta),boost)==eta # symmetric boost: B^T eta B
O=[F(0),F(0)];T=[F(5),F(3)];R=[F(10),F(0)]
Op,Tp,Rp=[mv(boost,event) for event in [O,T,R]]
assert Op==[0,0] and Tp==[4,0] and Rp==[F(25,2),F(-15,2)]
def interval(a,b):return (b[0]-a[0])**2-(b[1]-a[1])**2
assert interval(O,R)==interval(Op,Rp)==100
assert interval(O,T)==interval(T,R)==interval(Op,Tp)==interval(Tp,Rp)==16
assert F(Rp[1]-Tp[1],Rp[0]-Tp[0])==F(-15,17)
assert interval(O,[5,4])==9 and interval([5,4],R)==9
# The legal turn condition is independently checked against both speeds.
legal=invalid=0
for ti in range(1,40):
 t=F(ti,4)
 for di in range(-20,21):
  d=F(di,4)
  condition=abs(d)<min(t,10-t)
  direct=0<t<10 and abs(d/t)<1 and abs(d/(10-t))<1
  assert condition==direct
  if direct:legal+=1
  else:invalid+=1
record('AP-17',dict(primed_events={'O':Op,'T':Tp,'R':Rp},proper_time_A=10,proper_time_B=8,desired_six_turn_positions=[-4,4],return_primed_velocity='−15/17',exact_boost_metric_identity=True,turn_grid_legal=legal,turn_grid_invalid=invalid,extension_legal_time_interval='(3,7)',extension_maximum=8,extension_unattained_infimum='sqrt(40)'))

# AP18: exact inverse and interval endpoints, including equality threshold.
assert [v*v*r for r,v in [(1,6),(4,3),(9,2)]]==[36]*3
assert 4*4*4==64 and F(3,2)**2*16==36
bounds=[]
for r,lo,hi in [(4,F(29,10),F(31,10)),(9,F(19,10),F(21,10))]:bounds.append((r*lo*lo,r*hi*hi))
assert bounds==[(F(841,25),F(961,25)),(F(3249,100),F(3969,100))]
intersection=(max(x[0] for x in bounds),min(x[1] for x in bounds))
assert intersection==bounds[0]
for eps in [F(0),F(1,10),F(1,4),F(1,2)]:assert (F(3,2)+eps<2-eps)==(eps<F(1,4))
assert F(3,2)+F(1,4)==2-F(1,4)==F(7,4)
for m,q in [(36,F(1)),(144,F(1,2)),(64,F(3,4))]:assert q*q*m==36
# Period coefficient T=(4/3)*pi, so v=(2*r)/(4/3), exactly.
r=F(4);t_over_pi=F(4,3);v=2*r/t_over_pi
assert v==6 and v*v*r==144 and F(3)/v==F(1,2)
record('AP-18',dict(common_mass=36,incompatible_mass=64,predicted_speed='3/2',individual_mass_intervals=bounds,intersection=intersection,error_threshold='1/4 (strict)',ambiguous_reading_at_threshold='7/4',projection_examples=[[36,1],[144,'1/2'],[64,'3/4']],period_decoded={'v':6,'M':144,'q':'1/2'}))

# Direct printed-key anchors guard against later copyediting damaging constants.
joined=lambda fid:' '.join(p['solution'] for pg in FAMS[fid]['pages'] for p in pg['prompts'])
for fid,anchors in {
 'AP-12':['35/12','25√2/12','1/(12√2)'],
 'AP-13':['37/5','3/5','4/5','J−I−1'],
 'AP-14':['21/4','27/4','1/400'],
 'AP-15':['288/625','1/4','1/2'],
 'AP-16':['54','82','41/81','16/41'],
 'AP-17':['25/2','−15/2','−15/17'],
 'AP-18':['33.64','38.44','1/4','144']}.items():
 for anchor in anchors: assert anchor in joined(fid),(fid,anchor)

def serialize(obj):
 if isinstance(obj,F):return str(obj)
 raise TypeError(type(obj).__name__)
(HERE/'ap2-checks-results.json').write_text(json.dumps(RESULT,ensure_ascii=False,indent=2,default=serialize)+'\n')
print('AP2 PASS: 8 families, 48 prompts, 8 extensions; exact instances, identities and exhaustive finite samplers checked.')
