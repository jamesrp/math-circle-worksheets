#!/usr/bin/env python3
"""Exact finite audits of GA3. General theorems are proved in the written keys."""
from fractions import Fraction as R
from itertools import product, combinations
from math import gcd, isclose, sqrt
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
DATA=HERE/'ga3-data.json'
d=json.loads(DATA.read_text()); families={f['id']:f for f in d['families']}
assert set(families)=={'GA-18','GA-19','GA-20','GA-21','GA-22','GA-23','GA-24','GA-27'}
for f in families.values():
 for key in ['title','core_gate','index_gate','extension_gate','reading','materials','timing','launch','satisfying_stop','prior_use','assessment','mathematical_connection']:assert f[key]
 assert all(all(s[k] for k in ['title','url','locator','adaptation','checked']) for s in f['sources'])
 qs=[q for p in f['pages'] for q in p['prompts']]
 assert len({q['id'] for q in qs})==len(qs)
 assert all(q['text'] and q['solution'] and q['hints'] for q in qs)
 assert all(e['prompt'] and e['solution'] and e['gate'] for e in f['extensions'])

def add(a,b):
 c=a.copy()
 for k,v in b.items():c[k]=c.get(k,R(0))+v
 return {k:v for k,v in c.items() if v}
def scale(a,c):return {k:v*c for k,v in a.items() if v*c}
def mul(a,b):
 c={}
 for i,x in a.items():
  for j,y in b.items():
   k=tuple(u+v for u,v in zip(i,j));c[k]=c.get(k,R(0))+x*y
 return {k:v for k,v in c.items() if v}
def deriv(a,axis):
 c={}
 for k,v in a.items():
  if k[axis]:
   j=list(k);j[axis]-=1;c[tuple(j)]=v*k[axis]
 return c
def integ_t(a,T):
 c={}
 for (t,z),v in a.items():c[z]=c.get(z,R(0))+v*R(T)**(t+1)/(t+1)
 return {k:v for k,v in c.items() if v}

# GA18: formal expansion in c and p, plus exact piecewise-loss classifications.
c={(1,0):R(1)};p={(0,1):R(1)};one={(0,0):R(1)}
Q=add(mul(p,mul(c,c)),mul(add(one,scale(p,-1)),mul(add(scale(one,6),scale(c,-1)),add(scale(one,6),scale(c,-1)))))
mu=scale(add(one,scale(p,-1)),6)
rhs=add(mul(add(c,scale(mu,-1)),add(c,scale(mu,-1))),scale(mul(p,add(one,scale(p,-1))),36))
assert Q==rhs
loss_cases=0
for p0 in [R(i,20) for i in range(1,20)]:
 m=6*(1-p0)
 for c0 in [R(i,4) for i in range(-16,41)]:
  cost=p0*c0*c0+(1-p0)*(6-c0)**2
  assert cost==(c0-m)**2+36*p0*(1-p0)
  A=p0*abs(c0)+(1-p0)*abs(6-c0)
  Amin=6*min(p0,1-p0)
  expected=(c0==0 if p0>R(1,2) else c0==6 if p0<R(1,2) else 0<=c0<=6)
  assert A>=Amin and (A==Amin)==expected
  W=max(abs(c0),abs(6-c0));assert W>=3 and (W==3)==(c0==3)
  loss_cases+=1
for heights in product(range(-2,3),repeat=3):
 w=[R(1,6),R(1,3),R(1,2)];m=sum(x*y for x,y in zip(w,heights))
 assert sum(x*(y-m) for x,y in zip(w,heights))==0
 for cand in [R(-3),R(0),R(7,2)]:
  assert sum(x*(y-cand)**2 for x,y in zip(w,heights))==sum(x*(y-m)**2 for x,y in zip(w,heights))+(cand-m)**2

# GA19: derivatives are formal coefficient identities; sup extrema are at 1 for these powers.
derivative_cases=0
for n in range(1,101):
 assert deriv({(n,0):R(1,n)},0)=={(n-1,0):R(1)}
 assert R(1)/R(1,n)==n
 assert R(1)/(R(1,n)+1)==R(n,n+1)<1
 derivative_cases+=1
