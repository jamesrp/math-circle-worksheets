+++
id = "w56.reverse-inventory"
title = "Counts from one corner: five triangles, three pentagons"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'A gap of $60^\circ$ or $36^\circ$ at every vertex forces $V=720/\mathrm{gap}$, then $F$ and $E$ by double counting: $(12,30,20)$ and $(20,30,12)$.'
+++

## text
A regular polygon has equal sides and equal angles. Every face of each solid below is one regular polygon.

## prompt
Find the number of vertices, edges and faces each closed convex solid with polygon faces must have, without a model of the whole solid.

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
 \begin{scope}[shift={(0,0)}]
  \foreach \a in {0,60,120,180,240}{\draw[fill=blue!10] (0,0)--(\a:1.5)--(\a+60:1.5)--cycle;}
  \draw[gray!50] (0,0) circle (1.5);\fill (0,0) circle (1.7pt);
  \node[align=center,text width=6.5cm] at (0,-2.2) {Triangle faces; five meet\\at every vertex};
 \end{scope}
 \begin{scope}[shift={(8,0)}]
  \foreach \a in {0,108,216}{\begin{scope}[rotate=\a]
   \draw[fill=blue!10] (0,0)--(.9,0)--(1.178115,.855951)--(.45,1.384957)--(-.278115,.855951)--cycle;
  \end{scope}}
  \draw[gray!50] (0,0) circle (1.5);\fill (0,0) circle (1.7pt);
  \node[align=center,text width=6.5cm] at (0,-2.2) {Pentagon faces; three meet\\at every vertex};
 \end{scope}
\end{tikzpicture}\end{center}
\begin{center}\renewcommand{\arraystretch}{1.2}
\begin{tabular}{|m{5.5cm}|>{\centering\arraybackslash}m{3.1cm}|>{\centering\arraybackslash}m{3.1cm}|>{\centering\arraybackslash}m{3.1cm}|}
\hline Solid & Vertices & Edges & Faces\\\hline
Five triangles at each vertex &&&\\[35pt]\hline
Three pentagons at each vertex &&&\\[35pt]\hline
\end{tabular}\end{center}
\blank{.35cm}\workbox{9.0}
