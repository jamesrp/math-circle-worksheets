from itertools import product,combinations

def adj(vertices,edges):
 return {v:{v}|{b for a,b in edges if a==v}|{a for a,b in edges if b==v} for v in vertices}
def win(a,k=1):
 # A whole cops-turn is one action; terminal captures are absorbing.
 states=list(product(product(a,repeat=k),a,(0,1)))
 good={(cs,r,t) for cs,r,t in states if r in cs}
 while True:
  extra=set()
  for cs,r,t in states:
   if (cs,r,t) in good:continue
   if t==0:
    if any((ds,r,1) in good for ds in product(*(a[c] for c in cs))):extra.add((cs,r,t))
   elif all((cs,s,0) in good for s in a[r]):extra.add((cs,r,t))
  if not extra:return {cs for cs in product(a,repeat=k) if all((cs,r,0) in good for r in a)}
  good|=extra

def cycle(n):return [(i,(i+1)%n) for i in range(n)]
assert win(adj(range(5),[(i,i+1) for i in range(4)]))=={(i,) for i in range(5)}
for n in range(3,10):
 a=adj(range(n),cycle(n))
 assert bool(win(a))==(n==3)
 assert (0,0) in win(a,2)
for n,need in [(4,1),(5,2)]:
 edges=cycle(n);missing=[e for e in combinations(range(n),2) if e[1] not in adj(range(n),edges)[e[0]]]
 found=[]
 for m in range(len(missing)+1):
  for add in combinations(missing,m):
   if win(adj(range(n),edges+list(add))):found.append(m)
 assert min(found)==need
f1=adj('abcdef',[tuple(e) for e in ['ab','bc','ac','cd','de','af']])
for v,u in [('e','d'),('d','c'),('f','a'),('a','b'),('b','c')]:
 assert f1[v]<=f1[u]
 del f1[v]
 for x in f1:f1[x].discard(v)
assert list(f1)==['c']
f2=adj('abcde',[tuple(e) for e in ['ab','bc','cd','de','ea','ac']])
assert {(v,u) for v in f2 for u in f2 if v!=u and f2[v]<=f2[u]}=={('b','a'),('b','c')}
print('PASS: independent finite pursuit solver; rings3–9 for one/two cops; every square/pentagon chord set; exact printed fold sequence and all initial F2 folds.')
