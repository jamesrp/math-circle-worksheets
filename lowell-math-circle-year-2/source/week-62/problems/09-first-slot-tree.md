+++
id = "w62.first-slot-tree"
title = "First-slot orders on a tree"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'On this tree some order uses 4 slots and some 2; no order uses 5.'
+++

## text
\gdef\band{Grades 4--5}

## prompt
Find an order that makes the first-slot rule use four slots on this network. Find an order that uses two. Could any order use five? Explain.

## figure
center(graph("p8-tree",TREE8,TREE8e))
+r"\recordline{Four-slot order:}\recordline{Two-slot order:}"
+notespace(1.3)
+r"\hrule\vspace{1cm}\hrule"
+"\n"
