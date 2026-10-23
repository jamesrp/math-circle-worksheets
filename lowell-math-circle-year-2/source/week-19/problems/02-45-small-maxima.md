+++
id = "w19.45-small-maxima"
title = "Largest collections from the four- and eight-card decks"
grades = ["4-5"]
route = "first"
page = "same"
kernel = "The maxima are 2 and 3, and a cover by that many nested rows proves no larger collection works."
+++

## prompt @2.14
For each deck, find the largest collection you can. Explain why no larger collection can work.

## figure
deck(D4,3.10,s=.83,gap=.29)+line(5.57)+deck(D8,5.89,cols=8,s=.69,gap=.20)
