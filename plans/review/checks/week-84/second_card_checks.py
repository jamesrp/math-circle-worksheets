# Independent possible-worlds checks for the Week 84 card (second run).
from itertools import product

def hat_reply(world, i, S):
    m = [w for w in S if all(w[j]==world[j] for j in range(len(world)) if j!=i)]
    return 'P' if all(w[i]=='B' for w in m) else 'N'

def hat_run(actual, S, rounds):
    S = list(S); hist = []
    for r in range(rounds):
        rep = tuple(hat_reply(actual,i,S) for i in range(len(actual)))
        hist.append(''.join(rep))
        S = [w for w in S if tuple(hat_reply(w,i,S) for i in range(len(w)))==rep]
    return hist, S

def worlds(n, announce=True):
    W = [''.join(p) for p in product('BR', repeat=n)]
    return [w for w in W if 'B' in w] if announce else W

# P2 and P3, three dolls
W7 = worlds(3)
print("P2/P3 histories (3 rounds) with announcement:")
for a in W7:
    h,_ = hat_run(a, W7, 3); print(" ", a, h)
# bookkeeping: private-view checks needed for a correct public update in round r
print("Public update in round 1 needs", len(W7)*3, "private-view checks (7 worlds x 3 dolls)")
# P4
W8 = worlds(3, False)
print("P4 no announcement:", {a: hat_run(a, W8, 4)[0] for a in W8})
# unordered reading of P3
from collections import defaultdict
g = defaultdict(list)
for a in W7:
    h,_ = hat_run(a, W7, 4); g[tuple(''.join(sorted(x)) for x in h)].append(a)
print("Unordered histories over 4 rounds:", dict(g))
# Two-doll non-task update example: actual BR, replies P then N
W3 = worlds(2)
rep = tuple(hat_reply('BR',i,W3) for i in range(2))
keep = [w for w in W3 if tuple(hat_reply(w,i,W3) for i in range(2))==rep]
print("Two dolls, actual BR: replies", rep, "keep", keep, "removed", [w for w in W3 if w not in keep])
# NOT YET example for p.2: doll 1 sees B on doll 2
print("Two dolls, doll 1 sees B: matches", [w for w in W3 if w[1]=='B'])
# Four dolls all blue
W15 = worlds(4)
print("Four dolls BBBB:", hat_run('BBBB', W15, 4)[0])
print("Four dolls BBBR:", hat_run('BBBR', W15, 4)[0])

# Cafe, n people
def cafe_conv(deal):
    S = [''.join(p) for p in product('YN', repeat=len(deal))]
    conv = []
    for i in range(len(deal)):
        def ans(d, S):
            m = [w for w in S if w[i]==d[i]]
            if all(all(c=='Y' for c in w) for w in m): return 'YES'
            if all(not all(c=='Y' for c in w) for w in m): return 'NO'
            return 'NOT YET'
        a = ans(deal, S); conv.append(a)
        S = [w for w in S if ans(w, S)==a]
    return tuple(conv)
for n in (2,3):
    g = defaultdict(list)
    for d in product('YN', repeat=n):
        g[cafe_conv(''.join(d))].append(''.join(d))
    print(f"Cafe {n} people:", dict(g))
    if n==3:
        from collections import Counter
        need = Counter()
        for c in g:
            for k,v in Counter(c).items(): need[k]=max(need[k],v)
        print("  most reply cards of each kind in one conversation:", dict(need))

# Proposed p.2 worked round: two dolls, actual RB
rep = tuple(hat_reply('RB',i,W3) for i in range(2))
print("Two dolls, actual RB: doll1 matches", [w for w in W3 if w[1]=='B'], "doll2 matches", [w for w in W3 if w[0]=='R'],
      "replies", rep, "removed", {w: tuple(hat_reply(w,i,W3) for i in range(2)) for w in W3 if tuple(hat_reply(w,i,W3) for i in range(2))!=rep})
