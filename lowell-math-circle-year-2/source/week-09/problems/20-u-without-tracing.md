+++
id = "w09.u-without-tracing"
title = "Six tables without tracing"
grades = ["4-5"]
route = "first"
page = "new"
+++

## prompt
Without tracing, find where the ball stops and how many times it bounces on each of these tables. Then trace the 6 by 10 table to check.

## figure
vspace(0.15) + record_beside([(6, 10), (8, 12), (12, 9), (7, 5), (5, 8), (20, 30)], table(6, 10, 0.5, label=lab(6, 10)))
