# Generates every map figure for Week 106 as figs/<name>.tex and checks each one.
import math, os, sys
from maplib import *
os.makedirs('figs',exist_ok=True)
FIG={}   # name -> (Map or raw tikz, expected chromatic number or None)

def wob(R, a=0.05, b=0.035, p=0.0):
    return lambda t: R*(1+a*math.sin(3*t+1+p)+b*math.cos(5*t+2+p))

def ring_map(n, R, ri, middle=False, flower=False, t0=math.pi/2, seed=0, lw=None, labels=None, lfont="\\large"):
    if flower:
        fo=lambda t: R*(0.80+0.20*abs(math.sin(n*(t-t0)/2))**0.7)
    else:
        fo=wob(R, p=seed)
    fi=(lambda t: ri) if middle else wob(ri, a=0.06, b=0.03, p=seed+1)
    outer=polar(fo, 480)
    inner=polar(fi, 240)
    m=Map(outline=outer)
    if middle: m.loops.append(inner)
    else: m.holes.append(inner); m.extra+=lake_waves(0,0,ri*0.95)
    for k in range(n):
        t=t0+2*math.pi*k/n+(0 if flower or middle else 0.12*math.sin(7*k+seed))
        a=(fi(t)-0.02)*math.cos(t),(fi(t)-0.02)*math.sin(t)
        b=(fo(t)+0.02)*math.cos(t),(fo(t)+0.02)*math.sin(t)
        m.lines.append([a,b])
    if labels:
        for k,L in enumerate(labels[1:]):
            t=t0+2*math.pi*(k+0.5)/n
            rr=(fi(t)+fo(t))/2
            m.extra.append("\\node at (%.3f,%.3f) {%s %s};"%(rr*math.cos(t),rr*math.sin(t),lfont,L))
        m.extra.append("\\node at (0,0) {%s %s};"%(lfont,labels[0]))
    return m

def on(curve, x):
    """point of a dense polyline closest to the given x"""
    return min(curve, key=lambda p: abs(p[0]-x))
def onxy(curve, p0):
    return min(curve, key=lambda p: (p[0]-p0[0])**2+(p[1]-p0[1])**2)

# ---------------- K-1 scribble maps (17 x 8.2) ----------------
W,H=17,8.2
m=Map(frame=(W,H))
m.lines.append(catmull([(-0.6,7.4),(3,6.4),(6,7.0),(9,4.9),(12,3.2),(15,3.0),(17.6,1.4)]))
m.lines.append(catmull([(-0.6,1.0),(3,2.4),(6,1.6),(9,3.8),(12,5.6),(15,6.2),(17.6,5.4)]))
m.lines.append(catmull([(13.2,8.8),(14.2,6.6),(13.0,4.4),(14.0,2.0),(13.4,-0.6)]))
FIG['k_lines_a']=(m,2)

m=Map(frame=(W,H))
m.lines.append([(x/10, 4.1+2.6*math.sin(2*math.pi*(x/10)/7.2+0.3)) for x in range(-6,177)])
m.lines.append([(x/10, 4.0-2.2*math.sin(2*math.pi*(x/10)/7.4+0.45)) for x in range(-6,177)])
FIG['k_lines_b']=(m,2)

m=Map(frame=(W,10.6))
for (cx,cy) in ((6.75,6.45),(10.25,6.45),(8.5,3.55)):
    m.loops.append(polar(lambda t:3.15,240,cx,cy))
FIG['k_venn']=(m,2)

m=Map(frame=(W,H))
# one closed scribble that crosses itself several times
m.loops.append(polar(lambda t: 1.0, 600))  # placeholder replaced below
pts=[]
for k in range(720):
    t=4*math.pi*k/720
    r=2.6+1.25*math.sin(2.5*t)
    pts.append((8.5+2.05*r*math.cos(t), 4.1+1.05*r*math.sin(t)))
m.loops=[pts]
FIG['k_scribble_loop']=(m,2)

# K-1 lines that stop (8 x 6)
w,h=8,5.6
m=Map(frame=(w,h))
L=catmull([(-0.5,3.4),(2,3.9),(4.5,3.1),(6.5,3.6),(8.5,3.3)]); m.lines.append(L)
e=on(L,4.6); m.lines.append(catmull([(4.0,-0.5),(4.6,1.2),(4.2,2.2),e]))
FIG['k_T']=(m,3)
m=Map(frame=(w,h))
c=(4.0,2.8)
m.lines.append(catmull([(-0.5,2.4),(2,3.2),c,(6,2.4),(8.5,3.2)]))
m.lines.append(catmull([(3.4,-0.5),(4.4,1.3),c,(3.6,4.4),(4.3,6.1)]))
FIG['k_plus']=(m,2)
m=Map(frame=(w,h))
c=(4.0,2.6)
for end,mid in (((4.4,6.2),(3.6,4.4)),((-0.5,0.4),(1.8,1.9)),((8.5,0.8),(6.2,1.4))):
    m.lines.append(catmull([c,mid,end]))
