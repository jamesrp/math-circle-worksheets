#!/usr/bin/env python3
"""Independent network enumeration and tagged-card checks; standard library only."""
from itertools import combinations,permutations,product
from pathlib import Path
import json,re,hashlib
def run(values,bars):
    v=list(values)
    for a,b in bars:
        if v[a]>v[b]:v[a],v[b]=v[b],v[a]
    return tuple(v)
def tagged(values,bars):
    v=list(values)
    for a,b in bars:
        if v[a][0]>v[b][0]:v[a],v[b]=v[b],v[a]
    return tuple(v)
def stable(before,after):
    return all([tag for x,tag in before if x==value]==[tag for x,tag in after if x==value] for value in {x for x,t in before})
bars4=list(combinations(range(4),2));inputs=list(permutations(range(1,5)))
selector=((0,1),(0,2),(0,3))
selector_counts={}
merge_counts={};mergers=[]
legal=[v for v in inputs if v[0]<v[1] and v[2]<v[3]]
assert legal==[(1,2,3,4),(1,3,2,4),(1,4,2,3),(2,3,1,4),(2,4,1,3),(3,4,1,2)]
for n in range(4):
    count_s=count_m=0
    for net in product(bars4,repeat=n):
        if all(run(v,net)[0]==1 for v in inputs):count_s+=1
        if all(run(v,net)==(1,2,3,4) for v in legal):
            count_m+=1
            if n==3:mergers.append(net)
    selector_counts[str(n)]=count_s;merge_counts[str(n)]=count_m
assert selector_counts['0']==selector_counts['1']==selector_counts['2']==0 and selector_counts['3']>0
assert merge_counts['0']==merge_counts['1']==merge_counts['2']==0 and merge_counts['3']>0
assert all(run(v,selector)[0]==1 for v in inputs)
partial=((0,1),(2,3),(0,3),(1,2))
partial_outputs=[]
for v in inputs:
    out=run(v,partial);assert set(out[:2])=={1,2} and set(out[2:])=={3,4}
    partial_outputs.append({'input':v,'output':out})
assert run((3,4,1,2),partial)==(2,1,4,3)
repeated=list(product(range(1,5),repeat=4))
for v in repeated:
    out=run(v,partial)
    assert sorted(out[:2])==sorted(v)[:2] and sorted(out[2:])==sorted(v)[2:]
merger=((0,2),(1,3),(1,2))
legal_repeated=[v for v in repeated if v[0]<=v[1] and v[2]<=v[3]]
for net in mergers:
    assert all(run(v,net)==tuple(sorted(v)) for v in legal_repeated)
    assert any(run(v,net)!=tuple(sorted(v)) for v in inputs)
p4_bad=(2,1,4,3);assert run(p4_bad,merger)==p4_bad
merger_counterexamples=[{'bars':[[a+1,b+1] for a,b in net],'input':next(v for v in inputs if run(v,net)!=tuple(sorted(v)))} for net in mergers]
X=((0,2),(0,1),(1,2));Y=((0,1),(1,2),(0,1))
# Confirm actual dotted-lane diagrams have precisely these left-to-right bars.
tex=(Path(__file__).parent/'fixtures'/'reviewed-draft.tex').read_text()
printed=[]
for lanes,body in re.findall(r'\\machine(?:\[[^]]*\])?\{(\d+)\}\{([^}]+)\}',tex):
    printed.append(tuple((int(a)-1,int(b)-1) for x,a,b in (entry.split('/') for entry in body.split(','))))
assert printed==[partial,X,Y]
tag_inputs=[((2,'A'),(2,'B'),(1,'C')),((2,'A'),(1,'C'),(2,'B')),((2,'B'),(2,'A'),(1,'C')),((2,'B'),(1,'C'),(2,'A')),((1,'C'),(2,'A'),(2,'B')),((1,'C'),(2,'B'),(2,'A'))]
tag_outputs=[]
for before in tag_inputs:
    x,y=tagged(before,X),tagged(before,Y)
    assert [a for a,t in x]==[1,2,2] and [a for a,t in y]==[1,2,2] and stable(before,y)
    tag_outputs.append({'input':[f'{v}{t}' for v,t in before],'X':[f'{v}{t}' for v,t in x],'Y':[f'{v}{t}' for v,t in y],'X_preserves_equal_order':stable(before,x),'Y_preserves_equal_order':stable(before,y)})
assert sum(not row['X_preserves_equal_order'] for row in tag_outputs)==2
for values in product(range(1,4),repeat=3):
    before=tuple(zip(values,'ABC'))
    assert tuple(v for v,t in tagged(before,X))==tuple(sorted(values))
    assert tuple(v for v,t in tagged(before,Y))==tuple(sorted(values)) and stable(before,tagged(before,Y))
before=((3,'A'),(1,'B'),(3,'C'));after=tagged(before,((0,1),))
assert after==((1,'B'),(3,'A'),(3,'C')) and stable(before,after)
atomic=0
for values in product(range(1,4),repeat=4):
    before=tuple(zip(values,'ABCD'))
    for edge in ((0,1),(1,2),(2,3)):
        assert stable(before,tagged(before,(edge,)));atomic+=1
out={'week':23,'verified_tasks':[1,2,3,4,5,6],'issues':[],'P1_minimum_bars':3,'P1_selector_counts_by_length':selector_counts,'P1_witness':[[a+1,b+1] for a,b in selector],'P2_all_24_distinct_outputs':partial_outputs,'P2_unsorted_witness':{'input':[3,4,1,2],'output':[2,1,4,3]},'P2_repeated_value_inputs_checked':256,'P3_minimum_bars':3,'P3_merger_counts_by_length':merge_counts,'P3_witness':[[a+1,b+1] for a,b in merger],'P3_repeated_value_legal_inputs_checked_per_merger':len(legal_repeated),'P4_witness_for_standard_merger':{'input':p4_bad,'output':run(p4_bad,merger)},'P4_witness_for_every_three_bar_merger':merger_counterexamples,'P5_all_tagged_traces':tag_outputs,'P5_repeated_value_three_card_assignments_checked':27,'P6_adjacent_atomic_actions_checked':atomic,'P6_general_proof':'An adjacent swap reverses only its two swapped cards; equal values never swap. Induction preserves every equal pair for any number of bars.','actual_diagram_bar_orders':'parsed and verified','non_task_tag_example':'3A,1B,3C -> 1B,3A,3C; A remains before C'}
finalsrc=Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
if finalsrc.exists():
    finaltex=finalsrc.read_text()
    assert tex.replace('A bar between neighboring lanes swaps no card over a third card. Can a machine made only from such bars ever reverse two equal cards?','Can a machine whose bars join only neighboring lanes ever reverse two equal cards?')==finaltex
    finalbars=[]
    for lanes,body in re.findall(r'\\machine(?:\[[^]]*\])?\{(\d+)\}\{([^}]+)\}',finaltex):
        finalbars.append(tuple((int(a)-1,int(b)-1) for x,a,b in (entry.split('/') for entry in body.split(','))))
    assert finalbars==[partial,X,Y]
    pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-23-bonus.pdf'
    out['final_audit']={'P6_investigation_question_preserves_stability_claim_without_printed_hint':True,'actual_final_diagram_bar_orders':'verified','other_tasks_and_example_unchanged':True,'issues':[],'source_sha256':hashlib.sha256(finalsrc.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
