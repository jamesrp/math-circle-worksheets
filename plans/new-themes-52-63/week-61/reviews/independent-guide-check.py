"""Coordinator sphere checks from manually supplied angles, no author imports."""
from math import sin,cos,acos,atan2,sqrt,pi
from itertools import product
from fractions import Fraction
from pathlib import Path
import json

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def unit(a):
    l=sqrt(dot(a,a));return tuple(x/l for x in a)
def angle_at(a,b,c):
    tb=unit(tuple(b[i]-dot(a,b)*a[i] for i in range(3)))
    tc=unit(tuple(c[i]-dot(a,c)*a[i] for i in range(3)))
    return acos(max(-1,min(1,dot(tb,tc))))*180/pi

table=[]
for degrees in [(90,90,90),(60,60,90),(80,80,80),(100,100,100)]:
    alpha,beta,gamma=[x*pi/180 for x in degrees]
    b=acos((cos(beta)+cos(alpha)*cos(gamma))/(sin(alpha)*sin(gamma)))
    c=acos((cos(gamma)+cos(alpha)*cos(beta))/(sin(alpha)*sin(beta)))
    A=(0,0,1);B=(sin(c),0,cos(c));C=(sin(b)*cos(alpha),sin(b)*sin(alpha),cos(b))
    vertices=[A,B,C]
    corners=[angle_at(A,B,C),angle_at(B,C,A),angle_at(C,A,B)]
    assert all(abs(x-y)<1e-10 for x,y in zip(corners,degrees))
    det=dot(A,cross(B,C));assert det>0
    area=2*atan2(det,1+dot(A,B)+dot(B,C)+dot(C,A))
    fraction=Fraction(sum(degrees)-180,720)
    assert abs(area/(4*pi)-float(fraction))<1e-12
    pole=unit(tuple(sum(v[i] for v in vertices) for i in range(3)))
    assert all(dot(pole,v)>0 for v in vertices) # explicit open hemisphere
    normals=[]
    for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
        n=unit(cross(vertices[j],vertices[k]))
        if dot(n,vertices[i])<0:n=tuple(-x for x in n)
        normals.append(n)
    cells=[]
    for signs in product([1,-1],repeat=3):
        point=unit(tuple(sum(s*v[i] for s,v in zip(signs,vertices)) for i in range(3)))
        assert all(dot(n,point)*s>0 for n,s in zip(normals,signs))
        members=[signs[1]==signs[2],signs[0]==signs[2],signs[0]==signs[1]]
        count=sum(members);assert count==(3 if len(set(signs))==1 else 1)
        rays=[tuple(s*x for x in v) for s,v in zip(signs,vertices)]
        cell_area=2*atan2(abs(dot(rays[0],cross(rays[1],rays[2]))),
                        1+dot(rays[0],rays[1])+dot(rays[1],rays[2])+dot(rays[2],rays[0]))
        cells.append({'signs':signs,'pairs':['ABC'[i] for i,m in enumerate(members) if m],
                      'count':count,'solid_angle_fraction':cell_area/(4*pi)})
    assert [x['count'] for x in cells]==[3,1,1,1,1,1,1,3]
    assert abs(sum(x['solid_angle_fraction'] for x in cells)-1)<1e-12
    pairs=[Fraction(d,180) for d in degrees]
    for i,pair in enumerate('ABC'):
        assert abs(sum(x['solid_angle_fraction'] for x in cells if pair in x['pairs'])-float(pairs[i]))<1e-12
    assert sum(pairs)==1+4*fraction
    table.append({'angles_degrees':degrees,'vertices':vertices,'measured_corners':corners,
                  'fraction_exact':str(fraction),'solid_angle_fraction':area/(4*pi),
                  'pair_fractions_exact':[str(x) for x in pairs],'covering_cells':cells})

# Exact supplied lune and northern-half-lune tasks.
gaps={str(t):{'lune':str(Fraction(t,360)),'triangle':str(Fraction(t,720))} for t in [40,45,72,120]}
assert gaps['45']['triangle']=='1/16' and gaps['72']['triangle']=='1/10' and gaps['120']['triangle']=='1/6'
unequal=[Fraction(1,12)]+[Fraction(5,36)]*6+[Fraction(1,12)]
assert sum(unequal)==1
assert all(abs(float(a)-c['solid_angle_fraction'])<1e-12 for a,c in zip(unequal,table[2]['covering_cells']))
for pair in 'ABC':
    members=table[2]['covering_cells']
    assert sum(a for a,c in zip(unequal,members) if pair in c['pairs'])==Fraction(4,9)
assert sum(a*c['count'] for a,c in zip(unequal,table[2]['covering_cells']))==Fraction(4,3)
data={'scope':'independent inverse-angle coordinates, tangent angles, solid angle, exact fractions and sign-cell witnesses',
      'triangles':table,'lune_and_pole_equator_keys':gaps,
      '80_degree_cell_fractions':[str(x) for x in unequal],
      'universal_proof':'reviewed separately: sign agreements and antipodal equal area; numeric coordinates are example checks',
      'physical_tests':'unperformed'}
out=Path(__file__).resolve().parent/'guide-review-assets';out.mkdir(exist_ok=True)
(out/'independent-guide-checks.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'exact_triangle_keys':[x['fraction_exact'] for x in table],'unequal_cover_total':'4/3','example_and_cover_checks':'passed'}))
