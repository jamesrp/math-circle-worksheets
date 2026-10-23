+++
id = "w62.why-fewer-fail"
title = "Fewest slots, and why fewer cannot work"
grades = ["shared"]
route = "first"
page = "new"
kernel = 'The diamond needs 3 (a triangle), K4 needs 4, and the six-line network K2,3 needs only 2.'
+++

## text
\gdef\band{Grades 2--5}

## prompt
Find the fewest slots for each network. Show why fewer slots cannot work.

## figure
r"\begin{center}\begin{minipage}[c]{0.48\linewidth}\centering"
+"\n"
+graph("p2-diamond",DIAM,DIAMe)
+minimum_line()
+r"\end{minipage}\hfill\begin{minipage}[c]{0.48\linewidth}\centering"
+"\n"
+graph("p2-complete",K4,K4e)
+minimum_line()
+r"\end{minipage}\end{center}"
+"\n"
+center(graph("p2-many-lines",K23,K23e))
+minimum_line()
+notespace(1)
