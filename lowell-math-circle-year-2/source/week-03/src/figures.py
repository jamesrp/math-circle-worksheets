"""Generate every diagram for the three Week 3 packets and check the intended answers.

Run:  python3 figures.py      (clears fig/ and writes fig/*.tex)
"""
import glob
import os
from functools import reduce
from itertools import permutations

from machines import (BLOCK_ORDER, FULL, FULL6, SMALL, Size, block_home_times, box, cycle_type, is_perm, lcm,
                      mat_tikz, mat_width, order, order_by_simulation, then, tikzpicture, undo)

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "fig")
os.makedirs(FIG, exist_ok=True)
TEXTWIDTH = 7.5

KSMALL = Size(slot=0.66, gap=0.07, rowgap=0.7, stub=0.08, arrow_lw=1.4, slot_lw=0.9, tip=0.11, dot=0.03)
GRID5 = Size(slot=0.48, gap=0.07, rowgap=0.62, stub=0.06, arrow_lw=1.1, slot_lw=0.8, tip=0.09, dot=0.025)
GRID6 = Size(slot=0.40, gap=0.05, rowgap=0.6, stub=0.06, arrow_lw=1.0, slot_lw=0.7, tip=0.085, dot=0.022)
TINY = Size(slot=0.38, gap=0.05, rowgap=0.85, stub=0.06, arrow_lw=1.0, slot_lw=0.7, tip=0.085, dot=0.022)
TINY4 = Size(slot=0.40, gap=0.06, rowgap=0.62, stub=0.06, arrow_lw=1.0, slot_lw=0.7, tip=0.085, dot=0.022)
G3 = Size(slot=0.38, gap=0.05, rowgap=0.6, stub=0.05, arrow_lw=1.0, slot_lw=0.7, tip=0.08, dot=0.02)
QUAD = Size(slot=0.38, gap=0.04, rowgap=0.8, stub=0.05, arrow_lw=1.0, slot_lw=0.7, tip=0.085, dot=0.022)
UNDO = Size(slot=0.42, gap=0.06, rowgap=0.6, stub=0.06, arrow_lw=1.1, slot_lw=0.8, tip=0.09, dot=0.025)
CARD = Size(slot=0.55, gap=0.08, rowgap=0.85, stub=0.07, arrow_lw=1.2, slot_lw=0.8, tip=0.1, dot=0.028)
CENTRED = [0.0]   # K-1 mats: every arrowhead points at the middle of its bottom slot


def P(*one_indexed_targets):
    """Machine from 1-indexed targets: P(3,1,2) means 1->3, 2->1, 3->2."""
    p = [t - 1 for t in one_indexed_targets]
    assert is_perm(p), p
    return p


def write(name, lines):
    with open(os.path.join(FIG, name + ".tex"), "w") as f:
        f.write(tikzpicture(lines))


def check(p, turns=None, ctype=None):
    assert order(p) == order_by_simulation(p)
    if turns is not None:
        assert order(p) == turns, (p, order(p), turns)
    if ctype is not None:
        assert cycle_type(p) == sorted(ctype), (p, cycle_type(p), ctype)


# ----------------------------------------------------------------------------------------------
# full-size mats with a recording area


def full_size(n, rowgap=None):
    if n >= 6:
        base = FULL6
    elif n == 3:
        base = Size(**{**FULL.__dict__, "rowgap": 0.95})
    elif n == 4:
        base = Size(**{**FULL.__dict__, "rowgap": 1.0})
    else:
        base = FULL
    if rowgap is not None:
        base = Size(**{**base.__dict__, "rowgap": rowgap})
    return base


