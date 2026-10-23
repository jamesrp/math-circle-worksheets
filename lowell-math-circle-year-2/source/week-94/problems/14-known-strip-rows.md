+++
id = "w94.known-strip-rows"
title = "A known strip finds the hidden strips"
grades = ["K-1", "2-3"]
route = "first"
page = { "2-3" = "new" }
kernel = 'A known strip fixes the extra (4, 2, 6), and then the hidden lengths. In K--1, the known towers give extras 1, 3 and 2, so P and Q went in as (3, 5), (1, 3) and (2, 4).'
+++

## prompt [K-1]
P and Q still come out as 4 and 6 cubes, but each machine has its own extra. Build P and Q for each machine, and color them.

## prompt
Each row uses a different machine. A known strip gives report 8. Two hidden strips give reports 9 and 12. Build the hidden strips for each row.

## text [K-1]
\begin{center}\begin{tikzpicture}[x=6.5mm,y=6.5mm]
\foreach\i/\a/\b in{0/1/2,1/2/5,2/3/5}{\begin{scope}[shift={(9*\i,0)}]
\draw[gray,rounded corners](-1,-10.9)rectangle(6.8,7.1);
\node at(2.9,6.3){known tower};
\tcubes{.4}{0}{\a}\node[below,text height=1.6ex,text depth=.3ex]at(.9,0){in};
\draw[->,thick](1.8,1)--(3.6,1);
\tcubes{4.4}{0}{\b}\node[below,text height=1.6ex,text depth=.3ex]at(4.9,0){out};
\draw[gray!60](-1,-2)--(6.8,-2);
\node at(2.9,-2.9){P and Q went in};
\tcells{1.4}{-9.8}{6}\node[below]at(1.9,-9.8){P};
\tcells{3.4}{-9.8}{6}\node[below]at(3.9,-9.8){Q};
\end{scope}}
\end{tikzpicture}\end{center}

## text
\begin{center}\begin{tabular}{|p{4.8cm}|p{4.1cm}|p{4.1cm}|}\hline
Known strip & Length that reports 9 & Length that reports 12 \\\hline
\rule{0pt}{22mm}4 units $\longrightarrow$ 8&&\\\hline
\rule{0pt}{22mm}6 units $\longrightarrow$ 8&&\\\hline
\rule{0pt}{22mm}2 units $\longrightarrow$ 8&&\\\hline
\end{tabular}\end{center}
\vspace{8mm}
