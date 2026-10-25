"""TikZ figures for the Hex facilitator guide.

Writes figs/*.tex, which facilitator.tex inputs.  hexgeom.py is copied
unchanged from the student source (plans/topic-scouting/drafts/hex/src/), so
the guide's boards are drawn exactly like the students' boards.  Every
position drawn here is checked in check_guide.py.

Run:  python3 figs.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hexgeom as h  # noqa: E402
import check_guide as cg  # noqa: E402

OUT = os.path.join(HERE, "figs")
os.makedirs(OUT, exist_ok=True)


def save(name, tex):
    with open(os.path.join(OUT, name + ".tex"), "w") as f:
        f.write(tex + "\n")


def add(tikz, extra):
    return tikz.replace(r"\end{tikzpicture}", extra + "\n" + r"\end{tikzpicture}")


def mini(n, w, counters=None, fills=None, band=2.2, stars=(), lw=0.35, cs=0.36):
    return h.hex_board(n, w, band=band, labels=False, counters=counters or {}, fills=fills or {},
                       stars=stars, line_width=lw, counter_scale=cs, star_size=0.45 * w)


def ctrs(red, blue):
    d = {p: 'R' for p in red}
    d.update({p: 'B' for p in blue})
    return d


def text_at(cells, w, label, size=r"\scriptsize\bfseries"):
    out = []
    for (r, c) in cells:
        x, y = h.centre(r, c, w)
        out.append(rf"\node[font={size}] at ({x:.3f},{y:.3f}) {{{label}}};")
    return "\n".join(out)


def caption(n, w, band, text):
    """A caption node centred under a board."""
    xs = [h.centre(r, c, w)[0] for r in range(n) for c in range(n)]
    x = (min(xs) + max(xs)) / 2
    y = h.centre(n - 1, 0, w)[1] - w / 1.732 - band - 2.6
    return rf"\node[font=\footnotesize,anchor=north] at ({x:.3f},{y:.3f}) {{{text}}};"


# ------------------------------------------------------------ launch panels

EX_RED = [(0, 2), (1, 2), (2, 1), (3, 1), (3, 2), (4, 2), (5, 1)]
EX_BLUE = [(1, 1), (2, 2), (2, 3), (4, 1), (4, 3), (1, 4)]
L_RED = [(0, 2), (1, 2), (2, 1), (3, 1)]
L_BLUE = [(1, 1), (2, 2), (2, 3), (4, 1)]


def launch_panels():
    w, band = 4.8, 2.0
    p1 = mini(6, w, ctrs(L_RED, L_BLUE), band=band)
    p1 = add(p1, caption(6, w, band, "Input: Red to move"))
    p2 = mini(6, w, ctrs(L_RED + [(3, 2)], L_BLUE), band=band)
    x, y = h.centre(3, 2, w)
    p2 = add(p2, rf"\draw[black,line width=1.1pt] ({x:.3f},{y:.3f}) circle ({0.47 * w:.3f});" + "\n" +
             caption(6, w, band, "One step: a sideways move"))
    p3 = mini(6, w, ctrs(EX_RED, EX_BLUE), band=band)
    pts = " -- ".join("({:.3f},{:.3f})".format(*h.centre(r, c, w)) for r, c in EX_RED)
    top = h.centre(0, 2, w)
    bot = h.centre(5, 1, w)
    R = w / 1.732
    line = (rf"\draw[black,line width=1.2pt,line cap=round] ({top[0]:.3f},{top[1] + R + band * 0.6:.3f}) -- {pts}"
            rf" -- ({bot[0]:.3f},{bot[1] - R - band * 0.6:.3f});")
    p3 = add(p3, line + "\n" + caption(6, w, band, "Output: trace the chain"))
    save("launch-panels", p1 + r"\hspace{6mm}" + p2 + r"\hspace{6mm}" + p3)


def launch_board():
    """Full-size 6 x 6 board (24 mm hexagons) for the whole-group launch."""
    tikz = h.hex_board(6, 24.0, band=8.0, label_size=r"\small")
    save("launch-board", tikz)


# ------------------------------------------------------------ answers

def openings():
    w, band = 6.0, 2.0
    win = [(0, 2), (1, 0), (1, 1), (1, 2), (2, 0)]
    b = mini(3, w, band=band)
    b = add(b, text_at(win, w, "W"))
    save("openings", b)


def p5_answer():
    w, band = 5.0, 2.0
    red = [(0, 2), (1, 2), (2, 2), (3, 2), (4, 0)]
    blue = [(3, 0), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]
    save("p5-answer", mini(5, w, ctrs(red, blue), band=band))


def puzzle_answers():
    w, band = 4.6, 2.0
    games = [
        ([(0, 1), (1, 1), (2, 1)], [(3, 0), (0, 3)], [(3, 1)], "P6 top: yes"),
        ([(0, 2), (1, 1), (3, 0)], [(1, 2), (2, 2)], [], "P6 bottom: no"),
        ([(1, 1), (2, 2)], [(0, 0)], [], "P7 top: no"),
        ([(0, 0), (1, 1), (2, 2)], [(2, 3), (3, 2)], [(2, 1)], "P7 bottom: yes"),
    ]
    parts = []
    for red, blue, stop, cap in games:
        b = mini(4, w, ctrs(red, blue), band=band)
        b = add(b, text_at(stop, w, r"X", size=r"\small\bfseries") + "\n" + caption(4, w, band, cap))
        parts.append(b)
    save("puzzle-answers", (r"\hspace{4mm}").join(parts))


def walk_answers():
    w, band = 5.6, 2.0
    boards = [
        ["BRBBR", "BRRRB", "RBBRB", "BRRBR", "BRBRB"],
        ["RRBRB", "BRRBR", "RBRBB", "BBRBR", "RBBRB"],
    ]
    caps = ["Board 1: ends bottom left (23 sides)", "Board 2: ends top right (26 sides)"]
    parts = []
    for rows, cap in zip(boards, caps):
        col = {(r, c): rows[r][c] for r in range(5) for c in range(5)}
        end, verts = cg.walk(5, col, vertices=True)
        pts = []
        for V in verts:
            xs = [h.centre(r, c, w) for (r, c) in V]
            pts.append((sum(p[0] for p in xs) / 3, sum(p[1] for p in xs) / 3))
        b = h.hex_board(5, w, band=band, labels=False, fills=col, line_width=0.3)
        path = " -- ".join("({:.3f},{:.3f})".format(*p) for p in pts)
        b = add(b, rf"\draw[black,line width=1.3pt,line join=round,line cap=round] {path};" + "\n" +
                rf"\fill[black] ({pts[0][0]:.3f},{pts[0][1]:.3f}) circle (0.9);" + "\n" +
                caption(5, w, band, cap))
        parts.append(b)
    save("walk-answers", (r"\hspace{8mm}").join(parts))


if __name__ == "__main__":
    launch_panels()
    launch_board()
    openings()
    p5_answer()
    puzzle_answers()
    walk_answers()
    print("figures written to", OUT)
