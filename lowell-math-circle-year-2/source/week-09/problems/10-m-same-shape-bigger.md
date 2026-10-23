+++
id = "w09.m-same-shape-bigger"
title = "Same shape, bigger tables"
grades = ["2-3"]
route = "first"
page = "new"
+++

## prompt
Trace the path on each table, and write the corner where the ball stops and the number of bounces.

## figure
vspace(0.1) + row([table(w, h, 0.5, label=lab(w, h)) for w, h in [(1, 2), (2, 4), (3, 6)]], gap=1.2)
+ vspace(0.5) + row([table(w, h, 0.5, label=lab(w, h)) for w, h in [(1, 3), (2, 6), (4, 6)]], gap=1.2)
