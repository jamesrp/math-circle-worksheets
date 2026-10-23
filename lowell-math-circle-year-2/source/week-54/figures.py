"""Week 54 (Partitions and rebuilding): the canvas page template, carried over unchanged
from the old students.tex (now in archive-before-problem-files-2026-10-23/).

Each page is one overlay picture in inches from the bottom-left corner of the sheet.
The first text section on each page opens it with \\beginpage{<grades>}, which draws the
page's own header (its grade range differs by page), rule, footer and page number;
page_close ends the picture. Prompts are placed by their y position (## prompt @y),
text sections without a position are TikZ code copied as written.
"""

PREAMBLE = r'''\documentclass[letterpaper,12pt]{article}
\usepackage[margin=0.6in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[scaled=0.96]{helvet}
\renewcommand\familydefault{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\pagestyle{empty}
\setlength\parindent{0pt}
\pdfinfo{/Title (Week <<week>>: <<topic>>) /Author (Bellingham Math Circle)}
\definecolor{ink}{gray}{0.12}
\definecolor{rulegray}{gray}{0.66}
\definecolor{gridgray}{gray}{0.84}
\definecolor{squaregray}{gray}{0.94}
\newcommand{\beginpage}[1]{%
  \begin{tikzpicture}[remember picture,overlay,x=1in,y=1in]
  \begin{scope}[shift={(current page.south west)},color=ink]
  \node[anchor=north west,inner sep=0,font=\fontsize{11.5}{14}\selectfont] at (0.6,10.42)
       {Week <<week>> / <<topic>> / Grades #1};
  \draw[rulegray,line width=0.45pt] (0.6,10.12)--(7.9,10.12);
  \node[anchor=south west,inner sep=0,font=\fontsize{9.5}{12}\selectfont] at (0.6,0.35)
       {Bellingham Math Circle / Week 54 / <<footer>>};
  \node[anchor=south east,inner sep=0,font=\fontsize{9.5}{12}\selectfont] at (7.9,0.35) {\thepage};
}
\newcommand{\finishpage}{\end{scope}\end{tikzpicture}\null\newpage}
\newcommand{\lastpage}{\end{scope}\end{tikzpicture}\null}
\newcommand{\textat}[3]{\node[anchor=north west,inner sep=0,text width=7.3in,align=left,font=\fontsize{13.5}{17}\selectfont] at (#1,#2) {#3};}
\newcommand{\labelat}[3]{\node[anchor=north west,inner sep=0,font=\fontsize{11.5}{14}\selectfont] at (#1,#2) {#3};}
\newcommand{\centerlabel}[3]{\node[anchor=north,inner sep=0,font=\fontsize{11.5}{14}\selectfont] at (#1,#2) {#3};}
\newcommand{\problem}[3]{\textat{0.6}{#1}{\textbf{Problem #2:} #3}}
% A strip diagram has a small gap between rows; labels give each strip's size.
\newcommand{\strips}[4]{%
 \foreach \n [count=\r from 0] in {#4}{%
  \pgfmathsetmacro{\yy}{#2-\r*(#3+0.045)}
  \foreach \c in {1,...,\n}{%
   \pgfmathsetmacro{\xx}{#1+(\c-1)*#3}
   \draw[fill=squaregray,line width=0.55pt] (\xx,\yy) rectangle ++(#3,-#3);
  }
  \pgfmathsetmacro{\lx}{#1+\n*#3+0.07}
  \node[anchor=west,inner sep=0,font=\fontsize{10}{11}\selectfont] at (\lx,{\yy-#3/2}) {\n};
 }
}
% A row/column diagram uses touching squares, with equal scale in both axes.
\newcommand{\rows}[4]{%
 \foreach \n [count=\r from 0] in {#4}{%
  \foreach \c in {1,...,\n}{%
   \pgfmathsetmacro{\xx}{#1+(\c-1)*#3}
   \pgfmathsetmacro{\yy}{#2-\r*#3}
   \draw[fill=squaregray,line width=0.55pt] (\xx,\yy) rectangle ++(#3,-#3);
  }
 }
}
\newcommand{\arrowat}[5]{%
 \draw[-{Stealth[length=5pt]},line width=0.7pt] (#1,#3)--(#2,#3);
 \node[anchor=south,inner sep=2pt,font=\fontsize{10.5}{12}\selectfont] at ({(#1+#2)/2},#3) {#4};
 \ifx\relax#5\relax\else\node[anchor=north,inner sep=2pt,font=\fontsize{10.5}{12}\selectfont] at ({(#1+#2)/2},#3) {#5};\fi
}
\newcommand{\cataloggrid}[5]{%
 \draw[rulegray,line width=0.5pt] (#1,#2) rectangle ++(#3,-#4);
 \foreach \i in {1,...,#5}{%
   \pgfmathsetmacro{\yy}{#2-\i*#4/(#5+1)}
   \draw[gridgray,line width=0.4pt] (#1,\yy)--++(#3,0);
 }
}
% Problem 7's answer grids: 5 x 5 cells of 0.22 in, the size of the input squares.
\newcommand{\tinygrid}[2]{%
 \foreach \i in {0,...,5}{%
  \draw[gridgray,line width=0.35pt] ({#1+\i*0.22},#2)--++(0,-1.1);
  \draw[gridgray,line width=0.35pt] (#1,{#2-\i*0.22})--++(1.1,0);
 }
}
\begin{document}

'''
PAGE_OPEN = ''


def page_preamble(week, topic, header, footer):
    return PREAMBLE.replace('<<week>>', str(week)).replace('<<topic>>', topic).replace('<<footer>>', footer)


def page_close(page):
    return '\\lastpage\n'   # = \finishpage without its \newpage, which the layout adds between pages


def page_prompt(n, body, x, y, size):
    return f'\\problem{{{y}}}{{{n}}}{{{body}}}\n'


def page_text(x, y, body, w, size):
    if x is None and y is None:
        return body + '\n'
    return f'\\textat{{{x}}}{{{y}}}{{{body}}}\n'
