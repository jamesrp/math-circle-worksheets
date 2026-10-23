"""Week 25 figures and canvas page template, carried over from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py and examples.py).

Coordinates are millimetres from the top-left corner of the paper, y down. Each page is
one overlay picture on the whole sheet that draws its own header, rules, footer and page
number (page_open and page_close). Problem files call the functions below by name in
their `figure` sections; the rule, prompt and caption wording lives in the problem files.
"""

CELL=22


# ---------------------------------------------------------------- drawing primitives (build_packets.py)

# A circled total is separate from the permanent row/column labels.
def board(x,y,r,c,rows=None,cols=None,picture=None,blank_counts=False,cell=CELL):
    s=[]
    for j in range(c+1):
        s.append(fr'\draw[line width=0.55pt] ({x+j*cell},{y}) -- ({x+j*cell},{y+r*cell});')
    for i in range(r+1):
        s.append(fr'\draw[line width=0.55pt] ({x},{y+i*cell}) -- ({x+c*cell},{y+i*cell});')
    for i in range(r):
        yy=y+(i+.5)*cell
        s.append(fr'\node[font=\fontsize{{11}}{{13}}\selectfont] at ({x-5.2},{yy}) {{{chr(65+i)}}};')
        if rows is not None or blank_counts:
            xx=x+c*cell+6
            s.append(fr'\draw[line width=.45pt] ({xx},{yy}) circle[radius=3.6mm];')
            value='' if rows is None else str(rows[i])
            s.append(fr'\node[font=\fontsize{{12}}{{14}}\selectfont] at ({xx},{yy}) {{{value}}};')
    for j in range(c):
        xx=x+(j+.5)*cell
        s.append(fr'\node[font=\fontsize{{11}}{{13}}\selectfont] at ({xx},{y-5.2}) {{{j+1}}};')
        if cols is not None or blank_counts:
            yy=y+r*cell+6
            s.append(fr'\draw[line width=.45pt] ({xx},{yy}) circle[radius=3.6mm];')
            value='' if cols is None else str(cols[j])
            s.append(fr'\node[font=\fontsize{{12}}{{14}}\selectfont] at ({xx},{yy}) {{{value}}};')
    if picture:
        assert len(picture)==r and all(len(a)==c for a in picture)
        for i,row in enumerate(picture):
            for j,value in enumerate(row):
                if value=='1':
                    s.append(fr'\fill ({x+(j+.5)*cell},{y+(i+.5)*cell}) circle[radius={4.6 if cell == CELL else min(4.6,cell*.20)}mm];')
    return '\n'.join(s)

def text(y,content,size=13,leading=17):
    return fr'\node[anchor=north west,inner sep=0pt,text width=188mm,font=\fontsize{{{size}}}{{{leading}}}\selectfont,align=left] at (14,{y}) {{{content}}};'

def pair(y,r,c,rows,cols,pictures=None,blank=False):
    xs=[25,122] if c==3 else [36,133]
    return '\n'.join(board(x,y,r,c,rows,cols,None if pictures is None else pictures[i],blank) for i,x in enumerate(xs))

def center(y,r,c,rows=None,cols=None,picture=None,blank=False,cell=CELL):
    return board((215.9-c*cell)/2,y,r,c,rows,cols,picture,blank,cell)

def switch_example(y,caption,record=False):
    # A small notation example, not an answer to any displayed task. With record=True the
    # switch's rectangle is drawn through its four corner cells on the left picture, the way
    # children record a switch they find (grades 2-3; card should 7, October 23, 2026).
    out=fr'\node[anchor=west,font=\fontsize{{11}}{{13}}\selectfont] at (16,{y+8}) {{{caption}}};'
    if record:
        out+=fr'\draw[line width=1.1pt,black!55,rounded corners=.6mm] (75,{y+4}) rectangle (83,{y+12});'
    out+=board(71,y,2,2,[1,1],[1,1],['10','01'],cell=8)
    out+=board(135,y,2,2,[1,1],[1,1],['01','10'],cell=8)
    out+=fr'\draw[->,>=stealth,line width=.8pt] (103,{y+8}) -- (120,{y+8});'
    return out


