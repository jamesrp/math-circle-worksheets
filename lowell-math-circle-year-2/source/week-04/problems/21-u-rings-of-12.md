+++
id = "w04.u-rings-of-12"
title = "Hops 1 to 6 on rings of 12: pieces"
grades = ["4-5"]
route = "first"
+++

## prompt
Draw hops 1 to 6 on these rings of 12 dots. Write how many pieces each drawing has.

## figure
grid([ring_cell(12, 1.0, [f"hop {k}", "pieces~\\bx"], 2.42) for k in range(1, 7)], 3, 2.42, before='0.3in', between='0.4in')
