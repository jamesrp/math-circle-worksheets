#!/usr/bin/env python3
from itertools import product
from collections import Counter
from fractions import Fraction
import json
# Candidate three-way selector: position of singleton color, regardless of majority.
def tri(w):
 if len(set(w))==1:return None
 single='R' if w.count('R')==1 else 'B'
 return w.index(single)
def pair(w):return {'BR':'square','RB':'circle'}.get(w)
def recycled(w):
 outputs=[pair(w[:2]),pair(w[2:])];out=[s for s in outputs if s]
 if not out:
  if w=='RRBB':out.append('circle')
  elif w=='BBRR':out.append('square')
 return out
results={}
for bag in ['RB','RRRB','RRB','RBBBB']:
 weights=Counter(tri(''.join(w)) for w in product(bag,repeat=3))
 assert weights[0]==weights[1]==weights[2]>0
 basic=Counter(s for p in product(bag,repeat=4) for s in [pair(''.join(p[:2])),pair(''.join(p[2:]))] if s)
 recycle=Counter(s for p in product(bag,repeat=4) for s in recycled(''.join(p)))
 assert recycle['square']==recycle['circle'];assert recycle.total()>basic.total()
 results[bag]={'three_draw_outputs':dict(weights),'basic_four_draw_outputs':dict(basic),'recycled_four_draw_outputs':dict(recycle)}
assert results['RB']['basic_four_draw_outputs']=={'square':8,'circle':8}
assert results['RB']['recycled_four_draw_outputs']=={'square':9,'circle':9}
# Exact general probabilities checked as polynomials via symbolic monomial counts.
for k in [1,2]:
 classes=Counter(tri(w) for w in map(''.join,product('RB',repeat=3)) if w.count('R')==k)
 assert classes=={0:1,1:1,2:1}
A=[('S','S'),('S','S'),('C','C'),('C','C')]
B=list(product('SC',repeat=2))
for selector in [A,B]:
 assert Counter(x for x,y in selector)==Counter(y for x,y in selector)=={'S':2,'C':2}
assert len(set(A))==2 and len(set(B))==4
print(json.dumps({'bags':results,'copied_joint':{str(k):v for k,v in Counter(A).items()},'independent_joint':{str(k):v for k,v in Counter(B).items()}},indent=2))

# Non-task four-draw visual retains two successful pair outputs.
assert recycled('BRRB')==['square','circle']
# All four-ticket designs with fair positions have support two or four, never three.
valid=Counter()
for tickets in product(list(product('SC',repeat=2)),repeat=4):
 if Counter(x for x,y in tickets)==Counter(y for x,y in tickets)=={'S':2,'C':2}:
  valid[len(set(tickets))]+=1
assert valid=={2:12,4:24}
