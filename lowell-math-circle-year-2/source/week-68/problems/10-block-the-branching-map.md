+++
id = "w68.block-the-branching-map"
title = "Blocking the branching map"
grades = ["3-5"]
route = "first"
kernel = "Blocking the centre and then each ring doubles the forever pieces: 3, 6, 12."
+++

## prompt
Cover the center dot. Next cover all dots one road from the center too. Next cover all dots two roads from the center too. Count the separate forever pieces each time.

## text
\begin{center}
\begin{tikzpicture}[x=1.25cm,y=1.25cm]
\coordinate (o) at (0,0);\node[above left=3pt,font=\small] at (o){center};
\foreach \a in {90,210,330}{
\coordinate (a\a) at (\a:1.4);\draw[line width=.9pt] (o)--(a\a);\fill (a\a) circle (2.5pt);
\foreach \b in {-25,25}{\pgfmathsetmacro{\ab}{\a+\b}
\coordinate (b\a\b) at (\ab:2.9);\draw[line width=.9pt] (a\a)--(b\a\b);\fill (b\a\b) circle (2.5pt);
\foreach \c in {-12,12}{\pgfmathsetmacro{\abc}{\ab+\c}
\coordinate (c\a\b\c) at (\abc:4.25);\draw[line width=.9pt] (b\a\b)--(c\a\b\c);\fill (c\a\b\c) circle (2.5pt);
\foreach \d in {-5,5}{\pgfmathsetmacro{\abcd}{\abc+\d}\draw[-{Latex},line width=.9pt] (c\a\b\c)--(\abcd:5.0);}
}}}\fill (o) circle (3pt);
\end{tikzpicture}
\end{center}
Center only: \rule{.6in}{.4pt}\hfill Through 1 road: \rule{.6in}{.4pt}\hfill Through 2 roads: \rule{.6in}{.4pt}
