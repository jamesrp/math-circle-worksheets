+++
id = "w74.moves-and-example"
kind = "setup"
title = "Moves, the partner's record and the URD example"
grades = ["4-5"]
route = ["first", "return"]
+++

## text
Move a marker. Your partner checks each move and writes its letter.
Swap jobs after a trip. Start at ground coordinate 0, level 0.

U and D move one level straight up or down, keeping the ground coordinate.
Do not go below level 0. R and L move right or left by the level's step size.
Every move costs one. The roads continue beyond this page; higher levels keep doubling.

\begin{center}
\begin{tikzpicture}[x=.95in,y=.4in,>=Stealth,font=\small]
\node[align=center] (a) at (0,0) {coordinate 1\\level 0};
\node[align=center] (b) at (2,0) {coordinate 1\\level 1};
\node[align=center] (c) at (4,0) {coordinate 3\\level 1};
\node[align=center] (d) at (6,0) {coordinate 3\\level 0};
\draw[->] (a)--node[above]{U}(b);\draw[->](b)--node[above]{R}(c);\draw[->](c)--node[above]{D}(d);
\node at (3,-1.2) {Example: U R D costs 3 moves.};
\end{tikzpicture}
\end{center}
