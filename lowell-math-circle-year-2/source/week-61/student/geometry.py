"""Original spherical diagrams. Standard library only; all figures are schematics."""
from itertools import product
from math import acos, atan2, cos, degrees, pi, radians, sin, sqrt

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(a,t): return tuple(x*t for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def unit(a): return mul(a,1/sqrt(dot(a,a)))
def clamp(x): return max(-1,min(1,x))
def slerp(a,b,t):
    w=acos(clamp(dot(a,b)))
    if w<1e-10: return a
    return add(mul(a,sin((1-t)*w)/sin(w)),mul(b,sin(t*w)/sin(w)))
def tangent(a,b): return unit(add(b,mul(a,-dot(a,b))))
def corner(a,b,c): return degrees(acos(clamp(dot(tangent(a,b),tangent(a,c)))))
def area(v):
    a,b,c=v
    return 2*atan2(abs(dot(a,cross(b,c))),1+dot(a,b)+dot(b,c)+dot(c,a))
def meridian(gap):
    h=radians(gap/2)
    return ((0,0,1),(cos(h),-sin(h),0),(cos(h),sin(h),0))
def from_angles(A,B,C):
    a,b,c=map(radians,(A,B,C))
    side_b=acos(clamp((cos(b)+cos(a)*cos(c))/(sin(a)*sin(c))))
    side_c=acos(clamp((cos(c)+cos(a)*cos(b))/(sin(a)*sin(b))))
    return ((0,0,1),(sin(side_c),0,cos(side_c)),
            (sin(side_b)*cos(a),sin(side_b)*sin(a),cos(side_b)))

class View:
    def __init__(self,eye=(cos(radians(35)),0,sin(radians(35))),right=(0,1,0),up=None):
        self.eye=unit(eye)
        self.right=unit(add(right,mul(self.eye,-dot(right,self.eye))))
        self.up=unit(cross(self.eye,self.right)) if up is None else up
    def p(self,v): return (dot(v,self.right),dot(v,self.up))
    def z(self,v): return dot(v,self.eye)
    def back(self): return View(mul(self.eye,-1),mul(self.right,-1),self.up)
    @classmethod
    def triangle(cls,verts):
        eye=unit(tuple(sum(v[i] for v in verts) for i in range(3)))
        up=unit(add(verts[0],mul(eye,-dot(eye,verts[0]))))
        return cls(eye,cross(up,eye),up)

def xy(p): return f"({p[0]:.5f},{p[1]:.5f})"
def path(vs,view): return ' -- '.join(xy(view.p(v)) for v in vs)
def horizon_intersection(a,b,view):
    # A side-normal view places entire side vertices exactly on the limb.
    # Treat roundoff there consistently with clip's boundary tolerance.
    if abs(view.z(a))<1e-10: return a
    if abs(view.z(b))<1e-10: return b
    lo,hi=0.,1.
    za=view.z(a)
    for _ in range(55):
        mid=(lo+hi)/2
        if (view.z(slerp(a,b,mid))>=0)==(za>=0): lo=mid
        else: hi=mid
    return slerp(a,b,(lo+hi)/2)
def clip(poly,view):
    if max(view.z(v) for v in poly)<=1e-10: return []
    result=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        inside_a=view.z(a)>=-1e-10; inside_b=view.z(b)>=-1e-10
        if inside_a: result.append(a)
        if inside_a != inside_b: result.append(horizon_intersection(a,b,view))
    return result
def curved_poly(poly,view):
    clipped=clip(list(poly),view)
    if len(clipped)<3: return None
    sampled=[]
    for a,b in zip(clipped,clipped[1:]+clipped[:1]):
        for j in range(25): sampled.append(slerp(a,b,j/25))
    return path(sampled,view)+' -- cycle'
def arc(a,b,view,style='ink,line width=.85pt',steps=90):
    pts=[slerp(a,b,j/steps) for j in range(steps+1)]
    chunks=[]; current=[pts[0]]; shown=view.z(pts[0])>=0
    for p in pts[1:]:
        now=view.z(p)>=0
        if now!=shown:
            current.append(p)
            chunks.append((shown,current));current=[p];shown=now
        else: current.append(p)
    chunks.append((shown,current))
    return '\n'.join('\\draw['+style+('' if vis else ',dashed,opacity=.45')+'] '+path(ps,view)+';' for vis,ps in chunks if len(ps)>1)
def great_circle(a,b,view,style='ink,line width=.55pt'):
    t=tangent(a,b)
    vs=[add(mul(a,cos(2*pi*j/240)),mul(t,sin(2*pi*j/240))) for j in range(241)]
    out=[]; current=[vs[0]]; vis=view.z(vs[0])>=0
    for v in vs[1:]:
        now=view.z(v)>=0
        if now!=vis:
            current.append(v);out.append((vis,current));current=[v];vis=now
        else: current.append(v)
    out.append((vis,current))
    return '\n'.join('\\draw['+style+('' if shown else ',dashed,opacity=.4')+'] '+path(ps,view)+';' for shown,ps in out if len(ps)>1)
def visible_circle(a,b,view,style='ink,line width=.65pt'):
    """Exactly one visible semicircle; the rear copy is deliberately omitted.

    Circle a,t has depth za*cos(u)+zt*sin(u). Its positive-depth interval
    is phase-pi/2 through phase+pi/2. A circle at the limb is the outline.
    """
    t=tangent(a,b); za,zt=view.z(a),view.z(t)
    if sqrt(za*za+zt*zt)<1e-10: return ''
    phase=atan2(zt,za)
    vs=[add(mul(a,cos(phase-pi/2+pi*j/180)),
            mul(t,sin(phase-pi/2+pi*j/180))) for j in range(181)]
    return '\\draw['+style+'] '+path(vs,view)+';'
def visible_minor_arc(a,b,view,style='ink,line width=.85pt'):
    """Minor arc on the visible surface, with stable limb classification."""
    pts=[slerp(a,b,j/90) for j in range(91)]
    if max(view.z(p) for p in pts)<=1e-10: return ''
    chunks=[]; current=[]
    for p,q in zip(pts,pts[1:]):
        pin=view.z(p)>=-1e-10; qin=view.z(q)>=-1e-10
        if pin and not current: current=[p]
        if pin and qin: current.append(q)
        elif pin:
            current.append(horizon_intersection(p,q,view));chunks.append(current);current=[]
        elif qin: current=[horizon_intersection(p,q,view),q]
    if len(current)>1: chunks.append(current)
    return '\n'.join('\\draw['+style+'] '+path(ps,view)+';' for ps in chunks)
def side_view(verts):
    """Front is the positive hemisphere of side BC; back is its negative."""
    a,b,c=verts
    eye=unit(cross(b,c))
    if dot(eye,a)<0: eye=mul(eye,-1)
    projected=add(a,mul(eye,-dot(a,eye)))
    if dot(projected,projected)<1e-12: projected=b
    up=unit(projected)
    return View(eye,cross(up,eye),up)
def begin(radius=1.25):
    return '\\begin{tikzpicture}[x='+str(radius)+'in,y='+str(radius)+'in]\n\\path[use as bounding box] (-1.17,-1.16) rectangle (1.17,1.17);\n\\fill[ballgray] (0,0) circle (1);'
def end(): return '\\draw[ink,line width=.65pt] (0,0) circle (1);\n\\end{tikzpicture}'
def dotlabel(v,view,label,anchor='south',offset=(0,.035)):
    p=view.p(v);q=(p[0]+offset[0],p[1]+offset[1])
    return '\\fill[ink] '+xy(p)+' circle (.020);\\node[font=\\small,anchor='+anchor+',fill=white,inner sep=1pt] at '+xy(q)+' {$'+label+'$};'
def triangle(verts,radius=.82,view=None,labels=('N','A','B'),full=False,regions=False,shade=False,pair=None,
             surface_only=False,selected=None,focus=None,patch=None):
    view=view or View()
    lines=[begin(radius)]
    signs=list(product((1,-1),repeat=3))
    if pair is not None:
        # At vertex index k, the containing and opposite lunes have equal signs
        # on the other two side half-spaces. Four of the eight cells are covered.
        indices=[i for i in range(3) if i!=pair]
        for s in signs:
            if s[indices[0]]==s[indices[1]]:
                q=curved_poly([mul(v,t) for v,t in zip(verts,s)],view)
                if q: lines.append('\\fill[blue!22] '+q+';')
    elif shade:
        q=curved_poly(verts,view)
        if q: lines.append('\\fill[blue!18] '+q+';')
    for i in range(3):
        a,b=verts[i],verts[(i+1)%3]
        is_selected=selected is None or i in selected
        if selected is not None and not is_selected: continue
        style='blue,line width=1.2pt' if selected is not None else 'ink,line width=.65pt'
        lines.append((visible_circle(a,b,view,style) if surface_only else great_circle(a,b,view,style)) if full else
                     (visible_minor_arc(a,b,view) if surface_only else arc(a,b,view)))
    if labels:
        for v,label in zip(verts,labels):
            candidates=[(v,label)]+([(mul(v,-1),label+'^*')] if full else [])
            for w,text in candidates:
                depth=view.z(w)
                if depth>1e-8: lines.append(dotlabel(w,view,text))
                elif surface_only and abs(depth)<=1e-8:
                    p=view.p(w)
                    lines.append(dotlabel(w,view,text,'center',(p[0]*.105,p[1]*.105)))
    if focus is not None:
        lines.append('\\draw[blue,line width=1.1pt] '+xy(view.p(verts[focus]))+' circle (.046);')
    if patch is not None:
        # One interior patch in cell +--; this belongs to the A pair once.
        q=unit(add(mul(verts[0],3),mul(add(verts[1],verts[2]),-1)))
        assert view.z(q)>0
        p=view.p(q)
        lines.append('\\fill[blue] '+xy(p)+' circle (.025);')
        lines.append('\\node[font=\\small,anchor=north,fill=white,inner sep=1pt] at '+xy((p[0],p[1]-.035))+' {$'+patch+'$};')
    if regions:
        for j,s in enumerate(signs,1):
            cen=unit(tuple(sum(t*v[i] for t,v in zip(s,verts)) for i in range(3)))
            if view.z(cen)>0:
                lines.append('\\node[font=\\small,fill=white,inner sep=1.8pt] at '+xy(view.p(cen))+' {'+str(j)+'};')
    lines.append(end());return '\n'.join(lines)

def route(stage):
    view=View(); a=(cos(radians(-40)),sin(radians(-40)),0); b=(cos(radians(55)),sin(radians(55)),0)
    lines=[begin(.78)]
    if stage>=1:
        lines.append(great_circle(a,b,view,'ink,line width=.6pt'))
        lines.append('\\fill[ink] (0,0) circle (.016);\\node[font=\\scriptsize,anchor=south] at (0,.04) {center};')
    if stage==2: lines.append(arc(a,b,view,'blue,line width=2.4pt'))
    lines.extend([dotlabel(a,view,'P'),dotlabel(b,view,'Q'),end()]);return '\n'.join(lines)
def angle_input():
    # Vertex on the front center: the two actual surface tangents differ by 135 degrees.
    view=View((0,0,1),(1,0,0)); p=(0,0,1)
    a=(sin(radians(50)),0,cos(radians(50)))
    b=(sin(radians(50))*cos(radians(135)),sin(radians(50))*sin(radians(135)),cos(radians(50)))
    return '\n'.join((begin(.65),arc(p,a,view,'blue,line width=1.5pt'),arc(p,b,view,'blue,line width=1.5pt'),dotlabel(p,view,'P','north',(0,-.04)),end()))
def lune():
    verts=meridian(40);view=View();n,a,b=verts;s=(0,0,-1)
    poly=[n,a,s,b]
    lines=[begin(.73)]
    q=curved_poly(poly,view)
    if q: lines.append('\\fill[blue!22] '+q+';')
    for p in (a,b):
        lines.extend([arc(n,p,view,'blue,line width=1pt'),arc(p,s,view,'blue,line width=1pt')])
    lines.extend([great_circle(a,b,view,'ink,line width=.4pt'),dotlabel(n,view,'N')])
    p=view.p(s)
    lines.append('\\draw[ink,fill=white] '+xy(p)+' circle (.020);\\node[font=\\scriptsize,anchor=north,fill=white,inner sep=1pt] at '+xy((p[0],p[1]-.03))+' {$S$ (back)};')
    lines.append(end());return '\n'.join(lines)

def write_figures(pathname):
    eighty=from_angles(80,80,80); octant=meridian(90)
    ev=side_view(eighty); ov=side_view(octant)
    figures={
        'routeinput':route(0),'routecircle':route(1),'routeoutput':route(2),
        'angleinput':angle_input(),'luneexample':lune(),
        'triangleblank':triangle(meridian(75),1.13,shade=False),
        'movingtriangle':triangle(meridian(110),.86,shade=True),
        'pairinput':triangle(eighty,.62,ev,('A','B','C'),focus=0,surface_only=True,shade=True),
        'paircircles':triangle(eighty,.62,ev,('A','B','C'),full=True,surface_only=True,selected=(0,2),focus=0),
        'pairfront':triangle(eighty,.62,ev,('A','B','C'),full=True,pair=0,surface_only=True,patch='X'),
        'pairback':triangle(eighty,.62,ev.back(),('A','B','C'),full=True,pair=0,surface_only=True),
        'countfront':triangle(octant,1.08,ov,('N','A','B'),full=True,regions=True,surface_only=True),
        'countback':triangle(octant,1.08,ov.back(),('N','A','B'),full=True,regions=True,surface_only=True),
        'unequalfront':triangle(eighty,1.32,ev,('A','B','C'),full=True,regions=True,surface_only=True),
        'unequalback':triangle(eighty,1.32,ev.back(),('A','B','C'),full=True,regions=True,surface_only=True),
    }
    for key,angles in [('recorda',(60,60,90)),('recordb',(80,80,80)),('recordc',(100,100,100))]:
        v=from_angles(*angles)
        figures[key]=triangle(v,.83,View.triangle(v),('A','B','C'),shade=True)
    with open(pathname,'w') as f:
        f.write('% Original generated TikZ sphere schematics.\n')
        for name,body in figures.items(): f.write('\\newcommand{\\'+name+'}{%\n'+body+'%\n}\n')

if __name__=='__main__':
    import sys
    write_figures(sys.argv[1])
