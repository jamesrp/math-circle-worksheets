+++
id = "w63.two-families"
title = "Two families of home-free rows with E in home A"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'With E in home A, two home-free rows swap A and E and nine have a longer loop; deleting E rebuilds them reversibly from the two three-card and nine four-card rows.'
+++

## text
\renewcommand{\band}{Grades 4--5}
Smaller arrow loops keep their remaining letters. These examples remove U, then can be read backward to restore U.

\begin{center}\begin{tikzpicture}[x=1mm,y=1mm]
  \node[font=\small] at (25,28) {Input};
  \node[font=\small] at (86,28) {Remove U};
  \node[font=\small] at (148,28) {Output};
  \begin{scope}[shift={(25,2)}]
    \node[circle,draw,minimum size=6mm,inner sep=0pt,font=\small] (p) at (-12,15) {P};
    \node[circle,draw,minimum size=6mm,inner sep=0pt,font=\small] (u) at (12,15) {U};
    \draw[-{Stealth[length=1.8mm]}] (p) to[bend left=18] (u);
    \draw[-{Stealth[length=1.8mm]}] (u) to[bend left=18] (p);
    \begin{scope}[shift={(0,-13)}]\cyclefour{Q,R,S,T}{13}\end{scope}
  \end{scope}
  \draw[-{Stealth[length=2mm]}] (48,0)--(57,0);
  \node[font=\small,align=center] at (86,0) {P and U point\\to each other.\\Remove both.};
  \draw[-{Stealth[length=2mm]}] (114,0)--(123,0);
  \begin{scope}[shift={(148,0)}]\cyclefour{Q,R,S,T}{17}\end{scope}

  \node[font=\small] at (25,-45) {Input};
  \node[font=\small] at (86,-45) {Remove U};
  \node[font=\small] at (148,-45) {Output};
  \begin{scope}[shift={(25,-70)}]\cyclesix{P,Q,R,S,T,U}{19}\end{scope}
  \draw[-{Stealth[length=2mm]}] (48,-70)--(57,-70);
  \node[font=\small,align=center] at (86,-70) {T $\to$ U $\to$ P\\becomes\\T $\to$ P};
  \draw[-{Stealth[length=2mm]}] (114,-70)--(123,-70);
  \begin{scope}[shift={(148,-70)}]\cyclefive{P,Q,R,S,T}{18}\end{scope}
\end{tikzpicture}\end{center}

## prompt
Keep E in home A. Make every home-free A--E row in two families: A in home E, and A away from home E. How can each family be built from smaller home-free rows? Give constructions you can reverse.

## text
\vspace{4mm}
\worklines{4}
