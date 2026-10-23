#!/usr/bin/env python3
"""Geometric reflection checks, including every precise student ray example."""
from math import sqrt, isclose
from fractions import Fraction
R=sqrt(3)
# Counterclockwise vertex order; side names A,D,C,B.
SQUARE=[(0.,0.),(4.,0.),(4.,4.),(0.,4.)]
RHOMBUS=[(0.,0.),(4.,0.),(6.,2*R),(2.,2*R)]
NAMES='ADCB'
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def ray(poly,p,v,n):
 hits=[]
 for _ in range(n):
  candidates=[]
  for j,(a,b) in enumerate(zip(poly,poly[1:]+poly[:1])):
   e=sub(b,a); den=cross(v,e)
   if abs(den)<1e-11:continue
   t=cross(sub(a,p),e)/den; u=cross(sub(a,p),v)/den
   if t>1e-9 and -1e-9<=u<=1+1e-9:candidates.append((t,u,j,a,e))
  t,u,j,a,e=min(candidates)
  assert 1e-8<u<1-1e-8, 'Corner hit'
  p=(p[0]+t*v[0],p[1]+t*v[1]); hits.append((NAMES[j],p))
  # reflection: keep tangential component, reverse normal component
  c=2*dot(v,e)/dot(e,e); v=(c*e[0]-v[0],c*e[1]-v[1])
 return hits
assert ''.join(k for k,p in ray(SQUARE,(1.,2.),(1.,-1.),2))=='AD'
example=ray(SQUARE,(1.,2.),(1.,-1.),2)
assert example[0][1]==(3.,0.) and example[1][1]==(4.,1.)
aba=ray(RHOMBUS,(1.,.5),(-1.,-1.),3)
assert ''.join(k for k,p in aba)=='ABA'
expected=[(.5,0.),((R-1)/4,(3-R)/4),((R+1)/2,0.)]
for (_,p),q in zip(aba,expected):assert all(isclose(a,b,abs_tol=1e-10) for a,b in zip(p,q))
# The exact displayed ABA witness is documented by radical coordinates above.
# Each hit lies in an open wall segment; all earliest-positive-hit tests pass.
# Rectangle scaling in unfolded coordinates preserves vertical/horizontal
# crossing order and noncorner hits. Independent numerical checks of 30 words:
for a in range(1,7):
 for b in range(1,6):
  p=(.731,1.129);v=(a+.271,b+.391)
  q=(2*p[0],p[1]);w=(2*v[0],v[1])
  one=''.join(k for k,p in ray(SQUARE,p,v,12))
  two=''.join(k for k,p in ray([(0.,0.),(8.,0.),(8.,4.),(0.,4.)],q,w,12))
  assert one==two
print('PASS: non-task AD example, exact radical ABA witness with no corners, and 30 scaled 12-bounce rectangle words.')
print('Rhombus ABA witness:',aba)

# Exact rational crossing checks against the actual printed square windows.
# Original room is [0,2]^2; wall labels alternate under reflection.
def exact_window_word(v, low, high, count=3):
    p=(Fraction(1),Fraction(1)); events=[]
    for axis in (0,1):
        if not v[axis]: continue
        for k in range(low//2,high//2+1):
            t=Fraction(2*k-p[axis],v[axis])
            if t<=0: continue
            q=(p[0]+t*v[0],p[1]+t*v[1])
            if not all(low<=x<=high for x in q):continue
            label=('B' if k%2==0 else 'D') if axis==0 else ('A' if k%2==0 else 'C')
            events.append((t,label,q))
    events.sort()
    if len(events)<count:return None
    if any(events[j][0]==events[j+1][0] for j in range(min(count,len(events)-1))):return None
    return ''.join(e[1] for e in events[:count]),[e[2] for e in events[:count]]
words={}
for a in range(-12,13):
 for b in range(-12,13):
  if (a,b)==(0,0):continue
  result=exact_window_word((a,b),-4,6)
  if result:words.setdefault(result[0],(a,b))
assert len(words)>=6
for direction,wanted in [((3,2),'DCB'),((2,3),'CDA'),((-3,2),'BCD')]:
    result=exact_window_word(direction,-2,4)
    assert result and result[0]==wanted
    assert set(wanted)&set('AC') and set(wanted)&set('BD')
    # Doubling x in every hit lies in the displayed [-4,8] x [-2,4]
    # rectangle window. The same parameter times give the same wall word.
    assert all(-4<=2*x<=8 and -2<=y<=4 for x,y in result[1])
print('PASS: at least six exact three-bounce choices in page 1, and three distinct mixed-wall transfer witnesses for revised page 4.')
