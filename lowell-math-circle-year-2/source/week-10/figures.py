"""Figures for the Week 10 problem files (Bridges and one-stroke drawings).

A problem file's `## figure` section is a Python expression evaluated here; it
returns the LaTeX for that problem's figures. The drawing code is the old student
builders' (src/build_k1.py, build_23.py, build_45.py and common.py, archived in
archive-before-problem-files-2026-10-23/), carried over unchanged: the towns,
pictures and maps come from src/towns.py, designs.py, pictures.py and
koenigsberg.py, and src/layout.py places them in rows.

`figs(group, group, ...)` lays out a problem's figure groups as the old
Packet.problem did: the first group sits in the minipage that week.toml's prompt
opens, so a statement and its first figures stay on one page, and later groups
may move to the next page. Each group is a list of rows of items.

Towns and pictures are recorded by problem number in T and PICS as they are
drawn, as the old builders did, so that src/check.py can check them
(src/problem_figures.py evaluates each band's figures).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
from towns import triangle, diamond, bowtie, house, ladder, triforce, claw, k4, flower  # noqa: E402,F401
from designs import (rotate, triple, row_doubles, double_then_single, square_double_side,  # noqa: E402,F401
                     ladder_double_rung, lollipop, theta_square, square_x, square_adjacent_tails,
                     square_opposite_tails, reading_letters, fan, m_ladder, double_triangle,
                     square_center3, h_shape, grid_diag, lee_big)
from pictures import (house_nikolaus, closed_envelope, triforce_pic, square_diamond, wheel,  # noqa: E402,F401
                      circle_diameter, window, star_pentagon, olympic, cube, grid33)
from layout import TownItem, PicPair, BoxItem, LinesItem, RawItem, figure  # noqa: E402,F401
import koenigsberg  # noqa: E402

T = {}      # towns by problem number, as drawn
PICS = {}   # one-stroke pictures by problem number, as drawn


def k1_town(key, t, **kw):
    """A K-1 town: no island letters (build_k1.town)."""
    T.setdefault(key, []).append(t)
    return TownItem(t, labels=False, **kw)


def k1_pair(key, p, size):
    """A K-1 picture with a copy to trace (build_k1.pair)."""
    PICS.setdefault(key, []).append(p)
    sc = size / max(p.w, p.h)
    return PicPair(p, sc, gap=3.0)


def town(key, t, letters=True, line=9.0, nlines=1, **kw):
    """A grades 2-3 or 4-5 town with island letters and a writing line (build_23.town, build_45.town)."""
    if letters:
        reading_letters(t)
    T.setdefault(key, []).append(t)
    if line:
        kw.setdefault('below', 'line')
        kw['line_len'] = line
        kw['nlines'] = nlines
    return TownItem(t, labels=True, **kw)


def pair(key, p, size, nlines=2):
    """A grades 2-3 or 4-5 picture with a copy and writing lines (build_23.pair, build_45.pair)."""
    PICS.setdefault(key, []).append(p)
    sc = size / max(p.w, p.h)
    w = 2 * p.w * sc + 1.2
    return PicPair(p, sc, gap=1.2, nlines=nlines, line_len=max(w, 8.4))


def koenigsberg_map(key):
    """The Konigsberg map, recorded as a town for the checker (build_45, Problem 5)."""
    T[key] = [koenigsberg.as_town()]
    return RawItem(koenigsberg.tikz(), koenigsberg.MAP_W, koenigsberg.MAP_H)


def figs(*groups, gap=5, between=7, **kw):
    """The figure groups of one problem, laid out as common.Packet.problem did."""
    codes = [figure(g, **kw)[0] for g in groups]
    out = f"\\vspace{{{gap}mm}}\\noindent {codes[0]}\n\\end{{minipage}}\n"
    for c in codes[1:]:
        out += f"\n\n\\par\\vspace{{{between}mm}}\\noindent {c}\n"
    return out + "\n\n\\par\\vspace{9mm}"
