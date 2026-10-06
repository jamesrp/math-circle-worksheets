#!/usr/bin/env python3
"""Independent standard-library geometry checks for the Week65 construction.

This recomputes the construction rather than importing the student builder.
Finite numerical checks supplement the exact arguments in the guide.
"""
import cmath,json,math
from collections import Counter,defaultdict
from pathlib import Path
TOL=1e-7
r=math.sqrt(math.sqrt(2)-1)
base=[cmath.rect(r,math.pi/8+k*math.pi/4) for k in range(8)]
def circle(a,b):
 d=a.real*b.imag-a.imag*b.real
 if abs(d)<1e-12:return None
 u=(abs(a)**2+1)/2;v=(abs(b)**2+1)/2
 c=complex((u*b.imag-v*a.imag)/d,(a.real*v-b.real*u)/d)
 return c,math.sqrt(abs(c)**2-1)
def reflection(z,a,b):
 cr=circle(a,b)
 if cr is None:
  d=(b-a)/abs(b-a);return d*d*z.conjugate()
 c,s=cr;return c+s*s/(z-c).conjugate()
def vertex_key(poly):return tuple(sorted((round(z.real,8),round(z.imag,8)) for z in poly))
def center_key(c):return round(c.real,8),round(c.imag,8)
polys=[base];depths=[0];centers=[0j];by_vertices={vertex_key(base):0};by_centers={center_key(0j):0};adj=defaultdict(set)
for k,p in enumerate(polys):
 if depths[k]==2:continue
 for i in range(8):
  a,b=p[i],p[(i+1)%8]
  q=[reflection(z,a,b) for z in p];c=reflection(centers[k],a,b)
  key=vertex_key(q);ckey=center_key(c)
  assert (key in by_vertices)==(ckey in by_centers)
  if key not in by_vertices:
   by_vertices[key]=len(polys);by_centers[ckey]=len(polys)
   polys.append(q);centers.append(c);depths.append(depths[k]+1)
  j=by_vertices[key];assert j==by_centers[ckey]
  adj[k].add(j);adj[j].add(k)
assert Counter(depths)=={0:1,1:8,2:48}
inc=Counter(j for i in adj[0] for j in adj[i] if j!=0)
assert Counter(inc.values())=={1:40,2:8}
# Independent tangent test: rotate the two radius vectors by i.
angle_errors=[];orthogonal_errors=[];edge_lengths=[]
for p in polys:
 assert len(p)==8 and len(vertex_key(p))==8
 for i,z in enumerate(p):
  c1,s1=circle(p[(i-1)%8],z);c2,s2=circle(z,p[(i+1)%8])
  dot=((z-c1).conjugate()*(z-c2)).real/(s1*s2)
  angle_errors.append(abs(dot))
  orthogonal_errors.extend([abs(abs(c1)**2-s1*s1-1),abs(abs(c2)**2-s2*s2-1)])
  w=p[(i+1)%8]
  edge_lengths.append(math.acosh(1+2*abs(z-w)**2/((1-abs(z)**2)*(1-abs(w)**2))))
assert max(angle_errors)<TOL,max(angle_errors)
assert max(orthogonal_errors)<TOL
assert max(edge_lengths)-min(edge_lengths)<TOL
# Count four distinct tile corners at the chosen launch point.
P=base[0]
around=[i for i,p in enumerate(polys) if any(abs(z-P)<TOL for z in p)]
assert len(around)==4
# Verify shared destinations are all and only the opposite rooms at home corners.
for v in base:
 around_v=[i for i,p in enumerate(polys) if any(abs(z-v)<TOL for z in p)]
 assert len(around_v)==4
 assert Counter(depths[i] for i in around_v)=={0:1,1:2,2:1}
 dest=next(i for i in around_v if depths[i]==2)
 assert inc[dest]==2
# Exact inequality reduction: (C/sqrt(2))**2-r**2 = 1-sqrt(2)/2 > 0.
C=2**.25
assert 1-math.sqrt(2)/2>0
for i,expected in [(0,cmath.rect(C,math.pi/4)),(7,complex(C,0)),(3,complex(-C,0))]:
 c,s=circle(base[i],base[(i+1)%8]);assert abs(c-expected)<TOL and abs(s-r)<TOL
blue=circle(base[0],base[1]);green=circle(base[7],base[0]);red=circle(base[3],base[4])
assert red[0].real+red[1]<0<min(blue[0].real-blue[1],green[0].real-green[1])
# Repeated next-edge-and-left steering follows all eight oriented base edges.
# The polygon is counterclockwise; orientation at each turn checked using tangents.
def tangent_toward(a,b):
 c,s=circle(a,b);t=1j*(a-c)
 if (t.conjugate()*(b-a)).real<0:t=-t
 return t/abs(t)
for i,v in enumerate(base):
 incoming=-tangent_toward(v,base[(i-1)%8]);outgoing=tangent_toward(v,base[(i+1)%8])
 turn=cmath.phase(outgoing/incoming)
 assert abs(turn-math.pi/2)<TOL,turn
assert abs(base[4]-base[0])>1 and abs(base[(0+8)%8]-base[0])<TOL
report={"layers":dict(Counter(depths)),"two_step_routes":sum(inc.values()),"destination_multiplicities":dict(Counter(inc.values())),"tile_count_checked":len(polys),"eight_vertices_per_tile":True,"four_tiles_at_home_vertices":True,"max_right_angle_cosine_error":max(angle_errors),"max_circle_orthogonality_error":max(orthogonal_errors),"hyperbolic_edge_length_spread":max(edge_lengths)-min(edge_lengths),"two_whole_roads_disjoint_from_red":True,"eight_left_turns_restore_position_and_heading":True,"four_left_turns_do_not_close":True}
# Independently check the added two-room boundary in the midpoint-centered view.
m=C-r
left=[(z-m)/(1-m*z) for z in base]
right=[-z.conjugate() for z in left]
boundary=left+list(reversed(right[1:7]))
assert len(boundary)==14
turns=[]
for i,z in enumerate(boundary):
 incoming=-tangent_toward(z,boundary[i-1])
 outgoing=tangent_toward(z,boundary[(i+1)%14])
 turns.append(cmath.phase(outgoing/incoming)*180/math.pi)
assert Counter(round(t/90) for t in turns)=={0:2,1:12}
assert abs(turns[0])<TOL and abs(turns[7])<TOL
scale=3.6
separation=min(abs(a-b)*scale*25.4 for i,a in enumerate(boundary) for b in boundary[i+1:])
assert abs(separation-17.850196284)<1e-7
report['two_room_boundary']={'edge_moves':14,'quarter_turns':12,'straight_junctions':2,'start_and_finish_straight':True,'printed_width_inches':(max(z.real for z in boundary)-min(z.real for z in boundary))*scale,'printed_height_inches':(max(z.imag for z in boundary)-min(z.imag for z in boundary))*scale,'minimum_junction_separation_mm':separation}
square=[1+1j,1j,0j,1+0j,2+0j,2+1j]
sturns=[cmath.phase((square[(i+1)%6]-z)/(z-square[i-1]))*180/math.pi for i,z in enumerate(square)]
assert Counter(round(t/90) for t in sturns)=={0:2,1:4}
report['two_square_boundary']={'edge_moves':6,'quarter_turns':4,'straight_junctions':2}
print(json.dumps(report,indent=2))
