"""Recompute every answer printed in the Week 8 adult guide.

Reads the student pages as printed (the generated .tex in ../src: board sizes,
star squares, dots, move arrows, pile pictures, and the numbers in the text),
solves each game by brute force from the rules alone, and checks the answers
the guide prints (EXPECTED below).  It does not use the student sources'
comments, their check.py, or the reviews.  It also writes the answer pictures
used in the guide (figs/*.tex) from the computed positions.

Coordinates: square (a, b) is a squares right of the star's column and b rows
above the star's row; the star is (0, 0).

Run:  python3 check.py      (exits non-zero if any check fails)
"""
import os
import re
import sys
from functools import lru_cache
from itertools import combinations, combinations_with_replacement

HERE = os.path.dirname(os.path.abspath(__file__))
STU = os.path.join(HERE, "..", "src")
FIGS = os.path.join(HERE, "figs")
FAILS = []
NCHECK = 0


def check(cond, msg):
    global NCHECK
    NCHECK += 1
    if not cond:
        FAILS.append(msg)
        print("FAIL:", msg)


# ------------------------------------------------------------------ games --
def rook_moves(p):
    a, b = p
    return [(x, b) for x in range(a)] + [(a, y) for y in range(b)]


def queen_moves(p):
    a, b = p
    return rook_moves(p) + [(a - k, b - k) for k in range(1, min(a, b) + 1)]


def nim_moves(p):
    out = []
    for i, h in enumerate(p):
        for k in range(h):
            q = list(p)
            q[i] = k
            out.append(tuple(q))
    return out


def solver(moves):
    @lru_cache(None)
    def second_wins(p):
        # The player to move loses (second player wins) exactly when every
        # move leads to a position from which the player to move wins.  With
        # no moves left (token on the star, all piles empty) this is true.
        return all(not second_wins(q) for q in moves(p))
    return second_wins


ROOK_P = solver(rook_moves)
QUEEN_P = solver(queen_moves)


@lru_cache(None)
def _nim_p_sorted(p):
    return all(not _nim_p_sorted(tuple(sorted(q))) for q in nim_moves(p))


def NIM_P(p):
    return _nim_p_sorted(tuple(sorted(p)))


def who(second_wins):
    return "second" if second_wins else "first"


def winning_moves(p, moves, is_p):
    return [q for q in moves(p) if is_p(q)]


def nim_winning_moves(p):
    """Return winning moves as (pile index, new size)."""
    out = []
    for i, h in enumerate(p):
        for k in range(h):
            q = list(p)
            q[i] = k
            if NIM_P(tuple(q)):
                out.append((i, k))
    return out


# --------------------------------------------------------------- parsing --
NUM = r"(-?\d+(?:\.\d+)?)"


def problems(texfile):
    tex = open(os.path.join(STU, texfile)).read()
    tex = tex.split(r"\begin{document}", 1)[1]
    parts = re.split(r"\\prob\{(\d+)\}", tex)
    chunks = {0: parts[0]}
    for i in range(1, len(parts), 2):
        chunks[int(parts[i])] = parts[i + 1]
    return chunks


def pictures(chunk):
    return re.findall(r"\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}", chunk, re.S)


def parse_board(pic):
    m = re.search(r"grid\[step=" + NUM + r"\] \(" + NUM + "," + NUM + r"\)", pic)
    if not m:
        return None
    s, w, h = float(m.group(1)), float(m.group(2)), float(m.group(3))
    n = round(w / s)
    assert abs(n * s - w) < 1e-3 and abs(w - h) < 1e-3
    sq = lambda x, y: (round(x / s - 0.5), round(y / s - 0.5))
    stars = [sq(float(x), float(y)) for x, y in
             re.findall(r"node\[star.*?\] at \(" + NUM + "," + NUM + r"\)", pic)]
    dots = [sq(float(x), float(y)) for x, y in
            re.findall(r"filldraw\[fill=black!35[^\]]*\] \(" + NUM + "," + NUM + r"\) circle", pic)]
    arrows = [sq(float(x), float(y)) for x, y in
              re.findall(r"Stealth[^\n]*?-- \(" + NUM + "," + NUM + r"\)", pic)]
    return {"n": n, "s": s, "stars": stars, "dots": dots, "arrow_ends": arrows}