def full_mat(name, n, p, side="tally", side_label=None, perblock=False, below=None, sz=None, seed=1,
             end_steps=None, tally_h=0.8):
    sz = sz or full_size(n)
    lines, w, h = mat_tikz(n, p, sz, icons=BLOCK_ORDER[:n], perblock=perblock, seed=seed, end_steps=end_steps)
    slots_h = 2 * sz.slot + sz.rowgap
    if side == "tally":
        bw = min(2.7, TEXTWIDTH - w - 0.3)
        bh = slots_h - 0.3
        assert bw >= 1.5, (name, bw)
        lines += box(w + 0.25, 0.15, bw, bh, label=side_label, label_pos="inside")
    elif side == "tallybelow":
        # a tally box under the mat, as wide as the mat
        lines += box(0, -0.18 - tally_h, w, tally_h, label=side_label, label_pos="inside")
    elif side == "num":
        bw, bh = 0.8, 0.62
        lines += box(w + 0.2, slots_h / 2 - bh / 2, bw, bh, label=side_label, label_pos="above")
    elif side == "num2":
        bw, bh = 0.8, 0.62
        a, b = side_label
        lines += box(w + 0.2, slots_h / 2 + 0.3, bw, bh, label=a, label_pos="above")
        lines += box(w + 0.2, slots_h / 2 - 0.3 - bh - 0.15, bw, bh, label=b, label_pos="above")
    if below:
        # list of labels; boxes in a row under the mat, right-aligned
        bw, bh = 0.8, 0.5
        x = w
        for lab in reversed(below):
            x -= bw
            lines += box(x, -0.12 - bh, bw, bh, label=lab, label_pos="left")
            x -= 0.25 + 0.11 * len(lab)
    write(name, lines)


def order_pair(name, A, B, seed=1):
    """Grades 2-3: full-size machine A above full-size machine B (4 slots, with pictures), a big letter
    beside each, and two small rows on the right for drawing where the blocks end up in each order."""
    n = len(A)
    sz = Size(**{**FULL.__dict__, "gap": 0.1, "rowgap": 0.85})
    xm = 0.42
    lines = []
    lb, wb, hb = mat_tikz(n, B, sz, x0=xm, y0=0.0, icons=BLOCK_ORDER[:n], seed=seed)
    ya = hb + 0.4
    la, wa, ha = mat_tikz(n, A, sz, x0=xm, y0=ya, icons=BLOCK_ORDER[:n], seed=seed + 1)
    lines += la + lb
    slots_h = 2 * sz.slot + sz.rowgap
    for letter, y0 in (("A", ya), ("B", 0.0)):
        lines.append(f"\\node[font=\\LARGE\\bfseries] at (0.14,{y0 + slots_h / 2:.3f}) {{{letter}}};")
    # record rows
    rs, rg = 0.4, 0.04
    rx = xm + wa + 0.24
    rw = n * rs + (n - 1) * rg
    assert rx + rw <= TEXTWIDTH + 1e-9, rx + rw
    ymid = (ya + ha) / 2
    for k, lab in enumerate(("A then B", "B then A")):
        ry = ymid + 0.35 - k * 1.05
        lines.append(f"\\node[font=\\labelfont, anchor=south west, inner xsep=0pt] at ({rx:.3f},{ry + rs + 0.03:.3f}) {{{lab}}};")
        for i in range(n):
            x = rx + i * (rs + rg)
            lines.append(f"\\draw[line width=0.9pt, fill=slotfill] ({x:.3f},{ry:.3f}) rectangle ({x + rs:.3f},{ry + rs:.3f});")
    write(name, lines)


