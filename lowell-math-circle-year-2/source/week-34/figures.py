"""Week 34 figures and canvas page template, carried over unchanged from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py).

Coordinates are centimetres, y down from the top-left of the content area: each page is a
TikZ overlay on the whole sheet, shifted to (1.5 cm, 1.5 cm), that draws its own header,
footer and page number. Every drawing primitive below returns one TikZ line preceded by a
newline, which is how the old builder joined a page's lines. Prompts and texts are LaTeX,
not escaped, as in the old builder. Problem files call the functions by name in their
`figure` sections; the wording lives in the problem files.
"""
import math


# ---------------------------------------------------------------- page template (build_packets.py's Packet)

def page_preamble(week, topic, header, footer):
    return r'''\RequirePackage{fix-cm}
\documentclass[12pt,letterpaper]{article}
\usepackage[margin=.5in]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,patterns}
\pdfmapfile{+cm.map}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\begin{document}
'''


def _text(x, y, w, t, s=15):
    return r'\node[anchor=north west,inner sep=0,align=left,text width=' + str(w) + r'cm,font=\sffamily\fontsize{' + str(s) + '}{' + str(s*1.25) + r'}\selectfont] at (' + str(x) + ',' + str(y) + ') {' + t + '};'


def page_open(page):
    lines = [r'\null\begin{tikzpicture}[remember picture,overlay]', r'\begin{scope}[shift={(current page.north west)},x=1cm,y=-1cm]', r'\begin{scope}[shift={(1.5,1.5)}]']
    lines.append(_text(0, -.5, 18.5, 'Week ' + str(page.week) + ' / ' + page.topic + ' / ' + page.header, 11))
    lines.append(_text(0, 24.7, 17, 'Bellingham Math Circle / Week ' + str(page.week) + ' / ' + page.footer, 10))
    lines.append(_text(18, 24.7, .5, str(page.number), 10))
    return '\n'.join(lines)


def page_close(page):
    return r'\end{scope}\end{scope}\end{tikzpicture}' + '\n'


def page_prompt(n, body, x, y, size):
    return '\n' + _text(0, .5 if y is None else y, 18.4, r'\textbf{Problem ' + str(n) + ':} ' + body, size)


def page_text(x, y, body, w, size):
    return '\n' + _text(x, y, w, body, size)


# ---------------------------------------------------------------- drawing primitives

def symbol(x, y, v, s=.25):  # counter kinds: 0 filled circle, 1 hollow circle, 2 square
    if v == 0: return '\n' + f'\\fill ({x},{y}) circle ({s});'
    if v == 1: return '\n' + f'\\draw[line width=1pt] ({x},{y}) circle ({s});'
    if v == 2: return '\n' + f'\\draw[line width=1pt] ({x-s},{y-s}) rectangle ({x+s},{y+s});'
    return ''


def ring(x, y, n, R=7, spot=1.4, vals=None):  # a ring of n spots on a gray circle; vals puts counters on them
    # Blank unlabelled positions have no printed home tick.
    s = '\n' + f'\\draw[gray!45,line width=.5pt] ({x},{y}) circle ({R});'
    for i in range(n):
        a = 2*math.pi*i/n - math.pi/2; xx = x + R*math.cos(a); yy = y + R*math.sin(a)
        s += '\n' + f'\\draw[line width=1pt,fill=white] ({xx:.5f},{yy:.5f}) circle ({spot});'
        if vals is not None: s += symbol(xx, yy, vals[i], spot*.45)
    return s


def line(y):  # a gray answer line across the page
    return '\n' + f'\\draw[gray!40] (0,{y}) -- (18.3,{y});'


# ---------------------------------------------------------------- pictures

def caption(x, y, body, w=4.4, size=12):  # a centred caption under a picture
    return '\n' + r'\node[anchor=north,inner sep=0,align=center,text width=' + str(w) + r'cm,font=\sffamily\fontsize{' + str(size) + '}{' + str(size*1.25) + r'}\selectfont] at (' + str(x) + ',' + str(y) + ') {' + body + '};'


def demo(start, turn1, turn2, flip):  # the rules' example on an alternating four-ring: each move starts from the same original; captions from the problem file
    y = 4.9
    s = ''
    for x, v, label in [(1.9, [0, 1, 0, 1], start), (6.7, [1, 0, 1, 0], turn1), (11.5, [0, 1, 0, 1], turn2), (16.3, [0, 1, 0, 1], flip)]:
        s += ring(x, y, 4, 1, .37, v) + caption(x, 6.45, label)
    s += '\n' + f'\\draw[dashed,line width=.8pt] (16.3,{y-1.75}) -- (16.3,{y+1.75});'   # the flip's axis, through the top and bottom spots
    s += '\n' + f'\\draw[-{{Stealth}},line width=1pt] (3.45,{y}) -- (5.15,{y});'
    for x1, c in [(10.78, 2.6), (15.58, 2.2)]:   # the other two moves also start from the original, over the rings between
        s += '\n' + f'\\draw[-{{Stealth}},line width=1pt] (2.62,3.64) .. controls (4.5,{c}) and ({x1-1.9},{c}) .. ({x1},3.64);'
    return s
