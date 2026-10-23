+++
id = "w93.one-reshape"
title = "Reshape once and trap the side"
grades = ["3-5"]
route = "first"
kernel = 'The new pair of sides traps the side of the equal-area square more tightly than the old pair: $a<h<\sqrt{A}<m<b$.'
+++

## prompt
Reshape each rectangle once. Mark the old and new side lengths on its number line. Which two of those four lengths give the tightest guaranteed range for the side of a square with that area?

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\foreach \y/\a/\b/\area in {0/2/6/12,-4/3/6/18,-8/2/10/20} {
\node[anchor=west] at (0,\y) {$\a\ \text{by}\ \b\qquad\text{area }\area$};
\node[anchor=west] at (0,\y-.7) {New sides: \rule{2.0cm}{.4pt}\quad and\quad\rule{2.0cm}{.4pt}};
\draw (0,\y-1.7)--(16,\y-1.7);
\foreach \n in {0,...,10} {
\draw (1.6*\n,\y-1.6)--(1.6*\n,\y-1.8);
\node[below,font=\small] at (1.6*\n,\y-1.8) {\n};}
\node[anchor=west] at (0,\y-2.8) {Square side between \rule{2.0cm}{.4pt}\quad and\quad\rule{2.0cm}{.4pt}};
}
\end{tikzpicture}
\end{center}
