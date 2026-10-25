"""Exhaustive checks for the Week 98 K-1 pages (two-neighbour growth)."""
from itertools import combinations, permutations

def nbrs(r, c, R, C):
    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
        rr, cc = r+dr, c+dc
        if 1 <= rr <= R and 1 <= cc <= C:
            yield (rr, cc)

def grow(seeds, R, C):
    filled = set(seeds)
    changed = True
    while changed:
        changed = False
        for r in range(1, R+1):
            for c in range(1, C+1):
                if (r,c) not in filled and sum((n in filled) for n in nbrs(r,c,R,C)) >= 2:
                    filled.add((r,c)); changed = True
    return filled

def fills(seeds, R, C):
    return len(grow(seeds, R, C)) == R*C

def cells(R, C):
    return [(r,c) for r in range(1,R+1) for c in range(1,C+1)]

def fewest(R, C):
    k = 1
    while True:
        good = [s for s in combinations(cells(R,C), k) if fills(s,R,C)]
        if good:
            from math import comb
            return k, len(good), comb(R*C, k), good
        k += 1

print("== fewest seeds and how many starts of that size fill ==")
for R, C in [(2,2),(3,3),(4,4),(5,5),(1,3),(1,4),(1,5),(1,6),(2,3),(2,4),(2,5)]:
    k, n, tot, good = fewest(R, C)
    extra = good if n <= 10 else ""
    print(f"{R}x{C}: fewest {k}, {n} of {tot} fill", extra)

print("\n== P1: 2x2, every placement of 2 seeds ==")
for s in combinations(cells(2,2), 2):
    print(s, "fills" if fills(s,2,2) else f"stuck at {len(grow(s,2,2))}")
print("1 seed on 2x2 finishes:", {len(grow((c,),2,2)) for c in cells(2,2)})
print("3 seeds on 2x2 all fill:", all(fills(s,2,2) for s in combinations(cells(2,2),3)))

print("\n== 3x3 two seeds: finishes ==")
from collections import Counter
print(Counter(len(grow(s,3,3)) for s in combinations(cells(3,3),2)))

print("\n== Rule pictures (3x3 patches) ==")
import gen as _g
for name, (s, t) in [("check", _g.RULE_OK), ("cross", _g.RULE_NO)]:
    side = sum(n in s for n in nbrs(*t, 3, 3))
    near = sum(((t[0]+dr, t[1]+dc) in s) for dr in (-1,0,1) for dc in (-1,0,1) if (dr,dc)!=(0,0))
    print(name, s, "target", t, "side neighbours", side, "side+corner", near,
          "LEGAL" if side >= 2 else "not legal")
assert sum(n in _g.RULE_OK[0] for n in nbrs(*_g.RULE_OK[1],3,3)) >= 3   # shows 'or more'
assert sum(n in _g.RULE_NO[0] for n in nbrs(*_g.RULE_NO[1],3,3)) == 1

print("\n== Stuck-check boards ==")
def show(f, R, C, seeds=()):
    for r in range(1,R+1):
        print("   ", "".join(("S" if (r,c) in seeds else "#") if (r,c) in f else "." for c in range(1,C+1)))
def is_finish(s, R, C):
    return len(grow(s,R,C)) == len(set(s))

def removable(s, R, C):
    return [x for x in s if fills([y for y in s if y != x], R, C)]

print("\n== 3x3 filling starts by number of single removable seeds ==")
for k in (4, 5):
    tab = Counter()
    ex = {}
    for s in combinations(cells(3,3), k):
        if fills(s,3,3):
            m = len(removable(s,3,3))
            tab[m] += 1
            ex.setdefault(m, []).append(s)
    print(k, "seeds:", dict(tab))
    for m in sorted(ex):
        print("   removable", m, "e.g.", ex[m][:6])

def routes(s, R, C, path=()):
    """All maximal take-away routes; yields (path, end)."""
    r = removable(s, R, C)
    if not r:
        yield path, tuple(sorted(s))
        return
    for x in r:
        yield from routes(tuple(y for y in s if y != x), R, C, path + (x,))

print("\n== Problem 8 take-away boards: which single seeds can come off ==")
import gen
for name, (R, C, s) in zip(("2x2 bent three", "four corners", "three corners + centre", "middle of each side"), gen.TAKE_ONE):
    assert fills(s, R, C), name
    print(name, "fills; removable:", removable(s, R, C))
    for x in s:
        rest = [y for y in s if y != x]
        print("    without", x, "->", "fills" if fills(rest,R,C) else f"stuck at {len(grow(rest,R,C))}")

print("\n== Problem 9 take-away routes ==")
for name, s in [("printed P9 start", gen.TAKE_ALL),
                ("plus", [(1,2),(2,1),(2,2),(2,3),(3,2)])]:
    ends = Counter()
    for path, end in routes(tuple(s), 3, 3):
        ends[end] += 1
    print(name)
    for end, n in ends.items():
        print("   ends with", len(end), "seeds", end, "via", n, "routes; removals from end:",
              [len(grow([y for y in end if y != x],3,3)) for x in end])

print("\n== Problem 2 'which can still grow' boards (printed counters) ==")
import gen  # the positions actually printed
for name, s in zip("ABCD", gen.STARTS):
    f = grow(s, 3, 3)
    print(name, "already stuck" if len(f) == len(s) else f"grows to {len(f)}" + (" (filled)" if len(f)==9 else ""))
    show(f, 3, 3, s)
    # squares a diagonal-counting child might wrongly add at the start
    wrong = [x for x in cells(3,3) if x not in s
             and sum(n in s for n in nbrs(*x,3,3)) < 2
             and sum(((x[0]+dr, x[1]+dc) in s) for dr in (-1,0,1) for dc in (-1,0,1) if (dr,dc)!=(0,0)) >= 2]
    print("    squares that touch 2+ counters only if corners count:", wrong)

print("\n== counter budget (seed colour <= 6, total <= 26 per pair) ==")
print("5x5 from 5 seeds: 5 seed + 20 grow; 4x4 from 6 seeds: 6 + 10; P9: 5 + 4; P8 biggest: 4 + 5")

print("\n== Problem 1: 6 placements, 6 record boards ==")
from math import comb
print("placements", comb(4,2))
