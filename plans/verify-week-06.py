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

# v3 staged score records, independently recomputed from position matches.
for probes, expected in [
    (('RRR','BRR','RBR'), {'BRR':(2,3,1),'RBR':(2,1,3),'RRB':(2,1,1),'BBB':(0,1,1)}),
    (('RRRR','BRRR','RBRR','RRBR'), {'RBRB':(2,1,3,1),'BRBR':(2,3,1,3),'RBBB':(1,0,2,2),'RRRR':(4,3,3,3)}),
    (('00000','00011','00101','01001'), {'00000':(5,3,3,3),'11111':(0,2,2,2),'10010':(3,3,1,1),'01110':(2,2,2,2),'11110':(1,1,1,1),'00001':(4,4,4,4),'10001':(3,3,3,3)}),
]:
    for secret, scores in expected.items():
        assert tuple(score(q,secret) for q in probes)==scores
# Symmetry must preserve every score, not only the printed examples.
for n in (3,4):
    for mask in codes(n):
        flip=lambda a: tuple(x^m for x,m in zip(a,mask))
        for q in codes(n):
            for secret in codes(n):assert score(q,secret)==score(flip(q),flip(secret))
print('Week 06 v3 PASS: staged score records and every coordinate-renaming score')
