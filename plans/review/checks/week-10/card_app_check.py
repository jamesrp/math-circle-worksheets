import json, sys, itertools
from collections import Counter
from functools import lru_cache
d=json.load(open(sys.argv[1]))
ps=[p for p in d['puzzles'] if str(p.get('id','')).startswith('route-')]
def starts_ends(V,E):
    n=len(E)
    res=set()
    @lru_cache(None)
    def ends(v,mask):
        if mask==(1<<n)-1: return frozenset([v])
        out=set()
        for i,(a,b,w) in enumerate(E):
            if mask>>i&1: continue
            if a==v: out|=ends(b,mask|1<<i)
            elif b==v: out|=ends(a,mask|1<<i)
        return frozenset(out)
    for s in V:
        for e in ends(s,0): res.add((s,e))
    return res
def dist(V,E):
    INF=float('inf'); D={(a,b):(0 if a==b else INF) for a in V for b in V}
    for a,b,w in E:
        D[a,b]=min(D[a,b],w); D[b,a]=min(D[b,a],w)
    for k in V:
        for i in V:
            for j in V:
                if D[i,k]+D[k,j]<D[i,j]: D[i,j]=D[i,k]+D[k,j]
    return D
def minmatch(odd,D):
    if not odd: return 0
    a=odd[0]; best=float('inf')
    for i in range(1,len(odd)):
        b=odd[i]; rest=odd[1:i]+odd[i+1:]
        best=min(best,D[a,b]+minmatch(rest,D))
    return best
for p in ps:
    q=p['parameters']; V=q['vertices']; E=[tuple(e) for e in q['edges']]
    deg=Counter()
    for a,b,w in E: deg[a]+=1; deg[b]+=1
    odd=[v for v in V if deg[v]%2]
    if q['mode']=='each_edge_once':
        se=starts_ends(V,E)
        st=sorted(set(s for s,e in se))
        ok = (q['start'] is None or any(s==q['start'] and (not q['closed'] or e==s) for s,e in se))
        print(p['id'],'exact-once: valid starts',st,'closed?',all(s==e for s,e in se),'| instance satisfiable:',ok, '| odd',odd)
    else:
        D=dist(V,E); base=sum(w for a,b,w in E)
        opt=base+minmatch(odd,D)
        print(p['id'],'postman: optimum',opt,'target',q['target_cost'],'match' if opt==q['target_cost'] else 'MISMATCH','| odd',odd)
