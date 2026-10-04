#!/usr/bin/env python3
from itertools import combinations,product
from pathlib import Path
import json
def represented(kit): return {abs(sum(w*s for w,s in zip(kit,states))) for states in product((-1,0,1),repeat=len(kit))}
robust=[list(k) for k in combinations(range(1,9),3) if all({1,2,3}<=represented(pair) for pair in combinations(k,2))]
assert robust==[[1,2,3]]
assert not [k for k in combinations(range(1,9),3) if all({1,2,3,4}<=represented(pair) for pair in combinations(k,2))]
def partitions(items,m):
    target=sum(items)/m
    found=[]
    def rec(i,groups):
        if i==len(items):
            if len(groups)==m and all(sum(g)==target for g in groups):found.append([g[:] for g in groups])
            return
        w=items[i]
        for g in groups:
            if sum(g)+w<=target:g.append(w);rec(i+1,groups);g.pop()
        if len(groups)<m and w<=target:groups.append([w]);rec(i+1,groups);groups.pop()
    rec(0,[])
    return found
teams={str((tuple(k),m)):partitions(k,m) for k,m in [(list(range(1,5)),2),(list(range(1,7)),3),([1,2,5],2),(list(range(1,9)),4)]}
assert len(teams[str((tuple(range(1,7)),3))])==1
assert not teams[str(((1,2,5),2))]
def guess(t):
    if t==4:return 4
    threshold=2 if t<4 else 6
    return threshold-1 if t<threshold else threshold if t==threshold else threshold+1
assert all(guess(t)==t for t in range(1,8))
report={'robust_triples_1_to_8':robust,'pair_positive_targets':{str(p):sorted(represented(p)-{0}) for p in combinations((1,2,3),2)},'equal_team_partitions':teams,'two_comparison_capacity':7,'comparison_plan_checked':list(range(1,8))}
(Path(__file__).resolve().parent.parent/'writer-check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
