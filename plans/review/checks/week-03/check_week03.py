"""Independent math check of Week 3 (Shuffle machines): every problem in every band, and the adult guide.

Machines are read from the final PDFs by pdfmats.py (vector drawings only).  Every answer is recomputed
here by moving block labels turn by turn, by brute-force search, or by physically interleaving card lists;
the guide's printed answers are transcribed by hand below (GUIDE_*) and compared.

Run:  python3 -I check_week03.py   (from anywhere; the repository is found from this file's location)
"""
import math
import sys
from collections import Counter
from functools import reduce
from itertools import permutations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pdfmats import WEEK, colour_name, crossings, read_pdf  # noqa: E402
from guide_rows import rows_by_page  # noqa: E402
import pymupdf  # noqa: E402

FAIL = []


def ok(label, got, want):
    good = got == want
    print(f"  [{'ok' if good else 'MISMATCH'}] {label}: {got}" + ("" if good else f"   (expected/printed: {want})"))
    if not good:
        FAIL.append(label)


# ----------------------------------------------------------------------------------------------
# machines as 1-indexed target lists: p[i-1] = bottom slot that top slot i points to

def turn(row, p):
    """One turn: the block in slot i goes down its arrow to slot p(i), then the row slides up."""
    new = [None] * len(row)
    for i, b in enumerate(row):
        assert new[p[i] - 1] is None
        new[p[i] - 1] = b
    return new


def run_rows(p, start):
    rows, row = [], list(start)
    while True:
        row = turn(row, p)
        rows.append(row)
        if row == list(start):
            return rows


def turns_until_home(p):
    return len(run_rows(p, list(range(1, len(p) + 1))))


def home_times(p):
    start = list(range(1, len(p) + 1))
    out = {}
    row, t = list(start), 0
    while len(out) < len(p):
        row, t = turn(row, p), t + 1
        for slot, b in enumerate(row, 1):
            if b == slot and b not in out:
                out[b] = t
    return [out[b] for b in start]


def loops(p):
    seen, out = set(), []
    for i in range(1, len(p) + 1):
        if i not in seen:
            c, j = [], i
            while j not in seen:
                seen.add(j)
                c.append(j)
                j = p[j - 1]
            out.append(tuple(c))
    return out


def then_by_blocks(a, b):
    """The single machine that moves blocks as one turn of a and then one turn of b, found by running blocks."""
    row = turn(turn(list(range(1, len(a) + 1)), a), b)
    # block k ends in slot s: machine sends k -> s
    m = [None] * len(a)
    for s, k in enumerate(row, 1):
        m[k - 1] = s
    return m


def undo_by_search(p):
    sols = [list(q) for q in permutations(range(1, len(p) + 1))
            if turn(turn(list(range(1, len(p) + 1)), p), list(q)) == list(range(1, len(p) + 1))]
    assert len(sols) == 1
    return sols[0]


def lcm(a, b):
    return a * b // math.gcd(a, b)


def orders(n):
    return Counter(turns_until_home(list(q)) for q in permutations(range(1, n + 1)))


def partitions(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield []
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield [k] + r


COLOURS = ["green", "blue", "red", "yellow", "purple", "pink"]


def colour_rows(p):
    return [[COLOURS[b - 1] for b in r] for r in run_rows(p, list(range(1, len(p) + 1)))]


# ----------------------------------------------------------------------------------------------

def mats(pdf):
    return {pno: ms for pno, ms in read_pdf(pdf)}


def seg_dist(q, a, b):
    (px, py), (ax, ay), (bx, by) = q, a, b
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy
    t = 0 if L == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)


def legibility(name, pages):
    print(f"\n-- arrow legibility in {name}: smallest crossing angle and arrowhead offset per drawn mat")
    for pno, ms in pages.items():
        for k, m in enumerate(ms, 1):
            if m.perm is None:
                continue
            cr = crossings(m)
            ang = min((c[2] for c in cr), default=90)
            head = max((abs(o) for _, o in m.heads), default=0)
            # clearance: each arrow's start dot and end point to every other arrow, as a fraction of the slot width
            clear = 9.9
            for i in range(m.n):
                for j in range(m.n):
                    if i != j:
                        for q in (m.paths[i][0], m.paths[i][-1]):
                            clear = min(clear, min(seg_dist(q, a, b) for a, b in zip(m.paths[j], m.paths[j][1:])) / m.top[0].width)
            flag = "  <-- check" if ang < 12 or head > 0.3 or clear < 0.05 else ""
            print(f"  p{pno} mat{k} n={m.n}: {len(cr)} crossings, min angle {ang:.0f} deg, max head offset {head:.2f} slot, "
                  f"end clearance {clear:.2f} slot{flag}")


