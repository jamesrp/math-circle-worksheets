"""Independent re-derivation of every answer printed in the Week 98 K-1 guide draft.

Boards and printed seeds come from parse_pages.py's JSON (the final student PDF),
so the answers are keyed to the pages as printed. Rule: an empty square is added
when at least two side-neighbours are filled; no outside squares; counters stay.

Usage:
  python3 -I parse_pages.py k-1.pdf > pages.json
  python3 -I check_answers.py pages.json
"""
import itertools
import json
import math
import sys


def nbrs(r, c, R, C):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = r + dr, c + dc
        if 1 <= rr <= R and 1 <= cc <= C:
            yield rr, cc


def closure(seeds, R, C, exact_two=False):
    """Finish of a complete run (one deterministic order)."""
    filled = set(seeds)
    changed = True
    while changed:
        changed = False
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if (r, c) in filled:
                    continue
                k = sum((n in filled) for n in nbrs(r, c, R, C))
                if (k == 2) if exact_two else (k >= 2):
                    filled.add((r, c))
                    changed = True
    return filled


def all_finishes(seeds, R, C):
    """Every finish over every complete growth order (DFS with memo)."""
    seen, finishes = set(), set()
    stack = [frozenset(seeds)]
    while stack:
        s = stack.pop()
        if s in seen:
            continue
        seen.add(s)
        moves = [(r, c) for r in range(1, R + 1) for c in range(1, C + 1)
                 if (r, c) not in s and sum((n in s) for n in nbrs(r, c, R, C)) >= 2]
        if not moves:
            finishes.add(s)
        for m in moves:
            stack.append(s | {m})
    return finishes


def fills(seeds, R, C):
    return len(closure(seeds, R, C)) == R * C


def cells(R, C):
    return [(r, c) for r in range(1, R + 1) for c in range(1, C + 1)]


def minimum(R, C):
    for s in range(1, R * C + 1):
        sols = [set(x) for x in itertools.combinations(cells(R, C), s) if fills(x, R, C)]
        if sols:
            return s, sols
    return None


def single_removals(seeds, R, C):
    out = {}
    for x in sorted(seeds):
        rest = set(seeds) - {x}
        out[x] = len(closure(rest, R, C))
    return out


def removal_endings(seeds, R, C):
    """All endings of 'remove one seed at a time while it still fills'."""
    endings = {}
    def walk(s, path):
        nxt = [x for x in sorted(s) if fills(s - {x}, R, C)]
        if not nxt:
            endings.setdefault(frozenset(s), []).append(path)
            return
        for x in nxt:
            walk(s - {x}, path + [x])
    walk(frozenset(seeds), [])
    return endings


