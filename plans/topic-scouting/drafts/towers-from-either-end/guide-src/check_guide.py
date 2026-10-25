"""Independent answer check for the 'Towers from either end' facilitator guide.

Written from scratch for the guide; it does not import the page builder's
check.py or verify.py.  Rows are copied from the final student pages
(plans/topic-scouting/drafts/towers-from-either-end/*.pdf, read from the
rendered pages and src/gen.py).

Game: a row of towers; players alternate removing one whole tower from either
end; more cubes wins, equal is a tie.  "Best play" means each player collects
as many cubes as they can be sure of (equivalently maximises their margin,
since the total is fixed).

Run: python3 check_guide.py      (asserts every number printed in the guide)
"""
import os
from functools import lru_cache
from itertools import product


# ------------------------------------------------------------------ solver
def solve(row):
    """Full minimax by brute force over (lo, hi).  Returns the most cubes the
    player to move can be sure of collecting."""
    row = tuple(row)

    @lru_cache(maxsize=None)
    def best(lo, hi):
        if lo > hi:
            return 0
        rest = sum(row[lo:hi + 1])
        # take left: opponent then gets best(lo+1, hi) of the remainder
        take_left = rest - best(lo + 1, hi)
        take_right = rest - best(lo, hi - 1)
        return max(take_left, take_right)

    return best(0, len(row) - 1)


def score(row):
    """(first player, second player) under best play."""
    f = solve(row)
    return f, sum(row) - f


def after_first(row, side):
    """(first, second) when the first player takes side 'L' or 'R' and both
    then play their best."""
    row = tuple(row)
    if side == "L":
        taken, rest = row[0], row[1:]
    else:
        taken, rest = row[-1], row[:-1]
    s = solve(rest) if rest else 0
    return taken + (sum(rest) - s), s


def best_moves(row):
    f, _ = score(row)
    out = [s for s in ("L", "R") if after_first(row, s)[0] == f]
    if row[0:1] == row[-1:] and len(row) == 1:
        out = ["L"]
    return out


def outcome(row):
    f, s = score(row)
    return "first" if f > s else ("second" if s > f else "tie")


def colours(row):
    """Slot 1 is red: red = slots 1, 3, 5, ...; blue = slots 2, 4, 6, ..."""
    return sum(row[0::2]), sum(row[1::2])


def all_games(row):
    """Every legal complete game as a list of slot numbers taken."""
    n = len(row)
    games = []

    def rec(lo, hi, seq):
        if lo > hi:
            games.append(seq)
            return
        rec(lo + 1, hi, seq + [lo + 1])
        if hi > lo:
            rec(lo, hi - 1, seq + [hi + 1])

    rec(1 - 1, n - 1, [])
    return games


def plan_games(row, colour):
    """First player always takes the end on slots of `colour` ('red' = odd
    slots).  Every reply of the opponent.  Returns list of
    (slot sequence, planner haul, opponent haul)."""
    want = 1 if colour == "red" else 0   # slot number parity
    out = []
    for g in all_games(row):
        ok = all(g[i] % 2 == want for i in range(0, len(g), 2))
        if ok:
            a = sum(row[g[i] - 1] for i in range(0, len(g), 2))
            b = sum(row[g[i] - 1] for i in range(1, len(g), 2))
            out.append((g, a, b))
    return out


def greedy_vs_best(row):
    """Mover always takes the taller end (left if equal); opponent plays best
    against that.  Returns (greedy haul, opponent haul)."""
    row = tuple(row)

    @lru_cache(maxsize=None)
    def g(lo, hi, greedy_turn):
        # returns greedy player's haul from row[lo..hi] with opponent minimising it
        if lo > hi:
            return 0
        if greedy_turn:
            if row[lo] >= row[hi]:
                return row[lo] + g(lo + 1, hi, False)
            return row[hi] + g(lo, hi - 1, False)
        return min(g(lo + 1, hi, True), g(lo, hi - 1, True))

    a = g(0, len(row) - 1, True)
    return a, sum(row) - a


def triangle(row):
    n = len(row)
    return {(i, k): solve(row[i:i + k]) for k in range(1, n + 1)
            for i in range(n - k + 1)}


def fmt(row):
    return ",".join(map(str, row))


def report(title, rows):
    print(f"\n{title}")
    for r in rows:
        f, s = score(r)
        L = after_first(r, "L")
        R = after_first(r, "R")
        red, blue = colours(r)
        print(f"  {fmt(r):<18} best {f}-{s} ({outcome(r)}), "
              f"take slot 1 -> {L[0]}-{L[1]}, take slot {len(r)} -> {R[0]}-{R[1]}, "
              f"red {red} blue {blue}")


