from functools import lru_cache
from itertools import combinations_with_replacement as cwr

# Rook: positions (a,b), moves reduce one coordinate
@lru_cache(None)
def rookP(a,b):
    moves=[(x,b) for x in range(a)]+[(a,y) for y in range(b)]
    return all(not rookP(*m) for m in moves)
@lru_cache(None)
def queenP(a,b):
    moves=[(x,b) for x in range(a)]+[(a,y) for y in range(b)]+[(a-k,b-k) for k in range(1,min(a,b)+1)]
    return all(not queenP(*m) for m in moves)
@lru_cache(None)
def nimP(p):
    p=tuple(sorted(p))
    for i in range(len(p)):
        for k in range(p[i]):
            q=list(p); q[i]=k
            if nimP(tuple(sorted(q))): return False
    return True

print("rook P 8x8:", [(a,b) for a in range(8) for b in range(8) if rookP(a,b)])
print("queen P 8x8:", [(a,b) for a in range(8) for b in range(8) if queenP(a,b)])
print("queen P 20x20:", [(a,b) for a in range(20) for b in range(20) if queenP(a,b) and a<=b])
for s in [(1,1,1),(1,1,2),(1,2,3),(2,2,2),(1,1,3),(2,2,3),(1,2,2),(2,3,3),(2,2,5),(1,4,5),(1,3,4),(2,4,6),(1,3,5),(2,4,5),(3,5,7),(6,10,12),(13,9,7),(11,14,21),(3,3),(4,1),(2,2),(5,3),(7,7),(4,4),(6,3)]:
    print(s, "P (second wins)" if nimP(s) else "N (first wins)")
print("P starts 1..3:", [s for s in cwr(range(1,4),3) if nimP(s)])
print("P starts 1..6:", [s for s in cwr(range(1,7),3) if nimP(s)])
print("P starts 1..7:", [s for s in cwr(range(1,8),3) if nimP(s)])

# ---- answers for the positions used on the pages ----
def rook_targets(a, b):
    moves = [(x, b) for x in range(a)] + [(a, y) for y in range(b)]
    return [m for m in moves if rookP(*m)]

# K-1 P1, P2; 2-3 P1: True = second player wins
for n, d in [(3, (2, 2)), (4, (3, 3)), (4, (3, 0)), (4, (2, 2)), (4, (1, 3)),
             (5, (4, 4)), (5, (4, 2)), (5, (3, 3)), (5, (1, 4)), (8, (7, 7))]:
    print("board", n, d, "second" if rookP(*d) else "first")
# K-1 P3: the unique winning move
for d in [(0, 3), (3, 1), (2, 4), (4, 3)]:
    t = rook_targets(*d)
    assert len(t) == 1, (d, t)
    print("K-1 P3", d, "->", t[0])

def nim_moves(p):
    p = list(p)
    res = []
    for i in range(len(p)):
        for k in range(p[i]):
            q = p[:]; q[i] = k
            if nimP(tuple(sorted(q))):
                res.append(f"pile {p[i]} -> {k}")
    return res

for s in [(4, 4), (9, 6), (12, 5), (15, 15), (20, 1), (52, 37), (23, 17), (30, 30),
          (3, 5, 7), (6, 10, 12), (13, 9, 7), (11, 14, 21)]:
    x = 0
    for v in s: x ^= v
    print(s, "second" if x == 0 else "first", nim_moves(s))

# ---- revision checks ----
# K-1 P1: two 3x3 starts must contrast (far corner: second; top middle: first)
assert rookP(2, 2) and not rookP(1, 2)
# 2-3 P4: two-pile starts played with counters
assert [nimP(s) for s in [(4, 4), (6, 2), (5, 3), (7, 7)]] == [True, False, False, True]
# 2-3 P6: 52 and 37 is a first-player win; the only winning move is 52 -> 37
assert not nimP((52, 37)) and nim_moves((52, 37)) == ["pile 52 -> 37"]
# 4-5 P5: the given data
second = [(1, 2, 3), (1, 4, 5), (2, 4, 6), (3, 5, 6), (2, 5, 7)]
first = [(1, 2, 4), (2, 3, 5), (2, 4, 7), (3, 4, 6)]
assert all(nimP(s) for s in second) and not any(nimP(s) for s in first)
# 4-5 P5 stacks: each pile splits into distinct powers of two in exactly one way
from itertools import combinations
pw = [1, 2, 4, 8, 16]
for n in range(1, 22):
    ways = [c for k in range(1, 6) for c in combinations(pw, k) if sum(c) == n]
    assert len(ways) == 1, (n, ways)
# rule "each stack size used an even number of times" agrees with play for piles 1..21
for s in cwr(range(1, 22), 3):
    even = all(sum((v >> b) & 1 for v in s) % 2 == 0 for b in range(5))
    assert even == nimP(s), s
print("revision checks ok")
