#!/usr/bin/env python3
"""Independent exhaustive set-family checks; no writer notes or third-party modules."""
from itertools import combinations
from pathlib import Path
import json
import hashlib
def name(x,n=4): return ''.join(chr(65+i) for i in range(n) if x>>i&1) or 'empty'
def subset(a,b): return a&b==a
def family(mask,n): return [x for x in range(1<<n) if mask>>x&1]
def intersecting(F): return 0 not in F and all(a&b for a,b in combinations(F,2))
def no_triple(F): return not any(a!=b and b!=c and a!=c and subset(a,b) and subset(b,c) for a in F for b in F for c in F)
def triggers(T,n=4): return {x for x in range(1<<n) if any(subset(t,x) for t in T)}
def minimal(F): return {x for x in F if not any(y!=x and subset(y,x) for y in F)}
stats={}
for n in (3,4):
    maximal_i=[];maximal_t=[];mi=mt=-1
    for mask in range(1<<(1<<n)):
        F=family(mask,n)
        if intersecting(F):
            if len(F)>mi: mi=len(F);maximal_i=[]
            if len(F)==mi: maximal_i.append(F)
        if no_triple(F):
            if len(F)>mt: mt=len(F);maximal_t=[]
            if len(F)==mt: maximal_t.append(F)
    stats[str(n)]={'intersection_max':mi,'intersection_max_families':len(maximal_i),'no_nested_triple_max':mt,'no_nested_triple_max_families':len(maximal_t),'intersection_examples':[[name(x,n) for x in F] for F in maximal_i]}
assert stats['3']['intersection_max']==4 and stats['4']['intersection_max']==8
assert stats['3']['no_nested_triple_max']==6 and stats['4']['no_nested_triple_max']==10
F={3,5,6,7}; assert intersecting(F) and not (3&5&6&7)
p4a=triggers({3,8});p4b=triggers({1,6})
assert len(p4a)==len(p4b)==10
p5={2,3,6,10,7,11,14,15,5,13}
assert minimal(p5)=={2,5} and triggers({2,5})==p5
all_trigger_solutions=[]
for mask in range(1<<16):
    T=family(mask,4)
    if triggers(T)==p5: all_trigger_solutions.append(T)
best=min(map(len,all_trigger_solutions))
assert best==2 and [T for T in all_trigger_solutions if len(T)==best]==[[2,5]]
monotone=0
for mask in range(1<<16):
    F=set(family(mask,4))
    if all(not subset(x,y) or y in F for x in F for y in range(16)):
        monotone+=1
        assert triggers(minimal(F))==F
        single_remove_minimal={x for x in F if all((x ^ (1<<i)) not in F for i in range(4) if x>>i&1)}
        assert single_remove_minimal==minimal(F)
assert monotone==168
assert triggers(set())==set() and triggers({0})==set(range(16))
smallest_by_size={x for x in p5 if x.bit_count()==min(y.bit_count() for y in p5)}
assert smallest_by_size=={2} and 5 not in triggers(smallest_by_size)
chains3=[[0,1,3,7],[2,6],[4,5]]
chains4=[[0,1,3,7,15],[8,9,11],[4,5,13],[12],[2,6,14],[10]]
for n,chains in [(3,chains3),(4,chains4)]:
    assert sorted(x for chain in chains for x in chain)==list(range(1<<n))
    assert all(subset(a,b) and a!=b for chain in chains for a,b in zip(chain,chain[1:]))
    assert sum(min(2,len(c)) for c in chains)==stats[str(n)]['no_nested_triple_max']
assert subset(5,13)  # actual AC -> ACD worked example
out={'week':19,'verified_tasks':[1,2,3,4,5,7,8],'task6':'verified for inclusion-minimal cards; smallest by number of symbols is false','family_enumerations':stats,'P2_witness':['AB','AC','BC','ABC'],'P4_AB_or_D':[name(x) for x in sorted(p4a)],'P4_A_or_BC':[name(x) for x in sorted(p4b)],'P5_minimum_triggers':['B','AC'],'P5_minimum_trigger_count':best,'four_symbol_monotone_rules_checked':monotone,'chain_partition_certificates':{'3':[[name(x,3) for x in c] for c in chains3],'4':[[name(x) for x in c] for c in chains4]},'issues':[{'problem':6,'page':3,'issue':'smallest working cards can mean globally least cardinality, which omits larger inclusion-minimal triggers','counterexample':'P5 rule: B is size 1, AC is size 2, and B alone fails to generate AC/ACD','smallest_fix':'find every working card with no smaller working card inside it, and use those cards as triggers'}]}
finalsrc=Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
if finalsrc.exists():
    tex=finalsrc.read_text()
    assert 'every working card that stops working whenever any symbol is removed' in tex
    assert 'adding symbols to a working card never makes it fail' in tex
    assert minimal(set(range(16)))=={0} and triggers({0})==set(range(16))
    assert minimal(set())==set() and triggers(set())==set()
    pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-19-bonus.pdf'
    out['final_audit']={'P6_single_symbol_removal_definition':'verified equivalent to inclusion-minimal for all 168 monotone rules','empty_working_card_case':'qualifies vacuously; is the sole trigger of the all-working rule','no_working_card_case':'empty trigger collection recreates the all-failing rule','issues':[],'source_sha256':hashlib.sha256(finalsrc.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
