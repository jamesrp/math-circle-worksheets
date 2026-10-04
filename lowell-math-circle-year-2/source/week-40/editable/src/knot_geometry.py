import math,itertools,json
from pathlib import Path
TAU=2*math.pi
N=1200
pts=[(math.sin(t)+2*math.sin(2*t),math.cos(t)-2*math.cos(2*t)) for t in [TAU*i/N for i in range(N+1)]]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
xs=[]
for i in range(N):
 a=pts[i];v=sub(pts[i+1],a)
 for j in range(i+3,N):
  if i==0 and j>=N-2:continue
  b=pts[j];w=sub(pts[j+1],b);den=cross(v,w)
  if abs(den)<1e-12:continue
  d=sub(b,a);u=cross(d,w)/den;q=cross(d,v)/den
  if 0<=u<1 and 0<=q<1:
   t1=TAU*(i+u)/N;t2=TAU*(j+q)/N
   # z coordinate fixes a genuine spatial trefoil projection.
   z1=-math.sin(3*t1);z2=-math.sin(3*t2)
   xs.append({'t_under':t1 if z1<z2 else t2,'t_over':t2 if z1<z2 else t1,'point':[a[0]+u*v[0],a[1]+u*v[1]]})
assert len(xs)==3,xs
under=sorted(x['t_under'] for x in xs)
def arc(t):
 for i in range(3):
  if (t-under[i])%TAU<(under[(i+1)%3]-under[i])%TAU:return i
 raise AssertionError
crossings=[]
for c in xs:
 i=under.index(c['t_under']);crossings.append([arc(c['t_over']), (i-1)%3,i])
valid=[c for c in itertools.product(range(3),repeat=3) if all((2*c[o]-c[a]-c[b])%3==0 for o,a,b in crossings)]
assert len(valid)==9 and sum(len(set(c))>1 for c in valid)==6,(crossings,valid)
W=max(x[0] for x in pts)-min(x[0] for x in pts)
S=148/W
mind=min(math.dist(xs[i]['point'],xs[j]['point'])*S for i in range(3) for j in range(i))
assert mind>=25,mind
DATA={'under':under,'crossings':xs,'arc_relations':crossings,'total_colorings':9,'nonconstant_colorings':6,'diagram_width_mm':148,'min_crossing_distance_mm':mind}
if __name__=='__main__':
 Path(__file__).with_name('geometry-check.json').write_text(json.dumps(DATA,indent=2))
 print(json.dumps(DATA,indent=2))
