"""Week 11 figures and canvas page template, carried over unchanged from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py).

Coordinates are millimetres with y pointing down, measured from the page's top-left
corner, as the old builder drew them. Problem files call the figure functions below
by name; the rule and prompt wording lives in the problem files. The header, footer
and page number are drawn inside each page's picture by page_open(page) and
page_close(page), so the rebuilt LaTeX is the old builder's byte for byte.
"""

# ---------------------------------------------------------------- drawing helpers

def node(x,y,text,w=None,size=12,leading=None,anchor='north west',align='left'):
    leading=leading or size*1.25
    width=f', text width={w}mm' if w else ''
    return rf'\node[anchor={anchor},inner sep=0pt,align={align}{width},font=\fontsize{{{size}}}{{{leading}}}\selectfont] at ({x},{y}) {{{text}}};'+'\n'


def board(kind,top):
    """The triangle, the four-cycle ('square') or the four-cycle with the A-C line ('diagonal')."""
    if kind=='triangle':
        coords={'A':(61,top+22),'B':(155,top+22),'S':(108,top+84)}
        edges=[('A','B'),('A','S'),('B','S')]
    else:
        coords={'A':(61,top+22),'B':(155,top+22),'C':(155,top+104),'S':(61,top+104)}
        edges=[('S','A'),('A','B'),('B','C'),('C','S')]
        if kind=='diagonal': edges.append(('A','C'))
    s=''
    for v,(x,y) in coords.items():
        shape='rectangle,minimum width=60mm,minimum height=60mm' if v=='S' else 'circle,minimum size=44mm'
        s+=rf'\node[draw,line width=0.9pt,{shape},inner sep=0pt] ({v}) at ({x},{y}) {{}};'+'\n'
    for a,b in edges:
        s+=rf'\draw[line width=1.05pt] ({a}) -- ({b});'+'\n'
    for v,(x,y) in coords.items():
        if v=='S':
            s+=node(x,y+23,'SINK',size=12,anchor='center')
        elif v=='C':
            s+=node(x+28,y,v,size=14,anchor='center')
        else:
            s+=node(x,y-27,v,size=14,anchor='center')
    return s


def word_example(k=False,y=148):
    """The recording convention, beside the board before the first record. The sample
    word is not the solution to any printed start."""
    s=node(14,y,'A, then B, then A:',60,11.5,14)
    s+=node(14,y+10,r'$\mathrm{A}\;\to\;\mathrm{AB}\;\to\;\mathrm{ABA}$',60,11.5,14)
    if not k:
        s+=node(143,y,"After stopping, count letters: ABA has two A's and one B.",59,11.5,14)
    return s


def dots(n):
    """A K-1 pile drawn as n chip dots."""
    if n==0:return '0'
    return r'\tikz[baseline=-0.6ex,x=1mm,y=1mm]{'+''.join(rf'\fill ({3.5*i},0) circle (0.95mm);' for i in range(n))+'}'


def table(x,y,widths,headers,rows,rowh=8,headh=10,fontsize=11):
    xs=[x]
    for w in widths:xs.append(xs[-1]+w)
    s=''
    bottom=y+headh+rowh*len(rows)
    for xx in xs:
        s+=rf'\draw[black!45,line width=.35pt] ({xx},{y}) -- ({xx},{bottom});'+'\n'
    for yy in [y,y+headh]+[y+headh+rowh*i for i in range(1,len(rows)+1)]:
        s+=rf'\draw[black!45,line width=.35pt] ({x},{yy}) -- ({xs[-1]},{yy});'+'\n'
    for i,h in enumerate(headers):s+=node((xs[i]+xs[i+1])/2,y+headh/2,h,size=fontsize,anchor='center',align='center')
    for j,row in enumerate(rows):
        for i,t in enumerate(row):
            if t is not None:s+=node((xs[i]+xs[i+1])/2,y+headh+(j+.5)*rowh,str(t),size=fontsize,anchor='center',align='center')
    return s


def lines(y,number=3,step=10):
    return ''.join(rf'\draw[black!25,line width=.35pt] (14,{y+i*step}) -- (202,{y+i*step});'+'\n' for i in range(number))


# ---------------------------------------------------------------- page template
# The old builder's page: Latin Modern sans, one overlay picture per page holding the
# header, the footer with its page number, and the problem.

PRE=r'''\documentclass[letterpaper]{article}
\usepackage[margin=0mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}\pdfmapfile{+lm.map}\pdfmapfile{+cm.map}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{calc}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\begin{document}
'''
LEADING={14:18,12.5:16,11.5:14}   # the old builder's line spacing for each type size


def page_preamble(week, topic, header, footer):
    return PRE


