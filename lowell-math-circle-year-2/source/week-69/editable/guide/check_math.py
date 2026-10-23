#!/usr/bin/env python3
"""Independent guide checker for printed tree graphs and grid triangles."""
from collections import deque, Counter
from itertools import combinations, product
from math import comb
import json

def graph(names,edges):
    g={a:set() for a in names}
    for a,b in edges:g[a].add(b);g[b].add(a)
    return g

def path(g,a,b):
    parents={a:None};q=deque([a])
    while b not in parents:
        u=q.popleft()
        for v in g[u]:
            if v not in parents:parents[v]=u;q.append(v)
    route=[b]
    while route[-1]!=a:route.append(parents[route[-1]])
    return route[::-1]

trees=[
 graph('abcdefghijkl',[('a','b'),('b','c'),('c','d'),('d','e'),('d','f'),('c','g'),('g','h'),('h','k'),('b','i'),('i','j'),('a','l')]),
 graph('abcdefghijk',[('a','b'),('b','c'),('c','d'),('d','e'),('b','f'),('f','g'),('f','h'),('d','i'),('i','j'),('i','k')])]
tree_triples=0
for g in trees:
    assert len(g)-1==sum(len(v) for v in g.values())//2
    for homes in combinations(g,3):
        routes=[path(g,a,b) for a,b in combinations(homes,2)]
        counts=Counter(frozenset((a,b)) for route in routes for a,b in zip(route,route[1:]))
        assert set(counts.values())=={2}
        for i,s in enumerate(routes):assert set(s)<=set().union(*(set(t) for j,t in enumerate(routes) if i!=j))
        tree_triples+=1
assert tree_triples==385

def gap(sides):
    # Grid graph distance, including uncolored interior roads.
    return max(min(abs(x-u)+abs(y-v) for j,t in enumerate(sides) if j!=i for u,v in t)
               for i,s in enumerate(sides) for x,y in s)

def routes(n):
    for right_slots in combinations(range(2*n),n):
        right_slots=set(right_slots);x=y=0;route=[(0,0)]
        for k in range(2*n):
            if k in right_slots:x+=1
            else:y+=1
            route.append((x,y))
        yield route

results={}
for n in (2,4,6):
    bottom=[(x,0) for x in range(n+1)]
    right=[(n,y) for y in range(n+1)]
    via_b=bottom+right[1:]
    assert gap([bottom,right,via_b])==0
    left_top=[(0,y) for y in range(n+1)]+[(x,n) for x in range(1,n+1)]
    assert gap([bottom,right,left_top])==n
    values=[gap([bottom,right,r]) for r in routes(n)]
    assert len(values)==comb(2*n,n)
    assert max(values)==n
    results[n]={'routes':len(values),'maximum_gap':max(values)}
assert [results[n]['routes'] for n in (2,4,6)]==[6,70,924]
# Validate the guide's general bound on a wider finite family; proof is separate.
for n in range(1,13):
    bottom=[(x,0) for x in range(n+1)];right=[(n,y) for y in range(n+1)]
    left_top=[(0,y) for y in range(n+1)]+[(x,n) for x in range(1,n+1)]
    assert gap([bottom,right,left_top])==n
print(json.dumps({'status':'PASS','tree_distinct_triples':tree_triples,'grid_results':results,
 'P2':[0,4],'scope':'Finite enumeration verifies printed instances; proofs in the guide establish all trees and arbitrarily large gaps.'},indent=2))
