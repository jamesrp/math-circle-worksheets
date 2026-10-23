+++
id = "w82.row-cards"
kind = "setup"
title = "Numbered kid cards"
grades = ["3-5"]
route = ["first", "return"]
page = "new"
+++

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\foreach \row/\letter/\c/\offset in {0/R/queueR/0,1/R/queueR/4,2/R/queueR/8,3/B/queueB/0,4/B/queueB/4,5/B/queueB/8}{
 \foreach \col in {0,1,2,3}{
  \pgfmathtruncatemacro{\n}{\offset+\col+1}
  \draw[dashed,gray] (4.05*\col, -3.1*\row) rectangle ++(3.65,-2.65);
  \node[draw=\c,line width=1pt,rounded corners=3pt,minimum width=3.3cm,minimum height=2.3cm,font=\LARGE] at (4.05*\col+1.825,-3.1*\row-1.325) {\letter\n};
 }
}
\end{tikzpicture}
\end{center}
