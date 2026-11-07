"""Week 24 figures and canvas page template, carried over from the old builder
(archive-before-problem-files-2026-10-23/build_packets.py).

Coordinates are inches from the bottom-left corner of the paper, y up: each page is one
overlay picture anchored at the page's south-west corner, as the old builder drew it. The
header, footer and page number are drawn inside that picture (page_open and page_close);
the page number is the page's number in the view, which equals the problem number in the
full packets. Each prompt, text and figure is followed by a newline, as the old builder
joined its page items with newlines, so the rebuilt LaTeX is the old builder's (apart from
a final newline after \\end{document}).

Problem files call the functions below by name in their `figure` sections, through
art(...), which ends the figure's line; the rule and prompt wording lives in the problem
files.
"""

def text(x,y,t,size=14,width=7.2,anchor='north west'):
    return rf'\node[anchor={anchor},inner sep=0pt,text width={width}in,align=left,font=\fontsize{{{size}}}{{{size+4}}}\selectfont] at ({x},{y}) {{{t}}};'

def card(x,y,value,w=.62,h=.87,dots=False):
    # x,y is bottom-left; cards are illustrations, not a cutting template.
    # K-1 dot cards show the value in a ten-frame (two rows of five), so 8 and 9
    # differ by an empty space that can be seen without counting.
    s=[rf'\draw[line width=.8pt,rounded corners=2pt] ({x},{y}) rectangle ({x+w},{y+h});']
    if value is not None:
        s.append(rf'\node[font=\fontsize{{{25 if dots else 22}}}{{26}}\selectfont] at ({x+w/2},{y+h*(.76 if dots else .5)}) {{{value}}};')
        if dots:
            c=min(.13,(w-.1)/5); x0=x+w/2-2.5*c; y0=y+.12
            for k in range(3):
                s.append(rf'\draw[line width=.4pt,gray] ({x0:.3f},{y0+k*c:.3f}) -- ({x0+5*c:.3f},{y0+k*c:.3f});')
            for k in range(6):
                s.append(rf'\draw[line width=.4pt,gray] ({x0+k*c:.3f},{y0:.3f}) -- ({x0+k*c:.3f},{y0+2*c:.3f});')
            for i in range(value):
                col=i%5;row=i//5
                s.append(rf'\fill ({x0+(col+.5)*c:.3f},{y0+(1.5-row)*c:.3f}) circle ({.047 if c==.13 else round(.047*c/.13,3)});')
    return '\n'.join(s)

def kdeck(label,values,y,x=2.12):
    s=[rf'\node[font=\fontsize{{22}}{{25}}\selectfont] at (1.3,{y+.53}) {{{label}}};']
    for i,v in enumerate(values):s.append(card(x+i*1.26,y,v,.86,1.12,True))
    return '\n'.join(s)

def kdecks_row(y,w=.66,step=.72,gap=.42):
    """K-1 page 1: all three decks side by side, each labelled above, as dot cards,
    so the decks are shown before the first game."""
    s=[]; x=(8.5-(3*(2*step+w)+2*gap))/2
    for label,values in ABC:
        s.append(rf'\node[anchor=south,font=\fontsize{{18}}{{21}}\selectfont] at ({x+step+w/2:.3f},{y+.92}) {{{label}}};')
        for i,v in enumerate(values):s.append(card(x+i*step,y,v,w,.9,True))
        x+=2*step+w+gap
    return '\n'.join(s)

def kpool(values,y):
    w=.84;gap=.25;start=(8.5-len(values)*w-(len(values)-1)*gap)/2
    return '\n'.join(card(start+i*(w+gap),y,v,w,1.1,True) for i,v in enumerate(values))

