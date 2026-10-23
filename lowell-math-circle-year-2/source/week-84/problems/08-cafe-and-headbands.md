+++
id = "w84.cafe-and-headbands"
title = "Café cards and headbands"
grades = ["2-5"]
route = "first"
kind = "setup"
page = "new"
+++

## text
\begin{center}
\begin{tikzpicture}[x=1in,y=1in]
\foreach \row/\word in {0/YES,1/YES,2/YES,3/NO,4/NO,5/NO,6/B,7/B,8/B,9/R,10/R,11/R}{
 \pgfmathtruncatemacro{\rr}{floor(\row/3)}\pgfmathtruncatemacro{\cc}{mod(\row,3)}
 \pgfmathsetmacro{\xx}{2.45*\cc}\pgfmathsetmacro{\yy}{-2.12*\rr}
 \draw[dashed] (\xx,\yy) rectangle ++(2.18,-1.85);
 \ifnum\row<6\node[font=\Huge\bfseries] at (\xx+1.09,\yy-0.93) {\word};
 \else\ifnum\row<9\fill[hatblue] (\xx+1.09,\yy-0.76) circle (0.46);\node[text=white,font=\Huge\bfseries] at (\xx+1.09,\yy-0.76) {B};\node[font=\small] at (\xx+1.09,\yy-1.46) {BLUE};
 \else\fill[hatred] (\xx+1.09,\yy-0.76) circle (0.46);\node[text=white,font=\Huge\bfseries] at (\xx+1.09,\yy-0.76) {R};\node[font=\small] at (\xx+1.09,\yy-1.46) {RED};\fi\fi}
\end{tikzpicture}
\end{center}
