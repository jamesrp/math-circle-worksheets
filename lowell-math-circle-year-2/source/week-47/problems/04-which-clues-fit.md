+++
id = "w47.which-clues-fit"
title = "Which clue sets can be completed?"
grades = ["K-1", "2-3", "4-5"]
route = "return"
kernel = "Clues can be completed exactly when every pair differs by at most their distance: 0 and 3 two steps apart cannot, while 3 and 0 four steps apart can."
+++

## prompt [K-1]
Which clues can go together? Build the ones that work.

## prompt
Decide which clue sets can be completed. Build the possible ones; explain what prevents the others.

## figure
clue_sets()
