+++
id = "w24.compare-three-decks"
title = "Compare A, B and C"
grades = ["2-3", "4-5"]
route = "first"
page = "same"
kernel = "A beats B, B beats C and C beats A, each 5 pairs to 4 (chance 5/9); no deck beats both others, and every deck totals 15, so totals do not decide."
+++

## prompt @9.02 [2-3]
For each pair of decks, find which deck wins more of the possible card pairs. Is there a deck that wins more pairs than both of the others?

## prompt @9.02 [4-5]
For each pair of decks, find how many of the possible card pairs each deck wins. Is there a deck that wins more than half its pairs against both others? Do the three deck totals settle this question?

## figure [2-3]
art(decks(ABC,7.3))

## figure [4-5]
art(decks(ABC,7.15))
