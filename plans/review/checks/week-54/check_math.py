#!/usr/bin/env python3
"""Independent mathematical checks for Week 54 (partitions, joining/splitting,
rows/columns). Written from the student pages and guide text; it does not
import or run the packet's own verify_math.py or check_answers.py.

Run: python3 check_math.py > out_check_math.txt
"""
import json
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path


def find_repo():
    here = Path(__file__).resolve().parent
    for p in [here, *here.parents]:
        if (p / "lowell-math-circle-year-2").is_dir():
            return p
    raise SystemExit("repository not found")


REPO = find_repo()
FAIL = []


def check(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


def key(c):
    return tuple(sorted(c, reverse=True))


@lru_cache(None)
def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        return ((),)
    out = []
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - first, first):
            out.append((first,) + rest)
    return tuple(out)


def is_odd(p):
    return all(x % 2 for x in p)


def is_distinct(p):
    return len(set(p)) == len(p)


def odd_parts(n):
    return [p for p in partitions(n) if is_odd(p)]


def distinct_parts(n):
    return [p for p in partitions(n) if is_distinct(p)]


def join_moves(state):
    """All states reachable by one legal join (two equal strips -> one)."""
    c = Counter(state)
    out = set()
    for s, m in c.items():
        if m >= 2:
            d = c.copy()
            d[s] -= 2
            d[2 * s] += 1
            out.add(key(d.elements()))
    return out


