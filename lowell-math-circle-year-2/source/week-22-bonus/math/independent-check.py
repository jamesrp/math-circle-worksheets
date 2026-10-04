#!/usr/bin/env python3
"""Independent exact planar hull and all three-group partition checks."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from math import sin,cos,pi,hypot,isclose
import json
import hashlib
def p(x,y): return F(x),F(y)
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def orient(a,b,c):return cross(sub(b,a),sub(c,a))
def hull(points):
    points=sorted(set(points))
    if len(points)<2:return points
    lower=[];upper=[]
    for x in points:
        while len(lower)>1 and orient(lower[-2],lower[-1],x)<=0:lower.pop()
        lower.append(x)
    for x in reversed(points):
        while len(upper)>1 and orient(upper[-2],upper[-1],x)<=0:upper.pop()
        upper.append(x)
    return lower[:-1]+upper[:-1]
def contains(H,t):
    if not H:return False
    if len(H)==1:return H[0]==t
    if len(H)==2:
        a,b=H;return orient(a,b,t)==0 and all(min(x,y)<=z<=max(x,y) for x,y,z in zip(a,b,t))
    return all(orient(a,b,t)>=0 for a,b in zip(H,H[1:]+H[:1]))
def edges(H):
    if len(H)<2:return []
    if len(H)==2:return [(H[0],H[1])]
    return list(zip(H,H[1:]+H[:1]))
def intersection(a,b,c,d):
    u,v=sub(b,a),sub(d,c);den=cross(u,v)
    if den:
        t=cross(sub(c,a),v)/den;s=cross(sub(c,a),u)/den
        if 0<=t<=1 and 0<=s<=1:return [(a[0]+t*u[0],a[1]+t*u[1])]
        return []
    return list({x for x in (a,b,c,d) if contains([a,b],x) and contains([c,d],x)})
def common(Hs):
    candidates={t for H in Hs for t in H}
    for H,K in combinations(Hs,2):
        for a,b in edges(H):
            for c,d in edges(K):candidates.update(intersection(a,b,c,d))
    return sorted(t for t in candidates if all(contains(H,t) for H in Hs))
def partitions(n,k=3):
    # Restricted-growth partitions, unlabeled groups, every label used once.
    def rec(i,groups):
        if i==n:
            if len(groups)==k:yield tuple(tuple(g) for g in groups)
            return
        for j in range(len(groups)):
            groups[j].append(i);yield from rec(i+1,groups);groups[j].pop()
        if len(groups)<k:
            groups.append([i]);yield from rec(i+1,groups);groups.pop()
    yield from rec(0,[])

dots=[p(1,0),p(5,0),p(8,2),p(7,6),p(3,7),p(0,3)]
T=p(4,F(16,5));assert len(hull(dots))==6 and contains(hull(dots),T)
support={}
for n in (1,2,3):support[n]=[ids for ids in combinations(range(6),n) if contains(hull([dots[i] for i in ids]),T)]
assert not support[1] and not support[2] and support[3]
one=dots[0];two=p(3,0)
assert contains(hull([dots[0]]),one)
assert not any(two==t for t in dots) and contains(hull(dots[:2]),two)
square=[p(1,1),p(7,1),p(7,7),p(1,7)]
assert common([hull([square[0],square[2]]),hull([square[1],square[3]])])==[p(4,4)]
assert all(t[1]<4 for t in square[:2]) and all(t[1]>4 for t in square[2:])
line5=[p(x,6) for x in (1,2,4,5,7)];line4=[p(x,2) for x in (1,3,5,7)]
def audit(points):
    tested=0;wins=[]
    for groups in partitions(len(points)):
        tested+=1;C=common([hull([points[i] for i in group]) for group in groups])
        if C:wins.append((groups,C))
    return tested,wins
n5,w5=audit(line5);n4,w4=audit(line4)
assert n5==25 and len(w5)==2 and n4==6 and not w4
# Exact affine image of the printed regular hexagon, removing sqrt(3).
regular=[p(2,0),p(1,1),p(-1,1),p(-2,0),p(-1,-1),p(1,-1)]
nr,wr=audit(regular);ng,wg=audit(dots)
assert nr==ng==90 and len(wr)==1 and not wg
assert wr[0][0]==((0,3),(1,4),(2,5)) and wr[0][1]==[p(0,0)]
allpairings=[g for g in partitions(6) if all(len(a)==2 for a in g)]
assert len(allpairings)==15
crossing_pairings=[]
for g in allpairings:
    Hs=[hull([dots[i] for i in a]) for a in g]
    if all(common([a,b]) for a,b in combinations(Hs,2)):crossing_pairings.append(g)
assert crossing_pairings==[((0,3),(1,4),(2,5))]
AD_BE=intersection(dots[0],dots[3],dots[1],dots[4])[0]
assert AD_BE==p(F(37,9),F(28,9)) and not contains(hull([dots[2],dots[5]]),AD_BE)
assert orient(dots[2],dots[5],AD_BE)==-5
numeric=[(4+3.5*cos(t*pi/3),4+3.5*sin(t*pi/3)) for t in range(6)]
assert all(isclose(hypot(a[0]-b[0],a[1]-b[1]),3.5,abs_tol=1e-12) for a,b in zip(numeric,numeric[1:]+numeric[:1]))
# Actual non-task example consists of translated copies of one triangle.
assert [p(0,0),p(3,0),p(1,2)]==[p(x-F(11,2),y) for x,y in (p(F(11,2),0),p(F(17,2),0),p(F(13,2),2))]
def names(ids):return ''.join(chr(65+i) for i in ids)
def pt(t):return [str(x) for x in t]
out={'week':22,'verified_tasks':[1,2,3,4,5,6],'issues':[],'P1_minimum_support':3,'P1_successful_triples':[names(g) for g in support[3]],'P1_successful_pairs':0,'P2_one_dot_target':pt(one),'P2_two_dot_target':pt(two),'P2_three_dot_target':pt(T),'P2_four_required':False,'P3_AC_BD_intersection':pt(p(4,4)),'P3_AB_CD_separator':'y=4','P4_five_line_partitions_checked':n5,'P4_five_line_successes':[{'groups':[names(g) for g in groups],'common':[pt(t) for t in C]} for groups,C in w5],'P4_four_line_partitions_checked':n4,'P4_four_line_successes':0,'P5_regular_partitions_checked':nr,'P5_regular_successes':1,'P5_regular_split':['AD','BE','CF'],'P5_printed_common_point':[4,4],'P6_irregular_partitions_checked':ng,'P6_irregular_successes':0,'P6_pairings_checked':15,'P6_only_pairwise_crossing_pairing':['AD','BE','CF'],'P6_AD_BE_intersection':pt(AD_BE),'P6_CF_noncollinearity_determinant':-5,'regular_hexagon_equal_axes_and_side_lengths':'verified from source coordinates and numeric check; exact affine model used for intersection enumeration'}
finalsrc=Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
if finalsrc.exists():
    assert finalsrc.read_bytes()==(Path(__file__).parent/'fixtures'/'reviewed-draft.tex').read_bytes()
    pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-22-bonus.pdf'
    out['final_audit']={'all_tasks_and_diagram_coordinates_identical_to_verified_draft':True,'issues':[],'source_sha256':hashlib.sha256(finalsrc.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
