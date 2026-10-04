"""Recompute every answer printed in the adult guide from the student pages themselves.

The machines are read from the drawn coordinates in ../src/fig/*.tex (the files the final
student PDFs are built from); which figure belongs to which problem is read from the packet
sources ../src/*.tex.  Nothing is taken from figures.py, machines.py or the reviews.

Run:  python3 check_answers.py      (prints every answer; exits non-zero if a printed answer is wrong)

Conventions: slots are numbered 1, 2, 3, ... from the left.  A machine is written as the list of
arrow targets: [3, 1, 2] means slot 1 -> 3, slot 2 -> 1, slot 3 -> 2.  "A then B" is one turn of A
followed by one turn of B.
"""
import math
import os
import re
import sys
from collections import Counter, defaultdict
from functools import reduce
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src")
FIG = os.path.join(SRC, "fig")
EPS = 0.006

COLOUR = {"pbgreen": "green", "pbblue": "blue", "pbred": "red", "pbyellow": "yellow",
          "pbpurple": "purple", "pbpink": "pink", "pbteal": "teal", "pbgray": "gray"}

FAILURES = []
SEEN_MACHINES = set()   # every machine (1-indexed targets) computed or read from the pages and confirmed
SEEN_LOOPS = set()      # every loop (tuple of slots) computed and confirmed


def _collect(x):
    if isinstance(x, (list, tuple)) and x and all(isinstance(v, int) for v in x):
        if sorted(x) == list(range(1, len(x) + 1)) and isinstance(x, list):
            SEEN_MACHINES.add(tuple(x))
        if isinstance(x, tuple):
            SEEN_LOOPS.add(x)
    if isinstance(x, (list, tuple, set)):
        for v in x:
            _collect(v)
    if isinstance(x, dict):
        for k, v in x.items():
            _collect(k)
            _collect(v)


def example(ex, turns):
    """A machine printed in the guide as an example: check its number of turns, then record it."""
    p = [e - 1 for e in ex]
    expect(f"  example {arrows_str(p)} takes {turns} turns", order(p), turns)
    if order(p) == turns:
        SEEN_MACHINES.add(tuple(ex))


def expect(label, got, want):
    ok = got == want
    if ok:
        _collect(got)
    print(f"  [{'ok' if ok else 'FAIL'}] {label}: {got}" + ("" if ok else f"   (guide says {want})"))
    if not ok:
        FAILURES.append(label)


# ----------------------------------------------------------------------------------------------
# reading the pages

def problems_of(packet):
    """Map figure name -> problem number, in page order, from a packet's .tex source."""
    text = open(os.path.join(SRC, packet + ".tex")).read()
    text = text.split("\\begin{document}", 1)[1]
    out, prob = {}, 0
    for m in re.finditer(r"\\problem\{|\\fig(?:\[[^\]]*\])?\{([^}]*)\}", text):
        if m.group(0).startswith("\\problem"):
            prob += 1
        else:
            out[m.group(1)] = prob
    return out, prob


NUM = r"(-?\d+\.\d+)"


def parse_fig(name):
    t = open(os.path.join(FIG, name + ".tex")).read()
    rects = [tuple(map(float, m)) for m in re.findall(
        r"fill=slotfill\] \(" + NUM + "," + NUM + r"\) rectangle \(" + NUM + "," + NUM + r"\)", t)]
    arrows = []
    for line in t.splitlines():
        if "Stealth" in line:
            pts = [tuple(map(float, p)) for p in re.findall(r"\(" + NUM + "," + NUM + r"\)", line)]
            arrows.append((pts[0], pts[-1]))
    icons = []
    for m in re.finditer(r"\\filldraw\[fill=(pb\w+)[^\]]*\] (.*?) -- cycle;", t):
        pts = [tuple(map(float, p)) for p in re.findall(r"\(" + NUM + "," + NUM + r"\)", m.group(2))]
        icons.append((COLOUR[m.group(1)], sum(x for x, _ in pts) / len(pts), min(y for _, y in pts)))
    labels = [(float(x), float(y), s) for x, y, s in re.findall(
        r"\\node\[[^\]]*\] at \(" + NUM + "," + NUM + r"\) \{(.*)\};", t)]
    return rects, arrows, icons, labels


def rows_of(rects):
    """Group slot squares into rows of one mat: same y, same size, evenly spaced."""
    by_y = defaultdict(list)
    for x0, y0, x1, y1 in rects:
        by_y[(round(y0, 2), round(y1, 2))].append((x0, x1))
    rows = []
    for (y0, y1), xs in by_y.items():
        xs.sort()
        cur = [xs[0]]
        for a, b in zip(xs, xs[1:]):
            if b[0] - a[1] > 0.18:
                rows.append((y0, y1, cur))
                cur = []
            cur.append(b)
        rows.append((y0, y1, cur))
    return rows


class Mat:
    def __init__(self, top, bottom):
        self.top, self.bottom = top, bottom          # (y0, y1, [(x0, x1), ...])
        self.n = len(top[2])
        self.targets = [None] * self.n
        self.pictures = [None] * self.n
        self.label = None

    def slot_at(self, row, x):
        for i, (x0, x1) in enumerate(row[2]):
            if x0 - EPS <= x <= x1 + EPS:
                return i
        return None

    @property
    def perm(self):
        return None if None in self.targets else list(self.targets)

    @property
    def bbox(self):
        return (self.top[2][0][0], self.bottom[0], self.top[2][-1][1], self.top[1])


