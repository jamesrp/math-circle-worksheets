#!/usr/bin/env python3
"""Reviewer-owned independent checks; does not import the author's check script."""
import itertools
import json
from pathlib import Path
from fractions import Fraction as F

ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'geometry-data.json').read_text())['diagrams']

def braid(colors,word):
    colors=list(colors)
    for i,s in word:
        a,b=colors[i:i+2]
        colors[i:i+2]=[(2*a-b)%3,a] if s==1 else [b,(2*b-a)%3]
    return tuple(colors)

# The signs record A vs B, A vs C, and B vs C. A genuine R3 has a
# top/middle/bottom local height order. The two excluded patterns demand
# a cyclic height relation, impossible for a legitimate local R3 move.
valid=[s for s in itertools.product([-1,1],repeat=3)
       if s not in [(1,-1,1),(-1,1,-1)]]
for a,b,c in valid:
    for colors in itertools.product(range(3),repeat=3):
        assert braid(colors,[(0,a),(1,b),(0,c)]) == braid(colors,[(1,c),(0,b),(1,a)])

def tree(vertices,edges):
    if len(edges)!=len(vertices)-1:return False
    reached={next(iter(vertices))}
    while True:
        new=reached|{v for edge in edges for v in edge if reached.intersection(edge)}
        if new==reached:return new==vertices
        reached=new

E=D['grid_full']['edges'];V=set('ABCDEFGHI')
FACES=set(['NW','NE','SW','SE','OUT']);fmap=D['grid_courtyards']['face_edge_map']
trees=0
for bits in itertools.product([False,True],repeat=len(E)):
    kept=[e for e,b in zip(E,bits) if b]
    removed=[e for e,b in zip(E,bits) if not b]
    primal=tree(V,kept);dual=tree(FACES,[fmap[e] for e in removed])
    assert primal==dual
    trees+=primal
assert trees==192
A=set(D['grid_TA']['kept']);B=set(D['grid_TB']['kept'])
assert len(B-A)==4
for restore,remove in [('BE','DE'),('CF','EF'),('EH','GH'),('FI','HI')]:
    assert restore not in A and remove in A
    A.add(restore);A.remove(remove)
    assert tree(V,list(A))
assert A==B

color_counts={}
for name in ['knot_trefoil','knot_changed']:
    good=[c for c in itertools.product(range(3),repeat=2) if braid(c,D[name]['word'])==c]
    color_counts[name]=[len(good),sum(c[0]!=c[1] for c in good)]
assert color_counts=={'knot_trefoil':[9,6],'knot_changed':[3,0]}

addresses={}
for address in itertools.product('LR',repeat=4):
    lo=F(0);length=F(81)
    for choice in address:
        length/=3
        if choice=='R':lo+=2*length
    addresses[''.join(address)]=[lo,lo+length]
assert addresses['LLRR']==[8,9]
assert addresses['RLRL']==[60,61]
assert addresses['LRLR']==[20,21]
assert len({tuple(v) for v in addresses.values()})==16
rows=D['cantor_list']['rows']
diagonal=''.join(rows[i][i] for i in range(6))
anti=''.join('R' if c=='L' else 'L' for c in diagonal)
assert diagonal=='LRLLLR' and anti=='RLRRRL'
assert F(81)*F(2,3)**5>10
assert F(81)*F(2,3)**6<10

result={'status':'passed','R3_sign_patterns':[list(s) for s in valid],
        'R3_starting_color_cases':162,'grid_subsets':4096,'grid_trees':trees,
        'knot_color_counts':color_counts,'swap_length':4,'cantor_addresses':16,
        'cantor_missing_prefix':anti,
        'scope':'Reviewer recomputation; universal geometry and proof reasoning are recorded in systems-review-of-geometry.md.'}
(ROOT/'systems-review-geometry-checks-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
