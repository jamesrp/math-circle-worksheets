+++
id = "w09.trace-six-tables"
title = "Trace six tables: corner and bounces"
grades = ["2-3", "4-5"]
route = "first"
+++

## prompt
Trace the path on each table. Under each table, write the corner where the ball stops and the number of bounces.

## figure [2-3]
row([table(w, h, 0.5, label=lab(w, h)) for w, h in [(2, 3), (3, 2), (1, 4)]], gap=1.1)
+ vspace(0.45) + row([table(w, h, 0.5, label=lab(w, h)) for w, h in [(3, 4), (4, 3), (3, 5)]], gap=1.1)

## figure [4-5]
row([table(w, h, 0.5, label=lab(w, h)) for w, h in [(2, 3), (3, 2), (1, 4), (3, 4)]], gap=0.75)
+ vspace(0.2) + row([table(w, h, 0.5, label=lab(w, h)) for w, h in [(6, 4), (3, 5)]], gap=1.5)
