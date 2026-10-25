#!/usr/bin/env python3
"""Recompute every answer printed in the Pancake flips facilitator guide.

Written independently of the student-page checker. Stacks are tuples read
from the top; the sorted stack is (1, 2, ..., n). With dark sides, a negative
number means the dark side faces UP (wrong), positive means down (right).
A flip k turns over the top k pancakes as one block.

The stacks below are the ones printed on the FINAL student PDFs
(plans/topic-scouting/drafts/pancake-flips/*.pdf), read from the rendered
pages and the generator in src/gen.py.

Run: python3 check_guide.py   (prints a report; every assert must pass)
"""
from collections import deque, Counter
from itertools import permutations, product


# ------------------------------------------------------------ basic moves

def flip(s, k):
    return tuple(reversed(s[:k])) + s[k:]


def bflip(s, k):
    return tuple(-x for x in reversed(s[:k])) + s[k:]


def dist_table(n, burnt=False):
    goal = tuple(range(1, n + 1))
    d = {goal: 0}
    q = deque([goal])
    ks = range(1, n + 1) if burnt else range(2, n + 1)
    f = bflip if burnt else flip
    while q:
        s = q.popleft()
        for k in ks:
            t = f(s, k)
            if t not in d:
                d[t] = d[s] + 1
                q.append(t)
    return d


U = {n: dist_table(n) for n in range(1, 8)}
B = {n: dist_table(n, True) for n in range(1, 7)}


def needb(s):
    return B[len(s)][tuple(s)]


def needu(s):
    return U[len(s)][tuple(s)]


def shortest(s, burnt=False):
    """All shortest flip sequences (lists of k) sorting s."""
    d = (B if burnt else U)[len(s)]
    f = bflip if burnt else flip
    ks = range(1, len(s) + 1) if burnt else range(2, len(s) + 1)
    out = []

    def go(t, path):
        if d[t] == 0:
            out.append(path)
            return
        for k in ks:
            u = f(t, k)
            if d[u] == d[t] - 1:
                go(u, path + [k])
    go(tuple(s), [])
    return out


def breaks(s):
    n = len(s)
    t = list(s) + [n + 1]
    return sum(1 for a, b in zip(t, t[1:]) if abs(a - b) != 1)


def code(s):
    return " ".join(str(x) for x in s)


def bcode(s):
    # dark side up marked with ^
    return " ".join(f"{abs(x)}{'^' if x < 0 else ''}" for x in s)


# ------------------------------------------------------------ general facts

print("== General facts")
for n in range(2, 8):
    d = U[n]
    mx = max(d.values())
    cnt = Counter(d.values())
    worst = sorted(s for s, v in d.items() if v == mx)
    # breaks lower bound
    assert all(breaks(s) <= v for s, v in d.items())
    print(f"n={n}: max {mx}; distribution {sorted(cnt.items())}; worst count {len(worst)}")
assert [max(U[n].values()) for n in range(2, 8)] == [1, 3, 4, 5, 7, 8]
assert sorted(s for s, v in U[3].items() if v == 3) == [(1, 3, 2)]
assert sorted(s for s, v in U[4].items() if v == 4) == sorted([(4, 2, 3, 1), (2, 4, 1, 3), (3, 1, 4, 2)])
assert sorted(s for s, v in U[6].items() if v == 7) == sorted([(4, 6, 2, 5, 1, 3), (5, 3, 6, 1, 4, 2)])
print("burnt max for n=1..6:", [max(B[n].values()) for n in range(1, 7)])
assert [max(B[n].values()) for n in range(1, 6)] == [1, 4, 6, 8, 10]

# flips undo themselves
for n in range(1, 7):
    for s in permutations(range(1, n + 1)):
        for k in range(1, n + 1):
            assert flip(flip(s, k), k) == s
for s in B[4]:
    for k in range(1, 5):
        assert bflip(bflip(s, k), k) == s
print("every flip undoes itself (plain n<=6, dark sides n=4): ok")

# a flip changes at most one adjacency (the one at the spatula), so breaks
# change by at most 1
for n in range(2, 8):
    for s in U[n]:
        for k in range(2, n + 1):
            assert abs(breaks(flip(s, k)) - breaks(s)) <= 1
