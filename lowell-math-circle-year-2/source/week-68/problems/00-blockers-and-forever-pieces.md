+++
id = "w68.blockers-and-forever-pieces"
kind = "setup"
title = "Blockers, closed roads and forever pieces"
grades = ["3-5"]
route = ["first", "return"]
+++

## text
Cover dots with counters. A covered dot and every road touching it are closed. Before lifting counters, mark their dots with X. One partner places the blockers; the other traces open routes. Swap jobs between attempts.
\begin{center}
\begin{tikzpicture}[x=.75cm,y=.75cm,font=\small]
\foreach \s in {0,5,10}{\begin{scope}[shift={(\s,0)}]
\ifnum\s=10\draw[line width=1pt] (0,1.5)--(0,0)--(1.5,0);\else\draw[line width=1pt] (0,0) rectangle (1.5,1.5);\fi
\foreach \p in {(0,0),(0,1.5),(1.5,0)}\fill \p circle (2pt);
\ifnum\s<10\fill (1.5,1.5) circle (2pt);\fi
\ifnum\s=5\node[draw,fill=gray!25,minimum size=14pt] at (1.5,1.5){X};\fi
\end{scope}}
\node at (.75,-.65){open};\node at (5.75,-.65){cover one dot};\node at (10.75,-.65){roads left};
\draw[-{Latex}] (2.2,.7)--(4.2,.7);\draw[-{Latex}] (7.2,.7)--(9.2,.7);
\end{tikzpicture}
\end{center}
On the maps below, arrows mean the road pattern keeps going forever. A piece counts as a \textbf{forever piece} only if it keeps going beyond every distance. A trapped finite piece does not count.
