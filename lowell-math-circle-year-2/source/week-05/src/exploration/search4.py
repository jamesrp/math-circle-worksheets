import numpy as np
from itertools import combinations
from collections import Counter, defaultdict
from towers import *
from grader import grade
data=all_with_clues(4)
keys=sorted(data[0][1].keys())
M=np.array([[cl[k] for k in keys] for sq,cl in data])
used=set()
for s in ['1342 2413 3124 4231','1243 4132 3421 2314','3214 4123 1432 2341','2143 3412 4321 1234','4231 1324 2143 3412']:
    used|=set(s.split())
out=[]
for sub in combinations(range(16),4):
    vals=M[:,sub]
    cnt=Counter(map(tuple,vals))
    for i in range(576):
        t=tuple(vals[i])
        if cnt[t]==1 and 4 not in t:
            cs={keys[j]:int(M[i,j]) for j in sub}
            if len(set(k[0] for k in cs))<3: continue
            rows=set(''.join(map(str,x)) for x in data[i][0])
            if rows & used: continue
            g=grade(4,cs)
            if g[0]!='solved': continue
            out.append((g[2][3],g[2][2],cs,data[i][0]))
out.sort(key=lambda o:-o[0])
print(len(out))
from pick4 import fmt
for o in out[:8]:
    print(o[0],o[1]); a=fmt(o[2]).split('\n'); b=show(o[3]).split('\n')
    for j,l in enumerate(a): print(l.ljust(16), ('   '+b[j-1]) if 1<=j<=4 else '')
    print()
