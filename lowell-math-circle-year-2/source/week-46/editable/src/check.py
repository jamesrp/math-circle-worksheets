from itertools import product
from collections import Counter
boards=list(product('RB',repeat=3))
ops=list(product(range(3),'RB'))
def apply(board,story):
 a=list(board)
 for pos,color in story:
  a[pos]=('B' if a[pos]=='R' else 'R') if color=='T' else color
 return tuple(a)
for n in range(5):
 for story in product(ops,repeat=n):
  visited={p for p,c in story};ends={apply(b,story) for b in boards}
  assert len(ends)==2**(3-len(visited))
  for a,b in zip(boards,reversed(boards)):
   aa,bb=apply(a,story),apply(b,story)
   assert all(aa[i]==bb[i] for i in visited)
for story in product(ops+[(i,'T') for i in range(3)],repeat=4):
 reset={p for p,c in story if c!='T'}
 assert len({apply(b,story) for b in boards})==2**(3-len(reset))
for a in boards:
 for b in boards:
  d=sum(x!=y for x,y in zip(a,b))
  for n in range(d):assert not any(apply(a,h)==apply(b,h) for h in product(ops,repeat=n))
  assert any(apply(a,h)==apply(b,h) for h in product(ops,repeat=d))
for start in boards:
 counts=Counter(apply(start,list(zip([0,2,0,1],colors))) for colors in product('RB',repeat=4))
 assert len(counts)==8 and set(counts.values())=={2}
print('Checked all overwrite histories through length four, mixed reset/toggle histories, minimum coupling distances, and conditional uniformity.')
