+++
id = "w84.table-labels"
title = "Table areas and doll slots"
grades = ["2-5"]
route = "first"
kind = "setup"
page = "new"
+++

## text
\begin{center}
\begin{tikzpicture}[x=1in,y=1in]
 \draw[dashed] (0,0) rectangle (7.15,-0.85);
 \draw[dashed] (0,-1.25) rectangle (7.15,-2.1);
 \node[font=\Large\bfseries] at (3.575,-0.425) {Shared possibilities};
 \node[font=\Large\bfseries] at (3.575,-1.675) {Publicly ruled out};
 \foreach \i in {1,2,3}{
  \pgfmathsetmacro{\xx}{2.45*(\i-1)}
  \node[font=\large] at (\xx+1.09,-3.05) {Doll \i};
  \draw[rounded corners=3pt] (\xx,-3.4) rectangle ++(2.18,-2.3);}
\end{tikzpicture}
\end{center}