def k1():
    print("\n==== K-1 (F03-K-v5)")
    pg = mats("week-03-k-1.pdf")
    legibility("K-1", pg)
    print("P1")
    a, b = pg[1][0].perm, pg[1][1].perm
    ok("machines", [a, b], [[3, 1, 2], [1, 3, 2]])
    ok("pictures", pg[1][0].pictures, ["green", "blue", "red"])
    ok("turns", [turns_until_home(a), turns_until_home(b)], [3, 2])
    ok("guide rows top", colour_rows(a), [["blue", "red", "green"], ["red", "green", "blue"], ["green", "blue", "red"]])
    ok("guide rows bottom", colour_rows(b), [["green", "red", "blue"], ["green", "blue", "red"]])
    print("P2")
    c, d = pg[2][0].perm, pg[2][1].perm
    ok("turns", [turns_until_home(c), turns_until_home(d)], [4, 2])
    ok("guide rows top", colour_rows(c), [["yellow", "red", "green", "blue"], ["blue", "green", "yellow", "red"],
                                          ["red", "yellow", "blue", "green"], ["green", "blue", "red", "yellow"]])
    ok("guide rows bottom", colour_rows(d), [["red", "yellow", "green", "blue"], ["green", "blue", "red", "yellow"]])
    ok("bottom loops (guide: green-red and blue-yellow swap)", loops(d), [(1, 3), (2, 4)])
    print("P3")
    e, f = pg[3][0].perm, pg[3][1].perm
    ok("turns", [turns_until_home(e), turns_until_home(f)], [3, 6])
    ok("4-slot loops (guide: red straight)", loops(e), [(1, 2, 4), (3,)])
    ok("guide rows top", colour_rows(e), [["yellow", "green", "red", "blue"], ["blue", "yellow", "red", "green"],
                                          ["green", "blue", "red", "yellow"]])
    ok("guide rows bottom", colour_rows(f), [
        ["red", "purple", "green", "blue", "yellow"], ["green", "yellow", "red", "purple", "blue"],
        ["red", "blue", "green", "yellow", "purple"], ["green", "purple", "red", "blue", "yellow"],
        ["red", "yellow", "green", "purple", "blue"], ["green", "blue", "red", "yellow", "purple"]])
    ok("5-slot home times (guide: green, red 2; blue, yellow, purple 3)", home_times(f), [2, 3, 2, 3, 3])
    print("P4: 2, 3, 4 turns on blank 4-slot mats")
    ok("blank mats", [(m.n, m.perm) for m in pg[4] + pg[5]], [(4, None)] * 3)
    c4 = orders(4)
    ok("4-slot machines by turns (guide: 9 / 8 / 6)", (c4[2], c4[3], c4[4]), (9, 8, 6))
    print("P5: only one block in a different slot")
    one_moved = sum(1 for n in range(1, 8) for q in permutations(range(1, n + 1))
                    if sum(1 for i, t in enumerate(q, 1) if t != i) == 1)
    ok("machines with 1..7 slots moving exactly one block", one_moved, 0)
    # also after any number of turns (another reading): a power of a machine is a machine, so still 0
    print("P6: undo on the second mat")
    g = pg[7][0].perm
    ok("first machine", g, [4, 3, 1, 2])
    ok("row after one turn (guide)", [COLOURS[x - 1] for x in turn([1, 2, 3, 4], g)], ["red", "yellow", "blue", "green"])
    # arrows on the second mat act on the row as it lies; find all machines sending it home
    row = turn([1, 2, 3, 4], g)
    sols = [list(q) for q in permutations(range(1, 5)) if turn(row, list(q)) == [1, 2, 3, 4]]
    ok("all answers (guide: only 1->3, 2->4, 3->2, 4->1)", sols, [[3, 4, 2, 1]])
    print("P7: all 3-slot machines")
    ok("count", len(list(permutations(range(3)))), 6)
    ok("blank mats printed", len(pg[8]), 9)
    print("P8: 5-slot machines with 6 turns")
    six = [list(q) for q in permutations(range(1, 6)) if turns_until_home(list(q)) == 6]
    ok("count (guide 20, 19 besides P3)", (len(six), len([q for q in six if q != f])), (20, 19))
    ok("loop sizes", {tuple(sorted(len(c) for c in loops(q))) for q in six}, {(2, 3)})
    ok("guide examples take 6 turns", [turns_until_home(x) for x in ([2, 1, 4, 5, 3], [3, 4, 5, 2, 1])], [6, 6])


