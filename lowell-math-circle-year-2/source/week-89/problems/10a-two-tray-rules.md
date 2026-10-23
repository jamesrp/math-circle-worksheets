+++
id = "w89.two-tray-rules"
kind = "setup"
title = "Two trays: rules and a worked turn"
grades = ["K-5"]
route = "return"
page = "new"
+++

## text
Each turn, add the input to the first total. Then add a copy of the \emph{new first total} to the second total. Keep both totals; nothing moves out of either tray. Use one total card in each tray and change it when needed.

\begin{center}\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west] at (0,7.15){One turn with input 2:};
\node[draw,minimum width=1cm,minimum height=.7cm] at (.6,5.8){2};
\node[font=\small] at (.6,5.1){input};
\tray{2}{5.3}{first total}{1}\tray{5}{5.3}{second total}{1}
\node[font=\small,anchor=west] at (0,4.45){Add input 2 to the first total.};
\draw[-{Latex}] (3,4.1)--(3,3.75);
\node[draw,minimum width=1cm,minimum height=.7cm] at (.6,3.1){2};
\node[font=\footnotesize,align=center] at (.6,2.3){same input\\already added};
\tray{2}{2.5}{first total}{3}\tray{5}{2.5}{second total}{1}
\node[font=\small,anchor=west] at (0,1.65){Copy the new first total, 3, and add it to the second.};
\draw[-{Latex}] (3,1.3)--(3,.95);
\tray{2}{-.4}{first total}{3}\tray{5}{-.4}{second total}{4}
\node[font=\small,anchor=west] at (0,-1.25){Turn finished: both totals stay in their trays.};
\end{tikzpicture}\end{center}
