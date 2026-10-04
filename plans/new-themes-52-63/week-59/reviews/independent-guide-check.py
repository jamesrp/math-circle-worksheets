"""Coordinator derivation: manual nominal arcs, no author-module imports."""
from math import cos,sin,pi,sqrt,atan2
from pathlib import Path
import json

w=60.0
A=(0.0,0.0);B=(w,0.0);C=(w/2,sqrt(3)*w/2)
O=(w/2,sqrt(3)*w/6)
arcs=[(A,0,pi/3),(B,2*pi/3,pi),(C,4*pi/3,5*pi/3)]

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def support(u):
    vals=[]
    angle=atan2(u[1],u[0])%(2*pi)
    for center,start,end in arcs:
        for t in [start,end]+([angle] if start-1e-12<=angle<=end+1e-12 else []):
            vals.append(dot((center[0]+w*cos(t),center[1]+w*sin(t)),u))
    return max(vals)

widths=[];heights=[];square=[];triangle=[];ellipse=[]
for i in range(3600):
    t=2*pi*i/3600;u=(cos(t),sin(t));v=(-u[0],-u[1])
    widths.append(support(u)+support(v))
    heights.append(support(u)-dot(O,u))
    square.append(w*(abs(u[0])+abs(u[1])))
    projections=[dot(p,u) for p in [A,B,C]]
    triangle.append(max(projections)-min(projections))
    ellipse.append(2*sqrt(30**2*u[0]**2+20**2*u[1]**2))
assert max(abs(x-w) for x in widths)<1e-10
expected_h=[w-w/sqrt(3),w/sqrt(3)]
assert abs(min(heights)-expected_h[0])<1e-10
assert abs(max(heights)-expected_h[1])<1e-10
assert abs(min(square)-w)<1e-10 and abs(max(square)-w*sqrt(2))<1e-10
assert abs(min(triangle)-sqrt(3)*w/2)<1e-10 and abs(max(triangle)-w)<1e-10
assert abs(min(ellipse)-40)<1e-10 and abs(max(ellipse)-60)<1e-10
assert 44-12==32 # supplied pre-use off-center point support example

# Every manual arc point lies in all three radius-w disks, and every vertex
# serves as the fixed lower contact throughout its directed 60-degree sector.
sector_checks=0
for center,start,end in arcs:
    for i in range(121):
        t=start+(end-start)*i/120;u=(cos(t),sin(t))
        p=(center[0]+w*u[0],center[1]+w*u[1])
        assert all((p[0]-q[0])**2+(p[1]-q[1])**2<=w*w+1e-8 for q in [A,B,C])
        assert abs(support(u)-dot(center,u)-w)<1e-10
        assert abs(-support((-u[0],-u[1]))-dot(center,u))<1e-10
        sector_checks+=1

# Analytic destinations are derived in the guide review. These finite checks
# detect transcribed quantities; they do not prove universal support bounds.
data={'scope':'independently transcribed exact circular arcs and polygon coordinates; finite checks supplement proof',
      'orientations':3600,'sector_contacts':sector_checks,
      'reuleaux_width_range':[min(widths),max(widths)],
      'marked_support_distance_range':[min(heights),max(heights)],
      'ellipse_width_range':[min(ellipse),max(ellipse)],
      'square_width_range':[min(square),max(square)],
      'triangle_width_range':[min(triangle),max(triangle)],
      'exact_perimeters':{'disk':'pi*w','three_60_degree_arcs':'3*(pi*w/3)=pi*w'},
      'physical_tests':'unperformed'}
out=Path(__file__).resolve().parent/'guide-review-assets';out.mkdir(exist_ok=True)
(out/'independent-guide-checks.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