# ------------------------------------------------------------------ the pages
K1 = {
    1: [(5, 2, 1, 4), (1, 5, 2, 3), (2, 4, 3, 1)],
    2: [(2, 1, 5, 3), (3, 5, 1, 2), (1, 1, 5, 2), (2, 5, 1, 1), (5, 1, 3, 2), (2, 3, 1, 4)],
    3: [(1, 5, 1), (5, 1, 5), (1, 4, 2), (3, 4, 2), (2, 5, 2)],
    6: [(1, 2, 5, 2), (3, 4, 1, 2), (4, 1, 5, 2), (1, 4, 2, 3)],
    7: [(3, 1, 2, 5), (2, 4, 1, 1), (1, 3, 2, 1, 3, 1), (2, 1, 1, 3, 2, 2)],
    8: [(2, 1, 2, 3), (1, 3, 4, 2), (4, 1, 2, 5)],
}
G23 = {
    1: [(5, 2, 1, 4), (2, 6, 3, 4), (2, 4, 3, 1)],
    2: [(2, 1, 5, 3), (3, 6, 1, 2), (2, 3, 1, 5), (1, 4, 6, 2)],
    3: [(1, 5, 1), (5, 1, 5), (2, 6, 3), (3, 4, 2), (2, 5, 3), (4, 6, 1)],
    5: [(1, 2, 5, 1, 3, 2), (3, 1, 1, 4, 2, 2), (1, 2, 3, 1, 2, 1, 3, 2)],
    6: [(2, 4, 1, 1, 3, 2)],
    7: [(2, 1, 2, 3), (1, 3, 4, 2), (4, 1, 2, 5), (2, 4, 5, 3), (3, 2, 4, 5)],
    8: [(2, 1, 5, 1, 2), (4, 1, 1, 1, 4), (1, 4, 2, 4, 1), (1, 2, 4, 2, 1)],
}
G45 = {
    1: [(2, 1, 5, 3), (1, 4, 6, 2), (2, 4, 3, 1), (6, 2, 1, 5)],
    2: [(1, 5, 1), (5, 1, 5), (2, 6, 3), (3, 4, 2), (2, 5, 3), (6, 1, 2)],
    4: [(1, 2, 5, 1, 3, 2), (3, 1, 1, 4, 2, 2), (1, 2, 3, 1, 2, 1, 3, 2)],
    6: [(2, 1, 2, 3), (1, 3, 4, 2), (4, 1, 2, 5), (2, 4, 5, 3), (3, 1, 1, 3), (4, 2, 1, 3)],
    7: [(1, 4, 2, 4, 1), (2, 3, 1, 5, 2), (3, 5, 2, 4, 1), (1, 3, 3, 3, 1)],
    8: [(4, 1, 1, 1, 4), (1, 2, 4, 2, 1), (2, 1, 5, 1, 2), (4, 2, 1, 2, 4), (4, 1, 6, 2, 3)],
    10: [(3, 1, 4, 1, 5), (2, 1, 2, 5, 3), (5, 2, 6, 1, 3)],
    11: (2, 3, 6, 2, 1, 4),
}
LAUNCH = (3, 1, 4, 2)


# ------------------------------------------------------------------ rows as printed
PAGE_SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")


