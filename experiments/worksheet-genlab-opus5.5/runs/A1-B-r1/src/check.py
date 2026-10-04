def labels(S, N):
    L = []
    for n in range(N+1):
        L.append(not any(n-m >= 0 and L[n-m] for m in S))  # True = losing
    return L
def grundy(S, N):
    g = []
    for n in range(N+1):
        opts = {g[n-m] for m in S if n-m >= 0}
        v = 0
        while v in opts: v += 1
        g.append(v)
    return g
def show(S, N=40):
    L = labels(S, N)
    print(S, 'L piles:', [n for n in range(N+1) if L[n]])
for S in [(1,2),(1,3,4),(1,3,5),(1,2,3),(1,4),(1,2,4),(1,2,5),(1,2,6),(1,2,9),(1,3),(1,5),(1,4,6),(1,2,7)]:
    show(S)
print('grundy 134', grundy((1,3,4),21))
print('grundy 12', grundy((1,2),12))
# period / preperiod finder
def period(S, N=400):
    L = labels(S, N)
    for pre in range(0, 150):
        for p in range(1, 60):
            if all(L[i]==L[i+p] for i in range(pre, N-p)):
                return pre, p
    return None
import itertools
res=[]
for k in (2,3):
    for S in itertools.combinations(range(1,10),k):
        if 1 not in S: continue
        pp = period(S)
        res.append((pp[0], pp[1], S))
res.sort(reverse=True)
print(res[:25])
print()
for S in [(1,6,9),(1,2,9),(1,2,12)]:
    show(S, 45); print(period(S))
res=[]
for k in (2,3,4):
    for S in itertools.combinations(range(1,13),k):
        if 1 not in S: continue
        pp = period(S)
        if pp[0]>0: res.append((pp[0], pp[1], S))
res.sort()
print(res[:30])
