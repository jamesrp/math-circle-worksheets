"""Exact finite certificates supplement the general proofs in ad3-data.json."""
from fractions import Fraction as Q
from itertools import product,combinations
from collections import Counter,deque
from math import gcd,comb
from pathlib import Path
import json
P=Path(__file__).resolve().parent
out={}

def matmul(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def sub(A,B):return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]
def bracket(A,B):return sub(matmul(A,B),matmul(B,A))
def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def rank(A):
 A=[list(map(Q,row)) for row in A];r=0
 for c in range(len(A[0]) if A else 0):
  piv=next((i for i in range(r,len(A)) if A[i][c]),None)
  if piv is None:continue
  A[r],A[piv]=A[piv],A[r];v=A[r][c];A[r]=[z/v for z in A[r]]
  for i in range(len(A)):
   if i!=r:
    v=A[i][c];A[i]=[a-v*b for a,b in zip(A[i],A[r])]
  r+=1
  if r==len(A):break
 return r

def update(x,y,a,b):return ((1-a)*x+a*y,b*x+(1-b)*y)
# Independently iterate a grid of parameter and initial values, then compare the derived coordinates.
checks=0
for a,b in product([Q(i,8) for i in range(9)],repeat=2):
 for x0,y0 in [(-3,9),(4,-2),(0,0),(5,5),(-2,7)]:
  x,y=Q(x0),Q(y0);s=a+b
  for n in range(9):
   if s:
    L=(b*x0+a*y0)/s;d=Q(x0-y0)*(1-s)**n
    assert (x,y)==(L+a*d/s,L-b*d/s)
   else:assert (x,y)==(x0,y0)
   x,y=update(x,y,a,b);checks+=1
x,y=Q(-3),Q(9);errors=[]
for n in range(7):errors.append(max(abs(x-1),abs(y-1)));x,y=update(x,y,Q(1,4),Q(1,2))
assert next(i for i,e in enumerate(errors) if e<=Q(1,100))==5
for d in [Q(i,4) for i in range(-64,65)]:
 if not d:continue
 x,y=2+d/3,2-2*d/3;first=None
 for n in range(10):
  if max(abs(x-2),abs(y-2))<=Q(1,8):first=n;break
  x,y=update(x,y,Q(1,4),Q(1,2))
 assert (first==3)==(3<abs(d)<=12)
out['AD-17']={'exact_iterates':checks,'threshold_errors':list(map(str,errors)),'first_round':5,'design_difference_interval':'3<abs(d)<=12'}
# All small products, Gram identities, singular fibers and inverse formula.
matrices=[[[a,b],[c,d]] for a,b,c,d in product(range(-1,2),repeat=4)]
for A in matrices:
 a,b=A[0];c,d=A[1]
 assert det(A)**2==(a*a+c*c)*(b*b+d*d)-(a*b+c*d)**2
 for B in matrices:assert det(matmul(A,B))==det(A)*det(B)
for k in range(-10,11):
 A=[[2,k],[1,2]];assert det(A)==4-k
 if k!=4:
  inv=[[Q(2,4-k),Q(-k,4-k)],[Q(-1,4-k),Q(2,4-k)]]
  assert matmul(A,inv)==[[1,0],[0,1]]==matmul(inv,A)
 else:
  for s,t in product(range(-4,5),repeat=2):assert matmul(A,[[s-2*t],[t]])==[[2*s],[s]]
assert [k for k in range(-10,11) if abs(4-k)==1]==[3,5]
out['AD-18']={'matrix_product_pairs':len(matrices)**2,'gram_identities':len(matrices),'area_one_k':[3,5],'collapse_k':4}
# Explicit basis transformation and rank inventory; enumerate every binary 3x4 arrow.
T=[[1,1,0,0],[0,0,1,1],[1,1,1,1]]
U=[[1,0,-1,0],[0,0,1,0],[0,1,0,-1],[0,0,0,1]]
W=[[1,0,0],[0,1,0],[1,1,1]]
J=[[1,0,0,0],[0,1,0,0],[0,0,0,0]]
assert rank(U)==4 and rank(W)==3 and matmul(T,U)==matmul(W,J)
counts=Counter()
for bits in product(range(2),repeat=12):
 A=[list(bits[i:i+4]) for i in range(0,12,4)];r=rank(A);counts[r]+=1
 assert (4-r,r,3-r) in [(4,0,3),(3,1,2),(2,2,1),(1,3,0)]