for eps in [R(1,1000),R(1,7),R(2)]:
 for M in [R(1,9),R(7),R(100)]:
  ratio=M/eps;n=max(1,(ratio.numerator+ratio.denominator-1)//ratio.denominator)
  assert eps*n>=M and n>=1
assert R(1,1000)*7000==7
for C in [R(0),R(1,3),R(1),R(1000),R(100001,3)]:
 n=C.numerator//C.denominator+1;assert n>C and 1>C*R(1,n)
for eps,h in product([R(1,1000),R(1,2),R(3)],[R(1,100),R(1,3),R(1)]):
 vals=[abs(e1-e0)/h for e0,e1 in product([-eps,eps],repeat=2)]
 assert max(vals)==2*eps/h

# GA20: symbolic effort integral and exact finite schedules, including backward speeds.
t={(1,0):R(1)};a={(0,1):R(1)};one={(0,0):R(1)}
y=add(scale(t,2),mul(a,mul(t,add(scale(one,3),scale(t,-1)))))
yp=deriv(y,0);assert integ_t(mul(yp,yp),3)=={0:R(12),2:R(9)}
schedule_cases=0
for durations in [(R(1),R(2)),(R(1,2),R(1),R(3,2)),(R(1,3),R(2,3),R(2))]:
 for initial in product(range(-3,5),repeat=len(durations)-1):
  last=(6-sum(dt*v for dt,v in zip(durations,initial)))/durations[-1]
  vs=initial+(last,);E=sum(dt*v*v for dt,v in zip(durations,vs))
  excess=sum(dt*(v-2)**2 for dt,v in zip(durations,vs))
  assert E==12+excess and E>=12 and (E==12)==all(v==2 for v in vs)
  schedule_cases+=1
assert 4**2+2*1**2==18
for a0 in [R(i,12) for i in range(-18,19)]:
 assert (min(2+3*a0,2-3*a0)>=0)==(abs(a0)<=R(2,3))

# GA21: exact reflection crossings and clamp cases; numerical distance checks supplement proof.
mirror_cases=0
for aa,bb,h,k in product([-2,0,3],[-1,2,6],[1,3],[1,2]):
 aa,bb,h,k=map(R,(aa,bb,h,k));mstar=(k*aa+h*bb)/(h+k)
 s=h/(h+k)
 assert aa+s*(bb-aa)==mstar and h+s*(-k-h)==0
 for lo,hi in [(-3,2),(-1,4),(5,7)]:
  opt=max(R(lo),min(R(hi),mstar))
  cost=lambda m:sqrt(float((m-aa)**2+h*h))+sqrt(float((m-bb)**2+k*k))
  for j in range(25):
   m=R(lo)+(R(hi)-lo)*R(j,24)
   assert cost(m)>=cost(opt)-1e-12
  # Nonparallel displacement determinant is h*(n-m), proving strictness when m!=n.
  m,n=R(lo),R(hi);assert (m-aa)*(-h)-(-h)*(n-aa)==h*(n-m)!=0
  mirror_cases+=1
assert (R(1)*(-2)+R(3)*6)/(3+1)==4
assert isclose(sqrt(45)+sqrt(5),4*sqrt(5))
assert isclose(sqrt(25)+sqrt(17),5+sqrt(17))
assert R(13)>9 # F(1)^2=44+12sqrt(13)>80=F(4)^2.

# GA22: exact convex hull and affine dependence independently certify grid arrangements.
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def onseg(p,a,b):return cross(a,b,p)==0 and all(min(a[i],b[i])<=p[i]<=max(a[i],b[i]) for i in [0,1])
def hull(ps):
 ps=sorted(set(ps))
 if len(ps)<=1:return ps
 def half(seq):
  h=[]
  for x in seq:
   while len(h)>1 and cross(h[-2],h[-1],x)<=0:h.pop()
   h.append(x)
  return h
 return half(ps)[:-1]+half(ps[::-1])[:-1]
def inside(p,H):
 if len(H)==1:return p==H[0]
 if len(H)==2:return onseg(p,*H)
 return all(cross(H[i],H[(i+1)%len(H)],p)>=0 for i in range(len(H)))
def intersects(A,B):
 if any(inside(p,B) for p in A) or any(inside(p,A) for p in B):return True
 for i in range(len(A)):
  a,b=A[i],A[(i+1)%len(A)]
  for j in range(len(B)):
   c,d=B[j],B[(j+1)%len(B)]
   if cross(a,b,c)*cross(a,b,d)<0 and cross(c,d,a)*cross(c,d,b)<0:return True
 return False
def nullvector(points):
 rows=[list(map(R,c)) for c in zip(*points)]+[[R(1)]*len(points)]
 pivots=[];r=0
 for col in range(len(points)):
  k=next((k for k in range(r,len(rows)) if rows[k][col]),None)
  if k is None:continue
  rows[r],rows[k]=rows[k],rows[r];factor=rows[r][col];rows[r]=[x/factor for x in rows[r]]
  for k in range(len(rows)):
   if k!=r:
    factor=rows[k][col];rows[k]=[x-factor*y for x,y in zip(rows[k],rows[r])]
  pivots.append(col);r+=1
  if r==len(rows):break
 free=next(k for k in range(len(points)) if k not in pivots)
 v=[R(0)]*len(points);v[free]=1
 for row,col in zip(rows,pivots):v[col]=-row[free]
 assert sum(v)==0 and any(x>0 for x in v) and any(x<0 for x in v)
 assert all(sum(v[i]*points[i][j] for i in range(len(points)))==0 for j in range(len(points[0])))
 return v
radon_cases=0
for pts in combinations(list(product(range(4),repeat=2)),4):
 assert any(intersects(hull([pts[i] for i in range(4) if mask>>i&1]),hull([pts[i] for i in range(4) if not mask>>i&1])) for mask in range(1,15) if mask&1)
 v=nullvector(pts);S=sum(x for x in v if x>0)
 left=tuple(sum(v[i]*pts[i][j]/S for i in range(4) if v[i]>0) for j in [0,1])
 assert inside(left,hull([pts[i] for i in range(4) if v[i]>0]))
 assert inside(left,hull([pts[i] for i in range(4) if v[i]<0]))
 radon_cases+=1
for d0 in range(1,5):
 for seed in range(30):nullvector([tuple((seed*(i+1)+j*j+2*i*j)%7 for j in range(d0)) for i in range(d0+2)])
A,B,C,D=(0,0),(6,0),(5,4),(0,3)
assert tuple(R(7,13)*A[i]+R(6,13)*C[i] for i in [0,1])==tuple(R(5,13)*B[i]+R(8,13)*D[i] for i in [0,1])==(R(30,13),R(24,13))
assert tuple(R(1,2)*A[i]+R(1,3)*B[i]+R(1,6)*(0,6)[i] for i in [0,1])==(2,1)
tri=[(0,0),(2,0),(0,2)];assert not any(inside(tri[i],hull([tri[j] for j in range(3) if i!=j])) for i in range(3))

# GA23: exact rational points on the unit circle check every frame map algebraically.
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def va(a,b):return tuple(x+y for x,y in zip(a,b))
def vs(c,a):return tuple(c*x for x in a)
ex,ey,ez=(R(1),R(0),R(0)),(R(0),R(1),R(0)),(R(0),R(0),R(1))
def leg(v,T0,T1,N):return va(vs(dot(v,T0),T1),vs(dot(v,N),N))
transport_cases=0
for rat in [R(i,j) for i in range(1,8) for j in range(1,8)]:
 c,s=(1-rat*rat)/(1+rat*rat),2*rat/(1+rat*rat)
 assert c*c+s*s==1 and s>0
 B=(c,s,R(0));u=(-s,c,R(0));N=(s,-c,R(0))
 frames=[(ey,u,ez),(ez,vs(-1,B),N),(ex,vs(-1,ez),ey)]
 for T0,T1,n in frames:assert dot(T0,n)==dot(T1,n)==0 and dot(T0,T0)==dot(T1,T1)==dot(n,n)==1
 for a0,b0 in product(range(-2,3),repeat=2):
  v=va(vs(a0,ey),vs(b0,ez));start=v
  for frame in frames:v=leg(v,*frame)
  assert v==(0,a0*c-b0*s,a0*s+b0*c) and dot(v,v)==dot(start,start)
  for T0,T1,N0 in frames[::-1]:v=leg(v,vs(-1,T1),vs(-1,T0),vs(-1,N0))
  assert v==start
  transport_cases+=1
for frame,expected in zip(families['GA-23']['figures']['octant_frames'],[(ey,vs(-1,ex),ez),(ez,vs(-1,ey),ex),(ex,vs(-1,ez),ey)]):assert tuple(map(tuple,[frame['T0'],frame['T1'],frame['N']]))==expected
for q0 in range(2,21):
 for p0 in range(1,q0):
  if gcd(p0,q0)==1:assert next(k for k in range(1,q0+1) if (R(p0,q0)*k).denominator==1)==q0

# GA24: geometric graph punctures retain edge interiors by subdivision, never delete whole edges.
def component_count(nodes,edges,deleted=()):
 nodes=set(nodes)-set(deleted);count=0
 while nodes:
  count+=1;todo=[nodes.pop()]
  while todo:
   v=todo.pop()
   for a,b in edges:
    w=b if a==v else a if b==v else None
    if w in nodes:nodes.remove(w);todo.append(w)
 return count
def subdivide(edges):
 nodes=set();out=[];mids=[]
 for i,(a,b) in enumerate(edges):
  u,v=('e',i,0),('e',i,1);nodes.update([a,b,u,v]);out.extend([(a,u),(u,v),(v,b)]);mids.append(u)
 return nodes,out,mids
models={'circle':[(0,1),(1,2),(2,0)],'interval':[(0,1)],'Y':[(0,1),(0,2),(0,3)],'eight':[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)],'two':[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3)]}
puncture_counts={}
for name,E in models.items():
 nodes,edges,mids=subdivide(E)
 puncture_counts[name]=sorted({component_count(nodes,edges,[p]) for p in nodes})
