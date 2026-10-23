+++
id = "w72.two-e-two-n"
title = "Every route with two E and two N cards"
grades = ["4-5"]
route = "first"
kernel = "The endpoint does not fix the memory: the six orders of EENN leave five different memories."
+++

## prompt
Use two E cards and two N cards, in any order. Find every different route from O to the ring. What memories can you leave there?

## text
\vspace{.05in}
\begin{minipage}[t]{.50\linewidth}\centering\vspace{0pt}
\begin{tikzpicture}[scale=1.75]
\draw[step=1,gray!32] (0,0) grid (3,3);
\foreach \x in {0,1,2,3}{\node[below] at (\x,0){\x};}
\fill (0,0) circle (2.5pt);\node[above right] at(0,0){O};
\draw[line width=1.1pt] (2,2) circle (5pt);
\node[below] at (1.5,-.48){column number};
\end{tikzpicture}
\end{minipage}\hfill
\begin{minipage}[t]{.43\linewidth}\vspace{0pt}
route\hfill final memory\par\vspace{.10in}
\lines{7}
\end{minipage}
\vfill
