"""Independent interval intersections and exact endpoint extrema."""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json
rectangles=[(a,6-a,a*(6-a)) for a in range(1,6)];assert min(x[2] for x in rectangles)==5 and max(x[2] for x in rectangles)==9
rows=[[(2,7),(4,9),(5,6)],[(1,4),(3,8),(5,9)],[(1,4),(6,8),(7,9)]]
def intersect(intervals):return (max(a for a,b in intervals),min(b for a,b in intervals))
assert intersect(rows[0])==(5,6)
false=[]
for row in rows[1:]:
    solutions={}
    for i,(a,b) in enumerate(row):
        lo,hi=intersect([p for j,p in enumerate(row) if i!=j])
        candidates=[F(k,2) for k in range(0,21) if lo<=F(k,2)<=hi and not a<=F(k,2)<=b]
        if candidates:solutions[i+1]=[str(c) for c in candidates]
    false.append(solutions)
assert set(false[0])=={1,3} and set(false[1])=={1}
pairs=[((3,7),(5,9)),((2,4),(6,8)),((3,5),(5,7))];gaps=[]
for (a,b),(c,d) in pairs:
    samples=[(F(x,2),F(y,2)) for x in range(2*a,2*b+1) for y in range(2*c,2*d+1)]
    lo=min(abs(x-y) for x,y in samples);hi=max(abs(x-y) for x,y in samples)
    formula=(max(0,a-d,c-b),max(abs(a-d),abs(b-c)))
    assert (lo,hi)==formula
    gaps.append({'A':[a,b],'B':[c,d],'gap':list(formula),'A_can_be_longer':any(x>y for x,y in samples),'B_can_be_longer':any(y>x for x,y in samples),'tie_possible':any(x==y for x,y in samples)})
assert [x['gap'] for x in gaps]==[[0,6],[2,6],[0,4]]
assert [(x['A_can_be_longer'],x['B_can_be_longer'],x['tie_possible']) for x in gaps]==[(True,True,True),(False,True,False),(False,True,True)]
design=[(x,y) for x,y in product(range(4,7),repeat=2)];assert max(abs(x-y) for x,y in design)==2 and any(x>y for x,y in design) and any(y>x for x,y in design)
result={'rectangles':rectangles,'true_row_intersection':intersect(rows[0]),'false_card_witnesses':false,'absolute_gap_cases':gaps,'designed_ranges':{'A':[4,6],'B':[4,6],'max_gap':2},'worked_examples':{'tile_rectangle':[2,3,6],'shared_length':{'value':2.5,'ranges':[[2,3],[1,4]]}}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
