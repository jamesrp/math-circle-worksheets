from itertools import combinations, permutations, product
from collections import Counter
def w(x,y): return sum(a>b for a in x for b in y)
A,B,C=(2,4,9),(1,6,8),(3,5,7)
print("cycle",w(A,B),w(B,C),w(C,A))
# all labelled deals of 1..9
cyc=[]; n=0
S=set(range(1,10))
for a in combinations(sorted(S),3):
    r=S-set(a)
    for b in combinations(sorted(r),3):
        c=tuple(sorted(r-set(b))); n+=1
        e=(w(a,b),w(b,c),w(c,a))
        if min(e)>=5: cyc.append((a,b,c,e))
print("deals",n,"cycles",len(cyc),Counter(tuple(sorted(x[3])) for x in cyc))
print("min edge over cycles",set(min(x[3]) for x in cyc))
two6=[x for x in cyc if sorted(x[3])==[5,6,6]]
print("two edges at 6:",two6)
print("three at 6:",[x for x in cyc if min(x[3])>=6])
# pinned 9,8,7
pin=[x for x in cyc if 9 in x[0] and 8 in x[1] and 7 in x[2]]
print("pinned cycles",len(pin),pin)
# K-1 P6 swaps
ok=[]
for i,j in product(range(3),range(3)):
    a=list(A); b=list(B); a[i],b[j]=b[j],a[i]
    if w(b,a)>w(a,b): ok.append((A[i],B[j],w(b,a)))
print("K1 P6",len(ok),ok)
# 2-3 P4
for x in [0,2,4,9,10]:
    a=(2,x,9); print("23P4",x,w(a,B),w(B,C),w(C,a))
# K-1 P8 / 2-3 P7: two-card decks from 1..6
cnt=0
for p in permutations(range(1,7)):
    a,b,c=p[0:2],p[2:4],p[4:6]
    if w(a,b)>2 and w(b,c)>2 and w(c,a)>2: cnt+=1
print("two-card cycles from 1-6:",cnt)
# K-1 P7
c7=0
for a in combinations(range(1,7),3):
    b=tuple(sorted(set(range(1,7))-set(a)))
    if w(a,b)==w(b,a): c7+=1
print("K1 P7 equal splits",c7)
# 4-5 P4
A6,B6,C6=(2,2,4,4,9,9),(1,1,6,6,8,8),(3,3,5,5,7,7)
A4,B4,C4=(2,2,4,9),(1,1,6,8),(3,3,5,7)
print("six",w(A6,B6),w(B6,C6),w(C6,A6),"of",36)
print("four",w(A4,B4),w(B4,C4),w(C4,A4),"of",16)
# distinct printed number-pairs counted as equally likely
def wd(x,y):
    s=set(product(set(x),set(y))); return sum(a>b for a,b in s), len(s)
print("distinct six",wd(A6,B6),wd(B6,C6),wd(C6,A6))
print("distinct four",wd(A4,B4),wd(B4,C4),wd(C4,A4))
# 2-3 P6
sols=[];tot=0
for a in combinations(range(1,13),3):
    if sum(a)!=15: continue
    for b in combinations([v for v in range(1,13) if v not in a],3):
        if sum(b)!=18: continue
        for c in combinations([v for v in range(1,13) if v not in a+b],3):
            if sum(c)!=21: continue
            tot+=1
            if w(a,b)>4 and w(b,c)>4 and w(c,a)>4: sols.append((a,b,c))
print("23P6",tot,sols)
# six rounds
from math import comb
p=5/9
print("ahead",sum(comb(6,k)*p**k*(1-p)**(6-k) for k in (4,5,6)),"tie",comb(6,3)*p**3*(1-p)**3,"lose all",(4/9)**6)
