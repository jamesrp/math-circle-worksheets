+++
id = "w72.outlines"
title = "Memories of outlines in both directions"
grades = ["4-5"]
route = "return"
page = "new"
kernel = "A closed simple loop remembers its signed area, positive counterclockwise, and sliding it leaves the memory alone; the L and the 2-by-2 square use the same eight cards but remember 3 and 4."
+++

## prompt
Start at each dot with memory 0. Walk once around its outline in each direction. How does moving the same rectangle to a new place affect its final memory? What connects a loop's shape, direction and final memory?

## text
\vspace{.1in}
\begin{center}
\begin{tabular}{c@{\hspace{.30in}}c@{\hspace{.30in}}c}
\begin{tikzpicture}[scale=1.50]
\draw[gray!30,step=1] (0,0) grid (3,3);\foreach\x in{0,...,3}{\node[below]at(\x,0){\x};}
\draw[very thick](0,0)--(2,0)--(2,1)--(0,1)--cycle;\fill(0,0)circle(3pt);
\end{tikzpicture}&
\begin{tikzpicture}[scale=1.50]
\draw[gray!30,step=1] (2,0) grid (5,3);\foreach\x in{2,...,5}{\node[below]at(\x,0){\x};}
\draw[very thick](2,0)--(4,0)--(4,1)--(2,1)--cycle;\fill(2,0)circle(3pt);
\end{tikzpicture}&
\begin{tikzpicture}[scale=1.50]
\draw[gray!30,step=1] (-3,0) grid (0,3);\foreach\x in{-3,...,0}{\node[below]at(\x,0){\x};}
\draw[very thick](-3,0)--(-1,0)--(-1,1)--(-3,1)--cycle;\fill(-3,0)circle(3pt);
\end{tikzpicture}\\[5pt]
\memories&\memories&\memories
\end{tabular}\par\vspace{.24in}
\begin{tabular}{c@{\hspace{.30in}}c}
\begin{tikzpicture}[scale=1.50]
\draw[gray!30,step=1] (0,0) grid (3,3);\foreach\x in{0,...,3}{\node[below]at(\x,0){\x};}
\draw[very thick](0,0)--(2,0)--(2,1)--(1,1)--(1,2)--(0,2)--cycle;\fill(0,0)circle(3pt);
\end{tikzpicture}&
\begin{tikzpicture}[scale=1.50]
\draw[gray!30,step=1] (0,0) grid (3,3);\foreach\x in{0,...,3}{\node[below]at(\x,0){\x};}
\draw[very thick](0,0)--(2,0)--(2,2)--(0,2)--cycle;\fill(0,0)circle(3pt);
\end{tikzpicture}\\[5pt]
\memories&\memories
\end{tabular}\end{center}
\vspace{.12in}\lines{3}
