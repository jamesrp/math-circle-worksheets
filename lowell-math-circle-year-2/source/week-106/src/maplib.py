# Shared geometry for Week 106 maps: dense polylines used both for TikZ output
# and for a raster check of the countries each printed map really has.
import math
from PIL import Image, ImageDraw

def catmull(pts, closed=False, n=24):
    P=list(pts)
    if closed: P=P+P[:3]; ext=P[-4:-3]
    out=[]
    if closed:
        seq=[P[-4]]+P  # wrap
        seq=[pts[-1]]+list(pts)+[pts[0],pts[1]]
        rng=range(1,len(pts)+1)
    else:
        seq=[(2*pts[0][0]-pts[1][0],2*pts[0][1]-pts[1][1])]+list(pts)+[(2*pts[-1][0]-pts[-2][0],2*pts[-1][1]-pts[-2][1])]
        rng=range(1,len(pts))
    for i in rng:
        p0,p1,p2,p3=seq[i-1],seq[i],seq[i+1],seq[i+2]
        for k in range(n):
            t=k/n; t2=t*t; t3=t2*t
            x=0.5*((2*p1[0])+(-p0[0]+p2[0])*t+(2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*t2+(-p0[0]+3*p1[0]-3*p2[0]+p3[0])*t3)
            y=0.5*((2*p1[1])+(-p0[1]+p2[1])*t+(2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*t2+(-p0[1]+3*p1[1]-3*p2[1]+p3[1])*t3)
            out.append((x,y))
    if not closed: out.append(pts[-1])
    return out

def polar(f, n=360, cx=0, cy=0, t0=0, t1=2*math.pi):
    return [(cx+f(t0+(t1-t0)*k/n)*math.cos(t0+(t1-t0)*k/n), cy+f(t0+(t1-t0)*k/n)*math.sin(t0+(t1-t0)*k/n)) for k in range(n)]

def path(pts, closed=False):
    s=" -- ".join("(%.3f,%.3f)"%p for p in pts)
    return s+(" -- cycle" if closed else "")

class Map:
    """frame: (w,h) box with corner at origin, or None.
    outline: closed polyline bounding the map when there is no frame.
    lines: open polylines (clipped to the frame); loops: closed polylines.
    holes: closed polylines of lakes (not countries)."""
    def __init__(self, frame=None, outline=None):
        self.frame=frame; self.outline=outline
        self.lines=[]; self.loops=[]; self.holes=[]; self.extra=[]
    def tikz(self, lw="very thick", scale=1.0):
        o=[]
        o.append("\\begin{tikzpicture}[xscale=%.3f,yscale=%.3f,line join=round,line cap=round]"%(getattr(self,'xs',scale),getattr(self,'ys',scale)))
        if self.frame:
            w,h=self.frame
            o.append("\\begin{scope}\\clip (0,0) rectangle (%.3f,%.3f);"%(w,h))
        for L in self.lines: o.append("\\draw[%s] %s;"%(lw,path(L)))
        for L in self.loops: o.append("\\draw[%s] %s;"%(lw,path(L,True)))
        if self.frame:
            o.append("\\end{scope}")
            o.append("\\draw[%s] (0,0) rectangle (%.3f,%.3f);"%(lw,w,h))
        if self.outline: o.append("\\draw[%s] %s;"%(lw,path(self.outline,True)))
        for H in self.holes: o.append("\\draw[%s] %s;"%(lw,path(H,True)))
        o.extend(self.extra)
        o.append("\\end{tikzpicture}")
        return "\n".join(o)
    def countries(self, ppc=40, w=3):
        """Rasterize; return (number of countries, list of areas in cm^2, adjacency sets)."""
        if self.frame: W,H=self.frame; x0,y0=0,0
        else:
            xs=[p[0] for p in self.outline]; ys=[p[1] for p in self.outline]
            x0,y0=min(xs),min(ys); W,H=max(xs)-x0,max(ys)-y0
        pad=4
        NX,NY=int(W*ppc)+2*pad,int(H*ppc)+2*pad
        T=lambda p:((p[0]-x0)*ppc+pad, (H-(p[1]-y0))*ppc+pad)
        dom=Image.new('L',(NX,NY),0); dd=ImageDraw.Draw(dom)
        if self.frame: dd.rectangle([T((0,H)),T((W,0))],fill=1)
        else: dd.polygon([T(p) for p in self.outline],fill=1)
        for Hh in self.holes: dd.polygon([T(p) for p in Hh],fill=0)
        ln=Image.new('L',(NX,NY),0); ld=ImageDraw.Draw(ln)
        for L in self.lines: ld.line([T(p) for p in L],fill=1,width=w)
        for L in self.loops: ld.line([T(p) for p in L+[L[0]]],fill=1,width=w)
        D=dom.load(); Lp=ln.load()
        lab={}; areas=[]
        cid=0
        for i in range(NX):
            for j in range(NY):
                if D[i,j] and not Lp[i,j] and (i,j) not in lab:
                    st=[(i,j)]; lab[(i,j)]=cid; cnt=0
                    while st:
                        a,b=st.pop(); cnt+=1
                        for da,db in ((1,0),(-1,0),(0,1),(0,-1)):
                            q=(a+da,b+db)
                            if 0<=q[0]<NX and 0<=q[1]<NY and D[q] and not Lp[q] and q not in lab:
                                lab[q]=cid; st.append(q)
                    areas.append(cnt/ppc/ppc); cid+=1
        # adjacency: line pixels whose neighbourhood sees exactly two countries
        from collections import Counter
        cnt=Counter(); r=w+1
        for i in range(NX):
            for j in range(NY):
                if Lp[i,j] and D[i,j]:
                    s=set()
                    for da in range(-r,r+1):
                        for db in range(-r,r+1):
                            q=(i+da,j+db)
                            if q in lab: s.add(lab[q])
                    if len(s)==2: cnt[frozenset(s)]+=1
        adj={k:set() for k in range(cid)}
        for pr,c in cnt.items():
            if c>ppc*0.3:  # more than ~3 mm of shared border
                a,b=tuple(pr); adj[a].add(b); adj[b].add(a)
        return cid, areas, adj

def chromatic(adj):
    n=len(adj); order=sorted(adj,key=lambda v:-len(adj[v]))
    for k in range(1,n+1):
        col={}
        def bt(i):
            if i==n: return True
            v=order[i]
            for c in range(k):
                if all(col.get(u)!=c for u in adj[v]):
                    col[v]=c
                    if bt(i+1): return True
                    del col[v]
            return False
        if bt(0): return k
    return n

def lake_waves(cx,cy,r):
    out=[]
    for dy,ww in ((0.32,0.9),(0,1.1),(-0.32,0.9)):
        y=cy+dy*r; hw=ww*r*0.38
        pts=[(cx-hw+2*hw*k/16, y+0.06*r*math.sin(k/16*4*math.pi)) for k in range(17)]
        out.append("\\draw[thin] %s;"%path(pts))
    return out
