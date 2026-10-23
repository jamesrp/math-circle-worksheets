+++
id = "w62.add-lines"
title = "Fewest added lines to need three slots"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'The tree needs one added line (closing an odd cycle); the six cards with no lines need three (a triangle).'
+++

## text
\gdef\band{Grades 4--5}

## prompt
Add the fewest conflict lines you can so each network can no longer fit in two slots. Join only different circles that have no line yet. Show why fewer added lines cannot work.

## figure
center(graph("p6-tree",TREE6,TREE6e))
+r"\begin{center}Added lines: \rule{1.2in}{0.4pt}\end{center}"
+"\n"
+center(graph("p6-empty",EMPTY6,[]))
+r"\begin{center}Added lines: \rule{1.2in}{0.4pt}\end{center}"
+notespace(1.6)
