"""Coordinator sumset verification, independent of student/guide checkers."""
from itertools import combinations, product
from pathlib import Path
import json

def sums(a,b): return sorted({x+y for x in a for y in b})
def gap(a):
    ds={y-x for x,y in zip(a,a[1:])}
    return next(iter(ds)) if len(ds)==1 else None
fixed=[([0,2],[1,3]),([0,2],[1,4]),([0,1,2],[0,1,2]),
       ([0,1,3],[0,1,3]),([0,1,2],[0,3,6]),
       ([1,3,5],[2,4]),([0,2,4],[0,3]),([0,2,4],[1,3]),([0,3,6],[1,4]),
       ([4],[0,1,3]),([2],[0,2,4]),([0],[1,4,6,9]),
       ([1,4],[0,2,5,8]),([-2,0,2],[-3,-1,1])]
expected=[[1,3,5],[1,3,4,6],[0,1,2,3,4],[0,1,2,3,4,6],list(range(9)),
          [3,5,7,9],[0,2,3,4,5,7],[1,3,5,7],[1,4,7,10],
          [4,5,7],[2,4,6],[1,4,6,9],[1,3,4,6,9,12],[-5,-3,-1,1,3]]
assert [sums(*p) for p in fixed]==expected
triples=list(combinations(range(10),3))
sizes=[len(sums(a,b)) for a,b in product(triples,repeat=2)]
assert min(sizes)==5 and max(sizes)==9
p5=[list(b) for b in combinations(range(10),2) if len(sums([0,3,6],b))==4]
assert p5==[[i,i+3] for i in range(7)]
assert sum(len(sums([0,2,4],b))==4 for b in combinations(range(10),2))==8
assert not any(len(sums([0,1,3],b))==4 for b in combinations(range(10),2))
sets=[c for k in range(1,8) for c in combinations(range(7),k)]
eq=0
for a,b in product(sets,repeat=2):
    t=len(sums(a,b));m,n=len(a),len(b)
    assert m+n-1<=t<=m*n
    if min(m,n)>=2:
        assert (t==m+n-1)==(gap(a) is not None and gap(a)==gap(b))
        eq+=t==m+n-1

def routes(a,b):
    moves=len(a)+len(b)-2;out=[]
    for ups in combinations(range(moves),len(a)-1):
        word=''.join('U' if p in ups else 'R' for p in range(moves))
        i=j=0;vals=[a[0]+b[0]]
        for v in word:
            i+=v=='U';j+=v=='R';vals.append(a[i]+b[j])
        assert all(x<y for x,y in zip(vals,vals[1:]))
        assert len(vals)==len(a)+len(b)-1
        out.append({'moves':word,'totals':vals})
    return out
grids=[([1,5],[0,2,6]),([0,2,5],[1,3,4]),([1,3,5],[0,2,4,6])]
paths=[routes(*p) for p in grids];assert [len(p) for p in paths]==[3,6,10]
assert all(p['totals']==[1,3,5,7,9,11] for p in paths[2])
out={'fixed':[{ 'A':a,'B':b,'totals':s} for (a,b),s in zip(fixed,expected)],
     'all_14400_three_card_kit_pairs_extrema':[min(sizes),max(sizes)],
     'P5_complete_B':p5,'all_16129_nonempty_0_to_6_set_pairs_bounds_and_equality':True,
     'nonsingleton_equality_pairs_checked':eq,'routes':paths,
     'proof_review':'Every full monotone path strictly increases and contains m+n-1 values. At equality two full paths differing only RU/UR must have the same nonshared middle value, forcing every A gap equal to every B gap. Common-gap inputs realize every index sum; singleton has no gap. Pair count bounds above. This general proof does not depend on finite enumeration.'}
p=Path(__file__).parent/'guide-review-assets/independent-guide-checks.json';p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n')
print('Fixed examples, 14400 kit pairs, 45-choice catalogs, 16129 finite-set pairs and all19 routes verified.')
