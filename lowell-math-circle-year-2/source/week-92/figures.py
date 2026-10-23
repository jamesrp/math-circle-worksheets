"""Week 92 page template for the problem files.

The preamble and drawing macros are the previous students.tex, unchanged. Each page
is one TikZ canvas (\\canvas ... \\finishcanvas); a prompt is a \\prob node and a
text section a \\txt node at the y position given in its heading (millimetres, y
down from the top of the canvas). Figure sections are the old TikZ code, verbatim.
The packet is shared by two grade ranges: band(...) at the top of a page sets the
range its header prints.
"""

PREAMBLE = r'''\documentclass[11pt]{article}
\usepackage[letterpaper,left=18mm,right=18mm,top=20mm,bottom=18mm,headheight=14pt]{geometry}
\usepackage{tikz,xcolor,fancyhdr,lmodern}
\usetikzlibrary{arrows.meta,decorations.pathreplacing}
\renewcommand{\familydefault}{\sfdefault}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0.4pt}
\newcommand{\bandname}{Grades 2--3}
\fancyhead[L]{\small Week 92 / Fold-and-stretch predictions / \bandname}
\fancyfoot[L]{\scriptsize Bellingham Math Circle / Week 92 / <<footer>>}
\fancyfoot[R]{\scriptsize\thepage}
\setlength{\parindent}{0pt}\setlength{\parskip}{0pt}
\pdfinfo{/Title (Week 92 - Fold-and-stretch predictions) /Author (Bellingham Math Circle) /CreationDate (D:20261023000000Z) /ModDate (D:20261023000000Z)}
\pdftrailerid{<92A113BA84D2123FF010701001010101><92A113BA84D2123FF010701001010101>}
\definecolor{ink}{HTML}{203642}\definecolor{bandfill}{HTML}{B8D9E6}
\tikzset{every node/.style={font=\sffamily\small,text=ink},arr/.style={-{Stealth[length=2mm]},thick,draw=ink}}
\newcommand{\txt}[3]{\node[anchor=north west,align=left,text width=174mm,inner sep=0] at (0,#1) {#2#3};}
\newcommand{\prob}[3]{\txt{#1}{\textbf{Problem #2:} }{#3}}
\newcommand{\track}[2]{\begin{scope}[shift={(8,#1)}]\draw[ink] (0,0)--(160,0);\foreach \i in {0,...,16}{\draw[ink] (10*\i,-1.5)--(10*\i,1.5);\node[font=\scriptsize,anchor=north] at (10*\i,-2){\i};}\node[anchor=south west,font=\scriptsize] at (0,3){#2};\end{scope}}
\newcommand{\range}[3]{\fill[fill=bandfill,fill opacity=0.55] (8+10*#2,#1-1.3) rectangle (8+10*#3,#1+1.3);\fill[ink] (8+10*#2,#1) circle(0.7);\fill[ink] (8+10*#3,#1) circle(0.7);}
\newcommand{\point}[2]{\fill[ink] (8+10*#2,#1) circle(1.25);}
\newcommand{\canvas}{\begin{tikzpicture}[x=1mm,y=1mm]\path[use as bounding box] (0,-231) rectangle (178,0);}
\newcommand{\finishcanvas}{\end{tikzpicture}}

% Reusable continuous mapping aid: horizontal input, right distance, left output.
% The paired vertical scales encode the complete doubling operation.
\newcommand{\movemap}[2]{
\begin{scope}[shift={(12,#1)}]
\draw[ink] (0,0)--(160,0);
\foreach \i in {0,...,16}{\draw[ink] (10*\i,-1)--(10*\i,1);\node[font=\scriptsize,anchor=north] at (10*\i,-2){\i};}
\foreach \i in {0,...,8}{
\draw[gray!20] (0,2*#2*\i)--(160,2*#2*\i);
\draw[ink] (-1,2*#2*\i)--(1,2*#2*\i);
\node[font=\scriptsize,anchor=east] at (-2,2*#2*\i){\pgfmathparse{int(2*\i)}\pgfmathresult};
\draw[ink] (159,2*#2*\i)--(161,2*#2*\i);
\node[font=\scriptsize,anchor=west] at (162,2*#2*\i){\i};}
\draw[ink] (0,0)--(0,16*#2);\draw[ink] (160,0)--(160,16*#2);
\draw[ink,very thick] (0,0)--(80,16*#2)--(160,0);
\node[anchor=south west,font=\scriptsize] at (-10,16*#2+3){Output};
\node[anchor=south east,font=\scriptsize] at (165,16*#2+3){Nearer-end distance};
\node[anchor=north,font=\scriptsize] at (80,-8){Input};
\end{scope}}
\begin{document}
'''


def page_preamble(week, topic, header, footer):
    return PREAMBLE.replace('<<footer>>', footer)


def page_open(page):
    return '\\canvas\n'


def page_close(page):
    return '\\finishcanvas\n'


def page_prompt(n, body, x, y, size):
    return f'\\prob{{{y}}}{{{n}}}{{{body}}}\n'


def page_text(x, y, body, w, size):
    return f'\\txt{{{y}}}{{}}{{{body}}}\n'


def band(header):
    """The grade range printed in the header of this page and the pages after it."""
    return f'\\gdef\\bandname{{{header}}}\n'
