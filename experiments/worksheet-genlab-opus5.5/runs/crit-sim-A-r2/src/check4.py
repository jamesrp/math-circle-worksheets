from tri import *
from collections import deque
H = region_from_poly(hexagon_poly(2,2,2))
T = [frozenset(t) for t in all_tilings(H)]
words = [tuple(w for w,_ in chains(t,H)) for t in T]
idx={t:i for i,t in enumerate(T)}
adj={i:set(idx[s] for s in flip_neighbors(t,H)) for i,t in enumerate(T)}
def inv(w): return sum(1 for i in range(len(w)) for j in range(i+1,len(w)) if w[i]=='R' and w[j]=='L')
def bfs(s):
    d={s:0};q=deque([s])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if y not in d: d[y]=d[x]+1;q.append(y)
    return d
for i in range(20):
    d=bfs(i)
    for j in range(i+1,20):
        Ii=sum(inv(w) for w in words[i]); Ij=sum(inv(w) for w in words[j])
        if Ii==Ij and d[j]>=4: print(words[i],words[j],Ii,d[j])
# 12-cell shape check
sh = region_from_poly(triangle_poly(3)) | {('D',2,0),('U',3,0),('U',2,1)}
print(len(sh), counts(sh), 'greens', len(sh)-2*len(max_matching(sh)))
