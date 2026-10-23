"""Week 26 figures and canvas page template, carried over from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py).

Coordinates are millimetres from the top-left corner of the paper, y down: each page
is one overlay picture anchored at the page's north-west corner, as the old builder
drew it. The header, footer and page number are drawn inside that picture. The old
builder wrote the header and footer text into every page; here the preamble defines
them once per band (\\weekheader, \\weekfooter) and the page number is \\thepage, which
equals the problem number in the full packets. The conversion left the printed pages unchanged.

Problem files call the functions below by name in their `figure` sections; the rule
and prompt wording lives in the problem files.

October 23, 2026 card fixes: Grades 2-3 Problem 2 has a third recording box per start,
the third Grades 4-5 Problem 3 shape has a gap in its second row (boundary 20), and
Grades 4-5 Problem 6 labels say tiles.
"""


def node(x,y,text,size=14,width=None,anchor='north west'):
    opt=f'anchor={anchor},inner sep=0pt,outer sep=0pt,align=left'
    if width: opt+=f',text width={width}mm'
    return f'\\node[{opt}] at ({x},{y}) {{\\fontsize{{{size}}}{{{size*1.26:.2f}}}\\selectfont {text}}};\n'

def grid(x,y,c,r,s=8,cells=None):
    z=''
    if cells:
        for a,b in cells:
            z+=f'\\fill[black!13] ({x+a*s},{y+b*s}) rectangle ++({s},{s});\n'
    z+=f'\\draw[step={s}mm,black!27,line width=.3pt] ({x},{y}) grid ({x+c*s},{y+r*s});\n'
    # grid step uses absolute coordinates; replace with scoped local grid
    z=z[:z.rfind('\\draw[step=')]+f'\\begin{{scope}}[shift={{({x},{y})}}]\n\\draw[step={s}mm,black!27,line width=.3pt] (0,0) grid ({c*s},{r*s});\n\\end{{scope}}\n'
    z+=f'\\draw[black!27,line width=.3pt] ({x},{y}) rectangle ({x+c*s},{y+r*s});\n'
    if cells:
        for a,b in cells:
            z+=f'\\draw[black,line width=.75pt] ({x+a*s},{y+b*s}) rectangle ++({s},{s});\n'
    return z

def shape(x,y,cells,s=8):
    z=''
    for a,b in cells:
        z+=f'\\filldraw[fill=black!13,draw=black,line width=.75pt] ({x+a*s},{y+b*s}) rectangle ++({s},{s});\n'
    return z

def line(x,y,w=180):
    return f'\\draw[black!30,line width=.35pt] ({x},{y}) -- ++({w},0);\n'


# ---------------------------------------------------------------- page template

PRE=r'''\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0in]{geometry}
\usepackage{tikz}
\usepackage[T1]{fontenc}
\usepackage{lmodern}\pdfmapfile{+lm.map}
\pagestyle{empty}
\setlength{\parindent}{0pt}\hyphenpenalty=10000\exhyphenpenalty=10000
'''


def page_preamble(week, topic, header, footer):
    return (PRE + '\\newcommand{\\weekheader}{Week ' + f'{week} / {topic} / {header}' + '}\n'
            + '\\newcommand{\\weekfooter}{Bellingham Math Circle / Week ' + f'{week} / {footer}' + '}\n'
            + '\\begin{document}\n')


PAGE_OPEN=('\\null\n\\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]\n\\begin{scope}[shift={(current page.north west)}]\n'
           + node(15,12,'\\weekheader',11,width=187))
PAGE_CLOSE=(node(15,268,'\\weekfooter',9) + node(199,268,'\\thepage',9,anchor='north east')
            + '\\end{scope}\n\\end{tikzpicture}\n')


def page_prompt(n, body, x, y, size):
    """A numbered prompt at the left margin; y is 28 mm unless the heading places it (66 under the rules)."""
    return node(15, 28 if y is None else y, f'\\textbf{{Problem {n}:}} '+body, size or 14, width=184)


def page_text(x, y, body, w, size):
    return node(15 if x is None else x, y, body, size or 14, width=w)


