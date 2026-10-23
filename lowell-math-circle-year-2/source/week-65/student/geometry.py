"""Week 65 geometry: the regular hyperbolic {8,4} tiling in the Poincare disk.

Carried over unchanged from the old student builder (archive-before-problem-files-2026-10-23/
build.py), with CORNER_ROOMS and ROOMS_AROUND_HOME added for Problem 6's map (v4).
student/build.py checks it (verify) and ../figures.py draws the student pages with it, so
the pages and the checks use one construction.
"""
from math import sqrt, pi, cos, sin, atan2, acos, acosh
import cmath

R = sqrt(sqrt(2)-1)
V = [R*cmath.exp(1j*(pi/8+k*pi/4)) for k in range(8)]

def circle(p,q):
    det=p.real*q.imag-p.imag*q.real
    if abs(det)<1e-11: return None
    a=(abs(p)**2+1)/2; b=(abs(q)**2+1)/2
    c=complex((a*q.imag-p.imag*b)/det,(p.real*b-a*q.real)/det)
    return c,abs(c)**2-1

def reflect(z,p,q):
    cr=circle(p,q)
    if cr is None:
        d=q-p; return d/d.conjugate()*z.conjugate()
    c,r2=cr; return c+r2/(z-c).conjugate()

def key(z): return (round(z.real,8),round(z.imag,8))
def n(z): return f'({z.real:.9f},{z.imag:.9f})'

def path(p,q):
    cr=circle(p,q)
    if cr is None: return '-- '+n(q)
    c,r2=cr
    a=cmath.phase(p-c); b=cmath.phase(q-c)
    d=(b-a+pi)%(2*pi)-pi
    return f'arc[start angle={a*180/pi:.9f},delta angle={d*180/pi:.9f},radius={sqrt(r2):.9f}]'

def edge(p,q,style='black,line width=0.8pt'):
    return f'\\draw[{style}] {n(p)} '+path(p,q)+';\n'

def polygon(v,style):
    return f'\\path[{style}] '+n(v[0])+' '+ ' '.join(path(v[k],v[(k+1)%len(v)]) for k in range(len(v)))+' -- cycle;\n'

def full_ends(p,q):
    cr=circle(p,q)
    if cr is None:
        e=(q-p)/abs(q-p); return -e,e
    c,r2=cr; e=c/abs(c); h=sqrt(1-1/abs(c)**2)
    return e/abs(c)+1j*e*h,e/abs(c)-1j*e*h

def point(p,label=None,where='above right',style='black',rad='1.8pt'):
    out=f'\\fill[{style}] {n(p)} circle[radius={rad}];\n'
    if label: out+=f'\\node[{where},inner sep=3pt,font=\\sffamily\\bfseries\\normalsize,fill=white] at {n(p)} {{{label}}};\n'
    return out

def tangent(p,q):
    cr=circle(p,q)
    if cr is None: return (q-p)/abs(q-p)
    c,r2=cr; v=1j*(p-c); v/=abs(v)
    if (v.conjugate()*(q-p)).real<0: v=-v
    return v

# Exact isometry centered on the hyperbolic midpoint of side 7.
MIDPOINT = 2**0.25 - R
PAIR_SCALE = 3.6
SINGLE_SCALE = 3.23

def pair_view(z): return (z-MIDPOINT)/(1-MIDPOINT*z)
LEFT = [pair_view(z) for z in V]
RIGHT = [-z.conjugate() for z in LEFT]
BOUNDARY = LEFT + [RIGHT[k] for k in range(6,0,-1)]
SQUARE_BOUNDARY = [1+1j, 0+1j, 0j, 1+0j, 2+0j, 2+1j]

def extend(p,q,distance):
    """Continue beyond p, away from q, along its actual geodesic.
    distance is Euclidean arc length in disk units, for visual stub size only.
    """
    cr=circle(p,q)
    direction=-tangent(p,q)
    if cr is None: return p+distance*direction
    c,r2=cr
    turn=1 if ((1j*(p-c)).conjugate()*direction).real>0 else -1
    return c+(p-c)*cmath.exp(1j*turn*distance/sqrt(r2))

def stubs(polys,distance=.08):
    s=''; seen=set()
    for poly in polys:
        for k,p in enumerate(poly):
            q=poly[(k+1)%len(poly)]
            for a,b in ((p,q),(q,p)):
                e=extend(a,b,distance)
                ek=(key(a),key(e))
                if ek not in seen:
                    seen.add(ek)
                    s+=edge(a,e,'black!55,line width=.65pt')
    return s

def local_turns(poly,curved=True):
    angles=[]
    for k,z in enumerate(poly):
        prev,nxt=poly[(k-1)%len(poly)],poly[(k+1)%len(poly)]
        arrival=-tangent(z,prev) if curved else (z-prev)/abs(z-prev)
        departure=tangent(z,nxt) if curved else (nxt-z)/abs(nxt-z)
        angles.append(cmath.phase(departure/arrival)*180/pi)
    return angles

def min_separation(points,scale):
    return min(abs(z-w) for i,z in enumerate(points) for w in points[i+1:])*scale*25.4

def arc_length(p,q):
    cr=circle(p,q)
    if cr is None: return abs(q-p)
    c,r2=cr
    return abs(cmath.phase((q-c)/(p-c)))*sqrt(r2)

TILES=[(0j,V,0)]; INDEX={key(0j):0}; ADJ={}
for i,(center,poly,depth) in enumerate(TILES):
    ADJ.setdefault(i,set())
    if depth>=2: continue
    for k in range(8):
        p,q=poly[k],poly[(k+1)%8]
        z=reflect(center,p,q); zkey=key(z)
        if zkey not in INDEX:
            INDEX[zkey]=len(TILES)
            TILES.append((z,[reflect(w,p,q) for w in poly],depth+1))
        j=INDEX[zkey];ADJ[i].add(j);ADJ.setdefault(j,set()).add(i)

P=V[0]
def mob(z): return (z-P)/(1-P.conjugate()*z)
ROT=-cmath.exp(-1j*cmath.phase(mob(V[1])))
def corner_view(z): return ROT*mob(z)
FOUR=[i for i,(_,poly,_) in enumerate(TILES) if any(abs(z-P)<1e-7 for z in poly)]
# Determine names by actual adjacency, rather than by generation-order guesses.
HOME=0
NEIGHBORS=sorted(ADJ[HOME].intersection(FOUR))
STAR=next(i for i in FOUR if i!=0 and i not in NEIGHBORS)
# A occupies the upper-left quadrant in the recentered map; B lower-right.
A=next(i for i in NEIGHBORS if corner_view(TILES[i][0]).imag>0)
B=next(i for i in NEIGHBORS if i!=A)
NAMES={HOME:'Home', A:'A', B:'B', STAR:r'$\star$'}
# Problem 6's map (v4): Home's 8 side neighbours, then the 8 corner rooms, which share
# only a corner with Home (each is adjacent to two neighbours).
CORNER_ROOMS=sorted(i for i,(_,poly,_) in enumerate(TILES)
    if i!=HOME and i not in ADJ[HOME] and any(abs(z-v)<1e-7 for z in poly for v in V))
ROOMS_AROUND_HOME=sorted(ADJ[HOME])+CORNER_ROOMS
