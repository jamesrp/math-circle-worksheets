# Check: moving exactly two counters (two cells emptied, two filled) while keeping every count is always a switch.
from itertools import product
def m(g,R,C): return (tuple(sum(g[r][c] for c in range(C)) for r in range(R)), tuple(sum(g[r][c] for r in range(R)) for c in range(C)))
bad=0; tot=0
for R,C in [(2,3),(2,4),(3,3),(3,4)]:
    for bits in product([0,1],repeat=R*C):
        g=[list(bits[r*C:(r+1)*C]) for r in range(R)]
        mg=m(g,R,C)
        for bits2 in product([0,1],repeat=R*C):
            h=[list(bits2[r*C:(r+1)*C]) for r in range(R)]
            V=[(r,c) for r in range(R) for c in range(C) if g[r][c]==1 and h[r][c]==0]
            F=[(r,c) for r in range(R) for c in range(C) if g[r][c]==0 and h[r][c]==1]
            if len(V)==2 and len(F)==2 and m(h,R,C)==mg:
                tot+=1
                rows={V[0][0],V[1][0]}; cols={V[0][1],V[1][1]}
                ok = len(rows)==2 and len(cols)==2 and set(F)=={(r,c) for r in rows for c in cols}-set(V)
                if not ok: bad+=1
    print(R,C,"done")
print("two-counter count-preserving moves:",tot,"non-switch:",bad)
