from fractions import Fraction as F
from itertools import combinations_with_replacement as cwr, product
def V(bag, m):
    v = F(sum(bag), len(bag))
    out=[v]
    for _ in range(m-1):
        v = F(sum(max(x, v) for x in bag), len(bag)); out.append(v)
    return out  # V1..Vm
# Middle ticket tie at two offers among distinct 3-ticket bags 0..9
bags=[b for b in cwr(range(10),3) if len(set(b))==3]
tie=[b for b in bags if b[1]==V(b,1)[0]]
print("distinct bags",len(bags),"middle ties at 2 offers",len(tie), all(2*b[1]==b[0]+b[2] for b in tie))
# middle taken at 2 offers but passed at 3
flip=[b for b in bags if b[1]>V(b,2)[0] and b[1]<V(b,2)[1]]
print("middle taken at 2, passed at 3:",len(flip), flip[:20])
# 0,b,6 bags
print([b for b in range(1,6) if b> V((0,b,6),2)[0] and b< V((0,b,6),2)[1]])
# third ticket for bag with 1 and 9 so that middle ties (range 0..20)
sols=[]
for x in range(0,21):
    b=sorted((1,9,x))
    if len(set(b))<3: continue
    if 2*b[1]==b[0]+b[2]: sols.append(x)
print("1,9,x ties:",sols)
# brute-force check 2-offer and 3-offer best totals for 0,4,6
def best_total(bag,n):
    # exact optimum total over k^n words via recursion with integers
    k=len(bag)
    v=V(bag,n)
    return v[-1]*k**n
print(best_total((0,4,6),2),best_total((0,4,6),3),best_total((0,5,6),3),best_total((0,5,6),4))
# for 0,5,6: first horizon where first 5 is passed
for b in [(0,5,6),(0,4,6),(0,3,6),(1,3,5)]:
    vs=V(b,8); mid=b[1]
    h=[m+1 for m in range(1,8) if mid < vs[m-1]]
    print(b, "middle passed first at horizon", h[0] if h else None, [str(x) for x in vs[:4]])
