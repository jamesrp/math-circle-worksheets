+++
id = "w67.cube-labels"
kind = "setup"
title = "Three-digit labels: a road changes one digit"
grades = ["3-5"]
route = "return"
page = "new"
+++

## text
A road changes exactly one digit. Crossed roads connect only at a labeled dot.
\begin{center}
\begin{tikzpicture}[font=\small]
\node[draw,circle] (a) at (0,0){001};\node[draw,circle] (b) at (4,0){101};\node[draw,circle] (c) at (8,0){100};
\draw[-{Latex}] (a)--node[above]{change first digit}(b);
\draw[-{Latex}] (b)--node[above]{change last digit}(c);
\end{tikzpicture}
\end{center}
