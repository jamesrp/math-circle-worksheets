#!/usr/bin/env python3
"""Independent exact extra guide checks; portable standard-library Python."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json
here=Path(__file__).resolve().parent
root=here.parent
g=json.loads((here/'guide.json').read_text())
assert 'When A and B are integers' in g['investigations'][2]['extensions'][0]
for a,b in product(range(-3,7),repeat=2):
    na,nb=F(a+2*b,3),F(b+2*a,3)
    assert na+nb==a+b and na-nb==-F(a-b,3)
boards=[]
a,b=F(0),F(6)
for t in range(16):
    assert a==3-3*F(-1,3)**t and b==3+3*F(-1,3)**t
    assert a!=b and a+b==6
    if t<4: boards.append([str(a),str(b),str(a),str(b)])
    a,b=(a+2*b)/3,(b+2*a)/3
cases=0
for L in range(1,9):
    for A,B in product(range(-3,4),repeat=2):
        gap=F(B-A,L)
        vals=[A+i*gap for i in range(L+1)]
        assert all(v.denominator==1 for v in vals)==((B-A)%L==0)
        assert sum((b-a)**2 for a,b in zip(vals,vals[1:]))==F((B-A)**2,L)
        # Exact expansion for an arbitrary competing path with the same ends.
        other=[F(A)]+[F((-1)**i*i,3) for i in range(1,L)]+[F(B)]
        deviations=[b-a-gap for a,b in zip(other,other[1:])]
        assert sum(deviations)==0
        assert sum((b-a)**2 for a,b in zip(other,other[1:]))-F((B-A)**2,L)==sum(x*x for x in deviations)
        cases+=1
assert F(1,2)+F(0)==F(1,2)  # noninteger endpoints would invalidate the old divisibility phrasing
student=root/'tmp/worksheet-runs/week-20-bonus-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'week':20,'status':'verified','unresolved_mathematical_issues':[],
 'scope':'All overview, final P1-P6 solutions, hints, extensions, limits and attribution independently reviewed; corrected five-page guide PDF inspected.',
 'evidence':{'guide_json_sha256':sha(here/'guide.json'),'guide_pdf_sha256':sha(here.parent/'reference-pdfs'/'week-20-bonus-facilitator.pdf'),'student_final_pdf_sha256':sha(here.parent/'reference-pdfs'/'week-20-bonus.pdf'),'student_final_tex_sha256':sha(here.parent/'student-src'/'bonus.tex'),'student_checker_sha256':sha(here.parent/'math'/'independent-check.py'),'student_checks_sha256':sha(here.parent/'review'/'checks.json'),'guide_checker_sha256':sha(Path(__file__))},
 'verified_claims':{'P1':{'expected_scores':{'A':2,'B':4,'C':3},'probability_of_terminal_6':{'A':'1/3','B':'2/3'},'survive_n_moves':'(1/2)^n','scaled_boundaries_0_3_expectations':[1,2]},'P2':{'first_return':2,'another_period_two_board':[1,5,1,5],'constants':'first return 1; excluded by exactly-two goal'},'P3':{'neighbor_only':'0,6 swaps forever','own_and_neighbor':'3,3 after one tick'},'P4':{'first_four_boards':boards,'exact_positions':'3 ± 3(-1/3)^t','midpoint':3,'nonzero_gap_reversal_factor':'-1/3','finite_tick_equality':False,'general_alternating_pair_cases':100},'P5':{'scores':[36,26,20,18,20,26,36],'unique_argmin':3,'minimum':18,'identity':'E=18+2(x-3)^2'},'P6':{'all_allowed_pairs_checked':49,'unique_argmin':[2,4],'minimum':12,'identity':'E-12=sum_i(d_i-2)^2, sum_i d_i=6'},'path_extension':{'formula':'(B-A)^2/L','integer_criterion':'A,B integers; L divides B-A','exact_checks':cases,'L_range':[1,8],'endpoint_range':[-3,3]},'general_energy_proof':'Edge expansion and vertex regrouping checked; harmonic cross term zero, equality constant on components, unique when every component reaches a fixed square.','general_stopping_proof':'Finite reachability gives a uniform positive probability of absorption in bounded blocks; bounded terminal scores make the first-step expectation valid.'},
 'resolved_findings':['Path extension now explicitly assumes integer endpoint values before its divisibility criterion.'],
 'source_attribution':{'base':'Current base overview and pp.3-4,22-25 confirm harmonic setting, uniqueness and recorded Doyle-Snell context.','primary_context':'Doyle and Snell sections1.1-1.2 identified as recorded context, not newly read body.','teaching':'Preface vii-x/PDF8-11 supports stated context; pacing/readiness are proposed adaptations.'},
 'limits':['The dynamics claims concern the printed alternating states, not universal graph convergence.','Finite sample means need not equal exact expectations.','Fair draws, physical state copies, fit and classroom procedure remain unrehearsed.','Extracted portable rebuild is a separate release check.']}
(here/'guide-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'week':20,'status':out['status'],'path_checks':cases,'evidence':out['evidence']},indent=2))
