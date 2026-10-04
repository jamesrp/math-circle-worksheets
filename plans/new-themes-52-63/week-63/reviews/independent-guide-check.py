"""Coordinator permutation and reversible-map checks, no author imports."""
from itertools import permutations,combinations
from collections import Counter
from math import factorial
from pathlib import Path
import json

def ders(n):return [p for p in permutations(range(n)) if all(p[i]!=i for i in range(n))]
counts=[len(ders(n)) for n in range(9)]
assert counts==[1,0,1,2,9,44,265,1854,14833]
hist={n:dict(sorted(Counter(sum(x==i for i,x in enumerate(p)) for p in permutations(range(n))).items())) for n in [3,4,5]}
assert hist[3]=={0:2,1:3,3:1}

inclusive={}
for n in [3,4,5]:
    allp=list(permutations(range(n)))
    rows=[]
    for k in range(n+1):
        values=[sum(all(p[i]==i for i in s) for p in allp) for s in combinations(range(n),k)]
        assert all(v==factorial(n-k) for v in values)
        rows.append({'k':k,'sets':len(values),'each_count':factorial(n-k),'signed_total':(-1)**k*sum(values)})
    assert sum(r['signed_total'] for r in rows)==counts[n]
    inclusive[n]=rows

maps={}
for n in range(2,8):
    z=n-1;alln=ders(n);branches=[]
    for h in range(n-1):
        fixed=[p for p in alln if p[h]==z]
        reciprocal=[p for p in fixed if p[z]==h]
        longer=[p for p in fixed if p[z]!=h]
        assert len(reciprocal)==counts[n-2] and len(longer)==counts[n-1]
        reciprocal_images=set();longer_images=set()
        for p in reciprocal:
            survivors=[i for i in range(n) if i not in [h,z]]
            q=tuple(p[i] for i in survivors)
            assert set(q)==set(survivors) and all(x!=i for x,i in zip(q,survivors))
            inverse=list(p)
            for i,x in zip(survivors,q):inverse[i]=x
            inverse[h]=z;inverse[z]=h
            assert tuple(inverse)==p
            reciprocal_images.add(q)
        for p in longer:
            x=p[z];assert x!=h and x!=z
            q=list(p[:-1]);q[h]=x;q=tuple(q)
            assert set(q)==set(range(n-1)) and all(x!=i for i,x in enumerate(q))
            inverse=list(q)+[q[h]];inverse[h]=z
            assert tuple(inverse)==p
            longer_images.add(q)
        assert len(reciprocal_images)==len(reciprocal) and len(longer_images)==len(longer)
        branches.append({'home':h,'reciprocal':len(reciprocal),'longer':len(longer),'total':len(fixed)})
    assert counts[n]==(n-1)*(counts[n-1]+counts[n-2])
    maps[n]=branches

def names(p,alphabet):return ''.join(alphabet[x] for x in p)
four=[names(p,'ABCD') for p in ders(4)]
assert four==['BADC','BCDA','BDAC','CADB','CDAB','CDBA','DABC','DCAB','DCBA']
fixedD=[names(p,'ABCD') for p in ders(4) if p[0]==3]
assert fixedD==['DABC','DCAB','DCBA']
fixedE=[names(p,'ABCDE') for p in ders(5) if p[0]==4]
recipE=[s for s in fixedE if s[4]=='A'];longE=[s for s in fixedE if s[4]!='A']
assert recipE==['ECDBA','EDBCA']
assert longE==['EABCD','EADBC','EADCB','ECABD','ECBAD','ECDAB','EDABC','EDACB','EDBAC']
assert sum(p[0]!=0 and p[1]!=1 for p in permutations(range(4)))==14

data={'scope':'all independent permutations through 8; reversible branches through 7',
      'derangements_0_to_8':counts,'exact_home_histograms':hist,
      'inclusive_intersections':inclusive,'reversible_maps':maps,
      'four_card_catalog':four,'D_at_A':fixedD,'E_at_A_reciprocal':recipE,'E_at_A_longer':longE,
      'four_cards_A_B_away':14,'physical_tests':'unperformed'}
out=Path(__file__).resolve().parent/'guide-review-assets';out.mkdir(exist_ok=True)
(out/'independent-guide-checks.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'counts':counts,'fixed_D':fixedD,'fixed_E_split':[len(recipE),len(longE)],'inclusive_and_reversible_checks':'passed'}))
