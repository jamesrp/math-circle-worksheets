#!/usr/bin/env python3
"""Exact rational cell-intersection calculations, no geometry package required."""
from fractions import Fraction as F
import math

def intersection(a,b):
    x=max(a[0],b[0]);y=min(a[1],b[1]);return max(F(0),y-x)

def counts(dx,dy):
    # Disjoint-interior rectangle pieces of the fixed L polygon.
    shape=[(F(0),F(2),F(0),F(1)),(F(1),F(2),F(1),F(2))]
    inside=cover=0
    for i in range(-2,4):
        for j in range(-2,4):
            x,y=F(i)+dx,F(j)+dy
            a=sum(intersection((x,x+1),(r[0],r[1]))*intersection((y,y+1),(r[2],r[3])) for r in shape)
            inside+=a==1;cover+=a>0
    return inside,cover

if __name__=='__main__':
    expected={(F(0),F(0)):(3,3),(F(1,2),F(0)):(1,5),(F(1,2),F(1,2)):(0,8)}
    for shift,ans in expected.items():assert counts(*shift)==ans;print('Grid shift',shift,'bounds',ans)
    cards=[((2,8),(4,9)),((3,5),(6,7)),((1,6),(4,4))]
    assert [(max(a[0],b[0]),min(a[1],b[1])) for a,b in cards]==[(4,8),(6,5),(4,4)]
    for t in (F(1,4),F(3,4)):
        area=4*t-t*t;assert 0<area<3
        # three L cells: left-bottom t, right-bottom 2t-t², right-top t
        cellareas=[t,2*t-t*t,t];assert all(0<a<1 for a in cellareas)
        print('Corridor width',t,'cell areas',cellareas,'total',area)
    assert 4*F(1,4)-F(1,4)**2<1 and 4*F(3,4)-F(3,4)**2>2
    # Replace a length-1 horizontal edge with N balanced triangular waves.
    # Trapezoid integration checks exact area preservation.
    for n in (1,4,20):
        t=F(1,4);amp=F(1,8);pts=[(F(0),t)]
        for k in range(n):
            pts.extend([(F(4*k+1,4*n),t+amp),(F(4*k+2,4*n),t),(F(4*k+3,4*n),t-amp),(F(4*k+4,4*n),t)])
        a=sum((x2-x1)*(y1+y2)/2 for (x1,y1),(x2,y2) in zip(pts,pts[1:]));assert a==t
        length=sum(math.hypot(float(x2-x1),float(y2-y1)) for (x1,y1),(x2,y2) in zip(pts,pts[1:]))
        assert abs(length-math.sqrt(1+n*n/4))<1e-10
        print('Equal-area jagged boundary:',n,'waves; perimeter',7+length)
