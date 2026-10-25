#!/usr/bin/env python3
"""Generate the three Pancake flips student packets (LaTeX + TikZ) and compile them.

Stacks are written from the top. For pancakes with a dark side, a negative
number means the dark side faces up, a positive number means it faces down.

Revision of the draft after review.md and review-math.md:
- K-1 opens with all six three-stacks; the four-stack worst case is now
  "sort these" (three worst stacks and one 3-flip decoy) instead of
  "find one that cannot"; three blanks for the three one-flip stacks;
  taller recording slots with gaps.
- 2-3 order: sort, worst three-stack, six-stacks (two scrambled), method,
  four-stack hunt, then dark sides; the two-stack dark-side search is now
  the child's.
- 4-5 Problem 3 uses 3 5 2 1 4 (four breaks, not a worst stack), so
  Problem 5 stays a real hunt; break definition and marks clarified;
  outlines for recording a dark-side stack.
- Every band gets a worked dark-side flip (2, 1 dark up, 3; flip 2) beside
  its first dark-side problem; dark-side drawings have small gaps.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)  # final/
sys.path.insert(0, HERE)
from check import bfs_unburnt, bfs_burnt, breaks  # noqa: E402

WEEK = "NN"

# ---------------------------------------------------------------- drawing

PH = 0.15   # plate thickness (cm, before scaling)
H = 0.5     # pancake thickness
GAP = 0.2   # gap that holds the spatula
BSEP = 0.12  # gap between pancakes in dark-side drawings (cm)
SSEP = 0.14  # gap between blank recording slots (cm)


def pw(size, sc):
    return (0.7 + 0.32 * size) * sc


def fmt(v):
    return f"{v:.3f}"


def stack_cmds(x0, stack, sc, *, burnt=False, spatula=None, code=None,
               marks=False, plate_label=None, blank=0, blank_w=1.8,
               blank_h=None, numsize=r"\small", sep=0.0, plate_gap=0.0):
    """TikZ commands for one stack centred at x0 with the plate top at y=0.

    sep: gap between neighbouring pancakes (cm); plate_gap: gap above plate.
    Returns (cmds, top_y, bottom_y, right_x).
    """
    c = []
    h = H * sc
    if blank:
        n = blank
        bh = (blank_h or H) * sc
        widths = [blank_w * sc] * n
    else:
        n = len(stack)
        bh = h
        widths = [pw(abs(s), sc) for s in stack]
    wmax = max(widths) if widths else blank_w * sc
    plate_w = wmax + 0.5 * sc
    ph = PH * sc
    # plate
    c.append(rf"\draw[platedraw, platefill, rounded corners={fmt(ph/2)}cm] "
             rf"({fmt(x0-plate_w/2)},{fmt(-ph)}) rectangle ({fmt(x0+plate_w/2)},0);")
    right = x0 + plate_w / 2
    # stack bottom-up
    y = 0.0
    junction_y = {}   # spatula position below pancake k (1-based from top)
    gap_mid = [0.0] * n  # centre of the gap below pancake idx (0-based)
    ys = [0.0] * n
    for idx in range(n - 1, -1, -1):
        k = idx + 1
        if spatula == k:
            g = GAP * sc
            junction_y[k] = y + g / 2
        else:
            g = plate_gap if idx == n - 1 else sep
        gap_mid[idx] = y + g / 2
        y += g
        ys[idx] = y
        y += bh
    top = y
    for idx in range(n):
        w = widths[idx]
        yb = ys[idx]
        if blank:
            c.append(rf"\draw[slot, rounded corners={fmt(min(bh, w)*0.25)}cm] "
                     rf"({fmt(x0-w/2)},{fmt(yb)}) rectangle ({fmt(x0+w/2)},{fmt(yb+bh)});")
            continue
        s = stack[idx]
        rc = fmt(h * 0.42)
        shape = rf"[rounded corners={rc}cm] ({fmt(x0-w/2)},{fmt(yb)}) rectangle ({fmt(x0+w/2)},{fmt(yb+h)})"
        c.append(rf"\fill[cakefill] {shape};")
        ny = yb + h / 2
        if burnt:
            band = 0.3 * h
            c.append(r"\begin{scope}")
            c.append(rf"\clip {shape};")
            if s < 0:  # dark side up
                c.append(rf"\fill[burnt] ({fmt(x0-w/2)},{fmt(yb+h-band)}) rectangle ({fmt(x0+w/2)},{fmt(yb+h)});")
                ny = yb + (h - band) / 2
            else:
                c.append(rf"\fill[burnt] ({fmt(x0-w/2)},{fmt(yb)}) rectangle ({fmt(x0+w/2)},{fmt(yb+band)});")
                ny = yb + band + (h - band) / 2
            c.append(r"\end{scope}")
        c.append(rf"\draw[cakedraw] {shape};")
        c.append(rf"\node[font={numsize}\bfseries, inner sep=0pt] at ({fmt(x0)},{fmt(ny)}) {{{abs(s)}}};")
    # spatula
    if spatula:
        jy = junction_y[spatula]
        wk = widths[spatula - 1]
        bx0 = x0 - wk / 2 + 0.25 * sc
        bx1 = x0 + wmax / 2 + 0.55 * sc
        bt = 0.035 * sc
        c.append(rf"\fill[spatula, rounded corners=0.5pt] ({fmt(bx0)},{fmt(jy-bt)}) rectangle ({fmt(bx1)},{fmt(jy+bt)});")
        ht = 0.11 * sc
        hx1 = bx1 + 0.9 * sc
        c.append(rf"\fill[handle, rounded corners={fmt(ht*0.9)}cm] ({fmt(bx1)},{fmt(jy-ht)}) rectangle ({fmt(hx1)},{fmt(jy+ht)});")
        right = max(right, hx1)
    # break marks: a red line lying in the gap, wider than both neighbours
    left_ext = x0 - plate_w / 2
    if marks and not blank:
        nn = len(stack)
        seq = [abs(s) for s in stack] + [nn + 1]
        for i in range(nn):
            a, b = seq[i], seq[i + 1]
            if abs(a - b) != 1:
                wl = widths[i]
                wb = widths[i + 1] if i + 1 < nn else plate_w
                half = max(wl, wb) / 2 + 0.3
                gy = gap_mid[i]
                c.append(rf"\draw[breakmark] ({fmt(x0-half)},{fmt(gy)}) -- ({fmt(x0+half)},{fmt(gy)});")
                right = max(right, x0 + half)
                left_ext = min(left_ext, x0 - half)
    if plate_label is not None:
        c.append(rf"\node[anchor=east, inner sep=1pt, font=\small] at ({fmt(left_ext-0.12)},{fmt(-ph/2)}) {{{plate_label}}};")
    bottom = -ph
    if code:
        c.append(rf"\node[anchor=north, font=\normalsize, inner sep=0pt] at ({fmt(x0)},{fmt(-ph-0.18)}) {{{code}}};")
        bottom = -ph - 0.18 - 0.45
    return c, top, bottom, right


def code_of(stack):
    return r"\,\,".join(str(abs(s)) for s in stack)


def item(stack, sc, *, width, height, burnt=False, record=None, code=True,
         blank=0, blank_w=1.8, blank_h=None, numsize=r"\small", box=0.95):
    """One stack in a fixed-size box, with a record area under it.

    height: space reserved above the plate (so a row lines up on its plates).
    record: None, 'box' (K-1 flip count) or 'line' ('flips:' and a line).
    """
    sep = BSEP if burnt else (SSEP if blank else 0.0)
    cmds, top, bottom, right = stack_cmds(
        0, stack, sc, burnt=burnt, code=(code_of(stack) if (code and not blank) else None),
        blank=blank, blank_w=blank_w, blank_h=blank_h, numsize=numsize, sep=sep)
    y = bottom - 0.25 if bottom < -0.3 else -PH * sc - 0.35
    if record == 'box':
        s = box
        cmds.append(rf"\node[anchor=east, font=\normalsize] at ({fmt(-s/2-0.12)},{fmt(y-s/2)}) {{flips}};")
        cmds.append(rf"\draw[thick, rounded corners=2pt] ({fmt(-s/2)},{fmt(y-s)}) rectangle ({fmt(s/2)},{fmt(y)});")
        y -= s
    elif record == 'line':
        y -= 0.5
        cmds.append(rf"\node[anchor=base west, font=\normalsize, inner sep=0pt] (fl) at ({fmt(-width/2+0.1)},{fmt(y)}) {{flips:}};")
        cmds.append(rf"\draw[thin] ([xshift=3pt]fl.base east) -- ({fmt(width/2-0.1)},{fmt(y)});")
        y -= 0.3
    bb = rf"\useasboundingbox ({fmt(-width/2)},{fmt(y-0.05)}) rectangle ({fmt(width/2)},{fmt(height)});"
    return "\\begin{tikzpicture}\n" + bb + "\n" + "\n".join(cmds) + "\n\\end{tikzpicture}"


def row(items):
    return r"\noindent\makebox[\linewidth][s]{" + r"\hfill".join([""] + items + [""]) + "}\n"


def stack_height(n, sc, blank_h=None, sep=0.0):
    return n * (blank_h or H) * sc + (n - 1) * sep + 0.05


def flip_demo(seq, sc, *, labels, tokens, numsize, burnt=False, step=5.6):
    """A worked sequence of flips: seq is a list of (stack, spatula or None)."""
    cmds = []
    x = 0.0
    step = step * sc
    sep = BSEP if burnt else 0.0
    wmax = max(pw(abs(v), sc) for v in seq[0][0])
    for i, (st, sp) in enumerate(seq):
        cc, top, bottom, right = stack_cmds(x, st, sc, spatula=sp, burnt=burnt,
                                            code=(code_of(st) if (labels and not burnt) else None),
                                            numsize=numsize, sep=sep)
        cmds += cc
        if i < len(seq) - 1:
            ax0 = x + wmax / 2 + 1.55 * sc
            ax1 = x + step - wmax / 2 - 0.3 * sc
            ay = 0.75 * sc
            cmds.append(rf"\draw[-{{Stealth[length=7pt]}}, thick] ({fmt(ax0)},{fmt(ay)}) -- ({fmt(ax1)},{fmt(ay)});")
            if labels:
                cmds.append(rf"\node[above, font=\normalsize] at ({fmt((ax0+ax1)/2)},{fmt(ay+0.05)}) {{flip {sp}}};")
            if tokens:
                cmds.append(rf"\draw[tokdraw, tokfill] ({fmt((ax0+ax1)/2)},{fmt(ay-0.5*sc)}) circle ({fmt(0.22*sc)});")
        x += step
    return "\\begin{tikzpicture}\n" + "\n".join(cmds) + "\n\\end{tikzpicture}"


LAUNCH = [((3, 1, 2), 3), ((2, 1, 3), 2), ((1, 2, 3), None)]
# Worked dark-side flip: a state used in no task, and not a solution step.
BURNT_DEMO = [((2, -1, 3), 2), ((1, -2, 3), None)]


def breaks_demo():
    st = (2, 1, 5, 3, 4)
    cc, top, bottom, right = stack_cmds(0, st, 1.0, code=code_of(st), marks=True,
                                        plate_label="6", sep=0.16, plate_gap=0.16)
    cc.append(rf"\node[anchor=north, font=\normalsize] at (0,{fmt(bottom-0.05)}) {{3 breaks}};")
    return "\\begin{tikzpicture}\n" + "\n".join(cc) + "\n\\end{tikzpicture}"


def centred(tikz):
    return r"\par\smallskip\begin{center}" + tikz + r"\end{center}"


# ---------------------------------------------------------------- document

PREAMBLE = r"""\documentclass[%(size)s]{%(cls)s}
\usepackage[letterpaper, left=0.75in, right=0.75in, top=0.85in, bottom=0.85in, headsep=0.25in, footskip=0.4in]{geometry}
\usepackage[T1]{fontenc}
\usepackage[scaled=0.95]{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\lhead{\small Week %(week)s / Pancake flips / Grades %(band)s}
\lfoot{\small Bellingham Math Circle / Week %(week)s / %(pid)s}
\rfoot{\small \thepage}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\definecolor{cakefillc}{RGB}{248,224,170}
\definecolor{cakedrawc}{RGB}{140,95,35}
\definecolor{burntc}{RGB}{85,50,20}
\tikzset{
  cakefill/.style={fill=cakefillc},
  cakedraw/.style={draw=cakedrawc, line width=0.9pt},
  burnt/.style={fill=burntc},
  platedraw/.style={draw=black!55, line width=0.6pt},
  platefill/.style={fill=black!18},
  slot/.style={draw=black!70, dashed, line width=0.8pt},
  spatula/.style={fill=black!65},
  handle/.style={fill=black!40},
  tokdraw/.style={draw=black!70, line width=0.8pt},
  tokfill/.style={fill=black!12},
  breakmark/.style={draw=red!80!black, line width=1.8pt, line cap=round},
}
\newcommand{\problem}[1]{\par\medskip\textbf{Problem #1:}\ }
\begin{document}
"""


def doc(band, pid, cls, size, body):
    return (PREAMBLE % dict(band=band, pid=pid, cls=cls, size=size, week=WEEK)
            + body + "\n\\end{document}\n")


D = {n: bfs_unburnt(n) for n in range(2, 7)}
DB = {n: bfs_burnt(n) for n in range(1, 4)}


def need(st, burnt=False):
    return (DB if burnt else D)[len(st)][tuple(st)]


# ---------------------------------------------------------------- K-1

def k1():
    ns = r"\Large"
    b = []
    b.append(r"A stack is sorted when it goes from the smallest pancake on top to the biggest at the bottom. "
             r"To flip, slide the spatula under a pancake and turn over everything above the spatula, all together. "
             r"Put down a token for each flip.")
    b.append(centred(flip_demo(LAUNCH, 1.3, labels=False, tokens=True, numsize=r"\normalsize")))

    # Problem 1: all six stacks of three
    b.append(r"\problem{1}Find all six ways to stack pancakes 1, 2 and 3, and sort each one with as few flips as you can. "
             r"Circle the stack that needs the most flips.")
    b.append(r"\par\medskip")
    sh, sw = 1.4, 2.2
    hh = stack_height(3, 1.0, blank_h=sh, sep=SSEP)
    blanks = [item(None, 1.0, width=5.4, height=hh, record='box', box=1.3,
                   blank=3, blank_w=sw, blank_h=sh) for _ in range(3)]
    b.append(row(blanks))
    b.append(r"\par\vspace{0.9cm}")
    b.append(row(blanks))

    b.append(r"\newpage")
    # Problem 2: given stacks of four
    p2 = [(4, 1, 2, 3), (2, 3, 4, 1), (3, 4, 2, 1), (1, 2, 4, 3)]
    b.append(r"\problem{2}Build each stack of four and sort it with as few flips as you can.")
    b.append(r"\par\bigskip")
    hh = stack_height(4, 1.4)
    b.append(row([item(s, 1.4, width=4.3, height=hh, record='box', box=1.3, code=False, numsize=r"\large") for s in p2]))

    # Problem 3: the three one-flip stacks
    b.append(r"\par\vspace{1.4cm}")
    b.append(r"\problem{3}Find every mixed-up stack of pancakes 1, 2, 3 and 4 that you can sort with one flip.")
    b.append(r"\par\bigskip")
    hh = stack_height(4, 1.0, blank_h=sh, sep=SSEP)
    b.append(row([item(None, 1.0, width=5.4, height=hh, blank=4, blank_w=sw, blank_h=sh) for _ in range(3)]))

    b.append(r"\newpage")
    # Problem 4: the three worst stacks of four and one 3-flip decoy
    p4 = [(4, 2, 3, 1), (2, 1, 4, 3), (2, 4, 1, 3), (3, 1, 4, 2)]
    b.append(r"\problem{4}Build each stack and sort it with as few flips as you can.")
    b.append(r"\par\bigskip")
    hh = stack_height(4, 1.6)
    b.append(row([item(s, 1.6, width=4.35, height=hh, record='box', box=1.3, code=False, numsize=r"\Large") for s in p4]))

    b.append(r"\newpage")
    # Problem 5: dark sides, with a worked flip
    p5 = [(-1, 2), (-2, -1), (-2, 1), (2, 1)]
    b.append(r"\problem{5}Each pancake has a dark side. "
             r"Sort each stack so every dark side ends facing down, with as few flips as you can.")
    b.append(centred(flip_demo(BURNT_DEMO, 1.15, labels=False, tokens=True, numsize=r"\normalsize", burnt=True)))
    b.append(r"\par\vspace{0.6cm}")
    hh = stack_height(2, 1.6, sep=BSEP)
    b.append(row([item(s, 1.6, width=4.35, height=hh, burnt=True, record='box', box=1.3, code=False, numsize=r"\large") for s in p5]))

    b.append(r"\par\vspace{1.4cm}")
    # Problem 6: the hardest stack of two with dark sides
    b.append(r"\problem{6}Find the stack of pancakes 1 and 2 that needs the most flips. "
             r"Draw it with its dark sides.")
    b.append(r"\par\bigskip")
    hh = stack_height(2, 1.0, blank_h=sh, sep=SSEP)
    b.append(row([item(None, 1.0, width=5.4, height=hh, record='box', box=1.3,
                       blank=2, blank_w=2.8, blank_h=sh) for _ in range(3)]))
    return b, dict(p2=p2, p4=p4, p5=p5)


# ---------------------------------------------------------------- shared rules (2-3, 4-5)

RULES = (r"A stack is sorted when each pancake sits on a bigger one. "
         r"To flip, slide the spatula under any pancake and turn that pancake and everything above it over together. "
         r"Write a stack as its numbers from the top, and a flip as the number of pancakes it turns over.")


def rules_block():
    return [RULES, centred(flip_demo(LAUNCH, 1.0, labels=True, tokens=False, numsize=r"\small"))]


def burnt_intro():
    return [r"Now each pancake has a dark side, which must end facing down. "
            r"Sort each stack with as few flips as you can.",
            centred(flip_demo(BURNT_DEMO, 1.1, labels=True, tokens=False, numsize=r"\normalsize", burnt=True))]


# ---------------------------------------------------------------- 2-3

def g23():
    sc = 1.0
    b = rules_block()
    p1 = [(2, 3, 4, 1), (3, 4, 1, 2), (5, 4, 3, 2, 1), (5, 1, 2, 3, 4), (4, 5, 1, 2, 3), (1, 2, 3, 5, 4)]
    b.append(r"\problem{1}Sort each stack with as few flips as you can. Write down your flips.")
    b.append(r"\par\medskip")
    hh = stack_height(5, sc)
    b.append(row([item(s, sc, width=5.2, height=hh, record='line') for s in p1[:3]]))
    b.append(r"\par\vspace{0.6cm}")
    b.append(row([item(s, sc, width=5.2, height=hh, record='line') for s in p1[3:]]))

    b.append(r"\newpage")
    b.append(r"\problem{2}Which stack of pancakes 1, 2 and 3 needs the most flips? "
             r"Explain why it cannot be sorted in fewer.")
    b.append(r"\par\vspace{6.8cm}")
    p3 = [(6, 5, 4, 3, 2, 1), (3, 6, 1, 5, 2, 4), (1, 2, 3, 4, 6, 5), (5, 2, 6, 3, 1, 4)]
    b.append(r"\problem{3}Sort each stack of six with as few flips as you can.")
    b.append(r"\par\medskip")
    hh = stack_height(6, sc)
    b.append(row([item(s, sc, width=7.6, height=hh, record='line') for s in p3[:2]]))
    b.append(r"\par\vspace{0.7cm}")
    b.append(row([item(s, sc, width=7.6, height=hh, record='line') for s in p3[2:]]))

    b.append(r"\newpage")
    b.append(r"\problem{4}Find a way to sort any stack of six pancakes, however mixed up it is. "
             r"What is the most flips your way can need? "
             r"What about a stack of ten pancakes?")

    b.append(r"\newpage")
    b.append(r"\problem{5}Find all the stacks of pancakes 1, 2, 3 and 4 that cannot be sorted in three flips or fewer.")

    b.append(r"\newpage")
    p6 = [(-1, 2), (-2, -1), (-2, 1), (2, 1)]
    intro = burnt_intro()
    b.append(r"\problem{6}" + intro[0])
    b.append(intro[1])
    b.append(r"\par\medskip")
    s6 = 1.25
    hh = stack_height(2, s6, sep=BSEP)
    b.append(row([item(s, s6, width=4.2, height=hh, burnt=True, record='line', code=False, numsize=r"\normalsize") for s in p6]))

    b.append(r"\par\vspace{1.2cm}")
    b.append(r"\problem{7}Find the stack of pancakes 1 and 2 that needs the most flips. "
             r"Draw it with its dark sides.")
    b.append(r"\par\bigskip")
    hh = stack_height(2, 1.0, blank_h=0.75, sep=SSEP)
    b.append(row([item(None, 1.0, width=5.2, height=hh, record='line', blank=2, blank_w=2.4, blank_h=0.75)
                  for _ in range(3)]))

    b.append(r"\newpage")
    p8 = [(-3, 1, 2), (3, 1, 2), (3, 2, 1), (-1, -2, -3)]
    b.append(r"\problem{8}Sort each stack of three so that every dark side ends facing down, "
             r"with as few flips as you can.")
    b.append(r"\par\medskip")
    s8 = 1.5
    hh = stack_height(3, s8, sep=BSEP)
    b.append(row([item(s, s8, width=7.0, height=hh, burnt=True, record='line', code=False, numsize=r"\large") for s in p8[:2]]))
    b.append(r"\par\vspace{1.2cm}")
    b.append(row([item(s, s8, width=7.0, height=hh, burnt=True, record='line', code=False, numsize=r"\large") for s in p8[2:]]))
    return b, dict(p1=p1, p3=p3, p6=p6, p8=p8)


# ---------------------------------------------------------------- 4-5

def g45():
    sc = 1.0
    b = rules_block()
    p1 = [(5, 1, 2, 3, 4), (4, 5, 1, 2, 3), (1, 2, 3, 5, 4), (3, 2, 1, 5, 4), (2, 1, 4, 3, 6, 5)]
    b.append(r"\problem{1}Sort each stack with as few flips as you can. Write down your flips.")
    b.append(r"\par\medskip")
    hh = stack_height(6, sc)
    b.append(row([item(s, sc, width=5.2, height=hh, record='line') for s in p1[:3]]))
    b.append(r"\par\vspace{0.5cm}")
    b.append(row([item(s, sc, width=5.2, height=hh, record='line') for s in p1[3:]]))

    b.append(r"\newpage")
    b.append(r"\problem{2}Find a way to sort any stack of six pancakes, however mixed up it is. "
             r"What is the most flips your way can need? Explain why it never needs more. "
             r"How many flips can your way need for a stack of 20 pancakes?")

    b.append(r"\newpage")
    b.append(r"\problem{3}Think of each stack as sitting on a plate, and give the plate the number one bigger than the biggest pancake. "
             r"A break is a place where two touching pancakes, or the bottom pancake and the plate, "
             r"have numbers that differ by more than 1, such as 1 on 5, or 4 on plate 6 in the stack below.")
    b.append(centred(breaks_demo()))
    p3 = (3, 5, 2, 1, 4)
    b.append(r"Sort 3 5 2 1 4 with as few flips as you can. It has four breaks. "
             r"Explain why a stack with four breaks can never be sorted in fewer than four flips.")
    b.append(r"\par\medskip")
    hh = stack_height(5, sc)
    b.append(row([item(p3, sc, width=7.0, height=hh, record='line')]))

    b.append(r"\newpage")
    b.append(r"\problem{4}Find every stack of pancakes 1, 2, 3 and 4 that cannot be sorted in three flips or fewer. "
             r"How do you know that each one cannot be sorted in three, and that you have found them all?")

    b.append(r"\newpage")
    b.append(r"\problem{5}Find a stack of five pancakes that needs the most flips. "
             r"Explain why it cannot be sorted in fewer.")
    b.append(r"\par\vspace{9.5cm}")
    b.append(r"\problem{6}Stack 4 6 2 5 1 3 has six breaks. Can it be sorted in six flips? "
             r"If it can, show how. If it cannot, explain why.")

    b.append(r"\newpage")
    p7 = [(-3, 1, 2), (1, 2, -3), (3, 1, 2), (-1, -2, 3), (3, 2, 1)]
    intro = burnt_intro()
    b.append(r"\problem{7}" + intro[0])
    b.append(intro[1])
    b.append(r"\par\medskip")
    s7 = 1.15
    hh = stack_height(3, s7, sep=BSEP)
    b.append(row([item(s, s7, width=5.4, height=hh, burnt=True, record='line', code=False, numsize=r"\normalsize") for s in p7[:3]]))
    b.append(r"\par\vspace{0.5cm}")
    b.append(row([item(s, s7, width=5.4, height=hh, burnt=True, record='line', code=False, numsize=r"\normalsize") for s in p7[3:]]))
    b.append(r"\par\vspace{1.0cm}")
    b.append(r"\problem{8}Find a stack of three pancakes with dark sides that needs the most flips. "
             r"Draw it with its dark sides.")
    b.append(r"\par\bigskip")
    hh = stack_height(3, 1.0, blank_h=0.7, sep=SSEP)
    b.append(row([item(None, 1.0, width=5.2, height=hh, record='line', blank=3, blank_w=2.6, blank_h=0.7)
                  for _ in range(3)]))

    b.append(r"\newpage")
    b.append(r"\problem{9}Find a way to sort any stack of pancakes with dark sides. "
             r"What is the most flips your way can need for a stack of six?")
    return b, dict(p1=p1, p3=[p3], p7=p7)


# ---------------------------------------------------------------- build

def build(name, band, pid, cls, size, body):
    tex = doc(band, pid, cls, size, "\n".join(body))
    path = os.path.join(HERE, name + ".tex")
    with open(path, "w") as f:
        f.write(tex)
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", name + ".tex"],
                           cwd=HERE, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            raise SystemExit(f"pdflatex failed for {name}")
    os.replace(os.path.join(HERE, name + ".pdf"), os.path.join(OUT, name + ".pdf"))
    log = open(os.path.join(HERE, name + ".log")).read()
    if "Overfull" in log:
        print(f"WARNING: overfull boxes in {name}")
        for line in log.splitlines():
            if "Overfull" in line:
                print("   ", line)
    for ext in (".aux", ".log"):
        p = os.path.join(HERE, name + ext)
        if os.path.exists(p):
            os.remove(p)


def report(label, stacks, burnt=False):
    print(label, [(code_of(s).replace(r"\,\,", " "), need(s, burnt)) for s in stacks])


if __name__ == "__main__":
    kb, kd = k1()
    build("k-1", "K--1", f"{WEEK}-K-v1", "extarticle", "14pt", kb)
    tb, td = g23()
    build("grades-2-3", "2--3", f"{WEEK}-23-v1", "article", "12pt", tb)
    fb, fd = g45()
    build("grades-4-5", "4--5", f"{WEEK}-45-v1", "article", "12pt", fb)
    print("K-1:"); [report(k, v, k == 'p5') for k, v in kd.items()]
    print("2-3:"); [report(k, v, k in ('p6', 'p8')) for k, v in td.items()]
    print("4-5:"); [report(k, v, k == 'p7') for k, v in fd.items()]
    print("burnt demo:", [(s, need(s, True)) for s, _ in BURNT_DEMO])
    print("breaks of 2 1 5 3 4:", breaks((2, 1, 5, 3, 4)), " of 3 5 2 1 4:", breaks((3, 5, 2, 1, 4)),
          "needs", need((3, 5, 2, 1, 4)),
          " of 4 6 2 5 1 3:", breaks((4, 6, 2, 5, 1, 3)), "needs", need((4, 6, 2, 5, 1, 3)))
