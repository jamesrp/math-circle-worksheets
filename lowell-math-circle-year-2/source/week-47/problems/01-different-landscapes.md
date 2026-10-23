+++
id = "w47.different-landscapes"
title = "Different landscapes between two clues of height 1"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"             # shares page 1 with the rules
kernel = "With clues 1 at sites 0 and 4, many landscapes fit, and the middle site, two steps from each clue, can be any height from 0 to 3."
+++

## prompt @108 [K-1]
Make different landscapes with these clues.

## prompt @108
Make four different landscapes with these clues. Can the middle height be 0? Can it be 3?

## figure [K-1]
board(40,128,5,4,{0:1,4:1})

## figure
board(18,128,5,4,{0:1,4:1})+record_rows(120,128,[1,None,None,None,1],4)
