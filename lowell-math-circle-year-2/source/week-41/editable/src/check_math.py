from itertools import product
D={'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}
def disp(p):return tuple(sum(D[d][i] for d in p) for i in [0,1])
def square(p,start=(1,1)):
    dx,dy=disp(p);return ((start[0]+dx)%3,(start[1]+dy)%3)
def winding(p):
    x,y=disp(p);assert x%3==y%3==0
    return x//3,y//3
assert len({square(p) for p in product(D,repeat=2)})==9
# Same arrows are translations, so H and E cannot swap.
assert not any(square(p)==(2,1) and square(p,(2,1))==(1,1) for n in range(8) for p in product(D,repeat=n))
for p in ['RRR','UUU','RRRUUU','UUURRR','RRLL','RRRUUULLLDDD','RURURU']:
 print(p,winding(p))
assert winding('RRRUUU')==winding('UUURRR')==winding('RURURU')==(1,1)
assert winding('RRLL')==winding('RRRUUULLLDDD')==(0,0)
for n in [2,3,4,5,6]:
 count=sum(square(p)==(1,1) for p in product(D,repeat=n))
 assert count>1
 print(n,'steps:',count,'returns to H')
print('Finite route checks passed; no classroom trial claimed.')

# New first-page route RRD ends in the bottom-left cell F.
assert square('RRD')==(0,0)
# Both permitted centerline square paths have equal lifted displacement.
assert disp('RU')==disp('UR')==(1,1)
# A concrete legal sequence swaps adjacent perpendicular steps only.
w='RRRUUU'; target='UUURRR'; moves=[]
while 'RU' in w:
    k=w.index('RU'); nxt=w[:k]+'UR'+w[k+2:]
    assert disp(nxt)==disp(w); moves.append((w,nxt)); w=nxt
assert w==target
assert len(moves)==9
# Backtrack insertion supplies the reverse direction missing from the draft.
assert winding('RRR')==winding('RRRRL')==(1,0)
assert disp('RL')==disp('')==(0,0)
print('Centerline square example and nine-slide concrete transformation verified; insertion/deletion is reversible.')
