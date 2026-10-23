+++
id = "w04.m-exactly-three-starts"
title = "Exactly 3 starts"
grades = ["2-3"]
route = "return"
page = "new"
+++

## prompt
On each of these rings, find a hop bigger than 3 that makes you start exactly 3 times, and draw it. If a ring has no such hop, explain why.

## figure
parts(grid([ring_cell(n, 1.2, [f"{n} dots, hop \\blank"], 3.6) for n in (9, 16, 18, 15)], 2, 3.6, before='0.25in', between='0.35in'),
      lines(3, before='0.1in'))
