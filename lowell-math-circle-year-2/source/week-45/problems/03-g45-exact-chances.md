+++
id = "w45.g45-exact-chances"
title = "Exact hidden-color chances for each clue"
grades = ["4-5"]
route = "first"
page = "same"
kernel = "Red shows on tickets 1, 2, 3, which hide red, red, blue: P(hidden red | red showing) = 2/3. By symmetry P(hidden blue | blue showing) = 2/3."
+++

## prompt @14
Given only a red showing color, determine the chances of the hidden colors exactly. Do the same for a blue showing color.

## figure
bins(18,('red showing','blue showing'),h=3.8)
