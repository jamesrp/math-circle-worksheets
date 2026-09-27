"""Exact-position binary queries: exhaustive decision-tree and signature checks."""
from itertools import product
from functools import lru_cache

def codes(n):return tuple(product((0,1),repeat=n))
def score(q,s):return sum(a==b for a,b in zip(q,s))
for n in (2,3,4):
    C=codes(n)
    @lru_cache(None)
    def possible(candidates,k):
        if len(candidates)<=1:return True
        if k==0:return False
        for q in C:
            buckets={}
            for s in candidates:buckets.setdefault(score(q,s),[]).append(s)
            if len(buckets)>1 and all(possible(tuple(b),k-1) for b in buckets.values()):return True
        return False
    assert not possible(C,n-1) and possible(C,n)
    probes=[(0,)*n]+[tuple(int(j==i) for j in range(n)) for i in range(n-1)]
    assert len({tuple(score(q,s) for q in probes) for s in C})==2**n
    print(f'Week 06: {n} binary positions have exact worst-case identification cost {n}')
Q=tuple(tuple(map(int,s)) for s in ('00000','00011','00101','01001'))
assert len({tuple(score(q,s) for q in Q) for s in codes(5)})==32
secret=tuple(map(int,'10110'))
assert tuple(score(q,secret) for q in Q)==(2,2,2,0)
print('Week 06 PASS: all 32 five-bit signatures distinct; example verified')