print("one flip changes the break count by at most 1 (n<=7): ok")

# breaks = 0 exactly when sorted
for n in range(1, 8):
    for s in U[n]:
        assert (breaks(s) == 0) == (s == tuple(range(1, n + 1)))
print("0 breaks <=> sorted (n<=7): ok")


def method(s):
    """Biggest pancake not yet in place: to the top (if not there), then down."""
    s = tuple(s)
    n = len(s)
    flips = []
    for size in range(n, 1, -1):
        pos = s.index(size)
        if pos == size - 1:
            continue
        if pos != 0:
            s = flip(s, pos + 1)
            flips.append(pos + 1)
        s = flip(s, size)
        flips.append(size)
    assert s == tuple(range(1, n + 1))
    return flips


def method_noskip(s):
    """Always two flips (to top, then down) for sizes n..2, even if useless."""
    s = tuple(s)
    n = len(s)
    c = 0
    for size in range(n, 1, -1):
        pos = s.index(size)
        s = flip(s, pos + 1) if pos + 1 >= 2 else s
        c += 1
        s = flip(s, size)
        c += 1
    assert s == tuple(range(1, n + 1))
    return c


print("== Two-flips-per-pancake method")
for n in range(2, 8):
    w = max(len(method(s)) for s in U[n])
    assert w == 2 * n - 3, (n, w)
    print(f"n={n}: method worst {w} = 2n-3; never-skip version always {2 * (n - 1)}")
ex6 = [s for s in U[6] if len(method(s)) == 9]
print("six-stacks where the method uses 9 flips:", len(ex6), "e.g.", code(ex6[0]),
      "fewest", needu(ex6[0]), "method flips", method(ex6[0]))
print("formula 2n-3: six ->", 2 * 6 - 3, " ten ->", 2 * 10 - 3, " twenty ->", 2 * 20 - 3)
print("formula 2n-2: six ->", 10, " ten ->", 18, " twenty ->", 38)


def bmethod(s):
    """Dark sides: biggest not in place to top, make its dark side face up,
    flip it down. Last pancake: turn over if dark up."""
    s = tuple(s)
    n = len(s)
    c = 0
    for size in range(n, 1, -1):
        if s[size - 1] == size:
            continue
        pos = [abs(x) for x in s].index(size)
        if pos != 0:
            s = bflip(s, pos + 1)
            c += 1
        if s[0] > 0:  # dark side down while on top: turn it over alone
            s = bflip(s, 1)
            c += 1
        s = bflip(s, size)
        c += 1
    if s[0] < 0:
        s = bflip(s, 1)
        c += 1
    assert s == tuple(range(1, n + 1)), s
    return c


print("== Dark-side method")
for n in range(1, 7):
    w = max(bmethod(s) for s in B[n])
    print(f"n={n}: simple method worst {w} (3n-2 = {3 * n - 2}); true worst {max(B[n].values())}")
    assert w == 3 * n - 2
assert max(B[6].values()) == 12

# ------------------------------------------------------------ launch choice

print("== Launch stack")
task_stacks = set()
# K-1
task_stacks |= set(permutations((1, 2, 3)))                       # K-1 P1, 2-3 P2
task_stacks |= {(4, 1, 2, 3), (2, 3, 4, 1), (3, 4, 2, 1), (1, 2, 4, 3)}   # K-1 P2
task_stacks |= {s for s in U[4] if U[4][s] == 1}                  # K-1 P3 answers
task_stacks |= {(4, 2, 3, 1), (2, 1, 4, 3), (2, 4, 1, 3), (3, 1, 4, 2)}   # K-1 P4
# 2-3
task_stacks |= {(2, 3, 4, 1), (3, 4, 1, 2), (5, 4, 3, 2, 1), (5, 1, 2, 3, 4), (4, 5, 1, 2, 3), (1, 2, 3, 5, 4)}
task_stacks |= {(6, 5, 4, 3, 2, 1), (3, 6, 1, 5, 2, 4), (1, 2, 3, 4, 6, 5), (5, 2, 6, 3, 1, 4)}
# 4-5
task_stacks |= {(3, 2, 1, 5, 4), (2, 1, 4, 3, 6, 5), (2, 1, 5, 3, 4), (3, 5, 2, 1, 4), (4, 6, 2, 5, 1, 3)}
task_stacks |= {s for s in U[5] if U[5][s] == 5}                  # 4-5 P5 answers
LAUNCH = (4, 3, 1, 2, 5)
print("launch", code(LAUNCH), "in a task?", LAUNCH in task_stacks, "fewest", needu(LAUNCH),
      "breaks", breaks(LAUNCH), "shortest", shortest(LAUNCH))
