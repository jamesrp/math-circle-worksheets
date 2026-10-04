from itertools import combinations,product
from pathlib import Path
import json
P=list(product(range(3),repeat=2))
def third(a,b):return tuple((-x-y)%3 for x,y in zip(a,b))
lines={frozenset((a,b,third(a,b))) for a,b in combinations(P,2)}
assert len(lines)==12
def cap(S):return not any(L<=S for L in lines)
caps={n:[frozenset(c) for c in combinations(P,n) if cap(frozenset(c))] for n in range(6)}
assert [len(caps[n]) for n in range(6)]==[1,9,36,72,54,0]
extensions={n:sorted({sum(cap(S|{p}) for p in P if p not in S) for S in caps[n]}) for n in range(5)}
assert extensions[3]==[3] and extensions[4]==[0]
assert all(extensions[n][0]>0 for n in range(4))
intersections=sorted({len(a&b) for a,b in combinations(lines,2)})
assert intersections==[0,1]
assert {sum(p in L for L in lines) for p in P}=={4}
parts=[ls for ls in combinations(lines,3) if len(set().union(*ls))==9]
assert len(parts)==4
# Revised bent display and its fill-comparison row.
assert frozenset(((0,0),(1,2),(2,1))) in lines
assert frozenset(((0,0),(1,0),(2,2))) not in lines
pairs=[((0,0),(0,1)),((0,0),(1,0)),((0,1),(1,2)),((1,1),(2,0))]
assert [third(*q) for q in pairs]==[(0,2),(2,0),(2,0),(0,2)]
out={'affine_lines':12,'line_free_counts':{n:len(v) for n,v in caps.items()},'legal_extensions_by_size':extensions,'intersections_of_distinct_triples':intersections,'through_each_tile':4,'partitions':len(parts),'every_maximal_legal_collection_size':4,'youngest_readiness_test_performed':False}
Path(__file__).with_name('independent-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
