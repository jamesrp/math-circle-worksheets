#!/usr/bin/env python3
"""Exhaustive shortest edge-covering walks in tiny graphs, independent of pairing formula."""
from heapq import heappush,heappop
from collections import Counter
E=[('A','B'),('B','C'),('C','A'),('A','D'),('B','D'),('C','D')]
H=[('A','B'),('B','C'),('C','D'),('D','A'),('D','E'),('E','C')]
def route_cost(route,edges,weights):
 counts=Counter(tuple(sorted(e)) for e in zip(route,route[1:]));need=Counter(tuple(sorted(e)) for e in edges)
 assert all(counts[e]>=n for e,n in need.items())
 lookup={tuple(sorted(e)):w for e,w in zip(edges,weights)}
 return sum(lookup[e]*n for e,n in counts.items())
def shortest(edges,weights,closed=True,start='A'):
 adj={v:[] for e in edges for v in e}
 for i,((u,v),w) in enumerate(zip(edges,weights)):
  adj[u].append((v,i,w));adj[v].append((u,i,w))
 q=[(0,start,0,start)];seen={}
 while q:
  cost,u,mask,path=heappop(q)
  if (u,mask) in seen:continue
  seen[u,mask]=cost
  if mask==(1<<len(edges))-1 and (not closed or u==start):return cost,path
  for v,i,w in adj[u]:heappush(q,(cost+w,v,mask|(1<<i),path+v))
assert route_cost('DABCDE C'.replace(' ',''),H,[1]*6)==6
two_triangles=[('A','B'),('B','C'),('C','A'),('A','D'),('D','E'),('E','A')]
assert route_cost('ADEABCA',two_triangles,[1]*6)==6
assert shortest(E,[1]*6)[0]==8
assert shortest(E,[1]*6,False)[0]==7
assert route_cost('ABCADCDB',E,[1]*6)==7
assert route_cost('CABDABCD',E+[('A','B')],[1]*7)==7
prism=[('A','B'),('B','C'),('C','A'),('D','E'),('E','F'),('F','D'),('A','D'),('B','E'),('C','F')]
assert route_cost('ABCADEBEFCFDA',prism,[1]*9)==12
assert shortest(prism,[1]*9)[0]==12
assert route_cost('ABCDACDBA',E,[1]*6)==8
weights=[2,3,7,1,6,1]
assert sum(weights)==20
assert shortest(E,weights)[0]==23
assert route_cost('ABCDACDBA',E,weights)==23
print('House trail: D-A-B-C-D-E-C')
print('Unit K4 closed/open optimum:',shortest(E,[1]*6),shortest(E,[1]*6,False))
print('Weighted K4 optimum:',shortest(E,weights))
print('PASS: independent shortest-walk search verifies all postman bounds and explicit routes.')
