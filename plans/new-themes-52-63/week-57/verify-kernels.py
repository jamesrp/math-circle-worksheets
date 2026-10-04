#!/usr/bin/env python3
"""Exact integer-point classification, independent area, seam and hole checks."""
from fractions import Fraction
from math import gcd
from pathlib import Path
import json

def cross(a,b,p):
    return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])

def classify(poly,p):
    winding=0
    for a,b in zip(poly,poly[1:]+poly[:1]):
        c=cross(a,b,p)
        if c==0 and min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and min(a[1],b[1])<=p[1]<=max(a[1],b[1]):
            return 'boundary'
        if a[1]<=p[1]<b[1] and c>0: winding+=1
        if b[1]<=p[1]<a[1] and c<0: winding-=1
    return 'inside' if winding else 'outside'

def data(poly):
    lo_x,hi_x=min(x for x,y in poly),max(x for x,y in poly)
    lo_y,hi_y=min(y for x,y in poly),max(y for x,y in poly)
    inside=[]; boundary=[]
    for x in range(lo_x,hi_x+1):
        for y in range(lo_y,hi_y+1):
            category=classify(poly,(x,y))
            if category=='inside': inside.append((x,y))
            if category=='boundary': boundary.append((x,y))
    shoelace=sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1]))
    area=Fraction(abs(shoelace),2)
    b_gcd=sum(gcd(abs(b[0]-a[0]),abs(b[1]-a[1])) for a,b in zip(poly,poly[1:]+poly[:1]))
    assert len(boundary)==b_gcd
    q=Fraction(len(inside))+Fraction(len(boundary),2)-1
    assert area==q,(poly,area,q)
    return dict(vertices=poly,I=len(inside),B=len(boundary),area=str(area),inside=inside,boundary=boundary)

polygons=[
 ('3 by 2 rectangle',[(0,0),(3,0),(3,2),(0,2)],(2,10,Fraction(6))),
 ('slanted parallelogram',[(0,0),(2,0),(3,3),(1,3)],(4,6,Fraction(6))),
 ('inward-corner L',[(0,0),(3,0),(3,1),(1,1),(1,3),(0,3)],(0,12,Fraction(5))),
 ('right triangle',[(0,0),(3,0),(0,2)],(1,6,Fraction(3))),
 ('clear-sided nonempty triangle',[(0,0),(1,2),(3,1)],(2,3,Fraction(5,2))),
]
examples=[]
for name,poly,expected in polygons:
    d=data(poly); assert (d['I'],d['B'],Fraction(d['area']))==expected
    examples.append(dict(name=name,**d))

joins=[
 ('rectangle diagonal',[(0,0),(3,0),(3,2)],[(0,0),(3,2),(0,2)],[(0,0),(3,0),(3,2),(0,2)],((0,0),(3,2))),
 ('two rectangles',[(0,0),(2,0),(2,2),(0,2)],[(2,0),(4,0),(4,2),(2,2)],[(0,0),(4,0),(4,2),(0,2)],((2,0),(2,2))),
 ('slanted diagonal',[(0,0),(2,0),(3,3)],[(0,0),(3,3),(1,3)],[(0,0),(2,0),(3,3),(1,3)],((0,0),(3,3))),
]
seams=[]
for name,p1,p2,union,(a,b) in joins:
    d1,d2,d=data(p1),data(p2),data(union)
    k=gcd(abs(b[0]-a[0]),abs(b[1]-a[1]))+1
    assert d['I']==d1['I']+d2['I']+k-2
    assert d['B']==d1['B']+d2['B']-2*k+2
    assert Fraction(d['area'])==Fraction(d1['area'])+Fraction(d2['area'])
    seams.append(dict(name=name,seam_points=k,first=d1,second=d2,union=d))

outer=[(0,0),(4,0),(4,4),(0,4)]; hole=[(1,1),(3,1),(3,3),(1,3)]
inside=[]; boundary=[]
for x in range(5):
    for y in range(5):
        p=(x,y); o,h=classify(outer,p),classify(hole,p)
        if o=='boundary' or h=='boundary': boundary.append(p)
        elif o=='inside' and h=='outside': inside.append(p)
ring_area=Fraction(data(outer)['area'])-Fraction(data(hole)['area'])
assert (len(inside),len(boundary),ring_area)==(0,24,Fraction(12))
assert ring_area==len(inside)+Fraction(len(boundary),2)-1+1
out=dict(method='Exact cross products and winding number for all integer dots; shoelace area independently; edge gcd count cross-check.',
         examples=examples,seam_checks=seams,ring=dict(I=0,B=24,h=1,area='12',inside=inside,boundary=boundary),
         status='mathematical examples checked; physical fit and piloting unperformed')
Path(__file__).with_name('kernel-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('Verified five simple polygons, three seam joins and one separated-hole region with exact arithmetic.')
