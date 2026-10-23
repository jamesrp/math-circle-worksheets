+++
id = "w10.u-without-walking"
title = "Decide without walking, and where walks start and end"
grades = ["4-5"]
route = "first"
+++

## prompt
For each town, decide without walking it whether there is a walk that crosses every
bridge exactly once, and if there is, where it can start and end. If there is none, write
``none''. Then use counters to check each town that has a walk.

## figure
figs([[town(3, ladder('u3a', 4), line=11.0)]], [[town(3, bowtie('u3b'))]],
     [[town(3, grid_diag('u3c'))]])
