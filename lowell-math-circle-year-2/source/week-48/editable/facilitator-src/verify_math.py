from fractions import Fraction as F
from itertools import product, permutations, combinations
from collections import deque,Counter

def clip(poly,axis,level,sign):
 out=[]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  ina=sign*(a[axis]-level)>=0; inb=sign*(b[axis]-level)>=0
  if ina:out.append(a)
  if ina!=inb:
   t=(level-a[axis])/(b[axis]-a[axis]);out.append(tuple(a[j]+t*(b[j]-a[j]) for j in range(2)))
 return out

def area(poly):return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1])))/2 if poly else F(0)
def square_area(poly,x,y,u):
 for axis,lev,sign in [(0,x,1),(0,x+u,-1),(1,y,1),(1,y+u,-1)]:poly=clip(poly,axis,lev,sign)
 return area(poly)

def statuses(poly,x,y,u):
 a=square_area(poly,x,y,u)
 return 'I' if a==u*u else ('O' if a==0 else 'P')

trap=[(F(x),F(y)) for x,y in [('0.5','0.5'),('3.5','0.5'),('3','3.5'),('1','3.5')]]
diamond=[(F(x),F(y)) for x,y in [(0,2),(2,0),(4,2),(2,4)]]
tri=[(F(x),F(y)) for x,y in [(0,4),(4,4),(4,0)]]
for name,p in [('trapezoid',trap),('diamond',diamond),('triangle',tri)]:
 print(name,'exact area',area(p))
 for n in [4,8]:
  u=F(4,n);ss=[statuses(p,i*u,j*u,u) for j in range(n) for i in range(n)]
  print(n,'inside',ss.count('I'),'cover',len(ss)-ss.count('O'),'big unit bounds',ss.count('I')*u*u,(len(ss)-ss.count('O'))*u*u)
  if n==4:
   for y in range(4):print(''.join(ss[4*y:4*y+4]))
 if name=='trapezoid':
  records=[]
  for y in range(4):
   for x in range(4):
    s=statuses(p,F(x),F(y),F(1));sub=[statuses(p,F(x)+F(i,2),F(y)+F(j,2),F(1,2)) for j in range(2) for i in range(2)]
    gain=F(sub.count('I')+sub.count('O'),4) if s=='P' else F(0)
    records.append(((x+1,y+1),s,sub.count('I'),sub.count('P'),sub.count('O'),gain))
  print('refinement records (column,row; coarse; I/P/O; gap gain)',records)
  best2=max(sum(r[4] for r in pair) for pair in combinations(records,2))
  best3=max(sum(r[5] for r in triple) for triple in combinations(records,3))
  print('best 2 removal',best2,'best 3 gap reduction',best3)
  assert best2==6 and best3==F(3)

# Week 47 finite instance and shortest legal moves.
sol=[s for s in product(range(6),repeat=7) if s[0]==1 and s[4]==3 and s[6]==1 and all(abs(x-y)<=1 for x,y in zip(s,s[1:]))]
assert len(sol)==10
assert tuple(min(s[i] for s in sol) for i in range(7))==(1,0,1,2,3,2,1)
assert tuple(max(s[i] for s in sol) for i in range(7))==(1,2,3,4,3,2,1)
start=(1,2,1,2,1);goal=(1,0,0,0,1);q=deque([(start,0)]);seen={start}
while q:
 s,d=q.popleft()
 if s==goal:break
 for i in [1,2,3]:
  for change in [-1,1]:
   t=list(s);t[i]+=change;t=tuple(t)
   if min(t)>=0 and all(abs(x-y)<=1 for x,y in zip(t,t[1:])) and t not in seen:seen.add(t);q.append((t,d+1))
assert d==5
print('landscape minimum moves',d,'seven-site completions',len(sol))

# Week 49 complete finite searches, parity, and printed trajectories.
def D(s):return tuple(abs(s[i]-s[(i+1)%len(s)]) for i in range(len(s)))
def run(s):
 out=[s]
 while any(s):
  s=D(s)
  if s in out:return out+[s]
  out.append(s)
 return out
for m in [4,5]:
 rr=[run(s) for s in product(range(m+1),repeat=4)];assert all(not any(r[-1]) for r in rr);assert max(len(r)-1 for r in rr)==7
 print('heights 0..',m,'starts',len(rr),'max duration',max(len(r)-1 for r in rr))
for s in product(range(2),repeat=4):
 for _ in range(4):s=D(s)
 assert not any(s)
print('permutation move counts',Counter(len(run(s))-1 for s in permutations((0,1,2,4))))

# Week 50 rational witnesses, including every corridor segment.
wide=[(0,0),(20,0),(20,30),(60,30),(60,60),(100,60),(100,90),(140,90),(140,120),(160,120)]
narrow=[(0,0),(0,F(15,2))]
for i in range(1,9):narrow.extend([(20*i,15*i-F(15,2)),(20*i,min(120,15*i+F(15,2)))])
for ps,d in [(wide,F(15)),(narrow,F(8))]:
 assert ps[0]==(0,0) and ps[-1]==(160,120)
 assert all((a==c and b<e) or (b==e and a<c) for (a,b),(c,e) in zip(ps,ps[1:]))
 assert max(abs(y-F(3,4)*x) for x,y in ps)<=d
 assert sum(abs(a-c)+abs(b-e) for (a,b),(c,e) in zip(ps,ps[1:]))==280
print('wide witness turns',len(wide)-2,'narrow maximum gap',max(abs(y-F(3,4)*x) for x,y in narrow))
# At <=7 turns, <=8 alternating nonzero segments. Max horizontal travel:
# at most 4 horizontal segments; at least one is an endpoint segment, span <=20.
assert 20+3*40<160
for route in [[(0,0),(80,0),(80,40),(40,40),(40,80),(160,80),(160,120)],[(0,0),(120,0),(120,90),(80,90),(80,120),(160,120)]]:
 assert sum(abs(a-c)+abs(b-e) for (a,b),(c,e) in zip(route,route[1:]))==360

# Week 51 endpoints and dependent feasible set.
assert [(a,9-a) for a in range(4,7) if 3<=9-a<=5]==[(4,5),(5,4),(6,3)]
assert (13-12,15-10)==(1,5)
assert (7-6,9-5)==(1,4)
assert (4+4-6-1,6+4-4-1)==(1,5)
assert (2*7-12,2*9-12)==(2,6)
print('All checks passed. Exact finite mathematics, not physical testing.')
