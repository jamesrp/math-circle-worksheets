#!/usr/bin/env python3
"""Check every regular polygon board and each general quadrilateral flip example."""
from pathlib import Path
from collections import Counter
import json, math, re
ROOT=Path(__file__).resolve().parent
COORD=re.compile(r'\\coordinate \(v(\d+)\) at \((-?[\d.]+),(-?[\d.]+)\);')
EXPECTED={
    'src/k-1.tex': {5:26,6:27},
    'src/grades-2-3.tex': {5:23,6:42,7:3},
    'src/grades-4-5.tex': {5:14,6:23,8:13},
    'facilitator-src/facilitator-guide.tex': {5:7,6:38,8:9},
}
counts={}; exceptions={}; worst_side=0; worst_angle=0
for name,expected in EXPECTED.items():
    source=(ROOT/name).read_text()
    if name.startswith('src/'):
        blocks=re.findall(r'% polygon: (regular|general-convex) n=(\d+)\n(.*?)(?=\\end\{scope\})',source,re.S)
        assert len(blocks)==len(re.findall(r'\\coordinate \(v0\)',source)), (name,'unclassified polygon')
    else:
        blocks=[('regular',None,b) for b in re.split(r'(?=\\coordinate \(v0\))',source) if COORD.search(b)]
    found=Counter(); general=0
    for kind,declared,block in blocks:
        vertices=[(int(i),float(x),float(y)) for i,x,y in COORD.findall(block)]
        n=len(vertices)
        assert n>=3 and (declared is None or n==int(declared)),(name,'vertex count')
        assert [v[0] for v in vertices]==list(range(n)),(name,'vertex order')
        p=[(x,y) for _,x,y in vertices]
        sides=[math.dist(p[i],p[(i+1)%n]) for i in range(n)]
        angles=[]; crosses=[]
        for i in range(n):
            a=p[i-1];b=p[i];c=p[(i+1)%n]
            u=(a[0]-b[0],a[1]-b[1]);v=(c[0]-b[0],c[1]-b[1])
            co=sum(x*y for x,y in zip(u,v))/(math.hypot(*u)*math.hypot(*v))
            angles.append(math.degrees(math.acos(max(-1,min(1,co)))))
            crosses.append(u[0]*v[1]-u[1]*v[0])
        assert all(x>0 for x in crosses) or all(x<0 for x in crosses),(name,'nonconvex polygon')
        if kind=='general-convex':
            # The AC-to-BD insets illustrate flips on an arbitrary convex quadrilateral.
            assert n==4 and name in ('src/grades-2-3.tex','src/grades-4-5.tex'),(name,'unexpected exception')
            general+=1;continue
        side_error=max(sides)-min(sides)
        angle_error=max(abs(a-(n-2)*180/n) for a in angles)
        assert side_error<.0003,(name,n,'unequal sides',sides)
        assert angle_error<.025,(name,n,'unequal angles',angles)
        worst_side=max(worst_side,side_error);worst_angle=max(worst_angle,angle_error)
        found[n]+=1
    assert dict(found)==expected,(name,'unexpected regular polygon counts',dict(found))
    assert general==(2 if name in ('src/grades-2-3.tex','src/grades-4-5.tex') else 0),(name,'unexpected general examples',general)
    counts[name]=dict(found);exceptions[name]=general
# The fan-distance proof has two local general-quadrilateral close-ups, not boards.
guide=(ROOT/'facilitator-src/facilitator-guide.tex').read_text()
proof_blocks=re.findall(r'\\coordinate\(a\) at\(0,0\);(.*?)(?=\\end\{scope\})',guide,re.S)
assert len(proof_blocks)==2,('unexpected proof quadrilateral count',len(proof_blocks))
for block in proof_blocks:
    tail=re.findall(r'\\coordinate\(([uxw])\) at\((-?[\d.]+),(-?[\d.]+)\);',block)
    assert tail==[('u','2.5','0'),('x','3','2'),('w','.4','2.7')],('proof geometry changed',tail)
    p=[(0,0)]+[(float(x),float(y)) for _,x,y in tail]
    turns=[]
    for i in range(4):
        a,b,c=p[i-1],p[i],p[(i+1)%4]
        turns.append((a[0]-b[0])*(c[1]-b[1])-(a[1]-b[1])*(c[0]-b[0]))
    assert all(x>0 for x in turns) or all(x<0 for x in turns),'nonconvex proof close-up'
exceptions['facilitator-src/facilitator-guide.tex']=len(proof_blocks)
print(json.dumps({'regular_polygon_counts':counts,'total_regular_boards':sum(sum(v.values()) for v in counts.values()),'general_convex_quadrilateral_examples':exceptions,'total_general_examples':sum(exceptions.values()),'maximum_side_spread_source_units':worst_side,'maximum_angle_error_degrees':worst_angle,'maximum_coordinate_rounding':.0001,'all_sides_and_angles_checked':True},indent=2))
