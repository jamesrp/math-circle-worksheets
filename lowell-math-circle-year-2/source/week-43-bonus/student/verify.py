#!/usr/bin/env python3
from itertools import permutations,product
from collections import Counter,deque
import json
labeled=list(permutations(['A1','A2','B1','B2']))
pictures=Counter(''.join(s[0] for s in row) for row in labeled)
assert len(labeled)==24 and len(pictures)==6 and set(pictures.values())=={4}
def cut(s,k):return s[k:]+s[:k]
def closure(reverse=False):
 seen={'ABCD'};q=deque(seen)
 while q:
  s=q.popleft();news=[cut(s,k) for k in range(4)]+([s[::-1]] if reverse else [])
  for t in news:
   if t not in seen:seen.add(t);q.append(t)
 return seen
cuts=closure();both=closure(True)
assert len(cuts)==4 and len(both)==8 and 'ABDC' not in cuts and 'ABDC' not in both
assert Counter(s[0] for s in cuts)==dict.fromkeys('ABCD',1)
assert cut('WXYZ',2)=='YZWX'
orders=Counter();stories={}
for row in permutations('ABC'):
 for gap in range(4):
  final=''.join(row[:gap])+ 'D' + ''.join(row[gap:]);orders[final]+=1;stories[final]=(''.join(row),gap+1)
assert len(orders)==24 and set(orders.values())=={1}
assert 'X'+'Z'+'Y'=='XZY'
print(json.dumps({'labeled_orders':len(labeled),'picture_counts':pictures,'cut_only':sorted(cuts),'cut_and_reverse':sorted(both),'insertion_histories':len(orders),'target_stories':{s:stories[s] for s in ['ABCD','DACB','BDCA','CBAD']}},indent=2))