def mats_of(name):
    rects, arrows, icons, labels = parse_fig(name)
    rows = rows_of(rects)
    mats = []
    used = set()
    # pair each row with the nearest row below it that has the same slots
    for i, r in sorted(enumerate(rows), key=lambda t: -t[1][0]):
        if i in used:
            continue
        below = [(j, s) for j, s in enumerate(rows) if j not in used and j != i and s[0] < r[0]
                 and len(s[2]) == len(r[2]) and all(abs(a[0] - b[0]) < EPS for a, b in zip(s[2], r[2]))]
        if not below:
            continue
        j, s = max(below, key=lambda t: t[1][0])
        used |= {i, j}
        mats.append(Mat(r, s))
    for (xs, ys), (xe, ye) in arrows:
        hits = []
        for m in mats:
            if abs(ys - m.top[0]) < EPS and abs(ye - m.bottom[1]) < EPS:
                a, b = m.slot_at(m.top, xs), m.slot_at(m.bottom, xe)
                if a is not None and b is not None:
                    hits.append((m, a, b))
        assert len(hits) == 1, (name, xs, ys, xe, ye)
        m, a, b = hits[0]
        assert m.targets[a] is None, (name, "two arrows leave one slot")
        m.targets[a] = b
    for colour, cx, ybot in icons:
        for m in mats:
            if m.top[1] - EPS <= ybot <= m.top[1] + 0.2:
                k = m.slot_at(m.top, cx)
                if k is not None:
                    m.pictures[k] = colour
    for x, y, s in labels:
        best = min(mats, key=lambda m: dist_to_box(x, y, m.bbox))
        if dist_to_box(x, y, best.bbox) < 0.6:
            best.label = (best.label + " / " + s) if best.label else s
    mats.sort(key=lambda m: (-round(m.top[0], 1), m.top[2][0][0]))
    for m in mats:
        if m.perm is not None:
            assert sorted(m.perm) == list(range(m.n)), (name, m.targets)
    return mats


def dist_to_box(x, y, box):
    x0, y0, x1, y1 = box
    dx = max(x0 - x, 0, x - x1)
    dy = max(y0 - y, 0, y - y1)
    return math.hypot(dx, dy)


# ----------------------------------------------------------------------------------------------
# machines

def one(p):
    return [t + 1 for t in p]


def arrows_str(p):
    return ", ".join(f"{i + 1}->{j + 1}" for i, j in enumerate(p))


def turn(row, p):
    """row[slot] = block; move every block down its arrow, slide the row up."""
    new = [None] * len(p)
    for slot, blk in enumerate(row):
        new[p[slot]] = blk
    return new


def run_until_home(p, row):
    """Rows after each turn, until the row is back in its starting order."""
    seq, cur = [row], turn(row, p)
    while cur != row:
        seq.append(cur)
        cur = turn(cur, p)
    seq.append(cur)
    return seq


def home_times(p, row):
    """For each slot's block, the first turn after which it is back in its own slot (by simulation)."""
    out, cur, t = [None] * len(p), list(row), 0
    while None in out:
        cur = turn(cur, p)
        t += 1
        for i, b in enumerate(row):
            if out[i] is None and cur[i] == b:
                out[i] = t
    return out


def order(p):
    return len(run_until_home(p, list(range(len(p))))) - 1


def loops(p):
    seen, out = set(), []
    for i in range(len(p)):
        if i not in seen:
            c, j = [], i
            while j not in seen:
                seen.add(j)
                c.append(j + 1)
                j = p[j]
            out.append(tuple(c))
    return out


def loop_lengths(p):
    return sorted(len(c) for c in loops(p))


def then(a, b):
    return [b[a[i]] for i in range(len(a))]


def undo(p):
    q = [0] * len(p)
    for i, j in enumerate(p):
        q[j] = i
    return q


def lcm(a, b):
    return a * b // math.gcd(a, b)


