# Which B sets are reachable after N days if the child chooses any card in A to move each day?
from itertools import combinations
def reachable(N):
    states={(frozenset(),frozenset())}
    for d in range(1,N+1):
        new=set()
        for A,B in states:
            A2=A|{2*d-1,2*d}
            for c in A2:
                new.add((A2-{c},B|{c}))
        states=new
    return {B for A,B in states}
def ballot(B,N):
    return all(sum(1 for b in B if b<=2*d)>=d for d in range(1,N+1))
cat=[1,1,2,5,14,42,132,429,1430]
for N in range(1,8):
    R=reachable(N)
    C={frozenset(c) for c in combinations(range(1,2*N+1),N) if ballot(c,N)}
    # greedy: move smallest target card available each day
    ok=True
    for B in C:
        A=set();moved=set()
        for d in range(1,N+1):
            A|={2*d-1,2*d}
            cand=sorted(x for x in A if x in B)
            if not cand: ok=False;break
            A.remove(cand[0]);moved.add(cand[0])
        if moved!=set(B): ok=False
    print(N,len(R),R==C,'Catalan',cat[N+1],'greedy works',ok)
