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
Circle every dot visible from O. Then find hidden targets with as many different numbers of blockers as you can, and mark each blocker.

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
\emph{Print guide, p. 4.} The 25 visible dots are in the catalog on page 2. A hidden target has one blocker fewer than the gcd of its coordinates, and on this grid the gcd is at most 6, so the possible counts are 1, 2, 3, 4 and 5. The diagonal shows them all: (2,2) has 1 blocker, (3,3) has 2, (4,4) has 3, (5,5) has 4 and (6,6) has 5. The axes work the same way, and (6,4) or (6,3) give 1 or 2 off the diagonal. Other correct choices are welcome.
