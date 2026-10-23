+++
id = "w20.23-fill-together"
title = "Fill every circle at once"
grades = ["2-3"]
route = "first"
kernel = "Several circles must work on one unchanged board; paths take equal steps and the tree has the filling 4, 6."
+++

## prompt @7.62
Fill every circle so that all circles on a board work at once.

## figure
numeric_chain_example(9.18,9.86,divide=r'\div ') + path(6.80,(0,9)) + path(5.55,(2,11)) + path(4.30,(3,3)) + tree(3.65,1.98,(0,6,8))
