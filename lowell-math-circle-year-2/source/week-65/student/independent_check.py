#!/usr/bin/env python3
"""Independent mathematical audit; no imports from author/checker code.
Adapted by the reviser from the separate mathematical reviewer's audit for v2.
Reconstructs tiles by Lorentzian reflections, checks drawn TikZ arcs independently,
and produces two-room construction data. Only writes inside this audit directory.
"""
import cmath, itertools, json, math, re
from collections import Counter, deque
from pathlib import Path
ROOT=Path(__file__).resolve().parent
RUN=ROOT.parent
TOL=2e-7
pi=math.pi
r=math.sqrt(math.sqrt(2)-1)
C=2**0.25
V=[r*cmath.exp(1j*(pi/8+k*pi/4)) for k in range(8)]

def ld(a,b): return -a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def L(z):
    s=1-abs(z)**2
    return ((1+abs(z)**2)/s,2*z.real/s,2*z.imag/s)
def D(v): return complex(v[1],v[2])/(v[0]+1)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def reflect(w,u,v):
    a,b=L(u),L(v)
    n=cross((-a[0],a[1],a[2]),(-b[0],b[1],b[2]))
    z=L(w); f=2*ld(z,n)/ld(n,n)
    return D(tuple(z[k]-f*n[k] for k in range(3)))
def pk(z):return (round(z.real,8),round(z.imag,8))
def polykey(poly):return tuple(sorted(pk(z) for z in poly))
def edgekey(p,q):return tuple(sorted((pk(p),pk(q))))
def edges(poly):return {edgekey(poly[k],poly[(k+1)%len(poly)]) for k in range(len(poly))}
def center_radius(p,q):
    # Solving two Euclidean bisector equations derived from boundary orthogonality.
    det=p.real*q.imag-p.imag*q.real
    if abs(det)<1e-10:return None
    h=(1+abs(p)**2)/2; j=(1+abs(q)**2)/2
    c=complex((h*q.imag-j*p.imag)/det,(j*p.real-h*q.real)/det)
    return c,math.sqrt(abs(c)**2-1)
def tangent(p,q):
    cr=center_radius(p,q)
    if cr is None:return (q-p)/abs(q-p)
    c,s=cr
    t=1j*(p-c)/s
    if (t.conjugate()*(q-p)).real<0:t=-t
    return t

def signed_turn(prev,p,nxt):
    incoming=-tangent(p,prev);outgoing=tangent(p,nxt)
    return cmath.phase(outgoing/incoming)*180/pi

def edge_samples(p,q,n=1000):
    cr=center_radius(p,q)
    if cr is None:return [p+(q-p)*k/n for k in range(n+1)]
    c,s=cr;a=cmath.phase(p-c);d=cmath.phase((q-c)/(p-c))
    return [c+s*cmath.exp(1j*(a+d*k/n)) for k in range(n+1)]
def arc_length(p,q):
    cr=center_radius(p,q)
    if cr is None:return abs(q-p)
    c,s=cr;return s*abs(cmath.phase((q-c)/(p-c)))

# Independently enumerate all finite directed grid walks on the actual -3..3 board.
grid={}
steps=[(1,0),(0,1),(-1,0),(0,-1)]
for n in (4,6,8):
    valid=[]
    for turns in itertools.product((-1,0,1),repeat=n):
        x=y=0;d=0;legal=True
        for t in turns:
            dx,dy=steps[d];x+=dx;y+=dy
            if not(-3<=x<=3 and -3<=y<=3):legal=False;break
            d=(d+t)%4
        if legal and (x,y,d)==(0,0,0):valid.append(turns)
    grid[n]=len(valid)
assert grid=={4:2,6:6,8:54}
for word in ('ENWS','EENWWS','EENNWWSS','ENWSENWS'):
    ds=['ENWS'.index(c) for c in word];x=y=0
    assert ds[0]==0
    for k,d in enumerate(ds):
        dx,dy=steps[d];x+=dx;y+=dy
        assert max(abs(x),abs(y))<=3
        assert (ds[(k+1)%len(ds)]-d)%4!=2
    assert (x,y)==(0,0)

# Lorentz-reflect a regular octagon; deduplicate polygons (not just centers).
tiles=[V];centers=[0j];depth=[0];seen={polykey(V):0}
for j,poly in enumerate(tiles):
    if depth[j]==2:continue
    for k in range(8):
        u,v=poly[k],poly[(k+1)%8]
        new=[reflect(z,u,v) for z in poly];key=polykey(new)
        if key not in seen:
            seen[key]=len(tiles);tiles.append(new)
            centers.append(reflect(centers[j],u,v));depth.append(depth[j]+1)