def split_moves(state):
    c = Counter(state)
    out = set()
    for s in c:
        if s % 2 == 0:
            d = c.copy()
            d[s] -= 1
            d[s // 2] += 2
            out.add(key(d.elements()))
    return out


def all_terminals(start, moves):
    """Explore every legal route; return (terminal states, number of states, longest strip seen)."""
    seen = {key(start)}
    stack = [key(start)]
    terms = set()
    longest = max(start) if start else 0
    while stack:
        s = stack.pop()
        longest = max(longest, max(s) if s else 0)
        nxt = moves(s)
        if not nxt:
            terms.add(s)
        for t in nxt:
            if t not in seen:
                seen.add(t)
                stack.append(t)
    return terms, len(seen), longest


def count_routes(start, moves):
    """Number of distinct move sequences (choice of which size to join/split) to a terminal state."""
    @lru_cache(None)
    def f(s):
        nxt = moves(s)
        if not nxt:
            return 1
        return sum(f(t) for t in nxt)
    return f(key(start))


def join_all(p):
    terms, _, _ = all_terminals(p, join_moves)
    assert len(terms) == 1
    return next(iter(terms))


def split_all(p):
    terms, _, _ = all_terminals(p, split_moves)
    assert len(terms) == 1
    return next(iter(terms))


def conjugate(p):
    p = key(p)
    return tuple(sum(1 for r in p if r > j) for j in range(p[0] if p else 0))


def fmt(p):
    return "(" + ",".join(map(str, p)) + ")"


def legal_route(seq):
    """Check that each consecutive state in a printed route is one legal join."""
    return all(key(b) in join_moves(key(a)) for a, b in zip(seq, seq[1:]))


def main():
    print("== Partition numbers ==")
    pn = [len(partitions(n)) for n in range(25)]
    print("p(0..24) =", pn)
    check(sum(pn) == 7338, f"guide p.8: '7,338 partitions through total 24' = sum p(0..24) = {sum(pn)}")

    print("\n== Problem 1 (p.1): every collection of 4 and of 5 ==")
    for n, boxes in ((4, 6), (5, 8)):
        cat = partitions(n)
        print(f"  {n}: {len(cat)} collections: {' '.join(map(fmt, cat))}; boxes printed {boxes}")
        check(len(cat) <= boxes, f"P1 total {n}: {len(cat)} collections fit in {boxes} boxes")
    check([fmt(p) for p in partitions(4)] == ["(4)", "(3,1)", "(2,2)", "(2,1,1)", "(1,1,1,1)"],
          "guide P1 key for 4 (5 collections)")
    check([fmt(p) for p in partitions(5)] == ["(5)", "(4,1)", "(3,2)", "(3,1,1)", "(2,2,1)", "(2,1,1,1)",
                                            "(1,1,1,1,1)"], "guide P1 key for 5 (7 collections)")
    # guide: largest 3 for total 5 leaves 2 as (2) or (1,1)
    check([p[1:] for p in partitions(5) if p[0] == 3] == [(2,), (1, 1)], "guide P1: largest 3 leaves (2) or (1,1)")
    # demo record and launch: partitions of 3
    print("  launch/demo total 3:", [fmt(p) for p in partitions(3)], "(non-task total)")

    print("\n== Problem 2 (p.2): only odd / all different for 6 and 7 ==")
    guide2 = {6: ([(5, 1), (3, 3), (3, 1, 1, 1), (1,) * 6], [(6,), (5, 1), (4, 2), (3, 2, 1)]),
              7: ([(7,), (5, 1, 1), (3, 3, 1), (3, 1, 1, 1, 1), (1,) * 7],
                  [(7,), (6, 1), (5, 2), (4, 3), (4, 2, 1)])}
    for n in (6, 7):
        o, d = odd_parts(n), distinct_parts(n)
        print(f"  {n}: odd {len(o)} {' '.join(map(fmt, o))} | distinct {len(d)} {' '.join(map(fmt, d))}")
        check(sorted(o) == sorted(guide2[n][0]) and sorted(d) == sorted(guide2[n][1]), f"guide P2 table, total {n}")
        check(max(len(o), len(d)) <= 6, f"P2 total {n} fits the 6 printed rows per column")
        print(f"    overlap: {[fmt(p) for p in o if p in d]}")
        print(f"    largest odd sizes: {sorted({p[0] for p in o}, reverse=True)}; "
              f"largest distinct sizes: {sorted({p[0] for p in d}, reverse=True)}")
    check(sorted({p[0] for p in distinct_parts(6)}, reverse=True) == [6, 5, 4, 3], "guide P2: largest distinct sizes for 6 are 6,5,4,3")
    check(sorted({p[0] for p in distinct_parts(7)}, reverse=True) == [7, 6, 5, 4], "guide P2: largest distinct sizes for 7 are 7,6,5,4")
    print("  note: largest distinct size 3 is impossible for 7 because 3+2+1 = 6 < 7;"
          " the guide's stated reason covers only largest <= 2 (2+1 = 3).")

    print("\n== Page 3 demo and Problem 3: join equal pairs until all sizes differ ==")
    demo = (3, 3, 1, 1, 1, 1)
    print("  demo legal first joins:", sorted(join_moves(demo), reverse=True))
    check((6, 1, 1, 1, 1) in join_moves(demo), "demo (3,3,1,1,1,1) -> join 3 and 3 -> (6,1,1,1,1)")
    print("  -> the demo input has two different legal first joins (3+3 and 1+1); the guide's P3 bridge says it 'has one legal join 3+3'")
    check(join_all(demo) == (6, 4), "demo ends at (6,4)")
    p3 = {(1,) * 9: (8, 1), (5, 5, 3, 3, 3, 1, 1): (10, 6, 3, 2), (5, 3, 1): (5, 3, 1)}
    for start, want in p3.items():
        terms, nstates, longest = all_terminals(start, join_moves)
        print(f"  {fmt(start)} total {sum(start)}: terminals {[fmt(t) for t in terms]}, "
              f"{nstates} reachable states, {count_routes(start, join_moves)} routes, longest strip {longest}")
        check(terms == {want}, f"P3 {fmt(start)} -> {fmt(want)} on every route (guide key)")

    print("\n== Page 4 demo and Problem 4: split evens, then rejoin ==")
    demo4 = (4, 3, 2)
    check((3, 2, 2, 2) in split_moves(demo4), "demo (4,3,2) -> split 4 -> (3,2,2,2)")
    check(split_all(demo4) == (3, 1, 1, 1, 1, 1, 1), "demo ends at (3,1,1,1,1,1,1), total 9")
    guide4 = {(10, 7, 4, 2, 1): (7, 5, 5, 1, 1, 1, 1, 1, 1, 1), (12, 6, 3): (3,) * 7, (7, 3, 1): (7, 3, 1)}
    for start, want_odd in guide4.items():
        check(is_distinct(start), f"P4 input {fmt(start)} has all sizes different (so 'again' fits)")
        t1, _, l1 = all_terminals(start, split_moves)
        odd = next(iter(t1))
        t2, _, l2 = all_terminals(odd, join_moves)
        back = next(iter(t2))
        print(f"  {fmt(start)} total {sum(start)} -> {fmt(odd)} -> {fmt(back)}; split routes "
              f"{count_routes(start, split_moves)}, join routes {count_routes(odd, join_moves)}; longest strip {max(l1, l2)}")
        check(len(t1) == 1 and odd == want_odd, f"P4 {fmt(start)} all-split result {fmt(want_odd)} (guide key)")
        check(len(t2) == 1 and back == start, f"P4 {fmt(start)} returns after rejoining (guide: every input returns)")
    # guide Limits: splitting an arbitrary repeated-size input and rejoining need not restore it
    ex = (2, 2)
    check(join_all(split_all(ex)) != ex, f"guide Limits example: {fmt(ex)} -> {fmt(split_all(ex))} -> {fmt(join_all(split_all(ex)))}")

    print("\n== Problem 5 (p.5): the 8-unit matching ==")
    o8, d8 = odd_parts(8), distinct_parts(8)
    pairs = [(p, join_all(p)) for p in o8]
    for a, b in pairs:
        print(f"  {fmt(a)} <-> {fmt(b)}   (split back: {fmt(split_all(b))})")
    check(len(o8) == len(d8) == 6, "6 odd and 6 distinct collections of 8; 8 printed box pairs suffice")
    guide5 = [((7, 1), (7, 1)), ((5, 3), (5, 3)), ((5, 1, 1, 1), (5, 2, 1)), ((3, 3, 1, 1), (6, 2)),
              ((3, 1, 1, 1, 1, 1), (4, 3, 1)), ((1,) * 8, (8,))]
    check(sorted(pairs) == sorted(guide5), "guide P5 table matches")
    check(all(split_all(b) == a for a, b in pairs), "every pair splits back")
    check(sorted({p[0] for p in o8}, reverse=True) == [7, 5, 3, 1], "guide P5: odd largest 7,5,3,1")
    check(sorted({p[0] for p in d8}, reverse=True) == [8, 7, 6, 5, 4], "guide P5: distinct largest 8,7,6,5,4")
    selfpairs = [a for a, b in pairs if a == b]
    print(f"  pairs whose two sides are the same collection (zero moves): {[fmt(a) for a in selfpairs]}")
    # Any reading of "connected by joining and splitting": components of the single-move graph
    print("  components of the graph whose edges are single joins/splits:")
    ok = True
    for n in range(0, 31):
        parts = partitions(n)
        comp = {}
        for p in parts:
            comp[p] = split_all(p)        # full splitting gives the component invariant
        # verify the invariant is constant along every single move
        for p in parts:
            for q in join_moves(p) | split_moves(p):
                if comp[q] != comp[p]:
                    ok = False
        groups = {}
        for p, c in comp.items():
            groups.setdefault(c, []).append(p)
        for c, members in groups.items():
            if sum(map(is_odd, members)) != 1 or sum(map(is_distinct, members)) != 1:
                ok = False
        if n == 8:
            for c, members in sorted(groups.items()):
                print(f"    {fmt(c)}: {len(members)} collections, odd {[fmt(m) for m in members if is_odd(m)]}, "
                      f"distinct {[fmt(m) for m in members if is_distinct(m)]}")
    check(ok, "n<=30: every join/split component holds exactly one only-odd and one all-different collection "
              "(so any reading of 'connected' gives the same pairs)")

    print("\n== Problem 6 (p.6): all joining routes from four 3s and six 1s ==")
    s6 = (3, 3, 3, 3, 1, 1, 1, 1, 1, 1)
    terms, nstates, longest = all_terminals(s6, join_moves)
    print(f"  total {sum(s6)}; reachable states {nstates}; routes {count_routes(s6, join_moves)}; "
          f"terminals {[fmt(t) for t in terms]}; longest strip {longest}")
    check(terms == {(12, 4, 2)}, "P6: every route ends at (12,4,2) (guide key)")
    r1 = [(3, 3, 3, 3, 1, 1, 1, 1, 1, 1), (6, 3, 3, 1, 1, 1, 1, 1, 1), (6, 6, 1, 1, 1, 1, 1, 1), (12, 1, 1, 1, 1, 1, 1),
          (12, 2, 1, 1, 1, 1), (12, 2, 2, 1, 1), (12, 2, 2, 2), (12, 4, 2)]
    r2 = [(3, 3, 3, 3, 1, 1, 1, 1, 1, 1), (3, 3, 3, 3, 2, 1, 1, 1, 1), (3, 3, 3, 3, 2, 2, 1, 1), (3, 3, 3, 3, 2, 2, 2),
          (4, 3, 3, 3, 3, 2), (6, 4, 3, 3, 2), (6, 6, 4, 2), (12, 4, 2)]
    check(legal_route(r1), "guide P6 route 1: every arrow is one legal join")
    check(legal_route(r2), "guide P6 route 2: every arrow is one legal join")
    # every all-odd collection: unique terminal (Problem 6's general question)
    worst = 0
    ok = True
    for n in range(0, 25):
        for p in odd_parts(n):
            t, ns, _ = all_terminals(p, join_moves)
            worst = max(worst, ns)
            if len(t) != 1 or not is_distinct(next(iter(t))):
                ok = False
    check(ok, f"every only-odd collection with total <= 24 reaches exactly one terminal, all sizes different (max {worst} states)")
    ok = True
    for n in range(0, 19):
        for p in partitions(n):
            t, _, _ = all_terminals(p, join_moves)
            if len(t) != 1:
                ok = False
    check(ok, "also true from every collection (not only odd) with total <= 18")

    print("\n== Problem 9 / guide overview: Euler's odd = distinct ==")
    ok = True
    for n in range(0, 41):
        o, d = odd_parts(n), distinct_parts(n)
        img = {join_all(p) for p in o}
        if len(o) != len(d) or img != set(d) or any(split_all(join_all(p)) != p for p in o) \
                or any(join_all(split_all(q)) != q for q in d):
            ok = False
    check(ok, "n <= 40: join map is a bijection only-odd -> all-different, split is its inverse, counts equal")
    print("  counts q(n), n=0..16:", [len(distinct_parts(n)) for n in range(17)])
    same = [n for n in range(0, 41) if set(odd_parts(n)) == set(distinct_parts(n))]
    print("  totals where the two catalogs are identical:", same, "(guide: 'usually different catalogs')")
    # Uniqueness lemma: distinct subsets of {u,2u,4u,...} have distinct totals
    ok = True
    for u in (1, 3, 5, 7):
        sizes = [u * 2 ** j for j in range(10)]
        sums = {}
        for r in range(len(sizes) + 1):
            for c in combinations(sizes, r):
                s = sum(c)
                if s in sums:
                    ok = False
                sums[s] = c
    check(ok, "guide p.6 lemma: different selections of u,2u,4u,... (u odd, 10 levels) never share a total")
    # odd families never collide
    ok = all((a * 2 ** i) != (b * 2 ** j) for a in range(1, 40, 2) for b in range(1, 40, 2) if a != b
             for i in range(8) for j in range(8))
    check(ok, "different odd families u*2^i never share a size")

    print("\n== Page 7 demo, Problem 7 and Problem 8: rows/columns ==")
    check(conjugate((5, 3, 3, 1)) == (4, 3, 3, 1, 1), "demo (5,3,3,1) -> columns 4,3,3,1,1")
    g7 = {(5, 2, 1): (3, 2, 1, 1, 1), (4, 4): (2, 2, 2, 2), (3, 3, 1, 1): (4, 2, 2)}
    for p, q in g7.items():
        c = conjugate(p)
        print(f"  {fmt(p)} -> {fmt(c)} -> {fmt(conjugate(c))}; once fits 6x6 grid: {len(c) <= 6 and c[0] <= 6}")
        check(c == q and conjugate(c) == p, f"P7 {fmt(p)} once {fmt(q)} twice back (guide key)")
    cat8 = [p for p in partitions(8) if len(p) <= 3]
    print(f"  8 with at most 3 strips: {len(cat8)}")
    for p in cat8:
        print(f"    {fmt(p)} -> {fmt(conjugate(p))}")
    guide8 = {(8,): (1,) * 8, (7, 1): (2, 1, 1, 1, 1, 1, 1), (6, 2): (2, 2, 1, 1, 1, 1), (6, 1, 1): (3, 1, 1, 1, 1, 1),
              (5, 3): (2, 2, 2, 1, 1), (5, 2, 1): (3, 2, 1, 1, 1), (4, 4): (2, 2, 2, 2), (4, 3, 1): (3, 2, 2, 1),
              (4, 2, 2): (3, 3, 1, 1), (3, 3, 2): (3, 3, 2)}
    check({p: conjugate(p) for p in cat8} == guide8, "guide P8 table (ten pairs) matches")
    check(len(cat8) == 10 and len(cat8) <= 12, "P8: 10 collections, 12 printed rows")
    check(sorted(conjugate(p) for p in cat8) == sorted(p for p in partitions(8) if p[0] <= 3),
          "P8: outputs are exactly the 8-unit collections with all sizes <= 3")
    by_len = Counter(len(p) for p in cat8)
    print("  by number of strips:", dict(by_len), "(guide: 1 + 4 + 5)")
    check(by_len == Counter({1: 1, 2: 4, 3: 5}), "guide P8 'why complete' 1+4+5")
    ok = True
    for n in range(0, 21):
        for p in partitions(n):
            c = conjugate(p)
            if sum(c) != n or conjugate(c) != p or len(c) != (p[0] if p else 0) or (c[0] if c else 0) != len(p):
                ok = False
        for k in range(0, n + 1):
            a = [p for p in partitions(n) if len(p) <= k]
            b = [p for p in partitions(n) if (p[0] if p else 0) <= k]
            if sorted(conjugate(p) for p in a) != sorted(b):
                ok = False
    check(ok, "n <= 20: conjugation is an involution, swaps #rows and longest row, and maps <=k parts onto parts <=k")

    print("\n== Physical bounds stated in the guide ==")
    printed = [(1,) * 9, (5, 5, 3, 3, 3, 1, 1), (5, 3, 1), (10, 7, 4, 2, 1), (12, 6, 3), (7, 3, 1), s6,
               (3, 3, 1, 1, 1, 1), (4, 3, 2)]
    longest = 0
    for p in printed:
        for moves in (join_moves, split_moves):
            _, _, l = all_terminals(p, moves)
            longest = max(longest, l)
    # also the rejoin after splitting in Problem 4
    for p in [(10, 7, 4, 2, 1), (12, 6, 3), (7, 3, 1)]:
        _, _, l = all_terminals(split_all(p), join_moves)
        longest = max(longest, l)
    print("  max total of a printed physical case:", max(sum(p) for p in printed))
    check(max(sum(p) for p in printed) <= 24, "every printed physical case uses at most 24 units")
    check(longest == 12, f"longest strip printed or formed on any legal route = {longest} (guide: 12 units, 18 cm at 15 mm)")

    print("\n== Guide p.2: K-1 pattern-block subset against Week 1 K-1 boards ==")
    data = json.loads((REPO / "plans/week-01-k1-shape-checks.json").read_text())
    for name in ("Sailboat", "Cat", "Hexagon", "Diamond"):
        poly = data[name]["polygon"]
        # shoelace in lattice coords (u,v); one lattice parallelogram = 2 small triangles
        a2 = sum(poly[i][0] * poly[(i + 1) % len(poly)][1] - poly[(i + 1) % len(poly)][0] * poly[i][1]
                 for i in range(len(poly)))
        tri = abs(a2)  # = 2 * area in parallelograms
        print(f"  {name}: {tri} small triangles (an all-green filling needs {tri}; kit has 12 greens, "
              f"6 blues, 1 yellow = 30 triangles)")
        check(tri <= 12, f"{name} can be filled by the 12 greens alone")

    print("\nFAILURES:", len(FAIL))
    for f in FAIL:
        print("  ", f)


if __name__ == "__main__":
    main()
