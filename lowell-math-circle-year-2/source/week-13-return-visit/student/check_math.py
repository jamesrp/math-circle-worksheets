#!/usr/bin/env python3
"""Enumerate only the finite graphs printed in the packet; not a student guide."""
from collections import Counter
from itertools import combinations, product

def paths(edges, start, finish):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
    def walk(v, seen):
        if v == finish:
            return [tuple(seen)]
        return [p for w in adj.get(v, []) if w not in seen
                for p in walk(w, seen + [w])]
    return walk(start, [start])

def arrows(path):
    return set(zip(path, path[1:]))

def packing(edges, vertex_rule=False):
    pp = paths(edges, "S", "T")
    best = ()
    for k in range(len(pp) + 1):
        for chosen in combinations(pp, k):
            used = [arrows(p) for p in chosen]
            if any(used[i] & used[j] for i in range(k) for j in range(i)):
                continue
            if vertex_rule and any(set(chosen[i][1:-1]) & set(chosen[j][1:-1])
                                   for i in range(k) for j in range(i)):
                continue
            best = chosen
    return len(best), best

base = [("S", "A"), ("S", "B"), ("A", "H"), ("B", "H"),
        ("H", "C"), ("H", "D"), ("C", "T"), ("D", "T")]
for extra, expected in [(False, (2, 1)), (True, (2, 2))]:
    edges = base + ([("A", "C")] if extra else [])
    values = tuple(packing(edges, rule)[0] for rule in [False, True])
    assert values == expected, values
    print("Problem 1", "with A-C" if extra else "base", values)

paired = [("P", "A"), ("Q", "B"), ("A", "X"), ("B", "Y"),
          ("A", "C"), ("B", "C"), ("C", "D"), ("D", "X"), ("D", "Y")]
for finishes, expected in [(("X", "Y"), True), (("Y", "X"), False)]:
    options = list(product(paths(paired, "P", finishes[0]),
                           paths(paired, "Q", finishes[1])))
    feasible = [(p, q) for p, q in options if not arrows(p) & arrows(q)]
    assert bool(feasible) is expected
    print("Problem 2", finishes, "fits" if feasible else "impossible")

for ct in [3, 4]:
    capacities = {("S", "A"): 3, ("S", "B"): 2, ("A", "C"): 2,
                  ("B", "C"): 2, ("C", "T"): ct, ("A", "T"): 1}
    pp = paths(capacities, "S", "T")
    best, counts = -1, None
    for amounts in product(range(6), repeat=len(pp)):
        use = Counter()
        for p, n in zip(pp, amounts):
            for edge in arrows(p):
                use[edge] += n
        if all(use[e] <= c for e, c in capacities.items()) and sum(amounts) > best:
            best, counts = sum(amounts), amounts
    vertices = {v for e in capacities for v in e}
    middle = sorted(vertices - {"S", "T"})
    cuts = []
    for bits in product([False, True], repeat=len(middle)):
        side = {"S"} | {v for v, bit in zip(middle, bits) if bit}
        cut = {e for e in capacities if e[0] in side and e[1] not in side}
        cuts.append(sum(capacities[e] for e in cut))
    assert best == min(cuts) == ct + 1
    print("Problem 3", "C-T=" + str(ct), "packing=min cut=" + str(best),
          "path multiplicities=" + str(counts), "paths=" + str(pp))
