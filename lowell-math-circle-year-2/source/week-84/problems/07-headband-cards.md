+++
id = "w84.headband-cards"
title = "Headband possibility cards"
grades = ["2-5"]
route = "first"
kind = "setup"
page = "new"
+++

## text
\begin{center}
\begin{tikzpicture}[x=1in,y=1in]
\foreach \row/\one/\two/\three in {0/1/1/1,1/1/1/0,2/1/0/1,3/1/0/0,4/0/1/1,5/0/1/0,6/0/0/1,7/0/0/0}{
 \pgfmathtruncatemacro{\rr}{floor(\row/2)}\pgfmathtruncatemacro{\cc}{mod(\row,2)}
 \pgfmathsetmacro{\xx}{3.7*\cc}\pgfmathsetmacro{\yy}{-2.12*\rr}
 \draw[dashed] (\xx,\yy) rectangle ++(3.45,-1.85);
 \foreach \i/\val in {1/\one,2/\two,3/\three}{
  \node[font=\small] at ({\xx+0.58+1.13*(\i-1)},\yy-0.5) {\i};
  \ifnum\val=1\fill[hatblue] ({\xx+0.58+1.13*(\i-1)},\yy-1.15) circle (0.28);\node[text=white,font=\Large\bfseries] at ({\xx+0.58+1.13*(\i-1)},\yy-1.15) {B};
  \else\fill[hatred] ({\xx+0.58+1.13*(\i-1)},\yy-1.15) circle (0.28);\node[text=white,font=\Large\bfseries] at ({\xx+0.58+1.13*(\i-1)},\yy-1.15) {R};\fi}}
\end{tikzpicture}
\end{center}