def group(label,values,x,y,columns=3):
    s=[rf'\node[anchor=south,font=\fontsize{{16}}{{19}}\selectfont] at ({x+.99},{y+1.02}) {{{label}}};']
    for i,v in enumerate(values):s.append(card(x+(i%columns)*.7,y-(i//columns)*1.0,v))
    return '\n'.join(s)

def decks(ds,y=7.7):
    return '\n'.join(group(l,v,.72+i*2.4,y) for i,(l,v) in enumerate(ds))

def pool(values,y,columns=6):
    width=(min(columns,len(values))-1)*.86+.62; x=(8.5-width)/2
    return '\n'.join(card(x+(i%columns)*.86,y-(i//columns)*1.0,v) for i,v in enumerate(values))

def pair(label1,a,label2,b,x,y):
    s=[]
    for i,(l,v) in enumerate(((label1,a),(label2,b))):
        yy=y-i*1.1
        s.append(rf'\node[font=\fontsize{{15}}{{18}}\selectfont] at ({x},{yy+.435}) {{{l}}};')
        for j,n in enumerate(v):s.append(card(x+.36+j*.74,yy,n))
    return '\n'.join(s)

def shared_pairs(label1,a,label2,b):
    # Nine explicitly pictured pairs: a single pooled record, with no numeral
    # transcription or row/column convention required. Circle either card.
    s=[]
    for i,left in enumerate(a):
        for j,right in enumerate(b):
            x=1.04+j*2.33; y=3.75-i*1.45
            for label,value,xx in ((label1,left,x),(label2,right,x+1.0)):
                s.append(rf'\node[font=\fontsize{{12}}{{15}}\selectfont] at ({xx+.42},{y+1.27}) {{{label}}};')
                s.append(card(xx,y,value,.84,1.1,True))
    return '\n'.join(s)


def ktrack(top,bottom,y,x=1.9,d=.6,pitch=.78):
    """One K-1 game record: a row of six counter spaces for each deck. A label of
    None draws a blank box for the child's chosen deck letter."""
    s=[]
    for r,l in enumerate((top,bottom)):
        yy=y-r*pitch
        if l is None:
            s.append(rf'\draw[line width=.8pt] ({x-.95},{yy-.25}) rectangle ({x-.45},{yy+.25});')
        else:
            s.append(rf'\node[font=\fontsize{{22}}{{25}}\selectfont] at ({x-.7},{yy}) {{{l}}};')
        for i in range(6):
            s.append(rf'\draw[line width=.8pt] ({x+d/2+i*(d+.32):.3f},{yy}) circle ({d/2});')
    return '\n'.join(s)

def ktracks(games,y,gap=2.15,pitch=.78):
    return '\n'.join(ktrack(t,b,y-i*gap,pitch=pitch) for i,(t,b) in enumerate(games))

def triangle(cx,cy,r=.95):
    """A, B, C at the corners of a triangle, with a box beside each side for the
    letter of the deck that wins more pairs in that comparison."""
    import math
    pts={'A':(cx,cy+r),'B':(cx-r*math.sin(math.pi/3),cy-r/2),'C':(cx+r*math.sin(math.pi/3),cy-r/2)}
    s=[rf'\draw[line width=.8pt] ({pts["A"][0]:.3f},{pts["A"][1]:.3f}) -- ({pts["B"][0]:.3f},{pts["B"][1]:.3f}) -- ({pts["C"][0]:.3f},{pts["C"][1]:.3f}) -- cycle;']
    for l,(x,y) in pts.items():
        s.append(rf'\node[circle,draw,line width=.8pt,fill=white,minimum size=.42in,inner sep=0pt,font=\fontsize{{18}}{{20}}\selectfont] at ({x:.3f},{y:.3f}) {{{l}}};')
    for p,q in (('A','B'),('B','C'),('C','A')):
        mx=(pts[p][0]+pts[q][0])/2; my=(pts[p][1]+pts[q][1])/2
        dx=mx-cx; dy=my-cy; n=math.hypot(dx,dy); off=.38
        bx=mx+dx/n*off; by=my+dy/n*off
        s.append(rf'\draw[line width=.8pt,fill=white] ({bx-.2:.3f},{by-.2:.3f}) rectangle ({bx+.2:.3f},{by+.2:.3f});')
    return '\n'.join(s)

def swap_grid(a,b,y,x=2.3,c=1.2):
    """K-1 swap record: A's cards across the top, B's cards down the side; the box
    where a column and a row meet is the swap of those two cards."""
    s=[rf'\node[font=\fontsize{{22}}{{25}}\selectfont] at ({x+1.5*c},{y+1.45}) {{A}};',
       rf'\node[font=\fontsize{{22}}{{25}}\selectfont] at ({x-1.45},{y-1.5*c}) {{B}};']
    for i,v in enumerate(a):s.append(card(x+i*c+(c-.84)/2,y+.06,v,.84,1.1,True))
    for j,v in enumerate(b):s.append(card(x-1.07,y-(j+1)*c+(c-1.1)/2,v,.84,1.1,True))
    for i in range(3):
        for j in range(3):
            s.append(rf'\draw[line width=.8pt] ({x+i*c+.06:.3f},{y-(j+1)*c+.06:.3f}) rectangle ({x+(i+1)*c-.06:.3f},{y-j*c-.06:.3f});')
    return '\n'.join(s)

def score_table(y,rows=5,x=1.25,w=3.0,h=.55,example=None):
    """Grades 2-5 game record: one row per game, first and second picker's deck and rounds won."""
    s=[rf'\node[anchor=south,font=\fontsize{{13}}{{16}}\selectfont] at ({x+w/2},{y+.08}) {{First pick}};',
       rf'\node[anchor=south,font=\fontsize{{13}}{{16}}\selectfont] at ({x+1.5*w},{y+.08}) {{Second pick}};']
    s.append(rf'\draw[line width=.6pt] ({x},{y}) rectangle ({x+2*w},{y-rows*h});')
    s.append(rf'\draw[line width=.6pt] ({x+w},{y}) -- ({x+w},{y-rows*h});')
    for r in range(1,rows):
        s.append(rf'\draw[line width=.4pt] ({x},{y-r*h:.3f}) -- ({x+2*w},{y-r*h:.3f});')
    if example:
        # one example row just under the headings, shaded: each player's deck and rounds won
        s.append(rf'\fill[gray!12] ({x},{y}) rectangle ({x+2*w},{y-h:.3f});')
        s.append(rf'\draw[line width=.6pt] ({x},{y}) rectangle ({x+2*w},{y-h:.3f});')
        s.append(rf'\draw[line width=.6pt] ({x+w},{y}) -- ({x+w},{y-h:.3f});')
        s.append(rf'\node[anchor=east,font=\fontsize{{11}}{{13}}\selectfont\itshape] at ({x-.08},{y-h/2:.3f}) {{example}};')
        for k,t in enumerate(example):
            s.append(rf'\node[font=\fontsize{{14}}{{17}}\selectfont] at ({x+w/2+k*w:.3f},{y-h/2:.3f}) {{{t}}};')
    return '\n'.join(s)


def art(*parts):
    """A problem's figure: the drawing commands, then the newline that ends its line."""
    return ''.join(parts) + '\n'


ABC = [('A', [2, 4, 9]), ('B', [1, 6, 8]), ('C', [3, 5, 7])]


# ---------------------------------------------------------------- page template

PRE=r'''\documentclass[letterpaper]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\usepackage[margin=0in]{geometry}
\usepackage{tikz}
\pagestyle{empty}
\renewcommand{\familydefault}{\sfdefault}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\begin{document}
'''


def page_preamble(week, topic, header, footer):
    return PRE + '\n'


def page_open(page):
    return ('\\null\n\\begin{tikzpicture}[remember picture,overlay,x=1in,y=1in]\n'
            '\\begin{scope}[shift={(current page.south west)}]\n'
            + text(.62, 10.5, f'Week {page.week} / {page.topic} / {page.header}', 10.5, 7.25, 'west') + '\n')


def page_close(page):
    return (text(.62, .46, f'Bellingham Math Circle / Week {page.week} / {page.footer}', 9.5, 6.7, 'west') + '\n'
            + rf'\node[anchor=east,inner sep=0pt,font=\fontsize{{9.5}}{{12}}\selectfont] at (7.88,.46) {{{page.number}}};'
            + '\n\\end{scope}\n\\end{tikzpicture}\n')


def page_prompt(n, body, x, y, size):
    """A numbered prompt at the left margin: 9.02 in up on a first page under the rules, else 9.95."""
    return text(.62, 9.95 if y is None else y, rf'\textbf{{Problem {n}:}} ' + body, size) + '\n'


def page_text(x, y, body, w, size):
    return text(x, y, body, size, 7.2 if w is None else w) + '\n'
