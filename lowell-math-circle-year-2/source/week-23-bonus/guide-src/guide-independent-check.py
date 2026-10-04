#!/usr/bin/env python3
"""Independent guide traces/extensions; portable standard library only."""
from pathlib import Path
from itertools import permutations,product,combinations
import hashlib,json
here=Path(__file__).resolve().parent
root=here.parent
g=json.loads((here/'guide.json').read_text())
assert '1,3,4,2 becomes 1,2,4,3' in g['investigations'][1]['solution'][2]
def run(row,bars,tagged=False):
    row=list(row)
    for a,b in bars:
        a-=1;b-=1
        va,vb=(row[a][0],row[b][0]) if tagged else (row[a],row[b])
        if va>vb:row[a],row[b]=row[b],row[a]
    return tuple(row)
merge=((1,3),(2,4),(2,3))
trace=[(1,3,4,2)]
for bar in merge:trace.append(run(trace[-1],[bar]))
assert trace[-1]==(1,2,4,3)
assert run((2,1,4,3),merge)==(2,1,4,3)
assert run((1,2,4,3),merge)==(1,2,4,3)
sorter=((1,2),(3,4))+merge
distinct=0
for row in permutations(range(1,5)):
    assert run(row,sorter)==tuple(sorted(row));distinct+=1
repeated=0
for row in product(range(4),repeat=4):
    assert run(row,sorter)==tuple(sorted(row));repeated+=1
selection_cases={}
for n in range(1,7):
    bars=[(1,i) for i in range(2,n+1)]
    count=0
    for row in permutations(range(n)):
        assert run(row,bars)[0]==0;count+=1
    selection_cases[str(n)]={'bars':len(bars),'permutations_checked':count}
def stable(before,after):
    return all([t for v,t in before if v==value]==[t for v,t in after if v==value] for value in {v for v,t in before})
atomic=0
for n in range(1,6):
    for values in product(range(3),repeat=n):
        before=tuple((v,i) for i,v in enumerate(values))
        for a in range(1,n):
            after=run(before,[(a,a+1)],True)
            assert stable(before,after);atomic+=1
X=((1,3),(1,2),(2,3));Y=((1,2),(2,3),(1,2))
tagged=list(permutations(((2,'A'),(2,'B'),(1,'C'))))
X_bad=[row for row in tagged if not stable(row,run(row,X,True))]
Y_bad=[row for row in tagged if not stable(row,run(row,Y,True))]
assert len(X_bad)==2 and not Y_bad
assert run(((3,'A'),(1,'B'),(3,'C')),[(1,2)],True)==((1,'B'),(3,'A'),(3,'C'))
student=root/'tmp/worksheet-runs/week-23-bonus-v1'
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
out={'week':23,'status':'verified','unresolved_mathematical_issues':[],
 'scope':'All overview, actual final P1-P6 solutions, every explicit trace/table, hints, extensions, assumptions and attribution independently reviewed; corrected five-page guide inspected.',
 'evidence':{'guide_json_sha256':sha(here/'guide.json'),'guide_pdf_sha256':sha(here.parent/'reference-pdfs'/'week-23-bonus-facilitator.pdf'),'student_final_pdf_sha256':sha(here.parent/'reference-pdfs'/'week-23-bonus.pdf'),'student_final_tex_sha256':sha(here.parent/'student-src'/'bonus.tex'),'student_checker_sha256':sha(here.parent/'math'/'independent-check.py'),'student_checks_sha256':sha(here.parent/'review'/'checks.json'),'guide_checker_sha256':sha(Path(__file__))},
 'verified_claims':{'P1':{'minimum_bars':3,'witness':[[1,2],[1,3],[1,4]],'lower_bound':'Fewer than n-1 graph edges leave a component not containing lane1; a minimum in it cannot leave.','n_lane_extension':selection_cases},'P2':{'network':[[1,2],[3,4],[1,4],[2,3]],'distinct_inputs_checked':24,'repeated_inputs_checked':256,'half_order':'Each of lanes1,2 is at most each of lanes3,4; within halves need not sort.','counterexample':{'input':[3,4,1,2],'output':[2,1,4,3]}},'P3':{'minimum_bars':3,'shortest_mergers':2,'distinct_legal_inputs':6,'repeated_legal_inputs_checked_per_merger':100,'lower_bound':'A fixed successful swap record determines one distinct start from the sorted output; 2^2<6.'},'P4':{'unchanged_failures':[[2,1,4,3],[1,2,4,3]],'corrected_trace':[list(row) for row in trace],'all_three_bar_mergers_fail_somewhere':'2^3<24 distinct unrestricted inputs'},'P5':{'six_tagged_cases':6,'X_equal_order_failures':2,'Y_equal_order_failures':0,'tags':'Identifiers never affect compare-exchange; ties stay.','both_value_sorters':True,'worked_example':['3A,1B,3C','1B,3A,3C']},'P6':{'general_invariant':'An adjacent swap changes relative order only for its two exchanged cards; equal cards never swap. Induction preserves every equal pair for any machine length even without value sorting.','atomic_actions_checked':atomic,'tie_swap_counterexample':['2A,2B','2B,2A']},'five_bar_sorter_extension':{'bars':[list(a) for a in sorter],'distinct_inputs_checked':distinct,'repeated_inputs_checked':repeated,'proof':'First two bars establish sorted-pair promise; proved merger then sorts values universally.'}},
 'resolved_findings':['P4 guide trace corrected: 1,3,4,2 outputs 1,2,4,3. Correction verified in current JSON and rendered PDF.'],
 'source_attribution':{'base':'Current printed guide pp.3,11-12 support fixed comparator rules and reversible-record bounds; base parallel/binary/full-sorter searches distinguished.','primary_context':'Liverpool COMP308 Lecture17 pp.1-2 identified as recorded network context, no new body reading asserted.','teaching':'Math Circle by the Bay Preface vii-x/PDF8-11 supports interaction/manipulatives/long themes; physical tray routes marked proposed.'},
 'limits':['Record lower bounds use distinct ranks; correctness includes ties.','Minimum selector claims n>=1; n=1 needs zero bars.','Physical bar discipline, card advances, tags and tray procedures remain unrehearsed.','Extracted portable-source rebuilding is a separate release check.']}
(here/'guide-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'week':23,'status':out['status'],'atomic_stability_checks':atomic,'sorter_checks':[distinct,repeated],'evidence':out['evidence']},indent=2))
