import random, json
from towers import *
from grader import grade
from collections import Counter
n=4
data=all_with_clues(n)
fullcount=Counter(tuple(sorted(cl.items())) for sq,cl in data)
good=[(sq,cl) for sq,cl in data if fullcount[tuple(sorted(cl.items()))]==1]
print('cities determined by all 16 clues:',len(good))
random.seed(5)
results=[]
for trial in range(3000):
    sq,cl=random.choice(good)
    keys=list(cl.keys()); random.shuffle(keys)
    cur=dict(cl)
    target=random.choice([4,5,6,7,8,9,10,11,12])
    for k in keys:
        if len(cur)<=target: break
        t=dict(cur); del t[k]
        if len(solutions(n,t))==1: cur=t
    g=grade(n,cur)
    minimal=all(len(solutions(n,{kk:v for kk,v in cur.items() if kk!=k}))>1 for k in cur)
    results.append((len(cur),g[0],g[1],g[2][2],g[2][3],minimal,sq,cur))
import pickle
pickle.dump(results,open('gen4.pkl','wb'))
c=Counter((r[0],r[1],r[2]) for r in results)
for k in sorted(c): print(k,c[k])