def parse_piles(pic):
    cs = re.findall(r"fill=white\] \(" + NUM + "," + NUM + r"\) circle", pic)
    if not cs:
        return None
    xs = {}
    for x, _ in cs:
        xs.setdefault(round(float(x), 3), 0)
        xs[round(float(x), 3)] += 1
    return tuple(xs[k] for k in sorted(xs))


def boards_in(chunk):
    out = [parse_board(p) for p in pictures(chunk)]
    return [b for b in out if b]


def piles_in(chunk):
    out = [parse_piles(p) for p in pictures(chunk)]
    return [p for p in out if p]


def triples_in(text):
    return [tuple(int(v) for v in t) for t in re.findall(r"(\d+), (\d+), (\d+)", text)]


def pairs_in(text):
    return [(int(a), int(b)) for a, b in re.findall(r"(\d+) and (\d+)", text)]


def board_ok(b):
    """Star in the bottom-left square; every square inside the board."""
    check(b["stars"] == [(0, 0)], f"star not at bottom-left: {b}")
    for d in b["dots"] + b["arrow_ends"]:
        check(0 <= d[0] < b["n"] and 0 <= d[1] < b["n"], f"square off board: {d} in {b}")


# --------------------------------------------------------------- figures --
def fig_board(n, s, dot=None, shade=(), arrow=None, label=None, star=True, lw="0.4pt"):
    w = n * s
    o = [r"\begin{tikzpicture}[x=1in,y=1in,baseline=(current bounding box.south)]"]
    for (a, b) in shade:
        o.append(rf"\fill[ans] ({a*s:.4f},{b*s:.4f}) rectangle ({(a+1)*s:.4f},{(b+1)*s:.4f});")
    o.append(rf"\draw[line width={lw}, black!70] (0,0) grid[step={s}] ({w:.4f},{w:.4f});")
    o.append(rf"\draw[line width=0.8pt] (0,0) rectangle ({w:.4f},{w:.4f});")
    if star:
        o.append(rf"\node[star, star points=5, star point ratio=2.3, draw=black, line width=0.5pt,"
                 rf" inner sep=0pt, minimum size={0.7*s:.3f}in] at ({s/2:.4f},{s/2:.4f}) {{}};")
    if dot:
        o.append(rf"\filldraw[fill=black!35, line width=0.5pt] ({(dot[0]+.5)*s:.4f},{(dot[1]+.5)*s:.4f})"
                 rf" circle ({0.3*s:.4f});")
    if arrow:
        (p, q) = arrow
        o.append(rf"\draw[-{{Stealth[length=4pt,width=4pt]}}, line width=1.1pt, shorten <={0.3*s:.3f}in] "
                 rf"({(p[0]+.5)*s:.4f},{(p[1]+.5)*s:.4f}) -- ({(q[0]+.5)*s:.4f},{(q[1]+.5)*s:.4f});")
    if label:
        o.append(rf"\node[below, inner sep=1.5pt] at ({w/2:.4f},0) {{\scriptsize {label}}};")
    o.append(r"\end{tikzpicture}")
    return "\n".join(o)


def write_fig(name, body):
    os.makedirs(FIGS, exist_ok=True)
    with open(os.path.join(FIGS, name + ".tex"), "w") as f:
        f.write(body + "\n")


def rook_answer_figs(name, boards, s):
    """One small board per start: the dot, and for a first-player win the
    winning move as an arrow onto a shaded square; label 1st or 2nd."""
    for i, b in enumerate(boards, 1):
        d = b["dots"][0]
        if ROOK_P(d):
            write_fig(f"{name}-{i}", fig_board(b["n"], s, dot=d, label="2nd"))
        else:
            q = winning_moves(d, rook_moves, ROOK_P)[0]
            write_fig(f"{name}-{i}", fig_board(b["n"], s, dot=d, shade=[q], arrow=(d, q), label="1st"))


