#!/usr/bin/env python3
"""Independent polygon-motion, repair and ordered-layer enumeration; stdlib only."""
from pathlib import Path
from itertools import product
from collections import Counter
from math import sin,cos,pi,hypot
import hashlib,json

def motions(n):return [('turn',s,tuple((i+s)%n for i in range(n))) for s in range(n)]+[('flip',s,tuple((s-i)%n for i in range(n))) for s in range(n)]
def matches(s,perm):return all(s[i]==s[perm[i]] for i in range(len(s)))
def stabilizer(s):return {(kind,k) for kind,k,perm in motions(len(s)) if matches(s,perm)}
def census(n):
    out=[]
    for s in product('AB',repeat=n):
        st=stabilizer(s);r=sum(k=='turn' for k,_ in st);f=sum(k=='flip' for k,_ in st)
        assert n%r==0 and f in (0,r)
        out.append({'word':''.join(s),'turns_including_identity':r,'nonidentity_turns':r-1,'flips':f})
    return out

def repairs(s,perm):
    candidates=[]
    for t in product('AB',repeat=len(s)):
        if matches(t,perm):candidates.append((sum(a!=b for a,b in zip(s,t)),''.join(t)))
    least=min(d for d,_ in candidates)
    return {'minimum':least,'all_best':[t for d,t in candidates if d==least]}
def cycles(perm):
    todo=set(range(len(perm)));out=[]
    while todo:
        start=min(todo);cycle=[];i=start
        while i not in cycle:cycle.append(i);todo.remove(i);i=perm[i]
        out.append(cycle)
    return out

def cycle_cost(s,perm):return sum(len(c)-max(Counter(s[i] for i in c).values()) for c in cycles(perm))

c6,c8=census(6),census(8)
assert sorted({p['flips'] for p in c6})==[0,1,2,3,6]
assert sorted({p['flips'] for p in c8})==[0,1,2,4,8]
p1={k:s for k,s in [(1,'AABBBB'),(2,'ABBABB'),(3,'ABABAB')]}
for k,s in p1.items():assert sum(kind=='flip' for kind,_ in stabilizer(s))==k
start='AAABBABB'
perms={'half_turn':tuple((i+4)%8 for i in range(8)),'vertical_flip':tuple((-i)%8 for i in range(8)),'one_spot_turn':tuple((i+1)%8 for i in range(8)),'two_spot_turn':tuple((i+2)%8 for i in range(8))}
p34={name:repairs(start,p) for name,p in perms.items()}
assert [p34[n]['minimum'] for n in perms]==[2,3,4,4]
assert [len(p34[n]['all_best']) for n in perms]==[4,8,2,4]
for name,p in perms.items():
    assert p34[name]['minimum']==cycle_cost(start,p)
    p34[name]['cycles']=cycles(p)
    p34[name]['starting_cycle_kinds']=[''.join(start[i] for i in c) for c in cycles(p)]
    # Independently check formula against exhaustive best repair for every starting word.
    fixed=[t for t in product('AB',repeat=8) if matches(t,p)]
    for s in product('AB',repeat=8):assert cycle_cost(s,p)==min(sum(a!=b for a,b in zip(s,t)) for t in fixed)

words6=list(product((0,1),repeat=6));pair_checks=0;valid_p5=[]
for a in words6:
    sa=stabilizer(a)
    for b in words6:
        sb=stabilizer(b);stack=tuple(zip(a,b))
        assert stabilizer(stack)==sa&sb;pair_checks+=1
        if sum(k=='flip' for k,_ in sa)==sum(k=='flip' for k,_ in sb)==1 and stabilizer(stack)=={('turn',0)}:
            valid_p5.append({'first':a,'second':b,'stack':stack})
witness_a=(1,0,0,0,0,0);witness_b=(0,1,0,0,0,0)
assert stabilizer(witness_a)=={('turn',0),('flip',0)}
assert stabilizer(witness_b)=={('turn',0),('flip',2)}
assert stabilizer(tuple(zip(witness_a,witness_b)))=={('turn',0)}
# Uncolored union would instead gain a reflection; identity-preserving convention matters.
assert ('flip',1) in stabilizer(tuple(int(a or b) for a,b in zip(witness_a,witness_b)))
p6_a=(1,0,0,1,0,0);p6_b=(0,1,0,0,1,0)
assert all(('turn',3) in stabilizer(s) for s in (p6_a,p6_b,tuple(zip(p6_a,p6_b))))
half_layers=[s for s in words6 if ('turn',3) in stabilizer(s)]
assert len(half_layers)==8
assert all(('turn',3) in stabilizer(tuple(zip(a,b))) for a in half_layers for b in half_layers)
# Source's four-spot non-task layer visual, preserving both marks at the overlap.
example_a=(1,1,0,0);example_b=(0,1,0,1);example_stack=tuple(zip(example_a,example_b))
assert example_stack==((1,0),(1,1),(0,0),(0,1))
assert stabilizer(example_stack)==stabilizer(example_a)&stabilizer(example_b)
geometry=[]
for n,r,spot in [(6,1.05,.23),(6,3.1,1.4),(8,1.25,.28),(8,3.7,1.4),(8,1.1,.24),(8,1.5,.3),(8,1.35,.3),(6,1.05,.25),(4,.7,.25),(6,.95,.24)]:
    pts=[(r*cos(pi/2-2*pi*i/n),r*sin(pi/2-2*pi*i/n)) for i in range(n)]
    ds=[hypot(pts[i][0]-pts[(i+1)%n][0],pts[i][1]-pts[(i+1)%n][1]) for i in range(n)]
    assert max(ds)-min(ds)<1e-10 and min(ds)>2*spot
    geometry.append({'n':n,'ring_radius_cm':r,'spot_diameter_mm':20*spot,'adjacent_centers_mm':10*min(ds),'regular':True,'spot_overlap':False,'working_mat':spot==1.4})
