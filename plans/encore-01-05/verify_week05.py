"""Independent checks of Week 5 represented cities (standard library)."""
from collections import Counter
from itertools import combinations,permutations
from pathlib import Path
import json

def latin(g):
    n=len(g);want=set(range(1,n+1))
    return all(set(r)==want for r in g) and all({g[i][j] for i in range(n)}==want for j in range(n))
def diag(g):
    n=len(g);return len({g[i][i] for i in range(n)})==n and len({g[i][n-1-i] for i in range(n)})==n
def peaks(g):
    n=len(g)
    return [(i,j) for i in range(n) for j in range(n) if all(g[a][b]<g[i][j] for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if 0<=a<n and 0<=b<n)]
def trades(g):
    n=len(g)
    return [(a,b,c,d) for a,b in combinations(range(n),2) for c,d in combinations(range(n),2) if g[a][c]==g[b][d] and g[a][d]==g[b][c]]
def cities(n):
    def rec(rows):
        if len(rows)==n:yield tuple(rows);return
        for row in permutations(range(1,n+1)):
            if all(row[j] not in [r[j] for r in rows] for j in range(n)):yield from rec(rows+[row])
    yield from rec([])

trade=((1,2,3,4),(2,1,4,3),(3,4,1,2),(4,3,2,1))
fixed=((2,1,3,4),(1,2,4,3),(3,4,1,2),(4,3,2,1))
diagonal=((1,2,3,4),(3,4,1,2),(4,3,2,1),(2,1,4,3))
assert latin(trade) and latin(fixed) and (0,1,0,1) in trades(trade)
assert latin(diagonal) and diag(diagonal)
peakcases=[(((1,2,3),(3,1,2),(2,3,1)),3),(((1,2,3),(2,3,1),(3,1,2)),4),(trade,4),(((1,3,2,4),(3,1,4,2),(2,4,1,3),(4,2,3,1)),8)]
for g,k in peakcases:assert latin(g) and len(peaks(g))==k
out={}
for n in [3,4]:
    gs=list(cities(n));ds=sum(diag(g) for g in gs)
    th=Counter(len(trades(g)) for g in gs);ph=Counter(len(peaks(g)) for g in gs)
    assert len(gs)=={3:12,4:576}[n] and ds=={3:0,4:48}[n]
    assert dict(th)==({0:12} if n==3 else {4:432,12:144})
    assert dict(ph)==({3:8,4:4} if n==3 else {4:226,5:136,6:172,7:8,8:34})
    out[str(n)]={'cities':len(gs),'both_diagonal':ds,'trade_histogram':dict(th),'peak_histogram':dict(ph)}

# Actual printed cities and non-task conventions.
a=((1,2,3,4),(2,3,4,1),(3,4,1,2),(4,1,2,3))
b=trade;c=((1,2,3),(2,3,1),(3,1,2))
assert all(latin(g) for g in [a,b,c])
assert [len(trades(g)) for g in [a,b,c]]==[4,12,0]
assert set(trades(a))=={(r,r+2,k,k+2) for r in [0,1] for k in [0,1]}
d=((1,2,3),(3,1,2),(2,3,1));e=c
assert peaks(d)==[(0,2),(1,0),(2,1)]
assert peaks(e)==[(0,2),(1,1),(2,0),(2,2)]
assert 3>1 and abs(1-0)==1  # side-neighbor roof move on 1,3,2 strip
demo=((2,1),(1,2))
assert [demo[i][i] for i in range(2)]==[2,2]
assert [demo[i][1-i] for i in range(2)]==[1,1]

Path(__file__).with_name('week05-represented-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('Week 5 Latin trade, diagonal, and climbing examples independently verified')
