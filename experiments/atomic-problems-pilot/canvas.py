"""House drawing primitives for fixed-canvas pages (from Week 50's draw.py).

A canvas page is one TikZ picture, 185 x 235 mm, with y pointing down.
"""
BS = chr(92)


def text(x, y, s, w=180, size=13):
    return rf'\node[anchor=north west,inner sep=0pt,text width={w}mm,font=\fontsize{{{size}}}{{{size+3}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'


def label(x, y, s, size=11, anchor='center'):
    return rf'\node[anchor={anchor},inner sep=1pt,font=\fontsize{{{size}}}{{{size+2}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'


def line(x, y, X, Y, opts=''):
    return rf'\draw[{opts}] ({x},{y}) -- ({X},{Y});'+'\n'


def rect(x, y, w, h, opts=''):
    return rf'\draw[{opts}] ({x},{y}) rectangle ++({w},{h});'+'\n'


def circle(x, y, r=2, opts=''):
    return rf'\draw[{opts}] ({x},{y}) circle ({r});'+'\n'


def prob(n, s, y=0, size=13):
    return text(0, y, rf'\textbf{{Problem {n}:}} '+s, size=size)


PAGE_OPEN = '\\noindent\\begin{tikzpicture}[x=1mm,y=-1mm,line width=.5pt]\n\\path[use as bounding box] (0,0) rectangle (185,235);\n'
PAGE_CLOSE = '\\end{tikzpicture}\n'


def student_preamble(week, topic, header_band, footer_id):
    return rf'''\documentclass[letterpaper,12pt]{{article}}
\usepackage[margin=14mm,top=18mm,bottom=17mm,headheight=14pt]{{geometry}}
\pdfmapfile{{+cm.map}}\pdfmapfile{{+cmextra.map}}
\usepackage{{tikz,fancyhdr,amsmath,amssymb}}
\usetikzlibrary{{arrows.meta,patterns}}
\pagestyle{{fancy}}\fancyhf{{}}\renewcommand{{\headrulewidth}}{{0pt}}
\fancyhead[L]{{\small Week {week} / {topic} / {header_band}}}
\fancyfoot[L]{{\small Bellingham Math Circle / Week {week} / {footer_id}}}
\fancyfoot[R]{{\small\thepage}}
\setlength{{\parindent}}{{0pt}}\setlength{{\parskip}}{{0pt}}
\begin{{document}}
'''
