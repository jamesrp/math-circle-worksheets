# Card spot checks for Week 36: threes, caps, splits, lines on the printed board, shape-only maximum.
from itertools import combinations, product
S=['C','T','S']; F=['O','H','F']
tiles=[(s,f) for s in S for f in F]
def ok(a,b,c):
    return all(len({a[i],b[i],c[i]}) in (1,3) for i in range(2))
lines=[t for t in combinations(tiles,3) if ok(*t)]
print('lines',len(lines))
def comp(a,b):
    return [c for c in tiles if c not in (a,b) and ok(a,b,c)]
print('pairs P1', [comp(('C','O'),('C','H')), comp(('C','O'),('T','O')), comp(('C','H'),('T','F')), comp(('T','H'),('S','O'))])
def free(X): return not any(ok(*t) for t in combinations(X,3))
caps={k:[X for X in combinations(tiles,k) if free(X)] for k in range(6)}
print({k:len(v) for k,v in caps.items()})
# board straight lines: rows shapes, cols fills
pos={t:(S.index(t[0]),F.index(t[1])) for t in tiles}
def straight(l):
    ps=sorted(pos[t] for t in l)
    (r0,c0),(r1,c1),(r2,c2)=ps
    return (r1-r0,c1-c0)==(r2-r1,c2-c1)
print('straight on board', sum(straight(l) for l in lines))
for t in tiles:
    thr=[l for l in lines if t in l]
    print(t, len(thr), 'straight', sum(straight(l) for l in thr))
# partitions
parts=set()
for a,b,c in combinations(lines,3):
    if len(set(a)|set(b)|set(c))==9: parts.add(frozenset([a,b,c]))
print('partitions',len(parts))
print('bent', [''.join(a+b for a,b in l) for l in lines if not straight(l)])
# one-attribute (shape only) max collection with no three of shapes all same/all different
def ok1(a,b,c): return len({a[0],b[0],c[0]}) in (1,3)
best=max(k for k in range(10) for X in combinations(tiles,k) if not any(ok1(*t) for t in combinations(X,3)))
print('shape-only max', best)

# Random greedy cap sizes in 9, 27 and 81 cards (app fit).
import random, itertools
from collections import Counter
def run(d,trials):
    pts=list(itertools.product(range(3),repeat=d))
    def third(a,b): return tuple((-x-y)%3 for x,y in zip(a,b))
    cnt=Counter()
    for _ in range(trials):
        order=pts[:]; random.shuffle(order)
        chosen=[]; banned=set()
        for p in order:
            if p in banned or p in chosen: continue
            for q in chosen: banned.add(third(p,q))
            chosen.append(p)
        cnt[len(chosen)]+=1
    return cnt
random.seed(1)
print('AG(2,3)',run(2,2000))
print('AG(3,3)',run(3,20000))
print('AG(4,3)',run(4,5000))
