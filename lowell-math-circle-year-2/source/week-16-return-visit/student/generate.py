from pathlib import Path
from math import sqrt
ROOT = Path(__file__).resolve().parent
H = 3*sqrt(3)/2
PRE = r'''\documentclass[12pt]{article}
\usepackage[letterpaper,margin=0.65in,top=0.8in,headheight=16pt,headsep=17pt,footskip=24pt]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{fancyhdr}
\pagestyle{fancy}\fancyhf{}
\renewcommand{\headrulewidth}{0.35pt}
\fancyfoot[C]{\fontsize{9}{11}\selectfont Bellingham Math Circle / Week 16 / W16-RV-draft / \thepage}
\setlength{\parindent}{0pt}\setlength{\parskip}{9pt}
\newcommand{\header}[1]{\fancyhead[C]{\fontsize{11.5}{14}\selectfont Week 16 / Three-color meshes / #1}}
\newcommand{\problem}[2]{\textbf{Problem #1:} #2\par}
\newcommand{\blankdot}[2]{\draw[fill=white,line width=0.8pt] (#1,#2) circle[radius=0.14in];}
\newcommand{\letterdot}[3]{\draw[fill=white,line width=0.8pt] (#1,#2) circle[radius=0.14in];\node[font=\large] at (#1,#2) {#3};}
\begin{document}\fontsize{14}{17.5}\selectfont
'''
def mesh(scale=1.5):
    pts={(i,j):(i+j/2,j*sqrt(3)/2) for j in range(4) for i in range(4-j)}
    cells=[]
    for j in range(3):
        for i in range(3-j):
            cells.append([(i,j),(i+1,j),(i,j+1)])
            if i+j <= 1:
                cells.append([(i+1,j),(i+1,j+1),(i,j+1)])
    lines=[f'\\begin{{tikzpicture}}[x={scale}in,y={scale}in]']
    for cell in cells:
        xy=['('+','.join(f'{z:.8f}' for z in pts[p])+')' for p in cell]
        lines.append('\\draw[line width=0.6pt] '+'--'.join(xy)+'--cycle;')
    for p,(x,y) in pts.items():
        letter={(0,0):'R',(3,0):'B',(0,3):'Y'}.get(p)
        lines.append(f'\\{"letterdot" if letter else "blankdot"}{{{x:.8f}}}{{{y:.8f}}}'+(f'{{{letter}}}' if letter else ''))
    lines += [r'\node[font=\small,anchor=north] at (1.5,-0.19) {R or B};',
              r'\node[font=\small,rotate=60,anchor=south] at (0.58,1.38) {R or Y};',
              r'\node[font=\small,rotate=-60,anchor=south] at (2.42,1.38) {B or Y};',
              r'\end{tikzpicture}']
    return '\n'.join(lines)
def star():
    return r'''\begin{tikzpicture}[x=1.35in,y=1.35in]
\draw[line width=0.6pt] (0,0)--(3,0)--(1.5,2.59807621)--cycle;
\draw[line width=0.6pt] (0,0)--(1.5,0.86602540)--(3,0);
\draw[line width=0.6pt] (1.5,0.86602540)--(1.5,2.59807621);
\letterdot{0}{0}{R}\letterdot{3}{0}{B}\letterdot{1.5}{2.59807621}{Y}
\blankdot{1.5}{0.86602540}
\end{tikzpicture}'''
def squarepairs():
    out=[r'\begin{tikzpicture}[x=1in,y=1in]']
    for y in (3.0,0):
        for x,diag in ((0,0),(3.2,1)):
            out += [f'\\begin{{scope}}[shift={{({x},{y})}}]',r'\draw[line width=0.65pt] (0,0) rectangle (2.5,2.5);']
            out += [r'\draw[line width=0.65pt] (0,0)--(2.5,2.5);' if diag==0 else r'\draw[line width=0.65pt] (0,2.5)--(2.5,0);']
            for vx,vy in ((0,0),(2.5,0),(2.5,2.5),(0,2.5)):
                out += [f'\\blankdot{{{vx}}}{{{vy}}}']
            out += [r'\end{scope}']
    out += [r'\end{tikzpicture}']
    return '\n'.join(out)
