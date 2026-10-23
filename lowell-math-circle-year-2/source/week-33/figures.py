"""Week 33 figures and canvas page template, carried over unchanged from the old builder
(archive-before-problem-files-2026-10-23/draw.py and make_packets.py). Added later:
six_boards() (October 23, 2026), Problem 1's six boards in place of four_boards().

Coordinates are centimetres, y down from the top-left of the content area: each page is
a TikZ overlay on the whole sheet that draws its own header, footer and page number, then
shifts to the content area at (1.4 cm, 1.65 cm). Every drawing primitive below returns
one TikZ line preceded by a newline, which is how the old builder joined a page's lines.
Problem files call the functions by name in their `figure` sections; the wording lives in
the problem files.
"""
import math
from itertools import product


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


# ---------------------------------------------------------------- pictures


def ring(x, y, n, word=None, r=2.9, start=0, bead=.38, labels=False):  # a bead ring with its start arrow and clockwise arrow
    s = '\n' + r'\draw[gray!65,line width=.7pt] (' + f'{x},{-y}' + ') circle (' + str(r) + 'cm);'
    for i in range(n):
        a = math.pi/2 - 2*math.pi*i/n
        X = x + r*math.cos(a); Y = y - r*math.sin(a)
        fill = 'white' if word is None or word[i] == 'A' else 'gray!65'
        s += '\n' + r'\draw[fill=' + fill + '] (' + f'{X:.4f},{-Y:.4f}' + ') circle (' + str(bead) + 'cm);'
        if word is not None: s += node(X, Y, word[i], 12 if bead > .25 else 8)
        elif labels: s += node(X, Y, i+1, 10)
    a = math.pi/2 - 2*math.pi*start/n
    X = x + (r+.95)*math.cos(a); Y = y - (r+.95)*math.sin(a)
    XX = x + (r+bead+.12)*math.cos(a); YY = y - (r+bead+.12)*math.sin(a)
    s += line(X, Y, XX, YY, '->,line width=.8pt')
    if start == 0:
        s += node(X, Y - .2, 'start', 9)
    else:  # a moved start: label it just below its own bead, so neighbouring rings' labels stay apart
        s += node(x + r*math.cos(a), y - r*math.sin(a) + bead + .36, 'start', 9)
    # Keep the direction arrow outside bead positions.
    ar = r + bead + .2
    ax = x + ar*math.cos(math.radians(150))
    ay = y - ar*math.sin(math.radians(150))
    return s + '\n' + r'\draw[->,line width=.7pt] (' + f'{ax:.4f},{-ay:.4f}' + ') arc[start angle=150,end angle=110,radius=' + str(ar) + 'cm];'


def start_example(caption):  # the rules' example: AAB read from three starts, with the arrow caption from the problem file
    s = ''
    for x, i, word in [(2.5, 0, 'AAB'), (8.5, 1, 'ABA'), (14.5, 2, 'BAA')]:
        s += ring(x, 4.6, 3, 'AAB', 1.3, i, .29) + node(x, 6.65, word, 15)
    s += line(4.4, 4.6, 6.45, 4.6, '->,line width=.8pt') + line(10.4, 4.6, 12.45, 4.6, '->,line width=.8pt')
    return s + page_text(4.4, 3.1, caption, 3, 10) + page_text(10.4, 3.1, caption, 3, 10)


def mats(n, y):  # two blank n-bead ring boards side by side
    return ring(4.4, y, n, None, 3.65, 0, .42) + ring(14.0, y, n, None, 3.65, 0, .42)


def card(x, y, word, w=8.8, h=3.9, num=None):  # one readout card: beads in a row, start label, reading arrow, card number
    s = rect(x, y, w, h, 'line width=.65pt')
    n = len(word); small = w < 6
    step = .73 if small else 1.5
    radius = .245 if small else .47
    left = x + (w-(n-1)*step)/2
    cy = y + (1.0 if small else 1.7)
    for i, c in enumerate(word):
        X = left + i*step
        s += '\n' + r'\draw[fill=' + ('white' if c == 'A' else 'gray!60') + '] (' + f'{X},{-cy}' + ') circle (' + str(radius) + 'cm);'
        s += node(X, cy, c, 9 if small else 15)
    s += node(left, y+.3, 'start', 7 if small else 10)
    s += line(left-radius, y+h-.45, left+(n-1)*step+radius, y+h-.45, '->,line width=.6pt')
    if num is not None: s += node(x+w-.25, y+.3, num, 7 if small else 9)
    return s


def three_cards():  # all eight three-bead readouts, two to a row
    return ''.join(card((i % 2)*9.5, 2.5+(i//2)*5.1, ''.join(t), num=i+1) for i, t in enumerate(product('AB', repeat=3)))


def five_cards():  # all 32 five-bead readouts, four to a row
    return ''.join(card((i % 4)*4.7, 2.5+(i//4)*2.65, ''.join(t), w=4.4, h=2.3, num=i+1) for i, t in enumerate(product('AB', repeat=5)))


def short_lines(x, y, X, rows=3, gap=1.2):  # gray recording lines beside a board
    return ''.join(line(x, y+j*gap, X, y+j*gap, 'gray!45,line width=.35pt') for j in range(rows))


def four_boards(n):  # four smaller n-bead boards, 2 by 2, each with three recording lines beside it
    s = ''
    for y in (13.4, 20.3):
        s += ring(3.3, y, n, None, 2.3, 0, .42) + short_lines(6.3, y-.9, 9.6)
        s += ring(12.9, y, n, None, 2.3, 0, .42) + short_lines(15.9, y-.9, 18.5)
    return s


def six_boards(n, r=1.75):  # six n-bead boards, 3 rows by 2 columns, each with three recording lines beside it
    s = ''
    for y in (12.35, 17.45, 22.55):
        s += ring(2.7, y, n, None, r, 0, .42) + short_lines(5.3, y-1.15, 9.0, 3, 1.15)
        s += ring(12.0, y, n, None, r, 0, .42) + short_lines(14.6, y-1.15, 18.5, 3, 1.15)
    return s


def six_seven_nine():  # one six-, one seven- and one nine-bead board, each named, with answer lines beside the nine
    s = ring(4.4, 6.6, 6, None, 3.0, 0, .42) + node(4.4, 10.65, '6 beads', 11)
    s += ring(14.0, 6.6, 7, None, 3.0, 0, .42) + node(14.0, 10.65, '7 beads', 11)
    s += ring(5.0, 16.4, 9, None, 3.7, 0, .42) + node(5.0, 21.15, '9 beads', 11)
    return s + short_lines(10.4, 14.0, 18.5, 5)