def partitions(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield []
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield [k] + r


def orders_for(n):
    return sorted({order(list(q)) for q in permutations(range(n))})


# ----------------------------------------------------------------------------------------------

def figs(packet):
    fmap, nprob = problems_of(packet)
    byprob = defaultdict(list)
    for f, pr in fmap.items():
        byprob[pr].append(f)
    return byprob, nprob


def machines_in(fignames):
    out = []
    for f in fignames:
        for m in mats_of(f):
            out.append((f, m))
    return out


def check_k1():
    print("\n=== K-1 ===")
    byprob, nprob = figs("k-1")
    expect("number of problems", nprob, 8)

    print("Problem 1")
    ms = [m for _, m in machines_in(byprob[1])]
    expect("P1 machines", [one(m.perm) for m in ms], [[3, 1, 2], [1, 3, 2]])
    for m, rows, t in zip(ms, ([["blue", "red", "green"], ["red", "green", "blue"], ["green", "blue", "red"]],
                             [["green", "red", "blue"], ["green", "blue", "red"]]), (3, 2)):
        seq = run_until_home(m.perm, m.pictures)
        expect(f"  {arrows_str(m.perm)} turns", len(seq) - 1, t)
        expect("  rows after each turn", seq[1:], rows)

    print("Problem 2")
    ms = [m for _, m in machines_in(byprob[2])]
    expect("P2 machines", [one(m.perm) for m in ms], [[3, 4, 2, 1], [3, 4, 1, 2]])
    want_rows = [
        [["yellow", "red", "green", "blue"], ["blue", "green", "yellow", "red"],
         ["red", "yellow", "blue", "green"], ["green", "blue", "red", "yellow"]],
        [["red", "yellow", "green", "blue"], ["green", "blue", "red", "yellow"]],
    ]
    for m, rows in zip(ms, want_rows):
        seq = run_until_home(m.perm, m.pictures)
        expect(f"  {arrows_str(m.perm)} turns", len(seq) - 1, len(rows))
        expect("  rows", seq[1:], rows)
        expect("  loops", loops(m.perm), {4: [(1, 3, 2, 4)], 2: [(1, 3), (2, 4)]}[len(rows)])

    print("Problem 3")
    ms = [m for _, m in machines_in(byprob[3])]
    expect("P3 machines", [one(m.perm) for m in ms], [[2, 4, 3, 1], [3, 4, 1, 5, 2]])
    expect("  4-slot turns", order(ms[0].perm), 3)
    expect("  4-slot loops", loops(ms[0].perm), [(1, 2, 4), (3,)])
    expect("  4-slot rows", run_until_home(ms[0].perm, ms[0].pictures)[1:],
           [["yellow", "green", "red", "blue"], ["blue", "yellow", "red", "green"], ["green", "blue", "red", "yellow"]])
    expect("  5-slot turns", order(ms[1].perm), 6)
    expect("  5-slot loops", loops(ms[1].perm), [(1, 3), (2, 4, 5)])
    expect("  5-slot home times per block", home_times(ms[1].perm, ms[1].pictures), [2, 3, 2, 3, 3])
    expect("  5-slot rows", run_until_home(ms[1].perm, ms[1].pictures)[1:], [
        ["red", "purple", "green", "blue", "yellow"],
        ["green", "yellow", "red", "purple", "blue"],
        ["red", "blue", "green", "yellow", "purple"],
        ["green", "purple", "red", "blue", "yellow"],
        ["red", "yellow", "green", "purple", "blue"],
        ["green", "blue", "red", "yellow", "purple"]])

    print("Problem 4")
    labels = sorted(s for fg in byprob[4] for _, _, s in parse_fig(fg)[3])
    expect("  targets printed beside the mats", labels, ["2 turns", "3 turns", "4 turns"])
    blanks = [m for _, m in machines_in(byprob[4])]
    expect("  blank 4-slot mats", [(m.n, m.perm) for m in blanks], [(4, None)] * 3)
    c4 = Counter(order(list(q)) for q in permutations(range(4)))
    expect("  4-slot machines by turns", dict(sorted(c4.items())), {1: 1, 2: 9, 3: 8, 4: 6})
    for t, ex in ((2, [2, 1, 3, 4]), (3, [2, 3, 1, 4]), (4, [2, 3, 4, 1])):
        example(ex, t)

    print("Problem 5")
    bad = [q for n in range(1, 8) for q in permutations(range(n)) if sum(q[i] != i for i in range(n)) == 1]
    expect("  machines (1..7 slots) with exactly one block in a new slot", len(bad), 0)
    expect("  smallest possible number of blocks that end up in a new slot (other than 0)",
           min(sum(q[i] != i for i in range(4)) for q in permutations(range(4)) if list(q) != [0, 1, 2, 3]), 2)

    print("Problem 6")
    (fa, a), (fb, b) = machines_in(byprob[6])
    expect("  first machine", one(a.perm), [4, 3, 1, 2])
    expect("  second mat is blank", b.perm, None)
    row1 = turn(a.pictures, a.perm)
    expect("  row after one turn", row1, ["red", "yellow", "blue", "green"])
    sols = [one(list(q)) for q in permutations(range(4)) if turn(row1, list(q)) == b.pictures]
    expect("  machines on the second mat that put every block home", sols, [[3, 4, 2, 1]])
    expect("  equals the first machine with arrows reversed", sols[0], one(undo(a.perm)))

    print("Problem 7")
    ms = [m for _, m in machines_in(byprob[7])]
    expect("  blank 3-slot mats printed", len(ms), 9)
    all3 = sorted(one(list(q)) for q in permutations(range(3)))
    expect("  all 3-slot machines", all3, [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
    expect("  their turns", [order([x - 1 for x in q]) for q in all3], [1, 2, 2, 3, 3, 2])

    print("Problem 8")
    ms = [m for _, m in machines_in(byprob[8])]
    expect("  blank 5-slot mats", [(m.n, m.perm) for m in ms], [(5, None), (5, None)])
    six = [q for q in permutations(range(5)) if order(list(q)) == 6]
    expect("  5-slot machines taking 6 turns", len(six), 20)
    expect("  all have loops 2 and 3", {tuple(loop_lengths(list(q))) for q in six}, {(2, 3)})
    p3 = [m for _, m in machines_in(byprob[3])][1].perm
    expect("  other than the Problem 3 machine", sum(1 for q in six if list(q) != p3), 19)
    for ex in ([2, 1, 4, 5, 3], [3, 4, 5, 2, 1]):
        example(ex, 6)


def check_m23():
    print("\n=== Grades 2-3 ===")
    byprob, nprob = figs("grades-2-3")
    expect("number of problems", nprob, 8)

    print("Problem 1")
    ms = [m for _, m in machines_in(byprob[1])]
    expect("  machines", [one(m.perm) for m in ms], [[4, 2, 1, 3], [3, 5, 4, 1, 2]])
    expect("  per-block home times, machine 1", home_times(ms[0].perm, ms[0].pictures), [3, 1, 3, 3])
    expect("  all blocks, machine 1", order(ms[0].perm), 3)
    expect("  per-block home times, machine 2", home_times(ms[1].perm, ms[1].pictures), [3, 2, 3, 3, 2])
    expect("  all blocks, machine 2", order(ms[1].perm), 6)
    expect("  loops", [loops(m.perm) for m in ms], [[(1, 4, 3), (2,)], [(1, 3, 4), (2, 5)]])

    print("Problem 2")
    ms = [m for _, m in machines_in(byprob[2])]
    expect("  machines", [one(m.perm) for m in ms],
           [[2, 5, 1, 4, 3], [4, 3, 6, 1, 2, 5], [4, 1, 6, 2, 3, 5], [5, 6, 3, 1, 4, 2]])
    expect("  loops", [loops(m.perm) for m in ms],
           [[(1, 2, 5, 3), (4,)], [(1, 4), (2, 3, 6, 5)], [(1, 4, 2), (3, 6, 5)], [(1, 5, 4), (2, 6), (3,)]])
    expect("  turns", [order(m.perm) for m in ms], [4, 4, 3, 6])
    expect("  pictures on the 6-slot mats", ms[1].pictures, ["green", "blue", "red", "yellow", "purple", "pink"])

    print("Problem 3")
    expect("  turns possible with 5 slots", orders_for(5), [1, 2, 3, 4, 5, 6])
    for ex, t in (([1, 2, 3, 4, 5], 1), ([2, 1, 3, 4, 5], 2), ([2, 3, 1, 4, 5], 3), ([2, 3, 4, 1, 5], 4),
                  ([2, 3, 4, 5, 1], 5), ([2, 1, 4, 5, 3], 6)):
        example(ex, t)
    c5 = Counter(order(list(q)) for q in permutations(range(5)))
    expect("  5-slot machines by turns", dict(sorted(c5.items())), {1: 1, 2: 25, 3: 20, 4: 30, 5: 24, 6: 20})

    print("Problem 4")
    pairs = machines_in(byprob[4])
    arrowed = [m for _, m in pairs if m.perm]
    blanks = [m for _, m in pairs if not m.perm]
    expect("  machines with arrows", [one(m.perm) for m in arrowed], [[2, 4, 1, 3], [5, 1, 4, 3, 2]])
    for m, bl, row_want, sol_want in zip(arrowed, blanks,
                                         (["red", "green", "yellow", "blue"], ["blue", "purple", "yellow", "red", "green"]),
                                         ([3, 1, 4, 2], [2, 5, 4, 3, 1])):
        r = turn(m.pictures, m.perm)
        expect("  row after one turn", r, row_want)
        sols = [one(list(q)) for q in permutations(range(m.n)) if turn(r, list(q)) == bl.pictures]
        expect("  arrows for the empty machine (all solutions)", sols, [sol_want])
        expect("  = arrows reversed", sol_want, one(undo(m.perm)))
        expect("  same number of turns as the machine", order([s - 1 for s in sol_want]), order(m.perm))

    print("Problem 5")
    selfundo = [list(q) for q in permutations(range(5)) if then(list(q), list(q)) == list(range(5))]
    expect("  5-slot machines that undo themselves", len(selfundo), 26)
    expect("  their loop lengths", sorted({tuple(loop_lengths(q)) for q in selfundo}),
           [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2)])
    expect("  counts: none / one swap / two swaps",
           [sum(1 for q in selfundo if loop_lengths(q) == L) for L in ([1] * 5, [1, 1, 1, 2], [1, 2, 2])], [1, 10, 15])
    expect("  undoes itself <=> every loop has 1 or 2 slots (all 5-slot machines)",
           all((then(list(q), list(q)) == list(range(5))) == (max(loop_lengths(list(q))) <= 2)
               for q in permutations(range(5))), True)

    print("Problem 6")
    for f, want in (("m-p6a", ([2, 1, 3, 4], [1, 3, 2, 4],
                               ["blue", "red", "green", "yellow"], ["red", "green", "blue", "yellow"], False)),
                    ("m-p6b", ([3, 2, 1, 4], [1, 4, 3, 2],
                               ["red", "yellow", "green", "blue"], ["red", "yellow", "green", "blue"], True))):
        ms = mats_of(f)
        A = [m for m in ms if m.perm and m.label == "A"][0]
        B = [m for m in ms if m.perm and m.label == "B"][0]
        expect(f"  {f} A", one(A.perm), want[0])
        expect(f"  {f} B", one(B.perm), want[1])
        ab = turn(turn(A.pictures, A.perm), B.perm)
        ba = turn(turn(B.pictures, B.perm), A.perm)
        expect(f"  {f} row A then B", ab, want[2])
        expect(f"  {f} row B then A", ba, want[3])
        expect(f"  {f} rows the same", ab == ba, want[4])
        # the two 4-box record rows are read as one blank "mat" carrying both labels
        rec = [m for m in ms if not m.perm]
        expect(f"  {f} record rows", [(m.n, m.label) for m in rec], [(4, "A then B / B then A")])

    print("Problem 7")
    expect("  turns possible with 6 slots", orders_for(6), [1, 2, 3, 4, 5, 6])
    expect("  blank 6-slot mats printed", len([m for _, m in machines_in(byprob[7])]), 8)
    table = {tuple(pt): reduce(lcm, pt, 1) for pt in partitions(6)}
    print("  loop splits of 6:", table)
    expect("  number of loop splits of 6", len(table), 11)

    print("Problem 8")
    big = Counter(tuple(loop_lengths(list(q))) for q in permutations(range(7)) if order(list(q)) > 10)
    expect("  7-slot machines over 10 turns, by loops", dict(big), {(3, 4): 420})
    expect("  most turns with 7 slots", max(order(list(q)) for q in permutations(range(7))), 12)
    table = {tuple(pt): reduce(lcm, pt, 1) for pt in partitions(7)}
    print("  loop splits of 7:", table)
    example([2, 3, 1, 5, 6, 7, 4], 12)


def check_u45():
    print("\n=== Grades 4-5 ===")
    byprob, nprob = figs("grades-4-5")
    expect("number of problems (figures reach P8; P9, P10 have none)", nprob, 10)

    print("Problem 1")
    ms = [m for _, m in machines_in(byprob[1])]
    expect("  machines", [one(m.perm) for m in ms], [[3, 2, 5, 1, 4], [5, 4, 1, 2, 3]])
    expect("  per-block, machine 1", home_times(ms[0].perm, ms[0].pictures), [4, 1, 4, 4, 4])
    expect("  all, machine 1", order(ms[0].perm), 4)
    expect("  per-block, machine 2", home_times(ms[1].perm, ms[1].pictures), [3, 2, 3, 2, 3])
    expect("  all, machine 2", order(ms[1].perm), 6)
    expect("  loops", [loops(m.perm) for m in ms], [[(1, 3, 5, 4), (2,)], [(1, 5, 3), (2, 4)]])

    print("Problem 2")
    ms = [m for _, m in machines_in(byprob[2])]
    expect("  slots", [m.n for m in ms], [6, 6, 7, 7, 8, 8])
    expect("  machines", [one(m.perm) for m in ms], [
        [3, 6, 5, 2, 1, 4], [5, 3, 6, 4, 1, 2], [4, 5, 6, 7, 1, 3, 2],
        [4, 7, 5, 2, 6, 1, 3], [3, 5, 2, 8, 7, 1, 6, 4], [3, 5, 6, 2, 7, 8, 4, 1]])
    expect("  loop lengths", [loop_lengths(m.perm) for m in ms],
           [[3, 3], [1, 2, 3], [2, 5], [7], [2, 6], [4, 4]])
    expect("  turns", [order(m.perm) for m in ms], [3, 6, 10, 7, 6, 4])
    expect("  loops", [loops(m.perm) for m in ms], [
        [(1, 3, 5), (2, 6, 4)], [(1, 5), (2, 3, 6), (4,)], [(1, 4, 7, 2, 5), (3, 6)],
        [(1, 4, 2, 7, 3, 5, 6)], [(1, 3, 2, 5, 7, 6), (4, 8)], [(1, 3, 6, 8), (2, 5, 7, 4)]])

    print("Problem 3")
    expect("  turns possible with 5 slots", orders_for(5), [1, 2, 3, 4, 5, 6])
    table = {tuple(pt): reduce(lcm, pt, 1) for pt in partitions(5)}
    expect("  loop splits of 5", table, {(5,): 5, (4, 1): 4, (3, 2): 6, (3, 1, 1): 3, (2, 2, 1): 2,
                                         (2, 1, 1, 1): 2, (1, 1, 1, 1, 1): 1})
    expect("  mats printed", len([m for _, m in machines_in(byprob[3])]), 9)

    print("Problem 4")
    expect("  most turns, 6 slots", max(order(list(q)) for q in permutations(range(6))), 6)
    expect("  6-slot loop splits reaching 6", sorted(tuple(pt) for pt in partitions(6) if reduce(lcm, pt, 1) == 6),
           [(3, 2, 1), (6,)])
    expect("  most turns, 7 slots", max(order(list(q)) for q in permutations(range(7))), 12)
    expect("  7-slot loop splits reaching 12", [tuple(pt) for pt in partitions(7) if reduce(lcm, pt, 1) == 12], [(4, 3)])

    print("Problem 5")
    def lay_out_and_shuffle(row):
        h = len(row) // 2
        top, bot = row[:h], row[h:]
        out = []
        for a, b in zip(top, bot):
            out += [a, b]
        return out
    names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q"]
    expect("  printed example", lay_out_and_shuffle(names[:8]), ["A", "5", "2", "6", "3", "7", "4", "8"])
    got = {}
    for N in (4, 6, 8, 10, 12):
        start = names[:N]
        cur, k = lay_out_and_shuffle(start), 1
        while cur != start:
            cur, k = lay_out_and_shuffle(cur), k + 1
        got[N] = k
    expect("  shuffles to come back", got, {4: 2, 6: 4, 8: 3, 10: 6, 12: 10})
    m = mats_of("u-p5")[0]
    expect("  the card mat is blank, 8 slots", (m.n, m.perm), (8, None))
    _, _, _, labs = parse_fig("u-p5")
    expect("  labels above the 8 slots", [s for _, _, s in sorted(labs)], ["A", "2", "3", "4", "5", "6", "7", "8"])
    after = lay_out_and_shuffle(names[:8])
    machine = [after.index(c) for c in names[:8]]
    expect("  8-card shuffle as a machine", one(machine), [1, 3, 5, 7, 2, 4, 6, 8])
    expect("  its loops", loops(machine), [(1,), (2, 3, 5), (4, 7, 6), (8,)])
    for N in (4, 6, 10, 12):
        after = lay_out_and_shuffle(names[:N])
        mm = [after.index(c) for c in names[:N]]
        print(f"   {N} cards: machine {one(mm)} loops {loops(mm)}")

    print("Problem 6")
    ms = [m for _, m in machines_in(byprob[6])]
    expect("  labels", [m.label for m in ms], ["A", "B", "A then B", "B then A"] * 3)
    want = [([2, 1, 3, 4], [1, 3, 2, 4], [3, 1, 2, 4], [2, 3, 1, 4]),
            ([2, 1, 3, 4], [1, 2, 4, 3], [2, 1, 4, 3], [2, 1, 4, 3]),
            ([2, 3, 1, 4], [1, 3, 4, 2], [3, 4, 1, 2], [2, 1, 4, 3])]
    for k, w in enumerate(want):
        A, B = ms[4 * k].perm, ms[4 * k + 1].perm
        expect(f"  pair {k + 1}: A, B", (one(A), one(B)), (w[0], w[1]))
        expect(f"  pair {k + 1}: A then B", one(then(A, B)), w[2])
        expect(f"  pair {k + 1}: B then A", one(then(B, A)), w[3])
        # physical check with blocks: run A, move the row, run B
        row = list("gbry")
        expect(f"  pair {k + 1}: blocks agree with A then B", turn(turn(row, A), B), turn(row, then(A, B)))
        expect(f"  pair {k + 1}: blank mats", (ms[4 * k + 2].perm, ms[4 * k + 3].perm), (None, None))

    print("Problem 7")
    ms = [m for _, m in machines_in(byprob[7])]
    expect("  labels", [m.label for m in ms],
           ["A", "B", "A then B", "undoes A", "undoes B", "undoes (A then B)"] * 2)
    want = [([2, 3, 1, 4], [1, 4, 2, 3], [4, 2, 1, 3], [3, 1, 2, 4], [1, 3, 4, 2], [3, 2, 4, 1], [4, 1, 3, 2]),
            ([2, 1, 3, 4], [1, 3, 4, 2], [3, 1, 4, 2], [2, 1, 3, 4], [1, 4, 2, 3], [2, 4, 1, 3], [4, 1, 2, 3])]
    for k, w in enumerate(want):
        A, B = ms[6 * k].perm, ms[6 * k + 1].perm
        expect(f"  pair {k + 1}: A, B", (one(A), one(B)), (w[0], w[1]))
        AB = then(A, B)
        expect(f"  pair {k + 1}: A then B", one(AB), w[2])
        expect(f"  pair {k + 1}: undoes A", one(undo(A)), w[3])
        expect(f"  pair {k + 1}: undoes B", one(undo(B)), w[4])
        expect(f"  pair {k + 1}: undoes (A then B)", one(undo(AB)), w[5])
        expect(f"  pair {k + 1}: = undo B then undo A", one(then(undo(B), undo(A))), w[5])
        expect(f"  pair {k + 1}: undo A then undo B (the wrong order)", one(then(undo(A), undo(B))), w[6])
        expect(f"  pair {k + 1}: wrong order fails", then(AB, then(undo(A), undo(B))) == list(range(4)), False)
        expect(f"  pair {k + 1}: loops of A then B", loop_lengths(AB), [1, 3] if k == 0 else [4])
        uniq = [q for q in permutations(range(4)) if then(AB, list(q)) == list(range(4))]
        expect(f"  pair {k + 1}: only one machine undoes A then B", len(uniq), 1)
    expect("  rule holds for all 4-slot pairs", all(
        undo(then(list(a), list(b))) == then(undo(list(b)), undo(list(a)))
        for a in permutations(range(4)) for b in permutations(range(4))), True)

    print("Problem 8")
    der = [list(q) for q in permutations(range(4)) if all(q[i] != i for i in range(4))]
    pairs = [(a, b) for i, a in enumerate(der) for b in der[i + 1:] if then(a, b) == then(b, a)]
    expect("  machines moving all four blocks", len(der), 9)
    expect("  unordered commuting pairs", len(pairs), 12)
    kinds = Counter((tuple(loop_lengths(a)), tuple(loop_lengths(b))) if loop_lengths(a) >= loop_lengths(b)
                    else (tuple(loop_lengths(b)), tuple(loop_lengths(a))) for a, b in pairs)
    expect("  pair kinds", dict(kinds), {((2, 2), (2, 2)): 3, ((4,), (4,)): 3, ((4,), (2, 2)): 6})
    for a, b in (([2, 3, 4, 1], [4, 1, 2, 3]), ([2, 1, 4, 3], [3, 4, 1, 2]), ([2, 3, 4, 1], [3, 4, 1, 2])):
        A, B = [x - 1 for x in a], [x - 1 for x in b]
        expect(f"  example {a} and {b} agree", then(A, B) == then(B, A), True)
        if then(A, B) == then(B, A) and A in der and B in der:
            SEEN_MACHINES.update({tuple(a), tuple(b)})

    print("Problem 9")
    g = [max(reduce(lcm, pt, 1) for pt in partitions(n)) for n in range(1, 11)]
    expect("  most turns for 1..10 slots (loop splits)", g, [1, 2, 3, 4, 6, 6, 12, 15, 20, 30])
    brute = [max(order(list(q)) for q in permutations(range(n))) for n in range(1, 9)]
    expect("  same for 1..8 slots by running every machine", brute, g[:8])
    best = {n: sorted(tuple(pt) for pt in partitions(n) if reduce(lcm, pt, 1) == g[n - 1]) for n in range(1, 11)}
    print("  record loop splits:", best)
    expect("  record splits for 8, 9, 10", (best[8], best[9], best[10]), ([(5, 3)], [(5, 4)], [(5, 3, 2)]))
    expect("  slot counts where one more slot is not slower", [n + 1 for n in range(1, 10) if g[n] == g[n - 1]], [6])

    print("Problem 10")
    deck = list(range(52))
    cur, k = lay_out_and_shuffle(deck), 1
    while cur != deck:
        cur, k = lay_out_and_shuffle(cur), k + 1
    expect("  shuffles for 52 cards", k, 8)
    after = lay_out_and_shuffle(deck)
    mach = [after.index(c) for c in deck]
    expect("  loop lengths of the 52-card shuffle", Counter(loop_lengths(mach)), Counter({8: 6, 1: 2, 2: 1}))
    expect("  position rule (1-indexed): top half k -> 2k-1, bottom half k -> 2k-52",
           all(mach[k - 1] + 1 == (2 * k - 1 if k <= 26 else 2 * k - 52) for k in range(1, 53)), True)
    expect("  path of the card in position 2", [p for p in loops(mach) if 2 in p][0], (2, 3, 5, 9, 17, 33, 14, 27))
    expect("  2-loop", [p for p in loops(mach) if len(p) == 2], [(18, 35)])
    expect("  powers of 2 mod 51", [pow(2, e, 51) for e in range(1, 9)], [2, 4, 8, 16, 32, 13, 26, 1])


def check_launch():
    print("\n=== Launch (floor map, five chairs) ===")
    floor = [1, 0, 4, 2, 3]   # chair 1 -> 2, 2 -> 1, 3 -> 5, 4 -> 3, 5 -> 4
    expect("  floor map", one(floor), [2, 1, 5, 3, 4])
    expect("  loops", loops(floor), [(1, 2), (3, 5, 4)])
    expect("  switches until everyone is back", order(floor), 6)
    expect("  each child's first time back", home_times(floor, list("gbryp")), [2, 2, 3, 3, 3])
    printed = [[3, 1, 2], [1, 3, 2], [3, 4, 2, 1], [3, 4, 1, 2], [2, 4, 3, 1], [3, 4, 1, 5, 2], [4, 3, 1, 2],
               [4, 2, 1, 3], [3, 5, 4, 1, 2], [2, 5, 1, 4, 3], [2, 4, 1, 3], [5, 1, 4, 3, 2],
               [3, 2, 5, 1, 4], [5, 4, 1, 2, 3]]
    expect("  differs from every printed machine", one(floor) in printed, False)


LETTER = {"green": "g", "blue": "b", "red": "r", "yellow": "y", "purple": "p", "pink": "k"}


def crow(row):
    return "\\crow{" + ",".join(LETTER[c] for c in row) + "}"


def write_generated():
    """Coloured rows printed in the guide, computed here from the drawn machines."""
    defs = []

    def seq(macro, m):
        rows = run_until_home(m.perm, m.pictures)[1:]
        body = "".join(f"\\tn{{{k}}}{crow(r)}" for k, r in enumerate(rows, 1))
        defs.append(f"\\newcommand{{\\{macro}}}{{{body}}}")

    def one_row(macro, row):
        defs.append(f"\\newcommand{{\\{macro}}}{{{crow(row)}}}")

    k, _ = figs("k-1")
    for prob, names in ((1, ("KoneA", "KoneB")), (2, ("KtwoA", "KtwoB")), (3, ("KthreeA", "KthreeB"))):
        for macro, (_, m) in zip(names, machines_in(k[prob])):
            seq(macro, m)
    (_, a), _ = machines_in(k[6])
    one_row("KsixRow", turn(a.pictures, a.perm))
    m, _ = figs("grades-2-3")
    arrowed = [x for _, x in machines_in(m[4]) if x.perm]
    one_row("MfourRowA", turn(arrowed[0].pictures, arrowed[0].perm))
    one_row("MfourRowB", turn(arrowed[1].pictures, arrowed[1].perm))
    for f, tag in (("m-p6a", "One"), ("m-p6b", "Two")):
        ms = mats_of(f)
        A = [x for x in ms if x.perm and x.label == "A"][0]
        B = [x for x in ms if x.perm and x.label == "B"][0]
        one_row(f"Msix{tag}AB", turn(turn(A.pictures, A.perm), B.perm))
        one_row(f"Msix{tag}BA", turn(turn(B.pictures, B.perm), A.perm))
    floor = [1, 0, 4, 2, 3]   # the launch floor map, as in check_launch()
    rows = run_until_home(floor, ["green", "blue", "red", "yellow", "purple"])[1:]
    defs.append("\\newcommand{\\LaunchRows}{" + "".join(f"\\tn{{{k}}}{crow(r)}" for k, r in enumerate(rows, 1)) + "}")
    with open(os.path.join(HERE, "generated.tex"), "w") as fh:
        fh.write("% written by check_answers.py from the drawn machines in ../src/fig; do not edit\n")
        fh.write("\n".join(defs) + "\n")
    print("\nwrote generated.tex:", len(defs), "macros")


def check_extras():
    print("\n=== Mathematics section ===")
    def out_order(N):
        deck = list(range(N))
        h = N // 2
        cur, k = deck, 0
        while True:
            cur = [x for pair in zip(cur[:h], cur[h:]) for x in pair]
            k += 1
            if cur == deck:
                return k
    def in_order(N):
        deck = list(range(N))
        h = N // 2
        cur, k = deck, 0
        while True:
            cur = [x for pair in zip(cur[h:], cur[:h]) for x in pair]
            k += 1
            if cur == deck:
                return k
    def mult_order(a, m):
        k, x = 1, a % m
        while x != 1:
            x, k = x * a % m, k + 1
        return k
    expect("  out-shuffle order = order of 2 mod N-1 (N = 4..52 even)",
           all(out_order(N) == mult_order(2, N - 1) for N in range(4, 54, 2)), True)
    expect("  in-shuffle of 52 cards", in_order(52), 52)
    expect("  number of 3-slot machines", math.factorial(3), 6)
    expect("  turns possible with 7 slots", orders_for(7), [1, 2, 3, 4, 5, 6, 7, 10, 12])
    shuffled = ["A", "5", "2", "6", "3", "7", "4", "8"]
    pile = []
    for c in shuffled:          # dealt one at a time onto a pile: the last card dealt ends on top
        pile.insert(0, c)
    expect("  8 cards interleaved onto a pile instead of a row (top first)", pile, ["8", "4", "7", "3", "6", "2", "5", "A"])
    expect("  5-slot machines that undo themselves (involutions)", sum(
        1 for q in permutations(range(5)) if then(list(q), list(q)) == list(range(5))), 26)
    # Elmsley: to send the top card to position k (0 = top), do in-shuffles for the 1s of k in binary
    def shuffle(cur, kind):
        h = len(cur) // 2
        a, b = (cur[:h], cur[h:]) if kind == "out" else (cur[h:], cur[:h])
        return [x for pair in zip(a, b) for x in pair]
    ok = True
    for k in range(52):
        cur = list(range(52))
        for bit in bin(k)[2:] if k else "":
            cur = shuffle(cur, "in" if bit == "1" else "out")
        ok &= cur.index(0) == k
    expect("  Elmsley: binary of k as in/out shuffles moves the top card to position k", ok, True)


def check_guide_text():
    """Every machine and loop typed in facilitator.tex must be one this script computed and confirmed."""
    print("\n=== Machines and loops typed in facilitator.tex ===")
    tex = open(os.path.join(HERE, "facilitator.tex")).read()
    typed = [tuple(int(v) for v in m.split(",")) for m in re.findall(r"\\arrs\{([\d,]+)\}", tex)]
    typed += [tuple(int(v) for v in m.split(",")) for m in re.findall(r"\\minimat(?:\[[a-z,]*\])?\{([\d,]+)\}", tex)]
    typed += [tuple(int(v) for v in m.split(",")) for m in re.findall(r"\\mmc(?:\[[a-z,]*\])?\{([\d,]+)\}", tex)]
    bad = [t for t in typed if t not in SEEN_MACHINES]
    expect(f"  {len(typed)} typed machines all confirmed", bad, [])
    loops_typed = re.findall(r"\((\d(?:\\,\d)*)\)", tex)
    lt = [tuple(int(v) for v in g.split("\\,")) for g in loops_typed]
    lt = [t for t in lt if len(t) > 1]   # single numbers in brackets are mostly hint labels
    bad = [t for t in lt if t not in SEEN_LOOPS]
    expect(f"  {len(lt)} typed loops all confirmed", bad, [])


if __name__ == "__main__":
    check_launch()
    check_k1()
    check_m23()
    check_u45()
    check_extras()
    check_guide_text()
    write_generated()
    print()
    if FAILURES:
        print(f"{len(FAILURES)} FAILED:", FAILURES)
        sys.exit(1)
    print("all answers in the guide agree with the student pages")
