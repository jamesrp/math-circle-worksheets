+++
id = "w31.visible-dots"
title = "Every dot visible from O"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"
kernel = 'A dot (a, b) is visible from O exactly when a and b have no common factor larger than 1: 13 dots on the 0-4 grid, 25 on the 0-6 grid.'
+++

## prompt @8.4 [K-1]
Which dots can you see from O? Circle every visible dot.

## prompt @8.4 [2-3]
Circle every dot visible from O. For three hidden dots, mark their first blocker.

## prompt @8.4 [4-5]
Find three visible targets and three hidden targets with different numbers of blockers. Mark each blocker.

## figure [K-1]
draw(('dots', 4, 11.5, 4, 2))

## figure
draw(('dots', 3, 11, 6, 2))

## key [K-1]
\emph{Print guide, p. 2.} Each row gives the across-coordinates x of \emph{all} visible dots at height y. Exclude O. The K grid has 13 visible dots; the 0-6 grid has 25.

\begin{tabular}{lll}
Height y & K grid: x=0...4 & Larger grid: x=0...6 \\
0 & 1 & 1 \\
1 & 0,1,2,3,4 & 0,1,2,3,4,5,6 \\
2 & 1,3 & 1,3,5 \\
3 & 1,2,4 & 1,2,4,5 \\
4 & 1,3 & 1,3,5 \\
5 & Outside this grid & 1,2,3,4,6 \\
6 & Outside this grid & 1,5 \\
\end{tabular}

## key [2-3]
\emph{Print guide, p. 3.} Use the complete catalog on page 2. Three possible first-blocker marks: (6,4) $\to$ (3,2), (6,3) $\to$ (2,1), (4,4) $\to$ (1,1). Accept any three correct hidden targets.

## key [4-5]
\emph{Print guide, p. 4.} Sample visible targets: (1,1), (2,1), (3,2). Hidden examples with distinct counts: (2,2) has (1,1); (3,3) has (1,1), (2,2); (4,4) has (1,1), (2,2), (3,3). Other correct choices are welcome.
