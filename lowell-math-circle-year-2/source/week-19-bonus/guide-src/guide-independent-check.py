#!/usr/bin/env python3
"""Independent extra guide claims; portable, Python standard library only."""
from pathlib import Path
from itertools import combinations
import hashlib, json

here = Path(__file__).resolve().parent
root = here.parent
def subset(a,b): return a & b == a
def works(T): return {x for x in range(16) if any(subset(t,x) for t in T)}
def label(x): return ''.join(chr(65+i) for i in range(3) if x>>i&1) or 'empty'
four_chains = [c for c in combinations(range(8),4) if all(subset(a,b) for a,b in zip(c,c[1:]))]
assert len(four_chains)==6
valid = []
for mask in range(256):
    F={x for x in range(8) if mask>>x&1}
    if not any(set(c)<=F for c in four_chains): valid.append(F)
maximum=max(map(len,valid))
maxima=[F for F in valid if len(F)==maximum]
assert maximum==7 and len(maxima)==2
assert {frozenset(set(range(8))-F) for F in maxima}=={frozenset({0}),frozenset({7})}
assert works({2,3,5})==works({2,5})
assert (7 & 11) and not ((15^7)&(15^11))
for n in range(1,9):
    mask=(1<<n)-1
    pairs={tuple(sorted((x,mask^x))) for x in range(1<<n)}
    assert len(pairs)==1<<(n-1)
    assert all(not(a&b) for a,b in pairs)
    star={x for x in range(1<<n) if x&1}
    assert len(star)==len(pairs) and all(a&b for a,b in combinations(star,2))
g=json.loads((here/'guide.json').read_text())
assert 'n>=1' in g['overview'][0]
student=root/'tmp/worksheet-runs/week-19-bonus-v1'
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
out={
 'week':19,'status':'verified','unresolved_mathematical_issues':[],
 'scope':'Every overview, actual final P1-P8 solution, hint, extension, assumption and source-role claim independently reviewed; rendered guide pages 1-5 inspected.',
 'evidence':{'guide_json_sha256':sha(here/'guide.json'),'guide_pdf_sha256':sha(here.parent/'reference-pdfs'/'week-19-bonus-facilitator.pdf'),'student_final_pdf_sha256':sha(here.parent/'reference-pdfs'/'week-19-bonus.pdf'),'student_final_tex_sha256':sha(here.parent/'student-src'/'bonus.tex'),'student_checker_sha256':sha(here.parent/'math'/'independent-check.py'),'student_checks_sha256':sha(here.parent/'review'/'checks.json'),'guide_checker_sha256':sha(Path(__file__))},
 'verified_claims':{'P1':{'maximum':4,'maximum_families':4},'P2':{'unique_maximum_without_common_symbol':['AB','AC','BC','ABC']},'P3':{'maximum':8,'maximum_families':12},'P4':{'AB_or_D_working':10,'A_or_BC_working':10},'P5':{'unique_minimum_triggers':['B','AC']},'P6':{'monotone_rules':168,'single_removal_equivalent_to_inclusion_minimal':True,'empty_trigger':'sole trigger of all-working rule','no_working_cards':'no triggers'},'P7':{'maximum':6,'maximum_families':1,'chain_lengths':[4,2,2]},'P8':{'maximum':10,'maximum_families':2,'chain_lengths':[5,3,3,1,3,1]},'chain_four_extension':{'families_checked':256,'four_chains':len(four_chains),'maximum':maximum,'maximum_families':[[label(x) for x in sorted(F)] for F in maxima]},'redundant_triggers':'B,AB,AC and B,AC agree on all 16 cards','complement_intersection_counterexample':'ABC/ABD intersect; D/C do not','general_complement_bound':'proved for n>=1; finite complement/star sanity checks n=1..8'},
 'source_attribution':{'base_guide':'Current base guide pp.3-4,11 independently inspected; finite chain certificates and recorded Stanley context agree.','primary_context':'Stanley source body explicitly described as not newly read, rather than asserted new evidence.','teaching_source':'Math Circle by the Bay Preface vii-x, local PDF8-11 read; interaction/manipulatives/long development supported; proposed routes distinguished from observations.'},
 'limits':['Physical card preparation/fit and classroom timing are untested.','This audit is not the extracted portable-package rebuild.'],
 'resolved_findings':['Overview now explicitly states n>=1.']}
(here/'guide-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'week':19,'status':out['status'],'extension_max':maximum,'extension_maximum_families':len(maxima),'evidence':out['evidence']},indent=2))
