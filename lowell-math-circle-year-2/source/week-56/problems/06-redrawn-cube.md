+++
id = "w56.redrawn-cube"
title = "Redrawing the cube surface"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'Subdividing a face or an edge changes $V$, $E$ and $F$ but not $V-E+F$ or the total gap: a new point has zero gap.'
+++

## text
In a redrawn surface, marked points count as vertices, segments between vertices count as edges, and each face piece counts as a face.

## prompt
Compare $V-E+F$ for all four models in Problem 1. Keep the cube's shape and try these three changes to its surface drawing. What happens to $V-E+F$ and to the total gap? Can a new vertex have a gap while the cube keeps its shape?

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
 \draw[fill=blue!8] (0,0) rectangle (2.7,2.7);\draw[very thick] (0,0)--(2.7,2.7);
 \node[align=center] at (1.35,-.55) {one face divided\\by a diagonal};
 \draw[fill=blue!8] (4,0) rectangle (6.7,2.7);
 \foreach \p in {(4,0),(6.7,0),(6.7,2.7),(4,2.7)}{\draw[very thick] \p --(5.35,1.35);}
 \fill (5.35,1.35) circle (2pt);\node[align=center] at (5.35,-.55) {one face divided\\from its center};
 \draw[fill=blue!8] (8,0) rectangle (10.3,2.7);
 \draw[fill=blue!17] (10.3,0)--(12.3,.8)--(12.3,3.5)--(10.3,2.7)--cycle;
 \draw[very thick] (10.3,0)--(10.3,2.7);\fill (10.3,1.35) circle (2.2pt);
 \node[align=center] at (10.3,-.55) {one vertex inserted\\along a shared edge};
\end{tikzpicture}\end{center}
\begin{center}\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|m{3.3cm}|>{\centering\arraybackslash}m{2cm}|>{\centering\arraybackslash}m{2cm}|>{\centering\arraybackslash}m{2cm}|>{\centering\arraybackslash}m{2.7cm}|>{\centering\arraybackslash}m{3.1cm}|}
\hline Closed surface & $V$ & $E$ & $F$ & $V-E+F$ & Total gap\\\hline
Original cube &&&&&\\[25pt]\hline
One diagonal &&&&&\\[25pt]\hline
Center and 4 lines &&&&&\\[25pt]\hline
One edge vertex &&&&&\\[25pt]\hline
\end{tabular}\end{center}
\blank{.3cm}\workbox{6.0}
