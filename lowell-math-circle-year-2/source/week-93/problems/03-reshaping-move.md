+++
id = "w93.reshaping-move"
title = "The reshaping move"
grades = ["3-5"]
route = "first"
kind = "setup"
page = "new"
+++

## text
A reshaping move keeps the area: average the two sides, then divide the area by that average to get the other new side.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,>=stealth]
\draw[thick,fill=gray!8] (0,0) rectangle (3,1);
\node[below] at (1.5,0) {3};\node[left] at (0,.5) {1};
\node[above] at (1.5,1) {area 3};
\draw[->,thick] (3.4,.5)--(4.1,.5);
\draw[very thick] (4.5,.95)--(5.5,.95);
\draw[very thick,gray] (5.5,.95)--(8.5,.95);
\foreach \x in {4.5,5.5,8.5} \draw (\x,.82)--(\x,1.08);
\node[above] at (5,1.08) {1};\node[above] at (7,1.08) {3};
\draw[<->] (4.5,.4)--(6.5,.4);
\node[below] at (5.5,.4) {$\frac{1+3}{2}=2$};
\draw[->,thick] (8.9,.5)--(9.6,.5);
\draw[thick,fill=gray!8] (10,0) rectangle (12,1.5);
\node[below] at (11,0) {2};\node[right] at (12,.75) {$3\div2=\frac32$};
\node[above] at (11,1.5) {area 3};
\end{tikzpicture}
\end{center}

Write each side length exactly, using fractions when needed.
