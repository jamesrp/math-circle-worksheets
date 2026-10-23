"""Week 32 figures and canvas page template, carried over unchanged from the old builder
(archive-before-problem-files-2026-10-23/draw.py and make_packets.py).

Coordinates are centimetres, y down from the top-left of the content area: each page is
a TikZ overlay on the whole sheet that draws its own header, footer and page number, then
shifts to the content area at (1.4 cm, 1.65 cm). Every drawing primitive below returns
one TikZ line preceded by a newline, which is how the old builder joined a page's lines.
Problem files call the functions by name in their `figure` sections; the wording lives in
the problem files.
"""
import math


def esc(s):
    return s.replace('&',r'\&').replace('%',r'\%').replace('#',r'\#').replace('–','--').replace('×',r'$\times$').replace('≥',r'$\geq$').replace('→',r'$\to$')


# ---------------------------------------------------------------- page template (draw.py's build)

def page_preamble(week, topic, header, footer):
    return r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=.5in]{geometry}
\usepackage{tikz}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\pagestyle{empty}
\pdfmapfile{+cm.map}
\pdfmapfile{+ps2pk35.map}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
'''


def page_open(page):
    s = r'\null\begin{tikzpicture}[remember picture,overlay,x=1cm,y=1cm]' + '\n'
    s += r'\begin{scope}[shift={(current page.north west)}]' + '\n'
    s += r'\node[anchor=north west,inner sep=0pt,font=\fontsize{11.5}{13}\selectfont] at (1.4,-.72) {Week ' + str(page.week) + ' / ' + page.topic + ' / ' + page.header + '};\n'
    s += r'\node[anchor=south west,inner sep=0pt,font=\fontsize{9}{11}\selectfont] at (1.4,-27.2) {Bellingham Math Circle / Week ' + str(page.week) + ' / ' + page.footer + '};\n'
    s += r'\node[anchor=south east,inner sep=0pt,font=\fontsize{9}{11}\selectfont] at (20.15,-27.2) {' + str(page.number) + '};\n'
    return s + r'\begin{scope}[shift={(1.4,-1.65)}]'


def page_close(page):
    return r'\end{scope}\end{scope}\end{tikzpicture}' + '\n'


def page_prompt(n, body, x, y, size):
    return '\n' + r'\node[anchor=north west,inner sep=0pt,align=left,text width=18.6cm,font=\fontsize{' + str(size) + '}{' + str(size*1.27) + r'}\selectfont] at (0,' + str(-y) + ') {\\textbf{Problem ' + str(n) + ':} ' + esc(body) + '};'


def page_text(x, y, body, w, size):
    w = 18.5 if w is None else w
    size = 14 if size is None else size
    return '\n' + r'\node[anchor=north west,inner sep=0pt,align=left,text width=' + str(w) + r'cm,font=\fontsize{' + str(size) + '}{' + str(size*1.26) + r'}\selectfont' + '] at (' + f'{x},{-y}' + ') {' + esc(body) + '};'


# ---------------------------------------------------------------- drawing primitives (draw.py's Page methods)

def line(x, y, X, Y, style='black,line width=.6pt'):
    return '\n' + r'\draw[' + style + '] (' + f'{x},{-y}' + ') -- (' + f'{X},{-Y}' + ');'


def rect(x, y, w, h, style='black,line width=.65pt'):
    return '\n' + r'\draw[' + style + '] (' + f'{x},{-y}' + ') rectangle (' + f'{x+w},{-y-h}' + ');'


def node(x, y, s, size=12):
    return '\n' + r'\node[font=\fontsize{' + str(size) + '}{' + str(size+2) + r'}\selectfont,inner sep=1pt] at (' + f'{x},{-y}' + ') {' + esc(str(s)) + '};'


def ruled(y, rows=3, gap=1.15):
    return ''.join(line(0, y+j*gap, 18.5, y+j*gap, 'gray!45,line width=.35pt') for j in range(rows))


def gridrect(x, y, w, h, unit=1, lab=True):
    s = rect(x, y, w*unit, h*unit)
    for i in range(1, w): s += line(x+i*unit, y, x+i*unit, y+h*unit, 'gray!50,line width=.3pt')
    for i in range(1, h): s += line(x, y+i*unit, x+w*unit, y+i*unit, 'gray!50,line width=.3pt')
    if lab:
        s += node(x+w*unit/2, y-.35, w)
        s += node(x-.35, y+h*unit/2, h)
    return s


def workgrid(x, y, w, h, unit=1):
    s = ''
    for i in range(w+1): s += line(x+i*unit, y-.15, x+i*unit, y+h*unit+.15, 'gray!40,line width=.3pt')
    for j in range(h+1): s += line(x-.15, y+j*unit, x+w*unit+.15, y+j*unit, 'gray!40,line width=.3pt')
    return s


# ---------------------------------------------------------------- pictures

def worked_strip(first, rest):  # the rules' worked example: 5 by 2, a 2 by 2 square covered, 3 by 2 left; the two captions come from the problem file
    s = gridrect(.5, 2.5, 5, 2, .7)
    s += line(4.4, 3.2, 5.4, 3.2, '->,line width=.8pt')
    s += gridrect(6, 2.5, 5, 2, .7) + rect(6, 2.5, 1.4, 1.4, 'fill=gray!20,line width=1.2pt') + node(6.7, 3.2, 2, 12)
    s += line(10, 3.2, 11, 3.2, '->,line width=.8pt')
    s += gridrect(11.7, 2.5, 3, 2, .7)
    return s + page_text(5.8, 4.5, first, 5, 11) + page_text(11.4, 4.5, rest, 5, 11)


def answer_lines(ys, x0=12, x1=18.5):  # short gray lines to the right of a board
    return ''.join(line(x0, y, x1, y, 'gray!45,line width=.35pt') for y in ys)


def four_three_squares():  # K-1: the four 3 by 3 squares to arrange
    return ''.join(gridrect(1+i*4.1, 3, 3, 3) for i in range(4))


def cut_14_by_8():  # grades 4-5: the 14 by 8 rectangle, its 8 by 8 square shaded, and the 6 by 8 left over
    s = gridrect(.5, 4.5, 14, 8, .62) + rect(.5, 4.5, 8*.62, 8*.62, 'fill=gray!15,line width=1.1pt') + node(2.98, 6.98, '8 by 8', 13)
    return s + line(9.6, 7, 10.7, 7, '->,line width=.8pt') + gridrect(11.5, 4.5, 6, 8, .62)
