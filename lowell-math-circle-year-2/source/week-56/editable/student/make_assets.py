#!/usr/bin/env python3
"""Author-created regular-face nets; test geometry and emit portable TikZ."""
from pathlib import Path
from itertools import combinations, product
from collections import defaultdict, Counter
import math, random, json

ROOT = Path(__file__).resolve().parent
EDGE = 30.0

def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def orient(vertices, faces):
    center = tuple(sum(p[k] for p in vertices)/len(vertices) for k in range(3))
    out=[]
    for face in faces:
        f=list(face)
        n=cross(sub(vertices[f[1]],vertices[f[0]]),sub(vertices[f[2]],vertices[f[1]]))
        if dot(n,sub(vertices[f[0]],center))<0: f.reverse()
        out.append(f)
    return out

cube=list(product((0,1),repeat=3)); idx={p:i for i,p in enumerate(cube)}
cf=[]
for axis in range(3):
    other=[a for a in range(3) if a!=axis]
    for v in (0,1):
        f=[]
        for p,q in ((0,0),(1,0),(1,1),(0,1)):
            a=[0,0,0]; a[axis]=v; a[other[0]]=p; a[other[1]]=q
            f.append(idx[tuple(a)])
        cf.append(f)

models=[
 ('Cube',cube,cf,(8,12,6)),
 ('Tetrahedron',[(1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1)],list(combinations(range(4),3)),(4,6,4)),
 ('Octahedron',[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)],list(product((0,1),(2,3),(4,5))),(6,12,8)),
 ('Triangular prism',[(0,0,0),(1,0,0),(.5,math.sqrt(3)/2,0),(0,0,1),(1,0,1),(.5,math.sqrt(3)/2,1)],[(0,1,2),(3,4,5),(0,1,4,3),(1,2,5,4),(2,0,3,5)],(6,9,5)),
 ('Square pyramid',[(0,0,0),(1,0,0),(1,1,0),(0,1,0),(.5,.5,math.sqrt(.5))],[(0,1,2,3),(0,1,4),(1,2,4),(2,3,4),(3,0,4)],(5,8,5)),
]

def area(poly):
    return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1])))/2
def intersect(subject, clip):
    out=list(subject)
    for a,b in zip(clip,clip[1:]+clip[:1]):
        incoming=out; out=[]
        if not incoming: break
        def side(p): return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
        prev=incoming[-1]; ps=side(prev)
        for cur in incoming:
            cs=side(cur)
            if (cs>=-1e-8)!=(ps>=-1e-8):
                t=ps/(ps-cs)
                out.append((prev[0]+t*(cur[0]-prev[0]),prev[1]+t*(cur[1]-prev[1])))
            if cs>=-1e-8: out.append(cur)
            prev,ps=cur,cs
    return out
def ccw(poly):
    signed=sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1]))
    return poly if signed>0 else list(reversed(poly))
def overlap(a,b): return area(intersect(a,ccw(b)))>1e-6
def fresh_poly(n):
    p=[(0.,0.),(EDGE,0.)]; ang=0
    for i in range(2,n):
        ang+=2*math.pi/n
        p.append((p[-1][0]+EDGE*math.cos(ang),p[-1][1]+EDGE*math.sin(ang)))
    return p
def attach(face, a,b,pa,pb):
    # This face traverses b->a, opposite its already placed neighbor.
    j=face.index(b); f=face[j:]+face[:j]
    assert f[1]==a
    p={b:pb,a:pa}; angle=math.atan2(pa[1]-pb[1],pa[0]-pb[0])
    cur=pa
    for v in f[2:]:
        angle+=2*math.pi/len(face)
        cur=(cur[0]+EDGE*math.cos(angle),cur[1]+EDGE*math.sin(angle));p[v]=cur
    return p
def tab(a,b):
    # Six mm outside the face, with tapered ends.
    dx=(b[0]-a[0])/EDGE;dy=(b[1]-a[1])/EDGE
    nx=dy;ny=-dx
    return ccw([a,b,(b[0]-4*dx+6*nx,b[1]-4*dy+6*ny),(a[0]+4*dx+6*nx,a[1]+4*dy+6*ny)])