def main():
    pages = json.load(open(sys.argv[1]))
    ok = True

    def claim(label, cond):
        nonlocal ok
        ok &= bool(cond)
        print(("PASS " if cond else "FAIL ") + label)

    # Rule pictures (page 1): from the rendered page, check (2,2) with (1,2),(2,1),(2,3)
    check_k = sum(n in {(1, 2), (2, 1), (2, 3)} for n in nbrs(2, 2, 3, 3))
    cross_k = sum(n in {(1, 2), (3, 3)} for n in nbrs(2, 2, 3, 3))
    claim(f"page 1 check-mark target has {check_k} side-neighbours (guide: three)", check_k == 3)
    claim(f"page 1 cross target has {cross_k} side-neighbour (illegal)", cross_k == 1)

    # Launch 2x3 replay
    launch = {(1, 1), (2, 1), (2, 2)}
    f = closure(launch, 2, 3)
    claim(f"launch 2x3 finish {sorted(f)} has 4 squares; addition (1,2)", f == launch | {(1, 2)})
    claim("launch 2x3 has exactly one legal first addition", len(all_finishes(launch, 2, 3)) == 1)

    # Problem 1
    p1 = pages["1"]["boards"]
    R, C = p1[0]["rows"], p1[0]["cols"]
    starts = list(itertools.combinations(cells(R, C), 2))
    filling = [s for s in starts if fills(s, R, C)]
    print("P1 starts:", len(starts), "filling:", filling)
    claim("P1: 6 starts, exactly the two diagonals fill",
          len(starts) == 6 and sorted(filling) == [((1, 1), (2, 2)), ((1, 2), (2, 1))])
    claim("P1: side-by-side pairs never grow",
          all(len(closure(s, R, C)) == 2 for s in starts if s not in filling))
    claim("P1: page prints 6 record boards", sum(b["kind"] == "record" for b in p1) == 6)
    claim("P1: one seed never grows", all(len(closure({x}, R, C)) == 1 for x in cells(R, C)))

    # Problem 2
    guide_p2 = [4, 3, 6, 9]
    for b, g in zip(pages["2"]["boards"], guide_p2):
        seeds = {(r, c) for r, c, _ in b["seeds"]}
        fins = all_finishes(seeds, b["rows"], b["cols"])
        sizes = sorted(len(x) for x in fins)
        claim(f"P2 board at {b['top_left_mm']} seeds {sorted(seeds)}: finish sizes {sizes} "
              f"(guide {g}); finishes over all orders: {len(fins)}", sizes == [g])
        print("    finish:", sorted(next(iter(fins))))

    # Problems 3-5
    for pg, n in (("3", 3), ("4", 4), ("5", 5)):
        b = pages[pg]["boards"][0]
        R, C = b["rows"], b["cols"]
        claim(f"P{pg}: board is {R}x{C}", (R, C) == (n, n))
        diag = {(i, i) for i in range(1, n + 1)}
        anti = {(i, n + 1 - i) for i in range(1, n + 1)}
        claim(f"P{pg}: main and opposite diagonals fill", fills(diag, R, C) and fills(anti, R, C))
        # lower bound by exhaustive search of n-1 seeds
        cnt = sum(fills(x, R, C) for x in itertools.combinations(cells(R, C), n - 1))
        claim(f"P{pg}: no {n-1}-seed start fills (checked {math.comb(R*C, n-1)})", cnt == 0)
        nfill = sum(fills(x, R, C) for x in itertools.combinations(cells(R, C), n)) if n <= 4 else None
        if nfill is not None:
            print(f"    {n}-seed filling starts: {nfill} of {math.comb(R*C, n)}")
        # fence bound
        claim(f"P{pg}: perimeter {2*(R+C)} / 4 = {2*(R+C)/4}", math.ceil(2 * (R + C) / 4) == n)
    # counters: 5x5 from 5 seeds uses 20 growth counters
    claim("P5: 5x5 from 5 seeds uses 20 growth counters", 25 - 5 == 20)

    # Problem 6 strips
    guide_p6 = {3: (2, [{1, 3}]), 4: (3, [{1, 2, 4}, {1, 3, 4}]), 5: (3, [{1, 3, 5}]),
                6: (4, [{1, 2, 4, 6}, {1, 3, 4, 6}, {1, 3, 5, 6}])}
    for b in [b for b in pages["6"]["boards"] if b["kind"] == "working"]:
        L = b["cols"]
        m, sols = minimum(1, L)
        sol_cols = sorted(sorted(c for _, c in s) for s in sols)
        g = guide_p6[L]
        claim(f"P6 strip 1x{L}: min {m}, all minimum starts {sol_cols} (guide {g[0]}, "
              f"{sorted(sorted(s) for s in g[1])})",
              m == g[0] and sol_cols == sorted(sorted(s) for s in g[1]))
        claim(f"P6 strip 1x{L}: min equals floor(L/2)+1", m == L // 2 + 1)

    # Problem 7 two-wide boards
    guide_p7 = {3: (3, {(1, 1), (2, 2), (3, 1)}), 4: (3, {(1, 1), (2, 2), (4, 1)}),
                5: (4, {(1, 1), (2, 2), (4, 1), (5, 2)})}
    for b in [b for b in pages["7"]["boards"] if b["kind"] == "working"]:
        R, C = b["rows"], b["cols"]
        m, sols = minimum(R, C)
        g = guide_p7[R]
        claim(f"P7 board {R}x{C} at {b['top_left_mm']}: min {m} ({len(sols)} minimum starts); "
              f"guide {g[0]}; guide example fills: {fills(g[1], R, C)}",
              m == g[0] and fills(g[1], R, C) and len(g[1]) == m)
        claim(f"P7 {R}x{C}: fence bound ceil((r+2)/2) = {math.ceil((R+2)/2)}",
              math.ceil((R + 2) / 2) == m)
        # Does the guide example need a three-neighbour addition (exact-two misreading)?
        ex2 = len(closure(g[1], R, C, exact_two=True))
        print(f"    guide example under 'exactly two' misreading reaches {ex2} of {R*C}")

    # Problem 8
    guide_p8 = [{(1, 1)}, {(1, 1), (1, 3), (3, 1), (3, 3)}, {(1, 1), (2, 2)}, set()]
    for b, g in zip(pages["8"]["boards"], guide_p8):
        R, C = b["rows"], b["cols"]
        seeds = {(r, c) for r, c, _ in b["seeds"]}
        claim(f"P8 board {R}x{C} seeds {sorted(seeds)} fills as printed", fills(seeds, R, C))
        rem = single_removals(seeds, R, C)
        ring = {x for x, v in rem.items() if v == R * C}
        claim(f"P8 removable alone {sorted(ring)} (guide {sorted(g)}); finishes {rem}", ring == g)
        if len(seeds) == 4 and R == 3:
            twos = [p for p in itertools.combinations(sorted(seeds), 2)
                    if fills(seeds - set(p), R, C)]
            print("    pairs removable together:", twos)

    # Problem 9
    b = pages["9"]["boards"][0]
    R, C = b["rows"], b["cols"]
    seeds = {(r, c) for r, c, _ in b["seeds"]}
    first = sorted(x for x in seeds if fills(seeds - {x}, R, C))
    claim(f"P9 first removals {first} (guide (1,1),(1,2),(2,1))", first == [(1, 1), (1, 2), (2, 1)])
    ends = removal_endings(seeds, R, C)
    for e, paths in ends.items():
        print("    ending", sorted(e), "via", paths)
    claim("P9 exactly two endings: four seeds {(1,2),(1,3),(2,1),(3,1)} and three corners",
          set(ends) == {frozenset({(1, 2), (1, 3), (2, 1), (3, 1)}),
                        frozenset({(1, 1), (1, 3), (3, 1)})})
    four = frozenset({(1, 2), (1, 3), (2, 1), (3, 1)})
    print("    four-seed ending single removals:", single_removals(four, R, C))
    claim("P9 record boards printed: 2", sum(x["kind"] == "record" for x in pages["9"]["boards"]) == 2)

    # Counter budget per board (6 seed, 20 growth)
    print("Counter needs (seeds, growth) per printed-start board:")
    for pg in ("2", "8", "9"):
        for b in pages[pg]["boards"]:
            if b["kind"] != "working":
                continue
            seeds = {(r, c) for r, c, _ in b["seeds"]}
            f = closure(seeds, b["rows"], b["cols"])
            print(f"    page {pg} {b['rows']}x{b['cols']}: {len(seeds)} seeds, {len(f)-len(seeds)} growth")
    print("Seed counters to load whole page at once: P2 %d, P6 %d, P7 %d, P8 %d" % (
        sum(len(b["seeds"]) for b in pages["2"]["boards"]),
        2 + 3 + 3 + 4, 3 + 3 + 4,
        sum(len(b["seeds"]) for b in pages["8"]["boards"])))
    # Largest seed set a child could test with 6 seed counters on each hunt board
    print("ALL PASS" if ok else "SOME FAIL")


if __name__ == "__main__":
    main()
