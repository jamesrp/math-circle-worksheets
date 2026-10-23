+++
id = "w42.other-bags"
title = "The rule on other bags"
grades = ["2-3"]
route = "return"
kernel = "For any bag with both colors, RB and BR have the same count of labeled pairs."
+++

## prompt @0
Keep your rule for each bag below. Which bags give the two shapes the same chance? Show a reason that does not depend on a lucky run.

## figure
bags_blank_grids()

## key
Both bags work. Grid heads: R1, R2, B1, B2 and R, B1, B2, B3. Two red/two blue gives four labeled RB and four BR outcomes out of 16. One red/three blue gives three RB and three BR outcomes. Reversing a pair pairs the outputs exactly, regardless of the observed random run.