def grid(name, specs, sz, cols, colw, rowh, numbox=None, frame=True, pad=0.12, extra_after=None):
    """specs: list of (n, p_or_None, label).  numbox: None or (w, h, label, where) with where 'right'/'below'.

    A 'below' box sits inside its mat's frame, so it cannot be read as belonging to the next row.
    extra_after: {row index: extra vertical space after that row}.
    """
    lines = []
    extra_after = extra_after or {}
    rows = (len(specs) + cols - 1) // cols
    # y of each row's mat bottom, counting from the last row up
    ys = {}
    y = 0.0
    for r in range(rows - 1, -1, -1):
        ys[r] = y
        y += rowh + extra_after.get(r - 1, 0.0)
    for k, (n, p, label) in enumerate(specs):
        r, c = divmod(k, cols)
        w = mat_width(n, sz)
        extra = numbox[0] + pad + 0.15 if (numbox and numbox[3] == "right") else 0
        x0 = c * colw + (colw - w - extra) / 2
        y0 = ys[r]
        ml, _, mh = mat_tikz(n, p, sz, x0=x0, y0=y0, seed=k + 1)
        fbot = y0 - pad
        if numbox and numbox[3] == "below":
            bw, bh, blab, _ = numbox
            by = y0 - pad - bh
            fbot = by - 0.1
        if frame:
            lines.append(f"\\draw[framecol, line width=0.8pt, rounded corners=5pt] ({x0 - pad:.3f},{fbot:.3f}) rectangle ({x0 + w + pad:.3f},{y0 + mh + pad:.3f});")
        lines += ml
        if label:
            lines.append(f"\\node[font=\\labelfont, anchor=base west, inner xsep=0pt] at ({x0 - pad:.3f},{y0 + mh + pad + 0.07:.3f}) {{{label}}};")
        if numbox:
            bw, bh, blab, where = numbox
            if where == "right":
                lines += box(x0 + w + pad + 0.15, y0 + mh / 2 - bh / 2, bw, bh, label=blab, label_pos="above")
            else:
                lines += box(x0 + w - bw, y0 - pad - bh, bw, bh, label=blab, label_pos="left")
    write(name, lines)


# ==============================================================================================
# K-1
# ==============================================================================================

def k1():
    C = CENTRED
    a = P(3, 1, 2)          # loop of 3
    b = P(1, 3, 2)          # 1 fixed, 2<->3
    check(a, 3)
    check(b, 2)
    full_mat("k-p1a", 3, a, end_steps=C)
    full_mat("k-p1b", 3, b, end_steps=C)

    # Problem 2: one loop of 4, two swaps
    c = P(3, 4, 2, 1)       # 1->3->2->4->1
    d = P(3, 4, 1, 2)       # 1<->3, 2<->4
    check(c, 4, [4])
    check(d, 2, [2, 2])
    full_mat("k-p2a", 4, c, end_steps=C)
    full_mat("k-p2b", 4, d, end_steps=C)

    # Problem 3: fewer turns than blocks (a block that stays), more turns than blocks
    e = P(2, 4, 3, 1)       # 1->2->4->1, 3 fixed
    f = P(3, 4, 1, 5, 2)    # 1<->3, 2->4->5->2
    check(e, 3, [1, 3])
    check(f, 6, [2, 3])
    full_mat("k-p3a", 4, e, end_steps=C, sz=full_size(4, 0.9))
    full_mat("k-p3b", 5, f, side="tallybelow", end_steps=C, sz=full_size(5, 0.9), tally_h=0.75)

    # Problem 4: build to a target
    for t in (2, 3, 4):
        full_mat(f"k-p4-{t}", 4, None, side_label=f"{t} turns")
    orders4 = {order(list(q)) for q in permutations(range(4))}
    assert {2, 3, 4} <= orders4

    # Problem 5: no machine moves exactly one block to a different slot
    full_mat("k-p5a", 4, None, side=None)
    full_mat("k-p5b", 4, None, side=None)
    for n in range(1, 7):
        for q in permutations(range(n)):
            assert sum(1 for i in range(n) if q[i] != i) != 1

    # Problem 6: undo.  Start under the pictures, one turn of g, move the row over in that order.
    g = P(4, 3, 1, 2)       # 1->4->2->3->1
    check(g, 4, [4])
    full_mat("k-p6a", 4, g, side=None, end_steps=C)
    full_mat("k-p6b", 4, None, side=None)
    ug = undo(g)
    assert then(g, ug) == list(range(4))
    assert ug == P(3, 4, 2, 1)
    # the answer is unique
    assert [q for q in permutations(range(4)) if then(g, list(q)) == list(range(4))] == [tuple(ug)]

    # Problem 7: all 3-slot machines -- 6 of them, nine blanks on the page
    assert len(list(permutations(range(3)))) == 6
    grid("k-p7", [(3, None, None)] * 9, KSMALL, cols=3, colw=2.5, rowh=2.5)

    # Problem 8: other 5-slot machines with 6 turns (loops of 2 and 3); one mat per partner
    full_mat("k-p8a", 5, None, side="tallybelow")
    full_mat("k-p8b", 5, None, side="tallybelow")
    six = [q for q in permutations(range(5)) if order(list(q)) == 6]
    assert len(six) == 20 and all(cycle_type(list(q)) == [2, 3] for q in six)
    assert tuple(f) in six


