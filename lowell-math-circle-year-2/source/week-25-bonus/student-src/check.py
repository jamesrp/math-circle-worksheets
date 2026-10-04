#!/usr/bin/env python3
from itertools import permutations, product, combinations
from functools import lru_cache
import json
P=list(permutations(range(3)))
def diag(p): return tuple(sum(r-c==k for r,c in enumerate(p)) for k in (2,1,0,-1,-2))
def bits(p): return tuple(int(p[r]==c) for r in range(3) for c in range(3))
B=[bits(p) for p in P]
@lru_cache(None)
def depth(ids):
 if len(ids)<=1:return 0
 best=99
 for j in range(9):
  yes=tuple(i for i in ids if B[i][j]); no=tuple(i for i in ids if not B[i][j])
  if yes and no:best=min(best,1+max(depth(yes),depth(no)))
 return best
fixed={n:sum(len({tuple(b[j] for j in q) for b in B})==6 for q in combinations(range(9),n)) for n in range(1,5)}
cases=[((3,3,0),(3,3,0)),((3,2,1),(2,2,2)),((2,2,2),(3,3,0)),((3,3,1),(3,3,1))]
counts=[]
for rs,cs in cases:
 sol=[]
 for b in product((0,1),repeat=9):
  if tuple(sum(b[3*r:3*r+3]) for r in range(3))==rs and tuple(sum(b[3*r+c] for r in range(3)) for c in range(3))==cs:sol.append(' / '.join(''.join(str(x) for x in b[3*r:3*r+3]) for r in range(3)))
 counts.append({'rows':rs,'columns':cs,'solutions':sol})
assert depth(tuple(range(6)))==3 and fixed[3]==0 and fixed[4]>0
assert [len(c['solutions']) for c in counts]==[0,3,1,0]
print(json.dumps({'candidate_permutations':P,'diagonal_counts':[diag(p) for p in P],'adaptive_minimum':depth(tuple(range(6))),'fixed_separating_sets':fixed,'capacity_cases':counts},indent=2))
