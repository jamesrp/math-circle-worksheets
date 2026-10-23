"""Week 17 figures and canvas page template, carried over from the old student builder
(archive-before-problem-files-2026-10-23/build_packets.py).

Coordinates are inches from the top-left corner of the paper, y down: each page is one
overlay picture anchored at the page's north-west corner, as the old builder drew it,
with its own header, rule, footer and page number. The old builder's Packet methods are
the functions below; each returns LaTeX instead of appending it. Problem files call them
in their `figure` sections; the wording lives in the problem files.

A text section's line spacing is the old builder's: TEXT_LEADING gives it for the sizes
the pages use, and other sizes take 1.25 times the size.
"""

PRE = r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=0in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{tikz}
\usepackage{amssymb,amsmath}
\pdfmapfile{+lm.map}
\pdfmapfile{+symbols.map}
\usetikzlibrary{arrows.meta}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\renewcommand{\familydefault}{\sfdefault}
\definecolor{cardred}{RGB}{203,45,45}
\definecolor{cardblue}{RGB}{34,95,176}
\tikzset{state/.style={circle,draw=black,line width=1.1pt,minimum size=.66in,inner sep=0pt,font=\sffamily\bfseries\fontsize{13}{14}\selectfont},edge/.style={-{Stealth[length=7pt,width=5pt]},line width=1.15pt},lab/.style={fill=white,inner sep=2pt,font=\sffamily\bfseries\fontsize{12}{13}\selectfont}}
\newcommand{\R}{\tikz[baseline=-.045in,x=1in,y=1in]{\node[draw=cardred,fill=cardred!10,rectangle,minimum size=.23in,inner sep=0pt,line width=.85pt,text=black,font=\sffamily\bfseries\fontsize{11}{12}\selectfont] {R};}}
\newcommand{\B}{\tikz[baseline=-.045in,x=1in,y=1in]{\node[draw=cardblue,fill=cardblue!10,circle,minimum size=.23in,inner sep=0pt,line width=.85pt,text=black,font=\sffamily\bfseries\fontsize{11}{12}\selectfont] {B};}}
\newcommand{\Y}{$\checkmark$}
\newcommand{\N}{$\times$}
\begin{document}
'''

TEXT_LEADING = {12.5: 16, 12: 15, 11.5: 14}


def page_preamble(week, topic, header, footer):
    return PRE


def page_open(page):
    return (r'\begin{tikzpicture}[remember picture,overlay,x=1in,y=-1in,shift={(current page.north west)}]' + '\n'
            + text(.6, .34, 7.3, rf'Week {page.week} / {page.topic} / {page.header}', 11, 13)
            + r'\draw[line width=.45pt] (.6,.66)--(7.9,.66);' + '\n'
            + text(.6, 10.49, 6.8, f'Bellingham Math Circle / Week {page.week} / {page.footer}', 9, 11)
            + text(7.55, 10.49, .35, str(page.number), 9, 11))


def page_close(page):
    return '\\end{tikzpicture}\\null' + ('\n' if page.number == page.count else '')


def _size(size):
    return int(size) if float(size).is_integer() else size


def page_prompt(n, body, x, y, size):
    return text(.65, .96 if y is None else y, 7.2, rf'\textbf{{Problem {n}:}} {body}', _size(size or 15))


def page_text(x, y, body, w, size):
    size = _size(size or 14)
    return text(x, y, w, body, size, TEXT_LEADING.get(size))


def text(x, y, w, s, size=14, leading=None):
    leading = leading or size*1.25
    return rf'\node[anchor=north west,inner sep=0pt,align=left,text width={w}in,font=\sffamily\fontsize{{{size}}}{{{leading}}}\selectfont] at ({x},{y}) {{{s}}};'+'\n'


def line(x, y, w):
    return rf'\draw[black!38,line width=.45pt] ({x},{y})--({x+w},{y});'+'\n'


def lines(x, ys, w):
    return ''.join(line(x, y, w) for y in ys)


def cards(word, x, y, step=.35, size=.28):
    if not word:
        return text(x, y-.14, 1.2, 'no cards', 12, 14)
    out = ''
    for j, c in enumerate(word):
        shape = 'rectangle' if c == 'R' else 'circle'; color = 'cardred' if c == 'R' else 'cardblue'
        out += rf'\node[draw={color},fill={color}!10,{shape},minimum size={size}in,inner sep=0pt,line width=.9pt,font=\bfseries\fontsize{{12}}{{13}}\selectfont] at ({x+j*step},{y}) {{{c}}};'+'\n'
    return out


def blank_cards(x, y, n=6, size=.42, step=.54):
    return ''.join(rf'\draw[black!35,line width=.6pt,rounded corners=1.5pt] ({x+j*step-size/2},{y-size/2}) rectangle ++({size},{size});'+'\n' for j in range(n))


def choices(x, y):
    return rf'\node[font=\fontsize{{22}}{{24}}\selectfont] at ({x},{y}) {{\Y}};\node[font=\fontsize{{22}}{{24}}\selectfont] at ({x+.65},{y}) {{\N}};'+'\n'


def state(name, x, y, answer, k=False, blank=False, label=None):
    a = '' if blank else ((r'\Y' if answer else r'\N') if k else ('YES' if answer else 'NO'))
    if label: a = rf'\shortstack{{{{\fontsize{{9}}{{10}}\selectfont {label}}}\\{a}}}'
    return rf'\node[state] ({name}) at ({x},{y}) {{{a}}};'+'\n'


def start_arrow(x, name, y):
    return rf'\draw[edge] ({x},{y})--({name}.west);'+'\n'


def two(kind, x1, x2, y, k=False, prefix='s', labels=False):
    # even: red toggles and blue loops. lastR/lastB: each symbol sets the current answer.
    if kind == 'even': answers = [True, False]; forward = 'R'; backward = 'R'; loops = ['B', 'B']
    elif kind == 'lastR': answers = [False, True]; forward = 'R'; backward = 'B'; loops = ['B', 'R']
    elif kind == 'lastB': answers = [False, True]; forward = 'B'; backward = 'R'; loops = ['R', 'B']
    out = ''
    for i, (x, a) in enumerate(zip([x1, x2], answers)): out += state(prefix+str(i), x, y, a, k, label=str(i+1) if labels else None)
    out += rf'\draw[edge] ({x1-.95},{y})--({prefix}0.west);'+'\n'
    for i, l in enumerate(loops): out += rf'\draw[edge] ({prefix}{i}) edge[loop above,min distance=.57in] node[lab] {{\{l}}} ({prefix}{i});'+'\n'
    out += rf'\draw[edge] ({prefix}0) to[bend left=24] node[lab,above] {{\{forward}}} ({prefix}1);'+'\n'
    out += rf'\draw[edge] ({prefix}1) to[bend left=24] node[lab,below] {{\{backward}}} ({prefix}0);'+'\n'
    return out


def three(y, k=False, prefix='t', xs=(2.0, 4.25, 6.5), labels=False):
    out = ''
    for i, x in enumerate(xs): out += state(prefix+str(i), x, y, i == 0, k, label=str(i+1) if labels else None)
    out += rf'\draw[edge] ({xs[0]-.95},{y})--({prefix}0.west);'+'\n'
    for i in range(3): out += rf'\draw[edge] ({prefix}{i}) edge[loop above,min distance=.56in] node[lab] {{\B}} ({prefix}{i});'+'\n'
    for i in range(2): out += rf'\draw[edge] ({prefix}{i})--node[lab,above] {{\R}} ({prefix}{i+1});'+'\n'
    out += rf'\draw[edge] ({prefix}2.south) .. controls ({xs[2]},{y+1.03}) and ({xs[0]},{y+1.03}) .. node[lab,below] {{\R}} ({prefix}0.south);'+'\n'
    return out


def pair(a, b, y, k=False):
    out = ''
    if k:
        out += rf'\draw[black!45,line width=.6pt] (.8,{y-.22})--(.72,{y-.22})--(.72,{y+.72})--(.8,{y+.72});'+'\n'
        for word, yy in [(a, y), (b, y+.48)]:
            out += cards(word, 1.25, yy)
            out += text(3.25, yy-.13, .3, '+', 18, 19)
            out += line(3.75, yy+.15, 2.65)
            out += choices(7.03, yy)
    else:
        for word, x in [(a, .9), (b, 4.5)]:
            out += cards(word, x, y, step=.31, size=.25)
            out += text(x+1.35, y-.13, .25, '+', 15, 16)
            out += line(x+1.75, y+.12, 1.3)
            out += text(x+1.7, y+.3, 1.5, 'YES / NO', 10.5, 12)
        out += line(.9, y+.85, 6.8)
    return out


def pairs(rows, k=False):
    return ''.join(pair(a, b, y, k) for a, b, y in rows)


def answer_rows(rows, ys):
    return ''.join(cards(row, 1.45, y, step=.4, size=.31) + choices(6.75, y) for row, y in zip(rows, ys))


def blank_rows(xs, ys, n, size, step):
    return ''.join(blank_cards(x, y, n, size, step) for y in ys for x in xs)
