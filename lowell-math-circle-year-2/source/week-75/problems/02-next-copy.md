+++
id = "w75.next-copy"
kind = "setup"
title = "Continuing into the next copy"
grades = ["4-5"]
route = ["first", "return"]
page = "new"
+++

## text
Instead of jumping back across the cut, continue into the next copy of the rectangle. The top dots are copies of the same B on the cylinder.
\begin{center}\begin{tikzpicture}[x=.78in,y=.9in,font=\small,>=Stealth]
\draw(0,0)rectangle(1.5,1);
\draw[very thick](.75,0)--(1.5,.5);\draw[very thick](0,.5)--(.75,1);
\fill(.75,0)circle(1.5pt)node[below]{A};\fill(.75,1)circle(1.5pt)node[above]{B};
\draw[->](1.9,.5)--(2.7,.5);
\draw(3.1,0)rectangle(6.1,1);\draw[dashed](4.6,0)--(4.6,1);
\draw[very thick](3.85,0)--(5.35,1);\fill(3.85,0)circle(1.5pt)node[below]{A};\fill(5.35,1)circle(1.5pt)node[above]{B};
\node at(3.85,1.3){copy 0};\node at(5.35,1.3){copy 1};
\node at(3.05,-.65){Example: winding $+1$ ends at B in copy 1.};
\end{tikzpicture}\end{center}
