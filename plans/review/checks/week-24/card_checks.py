"""Week 24 card spot checks: answers cited in card.md, the strongest 1-9 cycles, and best cycles with repeats."""
from itertools import combinations, permutations
from fractions import Fraction as F
from math import comb
def w(X,Y): return sum(1 for x in X for y in Y if x>y)
A,B,C=(2,4,9),(1,6,8),(3,5,7)
print("cycle",w(A,B),w(B,C),w(C,A))
print("K1 P5",[w((2,4,x),B) for x in (3,5,7,9)])
sw=[]
for i,a in enumerate(A):
  for j,b in enumerate(B):
    A2=list(A);B2=list(B);A2[i]=b;B2[j]=a
    sw.append((a,b,w(B2,A2),w(B2,A2)>w(A2,B2)))
print("K1 P6",sw)
# K1 P7
ok=[S for S in combinations(range(1,7),3) if w(S,tuple(set(range(1,7))-set(S)))*2==9]
print("K1 P7",ok)
print("23 P4",[(x,w((2,x,9),B),w(B,C),w(C,(2,x,9))) for x in (0,2,4,9,10)])
# 2-3 P3 fixed maxima
sols=[]
for a in combinations(range(1,7),2):
  rest=[v for v in range(1,7) if v not in a]
  for b in combinations(rest,2):
    c=tuple(v for v in rest if v not in b)
    AA,BB,CC=a+(9,),b+(8,),c+(7,)
    if w(AA,BB)>=5 and w(BB,CC)>=5 and w(CC,AA)>=5: sols.append((AA,BB,CC,w(AA,BB),w(BB,CC),w(CC,AA)))
print("fixed max",sols)
# 2-3 P6
cnt=0;s6=[]
vals=range(1,13)
for AA in combinations(vals,3):
  if sum(AA)!=15: continue
  r=[v for v in vals if v not in AA]
  for BB in combinations(r,3):
    if sum(BB)!=18: continue
    r2=[v for v in r if v not in BB]
    for CC in combinations(r2,3):
      if sum(CC)!=21: continue
      cnt+=1
      if w(AA,BB)>=5 and w(BB,CC)>=5 and w(CC,AA)>=5: s6.append((AA,BB,CC))
print("23 P6 assignments",cnt,s6)
A4,B4,C4=(2,2,4,9),(1,1,6,8),(3,3,5,7)
print("45 P4 four",w(A4,B4),w(B4,C4),w(C4,A4))
A6,B6,C6=(2,2,4,4,9,9),(1,1,6,6,8,8),(3,3,5,5,7,7)
print("six",w(A6,B6),w(B6,C6),w(C6,A6))
p=F(5,9);q=F(4,9)
ahead=sum(comb(6,k)*p**k*q**(6-k) for k in (4,5,6)); tie=comb(6,3)*p**3*q**3
print("six rounds",float(ahead),float(tie),float(1-ahead-tie))
# 45 P5
for X,Y in [((1,5),(2,4)),((2,6),(1,5)),((4,6),(2,3)),((1,3),(2,6))]: print(X,Y,w(X,Y),w(Y,X))
from itertools import combinations
from collections import Counter
from collections import Counter
def w(X,Y): return sum(1 for x in X for y in Y if x>y)
S=set(range(1,10));cyc=[]
for A in combinations(sorted(S),3):
  r=sorted(S-set(A))
  for B in combinations(r,3):
    C=tuple(sorted(set(r)-set(B)))
    e=(w(A,B),w(B,C),w(C,A))
    if min(e)>=5: cyc.append((A,B,C,e))
print(len(cyc)); print(Counter(tuple(sorted(c[3])) for c in cyc))
for c in cyc:
  if 9 in c[0]: print(c)
# 4-card decks from 1..12: best min edge out of 16
S=set(range(1,13));best=0;ex=None;n=0
for A in combinations(sorted(S),4):
  if 12 not in A: continue
  r=sorted(S-set(A))
  for B in combinations(r,4):
    C=tuple(sorted(set(r)-set(B)))
    e=(w(A,B),w(B,C),w(C,A))
    if min(e)>=9:
      n+=1
      if min(e)>best: best=min(e);ex=(A,B,C,e)
print("4-card 1..12 cycles with 12 in A:",n,"best min",best,ex)
from itertools import combinations_with_replacement as cwr
from itertools import combinations_with_replacement as cwr, product
def w(X,Y): return sum(1 for x in X for y in Y if x>y)
for N in (6,9):
  best=0;ex=None;count66=0
  decks=list(cwr(range(1,N+1),3))
  for A in decks:
    for B in decks:
      if set(A)&set(B): continue
      ab=w(A,B)
      if ab<5: continue
      for C in decks:
        if set(C)&set(A) or set(C)&set(B): continue
        m=min(ab,w(B,C),w(C,A))
        if m>best: best=m;ex=(A,B,C,ab,w(B,C),w(C,A))
  print(N,best,ex)