assert LAUNCH not in task_stacks
seq = [LAUNCH]
for k in (4, 2):
    seq.append(flip(seq[-1], k))
print("launch run (flip 4, flip 2):", " -> ".join(code(s) for s in seq))
assert seq[-1] == (1, 2, 3, 4, 5)
for s in seq:
    assert s not in task_stacks
# a legal flip that is not a sorting step, shown before the run
print("demo of one legal flip from the launch stack: flip 3 ->", code(flip(LAUNCH, 3)),
      "(task?", flip(LAUNCH, 3) in task_stacks, ")")
# every four-pancake sort ends through a one-flip stack (a K-1 P3 answer),
# which is why the launch uses five pancakes
for s in U[4]:
    if U[4][s] >= 1:
        for p in shortest(s):
            t = s
            for k in p[:-1]:
                t = flip(t, k)
            assert U[4][t] == 1
print("every complete four-stack sort passes through a K-1 P3 answer: ok")

BDEMO = (2, -1, 3)
print("dark-side demo", bcode(BDEMO), "flip 2 ->", bcode(bflip(BDEMO, 2)),
      "(fewest from start", needb(BDEMO), ", from result", needb(bflip(BDEMO, 2)), ")")
assert bflip(BDEMO, 2) == (1, -2, 3)

# ------------------------------------------------------------ K-1

print("== K-1")
p1 = {code(s): needu(s) for s in permutations((1, 2, 3))}
print("P1 (all six of 1,2,3):", p1)
assert [s for s, v in p1.items() if v == 3] == ["1 3 2"]
print("   1 3 2 shortest:", shortest((1, 3, 2)))
for s in [(4, 1, 2, 3), (2, 3, 4, 1), (3, 4, 2, 1), (1, 2, 4, 3)]:
    print("P2", code(s), "fewest", needu(s), "shortest", shortest(s))
one = sorted(s for s in U[4] if U[4][s] == 1)
print("P3 one-flip stacks:", [code(s) for s in one])
assert one == sorted([(2, 1, 3, 4), (3, 2, 1, 4), (4, 3, 2, 1)])
for s in [(4, 2, 3, 1), (2, 1, 4, 3), (2, 4, 1, 3), (3, 1, 4, 2)]:
    sh = shortest(s)
    print("P4", code(s), "fewest", needu(s), "breaks", breaks(s), "#shortest", len(sh), sh[:4])
for s in [(-1, 2), (-2, -1), (-2, 1), (2, 1)]:
    print("P5", bcode(s), "fewest", needb(s), "shortest", shortest(s, True))
two = {bcode(s): v for s, v in B[2].items()}
print("all dark-side stacks of 2:", two)
assert [s for s, v in B[2].items() if v == 4] == [(-1, -2)]
print("   P6 answer 1^ 2^ shortest:", shortest((-1, -2), True))

# ------------------------------------------------------------ 2-3

print("== Grades 2-3")
for s in [(2, 3, 4, 1), (3, 4, 1, 2), (5, 4, 3, 2, 1), (5, 1, 2, 3, 4), (4, 5, 1, 2, 3), (1, 2, 3, 5, 4)]:
    print("P1", code(s), "fewest", needu(s), "shortest", shortest(s))
print("P2: 1 3 2 needs", needu((1, 3, 2)), "; one flip from 1 3 2 gives",
      [code(flip((1, 3, 2), k)) for k in (2, 3)], "each needing",
      [needu(flip((1, 3, 2), k)) for k in (2, 3)])
for s in [(6, 5, 4, 3, 2, 1), (3, 6, 1, 5, 2, 4), (1, 2, 3, 4, 6, 5), (5, 2, 6, 3, 1, 4)]:
    sh = shortest(s)
    print("P3", code(s), "fewest", needu(s), "breaks", breaks(s), "#shortest", len(sh), sh[:3],
          "method uses", len(method(s)), method(s))
