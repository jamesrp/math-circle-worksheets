# Painter/Spoiler coloring game solver and chromatic numbers for the maps used.
from functools import lru_cache
import itertools

def solve(adj, k, painter_first):
    n=len(adj)
    @lru_cache(None)
    def win(state, painter_turn):
        # state: tuple of colors (-1 uncolored). return True if Painter wins
        unc=[v for v in range(n) if state[v]<0]
        if not unc: return True
        for v in unc:
            used={state[u] for u in adj[v] if state[u]>=0}
            if len(used)>=k: return False
        moves=[]
        for v in unc:
            used={state[u] for u in adj[v] if state[u]>=0}
            for c in range(k):
                if c not in used:
                    s=list(state); s[v]=c; moves.append(tuple(s))
        res=[win(m, not painter_turn) for m in moves]
        return any(res) if painter_turn else all(res)
    return win(tuple([-1]*n), painter_first)

def chrom(adj):
    n=len(adj)
    for k in range(1,n+1):
        for col in itertools.product(range(k),repeat=n):
            if all(col[u]!=col[v] for u in range(n) for v in adj[u]): return k

def path(n): return [[j for j in (i-1,i+1) if 0<=j<n] for i in range(n)]
def ring(n): return [[(i-1)%n,(i+1)%n] for i in range(n)]
def wheel(n): # 0 = middle, 1..n ring
    a=[list(range(1,n+1))]
    for i in range(n): a.append([0, 1+(i-1)%n, 1+(i+1)%n])
    return a
def grid(r,c,torus=False):
    a=[]
    for i in range(r):
        for j in range(c):
            nb=set()
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ii,jj=i+di,j+dj
                if torus: ii%=r; jj%=c
                if 0<=ii<r and 0<=jj<c and (ii,jj)!=(i,j): nb.add(ii*c+jj)
            a.append(sorted(nb))
    return a

def report(name, adj, ks):
    print(name, "chi=",chrom(adj))
    for k in ks:
        print("   k=%d  Painter first: %s   Spoiler first: %s"%(k,
          "Painter" if solve(adj,k,True) else "Spoiler",
          "Painter" if solve(adj,k,False) else "Spoiler"))

if __name__=="__main__":
    for n in (3,4,5): report("strip %d"%n, path(n), [2])
    for n in (3,4,5,6): report("ring %d"%n, ring(n), [2,3])
    report("3x3 grid", grid(3,3), [3,4])
    for n in (3,4,5,6,7): report("wheel %d"%n, wheel(n), [3,4])
    for (r,c) in ((1,3),(1,4),(1,5),(2,2),(3,3),(4,4)):
        print("torus grid",r,c,"chi=",chrom(grid(r,c,True)))
