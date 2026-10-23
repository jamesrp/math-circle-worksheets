+++
id = "w82.star-front-and-back"
title = "A star in front, a star after every kid"
grades = ["3-5"]
route = "first"
kernel = "A star in front of an endless row is absorbed (star to 1, each n to n + 1, keeping order), while a star after every numbered kid is a last kid, so that line matches the plain row completely but never keeping order."
+++

## prompt
Labels only identify kids. Partners may have different labels; identical labels in two lines do not have to be paired. Compare A with B, then A with C. Can you match every kid? Can a complete match keep order? Give a rule for every kid, or explain why it is impossible.

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=east] at (0.4,0) {A};
\foreach \x/\n in {2/1,4/2,6/3}{\longcard{\x}{0}{\n}{black}}
\continuation{7.5}{0}{numbers continue\\forever}{black}
\node[anchor=east] at (0.4,-3.0) {B};
\longcard{2}{-3.0}{$\bigstar$}{black}
\foreach \x/\n in {4/1,6/2,8/3}{\longcard{\x}{-3.0}{\n}{black}}
\continuation{9.5}{-3.0}{numbers continue\\forever}{black}
\node[anchor=east] at (0.4,-6.0) {C};
\draw[rounded corners=3pt,dashed,line width=0.8pt] (0.9,-7.35) rectangle (11.2,-5.2);
\foreach \x/\n in {2/1,4/2,6/3}{\longcard{\x}{-6.0}{\n}{black}}
\continuation{7.5}{-6.0}{numbers continue\\forever}{black}
\node[draw,rounded corners=3pt,align=center,minimum width=4.0cm,minimum height=2.15cm] at (13.7,-6.28) {$\bigstar$\\\small after EVERY\\\small numbered kid};
\end{tikzpicture}
\end{center}
\vspace{0.3cm}
\ruleline
\vspace{0.7cm}
\ruleline
