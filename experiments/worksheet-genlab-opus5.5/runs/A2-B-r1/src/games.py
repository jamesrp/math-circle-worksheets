from functools import lru_cache
def labels(moves, N):
    L = []
    for n in range(N+1):
        win = any(n-m >= 0 and not L[n-m] for m in moves)
        L.append(win)
    return L  # True = player to move wins
def grundy(moves, N):
    g=[]
    for n in range(N+1):
        s={g[n-m] for m in moves if n-m>=0}
        k=0
        while k in s: k+=1
        g.append(k)
    return g
rules=[(1,2),(1,2,3),(1,3),(1,3,4),(1,3,5),(1,4),(1,2,4),(1,4,5),(1,2,5),(1,2,3,4),(1,2,3,5),(1,4,6),(1,5,6),(1,3,6),(1,2,6),(1,5),(1,6),(1,4,7),(1,2,7),(1,3,7),(1,5,7),(1,6,7)]
for r in rules:
    L=labels(r,60)
    losing=[n for n in range(1,61) if not L[n]]
    print(r, "losing:", losing[:16])
    print("   grundy:", grundy(r,30))