def find_net(faces, seed):
    incid=defaultdict(list)
    for i,f in enumerate(faces):
        for a,b in zip(f,f[1:]+f[:1]): incid[tuple(sorted((a,b)))].append(i)
    assert all(len(v)==2 for v in incid.values())
    adjacency=defaultdict(list)
    for e,(i,j) in incid.items(): adjacency[i].append((j,e));adjacency[j].append((i,e))
    rng=random.Random(seed); best=None
    for attempt in range(14000):
        root=attempt%len(faces)
        maps={root:dict(zip(faces[root],fresh_poly(len(faces[root]))))};tree=set()
        valid=True
        while len(maps)<len(faces):
            choices=[(i,j,e) for i in maps for j,e in adjacency[i] if j not in maps]
            rng.shuffle(choices);added=False
            for i,j,e in choices:
                f=faces[i];a,b=e
                if f[(f.index(a)+1)%len(f)]!=b:a,b=b,a
                m=attach(faces[j],a,b,maps[i][a],maps[i][b]);p=[m[v] for v in faces[j]]
                if any(overlap(p,[mi[v] for v in faces[k]]) for k,mi in maps.items()): continue
                maps[j]=m;tree.add(e);added=True;break
            if not added:valid=False;break
        if not valid:continue
        boundary=[e for e in incid if e not in tree];tabs={};ok=True
        polygons=[[maps[i][v] for v in f] for i,f in enumerate(faces)]
        for e in boundary:
            opts=[]
            for i in incid[e]:
                f=faces[i];a,b=e
                if f[(f.index(a)+1)%len(f)]!=b:a,b=b,a
                t=tab(maps[i][a],maps[i][b])
                if any(overlap(t,p) for p in polygons):continue
                if any(overlap(t,old[1]) for old in tabs.values()):continue
                opts.append((i,t))
            if not opts:ok=False;break
            tabs[e]=opts[0]
        if not ok:continue
        points=[p for poly in polygons for p in poly]+[p for _,t in tabs.values() for p in t]
        minx=min(p[0] for p in points);maxx=max(p[0] for p in points)
        miny=min(p[1] for p in points);maxy=max(p[1] for p in points)
        w,h=maxx-minx,maxy-miny
        score=w*h+max(w,h)*20
        if max(w,h)>150:continue
        if best is None or score<best[0]:best=(score,maps,tree,tabs,(minx,miny,w,h),incid)
    if best is None:raise RuntimeError('No nonoverlapping tabbed net found')
    return best[1:]

