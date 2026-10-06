from itertools import combinations,product
from collections import deque

def distances(vertices,adj):
    result={}
    for s in vertices:
        d={s:0};q=deque([s])
        while q:
            v=q.popleft()
            for t in adj[v]:
                if t not in d:d[t]=d[v]+1;q.append(t)
        result[s]=d
    return result

def meetings(triple,vertices,d):
    return {m for m in vertices if all(d[a][m]+d[m][b]==d[a][b] for a,b in combinations(triple,2))}
for dim,size in [(2,5),(3,2)]:
    vs=list(product(range(size),repeat=dim)); adj={v:[w for w in vs if sum(abs(a-b) for a,b in zip(v,w))==1] for v in vs};d=distances(vs,adj)
    for triple in combinations(vs,3):
        med=tuple(sorted(t[i] for t in triple)[1] for i in range(dim))
        assert meetings(triple,vs,d)=={med}
    print('PASS: unique coordinate median for all',len(list(combinations(vs,3))),'triples, dimension',dim)
for n in [3,4]:
    vs=list(range(n));adj={v:[(v-1)%n,(v+1)%n] for v in vs};d=distances(vs,adj)
    assert meetings((0,1,2),vs,d)==(set() if n==3 else {1})
    print('Cycle',n,meetings((0,1,2),vs,d))
edges=[('a','u'),('u','v'),('v','w'),('w','b'),('v','t'),('t','c'),('w','s'),('s','r'),('u','q')]
vs=sorted(set(sum(([a,b] for a,b in edges),[])));adj={v:[] for v in vs}
for a,b in edges:adj[a].append(b);adj[b].append(a)
d=distances(vs,adj);assert meetings(('a','b','c'),vs,d)=={'v'}
print('Tree meeting: v at drawing coordinate (2,0). Cube targets: 100 and 011.')
