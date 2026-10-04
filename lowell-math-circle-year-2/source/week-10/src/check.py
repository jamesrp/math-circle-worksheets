"""Check the mathematics behind every problem and print answers.
Run after the three build scripts (it imports their town lists)."""

import itertools
from collections import Counter
import build_k1
import build_23
import build_45
import koenigsberg


ok = True


def claim(cond, msg):
    global ok
    if not cond:
        ok = False
        print("   FAIL:", msg)


def L(t, n):
    return t.letters.get(n, n)


def status(t):
    odd = t.odd()
    st = t.starts()
    return odd, st


def show(t, extra=""):
    d = t.deg()
    odd, st = status(t)
    starts = "; ".join(f"{L(t, s)}->{','.join(sorted(L(t, e) for e in es))}" for s, es in st.items())
    print(f"  {t.name}: {len(t.isl)} islands {len(t.br)} bridges; degrees "
          + " ".join(f"{L(t, n)}{d[n]}" for n in t.order)
          + f"; odd {[L(t, o) for o in odd]}; starts {starts or 'NONE'} {extra}")
    g = t.geometry_check(min_angle=40, min_visible=3.0)
    claim(not g, f"geometry {t.name}: {g}")
    c = t.counter_check()
    claim(not c, f"room for a 1-inch counter {t.name}: {c}")
    claim(t.connected(), f"{t.name} not connected")
    # parity theory agrees with exhaustive search
    if len(odd) == 0:
        claim(set(st) == set(t.order) and all(es == {s} for s, es in st.items()), f"{t.name} theory mismatch")
    elif len(odd) == 2:
        claim(set(st) == set(odd), f"{t.name} theory mismatch")
    else:
        claim(not st, f"{t.name} theory mismatch")


def additions(t):
    return [f"{L(t, u)}{L(t, v)}" for u, v in t.single_additions()]


def doubles(t):
    E = t.edges()
    return [f"{L(t, E[i][0])}{L(t, E[i][1])}" for i in t.double_bridge_works()]



def exists(n, m, pred, maxmult=2):
    """A connected town with n islands and m bridges, at most maxmult bridges between two islands."""
    pairs = list(itertools.combinations(range(n), 2))
    for combo in itertools.combinations_with_replacement(pairs, m):
        if max(Counter(combo).values()) > maxmult:
            continue
        deg = Counter()
        adj = {i: set() for i in range(n)}
        for u, v in combo:
            deg[u] += 1
            deg[v] += 1
            adj[u].add(v)
            adj[v].add(u)
        seen = {0}
        st = [0]
        while st:
            x = st.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    st.append(y)
        if len(seen) < n:
            continue
        odd = [i for i in range(n) if deg[i] % 2]
        if pred(odd, combo):
            return combo
    return None


def pictures(pics, expect=None):
    for k, p in enumerate(pics):
        o = p.odd_count()
        print(f"  {p.name}: odd points {o} -> {'one stroke' if o in (0, 2) else 'cannot'}; fewest strokes {max(1, o // 2)}")
        if expect is not None:
            claim((o in (0, 2)) == expect[k], f"picture {p.name} expectation")


def degree_set(towns):
    out = set()
    for t in towns:
        out |= set(t.deg().values())
    return sorted(out)


for mod in (build_k1, build_23, build_45):
    mod.T.clear()
    mod.PICS.clear()
build_k1.build()
build_23.build()
build_45.build()

# =============================================================== K-1
K = build_k1.T
print("K-1")
print(" P1 (all should be possible)")
for t in K[1]:
    show(t)
    claim(len(t.odd()) in (0, 2), f"{t.name} should be possible")
print(" P2 (colour start islands)")
for t in K[2]:
    show(t)
print(" P3 (check / X)")
exp3 = [False, True, True, True, False]
for t, e in zip(K[3], exp3):
    show(t, "CHECK" if len(t.odd()) in (0, 2) else "X")
    claim((len(t.odd()) in (0, 2)) == e, f"{t.name} P3 expectation")
print(" P4 (closed walk check / X)")
exp4 = [True, False, False, True, True]
for t, e in zip(K[4], exp4):
    show(t, "CHECK" if len(t.odd()) == 0 else "X")
    claim((len(t.odd()) == 0) == e, f"{t.name} P4 expectation")
print(" P5 pictures (possible iff 0 or 2 odd points)")
pictures(build_k1.PICS[5], [True, True, False, True, False, True])
print(" P6 (impossible; one new bridge between which islands works?)")
for t in K[6]:
    show(t)
    claim(len(t.odd()) == 4, f"{t.name} should have 4 odd islands")
    print("   working additions:", additions(t))
print(" P8 (which doubled bridge works)")
for t in K[8]:
    show(t)
    print("   bridges that work:", doubles(t), f"of {len(t.br)}")