FIG['k_Y']=(m,3)
m=Map(frame=(w,h))
m.lines.append(catmull([(-0.5,2.0),(2.0,2.4),(4.0,3.4),(6.0,2.6),(8.5,3.4)]))
m.loops=[[(4.0+2.6*math.cos(2*math.pi*k/200)*(1+0.06*math.sin(6*math.pi*k/200)), 2.8+1.85*math.sin(2*math.pi*k/200)) for k in range(200)]]
FIG['k_lineloop']=(m,2)

# K-1 rings around ponds and flowers
for n in (4,5,6,7):
    FIG['k_ring%d'%n]=(ring_map(n,3.6,1.45,seed=n),2 if n%2==0 else 3)
for n in (3,4,5,6):
    FIG['k_flower%d'%n]=(ring_map(n,3.8,1.45,middle=True,flower=True,t0=math.pi/2+math.pi/n),{3:4,4:3,5:4,6:3}[n])

# ---------------- Grades 2-5 scribble maps (8.4 x 6.6) ----------------
w,h=8.4,6.6
m=Map(frame=(w,h))
m.lines.append(catmull([(-0.5,5.4),(2.5,4.8),(5.5,2.6),(8.9,1.4)]))
m.lines.append(catmull([(-0.5,1.0),(3,1.9),(5.5,3.9),(8.9,5.4)]))
m.lines.append(catmull([(2.0,7.1),(2.8,5.0),(2.2,2.8),(3.2,-0.5)]))
m.lines.append(catmull([(6.6,7.1),(5.9,5.0),(6.6,2.4),(5.8,-0.5)]))
FIG['u_lines4']=(m,2)
m=Map(frame=(w,h))
m.loops.append([(3.1+2.0*math.cos(2*math.pi*k/200),3.4+2.1*math.sin(2*math.pi*k/200)) for k in range(200)])
m.loops.append([(5.3+2.0*math.cos(2*math.pi*k/200),3.2+2.0*math.sin(2*math.pi*k/200)) for k in range(200)])
m.lines.append(catmull([(-0.5,2.6),(2.0,3.6),(4.2,2.9),(6.4,3.7),(8.9,3.0)]))
FIG['u_loops2']=(m,2)
m=Map(frame=(w,h))
for (cx,cy) in ((3.45,4.55),(5.05,4.55),(4.25,3.2)):
    m.loops.append(polar(lambda t:1.6,200,cx,cy))
m.lines.append(catmull([(-0.5,5.7),(0.9,3.0),(2.6,0.9),(5.9,0.9),(7.6,3.0),(8.9,5.7)]))
FIG['u_venn_line']=(m,2)
m=Map(frame=(w,h))
pts=[]
for k in range(720):
    t=4*math.pi*k/720
    r=1.5+0.75*math.sin(2.5*t)
    pts.append((4.2+1.55*r*math.cos(t), 3.3+1.25*r*math.sin(t)))
m.loops=[pts]
FIG['u_scribble']=(m,2)

# Grades 2-5 lines that stop (8 x 5.4)
w,h=8,5.4
m=Map(frame=(w,h))
L=catmull([(-0.5,3.0),(2,3.5),(4.5,2.8),(6.5,3.3),(8.5,3.0)]); m.lines.append(L)
e=on(L,3.4); m.lines.append(catmull([(3.0,-0.5),(3.6,1.4),e]))
FIG['u_T']=(m,3)
def star(nr, c, ends):
    m=Map(frame=(w,h))
    for E in ends: m.lines.append(catmull([c,((c[0]+E[0])/2+0.25,(c[1]+E[1])/2-0.15),E]))
    return m
