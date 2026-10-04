#!/usr/bin/env python3
"""Independent finite checks, not an activity authoring script."""
from itertools import permutations,product,combinations
from collections import Counter,deque
from math import gcd
import json

def latin(n):
 rows=list(permutations(range(1,n+1)))
 out=[]
 def rec(a):
  if len(a)==n:out.append(a);return
  for r in rows:
   if all(r[j] not in [x[j] for x in a] for j in range(n)):rec(a+[r])
 rec([]);return out

def peaks(a):
 n=len(a);out=[]
 for i in range(n):
  for j in range(n):
   if all(a[i][j]>a[x][y] for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if 0<=x<n and 0<=y<n):out.append((i,j))
 return out

def trades(a):
 n=len(a)
 return [(r,s,c,d) for r,s in combinations(range(n),2) for c,d in combinations(range(n),2) if a[r][c]==a[s][d] and a[r][d]==a[s][c]]

out={}
for n in [3,4]:
 ls=latin(n)
 diag=[a for a in ls if len(set(a[i][i] for i in range(n)))==n and len(set(a[i][n-1-i] for i in range(n)))==n]
 mindiff=min(sum(x!=y for ra,rb in zip(a,b) for x,y in zip(ra,rb)) for i,a in enumerate(ls) for b in ls[i+1:])
 out[f'latin{n}']={'minimum_changed_cells':mindiff,'total':len(ls),'both_diagonals':len(diag),'diagonal_example':diag[0] if diag else None,'trade_distribution':dict(Counter(len(trades(a)) for a in ls)),'peak_distribution':dict(Counter(len(peaks(a)) for a in ls)),'peak_examples':{str(k):next(a for a in ls if len(peaks(a))==k) for k in sorted(set(len(peaks(a)) for a in ls))}}
# binary necklace classes
pats=[p for p in product(range(2),repeat=6) if sum(p)==3]
rots=lambda p:[p[i:]+p[:i] for i in range(len(p))]
classes=Counter(min(rots(p)) for p in pats)
out['necklaces6_3']={'rotation_classes':len(classes),'representatives':[(r,c) for r,c in classes.items()],'reflection_classes':len(set(min(rots(p)+rots(p[::-1])) for p in pats))}
# ring3-lamp switch image and kernel enumeration
for n in [4,5,6,7,8,9]:
 masks=[sum(1<<((i+j)%n) for j in range(3)) for i in range(n)]
 images=Counter()
 for s in range(1<<n):
  m=0
  for i,v in enumerate(masks):
   if s>>i&1:m^=v
  images[m]+=1
 out[f'triple_ring{n}']={'reachable':len(images),'do_nothing':images[0],'unique_preimage_counts':sorted(set(images.values()))}
 assert len(images)==2**(n-2 if n%3==0 else n)
# roots independently enumerate permutations; 4-slot targets odd swap vs two swaps
for n in [3,4,6]:
 ps=list(permutations(range(n)))
 roots=Counter(tuple(p[p[i]] for i in range(n)) for p in ps)
 def allowed(q):
  unseen=set(range(n));c=Counter()
  while unseen:
   x=min(unseen);k=0
   while x in unseen:unseen.remove(x);k+=1;x=q[x]
   c[k]+=1
  return all(v%2==0 for k,v in c.items() if k%2==0)
 assert all((q in roots)==allowed(q) for q in ps)
 out[f'roots{n}']={'targets_with_root':len(roots),'total_targets':len(ps)}
# line exchange min distance independently BFS ALL 5 and6 lamp pictures
for n in [5,6]:
 for s in range(1<<n):
  dist={s:0};q=deque([s])
  while q:
   a=q.popleft()
   for i in range(n-1):
    if ((a>>i)&1)!=((a>>(i+1))&1):
     b=a^((1<<i)|(1<<(i+1)))
     if b not in dist:dist[b]=dist[a]+1;q.append(b)
  aa=[i for i in range(n) if s>>i&1]
  for b,d in dist.items():
   bb=[i for i in range(n) if b>>i&1]
   assert d==sum(abs(a-b) for a,b in zip(aa,bb))
# rotate reverse reachable
for n in [4,5,6]:
 s=tuple(range(1,n+1));seen={s};q=deque([s])
 while q:
  p=q.popleft()
  for r in [p[-1:]+p[:-1],p[::-1]]:
   if r not in seen:seen.add(r);q.append(r)
 assert len(seen)==2*n
 out[f'rotate_reverse{n}']={'reachable':len(seen),'orders':sorted(seen)}
# adjacent swap distances exhaust n5
n=5;s=tuple(range(1,n+1));dist={s:0};q=deque([s])
while q:
 p=q.popleft()
 for i in range(n-1):
  r=list(p);r[i],r[i+1]=r[i+1],r[i];r=tuple(r)
  if r not in dist:dist[r]=dist[p]+1;q.append(r)
assert all(d==sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)) for p,d in dist.items())
out['sorting5']={'states':len(dist),'max_distance':max(dist.values())}
# directed two-hop reachability and relative-speed meeting all small examples
for n in range(3,15):
 for a in range(n):
  for b in range(n):
   seen={0};q=deque([0])
   while q:
    x=q.popleft()
    for y in [(x+a)%n,(x+b)%n]:
     if y not in seen:seen.add(y);q.append(y)
   assert len(seen)==n//gcd(n,gcd(a,b))
   for start in range(n):
    actual=any(((a-b)*t)%n==start for t in range(n))
    assert actual==(start%gcd(n,a-b)==0)
out['ring_checks']='all n3..14, all hop pairs and offsets passed'
# Unit regular-hexagon tilings and local corner count mixtures.
hex_tilings=[]
for mask in range(1<<6):
 if any(mask>>i&1 and mask>>((i+1)%6)&1 for i in range(6)):continue
 turns=[t for t in range(6) if sum((mask>>i&1)<<((i+t)%6) for i in range(6))==mask]
 hex_tilings.append({'blue_pair_starts':[i for i in range(6) if mask>>i&1],'matching_turns':turns})
assert len(hex_tilings)==18
out['unit_hex_green_blue']={'tilings':18,'symmetry_order_distribution':dict(Counter(len(t['matching_turns']) for t in hex_tilings)),'tilings_detail':hex_tilings}
out['corner_count_mixtures']=[{'green':g,'blue_acute':a,'blue_obtuse':o} for g in range(7) for a in range(7) for o in range(4) if g+a+2*o==6]
assert len(out['corner_count_mixtures'])==16
Path=__import__('pathlib').Path
Path(str(__import__('pathlib').Path(__file__).with_name('kernel-checks.json'))).write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2)[:5500])