assert puncture_counts=={'circle':[1],'interval':[1,2],'Y':[1,2,3],'eight':[1,2],'two':[2]}
nodes,edges,_=subdivide(models['circle'])
assert all(component_count(nodes,edges,pair)==2 for pair in combinations([0,1,2],2))
# Constructive disk detours: nine parabola candidates exceed eight possible line intersections.
disk_points=[(R(0),R(0)),(R(1),R(0)),(R(0),R(1)),(R(-1),R(0)),(R(0),R(-1)),(R(1,2),R(1,2))]
detours=0
for deleted in combinations(disk_points,2):
 for p0,q0 in combinations([x for x in disk_points if x not in deleted],2):
  candidates=[(R(i,20),R(i,20)**2) for i in range(-4,5)]
  z=next(z for z in candidates if z not in deleted and all(cross(p0,e,z)!=0 and cross(q0,e,z)!=0 for e in deleted))
  assert dot(z,z)<1 and all(not onseg(e,p0,z) and not onseg(e,z,q0) for e in deleted)
  detours+=1

# GA27: exact path certificates inside the actual clipped square, plus polynomial derivatives.
def f(x,y):return x*x-y*y
flood_cases=0
coords=[R(i,8) for i in range(-8,9)]
for c0 in [R(-3,2),R(-1),R(-3,4),R(-1,4),R(0),R(1,4),R(1),R(3,2)]:
 for x,y in product(coords,repeat=2):
  if f(x,y)>c0:continue
  if c0<0:
   assert y!=0;sign=1 if y>0 else -1
   assert x*x<=1+c0
   for r in [R(i,8) for i in range(9)]:
    assert f(x,(1-r)*y+r*sign)<=c0
    assert f((1-r)*x,sign)<=c0
  else:
   for r in [R(i,8) for i in range(9)]:assert f(r*x,r*y)==r*r*f(x,y)<=c0
  flood_cases+=1
