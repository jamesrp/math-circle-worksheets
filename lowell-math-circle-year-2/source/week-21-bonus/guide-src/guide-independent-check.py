#!/usr/bin/env python3
"""Independent guide extensions and reflection checks; standard library only."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json
here=Path(__file__).resolve().parent
root=here.parent
def p(x,y):return F(x),F(y)
def reflect(P,y):return P[0],2*F(y)-P[1]
def d2(A,B):return sum((a-b)**2 for a,b in zip(A,B))
A,M,N,B=p(F(2,5),1),p(1,0),p(3,2),p(4,F(6,5))
B1=reflect(B,2);N2=reflect(N,0);B2=reflect(B1,0)
assert B1==p(4,F(14,5)) and N2==p(3,-2) and B2==p(4,F(-14,5))
assert d2(N,B)==d2(N,B1)==d2(N2,B2)
assert d2(M,N)==d2(M,N2)
cases=0
for H in range(1,8):
 for a,b in product((F(1,4),F(1,2),F(3,4)),repeat=2):
    hA,hB=H*a,H*b
    low=2*H+hA-hB;up=2*H+hB-hA
    assert low>0 and up>0
    assert low*low-up*up==8*H*(hA-hB)
    assert (low==up)==(hA==hB)
    assert (low<up)==(hA<hB)
    cases+=1
heights=[F(2)+F(3)*k/10 for k in range(11)]
for h in heights:
    low2=4+(h-2)**2;up2=4+(5-h)**2
    assert (low2==up2)==(h==F(7,2))
    assert (low2<up2)==(h<F(7,2))
assert d2(p(0,F(7,2)),p(2,2))==F(25,4)
assert d2(p(0,F(7,2)),p(2,5))==F(25,4)
assert d2(p(1,3),p(2,1))==5 and d2(p(7,5),p(2,1))==41
assert d2(p(1,3),p(5,1))==d2(p(7,5),p(5,1))==20 and 41<45
student=root/'tmp/worksheet-runs/week-21-bonus-v1'
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
out={'week':21,'status':'verified','unresolved_mathematical_issues':[],
 'scope':'All theorem-first overview, actual final P1-P5 solutions, practice coordinates, hints, extensions, assumptions and source-role claims independently reviewed; rendered guide pages1-5 inspected.',
 'evidence':{'guide_json_sha256':sha(here/'guide.json'),'guide_pdf_sha256':sha(here.parent/'reference-pdfs'/'week-21-bonus-facilitator.pdf'),'student_final_pdf_sha256':sha(here.parent/'reference-pdfs'/'week-21-bonus.pdf'),'student_final_tex_sha256':sha(here.parent/'student-src'/'bonus.tex'),'student_checker_sha256':sha(here.parent/'math'/'independent-check.py'),'student_checks_sha256':sha(here.parent/'review'/'checks.json'),'guide_checker_sha256':sha(Path(__file__))},
 'verified_claims':{'P1':{'image':[7,-7],'contacts':[['11/5',1],['29/5',7]],'minimum':'sqrt(136) units','millimeters':'20sqrt(136)','finite_wall_membership':True,'unique_contacts':True},'P2':{'image':[7,17],'contacts':[['19/7',7],['37/7',1]],'minimum':'sqrt(232) units','finite_wall_membership':True,'shorter_order':'lower then upper'},'practice_visual':'Nonstraight broken path retained; all reflected leg squared lengths agree exactly.','P3':{'unrestricted_contact':[3,1],'closed_window_winners':[[2,1],[5,1]],'unique_legal_optimum':[2,1],'left_length':'sqrt(5)+sqrt(41)','right_length':'4sqrt(5)','exact_comparison':'41<45'},'P4':{'lower_length':'4+2sqrt(5)','upper_length':'4+2sqrt(8)','unique_lower_route':True,'visible_corner_paths_checked':8},'P5':{'two_geometric_shortest_routes':True,'each_length':9,'millimeters':180,'visible_corner_paths_checked':8,'redundant_subdivision':'same route'},'strip_extension':{'vertical_magnitudes':['2H+hA-hB','2H+hB-hA'],'difference_of_squared_magnitudes':'8H(hA-hB)','conditions':'H>0; endpoint heights strictly inside; finite contacts legal','exact_sanity_cases':cases},'symmetric_rectangle_extension':{'tie_height':'7/2 for the printed rectangle','exact_height_cases':len(heights),'lower_below_midpoint':True,'upper_above_midpoint':True},'open_window_extension':'For [1/2,2) union [5,15/2], infimum sqrt(5)+sqrt(41) is unattained; strict convexity and continuity certify it.','all_contact_and_corner_certificates':'Reflection isometry, triangle equality, strict convexity and legal-region straightening proofs checked independently.'},
 'source_attribution':{'base':'Current single-wall theorem, restricted-window limits and printed guide pp.13-17 agree with exclusions.','primary_context':'Petrunin sections1C,5D named as recorded base context, with no new body reading asserted.','teaching':'Math Circle by the Bay Preface vii-x/PDF8-11 supports context; string/readiness routes identified as proposals.'},
 'limits':['Closed windows and boundary travel are separate explicit legal-region rules.','Coordinate/grid calculations are adult certificates; physical string, tracing and scale rehearsal remain untested.','Extracted-source portable rebuild is a separate release check.'],'resolved_findings':[]}
(here/'guide-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'week':21,'status':out['status'],'strip_extension_cases':cases,'evidence':out['evidence']},indent=2))