def page_open(page):
    """The old builder's begin(): the overlay picture, header, footer and page number."""
    s=r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]'+'\n'+r'\begin{scope}[shift={(current page.north west)}]'+'\n'
    s+=node(14,12,rf'Week {page.week} / {page.topic} / {page.header}',size=11)
    s+=node(14,267,rf'Bellingham Math Circle / Week {page.week} / {page.footer}',size=9.5)
    s+=node(202,267,str(page.number),size=9.5,anchor='north east')
    return s


def page_close(page):
    """The old builder's end(); the composer adds the \\newpage between pages."""
    return r'\end{scope}\end{tikzpicture}'+('\n' if page.number==page.count else '')


def page_prompt(n, body, x, y, size):
    """The old builder's problem(): the label and statement in one node at the left margin."""
    return node(14,26 if y is None else y,rf'\textbf{{Problem {n}:}} {body}',188,size,LEADING[size])


def page_text(x, y, body, w, size):
    return node(14 if x is None else x,y,body,w,size,LEADING.get(size))


# ---------------------------------------------------------------- figures
# Each returns the drawing that followed a problem's statement on its page. The
# printed starts are named here so that editable/src/student_checks.py checks them.

K1_ORDER_TRIANGLE=[(2,2),(3,2),(2,3),(3,3)]          # K-1 P1, each on two rows
ORDER_TRIANGLE_23=[(2,2),(4,0),(3,3)]                # grades 2-3 P1, each on two rows
ORDER_TRIANGLE_45=[(2,2),(4,0),(3,3),(5,4)]          # grades 4-5 P1, each on two rows
K1_ORDER_SQUARE=[(0,4,0),(2,2,0),(0,2,2),(2,0,2)]    # K-1 P3, each on two rows
ORDER_SQUARE_23=[(0,4,0),(2,1,2),(2,4,2)]            # grades 2-3 P2, each on two rows
EXTRA_LINE_23=[(3,0,3),(0,6,0),(2,2,2),(4,1,2)]      # grades 2-3 P4, each on two rows
EXTRA_LINE_45=[(3,0,3),(0,6,0),(4,1,2)]              # grades 4-5 P4, each on two rows
K1_STABLE_ROWS=10                                    # K-1 P4: more rows than its 8 answers
K1_ADD_ONE_ROWS=11                                   # K-1 P6
BATCHES_23=((2,0,0),(0,4,0))                         # grades 2-3 P5: 2 at A and 4 at B on the four-cycle


def twice(starts):
    """Each start on two rows, one for each order."""
    return [s for s in starts for _ in (0,1)]

def k1_order_triangle():  # K-1 P1, triangle board, word example, four starts as dots, each twice
    return (board('triangle',72)+word_example(True,132)
            +table(20,196,[25,25,76,25,25],['Start A','Start B','Sharing word','Finish A','Finish B'],[[dots(a),dots(b),'','',''] for a,b in twice(K1_ORDER_TRIANGLE)],7,9,11))


def order_triangle_23():  # grades 2-3 P1, three starts twice each
    rows=[[a,b,'','',''] for a,b in twice(ORDER_TRIANGLE_23)]
    return (board('triangle',88)+word_example()
            +table(18,208,[24,24,76,28,28],['Start A','Start B','Sharing word','Finish A','Finish B'],rows,7.4,9,10.5))


def order_triangle_45():  # grades 4-5 P1, four starts twice each
    rows=[[a,b,'','',''] for a,b in twice(ORDER_TRIANGLE_45)]
    return (board('triangle',73)+word_example(y=134)
            +table(18,193,[24,24,76,28,28],['Start A','Start B','Sharing word','Finish A','Finish B'],rows,7.2,9,10.5))


def k1_four_and_five():  # K-1 P2, triangle board and two answer areas
    return (board('triangle',60)
            +node(28,190,'4 chips',size=13)+node(116,190,'5 chips',size=13)
            +r'\draw[black!30,line width=.4pt] (107,190) -- (107,257);'+'\n')


def k1_order_square():  # K-1 P3, four-cycle board, four starts as dots, each twice
    return (board('square',48)
            +table(13,190,[24,24,24,55,21,21,21],['Start A','Start B','Start C','Sharing word','Finish A','Finish B','Finish C'],[[dots(a),dots(b),dots(c),'','','',''] for a,b,c in twice(K1_ORDER_SQUARE)],7.7,9,10))


def order_square_23():  # grades 2-3 P2, three starts twice each
    rows=[[a,b,c,'','','',''] for a,b,c in twice(ORDER_SQUARE_23)]
    return (board('square',53)
            +table(13,201,[21,21,21,63,21,21,21],['Start A','Start B','Start C','Sharing word','Finish A','Finish B','Finish C'],rows,8.1,10,9.2))


