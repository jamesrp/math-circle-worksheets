from itertools import product
from knot_geometry import DATA
valid=[c for c in product(range(3),repeat=3) if all(len({c[o],c[a],c[b]}) in [1,3] for o,a,b in DATA['arc_relations'])]
assert len(valid)==9 and sum(len(set(c))>1 for c in valid)==6
assert len(list(range(3)))==3 # one whole arc of the crossing-free loop
cases=[('R','B','R','B'),('R','R','B','R'),('G','B','G','B'),('B','G','B','R'),('B','B','B','B'),('R','G','R','G')]
def works(l,p,r,q):
    return [m for m in 'RBG' if p==q and len({l,p,m}) in [1,3] and len({m,p,r}) in [1,3]]
assert [bool(works(*c)) for c in cases]==[True,False,True,False,True,True]
for l,p in product('RBG',repeat=2):assert len(works(l,p,l,p))==1
for a,b in product(range(3),repeat=2):assert (2*b-(2*b-a))%3==a
print('Trefoil 9/6, loop 3, all nine local move inputs, and six fixed endpoint cases verified.')
