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
    s=[rf'\draw[line width=.8pt,rounded corners=2pt] ({x},{y}) rectangle ({x+w},{y+h});']
    if value is not None:
        s.append(rf'\node[font=\fontsize{{{25 if dots else 22}}}{{26}}\selectfont] at ({x+w/2},{y+h*(.76 if dots else .5)}) {{{value}}};')
        if dots:
            for i in range(value):
                col=i%3;row=i//3
                xx=x+w/2+(col-1)*.14; yy=y+.37-row*.125
                s.append(rf'\fill ({xx},{yy}) circle (.025);')
    return '\n'.join(s)

def kdeck(label,values,y,x=2.12):
    s=[rf'\node[font=\fontsize{{22}}{{25}}\selectfont] at (1.3,{y+.53}) {{{label}}};']
    for i,v in enumerate(values):s.append(card(x+i*1.26,y,v,.86,1.12,True))
    return '\n'.join(s)

def kpool(values,y):
    w=.73;gap=.29;start=(8.5-len(values)*w-(len(values)-1)*gap)/2
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
                s.append(rf'\node[font=\fontsize{{12}}{{15}}\selectfont] at ({xx+.365},{y+1.27}) {{{label}}};')
                s.append(card(xx,y,value,.73,1.1,True))
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