four = sorted(s for s in U[4] if U[4][s] == 4)
print("P5 four-stacks needing 4:", [code(s) for s in four])
layers = Counter(U[4].values())
print("   four-stacks by fewest flips:", sorted(layers.items()))
for k in range(4):
    print(f"   need {k}:", [code(s) for s in sorted(U[4]) if U[4][s] == k])
for s in [(-1, 2), (-2, -1), (-2, 1), (2, 1)]:
    print("P6", bcode(s), "fewest", needb(s))
for s in [(-3, 1, 2), (3, 1, 2), (3, 2, 1), (-1, -2, -3)]:
    sh = shortest(s, True)
    print("P8", bcode(s), "fewest", needb(s), "#shortest", len(sh), sh[:3])

# ------------------------------------------------------------ 4-5

print("== Grades 4-5")
for s in [(5, 1, 2, 3, 4), (4, 5, 1, 2, 3), (1, 2, 3, 5, 4), (3, 2, 1, 5, 4), (2, 1, 4, 3, 6, 5)]:
    sh = shortest(s)
    print("P1", code(s), "fewest", needu(s), "breaks", breaks(s), "#shortest", len(sh), sh[:3])
print("P3 example 2 1 5 3 4: breaks", breaks((2, 1, 5, 3, 4)), "fewest", needu((2, 1, 5, 3, 4)))
s = (3, 5, 2, 1, 4)
print("P3 task 3 5 2 1 4: breaks", breaks(s), "fewest", needu(s), "shortest", shortest(s))
run = [s]
for k in shortest(s)[0]:
    run.append(flip(run[-1], k))
print("   run:", " -> ".join(code(t) for t in run), " breaks:", [breaks(t) for t in run])
# P4: neighbour argument for 4 2 3 1
for s in four:
    nb = {code(flip(s, k)): (needu(flip(s, k)), breaks(flip(s, k))) for k in (2, 3, 4)}
    print("P4", code(s), "breaks", breaks(s), "neighbours (fewest, breaks):", nb)
w5 = sorted(s for s in U[5] if U[5][s] == 5)
by_b = Counter(breaks(s) for s in w5)
print("P5: max for five =", max(U[5].values()), "; stacks needing 5:", len(w5), "by breaks", sorted(by_b.items()))
print("   five-break stacks:", [code(s) for s in w5 if breaks(s) == 5])
print("   fewer-break stacks needing 5:", [(code(s), breaks(s)) for s in w5 if breaks(s) < 5])
assert all(U[5][s] == 5 for s in U[5] if breaks(s) == 5)
# P6: 4 6 2 5 1 3
s = (4, 6, 2, 5, 1, 3)
print("P6", code(s), "breaks", breaks(s), "fewest", needu(s))
# tree of break-removing flips
seen = set()
dead = []
stack = [s]
while stack:
    t = stack.pop()
    if t in seen:
        continue
    seen.add(t)
    kids = [flip(t, k) for k in range(2, 7) if breaks(flip(t, k)) == breaks(t) - 1]
    if not kids and breaks(t) > 0:
        dead.append(t)
    stack.extend(kids)
print("   positions reachable by break-removing flips:", len(seen), "dead ends:", len(dead),
      [ (code(t), breaks(t)) for t in sorted(dead)])
assert (1, 2, 3, 4, 5, 6) not in seen
first = [(k, code(flip(s, k)), breaks(flip(s, k))) for k in range(2, 7)]
print("   first flips (k, result, breaks):", first)
print("   shortest 7:", shortest(s)[:3], "count", len(shortest(s)))
for s in [(-3, 1, 2), (1, 2, -3), (3, 1, 2), (-1, -2, 3), (3, 2, 1)]:
    sh = shortest(s, True)
    print("P7", bcode(s), "fewest", needb(s), "#shortest", len(sh), sh[:3])
w3 = sorted(s for s, v in B[3].items() if v == 6)
print("P8 burnt three-stacks needing 6:", [bcode(s) for s in w3])
assert sorted(w3) == sorted([(1, -2, -3), (-1, -2, -3)])
print("   burnt three-stacks by fewest:", sorted(Counter(B[3].values()).items()))
print("P9: simple method 3n-2 for six =", 3 * 6 - 2, "; true worst for six =", max(B[6].values()))

