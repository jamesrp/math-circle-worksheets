+++
id = "w47.seven-sites"
title = "Lowest and highest landscapes on seven sites"
grades = ["K-1", "2-3", "4-5"]
route = "return"
kernel = "With clues 1, 3, 1 at sites 0, 4, 6 there are 10 landscapes; the pointwise lowest (1,0,1,2,3,2,1) and highest (1,2,3,4,3,2,1) are themselves landscapes, with the least and greatest totals 10 and 16."
+++

## prompt [K-1]
Make three different landscapes with these clues.

## prompt [2-3]
Make a landscape with the fewest blocks, then one with the most blocks. Keep all three clues.

## prompt [4-5]
Make one landscape that is as low as possible at every site, and one that is as high as possible at every site. Explain why no marker can go beyond yours.

## figure
board(25,47,7,5,{0:1,4:3,6:1})+row(18,176,[None]*7,dx=23)+row(18,207,[None]*7,dx=23)
