from collections import deque
def mk(V,E):
    N={v:{v} for v in V}
    for a,b in E: N[a].add(b); N[b].add(a)
    return N
def dist(N,s):
    d={s:0};q=deque([s])
    while q:
        u=q.popleft()
        for w in N[u]:
            if w not in d: d[w]=d[u]+1;q.append(w)
    return d
def check(name,V,E,arms,hub):
    N=mk(V,E); D={v:dist(N,v) for v in V}
    armof={v:i for i,a in enumerate(arms) for v in a}
    found=[]
    # explore all R behaviours vs toward-R cop; state (c,r) cop to move
    for c0 in V:
        for r0 in V:
            if r0==c0: continue
            seen=set();stack=[(c0,r0,armof.get(r0))]
            while stack:
                c,r,arm=stack.pop()
                if (c,r,arm) in seen: continue
                seen.add((c,r,arm))
                # cop step toward r
                c2=min((w for w in N[c] if w!=c), key=lambda w:D[w][r])
                if c2==r: continue
                for r2 in N[r]:
                    if r2==c2 or r2 in N[c2] and False: pass
                    if r2==c2: continue
                    a2=armof.get(r2)
                    if arm is not None and a2 is not None and a2!=arm:
                        found.append((c0,r0,c,r,c2,r2))
                    stack.append((c2,r2,a2 if a2 is not None else arm))
    print(name,'arm switches ahead of cop:',len(found), found[:3])
T1=(list('abcdefg'),[('a','b'),('b','c'),('c','d'),('d','e'),('c','f'),('f','g')])
T2=(list('abcdefgh'),[('a','b'),('b','c'),('c','d'),('d','e'),('c','f'),('f','g'),('f','h')])
check('T1',*T1,[{'a','b'},{'d','e'},{'f','g'}],'c')
check('T2',*T2,[{'a','b'},{'d','e'},{'f','g','h'}],'c')
# spider 3 arms of 3
V=['o']+[x+str(i) for x in 'abc' for i in (1,2,3)]
E=[('o','a1'),('a1','a2'),('a2','a3'),('o','b1'),('b1','b2'),('b2','b3'),('o','c1'),('c1','c2'),('c2','c3')]
check('S333',V,E,[{'a1','a2','a3'},{'b1','b2','b3'},{'c1','c2','c3'}],'o')
# fix 4 proposal: T1 with branch c-f-g-h, C starting at h
T1x=(list('abcdefgh'),[('a','b'),('b','c'),('c','d'),('d','e'),('c','f'),('f','g'),('g','h')])
check('T1 with c-f-g-h',*T1x,[{'a','b'},{'d','e'},{'f','g','h'}],'c')
