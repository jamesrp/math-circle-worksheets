+++
id = "w40.two-crossing-move"
title = "Colorings before and after a two-crossing move"
grades = ["2-3", "4-5"]
route = "return"
kernel = "Each choice of end colors has exactly one coloring before the move and one after, with the same end colors."
+++

## prompt @27 [2-3]
Color both pictures so matching end dots have the same colors. An arc may stop at an end dot here. Find every pair of colors at L and P that works.

## prompt @27 [4-5]
An arc may stop at an end dot here. Which colors at L and P allow both pictures to be colored with matching end-dot colors? Can the same choice have more than one completion? Explain.

## figure [2-3]
move_pictures(68)+move_arrow()+blank(16,151,180,40)

## figure [4-5]
move_pictures(70)+move_arrow()
