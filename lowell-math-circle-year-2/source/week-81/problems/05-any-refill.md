+++
id = "w81.any-refill"
kind = "setup"
title = "Any finite refill"
grades = ["2-5"]
route = "return"
page = "new"
+++

## text
\renewcommand{\band}{Grades 4--5}
For Problems 4--5, a refill may be any finite number of counters. It still goes only to buckets strictly to the left of the bucket you took from.

When playing, you may write a number to stand for that many counters.
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
 \foreach \i in {0,...,11}{
  \pgfmathsetmacro{\xx}{mod(\i,4)*.44}
  \pgfmathsetmacro{\yy}{floor(\i/4)*.43}
  \node[fish] at (\xx,\yy) {};
 }
 \draw[arrow] (2.05,.43)--(3.05,.43);
 \draw (3.4,-.25) rectangle (5.65,1.25);
 \node[font=\large] at (4.525,.68) {12};
 \node[font=\small] at (4.525,.13) {counters};
 \draw[arrow] (6.1,.43)--(7.1,.43);
 \node[font=\small] at (6.6,1.05) {remove 1};
 \draw (7.45,-.25) rectangle (9.7,1.25);
 \node[font=\large] at (8.575,.68) {11};
 \node[font=\small] at (8.575,.13) {counters};
\end{tikzpicture}
\end{center}
