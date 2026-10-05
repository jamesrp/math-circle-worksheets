from itertools import combinations, product
def w(x,y): return sum(a>b for a in x for b in y)
S=set(range(1,10)); res=[]
for A in combinations(sorted(S),3):
  R=S-set(A)
  for B in combinations(sorted(R),3):
    C=tuple(sorted(R-set(B)))
    e=(w(A,B),w(B,C),w(C,A))
    if min(e)>=5: res.append((A,B,C,e))
print(len(res)); 
from collections import Counter
print(Counter(tuple(sorted(r[3])) for r in res))
for r in res: print(r)
# 1-6 repeats within deck allowed, no value shared across decks
best=None; cnt=Counter()
vals=range(1,7)
from itertools import combinations_with_replacement as cwr
decks=list(cwr(vals,3))
for A in decks:
  for B in decks:
    if set(A)&set(B): continue
    for C in decks:
      if set(C)&set(A) or set(C)&set(B): continue
      e=(w(A,B),w(B,C),w(C,A))
      if min(e)>=5:
        cnt[min(e)]+=1
        if best is None or min(e)>min(best[3]): best=(A,B,C,e)
print(cnt, best)
