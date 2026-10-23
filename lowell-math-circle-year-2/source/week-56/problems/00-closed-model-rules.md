+++
id = "w56.closed-model-rules"
title = "Closed models: faces, edges and vertices"
kind = "setup"
grades = ["shared"]
route = ["first", "return"]
+++

## text
Use closed models with all their faces attached. A vertex is a corner of the assembled solid; an edge is shared by two faces. Count each assembled edge and vertex once. Tabs and glue overlaps do not count.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
 \draw[fill=blue!8] (0,0) rectangle (1.1,1.1);
 \draw[fill=blue!16] (1.45,0) rectangle (2.55,1.1);
 \draw[very thick] (1.1,0)--(1.1,1.1) (1.45,0)--(1.45,1.1);
 \node at (1.25,-.4) {two face sides};
 \draw[-{Latex}] (2.9,.55)--(3.5,.55);
 \draw[fill=blue!8] (3.9,0) rectangle (5,1.1);
 \draw[fill=blue!16] (5,0)--(5.8,.4)--(5.8,1.5)--(5,1.1)--cycle;
 \draw[very thick] (5,0)--(5,1.1);
 \node at (4.85,-.4) {one shared edge};
 \draw[-{Latex}] (6.25,.55)--(6.85,.55);
 \begin{scope}[shift={(8,.35)}]
  \fill[blue!8] (0,0)--(-.95,0)--(-.95,.9)--(0,.9)--cycle;
  \fill[blue!16] (0,0)--(.75,.4)--(.75,1.3)--(0,.9)--cycle;
  \fill[blue!25] (0,.9)--(-.95,.9)--(-.2,1.3)--(.75,1.3)--cycle;
  \draw (0,0)--(-.95,0)--(-.95,.9)--(-.2,1.3)--(.75,1.3)--(.75,.4)--cycle;
  \draw (-.95,.9)--(0,.9)--(.75,1.3) (0,0)--(0,.9);
  \fill (0,.9) circle (2pt);
 \end{scope}
 \node[align=center] at (8,-.4) {three face corners\\one assembled vertex};
\end{tikzpicture}
\end{center}
