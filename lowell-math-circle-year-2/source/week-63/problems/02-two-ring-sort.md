+++
id = "w63.two-ring-sort"
title = "Two overlapping groups of six outcomes"
grades = ["shared"]
route = "first"
page = "new"
kernel = 'The A-home and B-home groups share ABC, so the rows outside both number $6-2-2+1=3$.'
+++

## text
\renewcommand{\band}{Grades 2--5}
One outcome card is one whole placement. It can belong to several groups at once. Group the outcome cards on the table.

\begin{center}\begin{tikzpicture}[x=1mm,y=1mm]
  \node[font=\small] at (28,35) {Whole outcome card};
  \draw[thin] (0,0) rectangle (56,27);
  \foreach \h [count=\i from 0] in {U,V,W,X}{%
    \node[font=\scriptsize] at ({10+\i*9+4.5},21) {\h};
    \draw[thin] ({10+\i*9},7) rectangle ++(9,10);
  }
  \foreach \c [count=\i from 0] in {V,U,W,X}{%
    \node[font=\normalsize\bfseries] at ({10+\i*9+4.5},12) {\c};
  }
  \node[font=\scriptsize] at (28,3) {VUWX};
  \node[font=\small,align=center] at (97,35) {Check the same row};
  \draw[thin] (73,15) rectangle (121,25);
  \draw[thin] (73,1) rectangle (121,11);
  \node[font=\small] at (97,20) {W in home W: yes};
  \node[font=\small] at (97,6) {X in home X: yes};
  \draw[-{Stealth[length=2mm]}] (56,20)--(73,20);
  \draw[-{Stealth[length=2mm]}] (56,6)--(73,6);
  \draw[-{Stealth[length=2mm]}] (124,13)--(133,13);
  \node[font=\small] at (154,35) {Record memberships};
  \node[font=\large] at (154,23) {VUWX};
  \node[font=\small,align=center] at (154,10) {W-home and\\X-home groups};
\end{tikzpicture}\end{center}

## prompt
Use the six A--C outcome cards. Make one group with A in home A and another with B in home B. A card may belong to both groups. How many rows are outside both groups? C may stay home.

## text
A student counts $6-2-2=2$. Repair this count and show what went wrong.

\vspace{4mm}
\begin{center}\begin{tikzpicture}[x=1mm,y=1mm]
  \draw[rounded corners=3mm,thin] (0,0) rectangle (173,70);
\end{tikzpicture}\end{center}
\vspace{7mm}
\worklines{3}
