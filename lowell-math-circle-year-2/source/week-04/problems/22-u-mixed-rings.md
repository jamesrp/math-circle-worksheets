+++
id = "w04.u-mixed-rings"
title = "Six mixed rings: pieces"
grades = ["4-5"]
route = "first"
page = "new"
+++

## prompt
Draw each of these, and write how many pieces it has.

## figure
grid([ring_cell(n, 1.0, [f"{n} dots, hop {k}", "pieces~\\bx"], 2.42) for n, k in [(10, 4), (9, 6), (15, 10), (16, 12), (18, 8), (24, 9)]], 3, 2.42, before='0.3in', between='0.45in')
