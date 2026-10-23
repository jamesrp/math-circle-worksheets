+++
id = "w30.two-weights-one-to-four"
title = "Every two-weight kit for targets 1 to 4"
grades = ["K-1", "4-5"]
route = { "K-1" = "return", "4-5" = "first" }
page = { "K-1" = "new", "4-5" = "same" }
kernel = 'Only 1 and 3 balances every target from 1 to 4: two weights give at most four positive targets, so there can be no repeat and no gap.'
+++

## prompt @0 [K-1]
Choose two different weights from 1, 2, 3 and 4. Find every kit that can balance all four targets: 1, 2, 3 and 4.

## prompt @10 [4-5]
Choose two different whole-number weights that balance every target from 1 through 4. Find every possible kit.

## figure [K-1]
draw(('weights', [1, 2, 3, 4], 2), ('blanks', [2, 4], 6), ('ruled', 17, 5))

## figure [4-5]
draw(('blanks', [2, 4], 13), ('ruled', 23, 1))