edge_sets=[edges(poly) for poly in tiles]
adj={j:{k for k in range(len(tiles)) if k!=j and len(edge_sets[j]&edge_sets[k])==1} for j in range(len(tiles))}
for j in range(len(tiles)):
    for k in range(j):assert len(edge_sets[j]&edge_sets[k])<=1
layers=Counter(depth)
assert layers=={0:1,1:8,2:48}
assert len({pk(c) for c in centers})==len(tiles)
counts=Counter(k for j in adj[0] for k in adj[j] if k!=0)
assert Counter(counts.values())=={1:40,2:8}
assert all(depth[k]==2 for k in counts)
all_angles=[];all_lengths=[]
for poly in tiles:
    for k,p in enumerate(poly):
        u=tangent(p,poly[k-1]);v=tangent(p,poly[(k+1)%8])
        all_angles.append(math.acos(max(-1,min(1,(u.conjugate()*v).real)))*180/pi)
        all_lengths.append(math.acosh(-ld(L(p),L(poly[(k+1)%8]))))
assert max(abs(x-90) for x in all_angles)<1e-7
assert max(all_lengths)-min(all_lengths)<1e-8
local_turns=[signed_turn(V[k-1],V[k],V[(k+1)%8]) for k in range(8)]
assert max(abs(x-90) for x in local_turns)<1e-8
assert abs(V[4]+V[0])<1e-12

# Actual page-3 circles; nonadjacent defining circles are disjoint.
circles=[center_radius(V[k],V[(k+1)%8]) for k in range(8)]
assert all(abs(c-C*cmath.exp(1j*(k+1)*pi/4))<1e-12 and abs(s-r)<1e-12 for k,(c,s) in enumerate(circles))
through=[k for k,(c,s) in enumerate(circles) if abs(abs(V[0]-c)-s)<1e-10]
assert through==[0,7]
gaps={k:abs(circles[k][0]-circles[3][0])-circles[k][1]-circles[3][1] for k in through}
assert min(gaps.values())>0

# Actual four-room recentered map, names assigned spatially.
P=V[0]
f=lambda z:(z-P)/(1-P.conjugate()*z)
rot=-f(V[1]).conjugate()/abs(f(V[1]))
four=[j for j,poly in enumerate(tiles) if any(abs(z-P)<1e-7 for z in poly)]
assert len(four)==4
names={0:'H'}
for j in four:
    if j==0:continue
    c=rot*f(centers[j])
    names[j]='A' if c.real<0<c.imag else 'B' if c.imag<0<c.real else '*'
assert set(names.values())=={'H','A','B','*'}
graph={names[j]:sorted(names[k] for k in adj[j] if k in four) for j in four}
assert graph=={'H':['A','B'],'A':['*','H'],'B':['*','H'],'*':['A','B']}
room_routes={}
for n in (2,4):
    routes=[['H']]
    for _ in range(n):routes=[path+[q] for path in routes for q in graph[path[-1]]]
    room_routes[n]=[path for path in routes if path[-1]=='*']
assert {n:len(rs) for n,rs in room_routes.items()}=={2:2,4:8}

# Read the actual TikZ arc numbers, rather than assuming writer's output is sound.
tex=(ROOT/'students.tex').read_text()
pattern=r'\\draw\[[^\]]*\]\s*\(([-\d.]+),([-\d.]+)\)\s*arc\[start angle=([-\d.]+),delta angle=([-\d.]+),radius=([-\d.]+)\]'
arcs=[]
for m in re.finditer(pattern,tex):
    x,y,a,d,s=map(float,m.groups());p=complex(x,y);c=p-s*cmath.exp(1j*a*pi/180)
    q=c+s*cmath.exp(1j*(a+d)*pi/180)
    err=abs(abs(c)**2-s*s-1)
    assert err<1e-7,(p,c,s,err)
    assert max(abs(p),abs(q))<1+1e-8
    arcs.append(err)
assert len(arcs)>100