def six_chip_starts():  # grades 2-3 P3, triangle board, seven start rows and two lines
    return (board('triangle',55)
            +table(27,180,[40]*4,['Start A','Start B','Finish A','Finish B'],[['','','',''] for _ in range(7)],7,9,11)
            +lines(247,2,10))


def k1_stable_placements():  # K-1 P4, four-cycle board and ten answer rows (8 placements are stable)
    return (board('square',48)
            +table(42,188,[44]*3,['A','B','C'],[['','',''] for _ in range(K1_STABLE_ROWS)],6.5,9,12))


def batches_45():  # grades 4-5 P2, four-cycle board and the six timing rows
    return (board('square',58)
            +table(13,201,[33,33,41,27,27,27],[r'First batch',r'Second batch','Timing','Finish A','Finish B','Finish C'],[[r'4 at B',r'2 at A','together','','',''],[r'4 at B',r'2 at A','first, then second','','',''],[r'4 at B',r'2 at A','second, then first','','',''],[r'3 at A',r'3 at C','together','','',''],[r'3 at A',r'3 at C','first, then second','','',''],[r'3 at A',r'3 at C','second, then first','','','']],8,11,9.7))


def add_one_45():  # grades 4-5 P3, triangle board, four stable starts and a line
    return (board('triangle',64)
            +table(17,192,[23,23,34,34,34,34],['Start A','Start B','After 1','After 2','After 3','After 4'],[[a,b,'','','',''] for a,b in [(0,0),(1,0),(0,1),(1,1)]],10,9,10.5)
            +lines(252,1))


def extra_line_23():  # grades 2-3 P4, extra-line board, four starts twice each
    rows=[[a,b,c,'','','',''] for a,b,c in twice(EXTRA_LINE_23)]
    return (board('diagonal',53)
            +table(13,194,[21,21,21,63,21,21,21],['Start A','Start B','Start C','Sharing word','Finish A','Finish B','Finish C'],rows,7.1,10,9.2))


def extra_line_45():  # grades 4-5 P4, extra-line board, three starts twice each
    rows=[[a,b,c,'','','',''] for a,b,c in twice(EXTRA_LINE_45)]
    return (board('diagonal',56)
            +table(13,204,[21,21,21,63,21,21,21],['Start A','Start B','Start C','Sharing word','Finish A','Finish B','Finish C'],rows,7.4,10,9.2))


def k1_batches():  # K-1 P5, triangle board, each addition row three times
    return (board('triangle',60)
            +table(20,191,[25,25,76,25,25],['Add at A','Add at B','Sharing word','Finish A','Finish B'],[[dots(a),dots(b),'','',''] for a,b in [(3,3)]*3+[(2,4)]*3],9.5,10,11))


def batches_23():  # grades 2-3 P5, four-cycle board and one row for each timing
    return (board('square',61)
            +table(18,211,[30,30,48,24,24,24],[r'Add at A',r'Add at B','Timing','Finish A','Finish B','Finish C'],[[2,4,t,'','',''] for t in ('together','2 at A first','4 at B first')],10,9,10.5))


def k1_add_one():  # K-1 P6, triangle board and eleven addition rows
    return (board('triangle',55)
            +table(42,178,[44]*3,['Chips added','Finish A','Finish B'],[[i,'',''] for i in range(1,K1_ADD_ONE_ROWS+1)],6.4,9,11.5))


def add_one_23():  # grades 2-3 P6, triangle board and twelve rows for both rules
    return (board('triangle',54)
            +table(23,176,[30,36,36,36,36],['Chips added',r'Add to A:\\final A',r'Add to A:\\final B',r'Add to B:\\final A',r'Add to B:\\final B'],[[i,'','','',''] for i in range(1,13)],6,13,10.5))


def termination_board():  # grades 4-5 P5, four-cycle board and four lines
    return board('square',65)+lines(220,4,11)


def order_proof_board():  # grades 4-5 P6, four-cycle board and four lines
    return board('square',64)+lines(216,4,12)


# ---------------------------------------------------------------- key figure (adult key view only)

def add_one_cycle():  # the guide's p. 7 diagram: add one chip at A and finish, on the triangle's stable states
    s=''
    for name,x,label in (('z',0,'(0,0)'),('a',3.6,'(1,0)'),('b',7.2,'(0,1)'),('c',10.8,'(1,1)')):
        s+=rf'\node[draw,rounded corners,minimum width=15mm,minimum height=8mm] ({name}) at ({x}cm,0cm) {{${label}$}};'+'\n'
    s+=r'\draw[-Stealth] (z)--(a);\draw[-Stealth] (a)--(b);\draw[-Stealth] (b)--(c);\draw[-Stealth] (c) to[bend right=38] (a);'+'\n'
    return s
