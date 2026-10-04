import sys
sys.path.insert(0,'/home/claude/genlab/runs/A1-B-r1/src')
S=(1,3,4)
N=60
L=[]
for n in range(N+1):
    L.append(not any(n-m>=0 and L[n-m] for m in S))
# greedy player G to move at n (G always takes max allowed); opponent optimal
from functools import lru_cache
@lru_cache(None)
def gwins(n, gturn):
    if n==0:
        return not gturn  # previous mover took last; if it's G's turn, opponent took last
    moves=[m for m in S if m<=n]
    if gturn:
        return gwins(n-max(moves), False)
    else:
        return all(gwins(n-m, True) for m in moves)
print('greedy first wins from:', [n for n in range(1,N) if gwins(n,True)])
print('W piles:', [n for n in range(1,N) if not L[n]])
print('take-4 winning:', [n for n in range(4,N) if L[n-4]])
# two-pile checks
g=[]
for n in range(30):
    o={g[n-m] for m in S if n-m>=0}; v=0
    while v in o: v+=1
    g.append(v)
@lru_cache(None)
def win2(a,b):
    for m in S:
        if a>=m and not win2(a-m,b): return True
        if b>=m and not win2(a,b-m): return True
    return False
for a,b in [(6,4),(5,1),(12,5),(11,3),(5,5),(7,2),(6,1),(9,8),(9,7)]:
    mv=[(a-m,b) for m in S if a>=m and not win2(a-m,b)]+[(a,b-m) for m in S if b>=m and not win2(a,b-m)]
    print((a,b), 'mover wins' if win2(a,b) else 'mover loses', g[a]^g[b], 'winning moves->', mv)
# K-1 two piles with {1,2}
S2=(1,2)
@lru_cache(None)
def w12(a,b):
    return any((a>=m and not w12(a-m,b)) or (b>=m and not w12(a,b-m)) for m in S2)
for a,b in [(2,2),(2,1),(5,5),(4,1),(3,1)]:
    print('K1',(a,b),'first wins' if w12(a,b) else 'second wins')