def m23():
    print("\n==== Grades 2-3 (F03-M-v5)")
    pg = mats("week-03-grades-2-3.pdf")
    legibility("2-3", pg)
    print("P1")
    a, c = pg[1][0].perm, pg[1][1].perm
    ok("machines (guide)", [a, c], [[4, 2, 1, 3], [3, 5, 4, 1, 2]])
    ok("home times / all", [home_times(a), turns_until_home(a), home_times(c), turns_until_home(c)],
       [[3, 1, 3, 3], 3, [3, 2, 3, 3, 2], 6])
    print("P2")
    ms = [pg[2][0].perm, pg[2][1].perm, pg[3][0].perm, pg[3][1].perm]
    ok("machines (guide table)", ms, [[2, 5, 1, 4, 3], [4, 3, 6, 1, 2, 5], [4, 1, 6, 2, 3, 5], [5, 6, 3, 1, 4, 2]])
    ok("loops (guide table)", [loops(m) for m in ms],
       [[(1, 2, 5, 3), (4,)], [(1, 4), (2, 3, 6, 5)], [(1, 4, 2), (3, 6, 5)], [(1, 5, 4), (2, 6), (3,)]])
    ok("turns (guide 4, 4, 3, 6)", [turns_until_home(m) for m in ms], [4, 4, 3, 6])
    ok("most loops on one machine (colours needed; guide asks for 3 per child)", max(len(loops(m)) for m in ms), 3)
    ok("pictures on 6-slot mats", pg[2][1].pictures, COLOURS)
    print("P3")
    ok("5-slot turns possible", sorted(orders(5)), [1, 2, 3, 4, 5, 6])
    ok("guide examples", [turns_until_home(x) for x in ([1, 2, 3, 4, 5], [2, 1, 3, 4, 5], [2, 3, 1, 4, 5],
                                                         [2, 3, 4, 1, 5], [2, 3, 4, 5, 1], [2, 1, 4, 5, 3])],
       [1, 2, 3, 4, 5, 6])
    print("P4")
    i, j = pg[5][0].perm, pg[6][0].perm
    ok("machines", [i, j], [[2, 4, 1, 3], [5, 1, 4, 3, 2]])
    ok("row after one turn (guide)", [[COLOURS[x - 1] for x in turn(list(range(1, len(p) + 1)), p)] for p in (i, j)],
       [["red", "green", "yellow", "blue"], ["blue", "purple", "yellow", "red", "green"]])
    ok("unique answers (guide)", [undo_by_search(i), undo_by_search(j)], [[3, 1, 4, 2], [2, 5, 4, 3, 1]])
    ok("same turns (guide 4 and 6)", [turns_until_home(undo_by_search(p)) for p in (i, j)], [4, 6])
    print("P5")
    inv = [list(q) for q in permutations(range(1, 6)) if turn(turn([1, 2, 3, 4, 5], list(q)), list(q)) == [1, 2, 3, 4, 5]]
    ok("5-slot self-undoing machines (guide 26 = 1 + 10 + 15)", (len(inv), Counter(sum(1 for c in loops(q) if len(c) == 2) for q in inv)),
       (26, Counter({0: 1, 1: 10, 2: 15})))
    ok("self-undoing <=> all loops of size 1 or 2", all((q in inv) == all(len(c) <= 2 for c in loops(q))
                                                       for q in map(list, permutations(range(1, 6)))), True)
    print("P6")
    for pno, want_ab, want_ba in ((8, ["blue", "red", "green", "yellow"], ["red", "green", "blue", "yellow"]),
                                  (9, ["red", "yellow", "green", "blue"], ["red", "yellow", "green", "blue"])):
        A, B = pg[pno][0].perm, pg[pno][2].perm
        ab = [COLOURS[x - 1] for x in turn(turn([1, 2, 3, 4], A), B)]
        ba = [COLOURS[x - 1] for x in turn(turn([1, 2, 3, 4], B), A)]
        ok(f"page {pno} A={A} B={B}: rows A then B / B then A (guide)", (ab, ba), (want_ab, want_ba))
    print("P7")
    o6 = orders(6)
    ok("6-slot turns possible", sorted(o6), [1, 2, 3, 4, 5, 6])
    ok("splits of 6 (guide 11) and their lcms", [(tuple(pt), reduce(lcm, pt)) for pt in partitions(6)],
       [((6,), 6), ((5, 1), 5), ((4, 2), 4), ((4, 1, 1), 4), ((3, 3), 3), ((3, 2, 1), 6), ((3, 1, 1, 1), 3),
        ((2, 2, 2), 2), ((2, 2, 1, 1), 2), ((2, 1, 1, 1, 1), 2), ((1, 1, 1, 1, 1, 1), 1)])
    ok("blank mats printed", len(pg[10]), 8)
    print("P8")
    o7 = orders(7)
    ok("7-slot turns possible", sorted(o7), [1, 2, 3, 4, 5, 6, 7, 10, 12])
    ok("more than 10 turns: loop sizes", {tuple(sorted(len(c) for c in loops(list(q))))
                                         for q in permutations(range(1, 8)) if turns_until_home(list(q)) > 10}, {(3, 4)})
    ok("guide example", turns_until_home([2, 3, 1, 5, 6, 7, 4]), 12)
    lc = {tuple(pt): reduce(lcm, pt) for pt in partitions(7)}
    ok("splits of 7 (15); guide's nine listed values", (len(lc), [lc[k] for k in [(7,), (6, 1), (5, 2), (5, 1, 1), (4, 3), (4, 2, 1), (3, 3, 1), (3, 2, 2), (3, 2, 1, 1)]]),
       (15, [7, 6, 10, 5, 12, 4, 3, 6, 6]))
    rest = [v for k, v in lc.items() if k not in [(7,), (6, 1), (5, 2), (5, 1, 1), (4, 3), (4, 2, 1), (3, 3, 1), (3, 2, 2), (3, 2, 1, 1)]]
    ok("the other six give 4 or less", (len(rest), max(rest)), (6, 4))


