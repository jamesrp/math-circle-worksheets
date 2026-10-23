+++
id = "w73.whole-sheet-rule"
title = "A rule for every point with stretch at most 2"
grades = ["4-5"]
route = "return"
page = "new"
kernel = "The rule (x/2, 2y) moves the whole sheet onto the square with every pair stretched at most twice."
+++

## prompt
Make a rule that moves every point of the rectangle into the square, with no gaps, overlaps or tears. Each named side must land on the same named side. Keep every new distance at most twice its old distance. Draw where the dotted lines go. Your partner chooses two points anywhere and tests your rule.

## text
\begin{center}\begin{tikzpicture}[x=.94in,y=.94in,font=\small]
\draw[dotted,thick,step=.5] (0,.5) grid(4,1.5);\draw[thick](0,.5)rectangle(4,1.5);
\node at(2,.17){bottom: 4 units};\node at(2,1.8){top};\node[rotate=90]at(-.35,1){left: 1 unit};\node[rotate=90]at(4.32,1){right};
\begin{scope}[shift={(4.9,0)}]\draw[thick](0,0)rectangle(2,2);\node at(1,-.32){bottom: 2 units};\node at(1,2.3){top};\node[rotate=90]at(-.35,1){left};\node[rotate=90]at(2.35,1){right: 2 units};\end{scope}
\end{tikzpicture}\end{center}
My rule for every point:
\answerline\answerline
\vspace{.25in}
