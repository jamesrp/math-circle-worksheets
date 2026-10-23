+++
id = "w45.g45-every-subset"
title = "Every subset with a fair red clue"
grades = ["4-5"]
route = "return"
page = "same"
kernel = "A red clue is fair exactly when the cup holds ticket 3 and exactly one of tickets 1 and 2; tickets 4, 5, 6 are free: $2 \\times 2^3 = 16$ subsets."
+++

## prompt @2
Find every subset that makes red showing equally likely to hide red or blue. Your cup must sometimes show red; it may also show blue.

## figure
ticket_row(5) + box(0,8,18,6)
