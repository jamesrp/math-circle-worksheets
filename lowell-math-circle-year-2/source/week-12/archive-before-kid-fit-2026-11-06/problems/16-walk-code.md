+++
id = "w12.walk-code"
kind = "setup"            # the walk code and a worked example, on page 2 with the next problem
title = "The walk code of a tree"
grades = ["4-5"]
route = ["first", "return"]
+++

## text @18,29 size=12.3
Start and finish at the root. Visit each child's whole branch from left to right before visiting the next child. Write U whenever you go away from the root along an edge and D whenever you return along it.

## figure
walk_code_example('Example:', 'On the path, U goes up and D goes down.')
