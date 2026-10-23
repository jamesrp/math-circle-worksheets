+++
id = "w69.the-gap"
kind = "setup"
title = "The gap of a dot on a side"
grades = ["4-5"]
route = ["first", "return"]
page = "new"
+++

## text
For a dot on one colored side, its \textbf{gap} is the fewest road steps needed to reach either of the other two colored sides. Use any road on the map, including uncolored roads. A dot already on another side has gap 0.
\begin{center}
\begin{tikzpicture}[x=.75cm,y=.75cm,font=\small]
\draw[gray!60,step=1] (0,0) grid (3,2);\foreach \x in {0,1,2,3}\foreach \y in {0,1,2}\fill (\x,\y) circle (1.5pt);
\draw[red!75!black,line width=2.2pt] (0,0)--(3,0);
\draw[blue!75!black,line width=2.2pt,dashed] (3,0)--(3,2);
\draw[green!40!black,line width=2.2pt,densely dotted] (3,2)--(0,2)--(0,0);
\home{0}{0}{A}\home{3}{0}{B}\home{3}{2}{C}\home{1}{0}{P}
\node[anchor=west,align=left] at (4,1){P is on the red side AB.\\To green CA: 1 step left.\\To blue BC: 2 steps right.\\The smaller distance is 1: gap 1.};
\end{tikzpicture}
\end{center}
