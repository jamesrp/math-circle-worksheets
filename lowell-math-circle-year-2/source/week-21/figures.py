"""Week 21 (Shortest reflected paths): boards and page template for the problem files.

Carried over from the old student builder (archive-before-problem-files-2026-10-23/
build_packets.py): each page is a TikZ overlay on the whole sheet, in centimetres from the
bottom-left corner, that draws its own header, footer and page number, with one true-scale
16.8 x 18.2 cm board. The board data below are the old builder's, line for line, and
board(name) returns the LaTeX of its picture(). editable/facilitator-src/check_geometry.py
reads these assignments to check them independently.

The opening rules (problems/00-rules.md) are typeset as the old builder did: in the same
text block as Problem 1, a paragraph and 9 pt above it. page_text() keeps them and
page_prompt() prints them before Problem 1. In a packet without Problem 1 (a return
packet), the rules file is alone on page 1, and page_close() prints them there in the same
place and size.
"""
from math import hypot

W, H = 16.8, 18.2


# The coordinates below are drawing data in centimetres, not student notation.
def horiz(points, marks=None, paths=None):
    return dict(axis='h', line=8.7, points=points, marks=marks or {}, paths=paths or [])


def vert(points):
    return dict(axis='v', line=8.4, points=points, marks={}, paths=[])


equal=horiz({'A':(2.8,13.4),'B':(14,13.4)})
mirror=horiz({'A':(2.4,14.4),'B':(13.5,13.1),'C':(13.5,4.3)})
unequal=horiz({'A':(2.3,12.1),'B':(14.3,15.5)})
compare=horiz({'A':(2.8,12.8),'B':(14,11.7),'C':(10.8,16.4)})
vertical=vert({'A':(3.1,2.5),'B':(5.6,9.2),'C':(2.2,15.9)})
guesses=horiz({'A':(2.2,12.5),'B':(14.4,15.4)},paths=[('A',(3.5,8.7),'B'),('A',(11.5,8.7),'B')])
inverse=horiz({'B':(13.4,14.3)},marks={'P':7.1})
matching=horiz({'A':(2.2,12.3),'B':(14.2,15.9),'C':(3.2,12.7),'D':(12.2,16.7)})
# A--B crosses at 6.2; C--D crosses at 6.2 as well.
restricted=horiz({'A':(2.5,12.7),'B':(14.5,16.7)},marks={'C':4.5,'D':8.2,'E':10.2,'F':14.9})
# The unrestricted contact is x=6.5. C--D and C--F allow it; E--F does not.
lengthtie=horiz({'A':(3,12.7),'B':(13,12.7),'C':(11,14.7)})
unique=horiz({'A':(3.2,15.6),'B':(13.7,11.7)})

BOARDS = dict(equal=equal, mirror=mirror, unequal=unequal, compare=compare, vertical=vertical, guesses=guesses,
              inverse=inverse, matching=matching, restricted=restricted, lengthtie=lengthtie, unique=unique)

# The old builder's text size and leading for each band's text block.
TEXT = {'K--1': (14.5, 18.3), 'Grades 2--3': (13.5, 17.3), 'Grades 4--5': (13, 16.5)}
FILES = {'K--1': 'k-1', 'Grades 2--3': 'grades-2-3', 'Grades 4--5': 'grades-4-5'}
STATE = {'header': 'K--1', 'page': 0, 'rules': None, 'rules_printed': False}
USED = []      # (packet, problem number, board name) for every board drawn, in order


def f(v):
    return f'{v:g}'


def board(name):
    """The true-scale board: the line and its end marks, any drawn routes, dots and marks."""
    USED.append((FILES[STATE['header']], STATE['page'], name))
    return picture(BOARDS[name]) + '\n'


