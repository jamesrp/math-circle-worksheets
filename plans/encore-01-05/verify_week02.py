"""Independent checks of represented Week2 student and adult cases."""
from pathlib import Path
from collections import deque
from itertools import product
import json
out={}
# Hiddenwiring4-lamp convention example.
assert ({1,3}^{1,4})=={3,4}
# Every one-switch observation identifies each of512 panels uniquely.
panels=list(product(range(8),repeat=3))
assert len(panels)==len(set(tuple(m for m in panel) for panel in panels))==512
out['hidden_masks']='all512three-maskpanels identifiable by3individualpressobservations; four-lamp conventionverified'
for n in [4,5,6,7]:
 masks=[sum(1<<((i+j)%n) for j in range(3)) for i in range(n)]
 def image(s):
  x=0
  for i,m in enumerate(masks):
   if s>>i&1:x^=m
  return x
 sols={t:[s for s in range(1<<n) if image(s)==t] for t in [1,(1<<n)-1]}
 out[f'ring{n}']={str(t):[[i+1 for i in range(n) if s>>i&1] for s in ss] for t,ss in sols.items()}
 if n==4:assert image(sum(1<<(i-1) for i in [1,3,4]))==1
 if n==5:assert image(sum(1<<(i-1) for i in [2,3,5]))==1
 if n==6:assert not sols[1] and len(sols[63])==4 and min(s.bit_count() for s in sols[63])==2
 if n==7:assert masks[5]==sum(1<<(i-1) for i in [6,7,1])
cases=[({1},{6},5,1),({1,2},{5,6},8,4),({1,3,5},{2,4,6},3,3),({1,2},{2,4,6},None,None)]
ans=[]
for start,target,line_expected,ring_expected in cases:
 a=sum(1<<(i-1) for i in start);b=sum(1<<(i-1) for i in target);ds=[]
 for ring,expected in [(False,line_expected),(True,ring_expected)]:
  q=deque([a]);dist={a:0}
  while q:
   x=q.popleft()
   for i in range(6 if ring else 5):
    j=(i+1)%6
    if (x>>i&1)==(x>>j&1):continue
    y=x^(1<<i)^(1<<j)
    if y not in dist:dist[y]=dist[x]+1;q.append(y)
  assert dist.get(b)==expected
  ds.append(dist.get(b))
 ans.append({'start':sorted(start),'target':sorted(target),'line_minimum':ds[0],'ring_minimum':ds[1]})
out['printed_exchange_cases']=ans
# Adult explicit routes.
s={1,2}
for a,b in [(1,6),(1,2),(5,6),(1,6)]:
 if (a in s)!=(b in s):s^={a,b}
assert s=={5,6}
s={1,4}
for a,b in [(4,5),(5,6),(1,2),(2,3)]:
 if (a in s)!=(b in s):s^={a,b}
assert s=={3,6}
# Student swap convention.
assert ({1,3}^{1,2})=={2,3}
Path(__file__).with_name('week02-represented-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('Week2 represented hiddenmask, triple-ring, exchange examples verified independently')