# ------------------------------------------------------------------- K-1 --
def k1():
    P = problems("k-1.tex")
    rules = boards_in(P[0])[0]
    board_ok(rules)
    d = rules["dots"][0]
    for e in rules["arrow_ends"]:
        check(e in rook_moves(d), f"K-1 rules arrow {d}->{e} is not a legal move")

    # Problem 1: two 3x3 boards
    b1 = boards_in(P[1])
    for b in b1:
        board_ok(b)
    check([(b["n"], b["dots"][0]) for b in b1] == [(3, (2, 2)), (3, (1, 2))], "K-1 P1 boards")
    check([who(ROOK_P(b["dots"][0])) for b in b1] == ["second", "first"], "K-1 P1 answers")
    check(winning_moves((1, 2), rook_moves, ROOK_P) == [(1, 1)], "K-1 P1 board 2 move")
    check(all(abs(b["s"] - 1.0) < 1e-9 for b in b1), "K-1 P1 squares are 1 inch")
    rook_answer_figs("k1-p1", b1, 0.17)

    # Problem 2: four 4x4 boards
    b2 = boards_in(P[2])
    for b in b2:
        board_ok(b)
    check([(b["n"], b["dots"][0]) for b in b2] == [(4, (3, 3)), (4, (3, 0)), (4, (2, 2)), (4, (1, 3))],
          "K-1 P2 boards")
    check([who(ROOK_P(b["dots"][0])) for b in b2] == ["second", "first", "second", "first"],
          "K-1 P2 answers")
    check(winning_moves((3, 0), rook_moves, ROOK_P) == [(0, 0)], "K-1 P2 (3,0) move")
    check(winning_moves((1, 3), rook_moves, ROOK_P) == [(1, 1)], "K-1 P2 (1,3) move")
    check(all(abs(b["s"] - 1.0) < 1e-9 for b in b2), "K-1 P2 squares are 1 inch")
    rook_answer_figs("k1-p2", b2, 0.13)

    # Problem 3: four 5x5 boards, the one winning move
    b3 = boards_in(P[3])
    expect = {(0, 3): (0, 0), (3, 1): (1, 1), (2, 4): (2, 2), (4, 3): (3, 3)}
    check([b["dots"][0] for b in b3] == list(expect), "K-1 P3 dots in page order")
    for i, b in enumerate(b3, 1):
        board_ok(b)
        d = b["dots"][0]
        wm = winning_moves(d, rook_moves, ROOK_P)
        check(wm == [expect[d]], f"K-1 P3 {d}: winning moves {wm}")
        write_fig(f"k1-p3-{i}", fig_board(5, 0.105, dot=d, shade=wm, arrow=(d, wm[0])))

    # Problem 4: 6x6, every square you want to move to
    b4 = boards_in(P[4])[0]
    board_ok(b4)
    want = sorted(q for q in [(a, b) for a in range(6) for b in range(6)] if ROOK_P(q))
    check(b4["n"] == 6 and want == [(k, k) for k in range(6)], "K-1 P4 diagonal")
    write_fig("k1-p4", fig_board(6, 0.15, shade=want))

    # Problem 5: two piles
    p5 = piles_in(P[5])
    check(p5 == [(3, 3), (4, 1), (2, 2), (5, 3)], f"K-1 P5 piles {p5}")
    check([who(NIM_P(p)) for p in p5] == ["second", "first", "second", "first"], "K-1 P5 answers")
    check(nim_winning_moves((4, 1)) == [(0, 1)], "K-1 P5 4,1 move: take 3 from the 4")
    check(nim_winning_moves((5, 3)) == [(0, 3)], "K-1 P5 5,3 move: take 2 from the 5")

    # Problem 6: 7 and 7
    p6 = piles_in(P[6])
    check(p6 == [(7, 7)] and NIM_P((7, 7)), "K-1 P6 7,7 second")

    # Problem 7: 8x8 from the far corner
    b7 = boards_in(P[7])[0]
    board_ok(b7)
    check(b7["n"] == 8 and b7["dots"] == [(7, 7)] and ROOK_P((7, 7)), "K-1 P7 corner second")

    # Problem 8: three piles
    p8 = piles_in(P[8])
    check(p8 == [(1, 1, 1), (1, 1, 2), (1, 2, 3), (2, 2, 3)], f"K-1 P8 piles {p8}")
    check([who(NIM_P(p)) for p in p8] == ["first", "first", "second", "first"], "K-1 P8 answers")
    check(nim_winning_moves((1, 1, 2)) == [(2, 0)], "K-1 P8 1,1,2: take the 2")
    check(nim_winning_moves((2, 2, 3)) == [(0, 1), (1, 1), (2, 0)],
          "K-1 P8 2,2,3: take the 3, or take 1 from a 2 (leaving 1,2,3)")
    check(len(nim_winning_moves((1, 1, 1))) == 3, "K-1 P8 1,1,1: take any one pile")

    # Counters needed per pair (largest single start on the page)
    return max(sum(p) for p in p5 + p6 + p8)


