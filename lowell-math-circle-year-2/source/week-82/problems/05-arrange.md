+++
id = "w82.arrange"
title = "Arrange rows and stars"
grades = ["3-5"]
route = "return"
page = "new"
kernel = "Two rows and up to two stars make ten arrangements of three shapes: they match keeping order exactly when they have the same shape once each star waiting before a row joins that row, so a star between the rows vanishes into the second row; any two match if order may change."
+++

## prompt
Arrange two endless numbered rows and up to two $\bigstar$ kids on the table. A star or new row following a whole endless row comes after EVERY kid in that row.

## text
Find two different arrangements that can be matched while keeping order. Find two that can be matched only if order may change. Sketch your arrangements in the boxes. Give matching rules or explain the obstruction.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\foreach \y in {0,-6.3}{
 \draw[gray,rounded corners=3pt,line width=0.55pt] (0,\y) rectangle (16.1,\y-2.0);
 \draw[gray,rounded corners=3pt,line width=0.55pt] (0,\y-3.0) rectangle (16.1,\y-5.0);
}
\end{tikzpicture}
\end{center}
\vspace{0.25cm}
\ruleline