def out_shuffle(deck):
    h = len(deck) // 2
    top, bot = deck[:h], deck[h:]
    out = []
    for x, y in zip(top, bot):
        out += [x, y]
    return out


def shuffles_to_return(n):
    start = list(range(1, n + 1))
    d, k = out_shuffle(start), 1
    while d != start:
        d, k = out_shuffle(d), k + 1
    return k


def u45():
    print("\n==== Grades 4-5 (F03-U-v5)")
    pg = mats("week-03-grades-4-5.pdf")
    legibility("4-5", pg)
    print("P1")
    a, b = pg[1][0].perm, pg[1][1].perm
    ok("machines (guide)", [a, b], [[3, 2, 5, 1, 4], [5, 4, 1, 2, 3]])
    ok("home times / all (guide)", [home_times(a), turns_until_home(a), home_times(b), turns_until_home(b)],
       [[4, 1, 4, 4, 4], 4, [3, 2, 3, 2, 3], 6])
    print("P2")
    ms = [m.perm for m in pg[2]]
    ok("loops (guide)", [loops(m) for m in ms],
       [[(1, 3, 5), (2, 6, 4)], [(1, 5), (2, 3, 6), (4,)], [(1, 4, 7, 2, 5), (3, 6)], [(1, 4, 2, 7, 3, 5, 6)],
        [(1, 3, 2, 5, 7, 6), (4, 8)], [(1, 3, 6, 8), (2, 5, 7, 4)]])
    ok("turns (guide 3, 6, 10, 7, 6, 4)", [turns_until_home(m) for m in ms], [3, 6, 10, 7, 6, 4])
    print("P3")
    ok("5-slot turns (guide 1..6)", sorted(orders(5)), [1, 2, 3, 4, 5, 6])
    ok("blank mats", len(pg[3]), 9)
    print("P4")
    ok("max turns 6 and 7 slots (guide 6, 12)", (max(orders(6)), max(orders(7))), (6, 12))
    ok("6-slot record loop sizes (guide: 6 or 3+2+1)", {tuple(sorted((len(c) for c in loops(list(q))), reverse=True))
                                                       for q in permutations(range(1, 7)) if turns_until_home(list(q)) == 6},
       {(6,), (3, 2, 1)})
    print("P5: perfect shuffles, by interleaving card lists")
    ok("8 cards, one shuffle", out_shuffle(["A", "2", "3", "4", "5", "6", "7", "8"]), ["A", "5", "2", "6", "3", "7", "4", "8"])
    ok("shuffles to return for 4, 6, 8, 10, 12 (guide 2, 4, 3, 6, 10)", [shuffles_to_return(n) for n in (4, 6, 8, 10, 12)],
       [2, 4, 3, 6, 10])
    d = out_shuffle(list(range(1, 9)))
    m8 = [d.index(k) + 1 for k in range(1, 9)]
    ok("8-card machine (guide 1->1, 2->3, 3->5, 4->7, 5->2, 6->4, 7->6, 8->8)", m8, [1, 3, 5, 7, 2, 4, 6, 8])
    ok("8-card loops", loops(m8), [(1,), (2, 3, 5), (4, 7, 6), (8,)])
    ok("mat labels", pg[5][0].labels[:8], ["A", "2", "3", "4", "5", "6", "7", "8"])
    pile = []
    for x, y in zip("A234", "5678"):
        pile = [x] + pile
        pile = [y] + pile
    ok("dealing alternately onto a pile, top to bottom (guide 8,4,7,3,6,2,5,A)", pile, list("8473625A"))
    print("P6")
    want = [([3, 1, 2, 4], [2, 3, 1, 4]), ([2, 1, 4, 3], [2, 1, 4, 3]), ([3, 4, 1, 2], [2, 1, 4, 3])]
    for k in range(3):
        A, B = pg[6][4 * k].perm, pg[6][4 * k + 1].perm
        ok(f"pair {k + 1} A={A} B={B}: A then B, B then A (guide)", (then_by_blocks(A, B), then_by_blocks(B, A)), want[k])
    print("P7")
    want = [([4, 2, 1, 3], [3, 1, 2, 4], [1, 3, 4, 2], [3, 2, 4, 1]), ([3, 1, 4, 2], [2, 1, 3, 4], [1, 4, 2, 3], [2, 4, 1, 3])]
    for k in range(2):
        A, B = pg[7][6 * k].perm, pg[7][6 * k + 1].perm
        AB = then_by_blocks(A, B)
        got = (AB, undo_by_search(A), undo_by_search(B), undo_by_search(AB))
        ok(f"pair {k + 1} A={A} B={B}: AB, undo A, undo B, undo AB (guide)", got, want[k])
        ok("  undo AB = undo B then undo A; other order fails",
           (then_by_blocks(undo_by_search(B), undo_by_search(A)) == undo_by_search(AB),
            then_by_blocks(undo_by_search(A), undo_by_search(B)) == undo_by_search(AB)), (True, False))
    print("P8")
    der = [list(q) for q in permutations(range(1, 5)) if all(q[i] != i + 1 for i in range(4))]
    pairs = [(x, y) for i, x in enumerate(der) for y in der[i + 1:] if then_by_blocks(x, y) == then_by_blocks(y, x)]
    ok("derangements / commuting unordered pairs (guide 9 / 12)", (len(der), len(pairs)), (9, 12))
    kinds = Counter()
    for x, y in pairs:
        tx = tuple(sorted(len(c) for c in loops(x)))
        ty = tuple(sorted(len(c) for c in loops(y)))
        if tx == ty == (2, 2):
            kinds["two double swaps"] += 1
        elif tx == ty == (4,):
            kinds["4-loop and reverse"] += 1 if then_by_blocks(x, y) == [1, 2, 3, 4] else 0
        else:
            kinds["4-loop and its square"] += 1 if (then_by_blocks(x, x) == y or then_by_blocks(y, y) == x) else 0
    ok("kinds (guide 3 / 3 / 6)", dict(kinds), {"two double swaps": 3, "4-loop and reverse": 3, "4-loop and its square": 6})
    print("P9")
    g = [max(reduce(lcm, pt) for pt in partitions(n)) for n in range(1, 11)]
    ok("largest turns 1..10 by partitions (guide)", g, [1, 2, 3, 4, 6, 6, 12, 15, 20, 30])
    ok("brute force agrees for 1..8", [max(orders(n)) for n in range(1, 9)], g[:8])
    rec = {n: sorted({tuple(pt) for pt in partitions(n) if reduce(lcm, pt) == g[n - 1]}) for n in range(5, 11)}
    ok("record loop sizes 5..10 (guide 3+2; 6 or 3+2+1; 4+3; 5+3; 5+4; 5+3+2)", rec,
       {5: [(3, 2)], 6: [(3, 2, 1), (6,)], 7: [(4, 3)], 8: [(5, 3)], 9: [(5, 4)], 10: [(5, 3, 2)]})
    ok("steps with no gain from 1 to 10 slots (guide: only 5 -> 6)", [n for n in range(1, 10) if g[n] <= g[n - 1]], [5])
    print("P10")
    ok("52 cards (guide 8)", shuffles_to_return(52), 8)
    d = out_shuffle(list(range(1, 53)))
    m52 = [d.index(k) + 1 for k in range(1, 53)]
    L = loops(m52)
    ok("52-card loop sizes (guide: six 8s, one 2, two fixed)", Counter(len(c) for c in L), Counter({8: 6, 2: 1, 1: 2}))
    ok("the 2-loop (guide 18 and 35)", [c for c in L if len(c) == 2], [(18, 35)])
    ok("orbit of position 2 (guide 2,3,5,9,17,33,14,27)", [c for c in L if 2 in c][0], (2, 3, 5, 9, 17, 33, 14, 27))