# ------------------------------------------------------------------- 2-3 --
def g23():
    P = problems("grades-2-3.tex")
    rules = boards_in(P[0])[0]
    board_ok(rules)
    for e in rules["arrow_ends"]:
        check(e in rook_moves(rules["dots"][0]), "2-3 rules arrow legal")

    b1 = boards_in(P[1])
    for b in b1:
        board_ok(b)
    check([(b["n"], b["dots"][0]) for b in b1] == [(5, (4, 4)), (5, (4, 2)), (5, (3, 3)), (5, (1, 4))],
          "2-3 P1 boards")
    check([who(ROOK_P(b["dots"][0])) for b in b1] == ["second", "first", "second", "first"],
          "2-3 P1 answers")
    check(winning_moves((4, 2), rook_moves, ROOK_P) == [(2, 2)], "2-3 P1 (4,2) only move")
    check(winning_moves((1, 4), rook_moves, ROOK_P) == [(1, 1)], "2-3 P1 (1,4) only move")
    rook_answer_figs("m-p1", b1, 0.1)

    b2 = boards_in(P[2])[0]
    board_ok(b2)
    red = [(a, b) for a in range(8) for b in range(8) if (a, b) != (0, 0) and ROOK_P((a, b))]
    check(b2["n"] == 8 and red == [(k, k) for k in range(1, 8)] and 63 - len(red) == 56,
          "2-3 P2: 7 red (diagonal), 56 green")
    write_fig("diag8", fig_board(8, 0.12, shade=[(k, k) for k in range(8)]))

    b3 = boards_in(P[3])[0]
    check(b3["n"] == 8 and b3["dots"] == [(7, 7)] and ROOK_P((7, 7)), "2-3 P3 top-right corner second")

    lab = pairs_in(P[4])
    p4 = piles_in(P[4])
    check(lab == [(4, 4), (6, 2), (5, 3), (7, 7)] and p4 == lab, f"2-3 P4 piles {p4} labels {lab}")
    check([who(NIM_P(p)) for p in p4] == ["second", "first", "first", "second"], "2-3 P4 answers")
    check(nim_winning_moves((6, 2)) == [(0, 2)] and nim_winning_moves((5, 3)) == [(0, 3)],
          "2-3 P4 moves: 6->2, 5->3")

    b5 = boards_in(P[5])[0]
    board_ok(b5)
    check(b5["n"] == 8 and b5["dots"] == [(5, 2)], "2-3 P5 dot at (5,2): piles 5 and 2")
    check(all(ROOK_P((a, b)) == NIM_P((a, b)) for a in range(30) for b in range(30)),
          "board square (a,b) = piles a and b")
    check(not NIM_P((5, 2)) and nim_winning_moves((5, 2)) == [(0, 2)], "2-3 P5 5,2: first, 5->2")

    p6 = pairs_in(P[6])
    check(p6 == [(52, 37)], "2-3 P6 numbers")
    check(not NIM_P((52, 37)) and nim_winning_moves((52, 37)) == [(0, 37)], "2-3 P6: first, take 15 from 52")

    lab = triples_in(P[7])
    p7 = piles_in(P[7])
    check(lab == [(1, 1, 1), (1, 1, 2), (2, 2, 3), (1, 2, 3)] and p7 == lab, f"2-3 P7 {p7} {lab}")
    check([who(NIM_P(p)) for p in p7] == ["first", "first", "first", "second"], "2-3 P7 answers")

    check("1, 2 or 3 counters" in P[8], "2-3 P8 range")
    all3 = list(combinations_with_replacement(range(1, 4), 3))
    sec3 = [p for p in all3 if NIM_P(p)]
    check(len(all3) == 10 and sec3 == [(1, 2, 3)], f"2-3 P8 {sec3}")
    # the explanation: every start with two equal piles is a first-player win
    check(all(not NIM_P(p) for p in combinations_with_replacement(range(1, 30), 3)
              if len(set(p)) < 3), "two equal piles -> first player wins")
    # every move from 1,2,3 can be answered by a move to two equal piles + empty
    for q in nim_moves((1, 2, 3)):
        check(any(sorted(r)[0] == 0 and sorted(r)[1] == sorted(r)[2] for r in nim_moves(q)),
              f"reply to {q} reaching 0,x,x")

    check("1 to 6 counters" in P[9], "2-3 P9 range")
    all6 = list(combinations_with_replacement(range(1, 7), 3))
    sec6 = [p for p in all6 if NIM_P(p)]
    check(len(all6) == 56 and len(list(combinations(range(1, 7), 3))) == 20, "2-3 P9 counts")
    check(sec6 == [(1, 2, 3), (1, 4, 5), (2, 4, 6), (3, 5, 6)], f"2-3 P9 {sec6}")


