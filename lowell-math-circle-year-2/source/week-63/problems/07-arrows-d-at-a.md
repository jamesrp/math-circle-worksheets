+++
id = "w63.arrows-d-at-a"
title = "Card-to-home arrows with D in home A"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'With D in home A there are three home-free rows: DCBA, where A and D swap, and two rows with a longer loop.'
+++

## text
\renewcommand{\band}{Grades 4--5}
An arrow points from a card's letter to the home where that card sits.

\begin{center}\begin{tikzpicture}[x=1mm,y=1mm]
  \node[anchor=west,font=\small] at (0,28) {Placement};
  \rowdraw{0}{19}{P,Q,R,S,T}{Q,R,S,T,P}
  \draw[-{Stealth[length=2mm]}] (63,11)--(71,11);
  \node[font=\small,align=center] at (92,18) {P is in home T};
  \node[font=\large] at (92,8) {P $\longrightarrow$ T};
  \draw[-{Stealth[length=2mm]}] (115,11)--(123,11);
  \node[font=\small] at (151,28) {All arrows};
  \begin{scope}[shift={(151,5)}]\cyclefive{P,T,S,R,Q}{17}\end{scope}
\end{tikzpicture}\end{center}

## prompt
Keep D in home A. Find every A--D row with no home matches, and draw its arrows. Sort the rows into those with A in home D and those with A away from home D. What makes your list complete?

## text
\begin{center}\begin{tikzpicture}[x=1mm,y=1mm]
  \fourworkspace{36}{-33}
  \fourworkspace{127}{-33}
  \fourworkspace{36}{-110}
  \fourworkspace{127}{-110}
\end{tikzpicture}\end{center}
\worklines{2}
