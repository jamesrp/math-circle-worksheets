+++
id = "w62.two-slots-or-a-cycle"
title = "A two-slot schedule or an odd cycle"
grades = ["shared"]
route = "first"
page = "new"
kernel = 'The 6-cycle with chord AD fits in 2 slots (both cycles are even); the 7-cycle with chord AD needs 3 (A-D-E-F-G-A is a 5-cycle).'
+++

## text
\gdef\band{Grades 4--5}
A cycle follows conflict lines through at least three different circles and back to its start. Only the start repeats, at the end.
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small,>=Stealth]
\foreach \shift/\caption in {0/conflict lines,4.6/partway,9.2/back at W}{
\begin{scope}[shift={(\shift,0)}]
\node at (1,2.2) {\caption};
\draw (0,0) -- (0,1.4) -- (2,1.4) -- (2,0) -- cycle;
\node[draw,circle,fill=white,minimum size=0.55cm] at (0,0) {W};
\node[draw,circle,fill=white,minimum size=0.55cm] at (0,1.4) {X};
\node[draw,circle,fill=white,minimum size=0.55cm] at (2,1.4) {Y};
\node[draw,circle,fill=white,minimum size=0.55cm] at (2,0) {Z};
\end{scope}}
\draw[->] (2.8,0.7) -- (3.7,0.7); \draw[->] (7.4,0.7) -- (8.3,0.7);
\node at (5.6,-0.6) {W--X--Y}; \node at (10.2,-0.6) {W--X--Y--Z--W};
\draw[line width=2.2pt] (4.6,0.3) -- (4.6,1.1); \draw[line width=2.2pt] (4.9,1.4) -- (6.3,1.4);
\draw[line width=2.2pt] (9.2,0.3) -- (9.2,1.1); \draw[line width=2.2pt] (9.5,1.4) -- (10.9,1.4);
\draw[line width=2.2pt] (11.2,1.1) -- (11.2,0.3); \draw[line width=2.2pt] (10.9,0) -- (9.5,0);
\end{tikzpicture}
\end{center}

## prompt
For each network, show a two-slot schedule if one exists. If it cannot fit in two slots, mark a cycle that explains why.

## figure
center(graph("p4-six-chord",CHORD6,CHORD6e))
+center(graph("p4-seven-chord",CHORD7,CHORD7e))
