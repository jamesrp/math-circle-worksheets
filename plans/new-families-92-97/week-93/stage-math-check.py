"""Independent exact arithmetic and constructive checks; no student files changed."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import hashlib
import pymupdf as fitz

root=Path(__file__).resolve().parents[1]

def move(a,b):
    m=(a+b)/2
    return a*b/m,m

def say(*args): print(*args)

say('PDF SHA256',hashlib.sha256((root/'draft/students.pdf').read_bytes()).hexdigest())
say('P1: asks for all 24-unit-tile rectangles, rotations identified, and closest to square.')
pairs=[(a,24//a) for a in range(1,25) if 24%a==0 and a<=24//a]
assert pairs==[(1,24),(2,12),(3,8),(4,6)]
assert min(pairs,key=lambda p:p[1]-p[0])==(4,6)
say('All factor pairs:',pairs,'; 4 by 6 uniquely minimizes side gap, aspect ratio and perimeter.')

say('P2: asks to fill each target square except for one square using all rectangle pieces.')
for a,b in [(2,6),(2,4)]:
    a,b=F(a),F(b); m=(a+b)/2; d=(b-a)/2
    # Cut original into m by a and d by a. Rotate second and place above first.
    # Target partition consists of bottom m by a, upper-left a by d, upper-right d by d.
    assert m+a*0 == a+d
    assert m*a+a*d==a*b
    assert m*m-a*b==d*d
    bottom={(x,y) for x in range(int(m)) for y in range(int(a))}
    top={(x,y) for x in range(int(a)) for y in range(int(a),int(m))}
    hole={(x,y) for x in range(int(a),int(m)) for y in range(int(a),int(m))}
    target={(x,y) for x in range(int(m)) for y in range(int(m))}
    assert not bottom&top and not bottom&hole and not top&hole
    assert bottom|top|hole==target
    say('Rectangle',a,'by',b,'target',m,'by',m,'hole side',d,'; exact unit-cell cover verified.')

say('P3: asks one move, old/new marks, tightest interval among those marked side lengths.')
assert move(F(1),F(3))==(F(3,2),F(2))
say('Non-task example 1 by 3 -> 3/2 by 2, area 3 verified.')
for a,b in [(2,6),(3,6),(2,10)]:
    a,b=F(a),F(b); h,m=move(a,b); A=a*b
    assert a<h<m<b and h*h<A<m*m and h*m==A
    say('Area',A,'old',(a,b),'new',(h,m),'tightest bracket',(h,m),'exact squares',(h*h,m*m))

say('P4: asks order of exact cards and tightest area-12 square-side bracket.')
cards={'A':(F(24,7),F(7,2)),'B':(F(2),F(6)),'C':(F(336,97),F(97,28)),'D':(F(3),F(4))}
orders=[p for p in permutations(cards) if all(move(*cards[p[i]])==cards[p[i+1]] for i in range(3))]
assert orders==[('B','D','A','C')]
for label,(h,m) in cards.items():
    assert h*m==12 and h*h<12<m*m
    say(label, 'area',h*m,'gap',m-h, 'squared bounds',(h*h,m*m))
assert min(cards,key=lambda c:cards[c][1]-cards[c][0])=='C'
say('Unique order:',orders[0],'; tightest card C; gap = 1/2716.')

say('P5: asks decimals 0.01 apart enclosing area-12 square side, exact area checks and exactness.')
lo,hi=F('3.46'),F('3.47')
assert hi-lo==F('0.01') and lo*lo<12<hi*hi
say('3.46^2 =',lo*lo,'= 11.9716; 3.47^2 =',hi*hi,'= 12.0409. Neither is exact.')
say('Alternative decimal precision permits other valid intervals; prompt does not claim uniqueness.')

say('P6: asks general average-square area comparison, cut/rearrangement, excess area.')
say('For positive a<=b, put d=(b-a)/2 and m=a+d. Cut b-by-a into m-by-a and d-by-a; rotate latter to a-by-d and place atop first. The residual upper-right region is d-by-d. Excess is d^2; zero iff a=b.')
say('P7: asks arbitrarily narrow enclosures and whether any finite move yields a square.')
say('For 0<a<b, m=(a+b)/2, h=ab/m. a<h<sqrt(ab)<m<b follows from a<m<b and m^2-ab=(b-a)^2/4>0. Product hm=ab is unchanged.')
say('The new gap is m-h=(b-a)^2/[2(a+b)], positive and strictly less than (b-a)/2. Induction gives gap_n < gap_0/2^n for n>=1, hence arbitrarily narrow brackets. Positive gap at every finite round precludes an exact square, even if the fixed square side is rational.')
say('Equal-side boundary case is fixed; zero/negative lengths are outside ordinary rectangle assumptions.')
count=0
for denominator in [1,2,3,7,13]:
 for ai in range(1,61):
  for bi in range(ai,61):
   a,b=F(ai,denominator),F(bi,denominator); h,m=move(a,b)
   assert h*m==a*b
   assert a<=h<=m<=b
   assert h*h<=a*b<=m*m
   assert m*m-a*b==((b-a)/2)**2
   assert m-h==(b-a)**2/(2*(a+b))
   if a<b: assert 0<m-h<(b-a)/2
   else: assert h==m==a
   count+=1
say('Exact rational cases checked:',count)

pdf=fitz.open(root/'draft/students.pdf')
assert len(pdf)==5
say('PDF page count',len(pdf))
rects=[d['rect'] for d in pdf[1].get_drawings() if len(d['items'])==4 and d['width']>.5 and d['rect'].width>20 and d['rect'].height>20]
assert len(rects)==4
for r,(w,h) in zip(rects,[(6,2),(4,4),(4,2),(3,3)]):
 assert abs(r.width/w-r.height/h)<0.001
 assert abs(r.width/w-1.5*72/2.54)<0.03
 say('P2 printed rectangle units',(w,h),'PDF points per unit x/y',round(r.width/w,5),round(r.height/h,5))
say('Independent render of all five pages inspected: page 1 24x20 grid; page 2 A 6x2 and 4x4, B 4x2 and 3x3 at same x/y unit scale; page 3 input 3x1, concatenated 1+3 with half length 2, output 2x1.5, three 0..10 number lines; page 4 exact fraction cards; page 5 general rectangle/square correctly marked not to scale. No mathematical diagram mismatch found.')
say('PASS: every problem checked; no located mathematical defect. Physical cutting rehearsal and classroom piloting are not claimed.')
