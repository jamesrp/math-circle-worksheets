+++
id = "w89.three-trays"
title = "A third tray"
grades = ["K-5"]
route = "return"
page = "new"
kernel = "With input 1 the three trays hold $n$, $n(n+1)/2$ and $n(n+1)(n+2)/6$."
+++

## prompt
What changes if a third tray keeps adding copies of the second total? Start three trays at 0 and use input 1 for six turns. Find a rule for each tray's total after any number of turns.

## text
On each turn, update the first tray, then the second, then the third. Each tray keeps its previous total. Copy each total only after it has been updated on that turn.

\begin{center}\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west] at (0,4.6){One turn with input 1:};
\foreach \yy/\aa/\bb/\cc/\txt in {3.1/3/3/3/before,1.3/4/3/3/add input 1,-0.5/4/7/3/add new first total,-2.3/4/7/10/add new second total}{
\node[anchor=west,font=\small] at (0,\yy+.55){\txt};
\tray{4}{\yy}{first}{\aa}\tray{6.2}{\yy}{second}{\bb}\tray{8.4}{\yy}{third}{\cc}}
\end{tikzpicture}\end{center}
\answer{15mm}
\begin{center}\renewcommand{\arraystretch}{2}
\begin{tabular}{c|ccc}
turns&first total&second total&third total\\\hline
1&&&\\
2&&&\\
3&&&\\
4&&&\\
5&&&\\
6&&&
\end{tabular}\end{center}
