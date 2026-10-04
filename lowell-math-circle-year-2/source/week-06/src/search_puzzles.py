from itertools import product
def score(t, s): return sum(a == b for a, b in zip(t, s))
def codes(n): return [''.join(p) for p in product('RY', repeat=n)]
def flips(a,b): return sum(x!=y for x,y in zip(a,b))
# 3-counter, 3 tests, unique solution, no test equal to the secret, no two tests one flip apart,
# no all-same test
n=3
out=[]
for s in codes(n):
    for ts in product(codes(n), repeat=3):
        if s in ts or len(set(ts))<3: continue
        if any(t in ('RRR','YYY') for t in ts): continue
        if any(flips(ts[i],ts[j])==1 for i in range(3) for j in range(i+1,3)): continue
        rec=[(t,score(t,s)) for t in ts]
        sols=[c for c in codes(n) if all(score(t,c)==sc for t,sc in rec)]
        # also require first two tests to leave >1
        sols2=[c for c in codes(n) if all(score(t,c)==sc for t,sc in rec[:2])]
        if len(sols)==1 and len(sols2)>1:
            out.append((s,rec,len(sols2)))
print(len(out))
for o in out[:30]: print(o)
