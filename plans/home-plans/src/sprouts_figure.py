#!/usr/bin/env python3
"""Draw the worked example for the Sprouts home plan.

    python3 plans/home-plans/src/sprouts_figure.py

Writes plans/home-plans/2026-11-08-sprouts-example.png (needs matplotlib). Two dots;
move 1 joins them, move 2 loops one dot back to itself, which kills it. Small grey
numbers are lives left; the ring marks a dead dot.
"""
import pathlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = pathlib.Path(__file__).resolve().parent.parent / "2026-11-08-sprouts-example.png"
BLUE, RED, GREY = "#1f5fbf", "#c8322b", "#555555"
A, B = np.array([0.0, 0.0]), np.array([2.0, 0.0])

def quad(p0, c, p1, t):
    return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * c + t ** 2 * p1

def cubic(p0, c1, c2, p1, t):
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * c1 + 3 * (1 - t) * t ** 2 * c2 + t ** 3 * p1

t = np.linspace(0, 1, 200)[:, None]
arc = quad(A, np.array([1.0, 1.1]), B, t)
C = quad(A, np.array([1.0, 1.1]), B, 0.5)
c1, c2 = np.array([-1.0, -1.45]), np.array([0.75, -1.45])
loop = cubic(A, c1, c2, A, t)
D = cubic(A, c1, c2, A, 0.5)

def spot(ax, p, name, lives, dx=0.0, dy=-0.32, dead=False):
    ax.plot(*p, "o", color="black", ms=9, zorder=3)
    if dead:
        ax.add_patch(plt.Circle(p, 0.17, fill=False, lw=1.6, color="black", zorder=3))
    ax.text(p[0] + dx, p[1] + dy, name, ha="center", va="center", fontsize=15, weight="bold")
    ax.text(p[0] + dx + 0.28, p[1] + dy, str(lives), ha="center", va="center",
            fontsize=12, color=GREY)

fig, axes = plt.subplots(1, 3, figsize=(9.6, 2.9))
titles = ["Start: 2 dots, 3 lives each", "Move 1 (blue): join A to B,\nnew dot C on the line",
          "Move 2 (red): loop A to itself,\nnew dot D. A has 3 lines: dead"]
for i, ax in enumerate(axes):
    ax.set_title(titles[i], fontsize=12)
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-1.3, 2.5); ax.set_ylim(-1.45, 0.95)
    if i >= 1:
        ax.plot(arc[:, 0], arc[:, 1], color=BLUE, lw=2.4)
    if i >= 2:
        ax.plot(loop[:, 0], loop[:, 1], color=RED, lw=2.4)
    if i == 0:
        spot(ax, A, "A", 3); spot(ax, B, "B", 3)
    elif i == 1:
        spot(ax, A, "A", 2); spot(ax, B, "B", 2); spot(ax, C, "C", 1, dy=0.3)
    else:
        spot(ax, A, "A", 0, dx=-0.62, dy=0.0, dead=True); spot(ax, B, "B", 2)
        spot(ax, C, "C", 1, dy=0.3); spot(ax, D, "D", 1, dx=0.0, dy=-0.3)
fig.text(0.5, 0.02, "Grey numbers: lives left (3 minus lines leaving the dot). "
         "Ring: a dead dot.", ha="center", fontsize=11, color=GREY)
fig.tight_layout(rect=(0, 0.05, 1, 1))
fig.savefig(OUT, dpi=170)
print("wrote", OUT)
