"""Coordinator lattice-area checks: manual guide data, no author imports."""
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from pathlib import Path
import json

def cross(a,b,p):return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
def info(poly):
    edges=list(zip(poly,poly[1:]+poly[:1]));boundary=[];inside=[]
    for x in range(min(p[0] for p in poly),max(p[0] for p in poly)+1):
        for y in range(min(p[1] for p in poly),max(p[1] for p in poly)+1):
            p=(x,y)
            if any(cross(a,b,p)==0 and min(a[0],b[0])<=x<=max(a[0],b[0]) and min(a[1],b[1])<=y<=max(a[1],b[1]) for a,b in edges):boundary.append(p);continue
            winding=0
            for a,b in edges:
                if a[1]<=y<b[1] and cross(a,b,p)>0:winding+=1
                if b[1]<=y<a[1] and cross(a,b,p)<0:winding-=1
            if winding:inside.append(p)
    area=F(abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in edges)),2)
    assert len(boundary)==sum(gcd(abs(b[0]-a[0]),abs(b[1]-a[1])) for a,b in edges)
    return {'I':len(inside),'B':len(boundary),'area':str(area),'Q':str(len(inside)+F(len(boundary),2)-1),'inside':inside,'boundary':boundary}
polys={
 'P1_rectangle':[(0,1),(3,1),(3,3),(0,3)],
 'P1_slanted':[(0,0),(2,0),(3,3),(1,3)],
 'P2_L':[(0,0),(3,0),(3,1),(1,1),(1,3),(0,3)],
 'P2_triangle':[(0,0),(3,0),(1,3)],
 'P3_triangle':[(0,0),(4,0),(1,2)],
 'P3_quad':[(0,0),(2,0),(3,2),(1,2)],
 'P5_I0':[(0,0),(6,0),(6,1),(0,1)],
 'P5_I1':[(0,0),(5,0),(5,1),(4,1),(3,2),(2,1),(0,1)],
 'P5_I2':[(0,0),(3,0),(3,2),(0,2)],
 'P5_I3':[(0,0),(3,0),(4,2),(1,2)],
 'P5_I4':[(0,0),(2,0),(3,3),(1,3)],
 'P5_I5':[(0,0),(2,1),(6,6),(4,5)],
 'P8_triangle':[(0,0),(4,1),(1,3)],
 'P8_concave':[(0,0),(4,0),(4,3),(2,2),(0,3)]}
out={k:info(p) for k,p in polys.items()}
expected={'P1_rectangle':(2,10,F(6)),'P1_slanted':(4,6,F(6)),'P2_L':(0,12,F(5)),
 'P2_triangle':(3,5,F(9,2)),'P3_triangle':(2,6,F(4)),'P3_quad':(2,6,F(4)),
 'P8_triangle':(5,3,F(11,2)),'P8_concave':(5,12,F(10))}
for k,(i,b,a) in expected.items():assert (out[k]['I'],out[k]['B'],F(out[k]['area']))==(i,b,a)
for i in range(6):assert (out[f'P5_I{i}']['I'],out[f'P5_I{i}']['B'],F(out[f'P5_I{i}']['area']))==(i,14-2*i,6)
seams=[([(0,0),(2,0),(2,2),(0,2)],[(2,0),(4,0),(4,2),(2,2)],[(0,0),(4,0),(4,2),(0,2)],3),
 ([(0,0),(2,0),(3,3)],[(0,0),(3,3),(1,3)],polys['P1_slanted'],4),
 ([(0,0),(2,0),(0,1)],[(2,0),(2,1),(0,1)],[(0,0),(2,0),(2,1),(0,1)],2)]
for p1,p2,whole,k in seams:
    a,b,c=map(info,(p1,p2,whole));assert c['I']==a['I']+b['I']+k-2 and c['B']==a['B']+b['B']-2*k+2
    assert F(c['area'])==F(a['area'])+F(b['area'])
out['seams']=[{'pieces':[info(a),info(b)],'whole':info(c),'k':k} for a,b,c,k in seams]
def hole(outer,holes):
    o=info(outer);hs=[info(h) for h in holes]
    interior=set(map(tuple,o['inside']));boundary=set(map(tuple,o['boundary']))
    for h in hs:
        interior-=set(map(tuple,h['inside']+h['boundary']));boundary|=set(map(tuple,h['boundary']))
    area=F(o['area'])-sum(F(h['area']) for h in hs);i,b=len(interior),len(boundary)
    assert area==i+F(b,2)-1+len(holes)
    return (i,b,str(area))
out['holes']=[hole([(0,0),(4,0),(4,4),(0,4)],[[(1,1),(3,1),(3,3),(1,3)]]),
 hole([(0,0),(6,0),(6,3),(0,3)],[[(1,1),(2,1),(2,2),(1,2)]]),
 hole([(0,0),(6,0),(6,4),(0,4)],[[(1,1),(2,1),(2,2),(1,2)],[(4,1),(5,1),(5,2),(4,2)]])]
assert out['holes']==[(0,24,'12'),(6,22,'17'),(7,28,'22')]
axis=bridge=0
for triple in combinations([(x,y) for x in range(5) for y in range(5)],3):
    if cross(*triple)==0:continue
    t=info(list(triple));assert t['area']==t['Q']
    if any(a[0]==b[0] or a[1]==b[1] for a,b in combinations(triple,2)):axis+=1;continue
    a,b,c=sorted(triple);ds=[(b[0],a[1]),(b[0],c[1])];d=next(p for p in ds if cross(a,c,p)*cross(a,c,b)<0)
    assert cross(b,d,a)*cross(b,d,c)<0
    abc,acd,abd,bcd,quad=[info(list(p)) for p in [(a,b,c),(a,c,d),(a,b,d),(b,c,d),(a,b,c,d)]]
    for field in ['area','Q']:
        assert F(abc[field])+F(acd[field])==F(quad[field])==F(abd[field])+F(bcd[field])
    bridge+=1
assert (axis,bridge)==(1600,548)
out['proof_cases']={'axis_side':axis,'bridge':bridge,'total':axis+bridge,
 'review':'General geometric bridge and legal-join ear induction reviewed independently; these finite cases do not prove the general theorem.'}
assert 12+10+10+10+6+3==51 and 3*3+10+6==25
assert 60+120//2==120
out['preparation']={'full_student_sheets':51,'first_visit_student_sheets':25,'raw_squares':120,'intact_squares':60,'halves':120}
p=Path(__file__).parent/'guide-review-assets/independent-guide-checks.json';p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n')
print('All guide keys, six area6 records, three seam lengths, three hole cases and2148 proof cases verified.')
