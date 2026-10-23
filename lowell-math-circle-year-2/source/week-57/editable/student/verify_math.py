#!/usr/bin/env python3
"""Independent exact point/geometry checks for every printed polygon and task."""
import argparse
import ast
import itertools
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json


def cross(a,b,p):
    return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])


def on_segment(a,b,p):
    return cross(a,b,p)==0 and min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and min(a[1],b[1])<=p[1]<=max(a[1],b[1])


def intersect(a,b,c,d):
    if any((on_segment(a,b,c),on_segment(a,b,d),on_segment(c,d,a),on_segment(c,d,b))): return True
    return (cross(a,b,c)*cross(a,b,d)<0 and cross(c,d,a)*cross(c,d,b)<0)


def validate(poly):
    assert len(poly)==len(set(map(tuple,poly)))
    assert all(isinstance(v,int) for p in poly for v in p)
    edges=list(zip(poly,poly[1:]+poly[:1]))
    for i,(a,b) in enumerate(edges):
        assert a!=b
        for j,(c,d) in enumerate(edges):
            if i>=j or j==i+1 or (i==0 and j==len(edges)-1): continue
            assert not intersect(a,b,c,d),(i,j,poly)
    assert area(poly)>0


def classify(poly,p):
    """Exact ray crossing parity, independent of generator's winding number."""
    hits=0
    for a,b in zip(poly,poly[1:]+poly[:1]):
        if on_segment(a,b,p): return 'boundary'
        if (a[1]>p[1])!=(b[1]>p[1]):
            crossing=F(a[0])+F(p[1]-a[1],b[1]-a[1])*(b[0]-a[0])
            hits += crossing>p[0]
    return 'inside' if hits%2 else 'outside'


def area(poly):
    return F(abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(poly,poly[1:]+poly[:1]))),2)


def expression(s):
    def visit(n):
        if isinstance(n,ast.Constant) and isinstance(n.value,int): return F(n.value)
        if isinstance(n,ast.BinOp):
            a,b=visit(n.left),visit(n.right)
            if isinstance(n.op,ast.Add): return a+b
            if isinstance(n.op,ast.Sub): return a-b
            if isinstance(n.op,ast.Mult): return a*b
            if isinstance(n.op,ast.Div): return a/b
        raise ValueError(s)
    return visit(ast.parse(s,mode='eval').body)