# ------------------------------------------------------------------- 4-5 --
def g45():
    P = problems("grades-4-5.tex")
    rules = boards_in(P[0])[0]
    board_ok(rules)
    for e in rules["arrow_ends"]:
        check(e in rook_moves(rules["dots"][0]), "4-5 rules arrow legal")

    b1 = boards_in(P[1])[0]
    board_ok(b1)
    check(b1["n"] == 8, "4-5 P1 8x8")

    b2 = boards_in(P[2])[0]
    board_ok(b2)
    check(b2["n"] == 8 and b2["dots"] == [(6, 3)], "4-5 P2 dot (6,3): piles 6 and 3")
    check(nim_winning_moves((6, 3)) == [(0, 3)], "4-5 P2 6,3: first, 6->3")
    pr = pairs_in(P[2])
    check(pr == [(23, 17), (30, 30)], "4-5 P2 numbers")
    check(nim_winning_moves((23, 17)) == [(0, 17)] and NIM_P((30, 30)), "4-5 P2 23,17 first; 30,30 second")

    s3 = triples_in(P[3])
    check(s3 == [(1, 1, 1), (1, 1, 2), (1, 2, 3), (2, 2, 5), (1, 3, 4), (1, 4, 5)], "4-5 P3 starts")
    check([who(NIM_P(p)) for p in s3] == ["first", "first", "second", "first", "first", "second"],
          "4-5 P3 answers")
    check(nim_winning_moves((2, 2, 5)) == [(2, 0)], "4-5 P3 2,2,5: take the 5")
    check(nim_winning_moves((1, 3, 4)) == [(2, 2)], "4-5 P3 1,3,4: only 4->2")

    check("1 to 7 counters" in P[4], "4-5 P4 range")
    all7 = list(combinations_with_replacement(range(1, 8), 3))
    sec7 = [p for p in all7 if NIM_P(p)]
    check(len(all7) == 84, "4-5 P4 84 starts")
    check(sec7 == [(1, 2, 3), (1, 4, 5), (1, 6, 7), (2, 4, 6), (2, 5, 7), (3, 4, 7), (3, 5, 6)],
          f"4-5 P4 {sec7}")

    blocks = re.findall(r"\\begin\{center\}(.*?)\\end\{center\}", P[5], re.S)
    sec, fst = triples_in(blocks[0]), triples_in(blocks[1])
    check(sec == [(1, 2, 3), (1, 4, 5), (2, 4, 6), (3, 5, 6), (2, 5, 7)] and all(NIM_P(p) for p in sec),
          "4-5 P5 second-player list")
    check(fst == [(1, 2, 4), (2, 3, 5), (2, 4, 7), (3, 4, 6)] and all(not NIM_P(p) for p in fst),
          "4-5 P5 first-player list")
    exp5 = {(1, 2, 4): [(2, 3)], (2, 3, 5): [(2, 1)], (2, 4, 7): [(2, 6)], (3, 4, 6): [(0, 2)]}
    for p, m in exp5.items():
        check(nim_winning_moves(p) == m, f"4-5 P5 {p} winning move {nim_winning_moves(p)}")
    # the stack rule (Bouton) agrees with brute force for all piles up to 20
    check(all(NIM_P(p) == (p[0] ^ p[1] ^ p[2] == 0)
              for p in combinations_with_replacement(range(0, 21), 3)), "stack rule = brute force")

    s6 = [tuple(int(v) for v in t) for t in re.findall(r"makebox\[1\.2in\]\[l\]\{(\d+), (\d+), (\d+)\}", P[6])]
    check(s6 == [(3, 5, 7), (6, 10, 12), (13, 9, 7), (11, 14, 21)], "4-5 P6 starts")
    check([who(NIM_P(p)) for p in s6] == ["first", "second", "first", "first"], "4-5 P6 answers")
    check(nim_winning_moves((3, 5, 7)) == [(0, 2), (1, 4), (2, 6)], "4-5 P6 3,5,7: take 1 from any pile")
    check(nim_winning_moves((13, 9, 7)) == [(2, 4)], "4-5 P6 13,9,7: only 7->4")
    check(nim_winning_moves((11, 14, 21)) == [(2, 5)], "4-5 P6 11,14,21: only 21->5")

    b8 = boards_in(P[8])
    qrule, q8 = b8[0], b8[1]
    board_ok(qrule)
    board_ok(q8)
    for e in qrule["arrow_ends"]:
        check(e in queen_moves(qrule["dots"][0]), "4-5 queen rule arrow legal")
    check(sorted(qrule["arrow_ends"]) == sorted([(0, 4), (3, 0), (0, 1)]), "4-5 queen arrows")
    red8 = sorted(q for q in [(a, b) for a in range(8) for b in range(8)] if q != (0, 0) and QUEEN_P(q))
    check(q8["n"] == 8 and red8 == sorted([(1, 2), (2, 1), (3, 5), (5, 3), (4, 7), (7, 4)]), f"4-5 P8 {red8}")
    write_fig("queen8", fig_board(8, 0.12, shade=red8 + [(0, 0)]))

    b9 = boards_in(P[9])[0]
    board_ok(b9)
    red20 = sorted(q for q in [(a, b) for a in range(20) for b in range(20)] if q != (0, 0) and QUEEN_P(q))
    pairs20 = [(1, 2), (3, 5), (4, 7), (6, 10), (8, 13), (9, 15), (11, 18)]
    check(b9["n"] == 20 and red20 == sorted(pairs20 + [(b, a) for a, b in pairs20]) and len(red20) == 14,
          f"4-5 P9 {red20}")
    check(QUEEN_P((12, 20)), "next pair (12,20) is just off the 20x20 board")
    write_fig("queen20", fig_board(20, 0.057, shade=red20 + [(0, 0)], lw="0.2pt", star=False))

    # Wythoff facts used in the guide: pairs ([n*phi], [n*phi^2]), difference n,
    # built by "smallest unused number, then add the next difference"
    import math
    phi = (1 + 5 ** 0.5) / 2
    pairs = [(a, b) for a in range(60) for b in range(a, 60) if QUEEN_P((a, b))]
    check(pairs[:10] == [(math.floor(n * phi), math.floor(n * phi * phi)) for n in range(10)],
          "Wythoff pairs = floor(n phi), floor(n phi^2)")
    used, built = set(), []
    for n in range(10):
        a = next(k for k in range(100) if k not in used)
        built.append((a, a + n))
        used |= {a, a + n}
    check(built == pairs[:10], "Wythoff pairs by smallest-unused rule")

    check(64 - 1 - len(red8) == 57, "4-5 P8: 57 green squares")
    return max(sum(p) for p in s6)