def guide_extra():
    print("\n==== Adult guide, other claims")
    print("launch: chairs 1->2, 2->1, 3->5, 5->4, 4->3")
    ok("who sits in chairs 1-5 after each switch (guide rows)", colour_rows([2, 1, 5, 3, 4]), [
        ["blue", "green", "yellow", "purple", "red"], ["green", "blue", "purple", "red", "yellow"],
        ["blue", "green", "red", "yellow", "purple"], ["green", "blue", "yellow", "purple", "red"],
        ["blue", "green", "purple", "red", "yellow"], ["green", "blue", "red", "yellow", "purple"]])
    ok("home after 2: green, blue; after 3: red, yellow, purple", home_times([2, 1, 5, 3, 4]), [2, 2, 3, 3, 3])
    print("guide example mats (read from the guide PDF)")
    gp = mats("week-03-facilitator.pdf")
    ok("P4 examples turns (captions 2, 3, 4)", [turns_until_home(m.perm) for m in gp[4]], [2, 3, 4])
    ok("P6 first machine / answer", [m.perm for m in gp[5][:2]], [[4, 3, 1, 2], [3, 4, 2, 1]])
    ok("P7 six machines, all different, turns (captions 1, 2, 2, 2, 3, 3)",
       (len({tuple(m.perm) for m in gp[5][2:]}), [turns_until_home(m.perm) for m in gp[5][2:]]), (6, [1, 2, 2, 2, 3, 3]))
    print("section 5")
    ok("return times on 7 slots (guide 1-7, 10, 12)", sorted({reduce(lcm, pt) for pt in partitions(7)}), [1, 2, 3, 4, 5, 6, 7, 10, 12])
    print("perfect shuffles: out-shuffle order = order of 2 mod 2m-1; in-shuffle 52 cards needs 52")

    def mult_order(a, n):
        k, x = 1, a % n
        while x != 1:
            x, k = x * a % n, k + 1
        return k

    ok("order of 2 mod 2m-1 for 4,6,8,10,12,52 (guide 2,4,3,6,10,8)", [mult_order(2, n - 1) for n in (4, 6, 8, 10, 12, 52)], [2, 4, 3, 6, 10, 8])
    ok("agrees with interleaving", [shuffles_to_return(n) for n in (4, 6, 8, 10, 12, 52)], [2, 4, 3, 6, 10, 8])

    def in_shuffle(deck):
        h = len(deck) // 2
        out = []
        for x, y in zip(deck[:h], deck[h:]):
            out += [y, x]
        return out

    start, d, k = list(range(52)), in_shuffle(list(range(52))), 1
    while d != start:
        d, k = in_shuffle(d), k + 1
    ok("in-shuffles for 52 cards (guide 52)", k, 52)
    print("Elmsley: top card to position k (from 0): binary of k, in for 1, out for 0, read from the left")
    bad = []
    for k in range(1, 52):
        deck = list(range(52))
        for bit in bin(k)[2:]:
            deck = in_shuffle(deck) if bit == "1" else out_shuffle(deck)
        if deck.index(0) != k:
            bad.append(k)
    ok("positions 1..51 that fail", bad, [])
    print("materials")
    ok("cubes: 25 + 30 + 20 = 75; green 5+5+4 = 14; pink 5", (5 * 5 + 5 * 6 + 4 * 5, 5 + 5 + 4, 5), (75, 14, 5))
    ok("pattern blocks (1 in sides): trapezoid 2, hexagon across corners 2, blue rhombus long diagonal 1.73",
       (2, 2, round(math.sqrt(3), 2)), (2, 2, 1.73))


