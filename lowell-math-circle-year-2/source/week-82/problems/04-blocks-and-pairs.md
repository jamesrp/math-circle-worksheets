+++
id = "w82.blocks-and-pairs"
title = "Two blocks against a row of pairs"
grades = ["3-5"]
route = "return"
page = "new"
kernel = "Two endless blocks match a row of pairs completely (namesakes), but not keeping order: B1 has infinitely many kids before it, and every kid in the row of pairs has only finitely many."
+++

## prompt
Compare D with E. Can you match every kid? Can a complete match keep order? Give a rule for every kid, or explain why it is impossible.

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=east] at (0.0,0) {D};
% One horizontal concatenation: the blue block is after the WHOLE red row.
\draw[rounded corners=3pt,dashed,queueR] (.3,-.8) rectangle (7.1,.8);
\foreach \x/\n in {1/1,2.35/2,3.7/3}{\card{\x}{0}{R\n}{queueR}}
\draw[queueR,line width=1.1pt,-{Stealth[length=2.8mm]}] (4.5,0)--(6.75,0);
\node[align=center,font=\small,text=queueR] at (3.7,-1.3) {red numbers continue forever};
\draw[rounded corners=3pt,dashed,queueB] (8.3,-.8) rectangle (15.9,.8);
\foreach \x/\n in {9.1/1,10.45/2,11.8/3}{\card{\x}{0}{B\n}{queueB}}
\draw[queueB,line width=1.1pt,-{Stealth[length=2.8mm]}] (12.6,0)--(15.5,0);
\node[align=center,font=\small,text=queueB] at (12.1,-1.3) {blue numbers continue forever};
\node[align=center,font=\small] at (8.1,-2.35) {The whole blue row starts after EVERY red kid.};
\node[anchor=east] at (0.4,-6.1) {E};
\foreach \x/\v/\c in {1.8/R1/queueR,3.8/B1/queueB,5.8/R2/queueR,7.8/B2/queueB,9.8/R3/queueR,11.8/B3/queueB}{\longcard{\x}{-6.1}{\v}{\c}}
\draw[line width=1.1pt,-{Stealth[length=2.8mm]}] (13.0,-6.1)--(15.2,-6.1);
\node[font=\small,align=center] at (13.65,-7.25) {R4, B4, R5, B5, $\ldots$\\pairs continue forever};
\end{tikzpicture}
\end{center}
\vspace{0.65cm}
\ruleline
\vspace{0.7cm}
\ruleline
