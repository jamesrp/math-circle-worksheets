from tri import *
from collections import deque
def analyze(abc):
    H = region_from_poly(hexagon_poly(*abc))
    T = [frozenset(t) for t in all_tilings(H)]
    idx = {t:i for i,t in enumerate(T)}
    words = [tuple(w for w,_ in chains(t,H)) for t in T]
    adj = {i:set() for i in range(len(T))}
    for t in T:
        for s in flip_neighbors(t,H):
            adj[idx[t]].add(idx[s])
    # check each flip changes exactly one chain by swapping adjacent pair
    for i in adj:
        for j in adj[i]:
            diffs=[(a,b) for a,b in zip(words[i],words[j]) if a!=b]
            assert len(diffs)==1, (words[i],words[j])
            a,b=diffs[0]
            pos=[k for k in range(len(a)) if a[k]!=b[k]]
            assert len(pos)==2 and pos[1]==pos[0]+1 and a[pos[0]]==b[pos[1]] and a[pos[1]]==b[pos[0]]
    return H,T,words,adj
for abc in [(2,2,1),(2,2,2),(1,3,3)]:
    H,T,words,adj=analyze(abc)
    print(abc,len(T),'edges',sum(len(v) for v in adj.values())//2, 'distinct words',len(set(words)))
    if abc==(2,2,1):
        for i,w in enumerate(words): print(i,w,sorted(adj[i]))
H,T,words,adj=analyze((2,2,2))
def bfs(s):
    d={s:0};q=deque([s])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if y not in d: d[y]=d[x]+1;q.append(y)
    return d
wi={w:i for i,w in enumerate(words)}
for w in sorted(words): print(w, len(adj[wi[w]]))
mn=wi[('LLRR','LLRR')]; mx=wi[('RRLL','RRLL')]
print('dist min-max',bfs(mn)[mx])
diam=max(max(bfs(i).values()) for i in adj); print('diam',diam)
# closed walks without immediate backtracking of length k
def nb_closed(k):
    found=set()
    for s in adj:
        def rec(path):
            if len(path)==k+1:
                if path[-1]==s: found.add(tuple(path))
                return
            for y in adj[path[-1]]:
                if len(path)>=2 and y==path[-2]: continue
                rec(path+[y])
        rec([s])
    return len(found)
for k in range(2,9): print('closed nonbacktracking',k,nb_closed(k))