def guide_rows_from_pdf():
    """Compare every coloured cube row printed in the guide PDF with rows computed by running the student machines."""
    print("\n==== Guide rows read from the PDF vs rows computed from the student mats")
    k1 = mats("week-03-k-1.pdf")
    m23 = mats("week-03-grades-2-3.pdf")
    expected = []   # (page, description, list of rows)
    expected.append((3, "launch chairs", colour_rows([2, 1, 5, 3, 4])))
    expected.append((4, "K-1 P1 top", colour_rows(k1[1][0].perm)))
    expected.append((4, "K-1 P1 bottom", colour_rows(k1[1][1].perm)))
    expected.append((4, "K-1 P2 top", colour_rows(k1[2][0].perm)))
    expected.append((4, "K-1 P2 bottom", colour_rows(k1[2][1].perm)))
    expected.append((4, "K-1 P3 top", colour_rows(k1[3][0].perm)))
    expected.append((4, "K-1 P3 bottom", colour_rows(k1[3][1].perm)))
    expected.append((5, "K-1 P6 row after one turn", [[COLOURS[x - 1] for x in turn([1, 2, 3, 4], k1[7][0].perm)]]))
    for p in (m23[5][0].perm, m23[6][0].perm):
        expected.append((6, f"2-3 P4 row after one turn of {p}", [[COLOURS[x - 1] for x in turn(list(range(1, len(p) + 1)), p)]]))
    for pno in (8, 9):
        A, B = m23[pno][0].perm, m23[pno][2].perm
        expected.append((6, f"2-3 P6 page {pno} A then B", [[COLOURS[x - 1] for x in turn(turn([1, 2, 3, 4], A), B)]]))
        if pno == 8:
            expected.append((6, f"2-3 P6 page {pno} B then A", [[COLOURS[x - 1] for x in turn(turn([1, 2, 3, 4], B), A)]]))
    printed = rows_by_page()
    used = set()
    for page, desc, rows in expected:
        cands = [(i, r) for i, r in enumerate(printed.get(page, [])) if (page, i) not in used]
        # the printed rows of one answer appear consecutively in reading order
        seq = [r[3] for _, r in cands]
        found = None
        for start in range(len(seq) - len(rows) + 1):
            if seq[start:start + len(rows)] == rows:
                found = start
                break
        ok(f"guide p{page}: {desc} printed exactly as computed", found is not None, True)
        if found is not None:
            for _, (i, _) in zip(range(len(rows)), cands[found:found + len(rows)]):
                used.add((page, i))
    left = [(pg, r) for pg, rs in printed.items() for i, r in enumerate(rs) if (pg, i) not in used and len(r[3]) > 1
            and r[2] != "?"]
    ok("printed rows not accounted for", left, [])


