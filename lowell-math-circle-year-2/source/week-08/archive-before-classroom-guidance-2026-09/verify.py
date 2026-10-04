#!/usr/bin/env python3
"""Independent finite checks; proofs live in the facilitator guide."""
from functools import lru_cache
from itertools import product
from math import sqrt
@lru_cache(None)
def nim_win(p):
 return any(not nim_win(p[:i]+(v,)+p[i+1:]) for i,x in enumerate(p) for v in range(x))
for p in product(range(13),repeat=3):
 assert nim_win(p)==bool(p[0]^p[1]^p[2]),p
for a,b in product(range(13),repeat=2):
 assert nim_win((a,b))==(a!=b)
@lru_cache(None)
def wythoff_win(a,b):
 moves=[(v,b) for v in range(a)]+[(a,v) for v in range(b)]+[(a-d,b-d) for d in range(1,min(a,b)+1)]
 return any(not wythoff_win(*m) for m in moves)
phi=(1+sqrt(5))/2
pairs={(int(n*phi),int(n*phi*phi)) for n in range(40)}
for a,b in product(range(31),repeat=2):
 assert (not wythoff_win(a,b))==((min(a,b),max(a,b)) in pairs),(a,b)
for p,new in [((1,2,4),(1,2,3)),((3,4,5),(1,4,5)),((1,5,7),(1,5,4)),((7,10,12),(6,10,12))]:
 assert nim_win(p) and not nim_win(new)
 assert sum(x!=y for x,y in zip(p,new))==1 and all(x>=y for x,y in zip(p,new))
print('PASS: 2197 three-pile positions, 169 two-pile positions, 961 Wythoff positions; stated sample moves.')
print('Wythoff traps in 0<=a<=b<=7:',sorted(p for p in pairs if p[1]<=7))
