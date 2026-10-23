+++
id = "w47.starred-marker"
title = "How high and how low can the starred marker go?"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "With clues 0 at site 0 and 2 at site 4, the middle site can be exactly 0, 1 or 2: the left clue caps it at 2 and heights cannot go below 0."
+++

## prompt [K-1]
Put the starred marker as high as you can, then as low as you can.

## prompt
Which heights can the starred marker have? Make a landscape for each possible height and explain why the other heights cannot work.

## figure
board(40,50,5,4,{0:0,4:2},2)