def geometry():
    print("\n==== Geometry: slots square, block pictures regular, slot sizes")
    for name in ("week-03-k-1.pdf", "week-03-grades-2-3.pdf", "week-03-grades-4-5.pdf"):
        doc = pymupdf.open(WEEK / name)
        worst_sq, tri, hexa, sizes = 0.0, [], [], Counter()
        for page in doc:
            for d in page.get_drawings():
                r = d["rect"]
                f = d.get("fill")
                if d["type"] == "fs" and f and all(abs(c - 0.975) < 0.01 for c in f):
                    worst_sq = max(worst_sq, abs(r.width - r.height))
                    sizes[round(r.width / 72, 2)] += 1
                c = colour_name(f)
                pts = [q for it in d["items"] for q in it[1:] if hasattr(q, "x")]
                vs = []
                for q in pts:
                    if not any(abs(q.x - v.x) < 0.05 and abs(q.y - v.y) < 0.05 for v in vs):
                        vs.append(q)
                if c == "green" and len(vs) == 3:
                    e = [math.dist((vs[i].x, vs[i].y), (vs[(i + 1) % 3].x, vs[(i + 1) % 3].y)) for i in range(3)]
                    tri.append(max(e) / min(e))
                if c == "yellow" and len(vs) == 6:
                    e = [math.dist((vs[i].x, vs[i].y), (vs[(i + 1) % 6].x, vs[(i + 1) % 6].y)) for i in range(6)]
                    hexa.append(max(e) / min(e))
        print(f"  {name}: slot sizes (in) {dict(sizes)}; worst |w-h| {worst_sq:.3f} pt; "
              f"green triangles max side ratio {max(tri, default=1):.3f}; yellow hexagons max side ratio {max(hexa, default=1):.3f}")
        ok(f"{name} slots square, triangles equilateral, hexagons regular (within 1%)",
           (worst_sq < 0.2, max(tri, default=1) < 1.01, max(hexa, default=1) < 1.01), (True, True, True))


