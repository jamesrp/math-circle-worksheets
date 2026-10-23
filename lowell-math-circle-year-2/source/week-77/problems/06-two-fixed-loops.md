+++
id = "w77.two-fixed-loops"
title = "Two loops that can disappear in either order"
grades = ["4-5"]
route = "return"
page = "new"
kernel = "Loops equal on the current board can be separated on a fresh one exactly when neither needs only some of the other's tiles."
+++

## text
\promptat{0}

## prompt
Start with all eight edges and filled triangles ABO and BCO. Save two loops with different sets of edges. Both must survive now and first disappear at the last filling, whichever of the two unfilled triangles your partner fills first.

## text
\begin{scope}[shift={(9.5,4.15)}]
 \coordinate (A) at (0,0);\coordinate (B) at (8,0);\coordinate (C) at (8,8);\coordinate (D) at (0,8);\coordinate (O) at (4,4);
 \draw[line width=1.5pt] (A)--(B)--(C)--(D)--cycle (A)--(O)--(C) (B)--(O)--(D);
 \foreach \v/\pos in {A/above left,B/above right,C/below right,D/below left}{\fill (\v) circle(2.2pt);\node[\pos,inner sep=4pt,font=\large] at (\v) {\v};}
 \fill (O) circle(2.2pt);\node[above,fill=white,inner sep=2pt,font=\large] at (4,3.7) {O};
\end{scope}
\smallat{0}{4.15}{8.3}{First saved loop:}
\lineat{0}{5.35}{8.3}\lineat{0}{6.65}{8.3}
\smallat{0}{8.55}{8.3}{Second saved loop:}
\lineat{0}{9.75}{8.3}\lineat{0}{11.05}{8.3}
\textat{0}{13.65}{18.2}{Can you choose your pair so that either loop can disappear first on a fresh board with all eight edges and no filled triangles? Keep the two saved edge lists unchanged. Fill all four triangles, one at a time. Show a filling order for each outcome, or explain why it is impossible.}
\smallat{0}{17.4}{18.2}{First saved loop disappears first:}
\lineat{0}{18.65}{18.2}
\smallat{0}{20.0}{18.2}{Second saved loop disappears first:}
\lineat{0}{21.25}{18.2}