# ---------------------------------------------------------------- shapes printed on the pages

starts=[[(i,0) for i in range(6)],[(i,0) for i in range(4)]+[(0,1),(2,1)],[(i,0) for i in range(4)]+[(0,1),(0,2)]]
start2=[[(i,0) for i in range(5)],[(0,0),(1,0),(1,1),(2,1),(2,2)],[(0,0),(1,0),(2,0),(0,1),(2,1)],[(i,j) for i in range(3) for j in range(3) if (i,j)!=(1,1)]]
branch=[(i,1) for i in range(5)]+[(0,0),(2,2),(4,0)]
shapes5=[[(i,0) for i in range(8)],branch,[(i,j) for i in range(4) for j in range(2)],start2[-1]]
shape3=[[(i,j) for i in range(6) for j in range(2)],[(i,j) for i in range(4) for j in range(3)],[(i,j) for j,k in enumerate([5,3,2,1]) for i in range(k)]+[(4,1)]]


# ---------------------------------------------------------------- K-1 figures, by problem file

def k1_four_tile_grids():  # 01
    b=''
    for i,(x,y) in enumerate([(24,108),(123,108),(24,159),(123,159),(24,210),(123,210)]):
        b+=grid(x,y,4,4,9.5)+node(x,y+40,r'\rule{13mm}{.3pt} sides',12)
    return b

def k1_extreme_grids(counts,s,c):  # 02 (5 and 6 tiles: s=11, c=7) and 03 (7 and 8 tiles: s=10, c=8)
    b=''
    for i,(x,y) in enumerate([(15,77),(114,77),(15,166),(114,166)]):
        b+=grid(x,y,c,6,s)
        adjective='shortest' if i%2==0 else 'longest'
        b+=node(x,y+6*s+3,f'{counts[i]} tiles; {adjective}',12)
        b+=node(x,y+6*s+9,r'\rule{13mm}{.3pt} sides',12)
    return b

def k1_six_tile_grids():  # 04
    b=''
    for i,(x,y) in enumerate([(22,68),(121,68),(22,132),(121,132),(22,196),(121,196)]):
        b+=grid(x,y,6,5,10)+node(x,y+53,f'{[10,10,12,12,14,14][i]} sides',12)
    return b

def k1_five_tile_grids():  # 05
    b=''
    for i,(x,y) in enumerate([(26,68),(125,68),(26,132),(125,132),(26,196),(125,196)]):
        b+=grid(x,y,5,5,10)+node(x,y+53,f'{8+i} sides',12)
    return b

def k1_one_move():  # 06
    b=''
    for y,cells in zip([72,135,198],starts):
        b+=shape(15,y+5,cells,10)+grid(109,y,8,5,10)+node(109,y+53,r'\rule{13mm}{.3pt} sides',12)
    return b


# ---------------------------------------------------------------- Grades 2-3 figures

def m_eight_tile_grids():  # 07
    b=''
    for i,(x,y) in enumerate([(15,107),(114,107),(15,184),(114,184)]):
        b+=grid(x,y,10,6,7.5)
        b+=node(x,y+48,('Shortest' if i%2==0 else 'Longest')+r' boundary: \rule{12mm}{.3pt}',12)
    return b

def m_add_one_tile():  # 08
    b=''
    for y,cells in zip([63,112,161,210],start2):
        b+=shape(15,y+2,cells,8)
        b+=node(15,y+32,r'Before: \rule{12mm}{.3pt}',11)
        for x in [64,108,152]:
            b+=grid(x,y,6,4,6.5)+node(x,y+31,r'After: \rule{12mm}{.3pt}',11)
            b+=node(x,y+37,r'Change: \rule{10mm}{.3pt}',11)
    return b

def m_shared_side_grids():  # 09
    b=''
    for i,(x,y) in enumerate([(15,77),(114,77),(15,132),(114,132),(15,187)]):
        b+=grid(x,y,12,5,6.2)+node(x,y+34,f'{9+i} shared sides',11)+node(x,y+41,r'Boundary: \rule{14mm}{.3pt}',11)
    for y in [196,211,226,246,259]:
        b+=line(114 if y<230 else 15,y,80 if y<230 else 179)
    return b

