"""Independent AP3 review certificates; finite audits do not replace the written review proofs."""
from fractions import Fraction as F
from itertools import product, combinations
from collections import deque, Counter
from math import comb
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
D=json.loads((P/'ap3-data.json').read_text())
R={'data_sha256':hashlib.sha256((P/'ap3-data.json').read_bytes()).hexdigest()}
# Two sensor rows: their determinant is 6 min(x,12-x), except at endpoints.
rows=0
for x in [F(i,5) for i in range(61)]:
 a,b=min(x,6),max(x-6,0)
 det=6*a-6*b
 assert det==6*min(x,12-x)
 assert (det==0)==(x in [0,12])
 if det:
  for u in [F(1,12),F(1,3),F(1,2),F(3,4)]:
   v=F(5,6)-u;S=a*u+b*v
   uu=(6*S-5*b)/det;vv=(5*a-6*S)/det
   assert (uu,vv)==(u,v)
   rows+=1
assert [1/((S+e)/x)**2 for x,S,e in [(F(3),F(3,2),F(1,20)),(F(6),F(3),F(-1,20))]]==[F(3600,961),F(14400,3481)]
R['AP-19']={'exact_noninteger_sensor_reconstructions':rows,'all_sensor_determinant_formula':True}
# Independently check price slack decompositions at many nonnegative plans.
slacks=0
for x,y in product([F(i,3) for i in range(13)],repeat=2):
 for rr,bb in [(5,4),(4,4),(4,5)]:
  assert F(2,3)*(rr-2*x-y)+F(5,3)*(bb-x-2*y)==F(2*rr+5*bb,3)-3*x-4*y
  slacks+=1
# Completeness of whole-product two-counter argument when stock is 4+4.
assert all(3*x+4*y<=8 for x,y in product(range(5),repeat=2) if 2*x+y<=4 and x+2*y<=4)
R['AP-20']={'exact_price_slack_identities':slacks,'integer_gap_bound':True}
# A rational payoff polynomial and regret certificates, including both epsilon endpoints.
games=0
for p,q in product([F(i,60) for i in range(61)],repeat=2):
 pay=1-p-q+3*p*q
 assert pay==2*p*q+(1-p)*(1-q)
 assert min(2*p,1-p)<=pay<=max(2*q,1-q)
 for eps in [F(0),F(1,15),F(1,3)]:
  assert (min(2*p,1-p)>=F(2,3)-eps)==(F(1,3)-eps/2<=p<=F(1,3)+eps)
  assert (max(2*q,1-q)<=F(2,3)+eps)==(F(1,3)-eps<=q<=F(1,3)+eps/2)
 games+=1
R['AP-22']={'joint_payoff_and_regret_cases':games}
# Solve absorbing probabilities independently from linear first-step equations by elimination.
def solve(A,b):
 A=[list(map(F,r))+[F(v)] for r,v in zip(A,b)];n=len(A)
 for j in range(n):
  k=next(k for k in range(j,n) if A[k][j]);A[j],A[k]=A[k],A[j]
  z=A[j][j];A[j]=[x/z for x in A[j]]
  for k in range(n):
   if k!=j:
    z=A[k][j];A[k]=[x-z*y for x,y in zip(A[k],A[j])]
 return [r[-1] for r in A]
fixations=0
for N in range(2,11):
 T=[[F(comb(N,j))*F(i,N)**j*F(N-i,N)**(N-j) for j in range(N+1)] for i in range(N+1)]
 A=[[F(i==j)-T[i][j] for j in range(1,N)] for i in range(1,N)]
 b=[T[i][N] for i in range(1,N)]
 answer=solve(A,b)
 assert answer==[F(i,N) for i in range(1,N)]
 assert all(sum(j*T[i][j] for j in range(N+1))==i for i in range(N+1))
 fixations+=N-1
R['AP-24']={'independently_solved_absorption_probabilities':fixations,'scope':'finite N=2..10 supports the uniform-tail proof reviewed separately'}
# Shortest legal reaction routes: BFS distance, not just invariant membership.
routes=0
for start in product(range(5),repeat=3):
 seen={start:0};queue=deque([start])
 while queue:
  z=queue.popleft()
  for step in [(-1,-2,1),(1,2,-1)]:
   w=tuple(a+b for a,b in zip(z,step))
   if min(w)>=0 and w not in seen:seen[w]=seen[z]+1;queue.append(w)
 for end,dist in seen.items():
  assert dist==abs(end[2]-start[2])
  assert end[0]+end[2]==start[0]+start[2] and end[1]+2*end[2]==start[1]+2*start[2]
  routes+=1
R['AP-25']={'shortest_legal_route_distances':routes}
# Delays: exact sign identity plus determinant, not a numerical optimizer.
for k in range(1,101):
 d=F(3,4)**k-F(1,2)**k
 dd=F(3,4)**(k+1)-F(1,2)**(k+1)-d
 assert dd==F(1,4)*F(1,2)**k*(2-F(3,2)**k)
 assert (dd>0)==(k==1)
assert F(1,100)/(F(3,4)**2-F(1,2)**2)==F(4,125)
matrices=0
for alpha,beta,r,s in product(range(-2,3),repeat=4):
 assert alpha*beta*s-beta*alpha*r==alpha*beta*(s-r)
 matrices+=1
R['AP-27']={'consecutive_delay_sign_cases':100,'signed_observability_determinants':matrices}
# Every error pattern against every parity-kernel codeword, including multi-bit errors.
def h(w):return ((w[0]+w[1]+w[3])%2,(w[1]+w[2]+w[4])%2)
words=list(product(range(2),repeat=5));kernel=[w for w in words if h(w)==(0,0)]
errors=0
for c,e in product(kernel,words):
 received=tuple(x^y for x,y in zip(c,e))
 assert h(received)==h(e)
 assert (received in kernel)==(h(e)==(0,0))
 errors+=1
code=[tuple(map(int,s)) for s in ['00000','11100','10011','01111']]
counts=Counter()
for w in words:
 matches=[c for c in code if sum(x!=y for x,y in zip(w,c))<=1]
 counts[len(matches)]+=1
assert counts=={1:24,0:8}
R['AP-28']={'all_kernel_codeword_error_pairs':errors,'detected_error_patterns':24,'undetected_nonzero_patterns':7,'one_bit_code_received_partition':dict(counts)}
# General power identity follows directly from node balance; check arbitrary positive network values.
powers=0
for V,a,b,Rm in product([F(1,3),F(1),F(5,2),F(7)],repeat=4):
 X=(V/a)/(1/a+1/b+1/Rm);I=(V-X)/a
 assert V*I==I*I*a+X*X/b+X*X/Rm
 star=a*b/(a+b);v0=V*b/(a+b)
 assert (v0-X)/v0==star/(Rm+star)
 powers+=1
R['AP-30']={'arbitrary_network_exact_power_certificates':powers}
R['status']='passed; general arguments and scientific model scope reviewed in review-ap3-design.md'
(P/'review-ap3-checks-results.json').write_text(json.dumps(R,indent=2)+'\n')
print(json.dumps(R,indent=2))
