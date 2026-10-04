"""Coordinator fair-division calculations; authored student/guide checks not imported."""
import itertools,json
from fractions import Fraction as F
from pathlib import Path

def allocations(values):
    people=len(values);items=len(values[0]);found=[]
    for owners in itertools.product(range(people),repeat=items):
        scores=[[sum(values[observer][k] for k in range(items) if owners[k]==recipient) for recipient in range(people)] for observer in range(people)]
        ef=all(scores[p][p]>=scores[p][q] for p in range(people) for q in range(people))
        prop=all(people*scores[p][p]>=sum(values[p]) for p in range(people))
        found.append({'owners':owners,'observer_tray_values':scores,'EF':ef,'PROP':prop})
    assert all(not r['EF'] or r['PROP'] for r in found)
    if people==2:assert all(r['EF']==r['PROP'] for r in found)
    return found
p1=allocations([[3,3,3,1],[1,1,1,3]])
p2=allocations([[3,3,1,1],[1,1,3,3]])
p5=allocations([[1,1,1],[1,1,1]])
p6=allocations([[4,8,0],[0,4,8],[8,0,4]])
assert sum(r['EF'] for r in p1)==4
assert sum(r['EF'] for r in p2)==5
assert sum(r['EF'] for r in p5)==0
assert sum(r['EF'] for r in p6)==1 and sum(r['PROP'] for r in p6)==2
initial=next(r for r in p6 if r['owners']==(0,1,2));assert initial['PROP'] and not initial['EF']
def prefix(x,red,blue):return red*min(F(x),F(150))/150+blue*max(F(x)-150,F(0))/150
assert prefix(100,3,1)==2 and prefix(200,1,3)==2
assert prefix(100,1,3)==F(2,3) and 4-prefix(100,1,3)==F(10,3)
assert prefix(200,3,1)==F(10,3) and 4-prefix(200,3,1)==F(2,3)
assert prefix(150,3,1)==3 and 4-prefix(150,3,1)==1
out={'P1_successful_labelled_allocations':[r for r in p1 if r['EF']],
     'P2_all_five':[r for r in p2 if r['EF']],
     'P3_cuts_mm':[100,200],'P4_unequal_join_cut_scores':[1,3],
     'P5_whole_items_no_solution':True,'P5_replaced_R3_half_solution_values':['3/2','3/2'],
     'P6_initial':initial,'P6_unique_EF':[r for r in p6 if r['EF']],
     'P6_two_PROP':[r for r in p6 if r['PROP']],
     'P7_proof_review':'Own+others=total. For two, own>=other iff 2*own>=total. For n, every other<=own implies total<=n*own; initial P6 disproves converse for three.'}
p=Path(__file__).parent/'guide-review-assets/independent-guide-checks.json';p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if not isinstance(v,list)})
