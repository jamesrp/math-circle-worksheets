from functools import lru_cache
def labels(S,N=60):
    L=[]
    for n in range(N):
        L.append('W' if any(n-s>=0 and L[n-s]=='L' for s in S) else 'L')
    return L
def grundy(S,N=60):
    g=[]
    for n in range(N):
        opts={g[n-s] for s in S if n-s>=0}
        m=0
        while m in opts: m+=1
        g.append(m)
    return g

# fixed-strategy checks: plan(pile, history) -> move ; returns whether plan always wins
def plan_always_wins(S, start, plan_first, plan):
    # plan(state) where state=(pile, last_partner_move, turn_index) ; returns move or None (illegal)
    # returns (True, None) or (False, losing game)
    def rec(pile, planner_to_move, last_partner, hist, k):
        if pile==0:
            # previous mover took last counter
            return (not planner_to_move, hist)
        if planner_to_move:
            m=plan(pile,last_partner,k)
            if m is None or m not in S or m>pile:
                return (False, hist+['ILLEGAL'])
            return rec(pile-m, False, None, hist+[('P',m,pile-m)], k+1)
        else:
            for m in S:
                if m<=pile:
                    ok,h=rec(pile-m, True, m, hist+[('O',m,pile-m)], k)
                    if not ok: return (False,h)
            return (True,None)
    return rec(start, plan_first, None, [], 0)

L12=labels((1,2))
print('K1 P1', [(n,'1st' if L12[n]=='W' else '2nd') for n in (2,3,4,5)])
print('K1 P3 traps', [n for n in range(1,13) if L12[n]=='L'])
print('K1 P5 traps', [n for n in range(1,13) if labels((1,2,3))[n]=='L'])
print('K1 P6 traps', [n for n in range(1,13) if labels((1,3))[n]=='L'])
for S in [(1,2),(1,2,3),(1,3)]:
    print('K1 P7 20', S, '1st' if labels(S)[20]=='W' else '2nd')
g12=grundy((1,2))
for a,b in [(2,2),(1,2),(3,3),(1,4),(2,5)]:
    print('two piles {1,2}',a,b,'1st' if g12[a]^g12[b] else '2nd')

# Ben always takes 2 when he can, goes first. Can you beat him?
@lru_cache(None)
def you_win(pile, ben_to_move):
    if pile==0: return ben_to_move  # if Ben to move at 0, you took last
    if ben_to_move:
        m=2 if pile>=2 else 1
        return you_win(pile-m, False)
    return any(you_win(pile-m, True) for m in (1,2) if m<=pile)
print('Ben', [(n,you_win(n,True)) for n in range(1,13)])

# 2-3 P2 plans, S={1,2}
S=(1,2)
mia=lambda p,last,k: 2 if k==0 else (2 if last==1 else 1)
print('Mia', plan_always_wins(S,8,True,mia))
leo=lambda p,last,k: 2 if p>=2 else 1
print('Leo', plan_always_wins(S,10,True,leo))
ana=lambda p,last,k: 2 if last==1 else 1
print('Ana', plan_always_wins(S,9,False,ana))
sam=lambda p,last,k: 1 if k==0 else last
print('Sam', plan_always_wins(S,11,True,sam))
L134=labels((1,3,4))
print('2-3 P3 2nd piles', [n for n in range(1,21) if L134[n]=='L'])
S=(1,3,4)
kai=lambda p,last,k: max(m for m in S if m<=p)
print('Kai', plan_always_wins(S,10,True,kai))
theo=lambda p,last,k: last if last<=p else 1
print('Theo', plan_always_wins(S,7,False,theo))
def zoe(p,last,k):
    for m in S:
        if p-m in (7,2): return m
    return p
print('Zoe', plan_always_wins(S,9,False,zoe))
print('2-3 P5', [(n, '1st' if L134[n]=='W' else '2nd') for n in (25,30,37,50)])
print('2-3 P6 {1,2,4}', [n for n in range(1,16) if labels((1,2,4))[n]=='L'], [n for n in range(1,16) if L12[n]=='L'])
for a,b in [(5,5),(3,6),(1,5),(2,5)]:
    print('2-3 P7',a,b,'1st' if g12[a]^g12[b] else '2nd')

# 4-5
print('4-5 P1', [n for n in range(1,16) if L12[n]=='L'], 100%3)
print('4-5 P2', ''.join(L134[1:31]), [n for n in range(1,31) if L134[n]=='L'])
rules=[(1,2),(1,3),(1,2,3),(1,4),(1,3,5),(1,2,4),(1,4,6)]
for R in rules:
    LL=labels(R)
    greedy_bad=[n for n in range(1,31) if LL[n]=='W' and LL[n-max(m for m in R if m<=n)]=='W']
    print('4-5 P3', R, [n for n in range(1,25) if LL[n]=='L'], 'greedy bad', greedy_bad)
for R in [(1,2,3),(1,4),(1,2,6)]:
    print('4-5 P5', R, [n for n in range(1,22) if labels(R)[n]=='L'])
# brute force: any rule (subset of 1..12 containing 1) giving L = {3,5,8,10,13,15,...} up to 40?
from itertools import combinations
target=[n for n in range(1,40) if n%5 in (0,3)]
found=[]
for k in range(0,8):
    for c in combinations(range(2,16),k):
        R=(1,)+c
        if [n for n in range(1,40) if labels(R,40)[n]=='L']==target: found.append(R)
print('impossible list found rules:', found[:5])
# also check others are achievable via brute force smallest
for tgt,name in [([n for n in range(1,40) if n%4==0],'mult4'),([n for n in range(1,40) if n%5 in (0,2)],'0,2 mod5'),([n for n in range(1,40) if n%7 in (0,3)],'0,3 mod7')]:
    f=[]
    for k in range(0,5):
        for c in combinations(range(2,12),k):
            R=(1,)+c
            if [n for n in range(1,40) if labels(R,40)[n]=='L']==tgt: f.append(R)
    print(name, f[:6])
g134=grundy((1,3,4))
print('g134', g134[:21])
print('4-5 P6 losing pairs {1,2} 0..8', [(a,b) for a in range(9) for b in range(a,9) if g12[a]==g12[b]])
print('4-5 P7 losing pairs {1,3,4} 0..9', [(a,b) for a in range(10) for b in range(a,10) if g134[a]==g134[b]])
print('4-5 P8 (11,13)', g134[11],g134[13], '(12,18)', g134[12], g134[18])
L169=labels((1,6,9))
print('4-5 P9', ''.join(L169[0:41]), [n for n in range(1,41) if L169[n]=='L'])
