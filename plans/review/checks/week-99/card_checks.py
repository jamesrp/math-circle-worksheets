"""Week 99 card: checks for claims the card adds beyond math.md.
Run: python3 card_checks.py  (standard library only)."""
from itertools import combinations_with_replacement as cwr, permutations
from collections import deque

def line_work(s, t):
    return sum(abs(a - b) for a, b in zip(sorted(s), sorted(t)))

def greedy_outcomes(s, t):
    """All totals of 'shortest remaining delivery' over every tie-break."""
    res = set()
    def rec(S, T, acc):
        if not S:
            res.add(acc); return
        best = min(abs(a - b) for a in S for b in T)
        for i, a in enumerate(S):
            for j, b in enumerate(T):
                if abs(a - b) == best:
                    rec(S[:i] + S[i+1:], T[:j] + T[j+1:], acc + best)
    rec(list(s), list(t), 0)
    return res

# 1. Greedy waste on bins 0-5 (worst tie-break and best tie-break)
for n in (2, 3, 4):
    worst = (0, None); forced = (0, None)
    for s in cwr(range(6), n):
        for t in cwr(range(6), n):
            opt = line_work(s, t)
            outs = greedy_outcomes(s, t)
            w = max(outs) - opt
            if w > worst[0]: worst = (w, (s, t))
            f = min(outs) - opt          # waste even with the luckiest tie-break
            if f > forced[0]: forced = (f, (s, t))
    print(f"{n} counters: max waste (worst tie) {worst}; max waste every tie-break {forced}")

# 2. Ring of 6 bins vs open line: four counters at 0 to targets 1,2,4,5
def bfs(start, target, adj):
    start, target = tuple(start), tuple(target)
    seen = {start: 0}; q = deque([start])
    while q:
        st = q.popleft()
        if st == target: return seen[st]
        for i, c in enumerate(st):
            if c:
                for j in adj[i]:
                    nx = list(st); nx[i] -= 1; nx[j] += 1; nx = tuple(nx)
                    if nx not in seen:
                        seen[nx] = seen[st] + 1; q.append(nx)
line_adj = {i: [j for j in (i-1, i+1) if 0 <= j < 6] for i in range(6)}
ring_adj = {i: [(i-1) % 6, (i+1) % 6] for i in range(6)}
s = [4,0,0,0,0,0]; t = [0,1,1,0,1,1]
print("0000 -> 1245: line", bfs(s, t, line_adj), "ring", bfs(s, t, ring_adj))

# 3. Equal position totals: every distance is even
cards = [c for c in cwr(range(5), 4) if sum(c) == 8]
print("cards", ["".join(map(str, c)) for c in cards],
      "all distances even:", all(line_work(a, b) % 2 == 0 for a in cards for b in cards))

# 4. P1 pairs: does any printed P1/P2 pair need a counter to stay put or cross left?
for s0, t0 in [("00","24"),("03","12"),("0005","1234"),("1144","0225"),("2222","0134")]:
    print(s0, "->", t0, "least work", line_work(map(int,s0), map(int,t0)))

# 5. Total-8 arrangements of four counters: farthest pairs on bins 0-4 and 0-5
for m in (5, 6):
    A = [x for x in cwr(range(m), 4) if sum(x) == 8]
    M = max(line_work(a, b) for a in A for b in A)
    far = [(a, b) for i, a in enumerate(A) for b in A[i+1:] if line_work(a, b) == M]
    print(f"bins 0-{m-1}: {len(A)} arrangements, max work {M}, reached by {far}")
