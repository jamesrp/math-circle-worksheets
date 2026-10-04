from towers import *
from grader import grade
from itertools import combinations, product
from collections import Counter
n=3
data=all_with_clues(n)
keys=sorted(data[0][1].keys())
# single clue solution counts
for k in [('L',0)]:
    for v in (1,2,3):
        print(k,v,len(solutions(3,{k:v})))
# 2-clue sets (any values) with solution counts
cnt=Counter()
examples={}
for a,b in combinations(keys,2):
    for va,vb in product((1,2,3),repeat=2):
        s=len(solutions(3,{a:va,b:vb}))
        cnt[s]+=1
        examples.setdefault(s,[]).append(((a,va),(b,vb)))
print(sorted(cnt.items()))
for s in (2,3):
    print(s, examples[s][:12])