def coord(p):return '(%.5f,%.5f)'%p
def emit_net(name, vertices, faces, expected, seed):
    faces=orient(vertices,faces)
    maps,tree,tabs,bounds,incid=find_net(faces,seed)
    # Favor landscape nets, preserving regular geometry and upright node text.
    if bounds[3] > bounds[2]:
        maps={i:{v:(p[1],-p[0]) for v,p in m.items()} for i,m in maps.items()}
        tabs={e:(i,[(p[1],-p[0]) for p in t]) for e,(i,t) in tabs.items()}
        pts=[p for m in maps.values() for p in m.values()]+[p for _,t in tabs.values() for p in t]
        bounds=(min(p[0] for p in pts),min(p[1] for p in pts),max(p[0] for p in pts)-min(p[0] for p in pts),max(p[1] for p in pts)-min(p[1] for p in pts))
    V,E,F=len(vertices),len(incid),len(faces)
    assert (V,E,F)==expected
    contributions=[[] for _ in vertices]
    lengths=[]
    for f in faces:
        for i,v in enumerate(f):
            u,w=f[i-1],f[(i+1)%len(f)]
            a,b=sub(vertices[u],vertices[v]),sub(vertices[w],vertices[v])
            angle=math.degrees(math.acos(dot(a,b)/math.sqrt(dot(a,a)*dot(b,b))))
            contributions[v].append(angle)
    gaps=[360-sum(a) for a in contributions]
    assert abs(sum(gaps)-720)<1e-7
    letters={e:chr(65+j) for j,e in enumerate(sorted(tabs))}
    lines=['\\begin{tikzpicture}[x=1mm,y=1mm,line width=.55pt,font=\\sffamily\\scriptsize]']
    for i,f in enumerate(faces):
        poly=[maps[i][v] for v in f]
        lines.append('\\fill[blue!5] '+ ' -- '.join(coord(p) for p in poly)+' -- cycle;')
    for e,(i,t) in tabs.items():
        lines.append('\\fill[gray!17] '+' -- '.join(coord(p) for p in t)+' -- cycle;')
        # The fourth edge is the tab hinge: draw its dash only in the face loop.
        lines.append('\\draw '+' -- '.join(coord(p) for p in (t[3],t[0],t[1],t[2]))+';')
    done=set()
    for i,f in enumerate(faces):
        for a,b in zip(f,f[1:]+f[:1]):
            e=tuple(sorted((a,b)));pa,pb=maps[i][a],maps[i][b]
            if e in tree:
                if e in done:continue
                done.add(e);lines.append('\\draw[dashed] '+coord(pa)+' -- '+coord(pb)+';')
            elif tabs[e][0]==i:
                lines.append('\\draw[dashed] '+coord(pa)+' -- '+coord(pb)+';')
            else:lines.append('\\draw '+coord(pa)+' -- '+coord(pb)+';')
            if e in letters:
                mx,my=(pa[0]+pb[0])/2,(pa[1]+pb[1])/2
                dx,dy=(pb[0]-pa[0])/EDGE,(pb[1]-pa[1])/EDGE
                off=-3 if tabs[e][0]==i else 3
                lines.append('\\node[fill=white,inner sep=.3pt] at '+coord((mx-dy*off,my+dx*off))+' {'+letters[e]+'};')
        cx=sum(maps[i][v][0] for v in f)/len(f);cy=sum(maps[i][v][1] for v in f)/len(f)
        lines.append('\\node[font=\\sffamily\\small] at '+coord((cx,cy))+' {'+str(i+1)+'};')
        for v in f:
            p=maps[i][v];vx=cx-p[0];vy=cy-p[1];l=math.hypot(vx,vy)
            lines.append('\\node[text=blue!60!black,font=\\sffamily\\tiny] at '+coord((p[0]+vx*3.2/l,p[1]+vy*3.2/l))+' {'+str(v+1)+'};')
    lines+=['\\end{tikzpicture}']
    for i,f in enumerate(faces):
        for a,b in zip(f,f[1:]+f[:1]):
            lengths.append(math.dist(maps[i][a],maps[i][b]))
    assert all(abs(x-30)<1e-7 for x in lengths)
    # Polygon and tab intersections were screened during selection; repeat on final choice.
    polys=[[maps[i][v] for v in f] for i,f in enumerate(faces)]
    assert not any(overlap(a,b) for a,b in combinations(polys,2))
    assert not any(overlap(t,p) for _,t in tabs.values() for p in polys)
    assert not any(overlap(a[1],b[1]) for a,b in combinations(tabs.values(),2))
    key=name.lower().replace(' ','-')
    (ROOT/(key+'-net.tex')).write_text('\n'.join(lines)+'\n')
    return dict(name=name,V=V,E=E,F=F,vertex_face_angles=contributions,gaps=gaps,total_gap=sum(gaps),
                printed_edge_mm=30,net_bounds_mm=bounds,face_overlap=False,tab_overlap=False,
                boundary_seam_pairs=len(tabs),hinged_edges=len(tree),faces=faces)

if __name__=='__main__':
    checks=[emit_net(*m, seed=560+i) for i,m in enumerate(models)]
    (ROOT/'geometry-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
    print('Verified 5 closed models, 30 mm net edges, nonoverlapping faces/tabs, seam pairings and angle totals.')
