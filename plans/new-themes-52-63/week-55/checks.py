"""Independent finite integer-sumset outline checks."""
from itertools import combinations
from pathlib import Path
import json

sets = [p for n in range(1,10) for p in combinations(range(9),n)]
def gap(p):
    ds = [b-a for a,b in zip(p,p[1:])]
    return ds[0] if ds and len(set(ds)) == 1 else None
def sums(a,b):
    return tuple(sorted({x+y for x in a for y in b}))

equalities = singletons = 0
for a in sets:
    for b in sets:
        c = sums(a,b)
        lower = len(a)+len(b)-1
        assert len(c) >= lower
        equal = len(c) == lower
        if len(a) == 1 or len(b) == 1:
            assert equal
            singletons += 1
        else:
            structured = gap(a) is not None and gap(a) == gap(b)
            assert equal == structured, (a,b,c)
            equalities += equal
        # Every monotone path has this many strictly increasing sums;
        # this representative path independently checks the lower certificate.
        path = [a[0]+y for y in b] + [x+b[-1] for x in a[1:]]
        assert len(path) == lower and all(x<y for x,y in zip(path,path[1:]))

examples = [((0,1,2),(0,1,2)), ((0,1,3),(0,1,3)),
            ((0,1,2),(0,3,6)), ((1,3,5),(2,4)),
            ((0,2,4),(0,3)), ((4,),(0,1,3)),
            ((-2,0,2),(-3,-1,1))]
result = {
    'status':'pass', 'universe':list(range(9)), 'nonempty_sets':len(sets),
    'ordered_set_pairs_checked':len(sets)**2,
    'nonsingleton_equality_pairs':equalities, 'singleton_pairs':singletons,
    'examples':[{'A':a,'B':b,'sumset':sums(a,b),'size':len(sums(a,b)),
                 'lower_bound':len(a)+len(b)-1} for a,b in examples],
    'scope':'Finite checks of examples and exact equality characterization; general path-swap proof is in research.md. No physical rehearsal or classroom pilot.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS: {len(sets)**2} ordered pairs; lower bound, equality characterization, singleton exception')