assert all(g['spot_diameter_mm']>=28 for g in geometry if g['working_mat'])
result={'week':34,'status':'pass','source':'final/bonus.pdf','problems_checked':list(range(1,7)),
'problem1_witnesses':{str(k):{'word':s,'matching_motions':sorted(stabilizer(s))} for k,s in p1.items()},
'problem2_six_ring_flip_distribution':dict(sorted(Counter(p['flips'] for p in c6).items())),'eight_ring_flip_distribution':dict(sorted(Counter(p['flips'] for p in c8).items())),
'problem2_general_obstruction':'Matching rotations form a subgroup of the six rotations. Matching flips, if nonempty, are a coset of this subgroup: compose a fixed matching flip with each matching turn. Thus their number is either zero or a divisor of six, never four. This holds for any fixed kinds.',
'problem3_and_4_starting_word':start,'problem3_and_4_all_best_repairs':p34,
'non_task_layer_example':{'first':example_a,'second':example_b,'ordered_pair_stack':example_stack,'overlap_index':1},
'problem5_witness':{'first':witness_a,'second':witness_b,'first_motions':sorted(stabilizer(witness_a)),'second_motions':sorted(stabilizer(witness_b)),'stack_motions':sorted(stabilizer(tuple(zip(witness_a,witness_b))))},
'problem5_complete_ordered_pair_count':len(valid_p5),'all_six_layer_pair_intersection_checks':pair_checks,
'problem6_witness':{'first':p6_a,'second':p6_b,'stack_motions':sorted(stabilizer(tuple(zip(p6_a,p6_b))))},'problem6_complete_halfturn_layer_pairs':len(half_layers)**2,
'problem6_explanation':'For any spot i, both layers agree at i and i+3, so the ordered pair agrees there too. A motion common to both layers always survives in the stack.',
'geometry':geometry,'diagram_audit':'All four rendered pages inspected; both starting patterns read AAABBABB clockwise from top; half-turn card is 4 spots, reflection card vertical fixes top/bottom, rotation cards clockwise 1 and 2 spots; layer marks remain distinct at overlap; regular equal scaling and >=28 mm working spots verified. No physical overlay rehearsal.', 'issues':[]}
root=Path(__file__).resolve().parent
finalsrc=Path(__file__).resolve().parents[1]/'student-src'/'bonus.tex'
pdf=Path(__file__).resolve().parents[1]/'reference-pdfs'/'week-34-bonus.pdf'
result['pdf_sha256']=hashlib.sha256(pdf.read_bytes()).hexdigest()
# Bind checks to the actual final task/diagram source inspected in final-audit.md.
result['stage']='independent final mathematical audit'
result['source_sha256']=hashlib.sha256(finalsrc.read_bytes()).hexdigest()
assert result['source_sha256']=='0dff27ad474e9d3f47d33468f247a378f2b8155482d21f5cb3889c0dbff3b3dc', 'Final source changed: re-audit tasks/diagrams.'
result['final_source_bound']=True
try:
    import pymupdf
except ImportError:
    result['pdf_text_verification']='PyMuPDF unavailable; PDF file hash recorded.'
else:
    import re
    with pymupdf.open(pdf) as document:
        result['pages']=len(document)
        printed='\n'.join(page.get_text() for page in document)
        numbers=list(map(int,re.findall(r'Problem (\d+):',printed)))
        assert numbers==result['problems_checked']
        result['actual_pdf_problem_numbers']=numbers
        assert 'ignore' in printed and 'square faces' in printed
        result['pdf_text_verification']='All final pages, numbered tasks and mark-only convention checked.'
result['diagram_audit']='All four actual final PDF pages inspected, including reordered P5 working/record rings and three new P6 six-spot recording rings. Regular equal scaling and 28 mm working spots preserved. See final-audit.md; physical procedure untested.'
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'repair_results':p34,'six_flip_counts':result['problem2_six_ring_flip_distribution'],'eight_flip_counts':result['eight_ring_flip_distribution'],'layer_pairs_checked':pair_checks,'p5_valid_ordered_pairs':len(valid_p5)},indent=2))
