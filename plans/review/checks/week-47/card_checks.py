import itertools
def legal(h): return all(x>=0 for x in h) and all(abs(h[i]-h[i+1])<=1 for i in range(len(h)-1))
def comps(n,clues,H=12):
    out=[]
    def rec(p):
        if len(p)==n:
            out.append(tuple(p));return
        i=len(p)
        for v in range(H+1):
            if i in clues and v!=clues[i]: continue
            if p and abs(p[-1]-v)>1: continue
            rec(p+[v])
    rec([]); return out
# K-1 P1, P5 counts; K-1 P6 min moves; 2-3 P6 forcing pairs
print('P1',len(comps(5,{0:1,4:1})))
print('P5',len(comps(7,{0:1,4:3,6:1})))
c=comps(7,{0:1,4:3,6:1}); print(min(c,key=sum),max(c,key=sum))
# forcing pairs on 7 sites heights 0..6
forcing=[]
for i,j in itertools.combinations(range(7),2):
    for a in range(7):
        for b in range(7):
            cs=comps(7,{i:a,j:b},H=13)
            if len(cs)==1: forcing.append((i,a,j,b))
print('forcing',forcing)
# min clue set conjecture: endpoints + non-strict-slope sites
def forced(n,clues,H):
    return len(comps(n,clues,H))==1
def turning(h):
    n=len(h); s=set([0,n-1])
    for i in range(1,n-1):
        if not ((h[i-1]<h[i]<h[i+1]) or (h[i-1]>h[i]>h[i+1])): s.add(i)
    return s
bad=0;tot=0
for n in range(2,7):
    for h in itertools.product(range(4),repeat=n):
        if not legal(h): continue
        H=max(h)+n+1
        best=None
        for k in range(1,n+1):
            for S in itertools.combinations(range(n),k):
                if forced(n,{i:h[i] for i in S},H): best=k;break
            if best: break
        tot+=1
        T=turning(h)
        if best!=len(T) or not forced(n,{i:h[i] for i in T},H): bad+=1; print('mismatch',h,best,T)
print('min-clue rule checked',tot,'bad',bad)
# greedy lowering reaches L ; never-stuck moves
# every forcing set contains all turning points
viol=0;cnt=0
for n in range(2,7):
    for h in itertools.product(range(4),repeat=n):
        if not legal(h): continue
        H=max(h)+n+1; T=turning(h)
        for k in range(1,n+1):
            for S in itertools.combinations(range(n),k):
                if forced(n,{i:h[i] for i in S},H):
                    cnt+=1
                    if not T<=set(S): viol+=1
print('forcing sets',cnt,'missing a turning point',viol)
def comps15(n,clues,H=15):
    out=[]
    def rec(p):
        if len(p)==n: out.append(tuple(p));return
        i=len(p)
        for v in range(H+1):
            if i in clues and v!=clues[i]: continue
            if p and abs(p[-1]-v)>1: continue
            rec(p+[v])
    rec([]); return out
c=comps(7,{0:0,5:3})
for i in range(7): print(i, sorted(set(h[i] for h in c)))
print(len(c), max(max(h) for h in c))
# independent choice failure example: site2=0 and site3=3?
print(any(h[2]==0 and h[3]==3 for h in c))
# K-1 P6 board 0-3 forcing pairs check
import itertools
n=0
for i,j in itertools.combinations(range(5),2):
  for a in range(4):
    for b in range(4):
      cs=[h for h in comps(5,{i:a,j:b}) ]
      if cs and len(cs)==1: n+=1
print('forcing on 0-3 board (uncapped heights)',n)
# with empty 0-4 board, forcing pairs
f=[]
for i,j in itertools.combinations(range(5),2):
  for a in range(5):
    for b in range(5):
      cs=comps(5,{i:a,j:b})
      if len(cs)==1: f.append((i,a,j,b))
print('forcing on 0-4 board',f)
