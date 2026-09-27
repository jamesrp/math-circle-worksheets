"""Subtraction recurrences and independent two-pile outcome checks."""
from functools import lru_cache

def values(moves,N):
    g=[0]
    for n in range(1,N+1):
        seen={g[n-s] for s in moves if s<=n}; x=0
        while x in seen:x+=1
        g.append(x)
    return g
G=values((1,3,4),1000)
assert all((g==0)==(n%7 in (0,2)) for n,g in enumerate(G))
assert G==([0,1,0,1,2,3,2]*144)[:1001]
assert all((g==0)==(n%3==0) for n,g in enumerate(values((1,2),1000)))
assert all((g==0)==(n%2==0) for n,g in enumerate(values((1,3,5),1000)))
@lru_cache(None)
def win(a,b):
    return any(not win(a-s,b) for s in (1,3,4) if s<=a) or any(not win(a,b-s) for s in (1,3,4) if s<=b)
assert all(win(a,b)==(G[a]!=G[b]) for a in range(31) for b in range(31))
assert not win(1,1) and win(1,4)
assert not win(1,3) and not win(4,6) and win(5,6)
print('Week 07 PASS: recurrences through1000; g period 0101232; independent two-pile outcomes through30 agree')
