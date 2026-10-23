+++
id = "w84.doll-rules"
title = "Headband rules and a two-doll example"
grades = ["2-5"]
route = "first"
kind = "setup"
page = "new"
+++

## text
Each doll wears B (blue) or R (red), sees the other dolls' headbands and cannot see its own. Everyone hears: ``At least one headband is blue.''

A doll shows PROVE BLUE only when every possible arrangement matching what it sees gives it a blue headband. Otherwise it shows NOT YET.

A doll's matching cards are a temporary private view. Leave the shared set unchanged while choosing all three replies. Reveal replies together. Then remove arrangements that could not give those replies. Keep the headbands unchanged.

With two dolls, match a doll's view to the possibility cards:
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,>=Latex]
 \draw (0,0) rectangle (4.8,2.5);\draw (6,0) rectangle (10.8,2.5);\draw (12,0) rectangle (16.8,2.5);
 \node[font=\small] at (2.4,2.2) {Input};\node[font=\small] at (8.4,2.2) {Private matches for doll 1};\node[font=\small] at (14.4,2.2) {Doll 1's reply};
 \node[align=center,font=\small] at (2.4,1.05) {Possible: BB, BR, RB.\\Doll 1 sees R on doll 2.};
 \node[font=\Large\bfseries] at (8.4,1.15) {BR};
 \node[font=\small\bfseries] at (14.4,1.15) {PROVE BLUE};
 \draw[->,thick] (4.9,1.2)--(5.9,1.2);\draw[->,thick] (10.9,1.2)--(11.9,1.2);
\end{tikzpicture}
\end{center}
