"""Finite visible-position game checks; capture/stay/placement conventions match print."""
from itertools import product

def graph(n,edges):
 a=[{i} for i in range(n)]
 for u,v in edges:a[u].add(v);a[v].add(u)
 return a

def wins(a,k=1):
 n=len(a); cops=list(product(range(n),repeat=k))
 states=list(product(cops,range(n),range(2)))
 won={s for s in states if s[1] in s[0]}
 while True:
  new=set()
  for c,r,t in states:
   if (c,r,t) in won:continue
   if t==0 and any((cc,r,1) in won for cc in product(*(a[x] for x in c))):new.add((c,r,t))
   if t==1 and all((c,rr,0) in won for rr in a[r]):new.add((c,r,t))
  if not new:break
  won|=new
 return any(all((c,r,0) in won for r in range(n)) for c in cops)
def cyc(n):return [(i,(i+1)%n) for i in range(n)]
for n in (5,7):assert wins(graph(n,[(i,i+1) for i in range(n-1)]))
for n in (3,4,5,6,8):assert wins(graph(n,cyc(n)))==(n==3)
for n in (6,8):assert wins(graph(n,cyc(n)),2)
assert wins(graph(7,[(0,1),(1,2),(2,3),(3,4),(2,5),(5,6)]))
assert wins(graph(8,[(0,1),(1,2),(2,3),(3,4),(2,5),(5,6),(5,7)]))
assert wins(graph(4,cyc(4)+[(0,2)]))
for u in range(5):
 for v in range(u+1,5):
  if (u-v)%5 not in (1,4):assert not wins(graph(5,cyc(5)+[(u,v)]))
assert wins(graph(5,cyc(5)+[(0,2),(0,3)]))
f1=graph(6,[(0,1),(1,2),(2,0),(2,3),(3,4),(0,5)])
f2=graph(5,cyc(5)+[(0,2)])
assert wins(f1) and not wins(f2)
def fold(a,seq):
 a={i:set(n) for i,n in enumerate(a)}
 for v,u in seq:
  assert a[v]<=a[u],(v,u,a)
  del a[v]
  for ns in a.values():ns.discard(v)
 return a
assert len(fold(f1,[(4,3),(3,2),(5,0),(0,1),(1,2)]))==1
r=fold(f2,[(1,0)])
assert all(not(ns<=r[u]) for v,ns in r.items() for u in ns if u!=v)
print('PASS: paths, both trees, C3/C4/C5/C6/C8, road-edit minima, F1/F2 folds, two-cop C6/C8.')

# Exact finite-horizon check for the revised common-start Q6 investigation.
def common_start_turns(a):
 n=len(a); cs=list(product(range(n),repeat=2)); states=list(product(cs,range(n)))
 moves={c:list(product(*(a[x] for x in c))) for c in cs}
 wc={s for s in states if s[1] in s[0]}; wr=set(wc)
 for h in range(1,30):
  wc|={s for s in states if any((d,s[1]) in wr for d in moves[s[0]])}
  wr|={s for s in states if all((s[0],r) in wc for r in a[s[1]])}
  if all(((0,0),r) in wc for r in range(n)):return h
 raise AssertionError('No common-start bound found')
assert common_start_turns(graph(6,cyc(6)))==3
print('PASS: Q6 with both cops at a has optimal guarantee of 3 cop turns.')
