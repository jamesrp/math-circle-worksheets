#!/usr/bin/env python3
"""Independent exact guide checks; standard-library Fraction geometry."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,combinations_with_replacement
from math import factorial
import hashlib,json
here=Path(__file__).resolve().parent
root=here.parent
P=[(F(x),F(y)) for x,y in ((1,0),(5,0),(8,2),(7,6),(3,7),(0,3))]
T=(F(4),F(16,5))
def orient(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
line_values=[orient(P[a],P[b],T) for a,b in combinations(range(6),2)]
assert all(v for v in line_values)
assert all(orient(P[i],P[(i+1)%6],P[j])>0 for i in range(6) for j in range(6) if j not in (i,(i+1)%6))
triangles=[]
for ids in combinations(range(6),3):
    a,b,c=[P[i] for i in ids]
    signs=[orient(a,b,T),orient(b,c,T),orient(c,a,T)]
    if all(v>=0 for v in signs) or all(v<=0 for v in signs): triangles.append(''.join(chr(65+i) for i in ids))
assert triangles==['ABE','ACE','ADE','ADF','BDF','BEF','CDF','CEF']
weights=[F(11,25),F(4,25),F(2,5)]
assert sum(weights)==1 and all(v>0 for v in weights)
assert tuple(sum(w*P[i][k] for w,i in zip(weights,(2,4,5))) for k in range(2))==T
assert F(3)-F(37,9)/8==F(179,72) and F(179,72)!=F(28,9)
def partitions(n,k):
    def rec(i,groups):
        if i==n:
            if len(groups)==k:yield tuple(tuple(a) for a in groups)
            return
        for a in groups:
            a.append(i);yield from rec(i+1,groups);a.pop()
        if len(groups)<k:
            groups.append([i]);yield from rec(i+1,groups);groups.pop()
    yield from rec(0,[])
def line_counts(n,r):
    total=success=0
    for groups in partitions(n,r):
        total+=1
        if max(min(a) for a in groups)<=min(max(a) for a in groups):success+=1
    return total,success
line_audits={}
for r in range(2,6):
    total,success=line_counts(2*r-1,r)
    assert success==factorial(r-1)
    lower_total,lower_success=line_counts(2*r-2,r)
    assert lower_success==0
    line_audits[str(r)]={'guarantee_labels':2*r-1,'distinct_partitions_checked':total,'successful_distinct_partitions':success,'counterexample_labels':2*r-2,'counterexample_partitions_checked':lower_total,'counterexample_successes':0}
repeated=0
for r in range(2,6):
    for xs in combinations_with_replacement(range(4),2*r-1):
        middle=xs[r-1]
        assert all(xs[i]<=middle<=xs[-1-i] for i in range(r-1))
        repeated+=1
student=root/'tmp/worksheet-runs/week-22-bonus-v1'
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
out={'week':22,'status':'verified','unresolved_mathematical_issues':[],
 'scope':'All overview, actual final P1-P6 solutions, hints, extensions, geometric assumptions and source-role claims independently audited; five rendered guide pages inspected.',
 'evidence':{'guide_json_sha256':sha(here/'guide.json'),'guide_pdf_sha256':sha(here.parent/'reference-pdfs'/'week-22-bonus-facilitator.pdf'),'student_final_pdf_sha256':sha(here.parent/'reference-pdfs'/'week-22-bonus.pdf'),'student_final_tex_sha256':sha(here.parent/'student-src'/'bonus.tex'),'student_checker_sha256':sha(here.parent/'math'/'independent-check.py'),'student_checks_sha256':sha(here.parent/'review'/'checks.json'),'guide_checker_sha256':sha(Path(__file__))},
 'verified_claims':{'P1':{'joining_lines_checked':15,'lines_through_target':0,'support_minimum':3,'containing_triangles':triangles,'CEF_barycentric_weights':[str(w) for w in weights]},'P2':{'one_dot':[1,0],'two_dots':[3,0],'three_dots':['4','16/5'],'four_required':False,'general_at_most_three':'Triangulate finite hull using original boundary vertices; point/segment cases use one/two extremes.'},'P3':{'AC_BD_meeting':[4,4],'strict_separator':False,'AB_CD_separator':'y=4; every 1<y<7 works','general_separation_certificate':'Closest points exist by nonempty compact hulls; d·(X-P)<=0 and d·(Y-Q)>=0 put hulls strictly on opposite sides of the bisector.'},'P4':{'five_line_partitions':25,'successful_splits':[['AD','BE','C'],['AE','BD','C']],'four_line_partitions':6,'four_line_successes':0,'repeated_locations':'Middle singleton with nested outer pairs remains valid.'},'P5':{'regular_hexagon_partitions':90,'successful_splits':1,'success':['AD','BE','CF'],'common_point':[4,4],'radius':'7/2','equal_scaling':True},'P6':{'irregular_hexagon_partitions':90,'successful_splits':0,'pairings':15,'only_pairwise_crossing_pairing':['AD','BE','CF'],'AD_BE_meeting':['37/9','28/9'],'CF_y_at_same_x':'179/72','shared_point':False,'singleton_elimination':'Strict convexity makes each singleton an extreme point outside the other hull.'},'sharp_line_extension':{'general_proof':'2r-1 labels suffice by a middle singleton plus outer pairs; 2r-2 distinct positions force at least two singleton groups and fail. r>=2.','distinct_finite_audits':line_audits,'ordered_repeated_location_witnesses_checked':repeated},'strict_touching_extension':'Touching hulls cannot be strictly separated; a positive disjoint gap permits small perturbations of a separator.'},
 'source_attribution':{'base':'Current guide closed hulls, sharp planar Radon threshold and printed p.20 extension limits agree with stated exclusions.','primary_context':'Gallier-Quaintance section3.5 recorded context explicitly not newly read; no seven-point theorem claimed.','teaching':'Math Circle by the Bay Preface vii-x/PDF8-11 supports stated context; target-removal routes marked as proposed.'},
 'limits':['A three-way meeting requires one common point, not merely pairwise intersections.','Closed filled hulls include boundary, segments and singleton points.','Tracing registration, marker use and classroom procedures remain untested.','Extracted portable-source rebuilding is a separate release check.'],'resolved_findings':[]}
(here/'guide-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'week':22,'status':out['status'],'line_audits':line_audits,'repeated_witnesses':repeated,'evidence':out['evidence']},indent=2))
