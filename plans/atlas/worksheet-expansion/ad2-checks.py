"""Exact finite certificates for AD09–16. General proofs remain in the keyed text."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from math import gcd,lcm,isqrt
from pathlib import Path
import json
D=Path(__file__).resolve().parent
DATA=json.loads((D/'ad2-data.json').read_text())
F={f['id']:f for f in DATA['families']}
R={}
assert set(F)=={f'AD-{i:02d}' for i in range(9,17)}
for f in F.values():
 assert len({p['id'] for pg in f['pages'] for p in pg['prompts']})==sum(len(pg['prompts']) for pg in f['pages'])
 for pg in f['pages']:
  assert pg['intro'] and pg['gate']
  for p in pg['prompts']:assert p['text'] and p['solution'] and p['hints']
 for e in f['extensions']:assert all(e[k] for k in ['gate','prompt','solution'])
# CRT: exhaustive independently enumerated report maps and constructive extended Euclid.
def egcd(a,b):
 if not b:return a,1,0
 d,u,v=egcd(b,a%b);return d,v,u-(a//b)*v
systems=0
for m,n in product(range(1,17),repeat=2):
 d=gcd(m,n);period=lcm(m,n)
 reports={(t%m,t%n):t for t in range(period)}
 assert len(reports)==period
 for a,b in product(range(m),range(n)):
  possible=(b-a)%d==0
  assert ((a,b) in reports)==possible
  if possible:
   _,u,v=egcd(m//d,n//d)
   constructed=(a+m*u*((b-a)//d))%period
   assert constructed==reports[(a,b)]
  systems+=1
repairs={}
for a,b in [(1,5),(3,5),(2,4),(2,0)]:
 ts=[t for t in range(12) if (t%4,t%6)==(a,b)];assert len(ts)==1;repairs[f'{a},{b}']=ts[0]
assert list(repairs.values())==[5,11,10,6]
assert [t for t in range(60) if (t%4,t%6,t%5)==(3,5,2)]==[47]
R['AD-09']={'all_residue_pairs_checked_moduli_1_to_16':systems,'four_six_reports':[[t,t%4,t%6] for t in range(12)],'notice_repairs_first_times':repairs,'eight_twelve_example':21,'three_clock_first_time':47}
# Pell: independent isqrt scan, norm-preserving matrices, inverse/descent and threshold.
fig=F['AD-10']['figures'];U=fig['forward_matrix'];V=fig['inverse_matrix']
def apply(M,p):return tuple(sum(a*b for a,b in zip(row,p)) for row in M)
assert [[sum(U[i][k]*V[k][j] for k in range(2)) for j in range(2)] for i in range(2)]==[[1,0],[0,1]]
# Equality of norm polynomials: x²,xy,y² coefficients.
a,b=U[0];c,d=U[1];assert (a*a-2*c*c,2*a*b-4*c*d,b*b-2*d*d)==(1,0,-2)
solutions=[]
for m in range(1,100001):
 total=m*(m+1)//2;n=isqrt(total)
 if n*n==total:solutions.append((m,n,total))
generated=[];x,y=3,2
while (x-1)//2<=100000:
 assert x*x-2*y*y==1 and x%2==1 and y%2==0
 generated.append(((x-1)//2,y//2,(y//2)**2));x,y=apply(U,(x,y))
assert generated==solutions
for m,n,total in solutions:
 x,y=2*m+1,2*n
 if y==2:assert apply(V,(x,y))==(1,0)
 else:
  xx,yy=apply(V,(x,y));assert xx>0 and 0<yy<y and xx*xx-2*yy*yy==1
  assert apply(U,(xx,yy))==(x,y)
threshold=fig['threshold'];first=next(s for s in solutions if s[2]>threshold)
assert first==(1681,1189,1413721)
assert solutions[solutions.index(first)+1]==(9800,6930,48024900)
ns=[0]+[s[2] for s in solutions]
assert all(ns[k+2]==34*ns[k+1]-ns[k]+2 for k in range(len(ns)-2))
R['AD-10']={'independent_row_scan_through':100000,'complete_scanned_matches':solutions,'first_above_threshold':first,'descent_scope':'All scanned solutions verified; the written inequalities and positive-integer descent prove every positive solution.'}
# Two polynomial quotient rings on coefficient bit pairs.
def add(a,b):return a^b
# bit0 ordinary; bit1 coefficient of t; t²=t+constant.
def mul(a,b,constant=1):
 a0,a1=a&1,a>>1;b0,b1=b&1,b>>1
 return ((a0*b0+constant*a1*b1)%2) | (((a0*b1+a1*b0+a1*b1)%2)<<1)
ringtables={}
for constant in [0,1]:
 table=[[mul(a,b,constant) for b in range(4)] for a in range(4)]
 for a,b,c in product(range(4),repeat=3):
  assert mul(mul(a,b,constant),c,constant)==mul(a,mul(b,c,constant),constant)
  assert mul(a,add(b,c),constant)==add(mul(a,b,constant),mul(a,c,constant))
 inv={a:[b for b in range(4) if mul(a,b,constant)==1] for a in range(4)}
 assert inv==({0:[],1:[1],2:[],3:[]} if constant==0 else {0:[],1:[1],2:[3],3:[2]})
 ringtables['A' if constant==0 else 'B']={'products':table,'inverses':inv}
def affine(a,b,z,c=1):return add(mul(a,z,c),b)
for r,s,h,k in product(range(4),repeat=4):
 if r==s:continue
 fits=[(a,b) for a,b in product(range(4),repeat=2) if affine(a,b,r)==h and affine(a,b,s)==k]
 assert len(fits)==1
assert [(a,b) for a,b in product(range(4),repeat=2) if affine(a,b,1)==2 and affine(a,b,2)==0]==[(3,1)]
assert affine(3,1,3)==3
assert not [(a,b) for a,b in product(range(4),repeat=2) if affine(a,b,1,0)==2 and affine(a,b,2,0)==0]
assert [mul(z,z) for z in range(4)]==[0,1,3,2]
R['AD-11']={'label_order':['0','1','t','u'],'tables':ringtables,'two_report_cases_checked':12*16,'decode_a_b':[3,1],'prediction_at_u':3,'frobenius':[0,1,3,2]}
# Constructibility: check chosen cubes and rational-root classifications for finite N.
assert 1442**3==2998442888 and 1443**3==3004685307
assert 1442**3<3*1000**3<1443**3
classified={}
for N in range(1,513):
 roots=[k for k in range(1,9) if k**3==N]
 candidates=[k for k in range(1,N+1) if N%k==0 and k**3==N]
 assert roots==candidates
 classified[N]=bool(roots)
assert [N for N in classified if classified[N]]==[1,8,27,64,125,216,343,512]
assert all(k**3-3!=0 for k in [-3,-1,1,3])
assert all(k**3-3*k-1!=0 for k in [-1,1])
R['AD-12']={'rational_bracket_cube_numerators':[1442**3,1443**3],'common_denominator':10**9,'integer_volume_scan_1_to_512_constructible':[N for N in classified if classified[N]],'scope':'Only the finite arithmetic is checked here. Cubic irreducibility and the supplied degree theorem carry the general impossibility proof.'}
# Infinite staircase classification using exact axis bounds, not a truncated-grid guess.
def survivors(corners):
 xb=[a for a,b in corners if b==0];yb=[b for a,b in corners if a==0]
 if not xb or not yb:return None
 return {(i,j) for i in range(min(xb)) for j in range(min(yb)) if not any(i>=a and j>=b for a,b in corners)}
corners=[tuple(p) for p in F['AD-13']['figures']['corners']];S=survivors(corners)
assert S=={(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(2,0)}
move_results=[]
for k,(a,b) in enumerate(corners):
 for dx,dy in [(1,0),(0,1)]:
  new=corners.copy();new[k]=(a+dx,b+dy);T=survivors(new)
  move_results.append({'from':[a,b],'to':[a+dx,b+dy],'survivors':None if T is None else len(T),'added':None if T is None else sorted(T-S)})
assert [(r['from'],r['to']) for r in move_results if r['survivors']==10]==[([2,1],[3,1])]
assert [r['survivors'] for r in move_results]==[9,None,10,9,9,9,None,9]
def shift(p,d):
 t=(p[0]+d[0],p[1]+d[1]);return t if t in S else None
kx={p for p in S if shift(p,(1,0)) is None};ky={p for p in S if shift(p,(0,1)) is None}
assert kx&ky=={(0,3),(1,2),(2,0)} and len(kx)==4 and len(ky)==3
for d in [(1,0),(0,1)]:
 images=[shift(p,d) for p in S if shift(p,d) is not None];assert len(images)==len(set(images))
for r,s in product(range(1,8),repeat=2):
 T=survivors([(r,0),(0,s)]);assert len(T)==r*s
 common={p for p in T if (p[0]+1,p[1]) not in T and (p[0],p[1]+1) not in T};assert common=={(r-1,s-1)}
R['AD-13']={'survivors':sorted(S),'all_eight_moves':move_results,'common_annihilator_basis_exponents':sorted(kx&ky),'x_kernel_exponents':sorted(kx),'y_kernel_exponents':sorted(ky)}
# Dual arithmetic compared with independent derivative evaluation.
def dm(x,y):return (x[0]*y[0],x[0]*y[1]+x[1]*y[0])
def da(x,y):return (x[0]+y[0],x[1]+y[1])
def peval(c,x):
 out=Q(0)
 for a in reversed(c):out=out*x+a
 return out

def derivative(c):return [i*c[i] for i in range(1,len(c))]
def dualeval(c,a,b):
 out=(Q(0),Q(0))
 for z in reversed(c):out=da(dm(out,(a,b)),(z,0))
 return out
count=0
for coeff in product([-1,0,1],repeat=5):
 for a,b in product(map(Q,range(-2,3)),repeat=2):
  assert dualeval(coeff,a,b)==(peval(coeff,a),b*peval(derivative(coeff),a));count+=1
for a,b in product([Q(i,j) for i in range(-3,4) for j in range(1,4)],repeat=2):
 if a:assert dm((a,b),(1/a,-b/(a*a)))==(1,0)
f=[-2,1,-2,1]
assert dualeval(f,Q(3),Q(1))==(10,16) and dualeval(f,Q(3),Q(2))==(10,32)
assert dualeval([0,0,1],Q(2),Q(1))==dualeval([4,-4,2],Q(2),Q(1))==(4,4)
def jetmul(a,b):return tuple(sum(a[k]*b[j-k] for k in range(j+1)) for j in range(3))
assert jetmul(jetmul((2,1,3),(2,1,3)),(2,1,3))==(8,12,42)
R['AD-14']={'polynomial_seed_cases_checked':count,'program_at_3_seed1':[10,16],'program_at_3_seed2':[10,32],'inverse_of_3_minus_2epsilon':['1/3','2/9'],'second_order_cubic':[8,12,42]}
# Ellipse forward/inverse, exact rational-point enumeration and primitive conditions.
def point(t):return ((1-2*t*t)/(1+2*t*t),2*t/(1+2*t*t))
for p,q in product(range(-20,21),range(1,21)):
 t=Q(p,q);x,y=point(t);assert x*x+2*y*y==1 and x!=-1 and y/(x+1)==t
 A=q*q-2*p*p;B=2*p*q;C=q*q+2*p*p;assert A*A+2*B*B==C*C
 if gcd(p,q)==1:assert gcd(gcd(abs(A),abs(B)),C)==(1 if q%2 else 2)
rational_points=set()
for C in range(1,101):
 for A in range(-C,C+1):
  n=C*C-A*A
  if n%2:continue
  B=isqrt(n//2)
  if 2*B*B!=n:continue
  for s in [-1,1]:
   x,y=Q(A,C),Q(s*B,C);rational_points.add((x,y))
   if x!=-1:assert point(y/(x+1))==(x,y)
   else:assert y==0
assert point(Q(1))==(Q(-1,3),Q(2,3))
assert point(Q(2,3))==(Q(1,17),Q(12,17))
assert point(Q(3,2))==(Q(-7,11),Q(6,11))
R['AD-15']={'parameter_pairs_checked':41*20,'distinct_rational_points_with_common_denominator_up_to_100':len(rational_points),'selected_points':{'1':['-1/3','2/3'],'2/3':['1/17','12/17'],'3/2':['-7/11','6/11']},'primitive_rule':'gcd=1 for odd q; gcd=2 for even q, when gcd(p,q)=1'}
# F5 curve: exact projective enumeration, all point pairs/triples and cyclic labels.
p=5;a=b=1
curve=lambda a,b:{(x,y) for x,y in product(range(p),repeat=2) if (y*y-x*x*x-a*x-b)%p==0}
C=curve(a,b);expected={(0,1),(0,4),(2,1),(2,4),(3,1),(3,4),(4,2),(4,3)};assert C==expected
assert len(curve(1,0))==3 and len(curve(0,1))==5
assert (-16*(4*a**3+27*b*b))%p==4
proj=set()
for X,Y,Z in product(range(p),repeat=3):
 if (X,Y,Z)==(0,0,0) or (Y*Y*Z-X**3-X*Z*Z-Z**3)%p:continue
 pivot=next(v for v in (X,Y,Z) if v);inv=pow(pivot,-1,p);proj.add(tuple(v*inv%p for v in (X,Y,Z)))
assert len(proj)==9 and len([r for r in proj if r[2]==0])==1
O=None
pts=[O]+sorted(C)
def ecadd(P,Qp):
 if P is None:return Qp
 if Qp is None:return P
 x,y=P;xx,yy=Qp
 if x==xx and (y+yy)%p==0:return O
 if P==Qp:s=(3*x*x+a)*pow(2*y,-1,p)%p
 else:s=(yy-y)*pow((xx-x)%p,-1,p)%p
 z=(s*s-x-xx)%p;w=(s*(x-z)-y)%p;return z,w
for P,Qp,Rp in product(pts,repeat=3):
 assert ecadd(P,Qp) in pts
 assert ecadd(P,Qp)==ecadd(Qp,P)
 assert ecadd(ecadd(P,Qp),Rp)==ecadd(P,ecadd(Qp,Rp))
P=(0,1);orbit=[O]
for k in range(9):orbit.append(ecadd(orbit[-1],P))
assert orbit==[O,(0,1),(4,2),(2,1),(3,4),(3,1),(2,4),(4,3),(0,4),O]
assert len(set(orbit[:-1]))==9
for r,s in product(range(9),repeat=2):assert ecadd(orbit[r],orbit[s])==orbit[(r+s)%9]
solutions={'2Q=P':[orbit[k] for k in range(9) if 2*k%9==1],'3Q=P':[orbit[k] for k in range(9) if 3*k%9==1],'3Q=O':[orbit[k] for k in range(9) if 3*k%9==0],'3Q=(2,1)':[orbit[k] for k in range(9) if 3*k%9==3]}
assert solutions=={'2Q=P':[(3,1)],'3Q=P':[],'3Q=O':[O,(2,1),(2,4)],'3Q=(2,1)':[(0,1),(3,4),(4,3)]}
# All subsets: complete subgroup classification, not only possible orders.
subgroups=[]
for mask in range(1<<9):
 H={k for k in range(9) if mask>>k&1}
 if 0 in H and all((r+s)%9 in H for r,s in product(H,repeat=2)):subgroups.append(sorted(H))
assert subgroups==[[0],[0,3,6],list(range(9))]
R['AD-16']={'affine_points':sorted(C),'projective_point_count':len(proj),'discriminant_mod5':4,'generator_orbit_including_return':orbit,'point_pairs_checked':81,'associativity_triples_checked':729,'point_equations':solutions,'subgroup_labels':subgroups,'modified_affine_counts':{'a1_b0':3,'a0_b1':5}}
OUT={'status':'all exact checks passed','families':8,'student_pages':sum(len(f['pages']) for f in F.values()),'student_prompts':sum(len(pg['prompts']) for f in F.values() for pg in f['pages']),'guide_extensions':sum(len(f['extensions']) for f in F.values()),'checks':R,'scope':'Finite exhaustive checks verify the displayed instances and algebra identities. General CRT, descent, basis, derivative and parametrization conclusions also require the written arguments; constructibility and elliptic associativity use openly supplied theorems.'}
(D/'ad2-checks-results.json').write_text(json.dumps(OUT,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:OUT[k] for k in ['status','families','student_pages','student_prompts','guide_extensions']},indent=2))