def lines(*items):
    """Figure sections are lines of LaTeX, each ending in a newline, as the old pages were joined."""
    return ''.join(i+'\n' for i in items)


# ---------------------------------------------------------------- page template (build_packets.py's write_packet)

PREAMBLE=r'''\documentclass[letterpaper]{article}
\usepackage[margin=0mm]{geometry}
\usepackage{tikz}
\usepackage{fix-cm}
\pdfmapfile{+cm.map}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\renewcommand{\familydefault}{\sfdefault}
\begin{document}
'''


def page_preamble(week, topic, header, footer):
    return PREAMBLE


def page_open(page):
    return (r'\null\begin{tikzpicture}[remember picture,overlay,x=1mm,y=-1mm]'+'\n'+r'\begin{scope}[shift={(current page.north west)}]'+'\n'
            + text(10,fr'Week {page.week} / {page.topic} / {page.header}',11.5,14)+'\n'
            + r'\draw[line width=.35pt] (14,19) -- (202,19);'+'\n')


def page_close(page):
    return (r'\draw[line width=.35pt] (14,263.5) -- (202,263.5);'+'\n'
            + fr'\node[anchor=north west,inner sep=0pt,font=\fontsize{{9}}{{11}}\selectfont] at (14,267) {{Bellingham Math Circle / Week {page.week} / {page.footer}}};'+'\n'
            + fr'\node[anchor=north east,inner sep=0pt,font=\fontsize{{9}}{{11}}\selectfont] at (202,267) {{{page.number}}};'+'\n'
            + r'\end{scope}\end{tikzpicture}'+'\n')


def page_prompt(n, body, x, y, size):
    """The old problem(): 14 pt on 18 for K-1, 13 pt on 17 otherwise (week.toml), at the left margin."""
    return text(y,fr'\textbf{{Problem {n}:}} '+body,size,size+4)+'\n'


def page_text(x, y, body, w, size):
    """The shared rules are 12 pt on 15.5; other text keeps the problem spacing (size + 4)."""
    return text(y,body,size,15.5 if size==12 else size+4)+'\n'


# ---------------------------------------------------------------- the K-1 worked example (examples.py)

def shadow_example(caption,across,down):  # 00, K-1: two counters become row and column counts
    s=[text(49,caption,14,18)]
    s += [board(36,83,2,2,picture=['11','00']),board(128,83,2,2,[2,0],[1,1],['11','00'])]
    s += [r'\draw[->,>=stealth,line width=1pt] (92,105) -- (113,105);']
    # Sweeps run beside the discs and finish at the associated circled count.
    for y in (94,116):
        s += [fr'\draw[black!55,dashed,->,>=stealth,line width=.8pt] (131,{y-5.5}) -- (169,{y-5.5}) -- (174,{y});']
    for x in (139,161):
        s += [fr'\draw[black!55,dotted,->,>=stealth,line width=1pt] ({x-5.5},86) -- ({x-5.5},124) -- ({x},{129.4});']
    s += [fr'\node[anchor=west,font=\fontsize{{12}}{{15}}\selectfont] at (128,153) {{{across}}};',r'\draw[black!55,dashed,->,>=stealth] (128,162) -- (150,162);',
          fr'\node[anchor=west,font=\fontsize{{12}}{{15}}\selectfont] at (128,176) {{{down}}};',r'\draw[black!55,dotted,->,>=stealth,line width=1pt] (128,185) -- (150,185);']
    return lines(*s)


# ---------------------------------------------------------------- K-1 figures, by problem file

def k1_two_picture_pairs():  # 01
    return lines(pair(76,2,2,[1,1],[1,1]),pair(139,2,3,[1,1],[1,0,1]),pair(202,2,3,[2,1],[1,1,1]))

def k1_two_catalogs():  # 02: rows 1, 2 on the left and 2, 1 on the right
    return lines(*(board(x,y,2,3,rows,[1,1,1]) for y in (61,126,191) for x,rows in ((25,[1,2]),(122,[2,1]))))

def k1_three_counter_grids():  # 03
    return lines(pair(62,3,3,[1,1,1],[1,1,1]),pair(160,3,3,[1,1,1],[1,1,1]))

