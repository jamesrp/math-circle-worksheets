#!/usr/bin/env python3
"""Exact independent computations of every Week 20 task/example."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import hashlib

def solve(A,b):
    M=[[F(x) for x in row]+[F(rhs)] for row,rhs in zip(A,b)]
    n=len(M)
    for i in range(n):
        j=next(j for j in range(i,n) if M[j][i]);M[i],M[j]=M[j],M[i]
        pivot=M[i][i];M[i]=[x/pivot for x in M[i]]
        for j in range(n):
            if j!=i:
                q=M[j][i];M[j]=[a-q*b for a,b in zip(M[j],M[i])]
    return tuple(row[-1] for row in M)

expected=solve([[2,-1],[-1,2]],[0,6])
assert expected==(2,4)
hit6=solve([[2,-1],[-1,2]],[0,1]);assert hit6==(F(1,3),F(2,3))
assert F(0+3+6,3)==3
def update(values,edges,self_value=False):
    new=[]
    for v in range(len(values)):
        neighbors=[j if i==v else i for i,j in edges if v in (i,j)]
        if self_value: neighbors.append(v)
        new.append(sum(F(values[j]) for j in neighbors)/len(neighbors))
    return tuple(new)
cycle=[(0,1),(1,2),(2,3),(3,0)]
path3=[(0,1),(1,2)]
assert update((0,3,6),path3)==(3,3,3)  # printed non-task tick
states=[tuple(map(F,(0,6,0,6)))]
for t in range(4): states.append(update(states[-1],cycle))
assert states[1]==(6,0,6,0) and states[2]==states[0] and states[1]!=states[0]
other=(F(1),F(5),F(1),F(5));assert update(update(other,cycle),cycle)==other and update(other,cycle)!=other
twoedge=[(0,1)]
assert update((0,6),twoedge)==(6,0)
assert update((6,0),twoedge)==(0,6)
assert update((0,6),twoedge,True)==(3,3) and update((3,3),twoedge,True)==(3,3)
own=[tuple(map(F,(0,6,0,6)))]
for t in range(1,31):
    own.append(update(own[-1],cycle,True))
    a=F(3)-F(3)*F(-1,3)**t;b=F(3)+F(3)*F(-1,3)**t
    assert own[t]==(a,b,a,b) and a!=3 and b!=3
assert own[1]==(4,2,4,2) and own[2]==(F(8,3),F(10,3),F(8,3),F(10,3)) and own[3]==(F(28,9),F(26,9),F(28,9),F(26,9))
def energy(values): return sum((b-a)**2 for a,b in zip(values,values[1:]))
assert energy((0,1,3))==5  # actual scored worked example
scores5={x:energy((0,x,6)) for x in range(7)}
assert min(scores5.values())==18 and [x for x,e in scores5.items() if e==18]==[3]
scores6={(x,y):energy((0,x,y,6)) for x,y in product(range(7),repeat=2)}
assert min(scores6.values())==12 and [p for p,e in scores6.items() if e==12]==[(2,4)]
for x,y in product(range(7),repeat=2):
    assert energy((0,x,6))==18+2*(x-3)**2
    assert energy((0,x,y,6))==12+(x-2)**2+((y-4)-(x-2))**2+(y-4)**2

def frac(v): return [str(x) for x in v]
out={'week':20,'verified_tasks':[1,2,3,4,5,6],'issues':[],'P1_expectations_A_B_C':[str(x) for x in expected]+['3'],'P1_hit_6_probabilities_A_B':frac(hit6),'P1_stopping_bound':'Probability of staying in circles for n moves is (1/2)^n on the path; C stops after one move.','P2_ticks_0_to_4':[frac(v) for v in states],'P2_other_least_period_two_state':frac(other),'P3_neighbor_only':'0,6 -> 6,0 -> 0,6 indefinitely','P3_self_included':'0,6 -> 3,3 -> 3,3','P4_ticks_0_to_3':[frac(v) for v in own[:4]],'P4_exact_formula':'a_t=3-3*(-1/3)^t, b_t=3+3*(-1/3)^t; (a_t,b_t,a_t,b_t)','P4_limit':3,'P4_finite_exact_hit':False,'P5_all_integer_scores':scores5,'P5_minimum':{'x':3,'score':18},'P6_integer_assignments_checked':49,'P6_minimum':{'x':2,'y':4,'score':12},'P6_energy_identity':'E=12+(x-2)^2+[(y-4)-(x-2)]^2+(y-4)^2','non_task_examples_checked':{'tick_0_3_6':[3,3,3],'roughness_0_1_3':5}}
finalsrc=Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
if finalsrc.exists():
    tex=finalsrc.read_text()
    assert 'Use the walks to estimate the average score' in tex and 'first returns after two ticks' in tex
    draft=(Path(__file__).parent/'fixtures'/'reviewed-draft.tex').read_text()
    draft=draft.replace('What average score would you expect after many walks from each start?','Use the walks to estimate the average score after many walks from each start.').replace('also returns after exactly two ticks.','first returns after two ticks.')
    assert draft==tex
    pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-20-bonus.pdf'
    out['final_audit']={'P1_empirical_estimate_and_exact_expectation_distinct':True,'P2_first_return_period_explicit':True,'all_math_data_and_diagrams_unchanged':True,'issues':[],'source_sha256':hashlib.sha256(finalsrc.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
