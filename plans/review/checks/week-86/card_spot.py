import itertools
INF=10**9
def solve(V,E):
    N={v:{v} for v in V}
    for a,b in E: N[a].add(b); N[b].add(a)
    # f[c][r] = cop turns to guarantee capture, cop to move, c!=r
    f={(c,r):INF for c in V for r in V if c!=r}
    for k in range(1,60):
        new=dict(f)
        for (c,r),val in f.items():
            if val<INF: continue
            best=INF
            for c2 in N[c]:
                if c2==r: best=1;break
                # robber replies
                worst=0
                for r2 in N[r]:
                    if r2==c2: continue
                    worst=max(worst,f[(c2,r2)]+1)
                if worst<best: best=worst
            if best<=k: new[(c,r)]=best
        if new==f: break
        f=new
    starts={c:max(f[(c,r)] for r in V if r!=c) for c in V}
    return starts
def path(n): V=list(range(n)); return V,[(i,i+1) for i in range(n-1)]
def ring(n,extra=()): V=list(range(n)); return V,[(i,(i+1)%n) for i in range(n)]+list(extra)
print('P5',solve(*path(5)))
print('P7',solve(*path(7)))
T1=(list('abcdefg'),[('a','b'),('b','c'),('c','d'),('d','e'),('c','f'),('f','g')])
T2=(list('abcdefgh'),[('a','b'),('b','c'),('c','d'),('d','e'),('c','f'),('f','g'),('f','h')])
print('T1',solve(*T1)); print('T2',solve(*T2))
for n in (3,4,5,6): print('R',n,min(solve(*ring(n)).values()))
# E5 two chords
ch=[(0,2),(0,3),(1,3),(1,4),(2,4)]
for p in itertools.combinations(ch,2):
    print('E5',p,min(solve(*ring(5,p)).values()))
for c in ch: print('E5 one',c,min(solve(*ring(5,[c])).values()))
