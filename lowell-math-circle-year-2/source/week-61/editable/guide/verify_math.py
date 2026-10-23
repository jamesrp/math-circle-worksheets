#!/usr/bin/env python3
"""Independent guide checks, standard library; imports no student/research code."""
from fractions import Fraction
from itertools import product
from math import acos, atan2, cos, degrees, pi, radians, sin, sqrt
from pathlib import Path
import json
import sys

def dot(u, v):
    return sum(a*b for a,b in zip(u,v))

def scale(u, a):
    return tuple(a*x for x in u)

def cross(u, v):
    return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])

def normalized(u):
    return scale(u, 1/sqrt(dot(u,u)))

def add(*vectors):
    return tuple(sum(v[j] for v in vectors) for j in range(3))

def tangent(a,b):
    return normalized(add(b,scale(a,-dot(a,b))))

def angle(a,b,c):
    z=dot(tangent(a,b),tangent(a,c))
    return degrees(acos(max(-1,min(1,z))))

def solid_area(vertices):
    a,b,c=vertices
    return 2*atan2(abs(dot(a,cross(b,c))),1+dot(a,b)+dot(a,c)+dot(b,c))

def equal_corner(q):
    d=cos(radians(q))/(1-cos(radians(q)))
    y=d*(1-d)/sqrt(1-d*d)
    return ((1,0,0),(d,sqrt(1-d*d),0),(d,y,sqrt(1-d*d-y*y)))

def meridian(q):
    return ((0,0,1),(1,0,0),(cos(radians(q)),sin(radians(q)),0))

def close(actual,expected,tol=1e-10):
    assert abs(actual-expected)<tol,(actual,expected)

def verify_instance(name,vertices,corners,fraction,cell_fractions=None):
    a,b,c=vertices
    for v in vertices:
        close(dot(v,v),1)
    assert abs(dot(a,cross(b,c)))>1e-9
    for i in range(3):
        close(angle(vertices[i],vertices[(i+1)%3],vertices[(i+2)%3]),corners[i],1e-8)
        edge=acos(max(-1,min(1,dot(vertices[i],vertices[(i+1)%3]))))
        assert 0<edge<pi
    normals=[]
    for i in range(3):
        n=normalized(cross(vertices[(i+1)%3],vertices[(i+2)%3]))
        if dot(n,vertices[i])<0:
            n=scale(n,-1)
        normals.append(n)
    witness=normalized(add(*normals))
    assert min(dot(witness,v) for v in vertices)>0
    close(solid_area(vertices)/(4*pi),float(fraction))
    expected_counts=(3,1,1,1,1,1,1,3)
    expected_pair_letters=('ABC','C','B','A','A','B','C','ABC')
    cells=[]
    for j,signs in enumerate(product((1,-1),repeat=3)):
        rays=[scale(v,s) for v,s in zip(vertices,signs)]
        x=normalized(add(*rays))
        assert all(s*dot(n,x)>0 for s,n in zip(signs,normals))
        members=[signs[1]==signs[2],signs[0]==signs[2],signs[0]==signs[1]]
        assert sum(members)==expected_counts[j]
        letters=''.join(letter for letter,member in zip('ABC',members) if member)
        assert letters==expected_pair_letters[j]
        f=solid_area(rays)/(4*pi)
        assert 0<f<.5
        if cell_fractions:
            close(f,float(cell_fractions[j]))
        cells.append(dict(region=j+1,signs=signs,fraction=f,members=members,count=sum(members)))
    close(sum(cell['fraction'] for cell in cells),1)
    for i in range(3):
        pair_fraction=sum(cell['fraction'] for cell in cells if cell['members'][i])
        close(pair_fraction,2*corners[i]/360)
    for j in range(8):
        close(cells[j]['fraction'],cells[7-j]['fraction'])
    counted=sum(cell['fraction']*cell['count'] for cell in cells)
    close(counted,1+4*float(fraction))
    return dict(name=name,corners=corners,fraction=str(fraction),counted_area=counted,cells=cells)

def main():
    if len(sys.argv)!=2:
        raise SystemExit('Usage: python3 verify_math.py OUTPUT_JSON')
    results=[]
    for gap in (30,40,45,60,72,90,110,120):
        results.append(verify_instance(f'meridian-{gap}',meridian(gap),(gap,90,90),Fraction(gap,720),
            [Fraction(1,8)]*8 if gap==90 else None))
    first=((0,0,1),(2*sqrt(2)/3,0,1/3),(1/sqrt(6),1/sqrt(2),1/sqrt(3)))
    results.append(verify_instance('record-60-60-90',first,(60,60,90),Fraction(1,24)))
    results.append(verify_instance('record-80-each',equal_corner(80),(80,80,80),Fraction(1,12),
        [Fraction(1,12)]+[Fraction(5,36)]*6+[Fraction(1,12)]))
    results.append(verify_instance('record-100-each',equal_corner(100),(100,100,100),Fraction(1,6)))
    p4={str(gap):str(Fraction(gap,720)) for gap in (45,72,120)}
    assert p4=={'45':'1/16','72':'1/10','120':'1/6'}
    assert Fraction(40,360)==Fraction(1,9)
    roster={'k1':4,'middle':4,'upper':3,'adults':3,'kits':5,'strings':15,'string_cm':1200,
            'right_angle_tabs':11,'usable_dots':30,'spare_dots':10,'first_student_sheets':21,
            'plain_k1_sheets':4,'return_student_sheets':16,'all_student_sheets':37,
            'guide_pages':9,'adult_guide_sheets':27}
    assert roster['k1']+roster['middle']+roster['upper']==11
    assert roster['first_student_sheets']==3*(roster['middle']+roster['upper'])
    assert roster['return_student_sheets']==roster['middle']+4*roster['upper']
    report={'status':'passed','method':'Independent coordinates, tangent angles, determinant solid angles, oriented side normals, eight sign cells; no student imports.',
            'exact_p4':p4,'roster_materials_printing':roster,'instances':results,
            'limits':'Numerical checks illustrate the exact proof. Physical fabrication, marking, fit, handling rehearsal and classroom piloting are unperformed.'}
    out=Path(sys.argv[1]);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(f'Passed: {len(results)} coordinate triangles, {8*len(results)} sign cells, exact keys and kit/sheet counts.')

if __name__=='__main__':
    main()
