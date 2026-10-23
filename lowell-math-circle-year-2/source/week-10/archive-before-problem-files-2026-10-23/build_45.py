"""Week 10, grades 4-5 packet (F10-U-v4)."""

import os
from towns import house, bowtie, claw, k4, ladder, flower
from designs import (rotate, reading_letters, lollipop, row_doubles, fan, m_ladder, grid_diag, lee_big)
from pictures import house_nikolaus, window, olympic, cube, grid33, star_pentagon
from layout import TownItem, PicPair, LinesItem, RawItem
from common import preamble, Packet, write, compile_tex, SRC, OUT
import koenigsberg

T = {}
PICS = {}


def town(key, t, letters=True, line=9.0, nlines=1, **kw):
    if letters:
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
    P = Packet(preamble('Grades 4--5', 'F10-U-v4', '12pt'))

    P.text("Put a counter on every bridge of a town before you walk it. A walk goes from island to island "
           "across bridges, and crossing a bridge means picking up its counter. A bridge whose counter is "
           "gone cannot be crossed again. Two islands can be joined by more than one bridge. In every town "
           "you can get from any island to any other.\n\n\\vspace{6mm}")

    P.problem(r"\prob{1}In each town, find a walk that crosses every bridge exactly once, and write its islands "
              r"in order.",
              [[[town(1, house('u1a'), line=7.5), town(1, rotate(lollipop('u1b'), 90), line=7.5)]],
               [[town(1, row_doubles('u1c'))]]], align='bottom')

    P.problem(r"\prob{2}In each town, find every island where a walk that crosses every bridge exactly once can "
              r"start, and where such a walk can end. If a town has no such walk, write ``none''.",
              [[[town(2, fan('u2a', with_cd=False))]], [[town(2, fan('u2b'))]],
               [[town(2, m_ladder('u2c'))]], [[town(2, flower('u2d'))]]])

    P.problem(r"\prob{3}For each town, decide without walking it whether there is a walk that crosses every "
              r"bridge exactly once, and if there is, where it can start and end. If there is none, write "
              r"``none''. Then use counters to check each town that has a walk.",
              [[[town(3, ladder('u3a', 4), line=11.0)]], [[town(3, bowtie('u3b'))]],
               [[town(3, grid_diag('u3c'))]]])

    P.problem(r"\prob{4}Write a rule that tells you, from a picture of a town, whether it has a walk that crosses "
              r"every bridge exactly once, and where such a walk can start and end. Explain why a town that "
              r"breaks your rule cannot have such a walk.",
              [[[LinesItem(19.0, 6)]]])

    P.newpage()

    P.problem(r"\prob{5}In the city of K\"onigsberg, seven bridges joined four areas of land, A, B, C and D. Can "
              r"someone walk through the city crossing every bridge exactly once? Explain. Where could the city "
              r"build one new bridge so that such a walk becomes possible? What is the smallest number of new "
              r"bridges the city needs for a walk that crosses every bridge exactly once and ends where it "
              r"started?",
              [[[RawItem(koenigsberg.tikz(), koenigsberg.MAP_W, koenigsberg.MAP_H)]],
               [[LinesItem(19.0, 6)]]])
    T[5] = [koenigsberg.as_town()]

    P.problem(r"\prob{6}Can a town have exactly one island with an odd number of bridges? Can it have exactly "
              r"three? Explain.",
              [[[LinesItem(19.0, 6)]]])


    P.problem(r"\prob{7}Trace each picture with a colored pencil, without lifting the pencil and without going "
              r"over a line twice, or explain why it cannot be done. For each picture that cannot be traced "
              r"this way, find the fewest strokes that draw it without going over a line twice, using a new "
              r"color for each stroke.",
              [[[pair(7, house_nikolaus(), 3.9), pair(7, window(), 3.6)]],
               [[pair(7, cube(), 3.8), pair(7, grid33(), 3.6)]],
               [[pair(7, olympic(), 7.2)]],
               [[pair(7, star_pentagon(), 3.8)]]], align='bottom')

    P.problem(r"\prob{8}Lee walked around the outside of this town: \mbox{A B C D E F G H I A}. Find a walk from "
              r"A back to A that crosses every bridge exactly once, and in which Lee's nine bridges still come "
              r"in the order Lee crossed them.",
              [[[town(8, lee_big('u8a'), letters=False, line=None)], [LinesItem(19.0, 3)]]], vgap=0.9)

    P.problem(r"\prob{9}Explain why a town in which every island has an even number of bridges always has a walk "
              r"that crosses every bridge exactly once and ends where it started. Then explain why a town with "
              r"exactly two islands that have an odd number of bridges always has a walk that crosses every "
              r"bridge exactly once.",
              [[[LinesItem(19.0, 7)]]])
    P.newpage()

    P.problem(r"\prob{10}A truck must cross every bridge of a town at least once. Before it starts, you may put "
              r"extra counters on bridges, and a bridge with two counters is crossed two times. For each town, "
              r"find the fewest extra counters for a route that ends where it started, and the fewest for a "
              r"route that may end anywhere.",
              [[[town(10, k4('u10a'))], [town(10, claw('u10b'))]], [[town(10, m_ladder('u10c'))]]], vgap=0.6)

    P.problem(r"\prob{11}In the first town of Problem 10, explain why no route that ends where it started can "
              r"use fewer extra counters than your answer.",
              [[[LinesItem(19.0, 6)]]])

    write(os.path.join(SRC, 'grades-4-5.tex'), P.tex())
    return compile_tex('grades-4-5', os.path.join(OUT, 'grades-4-5.pdf')), P.heights


if __name__ == '__main__':
    (warn, pages), figs = build()
    print(pages)
    print("figure heights:", figs)
    for w in warn:
        print(w)
