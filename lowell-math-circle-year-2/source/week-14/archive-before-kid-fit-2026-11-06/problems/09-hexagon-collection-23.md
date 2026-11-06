+++
id = "w14.hexagon-collection-23"
title = "Every filling of the hexagon"
grades = ["2-3"]
route = "return"
kernel = "Sorting by the triangle on one boundary edge splits the hexagon's fillings into $5+2+2+5=14$, with no omissions or repeats."
+++

## prompt
Find every filling of this six-corner polygon. How do you know none are missing or repeated?

## figure
large_plus_copies(6,labels='letters')

## key
Student page 8 is labeled ``Problem 7 (continued)''. It supplies recording space for the same problem, not a second task. The complete hexagon collection has 14 fillings. Third corner B: five fillings. Diagonal BF cuts off triangle ABF, leaving a pentagon with five choices. Third corner C: two fillings. Triangle ACF leaves triangle ABC and quadrilateral CDEF. Third corner D: two fillings. Triangle ADF leaves quadrilateral ABCD and triangle DEF. Third corner E: five fillings. Triangle AEF leaves pentagon ABCDE. Why no omissions or repeats. A filling has exactly one triangle touching AF. Its third corner assigns it to exactly one group. The remaining polygon pieces can be filled independently; their complete smaller lists give $5+2+2+5=14$. No filling belongs to two groups.

## hints
Let children collect freely first. When a collection is hard to audit, ask which triangle touches AF in each picture. The student pages offer 17 recording outlines; the number of blank spaces is not the answer.
