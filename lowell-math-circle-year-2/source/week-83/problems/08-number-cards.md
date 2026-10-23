+++
id = "w83.number-cards"
title = "Number cards"
grades = ["2-5"]
route = "return"
kind = "setup"
page = "new"
+++

## text
\begin{sheet}
\node[anchor=north west,font=\small] at (0,232) {Number cards};
\foreach \num/\day/\col/\row in {0/0/0/0,-1/1/1/0,1/1/2/0,-2/2/3/0,-\frac12/2/0/1,\frac12/2/1/1,2/2/2/1,-3/3/3/1,-\frac32/3/0/2,-\frac34/3/1/2,-\frac14/3/2/2,\frac14/3/3/2,\frac34/3/0/3,\frac32/3/1/3,3/3/2/3}{%
  \pgfmathsetmacro{\cx}{2+44*\col}%
  \pgfmathsetmacro{\cy}{172-37*\row}%
  \draw[dashed,gray!60] (\cx,\cy) rectangle ++(40,24);
  \node[font=\Large] at (\cx+20,\cy+15) {$\num$};
  \node[font=\footnotesize] at (\cx+20,\cy+4) {day \day};
}
\end{sheet}
