+++
id = "w04.m-rings-of-8"
title = "Hops 1 to 4 on rings of 8"
grades = ["2-3"]
route = "first"
+++

## prompt
Draw hop 1, hop 2, hop 3 and hop 4 on these rings of 8 dots. Write how many times you started in the box under each drawing.

## figure
grid([ring_cell(8, 1.3, [f"hop {k}\\qquad\\bx"], 3.6) for k in (1, 2, 3, 4)], 2, 3.6, before='0.3in', between='0.4in')