def data(poly,holes=None):
    holes=holes or []
    validate(poly)
    for hole in holes:
        validate(hole)
        assert all(classify(poly,v)=='inside' for v in hole)
        for a,b in zip(poly,poly[1:]+poly[:1]):
            assert all(not intersect(a,b,c,d) for c,d in zip(hole,hole[1:]+hole[:1]))
    for i,hole in enumerate(holes):
        for other in holes[i+1:]:
            assert all(classify(other,v)=='outside' for v in hole)
            assert all(classify(hole,v)=='outside' for v in other)
            assert all(not intersect(a,b,c,d) for a,b in zip(hole,hole[1:]+hole[:1]) for c,d in zip(other,other[1:]+other[:1]))
    inside=[];boundary=[]
    for x in range(min(p[0] for p in poly),max(p[0] for p in poly)+1):
        for y in range(min(p[1] for p in poly),max(p[1] for p in poly)+1):
            p=(x,y);outer=classify(poly,p);h=[classify(hole,p) for hole in holes]
            if outer=='boundary' or 'boundary' in h: boundary.append(p)
            elif outer=='inside' and all(v=='outside' for v in h): inside.append(p)
    a=area(poly)-sum((area(h) for h in holes),F(0))
    b_gcd=sum(gcd(abs(a[0]-b[0]),abs(a[1]-b[1])) for loop in [poly]+holes for a,b in zip(loop,loop[1:]+loop[:1]))
    assert len(boundary)==b_gcd
    assert a==len(inside)+F(len(boundary),2)-1+len(holes)
    return dict(sides=len(poly),hole_sides=[len(h) for h in holes],I=len(inside),B=len(boundary),area=str(a),inside=inside,boundary=boundary)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
    cases=json.loads(Path(__file__).with_name('assets').joinpath('polygons.json').read_text())
    checked={}
    for name,c in cases.items():
        d=data(c['vertices'],c.get('holes'))
        assert d['sides']==c['sides']
        assert d['hole_sides']==c.get('hole_sides',[])
        assert (d['I'],d['B'],F(d['area']))==(c['expected'][0],c['expected'][1],F(c['expected'][2])),(name,d)
        assert F(d['area'])==expression(c['area_certificate']),name
        if c.get('draw',True):
            assert c['size_mm']==20
            w,h=c['board']
            assert all(0<=x<=w and 0<=y<=h for loop in [c['vertices']]+c.get('holes',[]) for x,y in loop)
        checked[name]=d
    p3=[[[0,0],[4,0],[1,2]],[[0,0],[2,0],[3,2],[1,2]]]
    construction=[]
    for poly in p3:
        d=data(poly);assert (d['I'],d['B'],F(d['area']))==(2,6,F(4));construction.append(dict(vertices=poly,**d))
    witnesses=[
        [[0,0],[6,0],[6,1],[0,1]],
        [[0,0],[5,0],[5,1],[4,1],[3,2],[2,1],[0,1]],
        [[0,0],[3,0],[3,2],[0,2]],
        [[0,0],[3,0],[4,2],[1,2]],
        [[0,0],[2,0],[3,3],[1,3]],
        [[0,0],[2,1],[6,6],[4,5]]]
    six=[]
    for i,poly in enumerate(witnesses):
        d=data(poly);assert (d['I'],d['B'],F(d['area']))==(i,14-2*i,F(6));six.append(dict(vertices=poly,**d))
    # With area 6, B=14-2I is even, and any polygon has B>=3.
    # Thus I=0,...,5 and B=14,12,10,8,6,4 are the complete possible records.
    seams=[]
    for whole,left,right in [('join-rectangle','join-rectangle-left','join-rectangle-right'),('join-slanted','join-slanted-lower','join-slanted-upper')]:
        d,l,r=checked[whole],checked[left],checked[right]
        a,b=cases[whole]['seams'][0];k=gcd(abs(a[0]-b[0]),abs(a[1]-b[1]))+1
        assert d['I']==l['I']+r['I']+k-2
        assert d['B']==l['B']+r['B']-2*k+2
        assert F(d['area'])==F(l['area'])+F(r['area'])
        seams.append(dict(whole=whole,k=k,interior_gain=k-2,boundary_loss=2*k-2))
    one_outer=[[0,0],[6,0],[6,3],[0,3]]
    one_holes=[[[1,1],[2,1],[2,2],[1,2]]]
    one=data(one_outer,one_holes);assert (one['I'],one['B'],F(one['area']))==(6,22,F(17))
    outer=[[0,0],[6,0],[6,4],[0,4]]
    holes=[[[1,1],[2,1],[2,2],[1,2]],[[4,1],[5,1],[5,2],[4,2]]]
    two=data(outer,holes);assert (two['I'],two['B'],F(two['area']))==(7,28,F(22))
    # Universal proof is in README. These finite tests check the bridge's
    # construction, legal diagonals, axis-side comparisons and exact identities.
    proof_tests=dict(axis_side_already=0,quadrilateral_bridge=0)
    for raw in itertools.combinations(itertools.product(range(5),repeat=2),3):
        if cross(*raw)==0: continue
        if any(a[0]==b[0] or a[1]==b[1] for a,b in zip(raw,raw[1:]+raw[:1])):
            proof_tests['axis_side_already']+=1;continue
        a,b,c=sorted(raw,key=lambda v:v[0])
        d=(b[0],c[1])
        if cross(a,c,b)*cross(a,c,d)>=0: d=(b[0],a[1])
        assert cross(a,c,b)*cross(a,c,d)<0
        assert cross(b,d,a)*cross(b,d,c)<0
        quad=[a,b,c,d]
        turns=[cross(quad[i-1],quad[i],quad[(i+1)%4]) for i in range(4)]
        assert all(v>0 for v in turns) or all(v<0 for v in turns)
        q=data(quad)
        t,ac_d,ab_d,bc_d=[data(list(v)) for v in [(a,b,c),(a,c,d),(a,b,d),(b,c,d)]]
        for poly in [(a,c,d),(a,b,d),(b,c,d)]:
            assert any(u[0]==v[0] or u[1]==v[1] for u,v in zip(poly,poly[1:]+poly[:1]))
        def Q(v):return v['I']+F(v['B'],2)-1
        assert F(q['area'])==F(t['area'])+F(ac_d['area'])==F(ab_d['area'])+F(bc_d['area'])
        assert Q(q)==Q(t)+Q(ac_d)==Q(ab_d)+Q(bc_d)
        # The seam's endpoint dots remain boundary in both joins.
        for x,y,endpoints in [(t,ac_d,{a,c}),(ab_d,bc_d,{b,d})]:
            shared=set(map(tuple,x['boundary']))&set(map(tuple,y['boundary']))
            assert shared&set(map(tuple,q['boundary']))==endpoints
            assert q['I']==x['I']+y['I']+len(shared)-2
            assert q['B']==x['B']+y['B']-2*len(shared)+2
        proof_tests['quadrilateral_bridge']+=1
    assert proof_tests==dict(axis_side_already=1600,quadrilateral_bridge=548)
    proof_example={name:dict(vertices=poly,**data(poly)) for name,poly in {
        'ABC':[[0,0],[2,1],[6,6]],
        'ACD':[[0,0],[6,6],[2,6]],
        'ABD':[[0,0],[2,1],[2,6]],
        'BCD':[[2,1],[6,6],[2,6]],
        'ABCD':[[0,0],[2,1],[6,6],[2,6]]}.items()}
    assert [F(proof_example[n]['area']) for n in ['ABC','ACD','ABD','BCD','ABCD']]==[3,12,5,10,15]
    result=dict(method='Exact ray parity and segment tests; shoelace area plus explicit geometric area certificates; gcd boundary count; no formula used to compute initial area.',printed_polygons=checked,problem3_witnesses=construction,problem5_complete_records=six,seams=seams,problem9_witness=dict(vertices=one_outer,holes=one_holes,**one),problem10_witness=dict(vertices=outer,holes=holes,**two),general_proof_bridge_tests=proof_tests,general_proof_bridge_example=proof_example,physical_pretest='unperformed',classroom_piloting='unperformed')
    target=Path(args.output);target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Checked {len(checked)} polygon definitions, fixed-count constructions, all six area-6 records, both joins, one-/two-hole witnesses and 2,148 proof-bridge cases.')


if __name__=='__main__': main()
