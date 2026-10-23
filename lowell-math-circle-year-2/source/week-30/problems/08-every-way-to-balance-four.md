+++
id = "w30.every-way-to-balance-four"
title = "Every way to balance 4 with 1, 3, 8 and with 1, 3, 9"
grades = ["2-3"]
route = "return"
kernel = 'With 1, 3, 8 target 4 balances two ways (1 + 3, and 8 against 4 + 1 + 3); with 1, 3, 9 only one.'
+++

## prompt @0
Use weights 1, 3 and 8 to balance 4 in every possible way. Then find every way to balance 4 with 1, 3 and 9.

## figure
three_boards_each(['1, 3, 8', '1, 3, 9'])