def picture(board):
    code=[r'\begin{scope}[shift={(2.395,3.1)}]',r'\path[use as bounding box] (0,0) rectangle (16.8,18.2);']
    axis,line=board['axis'],board['line']
    if axis=='h':
        code += [rf'\draw[line width=0.75pt] (0.6,{f(line)}) -- (16.2,{f(line)});',
                 rf'\draw[line width=0.75pt] (0.6,{f(line-.14)}) -- (0.6,{f(line+.14)});',
                 rf'\draw[line width=0.75pt] (16.2,{f(line-.14)}) -- (16.2,{f(line+.14)});']
    else:
        code += [rf'\draw[line width=0.75pt] ({f(line)},0.6) -- ({f(line)},17.6);',
                 rf'\draw[line width=0.75pt] ({f(line-.14)},0.6) -- ({f(line+.14)},0.6);',
                 rf'\draw[line width=0.75pt] ({f(line-.14)},17.6) -- ({f(line+.14)},17.6);']
    for i,(a,m,b) in enumerate(board['paths']):
        ax,ay=board['points'][a]; bx,by=board['points'][b]
        style='solid' if i==0 else 'dash pattern=on 4pt off 3pt'
        code.append(rf'\draw[line width=.75pt,{style}] ({f(ax)},{f(ay)}) -- ({f(m[0])},{f(m[1])}) -- ({f(bx)},{f(by)});')
    for label,(x,y) in board['points'].items():
        code.append(rf'\fill ({f(x)},{f(y)}) circle[radius=1.5pt];')
        # The label is kept off all route centers.
        code.append(rf'\node[anchor=south,font=\fontsize{{14}}{{17}}\selectfont,inner sep=0pt] at ({f(x)},{f(y+.20)}) {{{label}}};')
    for label,x in board['marks'].items():
        code.append(rf'\fill ({f(x)},{f(line)}) circle[radius=1.4pt];')
        code.append(rf'\node[anchor=north,font=\fontsize{{13}}{{16}}\selectfont,inner sep=0pt] at ({f(x)},{f(line-.22)}) {{{label}}};')
    code.append(r'\end{scope}')
    return '\n'.join(code)


def contacts():
    """Every same-side pair of dots on every board drawn, as the old builder checked them."""
    checks = []
    for packet, n, name in USED:
        b = BOARDS[name]
        pts = b['points']; axis = b['axis']; line = b['line']; ix = 1 if axis == 'h' else 0
        for label, (x, y) in pts.items():
            assert 0 < x < W and 0 < y < H
            reflected = (x, 2*line-y) if axis == 'h' else (2*line-x, y)
            assert 0 < reflected[0] < W and 0 < reflected[1] < H, (packet, n, label, reflected)
        for a, pa in pts.items():
            for c, pc in pts.items():
                if a >= c or (pa[ix]-line)*(pc[ix]-line) <= 0:
                    continue
                da = abs(pa[ix]-line); dc = abs(pc[ix]-line)
                along = (pa[1-ix]*dc+pc[1-ix]*da)/(da+dc)
                assert .6 < along < (16.2 if axis == 'h' else 17.6)
                checks.append(dict(packet=packet, page=n, pair=a+c, contact=along, minimum_cm=hypot(pa[1-ix]-pc[1-ix], da+dc)))
    return checks


# ---------------------------------------------------------------- page template

PREAMBLE=r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=0pt]{geometry}
\usepackage{tikz}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\begin{document}
'''


def page_preamble(week, topic, header, footer):
    STATE.update(header=header, page=0, rules=None, rules_printed=False)
    USED.clear()
    return PREAMBLE + '\n'


def _block(text):
    size, leading = TEXT[STATE['header']]
    return rf'\node[anchor=north west,inner sep=0pt,text width=18.65cm,align=left,font=\fontsize{{{size}}}{{{leading}}}\selectfont] at (1.45,25.66) {{{text}}};'


def page_open(page):
    return '\n'.join([r'\null', r'\begin{tikzpicture}[remember picture,overlay,x=1cm,y=1cm]', r'\begin{scope}[shift={(current page.south west)}]',
                      rf'\node[anchor=north west,inner sep=0pt,font=\fontsize{{10.4}}{{12}}\selectfont] at (1.45,26.72) {{Week {page.week} / {page.topic} / {page.header}}};']) + '\n'


def page_text(x, y, body, w, size):
    """The opening rules: kept for Problem 1's text block (see the module note)."""
    STATE['rules'] = body
    return ''


def page_prompt(n, body, x, y, size):
    STATE['page'] = n
    problem = rf'\textbf{{Problem {n}:}} {body}'
    if n == 1 and STATE['rules']:
        STATE['rules_printed'] = True
        problem = STATE['rules'] + r'\par\vspace{9pt}' + problem
    return _block(problem) + '\n'


def page_close(page):
    STATE['header'] = page.header
    alone = _block(STATE['rules']) + '\n' if page.number == 1 and STATE['rules'] and not STATE['rules_printed'] else ''
    return (alone
            + rf'\node[anchor=south west,inner sep=0pt,font=\fontsize{{9}}{{11}}\selectfont] at (1.45,1.05) {{Bellingham Math Circle / Week {page.week} / {page.footer}}};' + '\n'
            + rf'\node[anchor=south east,inner sep=0pt,font=\fontsize{{9}}{{11}}\selectfont] at (20.14,1.05) {{{page.number}}};' + '\n'
            + r'\end{scope}' + '\n' + r'\end{tikzpicture}' + '\n')