S=[[1,1,0,0],[2,2,0,0],[0,0,0,0]];assert rank(S)==1
A=[[1],[0]];assert rank(matmul([[1,0]],A))==1 and rank(matmul([[0,1]],A))==0
out['AD-19']={'basis_certificate':'TU=WJ, both bases full rank','binary_3_by_4_maps':sum(counts.values()),'rational_rank_counts':dict(counts),'designed_map_rank':1}
# Centralizer brute force; noncommutative word expansion verifies a symbolic general identity.
N=[[1,1],[-1,-1]];C=[[1,0],[0,0]];Z=[[0,0],[0,0]]
assert matmul(N,N)==Z
cen=0
for a,b,c,d in product(range(-4,5),repeat=4):
 B=[[a,b],[c,d]];comm=bracket(N,B)==Z
 assert comm==(c==-b and d==a-2*b)
 if comm:cen+=1
 assert (comm and bracket(C,B)==Z)==(b==c==0 and a==d)
assert bracket(bracket(N,C),C)==[[0,1],[-1,0]] and bracket(N,bracket(C,C))==Z
words=Counter()
for a,b,c in [('A','B','D'),('B','D','A'),('D','A','B')]:
 for w,v in [(a+b+c,1),(b+a+c,-1),(c+a+b,-1),(c+b+a,1)]:words[w]+=v
assert all(v==0 for v in words.values())
for A,B,D in product(matrices[:10],repeat=3):
 vals=[bracket(bracket(A,B),D),bracket(bracket(B,D),A),bracket(bracket(D,A),B)]
 assert [[sum(M[i][j] for M in vals) for j in range(2)] for i in range(2)]==Z
 assert bracket(A,matmul(B,D))==[[x+y for x,y in zip(r,s)] for r,s in zip(matmul(bracket(A,B),D),matmul(B,bracket(A,D)))]
out['AD-20']={'candidate_partners':9**4,'centralizer_hits':cen,'jacobi_word_coefficients':dict(words),'exact_identity_triples':1000}
# Pullback inventory, recoloring optimization and every compatible two-token assignment.
people={'Aster':'red','Birch':'red','Cedar':'blue','Dahlia':'blue','Elm':'green'}
badges={'r':'red','s':'red','t':'blue','u':'green','v':'green','w':'gold'}
def catalog(B):return [(a,b) for a in people for b in B if people[a]==B[b]]
pairs=catalog(badges);assert len(pairs)==8
recolors={}
for color in ['red','blue','green']:
 B=dict(badges,w=color);recolors[color]=len(catalog(B))
assert recolors=={'red':10,'blue':10,'green':9}
for assignments in product(pairs,repeat=2):
 mediators=[h for h in product(pairs,repeat=2) if all(h[i][0]==assignments[i][0] and h[i][1]==assignments[i][1] for i in range(2))]
 assert mediators==[assignments]
duplicates=pairs+[('Aster','r')];assert sum(p==('Aster','r') for p in duplicates)==2
out['AD-21']={'catalog':pairs,'recolor_sizes':recolors,'two_token_assignments':len(pairs)**2,'duplicate_one_token_mediators':2}
# Entire cycle space independently found by parity, then every face-subset orbit by BFS.
vertices=list('ABCDO');edges=['AB','BC','CD','DA','OA','OB','OC','OD']
faces=[['AB','OA','OB'],['BC','OB','OC'],['CD','OC','OD'],['DA','OD','OA']]
fm=[sum(1<<edges.index(e) for e in f) for f in faces]
def closed(mask):return all(sum(bool(mask>>i&1) for i,e in enumerate(edges) if v in e)%2==0 for v in vertices)
cycles=[m for m in range(256) if closed(m)];assert len(cycles)==16
for bits in product(range(2),repeat=4):
 a,b,c,d=bits;marks=[a,b,c,d,a^d,a^b,b^c,c^d];m=sum(v<<i for i,v in enumerate(marks));assert m in cycles
 assert m==fm[0]*a^fm[1]*b^fm[2]*c^fm[3]*d
