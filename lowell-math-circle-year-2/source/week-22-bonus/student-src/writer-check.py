#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations
import json

points = dict(A=(F(1),F(0)),B=(F(5),F(0)),C=(F(8),F(2)),D=(F(7),F(6)),E=(F(3),F(7)),F=(F(0),F(3)))
target=(F(4),F(16,5))
def sub(a,b): return a[0]-b[0],a[1]-b[1]
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def orient(a,b,c): return cross(sub(b,a),sub(c,a))
def bary(a,b,c,p):
    total=orient(a,b,c)
    if not total: return None
    return orient(p,b,c)/total,orient(a,p,c)/total,orient(a,b,p)/total
def intersection(a,b,c,d):
    u,v=sub(b,a),sub(d,c);den=cross(u,v)
    if not den: return None
    t=cross(sub(c,a),v)/den;s=cross(sub(c,a),u)/den
    if 0<=t<=1 and 0<=s<=1: return a[0]+t*u[0],a[1]+t*u[1]
    return None
def on_segment(p,a,b):
    return orient(a,b,p)==0 and all(min(a[i],b[i])<=p[i]<=max(a[i],b[i]) for i in (0,1))
def pairings(items):
    if not items: yield [];return
    a=items[0]
    for i in range(1,len(items)):
        for rest in pairings(items[1:i]+items[i+1:]):yield [(a,items[i])]+rest
pair_lines=[a+b for a,b in combinations(points,2) if orient(points[a],points[b],target)==0]
assert not pair_lines
triangles={''.join(abc):[str(x) for x in bary(*(points[x] for x in abc),target)] for abc in combinations(points,3) if all(x>=0 for x in bary(*(points[x] for x in abc),target))}
assert triangles
success=[]
for pairs in pairings(list(points)):
    (a,b),(c,d),(e,f)=pairs
    q=intersection(points[a],points[b],points[c],points[d])
    if q is not None and on_segment(q,points[e],points[f]):success.append(pairs)
assert not success
q=intersection(points['A'],points['D'],points['B'],points['E'])
assert q==(F(37,9),F(28,9))
cf_y=points['C'][1]+(q[0]-points['C'][0])*(points['F'][1]-points['C'][1])/(points['F'][0]-points['C'][0])
assert cf_y!=q[1]
print(json.dumps({'target_pair_lines':pair_lines,'containing_triangles':triangles,'AD_BE_intersection':[str(v) for v in q],'CF_y_at_intersection_x':str(cf_y),'generic_three_pair_successes':success},indent=2))