def m_longest_grids():  # 10
    b=''
    for n,(x,y) in zip([4,7,10,12],[(15,67),(114,67),(15,133),(114,133)]):
        b+=grid(x,y,14,5,5.5)+node(x,y+31,f'{n} tiles; boundary: '+r'\rule{12mm}{.3pt}',11)
    for y in [195,215,235,255]: b+=line(15,y,179)
    return b

def m_which_longest():  # 11
    b=''
    for (x,y),cells in zip([(15,86),(114,78),(29,132),(134,127)],shapes5):
        b+=shape(x,y,cells,7.5)
    for x in [15,114]: b+=grid(x,188,10,5,7.5)
    for y in [241,257]: b+=line(15,y,179)
    return b

def m_change_grids():  # 12
    b=''
    for ch,(x,y) in zip(['+2','0','$-2$','$-4$'],[(22,82),(121,82),(22,170),(121,170)]):
        b+=grid(x,y,8,5,8)+node(x,y+44,f'Boundary change: {ch}',12)
        b+=node(x,y+53,r'Starting tiles: \rule{10mm}{.3pt}',12)
    for y in [240,256]: b+=line(15,y,179)
    return b


# ---------------------------------------------------------------- Grades 4-5 figures

def u_shortest_grids():  # 13
    b=''
    for n,y in zip([7,10,13],[103,155,207]):
        for x in [20,119]:
            b+=grid(x,y,7,5,8)+node(x,y+42,f'{n} tiles; boundary: '+r'\rule{10mm}{.3pt}',11)
    return b

def u_longest_grids():  # 14
    b=''
    for x,y in [(15,78),(114,78),(15,138)]:
        b+=grid(x,y,14,5,5.5)+node(x,y+31,r'Boundary: \rule{14mm}{.3pt}',11)
    for y in [184,202,220,238,256]: b+=line(15,y,179)
    return b

def u_given_shapes():  # 15, the three shapes to count
    b=''
    for x,cells in zip([18,85,146],shape3):
        b+=shape(x,67,cells,7)
        b+=node(x,99,r'Rows: \rule{8mm}{.3pt}',11)
        b+=node(x,106,r'Columns: \rule{8mm}{.3pt}',11)
        b+=node(x,113,r'Boundary: \rule{8mm}{.3pt}',11)
    return b

def u_span_grids():  # 15, the two 4-by-5 grids
    b=''
    for x in [28,127]: b+=grid(x,184,5,4,11)+node(x,232,r'Boundary: \rule{12mm}{.3pt}',11)
    for y in [247,260]: b+=line(15,y,179)
    return b

def u_most_tiles_grids():  # 16
    b=''
    for P,(x,y) in zip([12,14,16,18],[(24,70),(123,70),(24,156),(123,156)]):
        b+=grid(x,y,7,6,9)+node(x,y+57,f'Boundary: {P}; tiles: '+r'\rule{10mm}{.3pt}',11)
    for y in [241,257]: b+=line(15,y,179)
    return b

def u_shortest_five_grids():  # 17
    b=''
    for n,(x,y) in zip([12,13,17,20,21],[(24,66),(123,66),(24,126),(123,126),(24,186)]):
        b+=grid(x,y,7,6,7)+node(x,y+45,f'{n} tiles; boundary: '+r'\rule{10mm}{.3pt}',11)
    for y in [194,210,226]: b+=line(114,y,80)
    for y in [245,259]: b+=line(15,y,179)
    return b

def u_rule_grids():  # 18
    b=''
    for n,(x,y) in zip([37,50,73],[(24,92),(123,92),(24,181)]):
        b+=grid(x,y,11,10,6)+node(x,y+63,f'{n} tiles; boundary: '+r'\rule{10mm}{.3pt}',11)
    for y in [186,202,218,234,250]: b+=line(113,y,80)
    return b
