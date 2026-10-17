#!/usr/bin/env python3
"""Independent Week 87 finite checks; stdlib, no imports from the writer."""
from itertools import permutations, combinations, combinations_with_replacement
from collections import Counter
import json
from pathlib import Path

def ballot(profile,a,b):
    av=sum(row.index(a)<row.index(b) for row in profile)
    return av,len(profile)-av

def winner(profile,a,b):
    x,y=ballot(profile,a,b)
    assert x!=y
    return a if x>y else b

def agendas(profile):
    return {c:winner(profile,winner(profile,*[a for a in 'ABC' if a!=c]),c) for c in 'ABC'}

def votes(favs,x,y):
    d=[abs(p-x)-abs(p-y) for p in favs]
    return [sum(z<0 for z in d),sum(z>0 for z in d),sum(z==0 for z in d)]

def winners(favs,strict):
    return [x for x in range(11) if all((votes(favs,x,y)[0]>votes(favs,x,y)[1] if strict else votes(favs,x,y)[0]>=votes(favs,x,y)[1]) for y in range(11) if y!=x)]

cycle=('ABC','BCA','CAB')
assert [ballot(cycle,*p) for p in ['AB','BC','CA']]==[(2,1)]*3
assert agendas(cycle)==dict(zip('ABC','ABC'))
demo=('DFE','EFD','FED')
assert ballot(demo,'D','E')==(1,2)
assert ballot(demo,'E','F')==(1,2)
profiles=list(combinations([''.join(p) for p in permutations('ABC')],3))
classes=Counter(len(set(agendas(p).values())) for p in profiles)
assert classes=={1:18,3:2}
assert agendas(('ABC','ACB','BAC'))==dict.fromkeys('ABC','A')
assert agendas(('ACB','CBA','BAC'))==dict(zip('ABC','ABC'))
# Every labelled assignment too: 6^3=216 profiles, 3 choices of waiter.
labelled=0
from itertools import product
for p in product([''.join(q) for q in permutations('ABC')],repeat=3):
    cond=[a for a in 'ABC' if all(winner(p,a,b)==a for b in 'ABC' if a!=b)]
    outcomes=set(agendas(p).values())
    assert (len(outcomes)==1)==bool(cond)
    if cond:assert outcomes==set(cond)
    labelled+=1
line_examples={}
for fs,ans in [((0,2,4,7,10),4),((0,0,0,8,10),0),((1,4,4,4,9),4),((0,1,6,9,10),6)]:
    assert winners(fs,True)==[ans]
    line_examples[str(fs)]={'winner':ans,'tallies_against_each_other_tick':{str(q):votes(fs,ans,q) for q in range(11) if q!=ans}}
assert votes([2],0,5)==[1,0,0]
assert votes([3],1,5)==[0,0,1]
assert votes([0,1,5,8,10],2,8)==[2,2,1] # critic's proposed worked case
odd_count=0
for fs in combinations_with_replacement(range(11),5):
    m=fs[2]
    for q in range(11):
        if q!=m:assert votes(fs,m,q)[0]>=3
    odd_count+=1
assert odd_count==3003
assert winners([1,3,7,9],False)==list(range(3,8))
assert winners([1,3,7,9],True)==[]
even_count=0
for fs in combinations_with_replacement(range(11),4):
    assert winners(fs,False)==list(range(fs[1],fs[2]+1))
    even_count+=1
assert even_count==1001
# Six candidate orders: whichever letter is middle, one required voter ranks it last.
obstructions=[]
for order in permutations('ABC'):
    mid=order[1];v=next(i+1 for i,row in enumerate(cycle) if row[-1]==mid)
    obstructions.append({'left_to_right':''.join(order),'middle':mid,'voter_requiring_middle_last':v})
# Supplemental finite experiment only; real-line proof is in verification-notes.md.
distance_checks=0
for a,b,c in combinations(range(-4,5),3):
    for p in range(-8,9):
        assert abs(p-b)<max(abs(p-a),abs(p-c))
        distance_checks+=1
out={'status':'PASS','distinct_card_sets':20,'distinct_card_classes':dict(classes),'labelled_card_profiles':labelled,'shared_cycle_waiter_to_winner':agendas(cycle),'line_examples':line_examples,'odd_profiles':odd_count,'odd_challenger_comparisons':odd_count*10,'even_profiles':even_count,'even_example_weak_winners':[3,4,5,6,7],'even_example_strict_winners':[],'real_line_order_obstructions':obstructions,'supplemental_distance_checks':distance_checks}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('line_examples','real_line_order_obstructions')},indent=2))