# ==============================================================================================
# Grades 2-3
# ==============================================================================================

def m23():
    # Problem 1: each block's own number and the whole row's number
    a = P(4, 2, 1, 3)        # 2 fixed, 1->4->3->1
    c = P(3, 5, 4, 1, 2)     # 2<->5, 1->3->4->1
    check(a, 3, [1, 3])
    check(c, 6, [2, 3])
    assert block_home_times(a) == [3, 1, 3, 3]
    assert block_home_times(c) == [3, 2, 3, 3, 2]
    full_mat("m-p1a", 4, a, side="num", side_label="all blocks", perblock=True)
    full_mat("m-p1b", 5, c, side="num", side_label="all blocks", perblock=True)

    # Problem 2: loops, predict, check (four machines on two pages)
    f = P(2, 5, 1, 4, 3)     # 4 fixed, 1->2->5->3->1
    d = P(4, 3, 6, 1, 2, 5)  # 1<->4, 2->3->6->5->2: loops 2 and 4 give 4, not 8
    g = P(4, 1, 6, 2, 3, 5)  # 1->4->2->1, 3->6->5->3: loops 3 and 3 give 3
    e = P(5, 6, 3, 1, 4, 2)  # 3 fixed, 2<->6, 1->5->4->1
    check(f, 4, [1, 4])
    check(d, 4, [2, 4])
    check(g, 3, [3, 3])
    check(e, 6, [1, 2, 3])
    full_mat("m-p2a", 5, f, side="num2", side_label=("predict", "check"), sz=full_size(5, 1.0))
    full_mat("m-p2b", 6, d, side=None, below=["predict", "check"])
    full_mat("m-p2c", 6, g, side=None, below=["predict", "check"])
    full_mat("m-p2d", 6, e, side=None, below=["predict", "check"])

    # Problem 3: every number of turns from 1 to 6 is possible with 5 slots
    assert {order(list(q)) for q in permutations(range(5))} == {1, 2, 3, 4, 5, 6}
    grid("m-p3", [(5, None, f"{t} turn{'s' if t > 1 else ''}") for t in range(1, 7)], GRID5,
         cols=2, colw=3.75, rowh=2.35)

    # Problem 4: machines that undo a given machine
    i = P(2, 4, 1, 3)        # 1->2->4->3->1
    j = P(5, 1, 4, 3, 2)     # 3<->4, 1->5->2->1
    check(i, 4, [4])
    check(j, 6, [2, 3])
    full_mat("m-p4a", 4, i, side=None)
    full_mat("m-p4a-blank", 4, None, side=None)
    full_mat("m-p4b", 5, j, side=None)
    full_mat("m-p4b-blank", 5, None, side=None)
    for q in (i, j):
        assert then(q, undo(q)) == list(range(len(q)))
        assert order(undo(q)) == order(q)
    assert undo(i) == P(3, 1, 4, 2) and undo(j) == P(2, 5, 4, 3, 1)

    # Problem 5: machines that undo themselves = all loops of length 1 or 2
    for q in permutations(range(5)):
        q = list(q)
        assert (then(q, q) == list(range(5))) == all(L <= 2 for L in cycle_type(q))
    assert sum(1 for q in permutations(range(5)) if then(list(q), list(q)) == list(range(5))) == 26
    grid("m-p5", [(5, None, None)] * 4, GRID5, cols=2, colw=3.75, rowh=2.1)

    # Problem 6: the two orders, run with blocks.  Pair 1 shares a slot and differs;
    # pair 2 has crossing arrows but moves separate blocks, and agrees.
    pairs = [
        (P(2, 1, 3, 4), P(1, 3, 2, 4)),   # swap 1,2 and swap 2,3
        (P(3, 2, 1, 4), P(1, 4, 3, 2)),   # swap 1,3 and swap 2,4
    ]
    (A1, B1), (A2, B2) = pairs
    assert then(A1, B1) != then(B1, A1)
    assert then(A2, B2) == then(B2, A2)
    # rows the children should draw (block in each slot, slots 1..4) for pair 1
    def row_after(m):
        row = [None] * len(m)
        for slot, blk in enumerate(range(len(m))):
            row[m[slot]] = blk
        return row
    assert row_after(then(A1, B1)) == [1, 2, 0, 3]   # rhombus, trapezoid, triangle, hexagon
    assert row_after(then(B1, A1)) == [2, 0, 1, 3]   # trapezoid, triangle, rhombus, hexagon
    order_pair("m-p6a", A1, B1, seed=3)
    order_pair("m-p6b", A2, B2, seed=5)

    # Problem 7: 6 slots give only 1..6, the same numbers as 5 slots; eight mats so the count is not given
    assert {order(list(q)) for q in permutations(range(6))} == {1, 2, 3, 4, 5, 6}
    grid("m-p7", [(6, None, None)] * 8, GRID6, cols=2, colw=3.75, rowh=1.95,
         numbox=(0.55, 0.45, "turns", "right"))

    # Problem 8: a 7-slot machine with more than 10 turns (only loops 3+4, 12 turns); 12 is the most
    big = {tuple(cycle_type(list(q))) for q in permutations(range(7)) if order(list(q)) > 10}
    assert big == {(3, 4)}
    assert max(order(list(q)) for q in permutations(range(7))) == 12
    grid("m-p8", [(7, None, None)] * 3, SMALL, cols=1, colw=7.4, rowh=2.15, numbox=(0.8, 0.6, "turns", "right"))