for a0 in coords:
 for r in [R(i,8) for i in range(9)]:
  assert f(r*a0,1)<=a0*a0 and f(a0,1-2*r)<=a0*a0 and f((1-r)*a0,-1)<=a0*a0
 assert f(a0,0)==a0*a0
fpoly={(2,0):R(1),(0,2):R(-1)};gpoly={(4,0):R(1),(0,4):R(-1)}
assert deriv(fpoly,0)=={(1,0):R(2)} and deriv(fpoly,1)=={(0,1):R(-2)}
assert deriv(deriv(fpoly,0),0)=={(0,0):R(2)} and deriv(deriv(fpoly,1),1)=={(0,0):R(-2)}
assert deriv(deriv(gpoly,0),0)=={(2,0):R(12)} and deriv(deriv(gpoly,1),1)=={(0,2):R(-12)}
for x,y in product(coords,repeat=2):assert (f(x,y)<=0)==(x**4-y**4<=0)
Fpoly={(4,0):R(1),(2,0):R(-2),(0,0):R(1),(0,2):R(1)}
assert deriv(Fpoly,0)=={(3,0):R(4),(1,0):R(-4)} and deriv(Fpoly,1)=={(0,1):R(2)}
for x in [-1,0,1]:assert 4*x*(x*x-1)==0
assert [12*x*x-4 for x in [-1,0,1]]==[8,-4,8]
# Printed/exact figure regressions prevent drift from the checked instances.
assert families['GA-18']['figures']['landscape']['breakpoint']=='2/3'
assert families['GA-21']['figures']['guide_only']['unconstrained_M']==[4,0]
assert '5+√17' in families['GA-21']['pages'][2]['prompts'][0]['solution']
assert families['GA-22']['figures']['guide_only']['crossing']==['30/13','24/13']
assert '7000' in families['GA-19']['pages'][0]['prompts'][0]['solution']
assert '12+9a²' in families['GA-20']['pages'][2]['prompts'][1]['solution']
assert '−1≤c<0' in families['GA-27']['pages'][1]['prompts'][0]['solution']
result={'batch':'ga3','status':'passed','data_sha256':hashlib.sha256(DATA.read_bytes()).hexdigest(),'coverage':{'families':8,'student_pages':sum(len(f['pages']) for f in families.values()),'keyed_prompts':sum(len(p['prompts']) for f in families.values() for p in f['pages']),'solved_extensions':sum(len(f['extensions']) for f in families.values())},'mathematics':{
 'GA-18':{'formal_two_variable_square_identity':True,'loss_cases':loss_cases,'weighted_residual_arrays':125,'scope':'Exact finite audits support the complete piecewise and square arguments in the key for all real constants/positive widths.'},
 'GA-19':{'formal_power_derivatives':derivative_cases,'arbitrary_threshold_rule_checked':True,'noise_corner_bounds_checked':9,'scope':'The key selects n for every C or epsilon/M; finite choices check indexing, not the universal quantifier. Integration and strict norm-ratio proofs are written.'},
 'GA-20':{'formal_effort_integral':'12+9a²','finite_schedules':schedule_cases,'scope':'Exact schedules and symbolic integration supplement the FTC and continuous-piece equality proof for every admissible path.'},
 'GA-21':{'exact_crossing_and_clamp_instances':mirror_cases,'scope':'Crossings and determinant strictness are exact. Floating distance grids are only a supplementary numerical check; reflection/equality and strict convexity prove the optimum.'},
 'GA-22':{'distinct_grid_arrangements':radon_cases,'higher_dimensional_affine_relations':120,'exact_two_board_certificates':True,'scope':'Every finite board is independently checked by hull intersection and affine dependence. General planar hull alternatives and linear-dependence fact are explicitly supplied in the tasks.'},
 'GA-23':{'exact_rational_frame_roundtrips':transport_cases,'octant_figure_frames':True,'scope':'Rational frame samples verify signs and inverse operations. The written symbolic calculation proves all alpha and all initial vectors; angle-area equality is limited to the selected family.'},
 'GA-24':{'geometric_puncture_counts':puncture_counts,'exact_disk_detours':detours,'scope':'Subdivided geometric edges retain interiors when punctures are removed. Finite models support the topological proofs, not a general classification; the disk proof uses an explicit planar path construction.'},
 'GA-27':{'exact_wet_point_path_certificates':flood_cases,'forced_crossings':len(coords),'formal_gradient_Hessian_checks':True,'scope':'Finite point/path checks support direct all-point inequalities and scaling certificates. No smooth-boundary theorem is applied to the clipped square.'}
}}
(HERE/'ga3-checks-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('GA3 checks passed:',result['coverage'])