# ------------------------------------------------------------ extra claims used in the guide

print("== Extra claims")
def run(s, ks, f=flip):
    out = [tuple(s)]
    for k in ks:
        out.append(f(out[-1], k))
    return out

r = run((4, 6, 2, 5, 1, 3), [2, 3, 4, 2, 6, 3, 2])
print("P6 seven-flip sort:", " -> ".join(code(t) for t in r))
assert r[-1] == tuple(range(1, 7))
# 4-break worst five-stacks: does every first flip keep 4 breaks?
for s in w5:
    if breaks(s) == 4:
        firsts = [breaks(flip(s, k)) for k in range(2, 6)]
        print("   4-break worst", code(s), "first-flip breaks", firsts,
              "-> simple 1+4 argument" if min(firsts) >= 4 else "")
s = (1, 3, 2, 5, 4)
print("   1 3 2 5 4 first-flip breaks", [breaks(flip(s, k)) for k in range(2, 6)])
# outward layers from 1 2 3 4, generated by flipping
lay = [[(1, 2, 3, 4)]]
seen = {(1, 2, 3, 4)}
for depth in range(1, 5):
    nxt = []
    cand = 0
    for t in lay[-1]:
        for k in (2, 3, 4):
            u = flip(t, k)
            if u not in seen:
                seen.add(u)
                nxt.append(u)
    lay.append(nxt)
    print(f"   layer {depth}:", [code(t) for t in nxt])
assert [len(x) for x in lay] == [1, 3, 6, 11, 3]
# 4 2 3 1: only flip 4 removes a break; from 1 3 2 4 none does
s = (4, 2, 3, 1)
print("   4 2 3 1 first flips:", [(k, code(flip(s, k)), breaks(flip(s, k))) for k in (2, 3, 4)])
t = (1, 3, 2, 4)
print("   1 3 2 4 flips:", [(k, code(flip(t, k)), breaks(flip(t, k))) for k in (2, 3, 4)])
# four-stacks with 4 breaks
print("   four-stacks with 4 breaks:", [code(x) for x in sorted(U[4]) if breaks(x) == 4])
# 2-3 P2 / K-1 P1: three-stacks one flip from sorted
print("   three-stacks one flip from sorted:", [code(x) for x in sorted(U[3]) if U[3][x] == 1])
# dark-side two-stack layers
for k in range(5):
    print(f"   dark two-stacks needing {k}:", [bcode(x) for x in sorted(B[2]) if B[2][x] == k])
# improved method for six: place 6 with <=2 flips, then a five-stack needs <=5
print("   improved bound for six: 2 + max five =", 2 + max(U[5].values()), "; true max six =", max(U[6].values()))
print("   improved bound for twenty using five:", 2 * 15 + 5)
# launch: the full worked visual
print("   launch visual:", " -> ".join(code(t) for t in run(LAUNCH, [4, 2])))
# method example run on 2 6 5 1 3 4
print("   method on 2 6 5 1 3 4:", method((2, 6, 5, 1, 3, 4)))
print("   method on P3 stacks 3 6 1 5 2 4 / 5 2 6 3 1 4:", len(method((3, 6, 1, 5, 2, 4))), len(method((5, 2, 6, 3, 1, 4))))
# K-1 P4 solutions
for s, ks in [((4, 2, 3, 1), [4, 2, 3, 2]), ((2, 1, 4, 3), [3, 4, 3]), ((2, 4, 1, 3), [2, 4, 3, 2]), ((3, 1, 4, 2), [2, 3, 4, 2])]:
    r = run(s, ks)
    assert r[-1] == (1, 2, 3, 4) and len(ks) == needu(s)
    print("   K-1 P4", code(s), "flips", ks, ":", " -> ".join(code(t) for t in r))
