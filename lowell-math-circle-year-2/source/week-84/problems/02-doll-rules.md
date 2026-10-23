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

Choose all three replies from the cards on the table, without removing any. Show them together. Then remove every card that would have given different replies. Keep the headbands unchanged.

With two dolls:
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,>=Latex]
 \draw (0,0) rectangle (5.2,3.7);\draw (6.3,0) rectangle (11.5,3.7);\draw (12.6,0) rectangle (17.8,3.7);
 \node[font=\small] at (2.6,3.35) {Cards on the table};\node[font=\small] at (8.9,3.35) {Replies, shown together};\node[font=\small] at (15.2,3.35) {Remove the others};
 \node[font=\Large\bfseries] at (2.6,2.45) {BB\enspace BR\enspace RB};
 \node[font=\small,anchor=east] at (2.4,1.3) {Deal:};
 \hatdisk{2.9}{1.3}{0}\hatdisk{3.7}{1.3}{1}
 \node[font=\scriptsize] at (2.9,0.75) {1};\node[font=\scriptsize] at (3.7,0.75) {2};
 \node[align=left,anchor=north west,font=\small] at (6.55,3.0) {Doll 1 sees B: BB, RB\\\textbf{NOT YET}};
 \node[align=left,anchor=north west,font=\small] at (6.55,1.75) {Doll 2 sees R: RB\\\textbf{PROVE BLUE}};
 \node[align=left,anchor=north west,font=\small] at (12.85,3.0) {BB would give\\NOT YET, NOT YET};
 \node[align=left,anchor=north west,font=\small] at (12.85,1.95) {BR would give\\PROVE BLUE, NOT YET};
 \node[align=left,anchor=north west,font=\small] at (12.85,0.85) {Left: \textbf{RB}};
 \draw[->,thick] (5.3,1.85)--(6.2,1.85);\draw[->,thick] (11.6,1.85)--(12.5,1.85);
\end{tikzpicture}
\end{center}