c=(4.1,2.7)
FIG['u_Y']=(star(3,c,[(4.6,5.9),(-0.5,0.2),(8.5,0.6)]),3)
FIG['u_star5']=(star(5,c,[(4.0,5.9),(-0.5,4.2),(-0.5,-0.2),(6.0,-0.5),(8.5,3.6)]),3)
FIG['u_star6']=(star(6,c,[(1.6,5.9),(6.6,5.9),(-0.5,2.0),(8.5,3.0),(2.0,-0.5),(6.4,-0.5)]),2)
m=Map(frame=(w,h))
L=catmull([(-0.5,2.6),(2.5,3.0),(5.5,2.4),(8.5,2.9)]); m.lines.append(L)
e1=on(L,2.7); m.lines.append(catmull([(2.4,5.9),(2.9,4.2),e1]))
e2=on(L,5.6); m.lines.append(catmull([(5.9,-0.5),(5.3,1.2),e2]))
FIG['u_ladder']=(m,3)
m=Map(frame=(w,h))
m.lines.append(catmull([(-0.5,1.0),(3,2.2),(5.5,3.6),(8.5,4.6)]))
m.lines.append(catmull([(1.2,5.9),(2.4,3.4),(4.4,1.2),(5.2,-0.5)]))
m.lines.append(catmull([(8.5,1.2),(7.0,1.6),(6.0,1.3)]))   # stops in the middle of a country
FIG['u_dangle']=(m,2)

# Grades 2-5 rings and wheels
for n in (4,5,6,7):
    FIG['u_ring%d'%n]=(ring_map(n,3.1,1.25,seed=n),2 if n%2==0 else 3)
    FIG['u_wheel%d'%n]=(ring_map(n,3.1,1.3,middle=True,seed=n,t0=math.pi/2+math.pi/n),3 if n%2==0 else 4)
FIG['u_wheel5_lab']=(ring_map(5,2.6,1.05,middle=True,seed=5,t0=math.pi/2+math.pi/5,labels="FABCDE",lfont="\\normalsize"),4)

for k in ('k_T','k_plus','k_Y','k_lineloop'):
    FIG[k][0].xs=1.06; FIG[k][0].ys=1.3
for k in ('u_lines4','u_loops2','u_venn_line','u_scribble'):
    FIG[k][0].xs=1.02; FIG[k][0].ys=1.14
def write_all():
    for k,(m,chi) in FIG.items():
        open('figs/%s.tex'%k,'w').write(m.tikz())
def check():
    ok=True
    for k,(m,chi) in FIG.items():
        n,areas,adj=m.countries()
        c=chromatic(adj)
        flag="" if c==chi else "   <-- MISMATCH"
        if c!=chi: ok=False
        print("%-16s countries=%2d  min area=%5.2f cm2  colors=%d (expected %d)%s"%(k,n,min(areas),c,chi,flag))
    return ok
if __name__=="__main__":
    write_all()
    if len(sys.argv)>1: check()

# ---------------- raw TikZ figures (boards, donuts) ----------------
RAW={}
def donut_frame(S, font="\\large"):
    # edges with the same letter are glued together
    o=["\\draw[very thick] (0,0) rectangle (%.3f,%.3f);"%(S,S)]
    m=S/2; g=0.38
    for x in (-g,S+g): o.append("\\node at (%.3f,%.3f) {%s\\bfseries A};"%(x,m,font))
    for y in (-g,S+g): o.append("\\node at (%.3f,%.3f) {%s\\bfseries B};"%(m,y,font))
    return o
def tk(body): return "\\begin{tikzpicture}[line join=round]\n"+"\n".join(body)+"\n\\end{tikzpicture}"
S=5.2
def stripes(n):
    o=["\\draw[very thick] (%.3f,0) -- (%.3f,%.3f);"%(S*k/n,S*k/n,S) for k in range(1,n)]
    o+=["\\node at (%.3f,%.3f) {\\large %d};"%(S*(k+0.5)/n,S*0.5,k+1) for k in range(n)]
    return tk(o+donut_frame(S))
def dgrid(n):
    o=["\\draw[very thick] (%.3f,0) -- (%.3f,%.3f);"%(S*k/n,S*k/n,S) for k in range(1,n)]+["\\draw[very thick] (0,%.3f) -- (%.3f,%.3f);"%(S*k/n,S,S*k/n) for k in range(1,n)]
    f="\\normalsize" if n>3 else "\\large"
    o+=["\\node at (%.3f,%.3f) {%s %d};"%(S*(j+0.5)/n,S*(n-i-0.5)/n,f,i*n+j+1) for i in range(n) for j in range(n)]
    return tk(o+donut_frame(S))
RAW['d_stripes3']=stripes(3); RAW['d_stripes4']=stripes(4); RAW['d_grid3']=dgrid(3); RAW['d_grid4']=dgrid(4)
def blank_donut(s):
    global S
    old=S; S=s; r=tk(donut_frame(s)); S=old; return r