def printed_rows(name):
    """Read every drawn row from a page source (read-only): tower pictures
    (cube rectangles over slot bases) and number strips (heights in squares)."""
    import os
    import re
    s = open(os.path.join(PAGE_SRC, name)).read()
    rows = []
    for pic in re.findall(r"\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}", s, re.S):
        bases = re.findall(r"\\draw\[thick, fill=(\w+)\] \(([\d.]+),0\) rectangle", pic)
        cubes = re.findall(r"\\draw\[fill=black!14\] \(([\d.]+),([\d.]+)\)", pic)
        nums = re.findall(r"\\node\[font=\\large\] at \(([\d.]+),([\d.]+)\) \{(\d+)\}", pic)
        if bases and cubes:
            width = float(bases[1][1]) - float(bases[0][1])
            h = [0] * len(bases)
            for cx, _ in cubes:
                h[int(float(cx) // width)] += 1
            rows.append(tuple(h))
        elif bases and nums and len(nums) == len(bases):
            rows.append(tuple(int(n[2]) for n in nums))
    return rows


def check(cond, msg):
    assert cond, msg



# ------------------------------------------------------------------ revision checks
MATERIALS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "materials.pdf")


def three_mover(a, m, b):
    """Adult shortcut printed in the guide: on a row of three the player to
    move collects both ends if the middle is the tallest (at least as tall as
    each end), otherwise the taller end plus the smaller of the other two."""
    if m >= a and m >= b:
        return a + b
    if a >= b:
        return a + min(m, b)
    return b + min(a, m)


def materials_strips():
    """Read the delivered materials.pdf: page titles, orientation, and the
    strips on each page (a strip = a run of slot numbers 1..n on one line)."""
    import pymupdf
    doc = pymupdf.open(MATERIALS)
    pages = []
    for pg in doc:
        words = pg.get_text("words")
        title = [w for w in words if 60 < w[1] < 100]
        title = " ".join(w[4] for w in sorted(title, key=lambda w: w[0]))
        nums = sorted((w[1], w[0], int(w[4])) for w in words
                      if w[4].isdigit() and int(w[4]) <= 12 and 100 < w[1] < pg.rect.height - 60)
        lines = []                # slot numbers grouped into lines, 3 pt tolerance
        for y, x, n in nums:
            if lines and abs(lines[-1][0] - y) < 3:
                lines[-1][1].append((x, n))
            else:
                lines.append((y, [(x, n)]))
        strips = []
        for _, line in lines:
            run = []
            for x, n in sorted(line):
                if n == 1 and run:
                    strips.append(len(run)); run = []
                run.append(n)
            if run:
                strips.append(len(run))
        pages.append((title, pg.rect.width > pg.rect.height, strips))
    return pages


def revision_checks():
    A = after_first
    # M1: the three-tower shortcut gives the mover's best total on every row of three
    for r in product(range(1, 7), repeat=3):
        check(three_mover(*r) == solve(r), ("three shortcut", r))
    print("adult shortcut for a row of three matches best play on all 216 rows (heights 1-6)")
    # M1: the row of three left after the first move does not settle the row of four
    for r, partner_rows, actual in [((2, 4, 3, 1), ((4, 3, 1), (2, 4, 3)), (5, 5)),
                                    ((6, 2, 1, 5), ((2, 1, 5), (6, 2, 1)), (8, 6))]:
        for t in partner_rows:
            check(outcome(t) == "first", (r, t, "partner, moving first on it, wins"))
        check(score(r) == actual, (r, score(r)))
        print(f"  {fmt(r)}: partner wins both rows of three left "
              f"({', '.join(fmt(t) + ' ' + str(score(t)) for t in partner_rows)}), "
              f"yet the row of four is {actual[0]}-{actual[1]}; after slot 1 {A(r, 'L')}, after slot {len(r)} {A(r, 'R')}")
    check(score((2, 1, 5)) == (6, 2) and score((6, 2, 1)) == (7, 2), "4-5 P1 rows of three")
    check(A((6, 2, 1, 5), "L") == (8, 6) and A((2, 4, 3, 1), "L") == (5, 5) and A((2, 4, 3, 1), "R") == (5, 5), "M1 totals")
    wrong = [r for r in product(range(1, 7), repeat=4)
             if outcome(r[1:]) == "first" and outcome(r[:-1]) == "first" and outcome(r) != "second"]
    print(f"  rows of four (1-6) the 'row of three rule' would wrongly call first-player losses: {len(wrong)}")
    # M2 / overview heading: equal colours, first player still wins (2, 1, 2, 3)
    check(colours((2, 1, 2, 3)) == (4, 4) and score((2, 1, 2, 3)) == (5, 3), "2123")
    # S2: putting 1, 1 in front of an equal-colour first-player win of four
    tested = fails = 0
    for r in product(range(1, 10), repeat=4):
        if colours(r)[0] == colours(r)[1] and outcome(r) == "first":
            tested += 1
            fails += outcome((1, 1) + r) != "first"
    print(f"  1,1 in front of equal-colour winning rows of four (heights 1-9): {fails} fail of {tested}")
    check(fails == 0 and tested == 168, "prefix four")
    six = (2, 1, 1, 2, 1, 1)
    check(colours(six) == (4, 4) and score(six) == (5, 3), ("six", score(six)))
    check(colours((1, 1) + six) == (5, 5) and score((1, 1) + six) == (5, 5), ("eight", score((1, 1) + six)))
    print(f"  {fmt(six)} {score(six)}; 1,1,{fmt(six)} {score((1, 1) + six)}")
    # K-1 P8: on 1, 3, 4, 2 the careful partner's reply
    r = (1, 3, 4, 2)
    after2 = (1, 3, 4)            # child took the 2 (slot 4)
    # partner takes x, leaving `rest` with the child to move: child 2 + solve(rest)
    take4 = 2 + solve((1, 3)), 4 + (sum((1, 3)) - solve((1, 3)))
    take1 = 2 + solve((3, 4)), 1 + (sum((3, 4)) - solve((3, 4)))
    check(take4 == (5, 5) and take1 == (6, 4), ("K1 P8 replies", take4, take1))
    after1 = (3, 4, 2)            # child took the 1 (slot 1)
    rep = [1 + solve((4, 2)), 1 + solve((3, 4))]   # partner takes the 3 / the 2
    check(rep == [5, 5], ("K1 P8 after slot 1", rep))
    print(f"  K-1 P8 1,3,4,2: child takes the 2, partner takes 4 -> {take4}, partner takes 1 -> {take1}; "
          f"child takes the 1 -> child gets {rep} for the two replies (a 5-5 tie)")
    # grown-up's card: no printed grown-up row has equal colour totals; equal totals give exactly half
    for row in K1[6] + G23[5]:
        check(colours(row)[0] != colours(row)[1], ("grown-up row equal", row))
    for row in product(range(1, 5), repeat=4):
        red, blue = colours(row)
        if red == blue:
            for col in ("red", "blue"):
                check(all(a == b for _, a, b in plan_games(row, col)), row)
    print("  no grown-up row has equal colour totals; with equal totals either colour gives exactly a tie")
    # materials.pdf: page titles, orientation, strips; which strips the problems need
    pages = materials_strips()
    for i, (t, land, st) in enumerate(pages, 1):
        print(f"  materials page {i}: '{t}', {'landscape' if land else 'portrait'}, strips {st}")
    check(len(pages) == 3, "materials pages")
    check(pages[0][0] == "Strips of slots" and not pages[0][1] and sorted(pages[0][2]) == [3] * 5 + [4] * 5, "mat p1")
    check(pages[1][0].startswith("Strips of slots / Grades 4") and sorted(pages[1][2]) == [5, 6], "mat p2")
    check(pages[2][0] == "Colored strips" and pages[2][1] and sorted(pages[2][2]) == [4, 5, 6, 8], "mat p3")
    pairs = 5                     # two K-1, two 2-3, one 4-5 (context.md)
    cut = len(pages[0][2]) + len(pages[1][2]) + pairs * len(pages[2][2])
    cut_k1_skip = cut - 2 * 2    # two K-1 copies of page 3 skip the 8 and the 5
    print(f"  strips to cut: {cut} ({cut_k1_skip} if the K-1 copies of page 3 skip the 8 and 5); sheets {1 + 1 + pairs}")
    check((cut, cut_k1_skip) == (32, 28), "cut count")
    # problem -> strip lengths needed (plain on the plain set, colored on the colored set)
    need = {
        "K-1 plain": {len(x) for k in (1, 2, 3) for x in K1[k]} | {3, 4},     # P4 draws 3, P5 draws 4
        "K-1 colored": {len(x) for k in (6, 7, 8) for x in K1[k]},
        "2-3 plain": {len(x) for k in (1, 2, 3) for x in G23[k]} | {4},       # P4 boards are rows of 4
        "2-3 colored": {len(x) for k in (5, 6, 7, 8) for x in G23[k]} | {6},  # P9 boards are rows of 6
        "4-5 plain": {len(x) for k in (1, 2) for x in G45[k]} | {4} | {len(x) for x in G45[10]} | {len(G45[11])},
        "4-5 colored": {len(x) for k in (4, 6, 7, 8) for x in G45[k]} | {5},  # P9 asks about rows of five
    }
    plain_supplied = set(pages[0][2]) | set(pages[1][2])
    col_supplied = set(pages[2][2])
    for k, v in need.items():
        sup = plain_supplied if "plain" in k else col_supplied
        check(v <= sup, (k, v, sup))
        print(f"  {k}: rows of {sorted(v)} -> supplied")
    check(need["K-1 colored"] == {4, 6}, "K-1 colored 4 and 6 only")
    check({len(x) for x in G23[5]} == {6, 8} and {len(x) for x in G45[4]} == {6, 8}, "plan rows 6 and 8")
    check({len(x) for x in G23[8]} == {5} and {len(x) for x in G23[7]} == {4}, "2-3 P7/P8 lengths")
    check({len(x) for x in G45[6]} == {4} and {len(x) for x in G45[7] + G45[8]} == {5}, "4-5 P6-P8 lengths")
    # the per-band "Strips:" lines printed at the head of each band's solutions
    check({len(x) for k in (1, 2) for x in K1[k]} == {4} and {len(x) for x in K1[3]} == {3}, "K-1 P1-P3 plain 4 and 3")
    check({len(x) for x in G23[6]} == {6}, "2-3 P6 row of 6")
    check({len(x) for x in G45[10]} == {5} and len(G45[11]) == 6, "4-5 P10 rows of 5, P11 row of 6")
    check({len(x) for x in G45[1]} == {4} and {len(x) for x in G45[2]} == {3}, "4-5 P1-P2 plain 4 and 3")
    # packets: one per child plus a spare (context.md: 4 K-1, 4 grades 2-3, 3 grades 4-5)
    check((4 + 1, 4 + 1, 3 + 1) == (5, 5, 4), "packet counts")
    print("  per-band strip lists and packet counts (5, 5, 4) match")
    # cubes per pair: tallest tower and largest row total (K-1 copy stacks double a P7 row)
    allrows = [x for b in (K1, G23) for v in b.values() for x in v] + \
              [x for k, v in G45.items() if k != 11 for x in v] + [G45[11]]
    check(max(max(x) for x in allrows) <= 6 and max(sum(x) for x in allrows) == 18, "cube budget")
    check(2 * max(sum(x) for x in K1[7]) == 22, "K-1 copy stacks")
    print("  tallest printed tower <= 6, largest row 18 cubes, K-1 copy stacks 22: 30 cubes per pair suffice")


if __name__ == "__main__":
    # ---------------------------------------------------------- rows match the final page sources
    k1_rows = [r for k in sorted(K1) for r in K1[k]]
    # 2-3 intro draws the launch row twice (towers, then its number strip)
    g23_rows = [LAUNCH, LAUNCH] + [r for k in sorted(G23) for r in G23[k]]
    g23_rows.insert(g23_rows.index(G23[6][0]), LAUNCH)   # worked record in P6 precedes its row
    # 4-5: intro draws the launch row twice; P1-P2 are text tables; P11 is a labelled triangle
    g45_rows = [LAUNCH, LAUNCH] + [r for k in sorted(G45) if k not in (1, 2, 11) for r in G45[k]]
    import re as _re
    _src = open(PAGE_SRC + "/grades-4-5.tex").read()
    tables = [tuple(int(x) for x in m.split(", "))
              for m in _re.findall(r"^(\d(?:, \d)+) & first player", _src, _re.M)]
    check(tables == G45[1] + G45[2], "4-5 P1/P2 tables differ from page source")
    labels = [x.replace(",\\,", ", ") for x in _re.findall(
        r"\\node\[font=\\footnotesize, anchor=north\] at \([\d.]+,[\d.]+\) \{([\d,\\]+)\}", _src)]
    runs = sorted(", ".join(map(str, G45[11][i:i + k])) for k in range(1, 7) for i in range(7 - k))
    check(sorted(labels) == runs and len(labels) == 21, ("4-5 P11 boxes", labels))
    check(printed_rows("k-1.tex") == k1_rows, "K-1 rows differ from page source")
    check(printed_rows("grades-2-3.tex") == g23_rows, "2-3 rows differ from page source")
    check(printed_rows("grades-4-5.tex") == g45_rows, "4-5 rows differ from page source")
    print("rows used here match every row drawn in the three page sources")
    # ---------------------------------------------------------- general facts
    # recurrence total - min(two inner rows) agrees with brute-force game tree
    def brute(row):
        if not row:
            return 0
        return max(row[0] + sum(row[1:]) - brute(row[1:]),
                   row[-1] + sum(row[:-1]) - brute(row[:-1]))
    for n in range(1, 7):
        for r in product(range(1, 4), repeat=n):
            check(brute(r) == solve(r), r)
    # even rows: the colour plan collects exactly max(red, blue), never loses
    for n in (2, 4, 6):
        for r in product(range(1, 7) if n <= 4 else range(1, 5), repeat=n):
            red, blue = colours(r)
            col = "red" if red >= blue else "blue"
            for g, a, b in plan_games(r, col):
                check(a == max(red, blue), (r, g))
            check(len(plan_games(r, col)) == 2 ** (n // 2 - 1), r)
            check(solve(r) >= sum(r) - solve(r), r)
    print("even rows (2, 4 heights 1-6; 6 heights 1-4): plan collects max colour "
          "against all 2^(n/2-1) replies; never a first-player loss")
    # outline: 2,1,2,3 plan ties, best play wins 5-3 by taking the 3
    check(score((2, 1, 2, 3)) == (5, 3) and best_moves((2, 1, 2, 3)) == ["R"], "2123")
    # odd rows: blue > red => second wins; blue == red => first cannot win
    for n in (1, 3, 5):
        for r in product(range(1, 7), repeat=n):
            red, blue = colours(r)
            f, s = score(r)
            if blue > red:
                check(s > f, r)
            if blue == red:
                check(f <= s, r)
    print("odd rows 1,3,5 (heights 1-6): blue>red => second wins; equal => first never wins")
    # rows of three rule
    for r in product(range(1, 7), repeat=3):
        a, b, c = r
        o = outcome(r)
        check((o == "second") == (b > a + c), r)
        check((o == "tie") == (b == a + c), r)
    print("rows of three (1-6): second wins iff middle > ends together; tie iff equal")
    rows5 = list(product(range(1, 5), repeat=5))
    L5 = sum(outcome(r) == "second" for r in rows5)
    T5 = sum(outcome(r) == "tie" for r in rows5)
    print(f"rows of five heights 1-4: {len(rows5)} rows, first loses {L5}, ties {T5}")
    check((L5, T5) == (143, 147), "outline counts")
    rows5_6 = list(product(range(1, 7), repeat=5))
    lose_redheavy = [r for r in rows5_6 if outcome(r) == "second" and colours(r)[0] > colours(r)[1]]
    print(f"rows of five heights 1-6 with red > blue that first player loses: {len(lose_redheavy)}")

    # ---------------------------------------------------------- launch row
    print("\nLaunch row", fmt(LAUNCH), "best", score(LAUNCH), "colours", colours(LAUNCH))
    # demonstrated game: slots 4, 3, 1, 2 (the 2-3 P6 worked record)
    g = [4, 3, 1, 2]
    check(g in all_games(LAUNCH), "launch game legal")
    a = LAUNCH[3] + LAUNCH[0]
    b = LAUNCH[2] + LAUNCH[1]
    print(f"  demo game 4,3,1,2: first {a}, second {b}")
    check((a, b) == (5, 5), "launch tie")
    # launch row is not printed as a task row anywhere
    for band in (K1, G23, G45):
        for k, v in band.items():
            rows = [v] if k == 11 and band is G45 else v
            check(LAUNCH not in rows, ("launch row is a task row", k))

    # ---------------------------------------------------------- K-1
    print("\n=== K-1 ===")
    report("P1", K1[1])
    check([score(r) for r in K1[1]] == [(7, 5), (8, 3), (5, 5)], "K1 P1")
    check(after_first((5, 2, 1, 4), "R") == (6, 6), "K1 P1 row1 right ties")
    report("P2", K1[2])
    expect = ["L", "R", "L", "R", "L", "R"]
    for r, e in zip(K1[2], expect):
        check(best_moves(r) == [e], r)
        other = "R" if e == "L" else "L"
        f2, s2 = after_first(r, other)
        check(f2 <= s2, (r, "other move must not win"))
    # which winning towers are the shorter end
    print("  winning tower heights:", [r[0] if e == "L" else r[-1] for r, e in zip(K1[2], expect)])
    report("P3", K1[3])
    check([outcome(r) for r in K1[3]] == ["second", "first", "second", "first", "second"], "K1 P3")
    lose3 = [r for r in product(range(1, 6), repeat=3) if outcome(r) == "second"]
    print("P4 losing rows of three, heights 1-5:", len(lose3), [fmt(r) for r in lose3])
    check(len(lose3) == 10, "K1 P4 count")
    four5 = [r for r in product(range(1, 6), repeat=4) if outcome(r) == "second"]
    check(not four5, "K1 P5")
    print("P5 rows of four, heights 1-5, first loses:", len(four5))
    print("P6 grown-up first with plan:")
    for r in K1[6]:
        red, blue = colours(r)
        col = "red" if red > blue else "blue"
        start = 1 if col == "red" else len(r)
        games = plan_games(r, col)
        hauls = sorted(set((a, b) for _, a, b in games))
        gr = greedy_vs_best(r)
        print(f"  {fmt(r)}: red {red} blue {blue}, plan colour {col}, start slot {start} "
              f"(height {r[start - 1]}, other end {r[len(r) - start]}), plan hauls {hauls}, "
              f"best {score(r)}, taller-end grown-up vs best team {gr}")
        check(min(a - b for _, a, b in games) > 0, r)
    print("P7 child first:")
    for r in K1[7]:
        red, blue = colours(r)
        col = "red" if red > blue else "blue"
        start = 1 if col == "red" else len(r)
        games = plan_games(r, col)
        hauls = sorted(set((a, b) for _, a, b in games))
        print(f"  {fmt(r)}: red {red} blue {blue}, plan {col}, start slot {start} "
              f"(height {r[start - 1]}, other end {r[len(r) - start]}), plan hauls {hauls}, "
              f"best {score(r)}, best first moves {best_moves(r)}, "
              f"taller-end vs best {greedy_vs_best(r)}")
        check(all(a > b for _, a, b in games), r)
    report("P8", K1[8])
    check([outcome(r) for r in K1[8]] == ["first", "tie", "first"], "K1 P8")
    check([score(r) for r in K1[8]] == [(5, 3), (5, 5), (7, 5)], "K1 P8 scores")
    for r in K1[8]:
        print("   best first moves", fmt(r), best_moves(r), "colours", colours(r))

    # ---------------------------------------------------------- 2-3
    print("\n=== 2-3 ===")
    report("P1", G23[1])
    check([score(r) for r in G23[1]] == [(7, 5), (10, 5), (5, 5)], "23 P1")
    report("P2", G23[2])
    exp = ["L", "R", "R", "L"]
    for r, e in zip(G23[2], exp):
        check(best_moves(r) == [e], r)
        o = "R" if e == "L" else "L"
        check(after_first(r, o)[0] < after_first(r, o)[1], (r, "other loses"))
    report("P3", G23[3])
    check([outcome(r) for r in G23[3]] == ["second", "first", "second", "first", "tie", "second"], "23 P3")
    four6 = [r for r in product(range(1, 7), repeat=4) if outcome(r) == "second"]
    check(not four6, "23 P4 / 45 P3")
    print("P4: rows of four heights 1-6 lost by first player:", len(four6), "of", 6 ** 4)
    print("P5 plan rows:")
    for r in G23[5]:
        red, blue = colours(r)
        col = "red" if red > blue else "blue"
        games = plan_games(r, col)
        print(f"  {fmt(r)}: red {red} blue {blue}, plan {col}, start slot "
              f"{1 if col == 'red' else len(r)}, plan hauls {sorted(set((a, b) for _, a, b in games))}, "
              f"best {score(r)} first moves {best_moves(r)}")
        check(all(a == max(red, blue) for _, a, b in games), r)
    r = G23[6][0]
    red, blue = colours(r)
    print(f"P6 {fmt(r)}: red {red} blue {blue}")
    games = plan_games(r, "blue")
    for gseq, a, b in games:
        print("   ", "-".join(map(str, gseq)), f"{a}-{b}")
    check(len(games) == 4 and all((a, b) == (7, 6) for _, a, b in games), "23 P6")
    check(sorted(tuple(x[0]) for x in games) == sorted(
        [(6, 1, 2, 3, 4, 5), (6, 1, 2, 5, 4, 3), (6, 5, 4, 1, 2, 3), (6, 5, 4, 3, 2, 1)]), "23 P6 list")
    print("   best play", score(r), best_moves(r))
    print("   total legal games on a row of six:", len(all_games(r)))
    report("P7", G23[7])
    check([score(r) for r in G23[7]] == [(5, 3), (5, 5), (7, 5), (7, 7), (8, 6)], "23 P7")
    for r in G23[7]:
        print("   best first moves", fmt(r), best_moves(r))
    report("P8", G23[8])
    check([score(r) for r in G23[8]] == [(4, 7), (6, 5), (4, 8), (5, 5)], "23 P8")
    eq6 = [r for r in product(range(1, 7), repeat=6) if colours(r)[0] == colours(r)[1]]
    win6 = [r for r in eq6 if outcome(r) == "first"]
    print(f"P9: equal-colour rows of six heights 1-6: {len(eq6)}, first wins {len(win6)}")
    check((len(eq6), len(win6)) == (4332, 1974), "23 P9 counts")
    examples = [(1, 1, 1, 1, 3, 3), (3, 1, 1, 1, 1, 3), (1, 2, 1, 1, 3, 2),
                (2, 1, 2, 3, 1, 1), (1, 1, 2, 1, 2, 3), (4, 1, 2, 5, 1, 1)]
    for e in examples:
        print("   example", fmt(e), colours(e), score(e), outcome(e), best_moves(e))
    # extending a P7 winning row of four by two towers of equal height on the left
    ext = [(1, 1) + r for r in [(2, 1, 2, 3), (4, 1, 2, 5), (3, 2, 4, 5)]]
    for e in ext:
        print("   1,1 + P7 row", fmt(e), colours(e), score(e), outcome(e))
    # small-height count
    eq6s = [r for r in product(range(1, 4), repeat=6) if colours(r)[0] == colours(r)[1]]
    print("   heights 1-3: equal rows", len(eq6s), "first wins",
          sum(outcome(r) == "first" for r in eq6s))

    # ---------------------------------------------------------- 4-5
    print("\n=== 4-5 ===")
    report("P1", G45[1])
    check([score(r) for r in G45[1]] == [(7, 4), (7, 6), (5, 5), (8, 6)], "45 P1")
    report("P2", G45[2])
    check([score(r) for r in G45[2]] == [(2, 5), (6, 5), (5, 6), (5, 4), (5, 5), (7, 2)], "45 P2")
    print("P4 plan rows: as 2-3 P5")
    check(G45[4] == G23[5], "same rows")
    report("P6", G45[6])
    check([score(r) for r in G45[6]] == [(5, 3), (5, 5), (7, 5), (7, 7), (4, 4), (6, 4)], "45 P6")
    for r in G45[6]:
        print("   best first moves", fmt(r), best_moves(r), "colours", colours(r))
    report("P7", G45[7])
    check([score(r) for r in G45[7]] == [(4, 8), (5, 8), (6, 9), (5, 6)], "45 P7")
    for r in G45[7]:
        check(colours(r)[1] > colours(r)[0], r)
    report("P8", G45[8])
    check([score(r) for r in G45[8]] == [(6, 5), (5, 5), (4, 7), (7, 6), (7, 9)], "45 P8")
    report("P10", G45[10])
    check([score(r) for r in G45[10]] == [(7, 7), (7, 6), (8, 9)], "45 P10")
    check([best_moves(r) for r in G45[10]] == [["R"], ["L"], ["L"]], "45 P10 moves")
    for r in G45[10]:
        print("   greedy both sides:", fmt(r), end=" ")
        rr = list(r); a = b = 0; t = 0
        while rr:
            x = rr.pop(0) if rr[0] >= rr[-1] else rr.pop()
            if t == 0: a += x
            else: b += x
            t ^= 1
        print(a, b)
    row = G45[11]
    T = triangle(row)
    print("P11 triangle (length: values left to right):")
    for k in range(len(row), 0, -1):
        vals = [T[(i, k)] for i in range(len(row) - k + 1)]
        print("  ", k, vals)
    check([T[(i, 1)] for i in range(6)] == [2, 3, 6, 2, 1, 4], "t1")
    check([T[(i, 2)] for i in range(5)] == [3, 6, 6, 2, 4], "t2")
    check([T[(i, 3)] for i in range(4)] == [8, 5, 7, 5], "t3")
    check([T[(i, 4)] for i in range(3)] == [8, 7, 8], "t4")
    check([T[(i, 5)] for i in range(2)] == [7, 9], "t5")
    check(T[(0, 6)] == 11, "t6")
    # each box = its row total minus the smaller of the two boxes below it
    for k in range(2, 7):
        for i in range(7 - k):
            check(T[(i, k)] == sum(row[i:i + k]) - min(T[(i + 1, k - 1)], T[(i, k - 1)]), (i, k))
    print("   whole row", score(row), "colours", colours(row), "first moves", best_moves(row),
          "take slot 1 ->", after_first(row, "L"))

    # ---------------------------------------------------------- extra facts quoted in the guide
    print("\n=== extra facts ===")
    # winning first move in K-1 P2 and 2-3 P2 stands on the colour with more cubes
    for r in K1[2] + G23[2]:
        red, blue = colours(r)
        m = best_moves(r)[0]
        check((m == "L") == (red > blue), ("P2 colour match", r))
    print("K-1 P2 and 2-3 P2: every winning first tower stands on the colour with more cubes")
    # 2-3 P6: choosing red instead loses
    r = G23[6][0]
    red_games = plan_games(r, "red")
    print("2-3 P6 with red plan:", [(("-".join(map(str, g))), a, b) for g, a, b in red_games])
    check(len(red_games) == 4 and all((a, b) == (6, 7) for _, a, b in red_games), "red plan")
    # 4-5 P9: an equal-colour row of five that ties, and one the second player wins
    for e in [(1, 2, 2, 2, 1), (2, 2, 1, 2, 1)]:
        print("  equal row of five", fmt(e), colours(e), score(e), outcome(e))
    check(colours((1, 2, 2, 2, 1)) == (4, 4) and score((1, 2, 2, 2, 1)) == (4, 4), "tie example")
    # K-1 P4 middle 3 only 1,3,1
    check([r for r in product(range(1, 6), repeat=3) if outcome(r) == "second" and r[1] == 3] == [(1, 3, 1)], "mid3")
    # four-row candidates: count of rows of four (1-6) that are first-player ties
    ties4 = sum(outcome(r) == "tie" for r in product(range(1, 7), repeat=4))
    print("rows of four heights 1-6 that tie:", ties4)
    # K-1 cube budget: row total + a copy of every tower for comparing colours
    print("largest K-1 P7 row total:", max(sum(r) for r in K1[7]))
    allrows = [x for b in (K1, G23) for v in b.values() for x in v] + \
              [x for k, v in G45.items() if k != 11 for x in v] + [G45[11]]
    print("largest printed row total:", max(sum(x) for x in allrows))
    # taller-end claims quoted in the guide (first move, then best play; and always-taller-end)
    check(after_first((1, 2, 5, 2), "R") == (4, 6) and greedy_vs_best((1, 2, 5, 2)) == (4, 6), "K1 P6 r1")
    check(after_first((3, 4, 1, 2), "L") == (5, 5) and greedy_vs_best((3, 4, 1, 2)) == (5, 5), "K1 P6 r2")
    check(after_first((2, 4, 1, 1), "L") == (3, 5), "K1 P7 r2")
    check(score((3, 1, 2, 5)) == (7, 4), "K1 P7 r1 best")
    # every alternative-move score printed in the guide
    A = after_first
    check(A((1, 5, 2, 3), "L") == (4, 7), "K1 P1 r2 alt")
    check([A(r, "R" if e == "L" else "L") for r, e in zip(K1[2], ["L", "R", "L", "R", "L", "R"])]
          == [(5, 6), (5, 6), (3, 6), (3, 6), (5, 6), (5, 5)], "K1 P2 alts")
    check([score(r) for r in K1[2]] == [(7, 4), (7, 4), (6, 3), (6, 3), (8, 3), (7, 3)], "K1 P2 scores")
    check([score(r) for r in K1[3]] == [(2, 5), (6, 5), (3, 4), (5, 4), (4, 5)], "K1 P3 scores")
    check([sorted(set((a, b) for _, a, b in plan_games(r, "red" if colours(r)[0] > colours(r)[1] else "blue")))
           for r in K1[6]] == [[(6, 4)], [(6, 4)], [(9, 3)], [(7, 3)]], "grown-up card hauls")
    check([sorted(set((a, b) for _, a, b in plan_games(r, "red" if colours(r)[0] > colours(r)[1] else "blue")))
           for r in K1[7]] == [[(6, 5)], [(5, 3)], [(6, 5)], [(6, 5)]], "K1 P7 plan hauls")
    check([colours(r) for r in K1[7]] == [(5, 6), (3, 5), (6, 5), (5, 6)], "K1 P7 colours")
    check([colours(r) for r in K1[6]] == [(6, 4), (4, 6), (9, 3), (3, 7)], "K1 P6 colours")
    check([A(r, "L") for r in K1[8]] == [(4, 4), (5, 5), (6, 6)], "K1 P8 slot-1 ties")
    check(A((5, 2, 1, 4), "R") == (6, 6) and A((2, 6, 3, 4), "L") == (6, 9), "23 P1 alts")
    check([A(r, "R" if e == "L" else "L") for r, e in zip(G23[2], ["L", "R", "R", "L"])]
          == [(5, 6), (5, 7), (5, 6), (6, 7)], "23 P2 alts")
    check([score(r) for r in G23[2]] == [(7, 4), (8, 4), (8, 3), (7, 6)], "23 P2 scores")
    check([score(r) for r in G23[3]] == [(2, 5), (6, 5), (5, 6), (5, 4), (5, 5), (5, 6)], "23 P3 scores")
    check([sorted(set((a, b) for _, a, b in plan_games(r, "red" if colours(r)[0] > colours(r)[1] else "blue")))
           for r in G23[5]] == [[(9, 5)], [(7, 6)], [(9, 6)]], "23 P5 plan hauls")
    check([colours(r) for r in G23[5]] == [(9, 5), (6, 7), (9, 6)], "23 P5 colours")
    check(score((3, 1, 1, 4, 2, 2)) == (8, 5) and best_moves((3, 1, 1, 4, 2, 2)) == ["L"], "23 P5 r2 best")
    check([A(r, "L") for r in (G23[7][0], G23[7][2], G23[7][4])] == [(4, 4), (6, 6), (7, 7)], "23 P7 slot-1 ties")
    for e, sc, mv in [((2, 1, 2, 3, 1, 1), (6, 4), ["L"]), ((1, 1, 2, 1, 2, 3), (6, 4), ["R"]),
                      ((1, 1, 4, 1, 2, 5), (10, 4), None), ((1, 1, 3, 2, 4, 5), (9, 7), None)]:
        check(colours(e)[0] == colours(e)[1] and score(e) == sc and (mv is None or best_moves(e) == mv), e)
    for e in [(1, 1, 1, 1, 3, 3), (3, 1, 1, 1, 1, 3)]:
        check(colours(e)[0] == colours(e)[1] and outcome(e) == "tie", e)
    check(A((6, 2, 1, 5), "R") == (7, 7), "45 P1 alt")
    check(A((4, 2, 1, 3), "R") == (5, 5) and best_moves((4, 2, 1, 3)) == ["L"], "45 P6 alt")
    check([A(r, "L") for r in G45[10]] == [(5, 9), (7, 6), (8, 9)], "45 P10 left")
    check([A(r, "R") for r in G45[10]] == [(7, 7), (6, 7), (6, 11)], "45 P10 right")
    check(A(G45[11], "L") == (9, 9) and A(G45[11], "R") == (11, 7), "45 P11 moves")
    check(solve((2, 3, 6, 2, 1)) == 7 and solve((3, 6, 2, 1, 4)) == 9, "45 P11 inner")
    check(colours(G45[11]) == (9, 9) and sum(G45[11]) == 18, "45 P11 colours")
    def greedy_both(r):
        rr = list(r); a = b = 0; t = 0
        while rr:
            x = rr.pop(0) if rr[0] >= rr[-1] else rr.pop()
            if t == 0:
                a += x
            else:
                b += x
            t ^= 1
        return a, b
    check(greedy_both((2, 1, 2, 5, 3)) == (6, 7), "45 P10 greedy")
    print("every alternative score, plan haul and example printed in the guide re-checked")

    # ---------------------------------------------------------- revision (final/) checks
    print("\n=== revision checks (final guide) ===")
    revision_checks()
    print("\nall guide checks passed")
