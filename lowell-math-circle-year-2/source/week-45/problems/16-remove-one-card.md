+++
id = "w45.remove-one-card"
title = "Remove one card"
grades = ["K-1", "2-3"]
route = "return"
page = "same"
kernel = "Removing the blue/blue card leaves red clues from 1, 2, 3 (hidden red 2/3); removing red/blue leaves only red/red (red hides red for certain); removing red/red leaves only red/blue (red hides blue for certain). No single removal makes a tie."
+++

## prompt @2 [K-1]
Remove one card so red showing always hides red. Can you remove a different card so red showing always hides blue?

## prompt @2 [2-3]
Remove exactly one card. Can you make red showing hide red for certain? Hide blue for certain? Give the two hidden colors the same chance?

## figure [K-1]
cards(5) + box(0,11,18,4)

## figure [2-3]
cards(6) + box(0,11.5,18,5)
