"""Week 10, K-1 packet (F10-K-v4)."""

import os
from towns import triangle, diamond, bowtie, house, ladder, triforce, claw, k4, flower
from designs import (rotate, triple, row_doubles, double_then_single, square_double_side, ladder_double_rung,
                     lollipop, theta_square, square_x, square_adjacent_tails, square_opposite_tails)
from pictures import house_nikolaus, closed_envelope, triforce_pic, square_diamond, wheel, circle_diameter
from layout import TownItem, PicPair, BoxItem
from common import preamble, Packet, write, compile_tex, SRC, OUT

T = {}   # towns by problem, for the checker
PICS = {}


def town(key, t, **kw):
    T.setdefault(key, []).append(t)
    return TownItem(t, labels=False, **kw)


def pair(key, p, size):
    PICS.setdefault(key, []).append(p)
    sc = size / max(p.w, p.h)
    return PicPair(p, sc, gap=3.0)


def build():
    P = Packet(preamble('K--1', 'F10-K-v4', '12pt', r'\large'))

    P.text("Put a counter on every bridge, and put your token on an island. "
           "The token moves by crossing bridges. Each time it crosses a bridge, pick up that "
           "bridge's counter. A bridge with no counter cannot be crossed.\n\n\\vspace{6mm}")

    P.problem(r"\prob{1}Pick up every counter in each town. Color the island where you started.",
              [[[town(1, triangle('k1a')), town(1, bowtie('k1b'))]],
               [[town(1, diamond('k1c')), town(1, house('k1d'))]]], align='bottom')
    P.newpage()

    P.problem(r"\prob{2}Color every island where your token can start and still pick up every counter.",
              [[[town(2, ladder('k2a', 3))], [town(2, triforce('k2b'))]]], vgap=1.6)
    P.newpage()

    P.problem(r"\prob{3}Can you pick up every counter? Put a check in the box if you can and an X if you cannot.",
              [[[town(3, claw('k3a'), below='box'), town(3, rotate(triple('k3b'), 90), below='box')]],
               [[town(3, lollipop('k3c'), below='box')]],
               [[town(3, theta_square('k3d'), below='side')]],
               [[town(3, k4('k3e'), below='side')]]], align='bottom')
    P.newpage()

    P.problem(r"\prob{4}Pick up every counter and end on the island where you started. "
              r"Put a check in the box if you can and an X if you cannot.",
              [[[town(4, row_doubles('k4a'), below='side')],
                [town(4, double_then_single('k4b'), below='side')],
                [town(4, square_double_side('k4c'), below='side')]],
               [[town(4, flower('k4d'), below='side')]],
               [[town(4, ladder_double_rung('k4e'), below='side')]]], vgap=1.0)
    P.newpage()

    P.problem(r"\prob{5}Trace each picture with a colored pencil, without lifting the pencil and without "
              r"going over a line twice. Cross out each picture that cannot be done.",
              [[[pair(5, house_nikolaus(), 5.6)], [pair(5, square_diamond(), 5.0)],
                [pair(5, closed_envelope(), 6.0)]],
               [[pair(5, circle_diameter(), 5.0)], [pair(5, wheel(), 5.0)], [pair(5, triforce_pic(), 5.6)]]],
              vgap=1.4)
    P.newpage()

    P.problem(r"\prob{6}Nobody can pick up every counter in these towns. Draw one more bridge in each town "
              r"so that you can.",
              [[[town(6, claw('k6a'))]], [[town(6, square_x('k6b'))]], [[town(6, square_adjacent_tails('k6c'))]]])

    P.problem(r"\prob{7}Join 4 hexagons with craft sticks into one town where your partner can pick up "
              r"every counter. Then make a town of 4 joined hexagons where your partner cannot, and draw "
              r"both towns.",
              [[[BoxItem(9.0, 9.0), BoxItem(9.0, 9.0)]]])
    P.newpage()

    P.problem(r"\prob{8}Put two counters on one bridge and try to pick up every counter. "
              r"Color each bridge where that works.",
              [[[town(8, k4('k8a'))]], [[town(8, square_opposite_tails('k8b'))]], [[town(8, square_x('k8c'))]]])

    write(os.path.join(SRC, 'k-1.tex'), P.tex())
    return compile_tex('k-1', os.path.join(OUT, 'k-1.pdf')), P.heights


if __name__ == '__main__':
    (warn, pages), figs = build()
    print(pages)
    print("figure heights:", figs)
    for w in warn:
        print(w)
