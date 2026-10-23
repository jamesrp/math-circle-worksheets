"""Week 18 figures and canvas page template, carried over from the old student builder
(archive-before-problem-files-2026-10-23/build_packets.py and examples.py).

Coordinates are centimetres, y down, inside the old builder's page frame: each page is
one overlay picture anchored at the page's north-west corner and shifted 1.5 cm right
and down, with its own header, footer and page number. The old builder's Packet methods
are the functions below; each returns LaTeX lines, each line starting with a newline, so
the pages come out exactly as the old builder joined them. Problem files call them in
their `figure` sections; the wording lives in the problem files.

A text section's line spacing is the old builder's: LEAD gives it for the sizes the
pages use, and other sizes take 1.24 times the size, as prompts do.
"""

PRE = r'''\RequirePackage{fix-cm}
\documentclass[12pt,letterpaper]{article}
\usepackage[margin=0.5in]{geometry}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000\exhyphenpenalty=10000
\pdfmapfile{+cm.map}
\begin{document}
'''

LEAD = {14: 18}


def page_preamble(week, topic, header, footer):
    return PRE


def page_open(page):
    return (r'\null\begin{tikzpicture}[remember picture,overlay]'
            + '\n' + r'\begin{scope}[shift={(current page.north west)},x=1cm,y=-1cm]'
            + '\n' + r'\begin{scope}[shift={(1.5,1.5)}]'
            + text(0, -.45, 18.5, f'Week {page.week} / {page.topic} / {page.header}', 11, 14)
            + text(0, 24.5, 16.5, f'Bellingham Math Circle / Week {page.week} / {page.footer}', 10, 12)
            + '\n' + r'\node[anchor=north east,inner sep=0,font=\sffamily\fontsize{10}{12}\selectfont] at (18.59,24.5) {'
            + str(page.number) + '};')


def page_close(page):
    return '\\end{scope}\\end{scope}\\end{tikzpicture}\n'


def page_prompt(n, body, x, y, size):
    return text(0, .45 if y is None else y, 18.4, r'\textbf{Problem ' + str(n) + ':} ' + body, 15 if size is None else size)


def page_text(x, y, body, w, size):
    size = 14 if size is None else size
    return text(x, y, w, body, size, LEAD.get(size))


def text(x, y, w, txt, size=14, lead=None):
    lead = lead or size*1.24
    return '\n' + r'\node[anchor=north west,inner sep=0,align=left,text width='+str(w)+'cm,font=\\sffamily\\fontsize{'+str(size)+'}{'+str(lead)+'}\\selectfont] at ('+str(x)+','+str(y)+') {'+txt+'};'


say = text   # a sentence placed inside a figure


def shape(x, y, shape, scale=.38):
    if shape == 'triangle':
        return '\n' + f'\\draw[line width=.8pt] ({x},{y-scale}) -- ({x-scale},{y+scale*.8}) -- ({x+scale},{y+scale*.8}) -- cycle;'
    elif shape == 'square':
        return '\n' + f'\\draw[line width=.8pt] ({x-scale},{y-scale}) rectangle ({x+scale},{y+scale});'
    elif shape == 'diamond':
        return '\n' + f'\\draw[line width=.8pt] ({x},{y-scale*1.2}) -- ({x+scale},{y}) -- ({x},{y+scale*1.2}) -- ({x-scale},{y}) -- cycle;'
    elif shape == 'star':
        return '\n' + f'\\node[star,star points=5,star point ratio=2.1,draw,line width=.8pt,minimum size={scale*2.4}cm,inner sep=0] at ({x},{y}) {{}};'
    return ''


def strip(x, y, bits, cell=2.05, h=None, mode='circle'):
    h = h or cell
    out = '\n' + f'\\fill ({x-.32},{y+h/2-.14}) -- ({x-.12},{y+h/2}) -- ({x-.32},{y+h/2+.14}) -- cycle;'
    out += '\n' + f'\\draw[line width=.7pt] ({x},{y}) rectangle ({x+len(bits)*cell},{y+h});'
    for i, b in enumerate(bits):
        if i:
            out += '\n' + f'\\draw[line width=.7pt] ({x+i*cell},{y}) -- ({x+i*cell},{y+h});'
        cx = x+(i+.5)*cell; cy = y+h/2
        if b in '01':
            if mode == 'circle':
                out += '\n' + f'\\draw[line width=.9pt,fill={"black" if b=="1" else "white"}] ({cx},{cy}) circle ({min(cell,h)*.205});'
            else:
                out += '\n' + f'\\node[font=\\ttfamily\\fontsize{{16}}{{18}}\\selectfont] at ({cx},{cy}) {{{b}}};'
    return out


def keyed(x, y, shp, bits, cell=2.05, h=None, mode='circle', small=False):
    """A picture and its row. Grades 2-3 pages (small=True) draw the picture smaller and closer."""
    h = h or cell
    if small:
        return shape(x+.25, y+h/2, shp, .27) + strip(x+.9, y, bits, cell, h, mode)
    return shape(x+.45, y+h/2, shp, .34) + strip(x+1.2, y, bits, cell, h, mode)


def line(x, y, w):
    return '\n' + f'\\draw[gray!50,line width=.35pt] ({x},{y}) -- ({x+w},{y});'


def example(mode='circle'):
    """The practice transmission on page 1: 0101 sent, the third counter turned, 0111 received."""
    out = say(.5, 4.8, 10, 'Sender and changer', 14, 18) + say(11.9, 4.8, 6.5, 'Receiver', 14, 18)
    out += '\n' + r'\draw[gray!60,dashed,line width=1pt] (11,6) -- (11,16);'
    out += '\n' + r'\node[rotate=90,font=\sffamily\fontsize{11}{13}\selectfont,fill=white,inner sep=3pt] at (11,8.5) {folder};'
    out += say(2.5, 6.2, 7, 'Start row', 12, 15)
    out += strip(2.5, 7, '0101', 1.5, 1.5, mode)
    out += '\n' + r'\draw[gray!65,dashed,line width=1pt] (5.5,7) rectangle (7,8.5);'
    out += say(.5, 9.2, 9.7, 'Turn over only the third counter.' if mode == 'circle' else 'Change only the third entry.', 14, 18)
    out += '\n' + r'\draw[->,line width=.9pt] (6.25,8.75) -- (6.25,9.05);'
    out += say(2.5, 10.7, 7, 'Final row', 12, 15)
    out += strip(2.5, 11.5, '0111', 1.5, 1.5, mode)
    out += '\n' + r'\draw[->,line width=1pt] (9,12.25) -- (11.8,12.25);'
    out += strip(12.2, 11.5, '0111', 1.3, 1.5, mode)
    return out
