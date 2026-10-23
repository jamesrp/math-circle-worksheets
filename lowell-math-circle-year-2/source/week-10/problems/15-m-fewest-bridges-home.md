+++
id = "w10.m-fewest-bridges-home"
title = "Fewest new bridges for a walk that comes home"
grades = ["2-3"]
route = "return"
+++

## prompt
In each town, draw as few new bridges as you can so that a walk can pick up every
counter and end on the island where it started.

## figure
figs([[town(5, house('m5a'), line=None), town(5, rotate(k4('m5b'), 90), line=None)]],
     [[town(5, rotate(h_shape('m5c'), 90), line=None)]], align='bottom')
