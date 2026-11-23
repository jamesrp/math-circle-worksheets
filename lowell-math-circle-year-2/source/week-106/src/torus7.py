# Seven-country donut map: hexagon tiling labeled (q+3r) mod 7, sheared so the
# period lattice becomes the unit square; clipped to the square board.
import math, sys
s3=math.sqrt(3)
def cart(q,r): return (q+r/2.0, r*s3/2.0)
v1=cart(1,2); v2=cart(-2,3)   # basis of the period lattice {q+3r = 0 mod 7}
det=v1[0]*v2[1]-v2[0]*v1[1]
# M = inverse of [v1 v2] -> maps v1->(1,0), v2->(0,1)
def M(p):
    x,y=p
    return ((x*v2[1]-y*v2[0])/det, (-x*v1[1]+y*v1[0])/det)
def hexverts(q,r):
    cx,cy=cart(q,r); R=1/s3
    return [M((cx+R*math.cos(math.radians(30+60*k)), cy+R*math.sin(math.radians(30+60*k)))) for k in range(6)]
def clip(poly, x0,y0,x1,y1):
    def cl(poly, inside, inter):
        out=[]
        for i in range(len(poly)):
            a=poly[i-1]; b=poly[i]
            if inside(b):
                if not inside(a): out.append(inter(a,b))
                out.append(b)
            elif inside(a): out.append(inter(a,b))
        return out
    def ix(a,b,X): t=(X-a[0])/(b[0]-a[0]); return (X, a[1]+t*(b[1]-a[1]))
    def iy(a,b,Y): t=(Y-a[1])/(b[1]-a[1]); return (a[0]+t*(b[0]-a[0]), Y)
    for inside,inter in ((lambda p:p[0]>=x0, lambda a,b:ix(a,b,x0)),(lambda p:p[0]<=x1, lambda a,b:ix(a,b,x1)),
                         (lambda p:p[1]>=y0, lambda a,b:iy(a,b,y0)),(lambda p:p[1]<=y1, lambda a,b:iy(a,b,y1))):
        poly=cl(poly,inside,inter)
        if not poly: return []
    return poly
def area(p): return abs(sum(p[i-1][0]*p[i][1]-p[i][0]*p[i-1][1] for i in range(len(p))))/2
def centroid(p):
    A=0;cx=0;cy=0
    for i in range(len(p)):
        x0,y0=p[i-1];x1,y1=p[i];c=x0*y1-x1*y0;A+=c;cx+=(x0+x1)*c;cy+=(y0+y1)*c
    A/=2; return (cx/(6*A),cy/(6*A))
def pieces(ox,oy):
    out=[]
    for q in range(-12,13):
        for r in range(-12,13):
            vs=[(x-ox,y-oy) for x,y in hexverts(q,r)]
            if max(x for x,y in vs)<0 or min(x for x,y in vs)>1 or max(y for x,y in vs)<0 or min(y for x,y in vs)>1: continue
            p=clip(vs,0,0,1,1)
            if p and area(p)>1e-9: out.append(((q+3*r)%7+1, p))
    return out
def best_offset():
    best=None
    N=40
    for i in range(N):
        for j in range(N):
            ox,oy=i/N,j/N
            ps=pieces(ox,oy)
            score=(len(ps), -min(area(p) for _,p in ps))
            if best is None or score<best[0]: best=(score,ox,oy)
    return best
if __name__=="__main__":
    b=best_offset(); print(b)
