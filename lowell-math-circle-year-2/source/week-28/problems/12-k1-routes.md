+++
id = "w28.k1-routes"
title = "Routes through the eight folds"
grades = ["K-1"]
route = "return"
kernel = "Two flat right-angle labelings always differ in an even number of rays; only the four complementary pairs differ in all four."
+++

## prompt
Visit all eight folds once, changing exactly two labels at each move. Find a route from A to H and a route from A to D.

## figure
k1_routes()

## key
\textbf{Two valid routes:} each visits all eight printed states exactly once, uses the required endpoints and changes exactly two ray labels at every step.

\begin{tabular}{llll}
Route ending H & Changed ray numbers & Route ending D & Changed ray numbers\\
A$\to$B & 3,4 & A$\to$B & 3,4\\
B$\to$C & 2,3 & B$\to$C & 2,3\\
C$\to$D & 1,2 & C$\to$E & 3,4\\
D$\to$F & 3,4 & E$\to$F & 1,2\\
F$\to$E & 1,2 & F$\to$G & 2,3\\
E$\to$G & 1,3 & G$\to$H & 3,4\\
G$\to$H & 3,4 & H$\to$D & 2,3\\
\end{tabular}

\textbf{Complete move rule:} any two distinct catalog states are two changes apart except the complementary pairs A-H, B-G, C-F and D-E, which are four changes apart.
