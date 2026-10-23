"""Week 55 (Few sums and equal spacing): the canvas page template, carried over unchanged
from the old students.tex (now in archive-before-problem-files-2026-10-23/).

Each page is one 245 x 171 mm TikZ picture in millimetres, y down (\\canvas ... \\finishcanvas);
fancyhdr draws the header, footer and page number. Prompts are placed by their y position
(## prompt @y); text sections without a position are TikZ code copied as written.
"""

PREAMBLE = r'''\documentclass[12pt]{article}
\usepackage[letterpaper,landscape,left=17mm,right=17mm,top=22mm,bottom=18mm,headheight=15pt,headsep=6mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small Week <<week>> / <<topic>> / <<header>>}
\fancyfoot[L]{\footnotesize Bellingham Math Circle / Week 55 / <<footer>>}
\fancyfoot[R]{\footnotesize\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\pdfinfoomitdate=1
\pdftrailerid{}
\newcommand{\canvas}{\begin{tikzpicture}[x=1mm,y=-1mm,>=Stealth, every node/.style={font=\fontsize{12}{15}\selectfont}]\useasboundingbox (0,0) rectangle (245,171);}
\newcommand{\finishcanvas}{\end{tikzpicture}}
\newcommand{\txt}[4]{\node[anchor=north west,inner sep=0,text width=#3mm,align=left] at (#1,#2) {#4};}
\newcommand{\prob}[3]{\txt{0}{#2}{245}{\textbf{Problem #1:} #3}}
\newcommand{\cards}[4]{%
  \node[anchor=east] at (#1-3,#2+7) {#3};%
  \foreach \v [count=\i from 0] in {#4} {%
    \draw[rounded corners=\ifx#3A2mm\else0mm\fi,line width=.6pt] (#1+15*\i,#2) rectangle ++(13,14);%
    \ifx#3B\draw[line width=.35pt] (#1+15*\i+1.2,#2+1.2) rectangle ++(10.6,11.6);\fi
    \node at (#1+15*\i+6.5,#2+7) {\v};%
  }}
\newcommand{\pair}[3]{\cards{9}{#1}{A}{#2}\cards{121}{#1}{B}{#3}}
\newcommand{\lane}[2]{%
  \foreach \i in {0,...,18} {%
    \draw[line width=.4pt] (#1+12*\i,#2) rectangle ++(12,18);%
    \node[font=\fontsize{9}{11}\selectfont] at (#1+12*\i+6,#2+3.6) {\i};%
  }}
\newcommand{\blankpair}[3]{%
  \node[anchor=east] at (6,#1+7) {A};%
  \foreach \i in {1,...,#2} {\draw[rounded corners=2mm,line width=.6pt] (9+15*\i-15,#1) rectangle ++(13,14);}%
  \node[anchor=east] at (118,#1+7) {B};%
  \foreach \i in {1,...,#3} {\draw[line width=.6pt] (121+15*\i-15,#1) rectangle ++(13,14);\draw[line width=.35pt] (122.2+15*\i-15,#1+1.2) rectangle ++(10.6,11.6);}}
\newcommand{\arraygrid}[5]{%
  % x, bottom y, A list (bottom to top), B list (left to right), step mm
  \foreach \a [count=\i from 0] in {#3} {%
    \node[anchor=east,font=\small] at (#1-9,#2-#5*\i) {\a};%
    \foreach \b [count=\j from 0] in {#4} {%
      \pgfmathtruncatemacro{\s}{\a+\b}%
      \ifnum\i>0 \draw[gray!45] (#1+#5*\j,#2-#5*\i) -- ++(0,#5);\fi%
      \ifnum\j>0 \draw[gray!45] (#1+#5*\j,#2-#5*\i) -- ++(-#5,0);\fi%
      \node[draw,fill=white,circle,inner sep=0,minimum size=9mm,line width=.45pt] at (#1+#5*\j,#2-#5*\i) {\s};%
    }}%
  \foreach \b [count=\j from 0] in {#4} {\node[font=\small] at (#1+#5*\j,#2+10) {\b};}%
  \node[anchor=east,font=\small] at (#1-9,#2+10) {A / B};}
\begin{document}
'''
PAGE_OPEN = '\\canvas\n'
PAGE_CLOSE = '\\finishcanvas'


def page_preamble(week, topic, header, footer):
    return PREAMBLE.replace('<<week>>', str(week)).replace('<<topic>>', topic).replace('<<header>>', header).replace('<<footer>>', footer)


def page_prompt(n, body, x, y, size):
    return f'\\prob{{{n}}}{{{y}}}{{{body}}}\n'


def page_text(x, y, body, w, size):
    if x is None and y is None:
        return body + '\n'
    return f'\\txt{{{x if x is not None else 0}}}{{{y}}}{{{w or 245}}}{{{body}}}\n'
