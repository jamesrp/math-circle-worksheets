+++
id = "w88.radius-bridge"
title = "Touching disks: centre distance is the sum of radii"
kind = "setup"
grades = ["K-5"]
route = "return"
page = "new"
+++

## text
A radius runs from a circle's center to its edge. For two touching disks, the distance between centers is the sum of their radii.
\begin{center}\begin{tikzpicture}[x=1mm,y=1mm,font=\small]
\foreach \x in {0,60,120}{
\draw (\x,0) circle (7.5);\draw ({\x+20},0) circle (12.5);
\fill (\x,0) circle (.6);\fill ({\x+20},0) circle (.6);
\node[below] at (\x,-1) {A};\node[below] at ({\x+20},-1) {B};}
\node at (10,24) {Touching disks};
\node at (10,-23) {radii 15 mm and 25 mm};
\node at (70,24) {Join the centers};
\draw[thick] (60,0)--(80,0);\fill (67.5,0) circle (.6);
\node[above,font=\scriptsize] at (62.5,1) {15 mm};\node[above,font=\scriptsize] at (73.75,1) {25 mm};
\node at (70,-23) {two radii end to end};
\node at (130,24) {Distance from A to B};
\draw[thick] (120,0)--(140,0);
\node[above] at (130,15) {40 mm};
\node at (130,-23) {$15+25=40$ mm};
\draw[->] (38,0)--(46,0);\draw[->] (98,0)--(106,0);
\node at (70,-35) {Same pair each time. Sketches, not actual size.};
\end{tikzpicture}\end{center}
