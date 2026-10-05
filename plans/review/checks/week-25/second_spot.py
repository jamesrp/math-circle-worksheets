# Independent spot check of week 25 answers (second reviewer).
from itertools import product
def pics(rows, cols):
    R, C = len(rows), len(cols)
    out = []
    for bits in product([0,1], repeat=R*C):
        g = [bits[r*C:(r+1)*C] for r in range(R)]
        if [sum(x) for x in g]==list(rows) and [sum(g[r][c] for r in range(R)) for c in range(C)]==list(cols):
            out.append(tuple(map(tuple,g)))
    return out
def s(g): return "/".join("".join(map(str,r)) for r in g)
cases = {
 "K1 P1a": ((1,1),(1,1)), "K1 P1b": ((1,1),(1,0,1)), "K1 P1c": ((2,1),(1,1,1)),
 "K1 P2L": ((1,2),(1,1,1)), "K1 P2R": ((2,1),(1,1,1)), "K1 P3": ((1,1,1),(1,1,1)),
 "K1 P4 p5": ((3,1),(2,1,1)), "K1 P4 p6 top": ((2,1,0),(2,1,0)), "K1 P4 p6 bot": ((2,1,1),(2,1,1)),
 "23 P1a": ((2,1),(1,1,1)), "23 P1b": ((3,1),(2,1,1)), "23 P1c": ((2,2),(2,1,1)),
 "23 P2": ((2,1,1),(2,1,1)), "45 P1": ((2,2),(1,1,1,1)), "45 P4": ((3,3),(2,1,0,1,1,1)),
 "launch": ((2,1),(1,1,1)),
}
for k,(r,c) in cases.items():
    p = pics(r,c); print(k, len(p), [s(x) for x in p][:6])
# switch distance BFS
def switches(g):
    R, C = len(g), len(g[0]); res=[]
    for a in range(R):
        for b in range(a+1,R):
            for c in range(C):
                for d in range(C):
                    if c!=d and g[a][c]==1 and g[b][d]==1 and g[a][d]==0 and g[b][c]==0:
                        h=[list(x) for x in g]; h[a][c]=0;h[b][d]=0;h[a][d]=1;h[b][c]=1
                        res.append(tuple(map(tuple,h)))
    return res
def dist(a,b):
    from collections import deque
    seen={a:0}; q=deque([a])
    while q:
        x=q.popleft()
        if x==b: return seen[x]
        for y in switches(x):
            if y not in seen: seen[y]=seen[x]+1; q.append(y)
P=lambda t: tuple(tuple(int(ch) for ch in row) for row in t.split("/"))
print("23 P4 1100/0011->0011/1100", dist(P("1100/0011"),P("0011/1100")))
print("45 P3", dist(P("111000/000111"),P("000111/111000")))
print("45 P4", dist(P("110100/100011"),P("100011/110100")))
# Lower bound check: D = |occupied in start, empty in target| ; each switch lowers D by at most 2
import itertools
bad=0;tot=0
for R,C in [(2,4),(3,3),(2,5),(3,4)]:
    from collections import defaultdict
    groups=defaultdict(list)
    for bits in product([0,1],repeat=R*C):
        g=tuple(tuple(bits[r*C:(r+1)*C]) for r in range(R))
        key=(tuple(map(sum,g)),tuple(sum(g[r][c] for r in range(R)) for c in range(C)))
        groups[key].append(g)
    for key,gs in groups.items():
        for a in gs:
            for b in gs:
                D=sum(1 for r in range(R) for c in range(C) if a[r][c]==1 and b[r][c]==0)
                tot+=1
                if (D+1)//2 > dist(a,b): bad+=1
print("halved-vacated-cells lower bound violations:", bad, "of", tot)
