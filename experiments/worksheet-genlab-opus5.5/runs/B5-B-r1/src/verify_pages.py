# Independent re-check of every answer the pages depend on (written by the page author).
from functools import lru_cache
def L(S, N, mis=False):
    t=[]
    for n in range(N+1):
        if n==0: t.append(not mis); continue
        t.append(all(not t[n-s] for s in S if s<=n))
    return t
def lp(S,a,b,mis=False):
    t=L(S,b,mis); return [n for n in range(a,b+1) if t[n]]
def wt(S,n,mis=False):
    t=L(S,n,mis); return [s for s in S if s<=n and t[n-s]]
def multi(S, piles):
    @lru_cache(None)
    def lose(p):
        for i,n in enumerate(p):
            for s in S:
                if s<=n:
                    q=list(p); q[i]-=s
                    if lose(tuple(sorted(q))): return False
        return True
    return lose(tuple(sorted(piles)))
ok=True
def chk(c,msg):
    global ok
    print(('ok   ' if c else 'FAIL ')+msg); ok&=c
# K-1
chk(lp((1,2),1,12)==[3,6,9,12],"K1 P4 traps 3,6,9,12")
chk([wt((1,2),n) for n in (3,4,5,6,7,8)]==[[],[1],[2],[],[1],[2]],"K1 P1/P2")
chk([wt((1,2),n) for n in (5,4,2,1)]==[[2],[1],[2],[1]],"K1 P3 replies")
chk([wt((1,2,3),n) for n in (3,4,5,8)]==[[3],[],[1],[]],"K1 P5")
chk(lp((1,3),1,10)==[2,4,6,8,10],"K1 P6")
chk([multi((1,2),p) for p in [(2,2),(4,4),(4,5)]]==[True,True,False],"K1 P7")
chk([wt((1,2),n,True) for n in (3,4,5,7)]==[[2],[],[1],[]],"K1 P8 poison")
chk([multi((1,2),p) for p in [(1,1,1),(2,2,2),(3,3,3)]]==[False,False,True],"K1 P9")
# 2-3
chk([wt((1,2),n) for n in (7,9,11,12)]==[[1],[],[2],[]],"23 P1")
chk(lp((1,3,4),1,20)==[2,7,9,14,16],"23 P2")
chk(wt((1,3,4),8)==[1] and wt((1,3,4),11)==[4] and wt((1,3,4),6)==[4] and wt((1,3,4),9)==[],"23 P3 Maya/Leo/Ravi/Zoe")
chk(wt((1,3,4),5)==[3],"23 P3 Ravi refuted only by taking 3")
chk([wt((1,3,4),n) for n in (23,25,28,31)]==[[],[4],[],[1,3]],"23 P4")
chk(lp((1,3),1,15)==[2,4,6,8,10,12,14] and lp((1,2,3),1,15)==[4,8,12] and lp((1,4),1,15)==[2,5,7,10,12,15],"23 P5")
chk([multi((1,3,4),p) for p in [(5,5),(1,3),(3,4),(4,6)]]==[True,True,False,True],"23 P6")
# Kai
S=(1,3,4)
def kai_take(n): return 4 if n>=4 else (3 if n==3 else 1)
@lru_cache(None)
def kai_wins(n, kai_to_move):
    if n==0: return not kai_to_move  # previous mover took last
    if kai_to_move: return kai_wins(n-kai_take(n), False)
    return all(kai_wins(n-s, True) for s in S if s<=n)
kw=[n for n in range(1,21) if kai_wins(n,True)]
chk(kw==[1,3,4,6,11],"23 P7 Kai wins only from 1,3,4,6,11: %s"%kw)
chk(not kai_wins(13,True) and 4 in wt(S,13),"23 P7 Kai's first move from 13 correct, still loses")
# 4-5
chk(lp((1,2),1,20)==[3,6,9,12,15,18] and lp((1,2,3),1,20)==[4,8,12,16,20],"45 P1")
chk(lp((1,3,4),1,30)==[2,7,9,14,16,21,23,28,30],"45 P2")
chk([wt((1,3,4),n) for n in (50,53,54,56,100)]==[[1],[4],[3],[],[]],"45 P3")
chk(lp((1,4),1,20)==[2,5,7,10,12,15,17,20] and lp((1,4,5),1,20)==[2,8,10,16,18] and lp((1,2,4),1,20)==[3,6,9,12,15,18] and lp((1,3,5),1,20)==list(range(2,21,2)),"45 P4")
chk(lp((1,3),1,60)==list(range(2,61,2)) and lp((1,2,3,4),1,60)==list(range(5,61,5)) and lp((1,2,6),1,60)==[n for n in range(1,61) if n%7 in (0,3)],"45 P5 sample rules")
seq=lp((1,6,9),1,35); chk(seq==[2,4,7,12,14,17,19,22,24,27,29,32,34],"45 P6 %s"%seq)
sq8=[(a,b) for a in range(7) for b in range(7) if multi((1,2),(a,b))]
chk(len(sq8)==17 and all((a-b)%3==0 for a,b in sq8),"45 P8 17 squares")
sq9=[(a,b) for a in range(8) for b in range(8) if multi((1,3,4),(a,b))]
fam={0:0,2:0,7:0,1:1,3:1,4:2,6:2,5:3}
chk(len(sq9)==18 and all(fam[a]==fam[b] for a,b in sq9),"45 P9 18 squares, families")
print("ALL OK" if ok else "SOMETHING FAILED")
