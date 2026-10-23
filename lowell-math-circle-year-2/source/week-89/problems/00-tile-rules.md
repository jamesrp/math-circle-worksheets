+++
id = "w89.tile-rules"
kind = "setup"
title = "Tile rules and a growth example"
grades = ["K-5"]
route = "first"
+++

## text
Use square tiles on the large boards or the tabletop. Build one picture at a time. Keep the old tiles in place when you grow a shape.

\begin{center}\begin{tikzpicture}[x=7mm,y=7mm]
\foreach \x in {0,1}{\foreach \y in {0,1}{\tile{\x}{\y}{white}}}
\node[below] at (1,-.2){old shape};
\draw[-{Latex}] (2.6,.7)--(3.5,.7);
\foreach \x in {4,5}{\foreach \y in {0,1}{\tile{\x}{\y}{white}}}
\tile{6}{0}{black!25}\tile{6}{1}{black!25}
\node[below] at (5.5,-.2){add shaded tiles};
\draw[-{Latex}] (7.5,.7)--(8.4,.7);
\foreach \x in {9,10,11}{\foreach \y in {0,1}{\tile{\x}{\y}{white}}}
\node[below] at (10.5,-.2){new shape};
\end{tikzpicture}\end{center}
