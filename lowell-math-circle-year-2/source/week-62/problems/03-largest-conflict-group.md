+++
id = "w62.largest-conflict-group"
title = "Fewest slots against the largest all-conflicting group"
grades = ["shared"]
route = "first"
page = "new"
kernel = 'A 5-cycle with a branch needs 3 slots though its largest all-conflicting group has 2; a 6-cycle with branches needs 2.'
+++

## text
\gdef\band{Grades 2--5}

## prompt
Find the fewest slots for each network. Also find the largest group of cards in which every pair conflicts. Does that group's size always give the fewest slots?

## figure
center(graph("p3-five-branch",C5,C5e))
+minimum_line()
+center(graph("p3-six-branches",C6B,C6Be))
+minimum_line()
+notespace(1)