# =============================================================== 2-3
M = build_23.T
print("\nGrades 2-3")
print(" degrees present in P1-P2:", degree_set(M[1] + M[2]))
for key in (1, 2, 3):
    print(f" P{key}")
    for t in M[key]:
        show(t)
        if key == 1:
            claim(len(t.odd()) in (0, 2), f"{t.name} P1 should have a walk")
            tr = t.trail_from(t.odd()[0]) if len(t.odd()) == 2 else t.trail_from(t.order[0])
            print("   sample walk:", " ".join(L(t, x) for x in tr))
print(" P4 (one new bridge)")
for t in M[4]:
    show(t)
    claim(len(t.odd()) == 4, f"{t.name} 4 odd")
    print("   working additions:", additions(t))
print(" P5 (fewest new bridges for closed walk = odd/2, parallel bridges allowed)")
for t in M[5]:
    show(t, f"-> {len(t.odd()) // 2} new bridges")
print(" P7 pictures")
pictures(build_23.PICS[7], [True, False, True, False, True, True])
print(" P8 specs (at most two bridges between two islands, so each can be built with craft sticks)")
ex1 = exists(4, 6, lambda odd, c: len(odd) == 0)
ex2 = exists(5, 5, lambda odd, c: len(odd) > 2)
ex3 = exists(6, 8, lambda odd, c: odd == [0, 5])
ex4 = exists(3, 5, lambda odd, c: odd == [0, 1])
ex4b = exists(3, 5, lambda odd, c: odd == [0, 1], maxmult=1)
print("  4 islands 6 bridges, all even:", ex1)
print("  5 islands 5 bridges, more than 2 odd:", ex2)
print("  6 islands 8 bridges, odd exactly A and F:", ex3)
print("  3 islands 5 bridges, odd exactly A and B:", ex4, " (with single bridges only:", ex4b, ")")
claim(ex1 and ex2 and ex3 and ex4, "P8 spec impossible")
print(" P9: a full walk can always be reversed, so starts come in pairs or every island works -> impossible")
print(" P10 (fewest doubled bridges, closed)")
for t in M[10]:
    show(t, f"postman(closed, open) = {t.postman()}")

# =============================================================== 4-5
U = build_45.T
print("\nGrades 4-5")
print(" degrees present in P1-P3:", degree_set(U[1] + U[2] + U[3]))
for key in (1, 2, 3):
    print(f" P{key}")
    for t in U[key]:
        show(t, f"postman={t.postman()}")
print(" P5 Koenigsberg")
kt = koenigsberg.as_town()
d = kt.deg()
print("  degrees", dict(d), "odd", kt.odd(), "postman(closed, open) =", kt.postman())
claim(sorted(d.values()) == [3, 3, 3, 5], "Koenigsberg degrees")
print("  one new bridge works between:", additions(kt))
print(" P7 pictures (fewest strokes = max(1, odd/2))")
pictures(build_45.PICS[7])
print(" P8 Lee")
t = U[8][0]
show(t)
inv = {v: k for k, v in t.letters.items()}
lee = "A B C D E F G H I A".split()
lee_edges = [(inv[lee[i]], inv[lee[i + 1]]) for i in range(9)]
E = t.edges()
claim(all((u, v) in E or (v, u) in E for u, v in lee_edges), "Lee walk uses real bridges")
a = inv['A']
claim(t.deg()[a] == 2, "A has two bridges, so Lee is stuck at A")
m = len(E)
inc = {n: [] for n in t.isl}
for i, (u, v) in enumerate(E):
    inc[u].append((i, v))
    inc[v].append((i, u))
lee_idx = [next(i for i, e in enumerate(E) if e in ((u, v), (v, u))) for u, v in lee_edges]
count = 0
example = None


def dfs(x, used, k, nxt, path):
    global count, example
    if k == m:
        if x == a and nxt == len(lee_idx):
            count += 1
            if example is None:
                example = list(path)
        return
    for i, y in inc[x]:
        if used[i]:
            continue
        if i in lee_idx:
            if nxt >= len(lee_idx) or lee_idx[nxt] != i:
                continue
            used[i] = True
            path.append(y)
            dfs(y, used, k + 1, nxt + 1, path)
        else:
            used[i] = True
            path.append(y)
            dfs(y, used, k + 1, nxt, path)
        path.pop()
        used[i] = False


dfs(a, [False] * m, 0, 0, [a])
print(f"  valid walks: {count}; example: {' '.join(L(t, x) for x in example)}")
claim(count > 0, "Lee problem solvable")
print(" P10 delivery (closed, open)")
for t in U[10]:
    show(t, f"postman={t.postman()}")

print("\nALL CHECKS PASSED" if ok else "\nSOME CHECKS FAILED")
