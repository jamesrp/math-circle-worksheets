#!/usr/bin/env python3
"""Exact finite verification for worksheet trial GA-25/26/29 (stdlib only)."""
from fractions import Fraction as F
from itertools import combinations, product
import json
from pathlib import Path
OUT=Path(__file__).with_name('geometry-checks-results.json')
vertices=list('ABCDEFGHI')
edges=['AB','BC','DE','EF','GH','HI','AD','DG','BE','EH','CF','FI']
faces=['NW','NE','SW','SE','OUT']
dual={'AB':['NW','OUT'],'BC':['NE','OUT'],'DE':['NW','SW'],'EF':['NE','SE'],'GH':['SW','OUT'],'HI':['SE','OUT'],'AD':['NW','OUT'],'DG':['SW','OUT'],'BE':['NW','NE'],'EH':['SW','SE'],'CF':['NE','OUT'],'FI':['SE','OUT']}
def components(vs,es):
    unseen=set(vs); ans=[]
    while unseen:
        stack=[unseen.pop()]; comp=set(stack)
        while stack:
            v=stack.pop()
            for a,b in es:
                if v==a: w=b
                elif v==b: w=a
                else: continue
                if w in unseen: unseen.remove(w);comp.add(w);stack.append(w)
        ans.append(sorted(comp))
    return ans

def tree(vs,es): return len(es)==len(vs)-1 and len(components(vs,es))==1
alltrees=[]
for kept in combinations(edges,8):
    if tree(vertices,kept):
        deleted=sorted(set(edges)-set(kept))
        assert tree(faces,[dual[e] for e in deleted])
        alltrees.append(list(kept))
assert len(alltrees)==192
# Stronger biconditional for EVERY subset (including 7-,9-edge candidates).
for mask in range(1<<len(edges)):
    kept=[e for i,e in enumerate(edges) if mask>>i&1]
    removed=set(edges)-set(kept)
    assert tree(vertices,kept)==tree(faces,[dual[e] for e in removed])
TA=set(['AB','BC','DE','EF','GH','HI','AD','DG'])
TB=set(['AB','BC','AD','DG','BE','EH','CF','FI'])
swaps=[('BE','DE'),('CF','EF'),('EH','GH'),('FI','HI')]
current=set(TA);swap_history=[sorted(current)]
for op,cl in swaps:
    assert op not in current and cl in current
    current.add(op);current.remove(cl)
    assert tree(vertices,list(current))
    swap_history.append(sorted(current))
assert current==TB and len(TB-TA)==4
perimeter=['AB','BC','CF','FI','HI','GH','DG','AD']
assert len(components(vertices,perimeter))==2

def cross(a,b,sign=1):
    return ((2*a-b)%3,a) if sign==1 else (b,(2*b-a)%3)
def braid(inp,word):
    v=list(inp);states=[v.copy()]
    for gen,sign in word:
        v[gen],v[gen+1]=cross(v[gen],v[gen+1],sign);states.append(v.copy())
    return v,states
kp=[(0,1)]*3;ku=[(0,1),(0,-1),(0,1)]
colorings={}
for name,word in [('trefoil',kp),('changed_middle',ku)]:
    solutions=[]
    for inp in product(range(3),repeat=2):
        out,st=braid(inp,word)
        if list(inp)==out: solutions.append({'input':list(inp),'states':st})
    colorings[name]=solutions
assert len(colorings['trefoil'])==9 and len(colorings['changed_middle'])==3
for a,b in product(range(3),repeat=2):
    for sign in [-1,1]: assert braid((a,b),[(0,sign),(0,-sign)])[0]==[a,b]
for a in range(3): assert (2*a-a)%3==a
r3=[]
for inp in product(range(3),repeat=3):
    l,ls=braid(inp,[(0,1),(1,1),(0,1)])
    r,rs=braid(inp,[(1,1),(0,1),(1,1)])
    assert l==r
    r3.append({'input':inp,'output':l,'left_states':ls,'right_states':rs})