# ------------------------------------------------ fallback games (Sec. 3) --
def fallbacks():
    # Take 1, 2 or 3 from one pile; last counter wins: P-positions are the
    # multiples of 4, so from 20 you would rather go second.
    take123 = solver(lambda n: [n - k for k in (1, 2, 3) if n - k >= 0])
    check(all(take123(n) == (n % 4 == 0) for n in range(60)) and take123(20), "take 1,2,3")

    # Last counter loses (misere Nim), three piles: the player to move loses
    # exactly when (all piles <= 1 and an odd number of 1s) or (some pile >= 2
    # and nim-sum 0).  This is the strategy printed in the guide.
    @lru_cache(None)
    def mis_p(p):
        if sum(p) == 0:
            return False  # the previous player took the last counter and lost
        return all(not mis_p(tuple(sorted(q))) for q in nim_moves(p))
    ok = True
    for p in combinations_with_replacement(range(0, 9), 3):
        rule = (sum(p) % 2 == 1) if max(p) <= 1 else (p[0] ^ p[1] ^ p[2] == 0)
        ok &= mis_p(p) == rule
    check(ok, "misere Nim rule")


if __name__ == "__main__":
    k1max = k1()
    g23()
    u_max = g45()
    fallbacks()
    print(f"K-1 largest start on the page: {k1max} counters")
    print(f"4-5 largest start in Problem 6: {u_max} counters")
    print(f"{NCHECK} checks, {len(FAILS)} failed")
    sys.exit(1 if FAILS else 0)
