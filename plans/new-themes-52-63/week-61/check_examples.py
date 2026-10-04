"""Check meridional triangle angles and area independently from coordinates."""
from fractions import Fraction
from math import acos, atan2, cos, degrees, isclose, pi, radians, sin, sqrt
from pathlib import Path
import json

def dot(u, v): return sum(a*b for a,b in zip(u,v))
def tangent(p, q):
    w = tuple(q[i] - dot(p, q)*p[i] for i in range(3))
    n = sqrt(dot(w, w))
    return tuple(x/n for x in w)
def angle(p, q, r):
    return degrees(acos(max(-1, min(1, dot(tangent(p,q), tangent(p,r))))))
def det(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

records=[]
for theta in (30, 60, 90, 120):
    t=radians(theta); n=(0.,0.,1.); a=(1.,0.,0.); b=(cos(t),sin(t),0.)
    angles=[angle(n,a,b), angle(a,n,b), angle(b,n,a)]
    assert all(isclose(x,y,abs_tol=1e-10) for x,y in zip(angles,(theta,90,90)))
    # Independent solid-angle determinant formula for the smaller spherical region.
    area=2*atan2(abs(det(n,a,b)),1+dot(n,a)+dot(a,b)+dot(b,n))
    assert isclose(area,t,abs_tol=1e-10)
    hemisphere_pole=(cos(t/2),sin(t/2),1.)
    assert all(dot(hemisphere_pole,p)>0 for p in (n,a,b))
    records.append({'meridian_gap_degrees':theta,'coordinate_angles_degrees':angles,
        'exact_angle_sum_degrees':180+theta,'exact_excess_degrees':theta,
        'exact_sphere_fraction':str(Fraction(theta,720)),
        'numeric_area_unit_sphere':area,'contained_in_open_hemisphere':True})
result={'model':'round sphere; shorter great-circle arcs; smaller convex triangle',
    'meridional_triangles':records,'radius_doubling_length_factor':2,
    'radius_doubling_area_factor':4,
    'invalid_boundary_cases':['theta=0: degenerate','theta=180: equator vertices antipodal'],
    'verified':True,'physical_pretest':'unperformed','pilot':'unperformed'}
Path(__file__).with_name('math-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
