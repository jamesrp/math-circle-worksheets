"""Tournament utilities used to check every answer in the packets."""
from itertools import combinations, permutations, product

def all_tournaments(n):
    pairs = list(combinations(range(n), 2))
    for bits in product([0, 1], repeat=len(pairs)):
        beat = set()
        for (a, b), x in zip(pairs, bits):
            beat.add((a, b) if x == 0 else (b, a))
        yield frozenset(beat)

def lineups(n, beat):
    return [p for p in permutations(range(n))
            if all((p[i], p[i+1]) in beat for i in range(n-1))]

def wins(n, beat):
    return [sum((i, j) in beat for j in range(n)) for i in range(n)]

def kings(n, beat):
    ks = []
    for x in range(n):
        ok = True
        for y in range(n):
            if y == x: continue
            if (x, y) in beat: continue
            if any((x, z) in beat and (z, y) in beat for z in range(n)): continue
            ok = False
        if ok: ks.append(x)
    return ks

def canon(n, beat):
    best = None
    for p in permutations(range(n)):
        s = tuple(sorted((p[a], p[b]) for a, b in beat))
        if best is None or s < best: best = s
    return best

def landau_ok(scores):
    s = sorted(scores); n = len(s)
    if sum(s) != n*(n-1)//2: return False
    return all(sum(s[:k]) >= k*(k-1)//2 for k in range(1, n+1))

def from_edges(edges, names):
    idx = {c: i for i, c in enumerate(names)}
    return frozenset((idx[a], idx[b]) for a, b in edges)
