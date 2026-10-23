+++
id = "w62.fewest-slots"
title = "Fewest slots for a path and a star"
grades = ["shared"]
route = "first"
kernel = 'The path and the star each need exactly 2 slots.'
+++

## prompt
Use your cards to schedule each network with the fewest slots you can.

## figure
center(graph("p1-path",P4,P4e)) 
+ minimum_line()
+center(graph("p1-star",STAR,STARe)) 
+ minimum_line()
