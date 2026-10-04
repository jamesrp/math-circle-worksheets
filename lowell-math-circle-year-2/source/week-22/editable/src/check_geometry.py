from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

def pt(p):return tuple(F(str(x)) for x in p)
def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
    points=sorted(set(points))
    if len(points)<=1:return points
    lo=[];hi=[]
    for p in points:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(points):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]
def onseg(p,a,b):return cross(a,b,p)==0 and all(min(a[i],b[i])<=p[i]<=max(a[i],b[i]) for i in (0,1))
def contains(h,p):
    if len(h)==1:return h[0]==p
    if len(h)==2:return onseg(p,*h)
    return all(cross(a,b,p)>=0 for a,b in zip(h,h[1:]+h[:1]))
def edges(h):
    if len(h)<2:return []
    if len(h)==2:return [h]
    return list(zip(h,h[1:]+h[:1]))
def intersects(a,b,c,d):
    v=[cross(a,b,c),cross(a,b,d),cross(c,d,a),cross(c,d,b)]
    if v[0]*v[1]<0 and v[2]*v[3]<0:return True
    return onseg(a,c,d) or onseg(b,c,d) or onseg(c,a,b) or onseg(d,a,b)
def meet(h,k):
    return any(contains(k,p) for p in h) or any(contains(h,p) for p in k) or any(intersects(*a,*b) for a in edges(h) for b in edges(k))
def wins(points):
    points={k:pt(v) for k,v in points.items()}
    labels=list(points)
    out=[]
    for n in range(1,len(labels)):
        for a in combinations(labels,n):
            if labels[0] not in a:continue
            b=tuple(x for x in labels if x not in a)
            if meet(hull([points[x] for x in a]),hull([points[x] for x in b])):
                out.append(''.join(a)+' | '+''.join(b))
    return out

results={}
configsets={
 'k_p1':({'A':(2,2),'B':(10,3),'C':(4,10)},[(9,9),(4.3,4.7),(0.8,7.2)]),
 'k_p2':({'A':(2,3),'B':(8,3),'C':(5,10)},[(5,3),(11,3),(3.5,6.5)]),
 '23_p1':({'A':(2,3),'B':(10,2),'C':(3,10)},[(9,9),(4,5),(6,2.5),(6,1)]),
 '45_p1':({'A':(2,2),'B':(10.5,3),'C':(4.5,10)},[(9.8,9),(5,5),(6.25,2.5),(1,6)]),
}
for name,(base,ds) in configsets.items():
    for i,d in enumerate(ds,1):
        w=wins(dict(base,D=d));assert w
        results[f'{name}_position_{i}']=w
for name,points in {
 'k_p3':{'A':(1.8,6.3),'B':(10.8,6.3),'C':(7.5,6.3),'D':(4.5,6.3)},
 '23_p2':{'A':(2,6.3),'B':(7.8,6.3),'C':(10.8,6.3),'D':(4.6,6.3)},
 '45_p2':{'A':(2,3),'B':(8,9),'C':(5,6),'D':(10,11)},
 '45_p4':{'A':(3,3),'B':(10,4.5),'C':(5.5,10),'D':(3,3)}
}.items():
    results[name]=wins(points);assert len(results[name])==4
for i,c in enumerate([(6,5.6),(11,5.6),(5.5,9.5)],1):
    w=wins({'A':(2.5,5.6),'B':(8.8,5.6),'C':c})
    results[f'k_p5_position_{i}']=w
    assert bool(w)==(i<3)
for name,points in {
 '23_p5':{'A':(2,3),'B':(10,4),'C':(6,10)},
 '45_p7':{'A':(2,3),'B':(10.3,4),'C':(4.8,10.1)}
}.items():
    results[name]=wins(points);assert not results[name]
# The revised K-1 P5 locus includes both extensions and both fixed points.
for x in [0,1,2.5,4,8.8,10,12.6]:
    assert wins({'A':(2.5,5.6),'B':(8.8,5.6),'C':(x,5.6)})
    for y in [0,5.5,5.7,12.6]:
        assert not wins({'A':(2.5,5.6),'B':(8.8,5.6),'C':(x,y)})
# Witnesses for construction tasks: two unique, disjoint successful-split sets.
outer={'A':(2,2),'B':(10,3),'C':(4,10),'D':(9,9)}
inner=dict(outer,D=(4.3,4.7))
wa,wb=wins(outer),wins(inner)
assert len(wa)==len(wb)==1 and set(wa).isdisjoint(wb)
results['unique_split_construction_examples']=[wa,wb]
# Two opposite pairs on a common line share a segment of positive length.
assert 'AB | CD' in wins({'A':(1,0),'B':(9,0),'C':(3,0),'D':(7,0)})
# 2 + 2 or 1 + 3 is unavoidable for four labels, so at least one hull has
# dimension at most one. A shared nondegenerate filled triangle is impossible.
out=Path(__file__).with_name('geometry-check.json')
out.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
print('All exact geometric checks passed.')
