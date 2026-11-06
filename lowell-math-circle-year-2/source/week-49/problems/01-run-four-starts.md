+++
id = "w49.run-four-starts"
title = "Run four starts to zero"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "The four starts reach all zeros in 3, 2, 2 and 4 moves; running the rule by hand makes its one-old-ring discipline concrete. Grades 4-5 run only (1,1,0,0) and (0,0,0,2), 3 and 4 moves, to reach their own problems sooner."
+++

## prompt @0 [K-1]
Build these starts and keep making new rings. Stop when all four towers are 0.

## prompt @0 [4-5]
Run each start until all four heights are 0. Which lasts longer?

## prompt @0
Run each start until all four heights are 0. Which lasts longest?

## figure [4-5]
four_starts(28, two=True)+big_mats(106)

## figure
four_starts(28)+big_mats(106)
