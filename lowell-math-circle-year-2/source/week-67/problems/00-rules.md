+++
id = "w67.rules"
kind = "setup"
title = "Roads, shortest routes and meeting dots, with the P-M-Q example"
grades = ["3-5"]
route = ["first", "return"]
+++

## text
Travel along roads from dot to dot. Each road counts as one step. A shortest route uses the fewest steps. Routes may share roads; draw their colors side by side.

A meeting dot works when \textbf{each pair of homes has a shortest route through it}. The meeting dot may also be a home. Keep all three homes and the meeting dot fixed while checking the three pairs. One partner draws the routes in three colors; the other checks them.

\begin{center}
\begin{tikzpicture}[x=1.6cm,y=1.6cm,font=\small]
\draw[gray!65,step=1] (0,0) grid (2,1);\foreach \x in {0,1,2}\foreach \y in {0,1}\fill (\x,\y) circle (1.5pt);
\draw[line width=2.2pt] (0,0)--(1,0)--(1,1)--(2,1);
\home{0}{0}{P}\home{2}{1}{Q}\node[draw,circle,fill=white,inner sep=2pt] at (1,1){M};
\node[align=left,anchor=west] at (3,.6){P to M: 2 steps\quad M to Q: 1 step\\Through M: 3 steps\\Shortest P to Q: 3 steps};
\end{tikzpicture}
\end{center}