def signs():
    return r'''\begin{tikzpicture}[x=1in,y=1in,font=\small]
\begin{scope}
\draw (0,0)--(1.25,0)--(0.625,1.08253175)--cycle;
\node[anchor=north east] at (0,0) {R};\node[anchor=north west] at (1.25,0) {B};\node[anchor=south] at (0.625,1.08253175) {Y};
\draw[-{Stealth[length=5pt]},line width=0.7pt] (0.24,0.10)--(0.95,0.10);
\draw[-{Stealth[length=5pt]},line width=0.7pt] (1.02,0.20)--(0.69,0.78);
\draw[-{Stealth[length=5pt]},line width=0.7pt] (0.48,0.81)--(0.16,0.23);
\node[anchor=north] at (0.625,-0.32) {R $\to$ B $\to$ Y: $+$};
\end{scope}
\begin{scope}[shift={(2.9,0)}]
\draw (0,0)--(1.25,0)--(0.625,1.08253175)--cycle;
\node[anchor=north east] at (0,0) {R};\node[anchor=north west] at (1.25,0) {Y};\node[anchor=south] at (0.625,1.08253175) {B};
\draw[-{Stealth[length=5pt]},line width=0.7pt] (0.24,0.10)--(0.95,0.10);
\draw[-{Stealth[length=5pt]},line width=0.7pt] (1.02,0.20)--(0.69,0.78);
\draw[-{Stealth[length=5pt]},line width=0.7pt] (0.48,0.81)--(0.16,0.23);
\node[anchor=north] at (0.625,-0.32) {R $\to$ Y $\to$ B: $-$};
\end{scope}
\end{tikzpicture}'''
text = PRE + r'''\header{Grades K--1 and up}
Keep the corner letters. A dot on a side uses one of that side's corner letters.
Inside, use R, B, Y or G. Count only triangles with no lines inside them.

\problem{1}{Which middle letters leave no small triangle with R, B and Y? Find every choice.}
\begin{center}
''' + star() + r'''
\end{center}
\vspace{0.35in}
\rule{\linewidth}{0.35pt}\par\vspace{0.45in}
\rule{\linewidth}{0.35pt}\par\vspace{0.45in}
\rule{\linewidth}{0.35pt}

\newpage\header{Grades 2--3 and up}
\problem{2}{Fill the blank dots so no small triangle has R, B and Y. Among those fillings, how few small triangles can have three different letters?}
\begin{center}
''' + mesh() + r'''
\end{center}
\vspace{0.20in}
\rule{\linewidth}{0.35pt}\par\vspace{0.55in}
\rule{\linewidth}{0.35pt}\par\vspace{0.55in}
\rule{\linewidth}{0.35pt}

\newpage\header{Grades 2--3 and up}
Use only R, B and Y. A rainbow triangle has R, B and Y and no lines inside.

\problem{3}{Label the corners, giving matching corners the same letter on the two squares in each row. Can switching the diagonal change the number of rainbow triangles? Can it change whether that number is even or odd? Find a rule from the outside letters.}
\begin{center}
''' + squarepairs() + r'''
\end{center}
\vspace{0.15in}\rule{\linewidth}{0.35pt}

\newpage\header{Grades 4--5}
Use only R, B and Y. Keep the corner letters and side choices shown.
A rainbow triangle has R, B and Y and no lines inside. Read it counterclockwise,
starting at R. Mark it $+$ or $-$ as shown.
\begin{center}
''' + signs() + r'''
\end{center}
\problem{4}{Fill the blank dots and mark the rainbow triangles. What can change between fillings, and what stays the same about the two totals?}
\begin{center}
''' + mesh(1.4) + r'''
\end{center}
\begin{center}
\begin{tabular}{p{2in}p{2in}}
$+$ total: \hrulefill & $-$ total: \hrulefill \\[13pt]
$+$ total: \hrulefill & $-$ total: \hrulefill \\[13pt]
$+$ total: \hrulefill & $-$ total: \hrulefill
\end{tabular}
\end{center}
\end{document}
'''
(ROOT/'return-visit.tex').write_text(text)
