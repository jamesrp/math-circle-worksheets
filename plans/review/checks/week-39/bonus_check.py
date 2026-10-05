#!/usr/bin/env python3
"""Week 39 bonus packet (week-39-bonus.pdf, W39-BONUS-v1): brief independent check.

P1  four-arm star H-A, H-B, H-C, H-D; add roads between outer stops.  Find the
    fewest additions allowing a reduced (no immediate reversal) closed walk at H
    visiting A, B, C, D; the shortest such walk; and whether deleting one added
    road keeps such a walk.  Searches all multisets of up to 3 added roads
    (parallel roads allowed, each added road its own identity).
P2  six-step (and four-step) closed walks at H on the unit 3-star and on the
    3-star with each arm extended by one edge; every one reduces to empty.
P3  two-ring map (H-L-M-H = a, H-R-S-H = b); all 21 pairs of the seven word
    cards, compared after concatenating in both orders, at the level of
    individual directed road steps.
Standard library only.  Run: python3 bonus_check.py > out_bonus_check.txt
"""
import itertools
from collections import deque

FAIL = []


def ok(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


# ---------- reduced walks on multigraphs with edge identities
def reduced_tour(edges, start, must, maxlen):
    """Shortest closed walk at start with no immediate reversal of the same edge id,
    visiting every vertex in must.  edges: list of (u, v); id = index."""
    inc = {}
    for i, (u, v) in enumerate(edges):
        inc.setdefault(u, []).append((i, v))
        inc.setdefault(v, []).append((i, u))
    must = frozenset(must)
    # state: (vertex, last edge id, visited subset of must)
    q = deque([(start, None, frozenset(), 0, (start,))])
    seen = set()
    while q:
        v, last, vis, d, path = q.popleft()
        if v == start and d > 0 and vis == must:
            return d, path
        if d == maxlen:
            continue
        for i, w in inc.get(v, []):
            if i == last:
                continue  # same road straight back = immediate reversal
            nv = vis | ({w} & must)
            key = (w, i, nv, d + 1)
            if key in seen:
                continue
            seen.add(key)
            q.append((w, i, nv, d + 1, path + (w,)))
    return None


print("== Bonus P1 (four-arm star)")
STAR = [("H", "A"), ("H", "B"), ("H", "C"), ("H", "D")]
LEAVES = "ABCD"
pairs = list(itertools.combinations(LEAVES, 2))
best = {}
for k in range(0, 4):
    for add in itertools.combinations_with_replacement(pairs, k):
        r = reduced_tour(STAR + list(add), "H", LEAVES, 12)
        if r:
            best.setdefault(k, []).append((add, r))
kmin = min(best)
ok(kmin == 2, f"fewest added roads = {kmin}")
opt = best[2]
ok(sorted("+".join("".join(p) for p in a) for a, _ in opt) == ["AB+CD", "AC+BD", "AD+BC"],
   f"exactly three optimal additions: {[ '+'.join(''.join(p) for p in a) for a, _ in opt]}")
ok(all(r[0] == 6 for _, r in opt), f"shortest surviving tour with two additions = 6 steps, e.g. {'-'.join(opt[0][1][1])}")
for add, _ in opt:
    for drop in range(2):
        rest = [add[1 - drop]]
        ok(reduced_tour(STAR + rest, "H", LEAVES, 20) is None,
           f"{'+'.join(''.join(p) for p in add)} minus {''.join(add[drop])}: no surviving tour visits all four (to 20 steps)")
five = [a for a, r in best.get(3, []) if r[0] == 5]
ok(len(five) > 0, f"extension: a 5-step tour exists with three additions (e.g. {'+'.join(''.join(p) for p in five[0])})")


# ---------- P2
def closed_walks(adj, s, n):
    out = []

    def rec(w):
        if len(w) == n + 1:
            if w[-1] == s:
                out.append(w)
            return
        for v in adj[w[-1]]:
            rec(w + [v])

    rec([s])
    return out


def stack(w):
    r = [w[0]]
    for v in w[1:]:
        if len(r) >= 2 and r[-2] == v:
            r.pop()
        else:
            r.append(v)
    return r


def adj_of(E):
    a = {}
    for u, v in E:
        a.setdefault(u, []).append(v)
        a.setdefault(v, []).append(u)
    return a


print("== Bonus P2 (two trees)")
U = adj_of([("H", "A"), ("H", "B"), ("H", "C")])
X = adj_of([("H", "A"), ("H", "B"), ("H", "C"), ("A", "D"), ("B", "E"), ("C", "F")])
for name, G, want6, want4 in [("unit star", U, 27, 9), ("extended star", X, 48, 12)]:
    w6, w4 = closed_walks(G, "H", 6), closed_walks(G, "H", 4)
    ok(len(w6) == want6 and len(w4) == want4 and all(stack(w) == ["H"] for w in w6),
       f"{name}: {len(w6)} six-step and {len(w4)} four-step returns; all reduce to H")
w6 = closed_walks(X, "H", 6)


def gaps(w):
    idx = [i for i, v in enumerate(w) if v == "H"]
    return tuple(b - a for a, b in zip(idx, idx[1:]))


from collections import Counter
ok(Counter(gaps(w) for w in w6) == Counter({(2, 2, 2): 27, (2, 4): 9, (4, 2): 9, (6,): 3}),
   "extended-star split (2,2,2)=27, (2,4)=9, (4,2)=9, (6)=3 as in the bonus guide")

print("== Bonus P3 (word cards on the two-ring map)")
LOOP = {"a": "HLMH", "A": "HMLH", "b": "HRSH", "B": "HSRH"}


def expand(word):
    w = "H"
    for ch in word.replace(" ", ""):
        w += LOOP[ch][1:]
    return w


def red(w):
    return "".join(stack(list(w)))


CARDS = ["a", "aa", "b", "ab", "abab", "abA", "abbA"]
comm = []
for x, y in itertools.combinations(CARDS, 2):
    if red(expand(x + y)) == red(expand(y + x)):
        comm.append((x, y, red(expand(x + y))))
ok([(x, y) for x, y, _ in comm] == [("a", "aa"), ("ab", "abab"), ("abA", "abbA")],
   f"exactly 3 of 21 pairs commute: {[(x, y) for x, y, _ in comm]}")
ok([r for _, _, r in comm] == [expand("aaa"), expand("ababab"), red(expand("abbbA"))],
   "their common reductions are aaa, ababab, abbbA")
ok(red(expand("aAb")) == expand("b"), "worked example aAb reduces to b")

print("\nSUMMARY:", "all checks passed" if not FAIL else f"{len(FAIL)} failed: {FAIL}")
