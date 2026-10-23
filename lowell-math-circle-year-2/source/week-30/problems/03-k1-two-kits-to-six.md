+++
id = "w30.k1-two-kits-to-six"
title = "Kit 1 and 4 against kit 1 and 3"
grades = ["K-1"]
route = "first"
kernel = 'Kit 1 and 4 balances 1, 3, 4 and 5 (missing 2 and 6); kit 1 and 3 balances 1 to 4 with no gap, so the spread-out kit is not the better one.'
+++

## prompt @0
Try weights 1 and 4, then weights 1 and 3. Does either kit balance more targets from 1 through 6?

## figure
draw(('weights', [1, 4], 2), ('weights', [1, 3], 2, 9), ('blanks', [2, 5], 10)) + k1_kit_strips()
