#!/usr/bin/env python3
"""Independent numerical checks on authored diagram coordinates and tasks.

This verifies the writer's mathematics; it is not the independent math-review stage.
Only the construction coordinates are imported from geometry.py. Angle, area,
hemisphere, half-space and coverage calculations below are separate computations.
"""
from itertools import product
from fractions import Fraction
from math import acos, atan2, cos, degrees, isclose, pi, radians, sin, sqrt
from pathlib import Path
import argparse,json,sys
sys.dont_write_bytecode=True
from geometry import from_angles, meridian, side_view

def d(a,b): return sum(a[i]*b[i] for i in range(3))
def c(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def normalize(v): return tuple(t/sqrt(d(v,v)) for t in v)
def determinant(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def tangent_angle(a,b,c):
    t1=normalize(tuple(b[i]-d(a,b)*a[i] for i in range(3)))
    t2=normalize(tuple(c[i]-d(a,c)*a[i] for i in range(3)))
    return degrees(acos(max(-1,min(1,d(t1,t2)))))
def solid_angle(a,b,c):
    return 2*atan2(abs(determinant(a,b,c)),1+d(a,b)+d(b,c)+d(c,a))

checked=[]
def check_triangle(name,vertices,expected):
    a,b,c0=vertices
    angles=[tangent_angle(a,b,c0),tangent_angle(b,c0,a),tangent_angle(c0,a,b)]
    assert all(isclose(x,y,abs_tol=1e-9) for x,y in zip(angles,expected)),(name,angles,expected)
    assert all(isclose(d(v,v),1,abs_tol=1e-12) for v in vertices)
    hemisphere=normalize(tuple(sum(v[i] for v in vertices) for i in range(3)))
    assert all(d(hemisphere,v)>1e-8 for v in vertices)
    lengths=[acos(max(-1,min(1,d(vertices[i],vertices[(i+1)%3])))) for i in range(3)]
    assert all(0<t<pi for t in lengths)
    area=solid_angle(*vertices)
    excess=radians(sum(expected)-180)
    assert isclose(area,excess,abs_tol=1e-9)
    assert 0<area<2*pi
    # The three oriented side half-spaces determine eight cells.
    normals=[normalize(c(b,c0)),normalize(c(c0,a)),normalize(c(a,b))]
    for i in range(3):
        if d(normals[i],vertices[i])<0: normals[i]=tuple(-t for t in normals[i])
    cells=[]
    for signs in product((1,-1),repeat=3):
        vv=[tuple(t*x for x in v) for t,v in zip(signs,vertices)]
        test=normalize(tuple(sum(v[i] for v in vv) for i in range(3)))
        observed=tuple(1 if d(n,test)>0 else -1 for n in normals)
        assert observed==signs
        membership=[observed[(k+1)%3]==observed[(k+2)%3] for k in range(3)]
        count=sum(membership)
        assert count==(3 if signs in ((1,1,1),(-1,-1,-1)) else 1)
        cells.append((solid_angle(*vv),membership,count))
    assert isclose(sum(x[0] for x in cells),4*pi,abs_tol=1e-9)
    for k in range(3):
        actual=sum(x[0] for x in cells if x[1][k])
        assert isclose(actual,4*radians(expected[k]),abs_tol=1e-9)
    weighted=sum(x[0]*x[2] for x in cells)
    assert isclose(weighted,4*pi+4*area,abs_tol=1e-9)
    fraction=Fraction(sum(expected)-180,720)
    checked.append({'name':name,'angles_degrees':angles,'surface_fraction':str(fraction),
        'coordinate_solid_angle':area,'open_hemisphere_vertex_dot_products':[d(hemisphere,v) for v in vertices],
        'region_pair_counts':[x[2] for x in cells],
        'cell_surface_fractions':[str(Fraction(x[0]/(4*pi)).limit_denominator(720)) for x in cells],
        'six_lune_area_fraction':str(Fraction(2*sum(expected),360)),
        'checked':True})

for theta in (45,72,90,110,120): check_triangle('meridian-'+str(theta),meridian(theta),(theta,90,90))
for angles in ((60,60,90),(80,80,80),(100,100,100)):
    check_triangle('record-'+str(angles),from_angles(*angles),angles)
assert Fraction(40,360)==Fraction(1,9)
assert tangent_angle((0,0,1),(sin(radians(50)),0,cos(radians(50))),
    (sin(radians(50))*cos(radians(135)),sin(radians(50))*sin(radians(135)),cos(radians(50))))==135
# Opposite points: distinct great-circle semicircles share the same length pi R.
opposite_paths=[]
for azimuth in (0,35,90):
    h=radians(azimuth)
    vs=[(sin(pi*j/180)*cos(h),sin(pi*j/180)*sin(h),cos(pi*j/180)) for j in range(181)]
    length=sum(acos(max(-1,min(1,d(a,b)))) for a,b in zip(vs,vs[1:]))
    assert isclose(length,pi,abs_tol=1e-10)
    opposite_paths.append({'meridian_degrees':azimuth,'unit_sphere_length':length})
# The example endpoints lie 95 degrees apart on their shorter great-circle arc.
p=(cos(radians(-40)),sin(radians(-40)),0);q=(cos(radians(55)),sin(radians(55)),0)
assert isclose(degrees(acos(d(p,q))),95,abs_tol=1e-12)
covering_views=[]
for name,v in [('octant',meridian(90)),('unequal-80',from_angles(80,80,80))]:
    camera=side_view(v)
    assert camera.z(v[0])>0 and abs(camera.z(v[1]))<1e-12 and abs(camera.z(v[2]))<1e-12
    front=[];back=[]
    for number,s in enumerate(product((1,-1),repeat=3),1):
        rays=[tuple(k*x for x in vv) for k,vv in zip(s,v)]
        depths=[camera.z(w) for w in rays]
        (front if s[0]>0 else back).append(number)
        assert min(depths)>-1e-12 if s[0]>0 else max(depths)<1e-12
    assert front==[1,2,3,4] and back==[5,6,7,8]
    covering_views.append({'name':name,'front_complete_cells':front,'back_complete_cells':back})
v=from_angles(80,80,80)
x=normalize(tuple(3*v[0][i]-v[1][i]-v[2][i] for i in range(3)))
normals=[normalize(c(v[(i+1)%3],v[(i+2)%3])) for i in range(3)]
assert tuple(1 if d(n,x)>0 else -1 for n in normals)==(1,-1,-1)
assert d(normals[1],x)*d(normals[2],x)>0
result={'status':'all checks passed','triangles':checked,'opposite_semicircle_examples':opposite_paths,
    'route_example_minor_arc_degrees':95,'angle_convention_example_degrees':135,
    'lune_example_angle_degrees':40,'lune_example_surface_fraction':'1/9',
    'physical_pretest':'unperformed','classroom_pilot':'unperformed',
    'covering_views':covering_views,'single_pair_patch_example':{'label':'X','signs':[1,-1,-1],'marked_pair':'A','count':1},
    'stage_limit':'authored coordinate verification; final emitted-geometry reconstruction and rebuild evidence are separate revision checks'}
p=argparse.ArgumentParser();p.add_argument('output_json',nargs='?');args=p.parse_args()
if args.output_json: Path(args.output_json).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