def return_visit():
    print("\n==== Return visit (companion, brief)")

    def inv(r):
        return sum(1 for i in range(len(r)) for j in range(i + 1, len(r)) if r[i] > r[j])

    def bfs_adjacent(r):
        start, goal = tuple(r), tuple(sorted(r))
        seen, frontier, d = {start}, [start], 0
        while goal not in seen:
            nxt = []
            for s in frontier:
                for i in range(len(s) - 1):
                    t = list(s)
                    t[i], t[i + 1] = t[i + 1], t[i]
                    t = tuple(t)
                    if t not in seen:
                        seen.add(t)
                        nxt.append(t)
            frontier, d = nxt, d + 1
        return d

    rows = [[2, 1, 3, 5, 4], [3, 1, 4, 2, 5], [5, 3, 4, 2, 1]]
    ok("P1 rows: fewest adjacent swaps by BFS (guide 2, 3, 9)", [bfs_adjacent(r) for r in rows], [2, 3, 9])
    ok("P1 hardest 5-card row distance (guide 54321, 10)", max(bfs_adjacent(list(q)) for q in permutations(range(1, 6))), 10)
    ok("inversions agree with BFS for all 5-card rows", all(inv(q) == bfs_adjacent(list(q)) for q in permutations(range(1, 6))), True)

    def reach(n):
        start = tuple(range(1, n + 1))
        seen, frontier = {start}, [start]
        while frontier:
            nxt = []
            for s in frontier:
                for t in (s[-1:] + s[:-1], s[::-1]):
                    if t not in seen:
                        seen.add(t)
                        nxt.append(t)
            frontier = nxt
        return seen

    R4 = reach(4)
    ok("P2 reachable from 1234 (guide 8; 10 for five cards)", (len(R4), len(reach(5))), (8, 10))
    ok("P2 targets 3412, 2143 reachable; 1324, 2413 not", [t in R4 for t in [(3, 4, 1, 2), (2, 1, 4, 3), (1, 3, 2, 4), (2, 4, 1, 3)]],
       [True, True, False, False])

    def square(p):
        return [p[p[i] - 1] for i in range(len(p))]

    def target_perm(row):
        # output row after two passes: slot s holds card row[s-1]; so card c went to slot row.index(c)+1
        return [row.index(c) + 1 for c in range(1, len(row) + 1)]

    for row, root in (([2, 3, 1], [2, 3, 1]), ([2, 1, 4, 3], [3, 4, 2, 1]), ([2, 3, 1, 5, 6, 4], [2, 3, 1, 5, 6, 4])):
        r1 = turn(list(range(1, len(row) + 1)), root)
        r2 = turn(r1, root)
        ok(f"P3 guide root {root} for output {row}: rows", (r1, r2 == row), ({(2, 3, 1): [3, 1, 2], (2, 1, 4, 3): [4, 3, 1, 2], (2, 3, 1, 5, 6, 4): [3, 1, 2, 6, 4, 5]}[tuple(row)], True))
    t213 = target_perm([2, 1, 3])
    ok("P3 output 213 has no root", [list(q) for q in permutations(range(1, 4)) if square(list(q)) == t213], [])
    cnt = [len({tuple(square(list(q))) for q in permutations(range(1, n + 1))}) for n in (3, 4, 6)]
    ok("targets with a root, 3/4/6 slots (guide 3, 12, 270)", cnt, [3, 12, 270])


if __name__ == "__main__":
    k1()
    m23()
    u45()
    guide_extra()
    guide_rows_from_pdf()
    geometry()
    return_visit()
    print(f"\n{len(FAIL)} mismatches" + (": " + "; ".join(FAIL) if FAIL else ""))
