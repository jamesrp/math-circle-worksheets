from itertools import product
from collections import Counter
from pathlib import Path
import json
states=list(product('RB',repeat=3))
def S(a):return ('R',)+a[1:]
def T(a):return a[1:]+a[:1]
def run(w,a):
    for c in w:a={'S':S,'T':T}[c](a)
    return a
sync={n:[''.join(w) for w in product('ST',repeat=n) if len({run(w,a) for a in states})==1] for n in range(6)}
assert all(not sync[n] for n in range(5)) and sync[5]==['STSTS']
def copy(a,i,j):
    b=list(a);b[j]=a[i];return tuple(b)
instructions=[('C',i,j) for i in range(3) for j in range(3)]+[('S',i) for i in range(3)]
def apply(a,op):
    if op[0]=='C':return copy(a,op[1],op[2])
    b=list(a);b[op[1]]='R';return tuple(b)
minimum=None;count=None
for n in range(1,4):
    winners=[]
    for w in product(instructions,repeat=n):
        if sum(op[0]=='S' for op in w)!=1:continue
        out=[]
        for a in states:
            for op in w:a=apply(a,op)
            out.append(a)
        if len(set(out))==1:winners.append(w)
    if winners:minimum=n;count=len(winners);break
assert minimum==3
coverage={n:sum(len(set(w))==3 for w in product([1,2,3],repeat=n)) for n in [3,4]}
assert coverage=={3:6,4:36}
# Exact final-color histogram for all covering four-slot stories.
color_hist_valid=True
for slots in product(range(3),repeat=4):
    if len(set(slots))<3:continue
    hist=Counter()
    for cols in product('RB',repeat=4):
        a=list('BBB')
        for i,c in zip(slots,cols):a[i]=c
        hist[''.join(a)]+=1
    color_hist_valid &= set(hist.values())=={2} and len(hist)==8
result={'S_T_synchronizing_words_by_length':sync,'one_reset_copy_minimum':minimum,'number_minimal_copy_reset_words':count,'coverage_numerator':coverage,'coverage_denominators':{3:27,4:81},'uniform_final_colors_all_covering_four_draw_stories':color_hist_valid,'worked_copy_example':{'RBR':copy(tuple('RBR'),0,1),'BRB':copy(tuple('BRB'),0,1)},'worked_rotation_example':{'RBB':T(tuple('RBB'))}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