RAW['d_blank']=blank_donut(8.0)
import torus7
def seven(s):
    o=[]
    for lab,p in torus7.pieces(0,0):
        o.append("\\draw[very thick] %s;"%path([(x*s,y*s) for x,y in p],True))
    for lab,p in torus7.pieces(0,0):
        cx,cy=torus7.centroid(p); A=torus7.area(p)
        f="\\Large" if A>0.1 else ("\\normalsize" if A>0.03 else "\\footnotesize")
        o.append("\\node at (%.3f,%.3f) {%s %d};"%(cx*s,cy*s,f,lab))
    o+=donut_frame(s)
    return tk(o)
RAW['d_seven']=seven(8.2)
def tiled7(t, lo=-0.5, hi=1.5):
    # the seven-country board (thick square) with the pieces around it seen across the glued edges
    o=["\\begin{scope}\\clip (%.3f,%.3f) rectangle (%.3f,%.3f);"%(lo*t,lo*t,hi*t,hi*t)]
    labs=[]
    for q in range(-14,15):
        for r in range(-14,15):
            vs=torus7.hexverts(q,r)
            if max(x for x,y in vs)<lo or min(x for x,y in vs)>hi or max(y for x,y in vs)<lo or min(y for x,y in vs)>hi: continue
            o.append("\\draw[thick] %s;"%path([(x*t,y*t) for x,y in vs],True))
            cx=sum(x for x,y in vs)/6; cy=sum(y for x,y in vs)/6
            if lo+0.06<cx<hi-0.06 and lo+0.06<cy<hi-0.06:
                labs.append("\\node at (%.3f,%.3f) {\\normalsize %d};"%(cx*t,cy*t,(q+3*r)%7+1))
    o.append("\\end{scope}")
    o.append("\\draw[thick] (%.3f,%.3f) rectangle (%.3f,%.3f);"%(lo*t,lo*t,hi*t,hi*t))
    o.append("\\draw[line width=2.6pt] (0,0) rectangle (%.3f,%.3f);"%(t,t))
    o+=[l.replace("\\node at","\\node[fill=white,inner sep=1.5pt] at") for l in labs]
    return tk(o)
RAW['d_tiled7']=tiled7(4.1)
# game boards
RAW['g_strip4']=tk(["\\draw[very thick] (%d*2.1,0) rectangle +(2.1,2.1);"%k for k in range(4)])
RAW['g_ttt']=tk(["\\draw[very thick] (0,0) grid[step=1.55] (4.65,4.65);"])
RAW['g_pond4']=ring_map(4,2.95,1.15,seed=11).tikz()
# rule pictures (pattern fills stand for colors)
def sq(x,y,pat): return "\\draw[thick,pattern=%s] (%.2f,%.2f) rectangle +(1,1);"%(pat,x,y)
RAW['rule_border']=tk([sq(0,0,"north east lines"),"\\draw[thick,fill=black!45] (1,0) rectangle +(1,1);"])
# K-1 game: an empty square between the two colors is stuck
RAW['k_stuck']=tk([sq(0,0,"north east lines"),"\\draw[thick] (1,0) rectangle +(1,1);","\\draw[thick,fill=black!45] (2,0) rectangle +(1,1);","\\node[below] at (1.5,-0.05) {\\normalsize stuck};"])
# K-1 drawing rule: a line goes all the way across (ok); a line that stops at another line (not ok)
from maplib import catmull as _cm
def _box(lines):
    o=["\\begin{scope}\\clip (0,0) rectangle (3.6,2.2);"]
    o+=["\\draw[very thick,line cap=round] %s;"%path(L) for L in lines]
    o.append("\\end{scope}\\draw[very thick] (0,0) rectangle (3.6,2.2);")
    return tk(o)
_L=_cm([(-0.2,1.3),(1.0,1.6),(2.2,1.0),(3.8,1.4)])
RAW['k_line_ok']=_box([_L,_cm([(1.2,2.4),(1.6,1.2),(1.1,-0.2)])])
_e=min(_L,key=lambda p:abs(p[0]-2.4))
RAW['k_line_bad']=_box([_L,_cm([(2.0,-0.2),(2.6,0.6),_e])])
RAW['rule_corner']=tk([sq(0,0,"north east lines"),sq(1,1,"north east lines")])
def write_raw():
    for k,v in RAW.items(): open('figs/%s.tex'%k,'w').write(v)
write_raw()
RAW['rule_bad']=tk([sq(0,0,"north east lines"),sq(1,0,"north east lines")])
write_raw()
