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

# v3 all-first-move comparisons and explicit equalizing replies.
assert [n for n in (1,3,4) if not win(1,4-n)] == [1,3]
replies=[(0,1,1,3),(0,3,1,3),(0,4,1,4),(1,1,1,1),(1,3,0,1),(1,4,0,4)]
for side,take,reply_side,reply_take in replies:
    pair=[4,6];pair[side]-=take
    assert pair[side]>=0 and G[pair[0]]!=G[pair[1]]
    pair[reply_side]-=reply_take
    assert pair[reply_side]>=0 and G[pair[0]]==G[pair[1]]
labels=['W' if g else 'L' for g in G]
for start in range(24):
    window=labels[start:start+4]
    assert labels[start+4] == ('W' if any(window[i]=='L' for i in (0,1,3)) else 'L')
assert labels[:4]==labels[7:11]==list('LWLW')
assert labels[1:5]==labels[8:12]==list('WLWW')
print('Week 07 v3 PASS: all equalizing replies and concrete window extensions')

# Printed upper Problem 7 strategy trial: 24 is W and take 1 leaves 23 L.
assert G[24] != 0 and G[23] == 0 and 24-1==23
assert 24 % 7 == 3 and 23 % 7 == 2
print('Week 07 printed-trial PASS: 24 -> 23 is a legal winning first move')
