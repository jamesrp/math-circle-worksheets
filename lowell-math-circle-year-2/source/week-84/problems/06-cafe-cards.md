+++
id = "w84.cafe-cards"
title = "Café deal cards"
grades = ["2-5"]
route = "first"
kind = "setup"
page = "new"
+++

## text
\begin{center}
\begin{tikzpicture}[x=1in,y=1in]
\foreach \row/\one/\two/\three in {0/YES/YES/YES,1/YES/YES/NO,2/YES/NO/YES,3/YES/NO/NO,4/NO/YES/YES,5/NO/YES/NO,6/NO/NO/YES,7/NO/NO/NO}{
 \pgfmathtruncatemacro{\rr}{floor(\row/2)}\pgfmathtruncatemacro{\cc}{mod(\row,2)}
 \pgfmathsetmacro{\xx}{3.7*\cc}\pgfmathsetmacro{\yy}{-2.12*\rr}
 \draw[dashed] (\xx,\yy) rectangle ++(3.45,-1.85);
 \foreach \i/\word in {1/\one,2/\two,3/\three}{
  \node[font=\small] at ({\xx+0.58+1.13*(\i-1)},\yy-0.5) {\i};
  \node[font=\large\bfseries] at ({\xx+0.58+1.13*(\i-1)},\yy-1.15) {\word};}}
\end{tikzpicture}
\end{center}