# dark-side sample solutions printed in the guide
for s, ks in [((-1, 2), [1]), ((-2, -1), [2]), ((-2, 1), [2, 1]), ((2, 1), [1, 2, 1]), ((-1, -2), [1, 2, 1, 2]),
              ((-3, 1, 2), [3, 2]), ((3, 1, 2), [1, 3, 2]), ((3, 2, 1), [2, 3, 2, 3, 2]),
              ((-1, -2, -3), [2, 3, 2, 3, 2, 3]), ((1, 2, -3), [3, 1, 3]), ((-1, -2, 3), [1, 2, 1, 2]),
              ((1, -2, -3), shortest((1, -2, -3), True)[0])]:
    r = run(s, ks, bflip)
    assert r[-1] == tuple(range(1, len(s) + 1)) and len(ks) == needb(s), (s, ks)
    print("   dark", bcode(s), "flips", ks, ":", " -> ".join(bcode(t) for t in r))

# the break-removing tree for 4 6 2 5 1 3 exactly as printed in the guide (4-5 Problem 6)
def tree(t, k=None, depth=0, out=None):
    out = [] if out is None else out
    kids = [(j, flip(t, j)) for j in range(2, len(t) + 1) if breaks(flip(t, j)) == breaks(t) - 1]
    out.append((depth, k, code(t), breaks(t), not kids))
    for j, u in kids:
        tree(u, j, depth + 1, out)
    return out
T = tree((4, 6, 2, 5, 1, 3))
PRINTED = [(0, None, "4 6 2 5 1 3", 6, False), (1, 3, "2 6 4 5 1 3", 5, False),
           (2, 4, "5 4 6 2 1 3", 4, False), (3, 2, "4 5 6 2 1 3", 3, False), (4, 5, "1 2 6 5 4 3", 2, True),
           (2, 5, "1 5 4 6 2 3", 4, False), (3, 4, "6 4 5 1 2 3", 3, False), (4, 6, "3 2 1 5 4 6", 2, True),
           (1, 5, "1 5 2 6 4 3", 5, False), (2, 2, "5 1 2 6 4 3", 4, False), (3, 3, "2 1 5 6 4 3", 3, True),
           (3, 4, "6 2 1 5 4 3", 3, False), (4, 3, "1 2 6 5 4 3", 2, True), (4, 6, "3 4 5 1 2 6", 2, True)]
assert T == PRINTED, T
print("   P6 printed break tree matches:", len(T), "nodes,", sum(1 for x in T if x[4]), "stuck ends")
print("EXTRA CHECKS PASSED")

# ------------------------------------------------------------ revision checks (final/ guide)
# Claims added or reworded in the revision, after the review and the materials file.

print("== Revision checks")
# M1: five never needs six (computer), so 7 always suffices for six; 4 6 2 5 1 3 needs 7,
# provable by hand with breaks and the break-removing tree (4-5 Problem 6).
assert max(U[5].values()) == 5 and 2 + max(U[5].values()) == 7 == max(U[6].values())
assert needu((4, 6, 2, 5, 1, 3)) == 7 and breaks((4, 6, 2, 5, 1, 3)) == 6
print("   seven always suffice for six (2 + max five = 7 = true max); 4 6 2 5 1 3 needs 7: ok")

# S1: the launch run and the printed example each flip the biggest pancake on top down
# into its place, i.e. they are exactly the two-flips-per-pancake method's own flips.
assert method(LAUNCH) == [4, 2] and method((3, 1, 2)) == [3, 2]
for st, ks in [(LAUNCH, [4, 2]), ((3, 1, 2), [3, 2])]:
    t = st
    for k in ks:
        top = t[0]
        biggest_unplaced = max(x for x in t if t[x - 1] != x)
        assert top == biggest_unplaced and k == top, (st, t, k)
        t = flip(t, k)
    assert t == tuple(range(1, len(st) + 1))
print("   launch 4 3 1 2 5 (flips 4 2) and printed example 3 1 2 (flips 3 2) are the method's flips: ok")

# S4: the K-1 recording demo uses the printed example 3 1 2, which needs 2 (already on the page).
assert needu((3, 1, 2)) == 2 and shortest((3, 1, 2)) == [[3, 2]]
print("   K-1 recording demo 3 1 2: fewest 2, only by 3 2 (the printed run): ok")

# S5 prerequisites: arithmetic the pages ask for.
assert 2 * 20 - 3 == 37 and 2 * (10 - 1) == 18 and 2 * 10 - 3 == 17
print("   prerequisites: 2*20-3 = 37; doubling to about 20 (2*9 = 18 for ten): ok")