# ==============================================================================================
# Grades 4-5
# ==============================================================================================

def u45():
    a = P(3, 2, 5, 1, 4)    # 2 fixed, 1->3->5->4->1
    b = P(5, 4, 1, 2, 3)    # 2<->4, 1->5->3->1
    check(a, 4, [1, 4])
    check(b, 6, [2, 3])
    assert block_home_times(a) == [4, 1, 4, 4, 4]
    assert block_home_times(b) == [3, 2, 3, 2, 3]
    full_mat("u-p1a", 5, a, side="num", side_label="all blocks", perblock=True)
    full_mat("u-p1b", 5, b, side="num", side_label="all blocks", perblock=True)

    # Problem 2: none of these is a record holder for its number of slots except the 6-slot 1+2+3,
    # which ties with a single loop of 6.  (The records for 7 and 8 slots are 12 and 15.)
    p2 = [
        (P(3, 6, 5, 2, 1, 4), 3, [3, 3]),
        (P(5, 3, 6, 4, 1, 2), 6, [1, 2, 3]),
        (P(4, 5, 6, 7, 1, 3, 2), 10, [2, 5]),
        (P(4, 7, 5, 2, 6, 1, 3), 7, [7]),
        (P(3, 5, 2, 8, 7, 1, 6, 4), 6, [2, 6]),
        (P(3, 5, 6, 2, 7, 8, 4, 1), 4, [4, 4]),
    ]
    for q, t, ct in p2:
        check(q, t, ct)
    assert all(t not in (12, 15) for _, t, _ in p2)
    grid("u-p2", [(len(q), q, None) for q, _, _ in p2], TINY, cols=2, colw=3.75, rowh=2.8,
         numbox=(0.75, 0.5, "turns", "below"))

    # Problem 3: 5 slots give exactly 1..6
    assert {order(list(q)) for q in permutations(range(5))} == set(range(1, 7))
    grid("u-p3", [(5, None, None)] * 9, G3, cols=3, colw=2.5, rowh=2.45, numbox=(0.62, 0.42, "turns", "below"))

    # Problem 4: slowest 6-slot and 7-slot machines
    best6 = max(order(list(q)) for q in permutations(range(6)))
    best7 = max(order(list(q)) for q in permutations(range(7)))
    assert (best6, best7) == (6, 12)
    specs = [(6, None, "6 slots"), (7, None, "7 slots"), (6, None, None), (7, None, None)]
    grid("u-p4", specs, TINY4, cols=2, colw=3.75, rowh=2.6, numbox=(0.62, 0.42, "turns", "below"))

    # Problem 5: perfect shuffles, done with the cards laid out in a row
    def out_shuffle(N):
        h = N // 2
        return [2 * i for i in range(h)] + [2 * i + 1 for i in range(h)]
    expect = {4: 2, 6: 4, 8: 3, 10: 6, 12: 10, 52: 8}
    for N, t in expect.items():
        check(out_shuffle(N), t)
    deck = ["A", "2", "3", "4", "5", "6", "7", "8"]
    after = [None] * 8
    for i, j in enumerate(out_shuffle(8)):
        after[j] = deck[i]
    assert after == ["A", "5", "2", "6", "3", "7", "4", "8"]
    lines, w, h = mat_tikz(8, None, CARD, labels=deck)
    write("u-p5", lines)

    # Problem 6: A then B and B then A
    pairs = [
        (P(2, 1, 3, 4), P(1, 3, 2, 4)),   # two swaps sharing slot 2
        (P(2, 1, 3, 4), P(1, 2, 4, 3)),   # two swaps on separate slots
        (P(2, 3, 1, 4), P(1, 3, 4, 2)),   # two loops of 3
    ]
    results = []
    for A, B in pairs:
        AB, BA = then(A, B), then(B, A)
        results.append((AB == BA, cycle_type(AB), cycle_type(BA)))
    assert results[0][0] is False and results[1][0] is True and results[2][0] is False
    assert cycle_type(then(*pairs[2])) == [2, 2] and cycle_type(then(pairs[2][1], pairs[2][0])) == [2, 2]
    specs = []
    for A, B in pairs:
        specs += [(4, A, "A"), (4, B, "B"), (4, None, "A then B"), (4, None, "B then A")]
    grid("u-p6", specs, QUAD, cols=4, colw=1.875, rowh=2.3, pad=0.08)

    # Problem 7: undoing A then B, two pairs.  Pair 1: two loops of 3; pair 2: a swap and a loop of 3
    # sharing slot 2.  In both, undo(A then B) = undo B then undo A, and the other order fails.
    undo_pairs = [
        (P(2, 3, 1, 4), P(1, 4, 2, 3)),
        (P(2, 1, 3, 4), P(1, 3, 4, 2)),
    ]
    specs = []
    for A, B in undo_pairs:
        AB = then(A, B)
        assert undo(AB) == then(undo(B), undo(A))
        assert undo(AB) != then(undo(A), undo(B))
        specs += [(4, A, "A"), (4, B, "B"), (4, None, "A then B"),
                  (4, None, "undoes A"), (4, None, "undoes B"), (4, None, "undoes (A then B)")]
    assert cycle_type(then(*undo_pairs[0])) == [1, 3]
    grid("u-p7", specs, UNDO, cols=3, colw=2.5, rowh=1.98, extra_after={1: 0.32})

    # Problem 8: commuting 4-slot machines, each moving all four blocks
    found = [(x, y) for x in permutations(range(4)) for y in permutations(range(4))
             if x != y and all(x[i] != i for i in range(4)) and all(y[i] != i for i in range(4))
             and then(list(x), list(y)) == then(list(y), list(x))]
    assert found
    grid("u-p8", [(4, None, "A"), (4, None, "B")], GRID5, cols=2, colw=3.75, rowh=1.8)

    # Problem 9: largest number of turns for 1..10 slots (Landau)
    def parts(n, m=None):
        m = n if m is None else m
        if n == 0:
            yield []
            return
        for k in range(min(n, m), 0, -1):
            for r in parts(n - k, k):
                yield [k] + r
    g = [max(reduce(lcm, pt, 1) for pt in parts(n)) for n in range(1, 11)]
    assert g == [1, 2, 3, 4, 6, 6, 12, 15, 20, 30]


if __name__ == "__main__":
    import sys
    which = sys.argv[1:] or ["k", "m", "u"]
    if which == ["k", "m", "u"]:
        for old in glob.glob(os.path.join(FIG, "*.tex")):
            os.remove(old)
    for key, fn in (("k", k1), ("m", m23), ("u", u45)):
        if key in which:
            fn()
    print("figures written, all checks passed")
