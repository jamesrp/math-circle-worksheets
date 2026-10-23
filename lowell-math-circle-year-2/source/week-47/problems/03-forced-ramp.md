+++
id = "w47.forced-ramp"
title = "A right clue that forces every marker"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"             # shares page 2 with the starred marker
kernel = "With clues 0 and 4 four steps apart, every step must rise by 1, so the ramp 0, 1, 2, 3, 4 is forced; 4 is the only right-clue height that forces every site."
+++

## prompt @170 [K-1]
Move the right clue to 4. Find every landscape that works.

## prompt @170
Keep the left clue at 0. Choose a height for the right clue that forces every marker. Find all such right-clue heights.

## text @40,197 w=140 size=11
Shaded boxes are fixed clues.

## figure [K-1]
row(40,216,[0,None,None,None,4],(0,4))

## figure
row(40,216,[0,None,None,None,None],(0,4))