# S7: sticky-note columns 1, 2, 3 flips hold 3, 6 and 11 notes; 3 stacks are never made.
cols = [sum(1 for v in U[4].values() if v == k) for k in (1, 2, 3)]
assert cols == [3, 6, 11] and 24 - 1 - sum(cols) == 3
print("   sticky-note columns:", cols, "; never made:", 24 - 1 - sum(cols), ": ok")

# M10: for four pancakes the plate is 5; with the example's plate 6 a bottom 4 would wrongly count.
def breaks_plate(st, plate):
    t = list(st) + [plate]
    return sum(1 for a, b in zip(t, t[1:]) if abs(a - b) != 1)
assert all(breaks_plate(st, 5) == breaks(st) for st in U[4])
wrong = [code(st) for st in sorted(U[4]) if breaks_plate(st, 6) != breaks(st)]
assert all(st.endswith("4") for st in wrong) and len(wrong) == 6
assert sorted(code(st) for st in U[4] if breaks(st) == 4) == ["2 4 1 3", "3 1 4 2"]
assert breaks_plate((1, 2, 3, 4), 6) == 1   # the sorted stack would show a break on plate 6
print("   plate 5 for four; plate 6 miscounts exactly the six stacks with 4 at the bottom:", wrong, ": ok")

# M11: number of answers for the three-blank problems.
assert sum(1 for v in B[2].values() if v == 4) == 1          # 2-3 P7, K-1 P6: one answer
assert sum(1 for v in B[3].values() if v == 6) == 2          # 4-5 P8: two answers
print("   2-3 P7 / K-1 P6 one answer; 4-5 P8 two answers: ok")

# Materials file: sizes, counts and preparation arithmetic quoted in the guide.
DIAMETERS_MM = [40, 50, 60, 70, 80, 90]                     # materials page 1, measured by its checker
assert all(b - a >= 10 for a, b in zip(DIAMETERS_MM, DIAMETERS_MM[1:]))
GROUP = {"K-1": 4, "2-3": 4, "4-5": 3}                      # worksheet-workflow/context.md
pairs = sum(c // 2 for c in GROUP.values())
copies = pairs + 1                                          # plus the launch set (to the 4-5 referee)
assert pairs == 5 and copies == 6
k1_pairs = GROUP["K-1"] // 2
assert 12 * k1_pairs == 24
CARD_MM, FOAM_MM = (0.23, 0.30), 2.0                        # card stock 65-110 lb cover
card_stack = [6 * c for c in CARD_MM]
foam_stack = [6 * (FOAM_MM + c) for c in CARD_MM]
print(f"   six card pancakes {card_stack[0]:.1f}-{card_stack[1]:.1f} mm tall (about 2); "
      f"foam-backed {foam_stack[0]:.1f}-{foam_stack[1]:.1f} mm (about 14)")
assert all(1.2 <= h <= 2.0 for h in card_stack) and all(13.0 <= h <= 14.5 for h in foam_stack)
assert 25 + 5 == 30
print(f"   {pairs} pairs + launch = {copies} copies of materials page 1; {12 * k1_pairs} K-1 counters; "
      "preparation 25 + 5 = 30 min (+15 foam): ok")
# The four-stack table, now printed in the shared section of facilitator.tex: parse and compare.
import os, re
tex = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "facilitator.tex")).read()
tab = tex[tex.index("All 24 stacks of four"):]
tab = tab[tab.index(r"\midrule"):tab.index(r"\end{tabular}")]
rows = {}
for line in tab.split(r"\\"):
    m = re.match(r"\s*(?:\\midrule)?\s*(\d)\s*&(.*)", line, re.S)
    if m:
        stacks = re.findall(r"\$([\d\\, ]+)\$", m.group(2))
        rows[int(m.group(1))] = sorted(tuple(int(x) for x in re.findall(r"\d", st)) for st in stacks)
for k in range(5):
    assert rows[k] == sorted(st for st in U[4] if U[4][st] == k), k
print("   printed four-stack table matches the layers 1, 3, 6, 11, 3 stack for stack: ok")
print("REVISION CHECKS PASSED")

print("ALL CHECKS PASSED")
