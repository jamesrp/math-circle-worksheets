#!/usr/bin/env python3
"""Independent finite checks of return-visit kernels. No worksheet generator imports."""
from functools import lru_cache
from itertools import product, combinations, permutations
from math import gcd,lcm
from fractions import Fraction as F

@lru_cache(None)
def passwin(n,available):
 if n==0:return False
 return any(not passwin(n-k,available) for k in (1,2) if k<=n) or bool(available and not passwin(n,False))
@lru_cache(None)
def lastwin(n,last):
 return any(not lastwin(n-k,k) for k in (1,2,3) if k<=n and k!=last)
@lru_cache(None)
def pairwin(runs):
 for j,n in enumerate(runs):
  for i in range(n-1):
   target=tuple(sorted(runs[:j]+runs[j+1:]+tuple(x for x in (i,n-i-2) if x)))
   if not pairwin(target):return True
 return False
@lru_cache(None)
def misere(piles):
 if not any(piles):return True  # formal post-game state: last mover lost
 return any(not misere(piles[:i]+(n-k,)+piles[i+1:]) for i,n in enumerate(piles) for k in range(1,n+1))
@lru_cache(None)
def coinswin(pos):
 for i,x in enumerate(pos):
  low=pos[i-1]+1 if i else 1
  for y in range(low,x):
   if not coinswin(pos[:i]+(y,)+pos[i+1:]):return True
 return False

def coingaps(pos):
 gaps=[pos[i]-pos[i-1]-1 for i in range(len(pos)-1,0,-2)]
 if len(pos)%2:gaps.append(pos[0]-1)
 return gaps

def xor(xs):
 t=0
 for x in xs:t^=x
 return t

def billiard(a,b,x=0,y=0,p=1,q=1):
 # Rational exact event simulation; interior loops stop on full state repetition.
 x,y,p,q=map(F,(x,y,p,q)); origin=(x,y,p,q);seen={origin};steps=[];time=F(0)
 for _ in range(1000):
  tx=((a-x)/p if p>0 else -x/p);ty=((b-y)/q if q>0 else -y/q);dt=min(tx,ty)
  nx,ny=x+p*dt,y+q*dt;steps.append(((x,y),(nx,ny)));time+=dt;x,y=nx,ny
  if x in (0,a) and y in (0,b):return 'corner',time,(x,y),steps
  if dt==tx:p=-p
  if dt==ty:q=-q
  state=(x,y,p,q)
  # An interior origin is not a wall event; detect it within next segment separately.
  txo=(origin[0]-x)/p;tyo=(origin[1]-y)/q
  nxt=min((a-x)/p if p>0 else -x/p,(b-y)/q if q>0 else -y/q)
  if p==origin[2] and q==origin[3] and txo==tyo and 0<txo<=nxt:
   return 'loop',time+txo,(origin[0],origin[1]),steps
  if state in seen:return 'loop',time,(x,y),steps
  seen.add(state)
 raise RuntimeError('unbounded trace')

def crosses(steps,a,b):
 pts=set()
 for i,((x1,y1),(x2,y2)) in enumerate(steps):
  for (x3,y3),(x4,y4) in steps[i+1:]:
   vx,vy=x2-x1,y2-y1;wx,wy=x4-x3,y4-y3;det=vx*wy-vy*wx
   if det==0:continue
   t=((x3-x1)*wy-(y3-y1)*wx)/det;s=((x3-x1)*vy-(y3-y1)*vx)/det
   if 0<t<1 and 0<s<1:
    z=(x1+t*vx,y1+t*vy)
    if 0<z[0]<a and 0<z[1]<b:pts.add(z)
 return pts

def aiming(a,b,start,target):
 sx,sy=map(F,start);tx,ty=map(F,target)
 images={'LEFT':(-tx,ty),'RIGHT':(2*a-tx,ty),'BOTTOM':(tx,-ty),'TOP':(tx,2*b-ty)}
 out={}
 for wall,(ix,iy) in images.items():
  dx,dy=ix-sx,iy-sy
  if wall in ('LEFT','RIGHT'):
   wallx=0 if wall=='LEFT' else a;z=(F(wallx)-sx)/dx;point=(F(wallx),sy+z*dy)
  else:
   wally=0 if wall=='BOTTOM' else b;z=(F(wally)-sy)/dy;point=(sx+z*dx,F(wally))
  assert 0<z<1
  assert 0<=point[0]<=a and 0<=point[1]<=b
  out[wall]=(point,dx*dx+dy*dy)
 return out

def wall_reflect(point,wall,a,b):
 x,y=point
 return {'L':(-x,y),'R':(2*a-x,y),'B':(x,-y),'T':(x,2*b-y)}[wall]

