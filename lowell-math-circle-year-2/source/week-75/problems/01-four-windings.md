+++
id = "w75.four-windings"
title = "Yarn routes of winding 0, $+1$, $-1$ and $+2$"
grades = ["4-5"]
route = "first"
scale = "actual"
kernel = "Signed seam crossings give each fixed-end route an integer winding, and routes that look different can share one."
+++

## prompt
Cut out the rectangle and tape its left and right edges together without overlap. Make yarn routes with winding 0, $+1$, $-1$ and $+2$. Your partner checks the seam crossings. Make two different-looking routes with the same winding.

## text
\vspace{.12in}
\begin{center}\begin{tikzpicture}[x=1in,y=1in,font=\small,>=Stealth]
\draw[dashed,thick](0,0)rectangle(6,2.4);
\draw[gray!45,dotted](0,.6)--(6,.6);\draw[gray!45,dotted](0,1.2)--(6,1.2);\draw[gray!45,dotted](0,1.8)--(6,1.8);
\fill(3,0)circle(2pt);\node[above]at(3,.02){A};\fill(3,2.4)circle(2pt);\node[below]at(3,2.38){B};
\node[rotate=90]at(.17,1.2){seam};\node[rotate=90]at(5.83,1.2){seam};
\draw[->,thick](4.6,1.3)--(5.35,1.3);\node[above]at(4.97,1.3){rightward};
\node at(1.35,.15){bottom rim};\node at(1.35,2.23){top rim};
\end{tikzpicture}\end{center}
\vspace{.15in}
Same winding, different routes: \hrulefill
