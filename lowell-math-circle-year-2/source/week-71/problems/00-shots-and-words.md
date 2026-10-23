+++
id = "w71.shots-and-words"
kind = "setup"            # unnumbered shared rules, the AD example and the window macros
title = "Shots, bounce words and the AD example"
grades = ["4-5"]
route = ["first", "return"]
+++

## figure
windows()

## text
A shot starts inside the room and bounces off its walls. Record the wall letters in the order hit. Stop after the last letter you want to record. A shot that hits a corner is not allowed.

One partner draws a shot with a ruler; the other checks it. To check a bounce, reflect the next room across the wall. The shot continues in a straight line through the reflected copy. Swap jobs for the next shot.

\begin{center}
\begin{tikzpicture}[scale=.50]
\draw[thick](0,0)rectangle(4,4);
\node[below]at(2,0){A};\node[left]at(0,2){B};\node[above]at(2,4){C};\node[right]at(4,2){D};
\fill(1,2)circle(2.5pt);\node[above,font=\scriptsize]at(1,2){start};
\draw[very thick,-{Stealth}](1,2)--(3,0)--(4,1)--(3,2);
\draw(3,0)circle(3pt);\draw(4,1)circle(3pt);
\node[below,font=\small]at(2,-.8){first A, then D: AD};
\end{tikzpicture}\hspace{.65in}
\begin{tikzpicture}[scale=.30]
\fill[gray!12](0,0)rectangle(4,4);
\draw[thick](0,0)rectangle(4,4);\draw[thick](0,0)rectangle(4,-4);\draw[thick](4,0)rectangle(8,-4);
\node[fill=white,inner sep=1pt]at(1,0){A};\node[fill=white,inner sep=1pt]at(4,-3){D};
\fill(1,2)circle(3pt);\draw[very thick,-{Stealth}](1,2)--(5,-2);
\draw(3,0)circle(4pt);\draw(4,-1)circle(4pt);
\node[below,font=\small]at(4,-4.7){the same shot through reflected copies};
\end{tikzpicture}
\end{center}
