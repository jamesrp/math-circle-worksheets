+++
id = "w69.road-triangles"
kind = "setup"
title = "Steps, shortest routes and road triangles"
grades = ["4-5"]
route = ["first", "return"]
+++

## text
Each road between neighboring dots is one step. A shortest route uses the fewest steps. Roads may be drawn at different lengths.

\begin{center}
\begin{tikzpicture}[x=.9cm,y=.9cm,font=\small]
\draw[gray!65,step=1] (0,0) grid (2,1);\foreach \x in {0,1,2}\foreach \y in {0,1}\fill (\x,\y) circle (1.5pt);
\draw[line width=2pt] (0,0)--(1,0)--(1,1)--(2,1);\home{0}{0}{P}\home{2}{1}{Q}
\node[anchor=west,align=left] at (3,.6){P to Q: 2 steps right, 1 step up.\\This shortest route uses 3 roads.};
\end{tikzpicture}
\end{center}
For three homes A, B, C, choose a shortest route for each pair. Color AB red, BC blue, and CA green. These three routes are a road triangle. Routes may overlap; draw the colors side by side when they do. Your partner checks that each route is shortest.
