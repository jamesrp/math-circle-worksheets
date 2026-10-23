+++
id = "w81.rules"
kind = "setup"
title = "The bucket rules and a worked move"
grades = ["2-5"]
route = ["first", "return"]
+++

## text
Take turns. Remove one counter from a nonempty bucket. You may then add counters only to buckets strictly to its left. If you cannot move, you lose.

For Problems 1--3, add at most one counter to each earlier bucket.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
 \node[font=\small] at (2.05,1.87) {Before};
 \node[font=\small] at (7.75,1.87) {Remove one from 3};
 \node[font=\small] at (13.45,1.87) {Add one to 1 and 2};
 \dotsbucket{0}{0}{1}{1}\dotsbucket{1.5}{0}{1}{2}\dotsbucket{3}{0}{2}{3}
 \dotsbucket{5.7}{0}{1}{1}\dotsbucket{7.2}{0}{1}{2}\dotsbucket{8.7}{0}{1}{3}
 \dotsbucket{11.4}{0}{2}{1}\dotsbucket{12.9}{0}{2}{2}\dotsbucket{14.4}{0}{1}{3}
 \draw[arrow] (4.62,.65)--(5.37,.65);
 \draw[arrow] (10.32,.65)--(11.07,.65);
 \node[fish] at (9.4,-.68) {};
 \draw[black,line width=.75pt] (9.17,-.91)--(9.63,-.45);
 \node[font=\scriptsize,anchor=west] at (9.75,-.68) {removed};
\end{tikzpicture}
\end{center}
\vspace{8pt}
