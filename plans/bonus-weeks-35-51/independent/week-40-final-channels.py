"""Independent PDF-pixel continuity checks from mathematical arc endpoints.

No builder/author verifier imports. Pixel regions reached by path midpoints must
coincide exactly when their mathematical gap-to-gap arcs coincide.
"""
from fractions import Fraction as F
from collections import deque
from array import array
from pathlib import Path
import json
import pymupdf

def paths(cx,yt,n,w=70,closed=True,cutleft=False,cutright=False):
    xl=F(cx)-F(w,2);xr=F(cx)+F(w,2);yb=F(yt)-35*n;out=[]
    for j in range(n):
        top=F(yt)-35*j
        under=lambda t:(xl+w*t,top-35*t)
        out.extend([[under(F(0)),under(F(17,50))],[under(F(33,50)),under(F(1))],[(xr,top),(xl,top-35)]])
    if closed:
        for x,outer,cut in [(xl,xl-30,cutleft),(xr,xr+30,cutright)]:
            out.extend([[(x,F(yt)),(x,F(yt)+15),(outer,F(yt)+15)],[(outer,yb-15),(x,yb-15),(x,yb)]])
            if cut:out.extend([[(outer,F(yt)+15),(outer,F(yt)-32)],[(outer,F(yt)-58),(outer,yb-15)]])
            else:out.append([(outer,F(yt)+15),(outer,yb-15)])
    return out
def groups(parts):
    parent=list(range(len(parts)))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    endpoints={}
    for i,p in enumerate(parts):
        for xy in [p[0],p[-1]]:
            if xy in endpoints:parent[find(i)]=find(endpoints[xy])
            else:endpoints[xy]=i
    return [find(i) for i in range(len(parts))]
pdf=pymupdf.open('tmp/worksheet-runs/week-40-bonus-v1/final/bonus.pdf');results=[]
def check(page,parts,expected,tag):
    xs=[float(x) for p in parts for x,y in p];ys=[float(y) for p in parts for x,y in p]
    clip=pymupdf.Rect(min(xs)-9,792-max(ys)-9,max(xs)+9,792-min(ys)+9)
    scale=4;pix=pdf[page].get_pixmap(matrix=pymupdf.Matrix(scale,scale),clip=clip,colorspace=pymupdf.csGRAY,alpha=False)
    data=pix.samples;w=pix.width;h=pix.height;labels=array('i',[0])*(w*h);nextlabel=0
    def label_point(x,y):
        nonlocal nextlabel
        px=int(float(x)*scale)-pix.x;py=int((792-float(y))*scale)-pix.y;start=py*w+px
        assert data[start]>=235,(tag,'midpoint not white',str(x),str(y),data[start])
        if labels[start]:return labels[start]
        nextlabel+=1;labels[start]=nextlabel;q=deque([start])
        while q:
            i=q.popleft();col=i%w
            for j in ([i-1] if col else [])+([i+1] if col+1<w else [])+([i-w] if i>=w else [])+([i+w] if i+w<w*h else []):
                if not labels[j] and data[j]>=235:labels[j]=nextlabel;q.append(j)
        return nextlabel
    graph_groups=groups(parts);pairset=set()
    for grp,p in zip(graph_groups,parts):
        samplelabels={label_point((a[0]+b[0])/2,(a[1]+b[1])/2) for a,b in zip(p,p[1:])}
        assert len(samplelabels)==1,(tag,'one stroke has broken channel',samplelabels)
        pairset.add((grp,next(iter(samplelabels))))
    assert len(set(graph_groups))==expected
    assert len(pairset)==expected and len({r for g,r in pairset})==expected,(tag,'pixel/math partition differ',pairset)
    # none of the white path channels may leak into the background
    background=label_point(F(pix.x,scale)+1,792-(F(pix.y,scale)+1))
    assert all(background!=region for grp,region in pairset)
    results.append({'diagram':tag,'mathematical_arcs':expected,'distinct_white_channels':len(pairset),'all_segment_midpoints_white':True})
check(0,paths(465,390,6,w=80,closed=False),8,'open six-crossing machine')
for cx,yt,n in [(115,557,1),(306,557,2),(495,557,3),(190,323,4),(435,323,6)]:check(1,paths(cx,yt,n),n,f'{n}-crossing closure')
yt=445;parts=paths(135,yt,3,cutright=True)+paths(475,yt,3,cutleft=True)+[[(F(200),F(yt)-32),(F(410),F(yt)-32)],[(F(200),F(yt)-58),(F(410),F(yt)-58)]]
check(2,parts,6,'joined three plus three')
yt=244;parts=paths(135,yt,3,cutright=True)+[[(F(410),F(yt)-32),(F(410),F(yt)+15),(F(525),F(yt)+15),(F(525),F(yt)-120),(F(410),F(yt)-120),(F(410),F(yt)-58)],[(F(200),F(yt)-32),(F(410),F(yt)-32)],[(F(200),F(yt)-58),(F(410),F(yt)-58)]]
check(2,parts,3,'joined three plus plain')
Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
