+++
id = "w84.reply-cards"
title = "Reply cards"
grades = ["2-5"]
route = "first"
kind = "setup"
page = "new"
+++

## text
\begin{center}
\begin{tikzpicture}[x=1in,y=1in]
\foreach \row/\word in {0/PROVE BLUE,1/PROVE BLUE,2/PROVE BLUE,3/NOT YET,4/NOT YET,5/NOT YET,6/YES,7/NO}{
 \pgfmathtruncatemacro{\rr}{floor(\row/3)}\pgfmathtruncatemacro{\cc}{mod(\row,3)}
 \pgfmathsetmacro{\xx}{2.45*\cc}\pgfmathsetmacro{\yy}{-2.65*\rr}
 \draw[dashed] (\xx,\yy) rectangle ++(2.18,-2.3);
 \node[align=center,text width=1.9in,font=\large\bfseries] at (\xx+1.09,\yy-1.15) {\word};}
\end{tikzpicture}
\end{center}