# Two side-sharing octagons, common side v7-v0. Its hyperbolic midpoint is
# the nearest-to-zero point of its supporting circle, m=C-r (real).
m=C-r
T=lambda z:(z-m)/(1-m*z)
left=[T(z) for z in V]
right=[T(reflect(z,V[7],V[0])) for z in V]
# As a cross-check, reflection becomes x -> -x in this midpoint-centered view.
assert max(abs(right[k]+left[k].conjugate()) for k in range(8))<1e-11
shared=edge_sets[0] & edges([reflect(z,V[7],V[0]) for z in V])
assert len(shared)==1
pair=[left,right]
counts_edges=Counter(edgekey(poly[k],poly[(k+1)%8]) for poly in pair for k in range(8))
assert Counter(counts_edges.values())=={1:14,2:1}
boundary_edges={e for e,v in counts_edges.items() if v==1}
# Trace the actual fourteen-edge cycle, placing both rooms on the left.
points={pk(z):z for poly in pair for z in poly}
badj={key:[] for e in boundary_edges for key in e}
for a,b in boundary_edges:badj[a].append(b);badj[b].append(a)
assert all(len(v)==2 for v in badj.values())
start=pk(left[0]);cycle=[start];prev=None;cur=start
while True:
    nxt=next(v for v in badj[cur] if v!=prev)
    if nxt==start:break
    cycle.append(nxt);prev,cur=cur,nxt
    assert len(cycle)<=14
assert len(cycle)==14
seq=[points[k] for k in cycle]
turns=[signed_turn(seq[k-1],seq[k],seq[(k+1)%14]) for k in range(14)]
if sum(turns)<0:
    cycle=[cycle[0]]+list(reversed(cycle[1:]));seq=[points[k] for k in cycle]
    turns=[signed_turn(seq[k-1],seq[k],seq[(k+1)%14]) for k in range(14)]
assert Counter(round(x/90) for x in turns)=={1:12,0:2}
assert all(abs(x/90-round(x/90))<1e-8 for x in turns)
samples=[z for k,p in enumerate(seq) for z in edge_samples(p,seq[(k+1)%14])]
bbox=[min(z.real for z in samples),max(z.real for z in samples),min(z.imag for z in samples),max(z.imag for z in samples)]
scale=3.6
lengths_mm=[arc_length(seq[k],seq[(k+1)%14])*scale*25.4 for k in range(14)]
chords_mm=[abs(seq[k]-seq[(k+1)%14])*scale*25.4 for k in range(14)]
# Square pair: rectangle with two marked middle-of-side junctions.
square=[0j,1+0j,2+0j,2+1j,1+1j,1j]
square_turns=[cmath.phase((square[(k+1)%6]-square[k])/(square[k]-square[k-1]))*180/pi for k in range(6)]
assert Counter(round(x/90) for x in square_turns)=={1:4,0:2}

result={
 'method':'Independent Lorentzian reflection construction, independent combinatorial enumerations, and actual generated TikZ arc-data audit; no author/checker code imported.',
 'square_grid_return_counts':grid,
 'central_left_turns_degrees':local_turns,
 'central_printed_arc_mm':r*pi/4*3.23*25.4,
 'central_printed_chord_mm':abs(V[1]-V[0])*3.23*25.4,
 'central_label_center_distance_mm':r*.22*3.23*25.4,
 'layers':dict(layers),'two_step_destination_multiplicity':dict(Counter(counts.values())),
 'all_reconstructed_corner_angle_range_degrees':[min(all_angles),max(all_angles)],
 'all_reconstructed_hyperbolic_side_length_range':[min(all_lengths),max(all_lengths)],
 'actual_tikz_draw_arc_count':len(arcs),'max_actual_arc_orthogonality_error':max(arcs),
 'P_on_drawn_street_numbers':through,'whole_circle_gaps':gaps,
 'whole_circle_x_gaps':{'R_max_x':-C+r,'side0_min_x':C/math.sqrt(2)-r,'side7_min_x':C-r},
 'four_room_adjacency':graph,'room_routes':room_routes,
 'two_room':{'m':m,'formula':'T(z)=(z-m)/(1-m*z), left=T(V), right=-conj(left)',
 'left_vertices':[[z.real,z.imag] for z in left],
 'boundary_ccw':[[z.real,z.imag] for z in seq],
 'boundary_local_left_turns_degrees':turns,
 'outer_edge_count':len(boundary_edges),'scale_inches_per_disk_unit':scale,
 'coordinate_bbox':bbox,'printed_bbox_inches':[(bbox[1]-bbox[0])*scale,(bbox[3]-bbox[2])*scale],
 'outer_edge_arc_lengths_mm':lengths_mm,'outer_edge_chord_lengths_mm':chords_mm,
 'minimum_distance_between_distinct_boundary_junctions_mm':min(abs(a-b)*scale*25.4 for j,a in enumerate(seq) for b in seq[j+1:])},
 'two_square':{'edge_moves':6,'quarter_turns':4,'straight_junctions':2},
}
(ROOT/'independent-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
