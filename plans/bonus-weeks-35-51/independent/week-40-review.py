"""Independent local-color, arc-incidence, cord and geometric checks."""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json
colors=range(3)
def legal(a,b,c):return len({a,b,c}) in [1,3]
def machine(a,b):
    candidates=[c for c in colors if legal(a,b,c)];assert len(candidates)==1
    return b,candidates[0]
periods={}
for a,b in product(colors,repeat=2):
    p=(a,b);q=p
    for n in range(1,4):
        q=machine(*q)
        if q==p:periods[str(p)]=n;break
assert sorted(periods.values())==[1,1,1,3,3,3,3,3,3]
assert machine(0,1)==(1,2)
class UF:
    def __init__(self):self.p={}
    def find(self,x):
        if x not in self.p:self.p[x]=x
        if self.p[x]!=x:self.p[x]=self.find(self.p[x])
        return self.p[x]
    def join(self,a,b):self.p[self.find(a)]=self.find(b)
def arc_graph(ns,join_models=False):
    uf=UF();constraints=[]
    def v(m,j,kind):return (m,j,kind)
    for m,n in enumerate(ns):
        for j in range(n):
            for k in ['LI','RI','LO','RO']:uf.find(v(m,j,k))
            uf.join(v(m,j,'RI'),v(m,j,'LO')) # uninterrupted over arc
            constraints.append((v(m,j,'LI'),v(m,j,'RI'),v(m,j,'RO')))
            if j+1<n:
                uf.join(v(m,j,'LO'),v(m,j+1,'LI'));uf.join(v(m,j,'RO'),v(m,j+1,'RI'))
        if n==0: # cut plain-loop arc, with two exposed ends
            uf.join((m,'top'),(m,'bottom'))
    # Linear composition: first model keeps left closure, last keeps right;
    # neighboring models use upper-to-upper/lower-to-lower on cut returns.
    def ends(m,side):
        n=ns[m]
        if n==0:return (m,'top'),(m,'bottom')
        return v(m,0,side+'I'),v(m,n-1,side+'O')
    for m,n in enumerate(ns):
        if n:
            for side in ['L','R']:
                cut=join_models and ((side=='L' and m>0) or (side=='R' and m<len(ns)-1))
                if not cut:uf.join(*ends(m,side))
    if join_models:
        for m in range(len(ns)-1):
            rt,rb=ends(m,'R');lt,lb=ends(m+1,'L');uf.join(rt,lt);uf.join(rb,lb)
    roots=sorted(set(uf.find(x) for x in uf.p),key=str);index={x:i for i,x in enumerate(roots)}
    triples=[tuple(index[uf.find(x)] for x in t) for t in constraints]
    count=sum(all(legal(*(values[i] for i in t)) for t in triples) for values in product(colors,repeat=len(roots)))
    return {'arc_count':len(roots),'triples':triples,'colorings':count}
closures={n:arc_graph([n]) for n in [1,2,3,4,6]}
assert [closures[n]['colorings'] for n in closures]==[3,3,9,3,9]
joined={str(ns):arc_graph(ns,True) for ns in [[3,3],[3,0],[3,3,3]]}
assert [joined[k]['colorings'] for k in joined]==[27,9,81]
# Cord connectivity ignores underpass splitting: endpoints follow both strands.
def components(ns):
    uf=UF()
    for m,n in enumerate(ns):
        for j in range(n):
            for k in ['LI','RI','LO','RO']:uf.find((m,j,k))
            uf.join((m,j,'LI'),(m,j,'RO'));uf.join((m,j,'RI'),(m,j,'LO'))
            if j+1<n:
                for side in ['L','R']:uf.join((m,j,side+'O'),(m,j+1,side+'I'))
        for side in ['L','R']:uf.join((m,0,side+'I'),(m,n-1,side+'O'))
    return len(set(uf.find(x) for x in uf.p))
assert [components([n]) for n in closures]==[1,2,1,2,2]
# Actual full centerline segments: exact intersection checks include hidden underpasses.
def polyline(points):return list(zip(points,points[1:]))
def geometry(cx,yt,n,cutleft=False,cutright=False):
    xl=F(cx)-35;xr=F(cx)+35;yb=F(yt)-35*n;segments=[]
    for j in range(n):
        top=F(yt)-35*j;bottom=top-35
        segments.extend([((xl,top),(xr,bottom)),((xr,top),(xl,bottom))])
    for x,out,cut in [(xl,xl-30,cutleft),(xr,xr+30,cutright)]:
        segments+=polyline([(x,F(yt)),(x,F(yt)+15),(out,F(yt)+15)])
        segments+=polyline([(out,yb-15),(x,yb-15),(x,yb)])
        if cut:
            high=F(yt)-32;low=F(yt)-58
            segments+=[((out,F(yt)+15),(out,high)),((out,low),(out,yb-15))]
        else:segments+=[((out,F(yt)+15),(out,yb-15))]
    return segments
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def strict_intersection(s,t):
    a,b=s;c,d=t;r=sub(b,a);q=sub(d,c);den=cross(r,q)
    if not den:return None
    u=cross(sub(c,a),q)/den;v=cross(sub(c,a),r)/den
    if 0<u<1 and 0<v<1:return a[0]+u*r[0],a[1]+u*r[1]
def intersections(segments):
    return sorted([strict_intersection(s,t) for i,s in enumerate(segments) for t in segments[i+1:] if strict_intersection(s,t)],key=str)
geometric={}
for cx,yt,n in [(115,557,1),(306,557,2),(495,557,3),(190,323,4),(435,323,6)]:
    got=intersections(geometry(cx,yt,n));expected=sorted([(F(cx),F(yt)-F(35,2)-35*j) for j in range(n)],key=str)
    assert got==expected;geometric[str(n)]=[list(map(str,p)) for p in got]
yt=445;segs=geometry(135,yt,3,cutright=True)+geometry(475,yt,3,cutleft=True)+[((F(200),F(yt)-32),(F(410),F(yt)-32)),((F(200),F(yt)-58),(F(410),F(yt)-58))]
assert len(intersections(segs))==6
yt=244;high=F(yt)-32;low=F(yt)-58;segs=geometry(135,yt,3,cutright=True)+polyline([(F(410),high),(F(410),F(yt)+15),(F(525),F(yt)+15),(F(525),F(yt)-120),(F(410),F(yt)-120),(F(410),low)])+[((F(200),high),(F(410),high)),((F(200),low),(F(410),low))]
assert len(intersections(segs))==3
result={'ordered_pair_periods':periods,'closure_arc_enumerations':closures,'closure_cords':{n:components([n]) for n in closures},'joined_arc_enumerations':joined,'actual_centerline_intersections':geometric,'joined_geometric_crossings':[6,3],'worked_example':'RB -> BG; two plain cut loops -> one loop'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
