+++
id = "w94.k1-ruler-rules"
title = "Strips on a ruler that starts at 2"
grades = ["K-1"]
route = "first"
kind = "setup"
+++

## text
Use the four loose strips and the uncut row of squares. Each square is one unit. Lay strips along the ruler with both ends at printed marks.

\begin{center}\begin{tikzpicture}[x=12mm,y=10mm,font=\small]
\draw[fill=gray!15](0,.3)rectangle(1,1);\node[above]at(.5,1){strip};
\draw[->,thick](1.5,.65)--(2.2,.65);
\draw(2.7,.2)--(5.7,.2);
\foreach\x/\n in{2.7/7,3.7/8,4.7/9,5.7/10}{\draw(\x,.05)--(\x,.35);\node[below]at(\x,0){\n};}
\draw[fill=gray!15](3.7,.2)rectangle(4.7,.9);
\node[above]at(4.2,1){place};
\draw[->,thick](6.1,.65)--(6.8,.65);
\draw(7.3,.2)--(10.3,.2);
\foreach\x/\n in{7.3/7,8.3/8,9.3/9,10.3/10}{\draw(\x,.05)--(\x,.35);\node[below]at(\x,0){\n};}
\fill(8.3,.2)circle(2.5pt);\fill(9.3,.2)circle(2.5pt);
\node[above]at(8.8,1){mark both ends};\node[below]at(8.8,-.55){length: 1 unit};
\end{tikzpicture}\end{center}
