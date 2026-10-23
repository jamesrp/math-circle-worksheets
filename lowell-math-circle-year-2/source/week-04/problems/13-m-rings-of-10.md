+++
id = "w04.m-rings-of-10"
title = "Hops 2 to 5 on rings of 10"
grades = ["2-3"]
route = "first"
page = "new"
+++

## prompt
Draw hop 2, hop 3, hop 4 and hop 5 on these rings of 10 dots. Write how many times you started in the box under each drawing.

## figure
grid([ring_cell(10, 1.3, [f"hop {k}\\qquad\\bx"], 3.6) for k in (2, 3, 4, 5)], 2, 3.6, before='0.35in', between='0.45in')
