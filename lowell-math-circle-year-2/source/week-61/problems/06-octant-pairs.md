+++
id = "w61.octant-pairs"
title = "Lune pairs on the three-right-angle triangle"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'Each lune pair covers half the ball; the triangle and its opposite are covered three times and every other region once, so 3/2 = 1 + 4T and T = 1/8.'
+++

## text
\band{4--5}
At a triangle corner, extend its two meeting sides to full great circles. Choose the lune containing the triangle and the opposite lune. Together they are a \textit{lune pair}. A starred point is exactly opposite its matching letter.

\begin{center}\begin{tabular}{cccc}
\pairinput & \paircircles & \pairfront & \pairback\\[-2pt]
\small Corner $A$ & \small Circles $AB$ and $AC$ & \small Pair at $A$: front & \small Same pair: back
\end{tabular}\end{center}
\begin{center}\renewcommand{\arraystretch}{1.05}\begin{tabular}{c|c|c}
Marked pair & Patch & Count\\\hline
$A$ & $X$ & $1$
\end{tabular}\end{center}
Each pair covers a patch once or not at all. Front and back show the same ball; these views omit hidden arcs.

## prompt
Use a triangle with three right angles on your ball. Extend its sides to full great circles. For each of its three corners, mark the lune pair. How many of the three pairs cover each of the eight regions? Use your counts to explain what fraction of the ball the triangle covers.

## text
\begin{center}\begin{tabular}{cc}
\countfront & \countback\\[-4pt]
\small Front & \small Back
\end{tabular}\end{center}
\begin{center}\renewcommand{\arraystretch}{1.45}\begin{tabular}{c|cccccccc}
Region & 1&2&3&4&5&6&7&8\\\hline
Pairs covering it & \rule{.30in}{.3pt}&\rule{.30in}{.3pt}&\rule{.30in}{.3pt}&\rule{.30in}{.3pt}&\rule{.30in}{.3pt}&\rule{.30in}{.3pt}&\rule{.30in}{.3pt}&\rule{.30in}{.3pt}
\end{tabular}\end{center}
\writing{2}
