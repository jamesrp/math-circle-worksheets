#!/usr/bin/env python3
"""Generate LaTeX sources for the Week 7 take-away game student pages."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

R = 0.30   # counter radius (cm)
S = 0.85   # counter spacing (cm)


def preamble(level, size="12pt", cls="article"):
    return rf"""\documentclass[{size},letterpaper]{{{cls}}}
\usepackage[letterpaper,left=0.7in,right=0.7in,top=0.85in,bottom=0.85in,headheight=18pt,headsep=14pt,footskip=0.45in]{{geometry}}
\usepackage[T1]{{fontenc}}
\usepackage{{newcent}}
\usepackage{{tikz}}
\usepackage{{array}}
\usepackage{{fancyhdr}}
\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[L]{{Week 7 / Take-away games / {level}}}
\fancyfoot[L]{{Bellingham Math Circle / Week 7}}
\fancyfoot[R]{{\thepage}}
\renewcommand{{\headrulewidth}}{{0.4pt}}
\renewcommand{{\footrulewidth}}{{0pt}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0pt}}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\newcommand{{\prob}}[1]{{\textbf{{Problem #1:}}}}
\newcommand{{\game}}[1]{{\mbox{{\{{#1\}}}}}}
\newenvironment{{problem}}{{\par\noindent\begin{{minipage}}{{\linewidth}}}}{{\end{{minipage}}\par\vspace{{0.9cm}}}}
\begin{{document}}
"""


END = r"\end{document}" + "\n"


# ---------------------------------------------------------------- TikZ helpers
def counter(x, y, r=R):
    return f"\\draw[fill=black!12,line width=0.9pt] ({x:.3f},{y:.3f}) circle ({r});"


def counters(x0, y0, n, perrow=5, s=S, r=R):
    """Counters with the first one centred at (x0, y0), rows going down."""
    out = []
    for i in range(n):
        c, rw = i % perrow, i // perrow
        out.append(counter(x0 + c * s, y0 - rw * s, r))
    return out


def tray(x, y, w, h):
    return (f"\\draw[black!55,line width=0.7pt,rounded corners=7pt] "
            f"({x:.3f},{y:.3f}) rectangle ({x + w:.3f},{y - h:.3f});")


def rows_needed(n, perrow):
    return (n + perrow - 1) // perrow


def pile_panel(piles, cols, tray_w=5.0, perrow=5, gap=1.0, label=True,
               choice=None, choice_font=r"\Large", rowgap=0.9, s=S, r=R, pad=0.6):
    """Single piles in trays laid out in a grid. Returns tikzpicture code."""
    out = [r"\begin{tikzpicture}"]
    y = 0.0
    for start in range(0, len(piles), cols):
        row = piles[start:start + cols]
        h = max(rows_needed(n, perrow) for n in row) * s + 2 * pad - s
        for j, n in enumerate(row):
            x = j * (tray_w + gap)
            out.append(tray(x, y, tray_w, h))
            out += counters(x + pad, y - pad, n, perrow, s, r)
            below = y - h
            if label:
                out.append(f"\\node[font=\\small] at ({x + tray_w / 2:.3f},{below - 0.35:.3f}) {{{n}}};")
                below -= 0.55
            if choice:
                a, b = choice
                out.append(f"\\node[font={choice_font}] at ({x + tray_w * 0.28:.3f},{below - 0.55:.3f}) {{{a}}};")
                out.append(f"\\node[font={choice_font}] at ({x + tray_w * 0.72:.3f},{below - 0.55:.3f}) {{{b}}};")
                below -= 1.0
        y = below - rowgap
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def two_pile_panel(cases, cols, perrow=2, gap=1.2, choice=("1st", "2nd"),
                   choice_font=r"\Large", rowgap=0.7, inner=0.45, s=S, r=R, pad=0.6,
                   frame=True):
    out = [r"\begin{tikzpicture}"]
    sub_w = (perrow - 1) * s + 2 * pad
    case_w = 2 * sub_w + inner
    fp = 0.35 if frame else 0.0
    y = 0.0
    for start in range(0, len(cases), cols):
        row = cases[start:start + cols]
        h = max(rows_needed(n, perrow) for c in row for n in c) * s + 2 * pad - s
        for j, (a, b) in enumerate(row):
            x = j * (case_w + 2 * fp + gap)
            for k, n in enumerate((a, b)):
                xx = x + k * (sub_w + inner)
                out.append(tray(xx, y, sub_w, h))
                out += counters(xx + pad, y - pad, n, perrow, s, r)
            below = y - h
            if choice:
                c1, c2 = choice
                mid = x + case_w / 2
                out.append(f"\\node[font={choice_font},anchor=east] at ({mid - 0.35:.3f},{below - 0.9:.3f}) {{{c1}}};")
                out.append(f"\\node[font={choice_font},anchor=west] at ({mid + 0.35:.3f},{below - 0.9:.3f}) {{{c2}}};")
                below -= 1.45
            if frame:
                out.append(f"\\draw[black!35,line width=0.6pt,rounded corners=4pt] "
                           f"({x - fp:.3f},{y + fp:.3f}) rectangle ({x + case_w + fp:.3f},{below - 0.1:.3f});")
                below -= 0.1
        y = below - rowgap
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def track(n, perrow=10, b=1.55, font=r"\Large"):
    out = [r"\begin{tikzpicture}"]
    for i in range(n):
        c, rw = i % perrow, i // perrow
        x, y = c * b, -rw * (b + 0.35)
        out.append(f"\\draw[line width=0.8pt] ({x:.3f},{y:.3f}) rectangle ({x + b:.3f},{y - b:.3f});")
        out.append(f"\\node[font={font}] at ({x + b / 2:.3f},{y - b / 2:.3f}) {{{i + 1}}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def chart(n, perrow=10, b=1.6, numfont=r"\small", gap=0.3):
    """Boxes with the pile number in the top-left corner and room to write."""
    out = [r"\begin{tikzpicture}"]
    for i in range(n):
        c, rw = i % perrow, i // perrow
        x, y = c * b, -rw * (b + gap)
        out.append(f"\\draw[line width=0.8pt] ({x:.3f},{y:.3f}) rectangle ({x + b:.3f},{y - b:.3f});")
        out.append(f"\\node[font={numfont},anchor=north west,inner sep=2pt] at ({x:.3f},{y:.3f}) {{{i + 1}}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def strip(label, n=20, c=0.78, labw=2.1):
    out = [r"\begin{tikzpicture}"]
    out.append(f"\\node[anchor=west] at (0,{-c / 2:.3f}) {{{label}}};")
    for i in range(n):
        x = labw + i * c
        out.append(f"\\draw[line width=0.7pt] ({x:.3f},0) rectangle ({x + c:.3f},{-c:.3f});")
        out.append(f"\\node[font=\\footnotesize] at ({x + c / 2:.3f},{-c / 2:.3f}) {{{i + 1}}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def grid(n, c=1.05):
    """Square grid for two piles, rows and columns labelled 0..n-1."""
    out = [r"\begin{tikzpicture}"]
    for i in range(n + 1):
        out.append(f"\\draw[line width=0.7pt] (0,{-i * c:.3f}) -- ({n * c:.3f},{-i * c:.3f});")
        out.append(f"\\draw[line width=0.7pt] ({i * c:.3f},0) -- ({i * c:.3f},{-n * c:.3f});")
    for i in range(n):
        out.append(f"\\node at ({(i + 0.5) * c:.3f},0.32) {{{i}}};")
        out.append(f"\\node at (-0.32,{-(i + 0.5) * c:.3f}) {{{i}}};")
    out.append(f"\\node[font=\\small] at ({n * c / 2:.3f},0.85) {{column}};")
    out.append(f"\\node[font=\\small,rotate=90] at (-1.15,{-n * c / 2:.3f}) {{row}};")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def center(code):
    return "\\begin{center}\n" + code + "\n\\end{center}\n"


def table(head, rows, widths, height=1.15):
    cols = "|".join(f">{{\\centering\\arraybackslash}}m{{{w}cm}}" for w in widths)
    lines = [r"\begin{center}", r"\renewcommand{\arraystretch}{1.25}",
             f"\\begin{{tabular}}{{|{cols}|}}", r"\hline",
             " & ".join(head) + r" \\ \hline"]
    for r in rows:
        cells = list(r) + [""] * (len(widths) - len(r))
        cells[0] = cells[0] + f"\\rule[-{height / 2 - 0.15:.2f}cm]{{0pt}}{{{height:.2f}cm}}"
        lines.append(" & ".join(cells) + r" \\ \hline")
    lines += [r"\end{tabular}", r"\end{center}"]
    return "\n".join(lines)


def problem(n, text, body="", space=0.0):
    text = re.sub(r"\\\{([0-9, ]+)\\\}", r"\\game{\1}", text)
    s = "\\begin{problem}\n\\prob{%d} %s\n" % (n, text)
    if body:
        s += body + "\n"
    if space:
        s += "\\vspace{%.1fcm}\n" % space
    s += "\\end{problem}\n"
    return s


def write(name, content):
    with open(os.path.join(HERE, name), "w") as f:
        f.write(content)


# ====================================================================== K-1
KS, KR, KP = 1.0, 0.36, 0.65   # bigger counters for the youngest children


def k1():
    big = dict(s=KS, r=KR, pad=KP)
    t = preamble("Grades K--1", size="14pt", cls="extarticle")
    t += ("Two players take turns taking counters from a pile. On each turn, a player "
          "takes 1 counter or 2 counters. Whoever takes the last counter wins.\n\n\\vspace{0.7cm}\n")
    t += problem(1, "It is your turn. Circle the counters you take now to be sure to win, "
                    "or cross out the pile if you cannot be sure to win.",
                 center(pile_panel([1, 2, 3, 4, 5], cols=3, tray_w=5.3, gap=0.85, **big)))
    t += problem(2, "Circle 1st or 2nd to show which player can be sure to win "
                    "with each pile.",
                 center(pile_panel([6, 7, 8, 9], cols=2, tray_w=5.3, gap=2.4,
                                   choice=("1st", "2nd"), **big)))
    t += problem(3, "It is your turn with a bigger pile. Circle the counters you take now to be "
                    "sure to win, or cross out the pile if you cannot be sure to win.",
                 center(pile_panel([10, 11, 12], cols=3, tray_w=5.3, gap=0.85, **big)))
    t += problem(4, "A pile is a trap if you cannot be sure to win when it is your turn. "
                    "Put an X on every trap from 1 to 20.",
                 "\\vspace{0.2cm}\n" + center(track(20, b=1.65)))
    t += problem(5, "Ben goes first and takes 2 counters. Put a check by each pile where Ben can "
                    "still be sure to win.",
                 center(pile_panel([4, 5, 7, 8, 10, 11], cols=3, tray_w=5.3, gap=0.85, **big)))
    # every way a game can go
    ways = [r"\begin{tikzpicture}"]
    sp, vp = 1.45, 1.8
    for i in range(5):
        ways += counters(0, -i * vp, 4, perrow=4, s=sp, r=KR)
    for i in range(8):
        ways += counters(7.8, -i * vp, 5, perrow=5, s=sp, r=KR)
    ways.append(r"\end{tikzpicture}")
    t += problem(6, "Show every different way a game with 4 counters can go, and then every "
                    "way a game with 5 counters can go. Circle the counters taken on each turn.",
                 "\\vspace{0.3cm}\n" + center("\n".join(ways)))
    t += problem(7, "Now each player may take 1, 2, or 3 counters on a turn. Put an X on "
                    "every trap from 1 to 20.",
                 "\\vspace{0.2cm}\n" + center(track(20, b=1.65)))
    t += problem(8, "Now there are two piles, and on your turn you take 1 or 2 counters from "
                    "one pile. Whoever takes the last counter on the table wins. "
                    "Circle 1st or 2nd to show which player can be sure to win.",
                 center(two_pile_panel([(1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (1, 4)],
                                       cols=2, gap=2.0, rowgap=1.0, **big)))
    t += problem(9, "Play the game from Problem 8 with two piles of 6 counters. If you go "
                    "second, how can you win every time, whatever the other player does?",
                 center(two_pile_panel([(6, 6)], cols=1, perrow=3, choice=None, inner=1.2,
                                       frame=False, **big)))
    t += problem(10, "Now there is one pile again. Each player takes 1 or 2 counters, and "
                     "whoever takes the last counter loses. Put an X on every trap from 1 to 20.",
                 "\\vspace{0.2cm}\n" + center(track(20, b=1.65)))
    t += END
    write("k-1.tex", t)


# ==================================================================== 2-3
def g23():
    t = preamble("Grades 2--3")
    t += ("In every game in this packet, two players take turns taking counters from a pile. "
          "Each problem says how many counters a player may take on a turn. "
          "Unless a problem says otherwise, whoever takes the last counter wins. "
          "If you cannot take any counters on your turn, you lose.\n\n\\vspace{0.7cm}\n")
    t += problem(1, "On each turn, a player takes 1 or 2 counters. For each starting pile in "
                    "the table, decide whether you would rather go first or second. If you would "
                    "rather go first, also write how many counters you take on your first turn.",
                 table(["Starting pile", "First or second?", "Counters you take first"],
                       [[str(n)] for n in range(5, 11)], [3.2, 4.6, 5.4]))
    t += problem(2, "Use the rule from Problem 1. Lee says, ``With 12 counters, I will go second "
                    "and always win. Whenever you take 1, I take 2, and whenever you take 2, I "
                    "take 1.'' Mo says, ``With 10 counters, I will go first and take 2, and then "
                    "I can always win.'' Decide whether each claim is right. If a claim is right, "
                    "explain why it always works. If it is wrong, show how to beat it.",
                 space=8.0)
    t += problem(3, "Now on each turn a player takes 1, 3, or 4 counters. Jo starts with 10 "
                    "counters and goes first. She takes 3, leaving 7, and says she can now win "
                    "however the other player plays. Kai starts with 12 counters and goes first. He "
                    "takes 4, leaving 8, and says the same thing. Decide whether each claim is "
                    "right. If a claim is right, show how to answer every move the other player can "
                    "make, all the way to the end of the game. If it is wrong, show how the "
                    "other player can win.",
                 space=10.5)
    t += problem(4, "Use the rule from Problem 3: take 1, 3, or 4 counters on each turn. For "
                    "each starting pile from 1 to 20, decide whether you would rather go first "
                    "or second. Shade the box of every pile where you would rather go second. "
                    "In every other box, write how many counters you take on your first turn.",
                 "\\vspace{0.2cm}\n" + center(chart(20)))
    t += problem(5, "Keep the rule from Problem 3. For each starting pile in the table, decide "
                    "whether you would rather go first or second. If you would rather go first, "
                    "also write how many counters you take on your first turn.",
                 table(["Starting pile", "First or second?", "Counters you take first"],
                       [["30"], ["50"], ["61"], ["100"]], [3.2, 4.6, 5.4]), space=1.0)
    t += problem(6, "Now on each turn a player takes 1, 3, or 5 counters. Shade the box of every "
                    "starting pile from 1 to 20 where you would rather go second. Explain why the "
                    "second player can always win from those piles.",
                 "\\vspace{0.2cm}\n" + center(chart(20, b=1.3)), space=6.0)
    t += problem(7, "Now there are two piles. On each turn, a player takes 1 or 2 counters from "
                    "one of the piles. Whoever takes the last counter on the table wins. "
                    "For each pair of piles below, circle whether you would "
                    "rather go first or second. When the two piles are the same size, which "
                    "player can always win? Explain why.",
                 center(two_pile_panel([(3, 3), (4, 2), (4, 1), (4, 4)], cols=2, perrow=2,
                                       gap=2.0, choice=("First", "Second"),
                                       choice_font=r"\large")),
                 space=6.0)
    t += problem(8, "Find a rule for how many counters a player may take on a turn, so that you "
                    "would rather go second exactly when the starting pile is 5, 10, 15, 20, 25, "
                    "and so on. Then find a different rule that does the same thing.",
                 space=10.0)
    t += problem(9, "Now whoever takes the last counter loses. On each turn a player takes 1, 3, "
                    "or 4 counters. Shade the box of every starting pile from 1 to 20 where you "
                    "would rather go second.",
                 "\\vspace{0.2cm}\n" + center(chart(20)))
    t += END
    write("grades-2-3.tex", t)


# ==================================================================== 4-5
def g45():
    t = preamble("Grades 4--5")
    t += ("In every game in this packet, two players take turns taking counters from a pile. "
          "Each problem says how many counters a player may take on a turn. Unless a problem "
          "says otherwise, whoever takes the last counter wins. "
          "If you cannot take any counters on your turn, you lose.\n\n\\vspace{0.7cm}\n")
    t += problem(1, "On each turn, a player takes 1, 3, or 4 counters. For each starting pile "
                    "from 1 to 24, decide whether you would rather go first or second. Shade the "
                    "box of every pile where you would rather go second. In every other box, "
                    "write how many counters you could take on your first turn to be sure to win.",
                 "\\vspace{0.2cm}\n" + center(chart(24, perrow=12, b=1.4)))
    t += problem(2, "A starting pile where you would rather go second is called a losing pile. "
                    "Every other starting pile is a winning pile. With the rule from Problem 1, "
                    "decide whether piles of 100, 1000, and 2026 counters are winning or losing. "
                    "For each winning pile, write how many counters to take first.",
                 table(["Starting pile", "Winning or losing?", "Counters to take first"],
                       [["100"], ["1000"], ["2026"]], [3.2, 4.6, 5.4]), space=3.5)
    strips = "\n\n\\vspace{2.4cm}\n".join(
        strip(lab) for lab in [r"\{1, 2\}", r"\{1, 2, 4\}", r"\{1, 4\}", r"\{1, 3, 5\}"])
    t += problem(3, "From now on, a game is named by its list of allowed moves, so the game in "
                    "Problem 1 is the \\{1, 3, 4\\} game. Shade the losing piles from 1 to 20 in "
                    "each of the games \\{1, 2\\}, \\{1, 2, 4\\}, \\{1, 4\\}, and \\{1, 3, 5\\}. "
                    "Describe the pattern of losing piles in each game.",
                 "\\vspace{0.4cm}\n\n" + strips, space=2.4)
    t += problem(4, "Dana's plan is to always take the biggest number of counters she is allowed "
                    "to take from the pile. In which "
                    "of the games \\{1, 2\\}, \\{1, 3, 4\\}, \\{1, 4\\}, and \\{1, 3, 5\\} does "
                    "Dana's plan always win when she starts at a winning pile? For each game where "
                    "it does not, find a winning pile where the plan loses against good play. For "
                    "each game where it does, explain why it always wins.",
                 table(["Game", "Does the plan always win?", "A winning pile where it loses"],
                       [[r"\{1, 2\}"], [r"\{1, 3, 4\}"], [r"\{1, 4\}"], [r"\{1, 3, 5\}"]],
                       [3.2, 5.6, 5.6]), space=5.0)
    t += problem(5, "Explain why the pattern of losing piles you found in Problem 1 must keep "
                    "going forever, for piles of every size.", space=8.0)
    t += problem(6, "Find every game whose allowed moves are some of the numbers 1, 2, 3, 4, 5, "
                    "and 6, and whose losing piles are exactly the multiples of 4. Explain why "
                    "your list is complete.", space=9.0)
    strips2 = "\n\n\\vspace{0.6cm}\n".join(strip(lab) for lab in [r"\{1, 2\}", r"\{1, 3, 4\}"])
    t += problem(7, "Change the rule so that whoever takes the last counter loses. Shade the "
                    "losing piles from 1 to 20 in the \\{1, 2\\} game and in the \\{1, 3, 4\\} "
                    "game with this new rule. Compare them with the losing piles you found when "
                    "taking the last counter wins, and explain the difference.",
                 "\\vspace{0.4cm}\n\n" + strips2, space=6.0)
    t += problem(8, "Now there are two piles. On each turn, a player takes 1 or 2 counters from "
                    "one of the piles, and whoever takes the last counter on the table wins. In the grid, the "
                    "square in row 3 and column 1 stands for a pile of 3 counters and a pile of "
                    "1 counter, and row 0 or column 0 stands for an empty pile. Shade every square "
                    "where you would rather go second. When the two piles are the same size, "
                    "which player can always win? Explain why.",
                 "\\vspace{0.3cm}\n" + center(grid(8)), space=4.0)
    t += problem(9, "Play the two-pile game again, but now each move takes 1, 3, or 4 counters "
                    "from one of the piles. Find every pair of piles of different sizes, each "
                    "with 1 to 8 counters, where you would rather go second. The grid works the "
                    "same way as in Problem 8.",
                 "\\vspace{0.3cm}\n" + center(grid(9, c=1.0)), space=2.0)
    t += END
    write("grades-4-5.tex", t)


if __name__ == "__main__":
    k1()
    g23()
    g45()
