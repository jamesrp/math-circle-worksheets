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

# Additional v3 concrete instances.
for after,reply in [((0,2,3),(0,2,2)),((1,0,3),(1,0,1)),((1,1,3),(1,1,0)),((1,2,0),(1,1,0)),((1,2,1),(1,0,1)),((1,2,2),(0,2,2)),((4,6,7),(1,6,7)),((4,6,7),(4,3,7)),((4,6,7),(4,6,2))]:
 assert nim_win(after) and not nim_win(reply)
 assert sum(x!=y for x,y in zip(after,reply))==1 and all(x>=y for x,y in zip(after,reply))
for start,end in [((2,4),(2,1)),((4,6),(3,5)),((5,7),(3,5)),((5,8),(4,7)),((8,12),(6,10))]:
 a,b=start;c,d=end
 assert a>=c and b>=d and ((a==c) != (b==d) or a-c==b-d>0)
 assert not wythoff_win(c,d)
assert not nim_win((2,5,7)) and not nim_win((3,6,5))
print('PASS: v3 complete six-reply experiment, extra repair moves, and designed balanced piles.')