r3_sign_cases=[]
for signs in product([-1,1],repeat=3):
    if signs in [(1,-1,1),(-1,1,-1)]: continue
    a,b,c=signs
    for inp in product(range(3),repeat=3):
        l,_=braid(inp,[(0,a),(1,b),(0,c)])
        r,_=braid(inp,[(1,c),(0,b),(1,a)])
        assert l==r
    r3_sign_cases.append(list(signs))
assert len(r3_sign_cases)==6
# Distinct colour equality patterns suffice, as arbitrary colour permutations preserve rule.
r3_patterns=[v for v in r3 if v['input'] in [(0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,1,2)]]
# Geometric braid shadow: each slab has exactly one intended double point;
# outer closure polylines cannot intersect slab interiors (x outside [-1,1]).
def orientation(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def strict_cross(a,b,c,d): return orientation(a,b,c)*orientation(a,b,d)<0 and orientation(c,d,a)*orientation(c,d,b)<0
segments=[]
for j in range(3):
    y=3-j
    segments += [((-1,y),(1,y-1)),((1,y),(-1,y-1))]
for side in [-1,1]:
    pts=[(side,0),(2*side,-.3),(2*side,3.3),(side,3)]
    segments.extend(zip(pts,pts[1:]))
intersections=[(i,j) for i,j in combinations(range(len(segments)),2) if strict_cross(*segments[i],*segments[j])]
assert intersections==[(0,1),(2,3),(4,5)]
# Closure of odd two-strand braid has one component: swap permutation's one cycle.
perm=[0,1]
for _ in range(3):perm.reverse()
assert perm==[1,0]

stages=[[(F(0),F(81))]]
for n in range(1,7):
    nxt=[]
    for a,b in stages[-1]:
        t=(b-a)/3;nxt.extend([(a,a+t),(b-t,b)])
    stages.append(nxt)
    assert len(nxt)==2**n and sum(b-a for a,b in nxt)==F(81)*F(2,3)**n
addresses=[]
for addr in product('LR',repeat=4):
    a,b=F(0),F(81)
    for c in addr:
        third=(b-a)/3
        if c=='L':b=a+third
        else:a=b-third
    addresses.append({'address':''.join(addr),'interval':[str(a),str(b)]})
assert [tuple(map(F,x['interval'])) for x in addresses]==stages[4]
assert sum(b-a for a,b in stages[5])>10 and sum(b-a for a,b in stages[6])<10
assert len(stages[6])>50
point_checks={}
for x in [9,18,27,40,54,60,63,15,5,26]:
    first=next((n for n,st in enumerate(stages) if not any(a<=x<=b for a,b in st)),None)
    point_checks[x]=first
assert point_checks=={9:None,18:None,27:None,40:1,54:None,60:None,63:None,15:2,5:3,26:None}
list_prefixes=['LLLLLL','RRRRRR','LRLRLR','RLRLRL','LLRRLL','RRLLRR']
diagonal=''.join(row[n] for n,row in enumerate(list_prefixes))
anti=''.join('R' if c=='L' else 'L' for c in diagonal)
assert anti=='RLRRRL'
result={'status':'pass','graph':{'vertices':vertices,'edges':edges,'spanning_tree_count':len(alltrees),'dual_tree_biconditional_subsets_checked':4096,'swap_history':swap_history,'minimal_swaps':4,'perimeter_components':components(vertices,perimeter)},'knots':{'counts':{k:len(v) for k,v in colorings.items()},'closed_braid_colorings':colorings,'R1_cases':3,'R2_cases':18,'R3_cases':27,'R3_all_legal_sign_cases':162,'R3_legal_sign_triples':r3_sign_cases,'R3_five_patterns':r3_patterns,'shadow_crossing_segment_pairs':intersections,'closed_components':1},'cantor':{'stages':[{'n':n,'pieces':len(st),'piece_length':str(F(81,3**n)),'total':str(sum(b-a for a,b in st)),'intervals':[[str(a),str(b)]for a,b in st]}for n,st in enumerate(stages)],'four_step_addresses':addresses,'first_removed_round':point_checks,'diagonal':diagonal,'missing_prefix':anti}}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print('PASS: 4096 graph/dual subsets; 192 trees; four optimal swaps; braid diagram intersections; 9/3 knot colors; all R1/R2/R3 cases, including162 signed R3 color assignments; exact Cantor intervals/addresses/budget.')