def two_bounces(a,b,start,target,word):
 # Unfold backwards, then independently trace the actual reflected rectangle.
 image=tuple(map(F,target))
 for wall in reversed(word):image=wall_reflect(image,wall,a,b)
 x,y=map(F,start);dx,dy=image[0]-x,image[1]-y
 squared=dx*dx+dy*dy;now=F(0);seen=[];contacts=[]
 for _ in range(10):
  vx=(F(a)-x)/dx if dx>0 else -x/dx if dx<0 else None
  vy=(F(b)-y)/dy if dy>0 else -y/dy if dy<0 else None
  times=[v for v in (vx,vy) if v is not None]
  delta=min(times)
  if now+delta>=1:
   end=(x+dx*(1-now),y+dy*(1-now))
   return ''.join(seen)==word and end==tuple(map(F,target)),image,squared,contacts
  x+=dx*delta;y+=dy*delta;now+=delta
  if vx==vy:return False,image,squared,contacts+[(x,y,'corner')]
  if delta==vx:
   seen.append('R' if dx>0 else 'L');dx=-dx
  else:
   seen.append('T' if dy>0 else 'B');dy=-dy
  contacts.append((x,y,seen[-1]))
 raise RuntimeError('too many two-bounce contacts')

def trail_possible(edges,start,end=None,directed=True):
 @lru_cache(None)
 def search(vertex,mask):
  if mask==0:return end is None or vertex==end
  for i,(u,v) in enumerate(edges):
   if mask>>i&1:
    if u==vertex and search(v,mask^(1<<i)):return True
    if not directed and v==vertex and search(u,mask^(1<<i)):return True
  return False
 return search(start,(1<<len(edges))-1)

def reachable_edges(edges,start):
 seen={start}
 while True:
  new=seen|{v for u,v in edges if u in seen}|{u for u,v in edges if v in seen}
  if new==seen:break
  seen=new
 return all(u in seen and v in seen for u,v in edges)

# Explicit assertions, not just printed patterns.
for n in range(1,200):
 assert passwin(n,False)==(n%3!=0)
 assert passwin(n,True)==(not (n>=4 and n%3==1))
 for last,res in [(0,{0}),(1,{0,1}),(2,{0}),(3,{0,3})]:
  assert lastwin(n,last)==(n%4 not in res)
assert [n for n in range(1,13) if not pairwin((n,))]==[1,5,9]
for n in range(2,22,2):assert pairwin((n,))
for n in range(1,15):assert not pairwin((n,n))
for pos in product(range(7),repeat=3):
 if not any(pos):continue
 predicted=(sum(x==1 for x in pos)%2==0) if max(pos)<=1 else xor(pos)!=0
 assert misere(pos)==predicted,(pos,misere(pos),predicted)
for k in range(1,5):
 for pos in combinations(range(1,11),k):assert coinswin(pos)==bool(xor(coingaps(pos))),pos
