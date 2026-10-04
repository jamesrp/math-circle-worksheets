"""Week 10, grades 2-3 packet (F10-M-v4)."""

import os
from towns import house, triforce, claw, k4, flower, ladder
from designs import (rotate, reading_letters, lollipop, row_doubles, fan, m_ladder, double_triangle,
                     square_center3, square_opposite_tails, h_shape)
from pictures import house_nikolaus, window, star_pentagon, closed_envelope, olympic, square_diamond
from layout import TownItem, PicPair, BoxItem, LinesItem
from common import preamble, Packet, write, compile_tex, SRC, OUT

T = {}
PICS = {}

SPECS = ["4 islands and 6 bridges. A walk that picks up every counter can start on any island.",
         "5 islands and 5 bridges. No walk picks up every counter.",
         "6 islands and 8 bridges. A walk that picks up every counter can start only on A or on F.",
         "3 islands and 5 bridges. A walk that picks up every counter can start only on A or on B."]


def town(key, t, line=9.0, nlines=1, **kw):
    reading_letters(t)
    T.setdefault(key, []).append(t)
    if line:
        kw.setdefault('below', 'line')
        kw['line_len'] = line
        kw['nlines'] = nlines
    return TownItem(t, labels=True, **kw)


def pair(key, p, size, nlines=2):
    PICS.setdefault(key, []).append(p)
    sc = size / max(p.w, p.h)
    w = 2 * p.w * sc + 1.2
    return PicPair(p, sc, gap=1.2, nlines=nlines, line_len=max(w, 8.4))


def build():
    P = Packet(preamble('Grades 2--3', 'F10-M-v4', '12pt'))

    P.text("Put a counter on every bridge of a town before you walk it. A walk starts on an island and crosses "
           "bridges one after another. Each time it crosses a bridge, pick up that bridge's counter. A bridge "
           "with no counter cannot be crossed. Two islands can be joined by more than one bridge. In every town "
           "you can get from any island to any other.\n\n\\vspace{6mm}")

    P.problem(r"\prob{1}In each town, find a walk that picks up every counter, and write its islands in order, "
              r"like A~B~C~A.",
              [[[town(1, house('m1a'), line=7.5), town(1, rotate(lollipop('m1b'), 90), line=7.5)]],
               [[town(1, row_doubles('m1c'), line=9.0)]]], align='bottom')

    P.problem(r"\prob{2}In each town, find every island where a walk that picks up every counter can start, "
              r"and where such a walk can end. If a town has no such walk, write ``none''.",
              [[[town(2, fan('m2a', with_cd=False))]], [[town(2, fan('m2b'))]],
               [[town(2, m_ladder('m2c'))]], [[town(2, flower('m2d'))]]])

    P.problem(r"\prob{3}For each town, decide without walking whether a walk can pick up every counter. If it "
              r"can, circle every island where such a walk can start. If it cannot, write ``none''. Then check "
              r"with counters.",
              [[[town(3, triforce('m3a'), line=6.0)]], [[town(3, double_triangle('m3b'), line=6.0)]],
               [[town(3, rotate(k4('m3c'), 90), line=6.0)]], [[town(3, square_center3('m3d'), line=6.0)]]])

    P.problem(r"\prob{4}No walk picks up every counter in these towns. In each town, draw one new bridge so "
              r"that a walk can, and write the walk.",
              [[[town(4, claw('m4a'))]], [[town(4, square_opposite_tails('m4b'), line=11.0)]],
               [[town(4, ladder('m4c', 4), line=11.0)]]])

    P.problem(r"\prob{5}In each town, draw as few new bridges as you can so that a walk can pick up every "
              r"counter and end on the island where it started.",
              [[[town(5, house('m5a'), line=None), town(5, rotate(k4('m5b'), 90), line=None)]],
               [[town(5, rotate(h_shape('m5c'), 90), line=None)]]], align='bottom')

    P.problem(r"\prob{6}How can you tell, without walking, whether a town has a walk that picks up every "
              r"counter, and where such a walk can start and end?",
              [[[LinesItem(19.0, 6)]]])

    P.problem(r"\prob{7}Trace each picture with a colored pencil, without lifting the pencil and without going "
              r"over a line twice. If a picture cannot be traced this way, explain how you know.",
              [[[pair(7, house_nikolaus(), 3.9), pair(7, window(), 3.6)]],
               [[pair(7, star_pentagon(), 3.8), pair(7, closed_envelope(), 4.2)]],
               [[pair(7, olympic(), 7.2)]],
               [[pair(7, square_diamond(), 3.6)]]], align='bottom')

    boxes = [BoxItem(9.0, 8.0, caption=s, caption_h=1.4) for s in SPECS]
    P.problem(r"\prob{8}Build each of these towns with hexagons and craft sticks for your partner to walk. "
              r"Draw each town you build.",
              [[boxes[0:2]], [boxes[2:4]]], vgap=0.9)

    P.problem(r"\prob{9}Can you make a town with at least one bridge where a walk that picks up every counter "
              r"can start on only one island? Make one, or explain why it cannot be done.",
              [[[LinesItem(10.0, 10), BoxItem(8.0, 10.0)]]])

    P.newpage()

    P.problem(r"\prob{10}A bridge can hold two counters, and then a walk can cross it two times. In each town, "
              r"put a second counter on as few bridges as you can so that a walk can pick up every counter and "
              r"end on the island where it started. Color each bridge that gets a second counter.",
              [[[town(10, rotate(k4('m10a'), 90), line=None)]], [[town(10, claw('m10b'), line=None)]]])

    write(os.path.join(SRC, 'grades-2-3.tex'), P.tex())
    return compile_tex('grades-2-3', os.path.join(OUT, 'grades-2-3.pdf')), P.heights


if __name__ == '__main__':
    (warn, pages), figs = build()
    print(pages)
    print("figure heights:", figs)
    for w in warn:
        print(w)
