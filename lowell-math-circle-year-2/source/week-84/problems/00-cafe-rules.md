+++
id = "w84.cafe-rules"
title = "Café rules and a two-person example"
grades = ["2-5"]
route = "first"
kind = "setup"
+++

## text
Each person sees only their own card: YES if they want a cup, NO if not. Everyone knows the cards can be dealt in any way.

In order, people 1, 2, 3 answer ``Does everyone want a cup?'' Say YES or NO when your card and the earlier answers settle it. Otherwise say NOT YET.

With two people:

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,>=Latex]
 \draw (0,0) rectangle (4.8,3.2);\draw (6,0) rectangle (10.8,3.2);\draw (12,0) rectangle (16.8,3.2);
 \node[font=\small] at (2.4,2.85) {Before};\node[font=\small] at (8.4,2.85) {Heard};\node[font=\small] at (14.4,2.85) {After};
 \node[font=\scriptsize] at (2.4,2.35) {1\qquad 2};\node[font=\scriptsize] at (14.4,2.35) {1\qquad 2};
 \node[align=center,font=\small] at (2.4,1.2) {YES\quad YES\\YES\quad NO\\NO\quad YES\\NO\quad NO};
 \node[align=center,font=\small] at (8.4,1.5) {Person 1 says NO.\\Their own card must be NO.};
 \node[align=center,font=\small] at (14.4,1.2) {NO\quad YES\\NO\quad NO};
 \draw[->,thick] (4.9,1.2)--(5.9,1.2);\draw[->,thick] (10.9,1.2)--(11.9,1.2);
\end{tikzpicture}
\end{center}
