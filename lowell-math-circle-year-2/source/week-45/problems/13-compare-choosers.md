+++
id = "w45.compare-choosers"
title = "Compare the two-ticket chooser with all six tickets"
grades = ["2-3", "4-5"]
route = "return"
page = "same"
kernel = "The two-ticket chooser gives hidden red 1/2; drawing from all six and keeping red rounds gives 2/3. The same clue can mean different things under different selection rules."
+++

## prompt @5 [2-3]
Compare this chooser with drawing from all six face tickets and keeping red-showing rounds. Do they give the same chances for the hidden color?

## prompt @5 [4-5]
Does this way of producing a red clue change the chance that red is hidden? Give an exact comparison with the six-face-ticket rule.

## figure [2-3]
bins(8.6,('two-ticket chooser','six-ticket chooser'),h=8) + space(19.5,3)

## figure [4-5]
box(0,7.2,18,7)
