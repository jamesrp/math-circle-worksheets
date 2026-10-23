+++
id = "w72.any-memory"
title = "Reach the ring with memory 7, -3, or any integer"
grades = ["4-5"]
route = "return"
page = "new"
kernel = "Repeating a unit loop changes only the memory by 1 or -1, so every integer memory can be reached anywhere."
+++

## prompt
Start at O with memory 0. Reach the ring with memory 7. Then start again and reach it with memory $-3$. You may use any number of E, N, W and S moves. Can you reach the ring with any integer memory (positive, zero or negative)? Explain a plan.

## text
\begin{center}
\begin{tikzpicture}[scale=1.80]
\draw[gray!32,step=1] (-1,-1) grid (4,4);
\foreach\x in{-1,...,4}{\node[below]at(\x,-1){\x};}
\foreach\y in{-1,...,4}{\node[left]at(-1,\y){\y};}
\fill(0,0)circle(2.5pt);\node[above right]at(0,0){O};\draw[line width=1.1pt](2,2)circle(5pt);
\node[below]at(1.5,-1.48){column number};
\end{tikzpicture}
\end{center}
route to memory 7: \hrulefill\par\vspace{.17in}
route to memory $-3$: \hrulefill\par\vspace{.17in}
\lines{3}
