+++
id = "w86.fold-rule"
title = "The fold rule and the path example"
kind = "setup"
grades = ["4-5"]
route = "return"
+++

## text @0,0 w=192 size=11
You may remove a dot v when a neighboring dot u can reach every place v can reach by staying or taking one road. This is a fold, written v $\to$ u. Remove v and all its roads. Test the next fold on the remaining map.

## figure
fold_example('Original: w can reach w, x.', 'Compare: x can reach w, x, y.', r'w $\to$ x: remove w and road w--x.')