allclasses={}
for subset in range(16):
 allowed=[fm[i] for i in range(4) if subset>>i&1];remaining=set(cycles);classes=[]
 while remaining:
  seed=min(remaining);seen={seed};todo=deque([seed])
  while todo:
   cur=todo.popleft()
   for face in allowed:
    nxt=cur^face
    if nxt not in seen:seen.add(nxt);todo.append(nxt)
  assert seen<=remaining;remaining-=seen;classes.append(sorted(seen))
 assert len(classes)==2**(4-subset.bit_count())
 allclasses[subset]=classes
initial=allclasses[5];assert len(initial)==4
for cl in initial:assert len({((m>>1)&1,(m>>3)&1) for m in cl})==1
outer=15;second=(1<<0)|(1<<1)|(1<<4)|(1<<6)
buys={}
for target in [outer,second]:
 good=[]
 for sub in [0,2,8,10]:
  zero=next(c for c in allclasses[5|sub] if 0 in c)
  if target in zero:good.append(sub)
 minnum=min(s.bit_count() for s in good);buys[target]=[s for s in good if s.bit_count()==minnum]
assert buys=={outer:[10],second:[2]}
cap=fm[0]^fm[1]^fm[2]^fm[3]
relations=[]
for m in range(32):
 bd=0
 for i,f in enumerate(fm+[cap]):
  if m>>i&1:bd^=f
 if bd==0:relations.append(m)
assert relations==[0,31]
out['AD-22']={'cycles':len(cycles),'all_face_subsets':16,'initial_classes':initial,'minimum_purchase_masks':buys,'cap_kernel_masks':relations}
# Dimension classification supplies the theorem; these checks audit chosen complements and formal relations.
dims=list(product(range(6),repeat=2));checks=0
for a,b in dims:
 n=max(a,b);comp=(n-a,n-b);assert (a+comp[0],b+comp[1])==(n,n)
 for m in range(n):assert a>m or b>m
for p,q,a,b in product(dims[:12],repeat=4):
 diff=tuple(x-y for x,y in zip(p,q));same=diff==tuple(x-y for x,y in zip(a,b))
 assert same==(tuple(x+y for x,y in zip(p,b))==tuple(x+y for x,y in zip(a,q)))
 checks+=1
for g1,g2 in product(range(7),repeat=2):
 for a,b,c,d in product(range(-2,3),repeat=4):
  phi=lambda x,y:(x*g1+y*g2)%7
  assert phi(a+c,b+d)==(phi(a,b)+phi(c,d))%7
out['AD-23']={'complement_cases':len(dims),'formal_difference_equalities':checks,'finite_group_extensions':49,'P_minimum_free_rank':3,'P_complement':[0,2],'virtual_pair':[2,-2]}
# Exhaustive necklaces, fixed rotations, reflection orbits and general fixed-weight formula.
def rotate(x,j):return x[j:]+x[:j]
def strings(n,r):return [x for x in product(range(2),repeat=n) if sum(x)==r]
def orbits(n,r,reflect=False):
 rest=set(strings(n,r));ans=[]
 while rest:
  x=min(rest);orb={rotate(x,j) for j in range(n)}
  if reflect:orb|={rotate(x[::-1],j) for j in range(n)}
  ans.append(sorted(orb));rest-=orb
 return ans
six=orbits(6,3);assert sorted(map(len,six))==[2,6,6,6]
assert len(orbits(6,3,True))==3
certificates=[]
for n in range(1,11):
 for r in range(n+1):
  xs=strings(n,r);fixed=[]
  for j in range(n):
   brute=sum(rotate(x,j)==x for x in xs);g=gcd(n,j);L=n//g
   formula=comb(g,r//L) if r%L==0 else 0
   assert brute==formula;fixed.append(brute)
  assert sum(fixed)==n*len(orbits(n,r))
  if gcd(n,r)==1:assert all(len(o)==n for o in orbits(n,r))
  if (n,r) in [(6,3),(8,4),(7,3)]:certificates.append({'n':n,'red':r,'fixed':fixed,'orbits':len(orbits(n,r))})
out['AD-24']={'six_representatives':[''.join(map(str,o[0])) for o in six],'six_orbit_sizes':[len(o) for o in six],'reflection_count':3,'tested_n_through':10,'certificates':certificates}
out['status']='all exact checks passed'
(P/'ad3-checks-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'families':8,'student_pages':24,'student_prompts':48,'guide_extensions':8},indent=2))
