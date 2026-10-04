#!/usr/bin/env python3
"""Independent exhaustive checks; standard library only. Run from any directory."""
from itertools import combinations, product
from functools import lru_cache
from pathlib import Path
import hashlib, json

def balances(weights, target):
    # -1 beside target, +1 opposite target, 0 off.
    return [dict(left=[w for w,s in zip(weights,signs) if s==-1],right=[w for w,s in zip(weights,signs) if s==1])
            for signs in product((-1,0,1),repeat=len(weights)) if sum(w*s for w,s in zip(weights,signs))==target]

def robust(kit, end):
    return all(balances(tuple(w for w in kit if w!=lost), t) for lost in kit for t in range(1,end+1))

def partitions(weights,m):
    result=set()
    for assignment in product(range(m),repeat=len(weights)):
        groups=tuple(tuple(w for w,g in zip(weights,assignment) if g==i) for i in range(m))
        if all(groups) and len({sum(g) for g in groups})==1:
            result.add(tuple(sorted(groups)))
    return sorted(result)

@lru_cache(None)
def possible(candidates,k):
    if len(candidates)<=1: return True
    if not k: return False
    # Every integer threshold including outside the candidate range.
    return any(all(possible(tuple(x for x in candidates if (x>q)-(x<q)==out), k-1)
                   for out in (-1,0,1)) for q in range(min(candidates)-1,max(candidates)+2))

p1={str(lost):{str(t):balances(tuple(w for w in (1,2,3) if w!=lost),t) for t in (1,2,3)} for lost in (1,2,3)}
pairs3=[p for p in combinations(range(1,9),2) if all(balances(p,t) for t in range(1,4))]
pairs4=[p for p in combinations(range(1,9),2) if all(balances(p,t) for t in range(1,5))]
robust3=[p for p in combinations(range(1,9),3) if robust(p,3)]
robust4=[p for p in combinations(range(1,9),3) if robust(p,4)]
assert pairs3==[(1,2),(1,3),(2,3)] and pairs4==[(1,3)]
assert robust3==[(1,2,3)] and robust4==[]
search={str(n):possible(tuple(range(1,n+1)),2) for n in range(1,10)}
assert search['7'] and not search['8']
# Explicit legal ordered plan, including singleton inference.
paths={}
for x in range(1,8):
    q=4; out=(x>q)-(x<q); path=[(q,out)]
    remaining=[v for v in range(1,8) if (v>q)-(v<q)==out]
    if len(remaining)>1:
        q=2 if x<4 else 6; out=(x>q)-(x<q);path.append((q,out));remaining=[v for v in remaining if (v>q)-(v<q)==out]
    assert remaining==[x] and len(path)<=2
    paths[str(x)]=path
cases=[((1,2,3,4),2),((1,2,3,4,5,6),3),((1,2,5),2),((1,2,3,4,5,6,7,8),4)]
p6=[{'kit':w,'teams':m,'partitions':partitions(w,m)} for w,m in cases]
assert [len(c['partitions']) for c in p6]==[1,1,0,1]
assert p6[1]['partitions']==[((1,6),(2,5),(3,4))]
result={'week':30,'stage':'independent math critic','status':'pass','source':'final/bonus.pdf','problems_checked':[1,2,3,4,5,6,7],
'problem1_all_balances':p1,'pairs_covering_1_to_3_with_weights_1_to_8':pairs3,'pairs_covering_1_to_4_with_weights_1_to_8':pairs4,
'robust_kits_1_to_8_for_1_to_3':robust3,'robust_kits_1_to_8_for_1_to_4':robust4,'two_comparison_feasibility':search,'explicit_seven_candidate_plan':paths,
'problem6_partitions':p6,'problem7_all_partitions':p6[1]['partitions'],
'unbounded_proof':'Two positive distinct weights a<b have positive attainable targets among a,b,b-a,a+b. To cover 1..4 all four values must be distinct and exactly 1..4, so a+b=4 and (a,b)=(1,3). Every remaining pair of a robust triple would have to equal this one pair, impossible. To cover 1..3, b>3 leaves at most a and b-a in that range, so b<=3; exhaustive pairs then give (1,2),(1,3),(2,3). A zero weight cannot improve coverage.',
'comparison_bound':'Equality retains at most one candidate; each strict branch can distinguish at most M(k-1). M(0)=1; M(k)=2*M(k-1)+1, so M(2)=7.',
'non_task_example':{'candidates':[8,9,10],'threshold':9,'heavier_survivors':[10],'lighter_survivors':[8],'equal_survivors':[9]},
'diagram_audit':'Inspected all four rendered PDF pages: cards, two-pan left/right labels, nine loss-target rows, three kit slots, candidate example and 2/3/2/4 team trays match tasks. No physical fit/rehearsal claim.',
'issues':[]}
root=Path(__file__).resolve().parent
finalsrc=Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-30-bonus.pdf'
if pdf.exists():result['pdf_sha256']=hashlib.sha256(pdf.read_bytes()).hexdigest()
# Binding to the actual final source inspected in final-audit.md. Future edits need fresh review.
result['stage']='independent final mathematical audit'
source_text=finalsrc.read_text()
result['source_sha256']=hashlib.sha256(finalsrc.read_bytes()).hexdigest()
assert result['source_sha256']=='3a3e02da716a1d59b9fbe22314c05e7a9ebfe9d84b40dde5334ab53647b84598', 'Final source changed: re-audit actual tasks/diagrams.'
result['final_source_bound']=True
try:
    import pymupdf
except ImportError:
    result['pdf_text_verification']='PyMuPDF unavailable; file hash recorded, source and mathematics checked.'
else:
    import re
    with pymupdf.open(pdf) as document:
        result['pages']=len(document)
        printed='\n'.join(page.get_text() for page in document)
        numbers=list(map(int,re.findall(r'Problem (\d+):',printed)))
        assert numbers==result['problems_checked']
        result['actual_pdf_problem_numbers']=numbers
        result['pdf_text_verification']='All final pages extracted; actual numbered task coverage matches.'
result['diagram_audit']='All actual final PDF pages visually inspected; see final-audit.md for final wording, numbering, instances, examples and geometry. Physical procedures remain untested.'
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
