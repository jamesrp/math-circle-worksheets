"""Exhaustive finite checks for Week 5; proofs are in the facilitator guide."""
from itertools import permutations, combinations

def latin(n):
    rows=list(permutations(range(1,n+1)))
    def grow(square):
        if len(square)==n:
            yield tuple(square); return
        for row in rows:
            if all(all(old[j]!=row[j] for old in square) for j in range(n)):
                yield from grow(square+[row])
    return list(grow([]))
def visible(row):
    high=0; count=0
    for x in row:
        if x>high: high=x; count+=1
    return count
def clues(a):
    return tuple(visible(row) for row in a)+tuple(visible(row[::-1]) for row in a)+tuple(visible(c) for c in zip(*a))+tuple(visible(c[::-1]) for c in zip(*a))
L3=latin(3); L4=latin(4)
assert len(L3)==12 and len(L4)==576
s1=[a for a in L3 if clues(a)[6]==3 and clues(a)[4]==2]
assert s1==[((1,2,3),(2,3,1),(3,1,2))]
assert len([a for a in L3 if clues(a)[6]==3])==2
for i in range(12):
    for val in range(1,4):assert sum(clues(a)[i]==val for a in L3)!=1
T=tuple(tuple((i+j)%4+1 for j in range(4)) for i in range(4))
indices=(2,3,5,6,7); tc=clues(T)
precomputed=[(a,clues(a)) for a in L4]
select=lambda ids:[a for a,c in precomputed if all(c[i]==tc[i] for i in ids)]
assert select(indices)==[T]
counts=[len(select([i for i in indices if i!=j])) for j in indices]
assert counts==[2,2,6,12,20]
minimum=None
for k in range(1,6):
    examples=[ids for ids in combinations(range(16),k) if select(ids)==[T]]
    if examples:minimum=(k,examples[0]);break
V=((1,2,3,4),(2,1,4,3),(3,4,1,2),(4,3,2,1))
for r in (0,2):
    for c in (0,2):
        b=[list(row) for row in V]
        for i in (r,r+1): b[i][c],b[i][c+1]=b[i][c+1],b[i][c]
        assert tuple(map(tuple,b)) in L4
entryids=((0,0),(0,2),(2,0),(2,2))
assert len([a for a in L4 if all(a[i][j]==V[i][j] for i,j in entryids)])>1
print('Week 05 PASS: Latin counts 12/576; two-clue 3x3 unique and optimal; five-clue deletion counts',counts,'; target minimum perimeter clues',minimum)
