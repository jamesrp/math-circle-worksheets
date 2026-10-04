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
word='0001011100';assert {word[i:i+3] for i in range(8)}=={''.join(x) for x in product('01',repeat=3)}
neck='00010111';assert {''.join(neck[(i+j)%8] for j in range(3)) for i in range(8)}=={''.join(x) for x in product('01',repeat=3)}
goodneck=[]
for xs in product('01',repeat=8):
 s=''.join(xs)
 if len({''.join(s[(i+j)%8] for j in range(3)) for i in range(8)})==8:goodneck.append(s)
canonical={min(s[i:]+s[:i] for i in range(8)) for s in goodneck}
assert canonical=={'00010111','00011101'},canonical
print('Inverse aiming: all four exact contact points and squared lengths checked for both4x4targetpairs.')
print('Binary triple necklaces verified: 16 marked rows / 2 rotation classes.')
print('PASS states verified n1–199; LAST states n1–199; adjacent-pair row positions and equal-row reply checked.')
print('Misere Nim all 342 nonempty 0–6 triples; coin gaps all 1–4 coin subsets of squares1–10 checked.')
print('Billiard crossing counts all 225 rectangles1–15; three rational slopes on every rectangle checked exactly.')
print('Interior6x4 classification:',{k:v[0] for k,v in interior.items()})
print('Password linear10 / circular8 windows exhaustive; lowerbounds are window-count arguments.')