def k1_three_counter_more():  # 04
    return lines(pair(57,3,3,[1,1,1],[1,1,1]))

def k1_forced_pair():  # 05
    return lines(pair(187,2,3,[3,1],[2,1,1]))

def k1_forced_or_not():  # 06
    return lines(pair(65,3,3,[2,1,0],[2,1,0]),pair(165,3,3,[2,1,1],[2,1,1]))

def blank_pairs(y1=86,y2=170):  # 07, 08 (K-1) and 15 (grades 2-3, y1=85): a 2 x 3 and a 3 x 3 pair, counts blank
    return lines(pair(y1,2,3,None,None,blank=True),pair(y2,3,3,None,None,blank=True))


# ---------------------------------------------------------------- grades 2-3 figures

def m_two_pictures_if_possible():  # 09
    return lines(pair(76,2,3,[2,1],[1,1,1]),pair(139,2,3,[3,1],[2,1,1]),pair(202,2,3,[2,2],[2,1,1]))

def m_211_grids():  # 10
    return lines(pair(62,3,3,[2,1,1],[2,1,1]),pair(160,3,3,[2,1,1],[2,1,1]))

def m_211_more():  # 11
    return lines(pair(55,3,3,[2,1,1],[2,1,1]))

def m_two_counter_move():  # 12
    return lines(pair(181,3,3,[1,0,1],[1,0,1],[['100','000','001'],None]))

def m_switch_pictures(caption,record=False):  # 13: the switch example, then pictures with 0, 1, 3 and 0 switches
    return lines(switch_example(55,caption,record),
                 board(25,91,3,3,[2,1,0],[2,1,0],['110','100','000']),
                 board(122,91,3,3,[1,0,1],[1,0,1],['100','000','001']),
                 board(25,183,3,3,[2,1,1],[2,1,1],['110','001','100']),
                 board(122,183,3,3,[3,2,1],[3,2,1],['111','110','100']))

def m_exact_switches():  # 14
    return lines(center(80,2,4,[2,2],[1,1,1,1],['1100','0011']),center(143,2,4,[2,2],[1,1,1,1]),center(206,2,4,[2,2],[1,1,1,1]))


# ---------------------------------------------------------------- grades 4-5 figures

# Grades 4-5 Problem 1 has eight recording grids for its six pictures, four on each page in two
# columns of 18.5 mm cells (card should 3, October 23, 2026: the page should not show the total).
# Left grids at x = 21 put the row labels inside the 14 mm margin; right grids at x = 118.4 end
# their circled counts at 202 mm, 7 mm clear of the left grids' circles.
SIX_CELL=18.5

def six_grid_rows(*ys):
    return lines(*(board(x,y,2,4,[2,2],[1,1,1,1],cell=SIX_CELL) for y in ys for x in (21,118.4)))

def h_six_pictures():  # 16
    return six_grid_rows(84,168)

def h_six_more():  # 17
    return six_grid_rows(58,148)

def h_switch_distances(caption):  # 18
    return lines(switch_example(55,caption),*(center(y,2,4,[2,2],[1,1,1,1],cell=20) for y in (94,152,210)))

def h_route_endpoints():  # 19
    return lines(center(70,2,6,[3,3],[1,1,1,1,1,1],['111000','000111']),center(146,2,6,[3,3],[1,1,1,1,1,1],['000111','111000']))

def h_route_grids():  # 20: three grids, one more than a shortest route's two intermediate pictures
    return lines(*(center(y,2,6,[3,3],[1,1,1,1,1,1]) for y in (44,114,184)))

def h_fixed_columns():  # 21
    return lines(center(74,2,6,[3,3],[2,1,0,1,1,1],['110100','100011']),center(150,2,6,[3,3],[2,1,0,1,1,1],['100011','110100']))

def h_fixed_blanks():  # 22: workspace with Problem 4's counts, fewer grids than its six pictures
    return lines(*(center(y,2,6,[3,3],[2,1,0,1,1,1]) for y in (44,114,184)))

def h_two_row_blanks():  # 23
    return lines(center(92,2,6,blank=True),center(170,2,6,blank=True))