for a,b in product(range(1,16),repeat=2):
 kind,t,corner,steps=billiard(a,b)
 g=gcd(a,b);assert len(crosses(steps,a,b))==(a//g-1)*(b//g-1)//2,(a,b,crosses(steps,a,b))
 for p,q in [(2,1),(1,2),(3,2)]:
  kind,t,corner,steps=billiard(a,b,p=p,q=q)
  T=lcm(a//gcd(a,p),b//gcd(b,q));assert t==T
  k=p*T//a;l=q*T//b
  assert corner==(a if k%2 else 0,b if l%2 else 0)
  assert len(steps)-1==k+l-2
interior={}
for x,y in product(range(1,6),range(1,4)):
 kind,t,corner,_=billiard(6,4,x,y)
 assert (kind=='corner')==((x-y)%2==0),(x,y,kind,t)
 if kind=='loop':assert t==24,(x,y,t)
 interior[x,y]=(kind,t,corner)
assert sum(v[0]=='corner' for v in interior.values())==8
r=aiming(4,4,(1,1),(2,3))
assert r=={'LEFT':((F(0),F(5,3)),13),'RIGHT':((F(4),F(11,5)),29),'BOTTOM':((F(5,4),F(0)),17),'TOP':((F(7,4),F(4)),17)},r
r=aiming(4,4,(1,1),(3,3));assert all(d==20 for p,d in r.values()),r
two_cases={}
for target,expected in [((2,3),{'LR','LT','RL','RT','BL','BR','BT','TB'}),((3,3),{'LR','LT','RL','BR','BT','TB'})]:
 checks={a+b:two_bounces(4,4,(1,1),target,a+b) for a,b in product('LRBT',repeat=2)}
 valid={word for word,result in checks.items() if result[0]}
 assert valid==expected,(target,valid)
 two_cases[target]=checks
assert two_cases[2,3]['LR'][3]==[(F(0),F(9,7),'L'),(F(4),F(17,7),'R')]
assert two_cases[2,3]['RL'][3]==[(F(4),F(5,3),'R'),(F(0),F(23,9),'L')]
assert two_cases[2,3]['BT'][3]==[(F(7,6),F(0),'B'),(F(11,6),F(4),'T')]
assert two_cases[2,3]['TB'][3]==[(F(13,10),F(4),'T'),(F(17,10),F(0),'B')]
assert {word:two_cases[2,3][word][2] for word in ('LR','RL','BT','TB','LT','BL','RT','BR')}=={'LR':53,'RL':85,'BT':37,'TB':101,'LT':25,'BL':25,'RT':41,'BR':41}
for word in ('LB','BL','RT','TR'):assert two_cases[3,3][word][3][-1][2]=='corner'
word='0001011100';assert {word[i:i+3] for i in range(8)}=={''.join(x) for x in product('01',repeat=3)}
neck='00010111';assert {''.join(neck[(i+j)%8] for j in range(3)) for i in range(8)}=={''.join(x) for x in product('01',repeat=3)}
goodneck=[]
for xs in product('01',repeat=8):
 s=''.join(xs)
 if len({''.join(s[(i+j)%8] for j in range(3)) for i in range(8)})==8:goodneck.append(s)
canonical={min(s[i:]+s[:i] for i in range(8)) for s in goodneck}
assert canonical=={'00010111','00011101'},canonical
# Independent legal-walk enumeration tests the directed criterion, including loops.
directed_options=list(product(range(3),repeat=2))
for mask in range(1,1<<9):
 edges=tuple(e for i,e in enumerate(directed_options) if mask>>i&1)
 vertices={v for e in edges for v in e};origin=min(vertices)
 delta=[sum(u==v for u,w in edges)-sum(w==v for u,w in edges) for v in range(3)]
 connected=reachable_edges(edges,origin)
 actual_closed=trail_possible(edges,origin,origin)
 assert actual_closed==(connected and delta==[0,0,0]),(edges,delta)
 actual_open=any(trail_possible(edges,s,t) for s,t in permutations(range(3),2))
 predicted_open=connected and sorted(delta)==[-1,0,1]
 assert actual_open==predicted_open,(edges,delta)
# In every feasible small undirected state, the token reachability test decides
# whether an incident first choice still permits a complete walk.
undirected_options=list(combinations(range(4),2))
for mask in range(1,1<<6):
 edges=tuple(e for i,e in enumerate(undirected_options) if mask>>i&1)
 for start in range(4):
  if not trail_possible(edges,start,directed=False):continue
  for i,(u,v) in enumerate(edges):
   if start not in (u,v):continue
   destination=v if start==u else u;remaining=edges[:i]+edges[i+1:]
   assert trail_possible(remaining,destination,directed=False)==reachable_edges(remaining,destination),(edges,start,i)
assert trail_possible(((0,1),(1,2),(2,0),(0,3)),0,directed=False)
assert not reachable_edges(((0,1),(1,2),(2,0)),3)
ten_rectangles=[]
for a,b in product(range(1,13),repeat=2):
 if len(crosses(billiard(a,b)[3],a,b))==10:ten_rectangles.append((a,b))
assert ten_rectangles==[(3,11),(5,6),(6,5),(10,12),(11,3),(12,10)],ten_rectangles
print('Ten-crossing integer rectangles within12x12:',ten_rectangles)
print('Inverse aiming: all four exact contact points and squared lengths checked for both4x4targetpairs.')
print('Two-bounce words: all16 ordered pairs exactly checked for both4x4targets; valid counts8 and6. Opposite contact coordinates and all8 squared lengths checked.')
print('Binary triple necklaces verified: 16 marked rows / 2 rotation classes.')
print('PASS states verified n1–199; LAST states n1–199; adjacent-pair row positions and equal-row reply checked.')
print('Misere Nim all 342 nonempty 0–6 triples; coin gaps all 1–4 coin subsets of squares1–10 checked.')
print('Billiard crossing counts all 225 rectangles1–15; three rational slopes on every rectangle checked exactly.')
print('Interior6x4 classification:',{k:v[0] for k,v in interior.items()})
print('Password linear10 / circular8 windows exhaustive; lowerbounds are window-count arguments.')
print('Directed Euler criterion checked all511 nonempty digraphs on3vertices, loops included; safe-first-step reachability checked all63 nonempty simple undirected graphs on4vertices and feasible starts.')
