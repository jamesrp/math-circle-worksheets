+++
id = "w73.stretch-rules"
kind = "setup"
title = "Stretch of a pair, with the 2 cm to 3 cm example"
grades = ["4-5"]
route = ["first", "return"]
+++

## text
Use paper dots, a ruler and strips of paper to compare straight-line distances.
Match dots with the same letters. A pair's stretch is its new distance divided by its old distance.
\begin{center}\begin{tikzpicture}[x=1cm,y=1cm,font=\small,>=Stealth]
\draw[thick] (0,0)--(2,0);\fill(0,0)circle(2pt);\fill(2,0)circle(2pt);
\node[above]at(1,0){old: 2 cm};
\draw[->](2.7,0)--(4,0);
\draw[thick](4.7,0)--(7.7,0);\fill(4.7,0)circle(2pt);\fill(7.7,0)circle(2pt);
\node[above]at(6.2,0){new: 3 cm};\node[below]at(6.2,-.1){stretch $1\frac12$};
\end{tikzpicture}\end{center}
