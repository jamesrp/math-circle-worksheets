"""Independent exact (rational) nearest-site computations for Week 15.
Closed cells: a point belongs to every nearest site."""
import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.normpath(_os.path.join(HERE, '..', '..', '..', '..'))
from fractions import Fraction as F
from itertools import combinations
import math

def Fr(v): return v if isinstance(v,F) else F(str(v))
def d2(p,q): return (Fr(p[0])-Fr(q[0]))**2+(Fr(p[1])-Fr(q[1]))**2

def nearest(p,sites):
    d={n:d2(p,q) for n,q in sites.items()}
    m=min(d.values())
    return ''.join(sorted(n for n in d if d[n]==m))

def halfplane(a,b):
    """closed half-plane of points at least as close to a as to b: u.x <= c"""
    ax,ay=map(Fr,a);bx,by=map(Fr,b)
    return (2*(bx-ax),2*(by-ay),bx*bx+by*by-ax*ax-ay*ay)

def clip(poly,hp):
    u,v,c=hp
    f=lambda p:u*p[0]+v*p[1]-c
    out=[]
    n=len(poly)
    for i in range(n):
        p,q=poly[i],poly[(i+1)%n]
        fp,fq=f(p),f(q)
        if fp<=0: out.append(p)
        if (fp<0<fq) or (fq<0<fp):
            t=fp/(fp-fq); out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    # dedupe consecutive
    ded=[]
    for p in out:
        if not ded or ded[-1]!=p: ded.append(p)
    if len(ded)>1 and ded[0]==ded[-1]: ded.pop()
    return ded

def cell(sites,name,M=1000):
    poly=[(F(-M),F(-M)),(F(M),F(-M)),(F(M),F(M)),(F(-M),F(M))]
    for n,q in sites.items():
        if n!=name: poly=clip(poly,halfplane(sites[name],q))
    return poly

def bounded(sites,name,M=1000):
    return all(abs(x)<M and abs(y)<M for x,y in cell(sites,name,M))

def frame_cell(sites,name,B=3):
    return cell(sites,name,B)

def shared(sites,i,j,M=10**6):
    """Return the set of points where i and j are both nearest: None, a point, or a segment/ray (endpoints, with M meaning infinite)."""
    a=sites[i];b=sites[j]
    ax,ay=map(Fr,a);bx,by=map(Fr,b)
    mx,my=(ax+bx)/2,(ay+by)/2
    dx,dy=-(by-ay),(bx-ax)  # direction of bisector
    lo,hi=F(-M),F(M)
    for k,c in sites.items():
        if k in (i,j): continue
        u,v,cc=halfplane(a,c)  # need point at least as close to a as to c
        # point = (mx+t dx, my+t dy); u*(mx+t dx)+v*(my+t dy) <= cc
        coef=u*dx+v*dy; const=u*mx+v*my-cc
        if coef==0:
            if const>0: return None
        elif coef>0: hi=min(hi,-const/coef)
        else: lo=max(lo,-const/coef)
        if lo>hi: return None
    P=lambda t:(mx+t*dx,my+t*dy)
    inf=lambda t: abs(t)>=M
    return (None if inf(lo) else P(lo), None if inf(hi) else P(hi), lo==hi)

def vertices(sites):
    """All points with >=3 nearest sites."""
    pts={}
    names=list(sites)
    for i,j,k in combinations(names,3):
        # circumcenter
        (ax,ay),(bx,by),(cx,cy)=[tuple(map(Fr,sites[n])) for n in (i,j,k)]
        D=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
        if D==0: continue
        ux=((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)*(ay-by))/D
        uy=((ax*ax+ay*ay)*(cx-bx)+(bx*bx+by*by)*(ax-cx)+(cx*cx+cy*cy)*(bx-ax))/D
        nn=nearest((ux,uy),sites)
        if len(nn)>=3: pts[(ux,uy)]=nn
    return pts

def fmt(p):
    if p is None: return 'inf'
    return '('+','.join(str(v) for v in p)+')'
def fmtpoly(poly): return ' '.join(fmt(p) for p in poly)

def report(title,sites,probes=()):
    print('====',title,sites)
    for n in sites:
        b=bounded(sites,n)
        print(f'  cell {n}: bounded={b}; in frame: {fmtpoly(frame_cell(sites,n))}')
        if b: print('     whole cell:',fmtpoly(cell(sites,n)))
    for i,j in combinations(list(sites),2):
        s=shared(sites,i,j)
        if s is None: print(f'  {i}{j}: no shared point')
        else:
            lo,hi,pt=s
            print(f'  {i}{j}: {"single point" if pt else "edge/ray"} from {fmt(lo)} to {fmt(hi)}')
    print('  vertices (>=3 nearest):',{fmt(k):v for k,v in vertices(sites).items()})
    if probes:
        from collections import Counter
        labs=[]
        for p in probes:
            nn=nearest(p,sites)
            ds={n:math.sqrt(float(d2(p,q))) for n,q in sites.items()}
            srt=sorted(ds.values())
            margin=srt[1]-srt[0]
            labs.append(nn)
            print(f'    probe {p}: {nn}   margin(2nd-1st, map units)={margin:.3f}  in={margin*0.9667:.3f}')
        print('  counts',Counter(labs))
