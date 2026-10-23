"""Check the printed tree family and all shortest diagonal paths up to n=6."""
from itertools import combinations
from collections import deque

def distance(a,b):return abs(a[0]-b[0])+abs(a[1]-b[1])
def gap(triangle):
    return max(min(distance(p,q) for j,side in enumerate(triangle) if j!=i for q in side) for i,side in enumerate(triangle) for p in side)
for n in range(1,7):
    ab={(x,0) for x in range(n+1)};bc={(n,y) for y in range(n+1)}
    got=[]
    for right in combinations(range(2*n),n):
        right=set(right);p=(0,0);ac={p}
        for step in range(2*n):
            p=(p[0]+1,p[1]) if step in right else (p[0],p[1]+1);ac.add(p)
        got.append(gap([ab,bc,ac]))
    assert min(got)==0 and max(got)==n
    fat={(0,y) for y in range(n+1)}|{(x,n) for x in range(n+1)}
    assert gap([ab,bc,fat])==n
    assert min(distance((0,n),q) for q in ab|bc)==n
    print('n=',n,':',len(got),'shortest diagonal paths; gap range',min(got),max(got))
for edges in [
 [('a','b'),('b','c'),('c','d'),('d','e'),('d','f'),('c','g'),('g','h'),('h','k'),('b','i'),('i','j'),('a','l')],
 [('a','b'),('b','c'),('c','d'),('d','e'),('b','f'),('f','g'),('f','h'),('d','i'),('i','j'),('i','k')]]:
    vs=sorted(set(sum(([a,b] for a,b in edges),[])));adj={v:[] for v in vs}
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    def route(a,b):
        q=deque([a]);prev={a:None}
        while b not in prev:
            v=q.popleft()
            for w in adj[v]:
                if w not in prev:prev[w]=v;q.append(w)
        path=[b]
        while path[-1]!=a:path.append(prev[path[-1]])
        return {frozenset((x,y)) for x,y in zip(path,path[1:])}
    for triple in combinations(vs,3):
        sides=[route(a,b) for a,b in combinations(triple,2)]
        assert all(sum(edge in side for side in sides)==2 for edge in set().union(*sides))
    print('PASS: all triples on',len(vs),'vertex printed tree have every used edge in exactly two sides.')
print('General argument: n-by-n corner family has a gap n measured in the full grid. Tree uniqueness of simple paths forces every triangle to be a tripod, including degenerate tripods. Finite experiments alone do not establish either universal statement.')
