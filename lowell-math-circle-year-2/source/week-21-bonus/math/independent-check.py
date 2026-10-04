#!/usr/bin/env python3
"""Independent exact reflection geometry and rectangle visibility checks."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
from math import sqrt,isclose
import json
import hashlib

def point(x,y): return (F(x),F(y))
def reflect(p,y): return p[0],2*y-p[1]
def sqdist(a,b): return sum((x-y)**2 for x,y in zip(a,b))
def cross_y(a,b,y):
    t=(y-a[1])/(b[1]-a[1]);return (a[0]+t*(b[0]-a[0]),y)
A=point(1,3);B=point(7,5);low=F(1);high=F(7)
img1=reflect(reflect(B,high),low)
M1=cross_y(A,img1,low);N1u=cross_y(A,img1,2*low-high);N1=reflect(N1u,low)
assert img1==point(7,-7) and M1==point(F(11,5),1) and N1==point(F(29,5),7) and sqdist(A,img1)==136
img2=reflect(reflect(B,low),high)
M2=cross_y(A,img2,high);N2u=cross_y(A,img2,2*high-low);N2=reflect(N2u,high)
assert img2==point(7,17) and M2==point(F(19,7),7) and N2==point(F(37,7),1) and sqdist(A,img2)==232
for M,N in ((M1,N1),(M2,N2)):
    assert 0<M[0]<8 and 0<N[0]<8
def route_len(vertices): return sum(sqrt(float(sqdist(a,b))) for a,b in zip(vertices,vertices[1:]))
assert isclose(route_len([A,M1,N1,B]),sqrt(136),abs_tol=1e-12)
assert isclose(route_len([A,M2,N2,B]),sqrt(232),abs_tol=1e-12)
folded=[point(F(2,5),1),point(1,0),point(3,2),point(4,F(6,5))]
upper=[folded[0],folded[1],folded[2],reflect(folded[3],F(2))]
lower=[upper[0],upper[1],reflect(upper[2],F(0)),reflect(upper[3],F(0))]
assert [sqdist(a,b) for a,b in zip(folded,folded[1:])]==[sqdist(a,b) for a,b in zip(upper,upper[1:])]==[sqdist(a,b) for a,b in zip(lower,lower[1:])]
assert lower[-1]==point(4,F(-14,5))
single_img=reflect(B,low);Mstar=cross_y(A,single_img,low)
assert Mstar==point(3,1)
win_left=point(2,1);win_right=point(5,1)
assert (sqdist(A,win_left),sqdist(win_left,B))==(5,41)
assert (sqdist(A,win_right),sqdist(win_right,B))==(20,20)
assert 41<45  # sqrt(5)+sqrt(41) < 4*sqrt(5), exact winner comparison

corners=[point(2,2),point(6,2),point(6,5),point(2,5)]
def crosses_open_rectangle(a,b):
    # Intersection of the two open coordinate intervals with 0<t<1.
    lo,hi=F(0),F(1)
    for start,end,mn,mx in zip(a,b,(F(2),F(2)),(F(6),F(5))):
        d=end-start
        if d==0:
            if not mn<start<mx:return False
        else:
            p,q=sorted(((mn-start)/d,(mx-start)/d));lo=max(lo,p);hi=min(hi,q)
    return lo<hi
assert crosses_open_rectangle(point(0,3),point(8,3))
assert not crosses_open_rectangle(corners[0],corners[1])
def visible_paths(height):
    a,b=point(0,height),point(8,height);routes=[]
    for n in range(5):
        for middle in permutations(corners,n):
            route=[a,*middle,b]
            if all(not crosses_open_rectangle(x,y) for x,y in zip(route,route[1:])):
                routes.append((route_len(route),route))
    best=min(x for x,p in routes)
    winners=[p for x,p in routes if isclose(x,best,abs_tol=1e-12)]
    return best,winners,len(routes)
p4_len,p4_routes,p4_checked=visible_paths(F(3))
p5_len,p5_routes,p5_checked=visible_paths(F(7,2))
assert isclose(p4_len,4+2*sqrt(5),abs_tol=1e-12) and len(p4_routes)==1
assert p4_routes[0]==[point(0,3),corners[0],corners[1],point(8,3)]
assert p5_len==9 and len(p5_routes)==2
def points(p):return [[str(x),str(y)] for x,y in p]
out={'week':21,'verified_tasks':[1,2,3,4,5],'issues':[],'P1':{'image':points([img1]),'contacts':points([M1,N1]),'length':'sqrt(136)','approx':sqrt(136)},'P2':{'image':points([img2]),'contacts':points([M2,N2]),'length':'sqrt(232)','approx':sqrt(232)},'shorter_order':'lower then upper','P3':{'unrestricted_contact':points([Mstar]),'window_winners':points([win_left,win_right]),'winner':points([win_left]),'left_length':'sqrt(5)+sqrt(41)','right_length':'4sqrt(5)'},'P4':{'minimum':'4+2sqrt(5)','routes':[points(p) for p in p4_routes],'visible_corner_paths_checked':p4_checked},'P5':{'minimum':9,'routes':[points(p) for p in p5_routes],'visible_corner_paths_checked':p5_checked},'non_task_unfolding':'Every reflected segment has exactly the same squared length as the preceding picture.'}
finalsrc=Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
if finalsrc.exists():
    assert finalsrc.read_bytes()==(Path(__file__).parent/'fixtures'/'reviewed-draft.tex').read_bytes()
    pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-21-bonus.pdf'
    out['final_audit']={'all_tasks_and_diagram_coordinates_identical_to_verified_draft':True,'issues':[],'source_sha256':hashlib.sha256(finalsrc.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
