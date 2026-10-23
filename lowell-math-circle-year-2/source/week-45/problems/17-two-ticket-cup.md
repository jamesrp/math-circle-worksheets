+++
id = "w45.two-ticket-cup"
title = "A two-ticket cup with a fair red clue"
grades = ["K-1", "2-3"]
route = "return"
page = "same"
kernel = "A red clue ties exactly when the cup holds one of tickets 1 and 2 and ticket 3: {1,3} and {2,3}."
+++

## prompt @17 [K-1]
Find every two-ticket cup where red showing gives the hidden colors the same chance. Red must sometimes show.

## prompt @19 [2-3]
Keep the cards and choose two tickets for the cup. Red must sometimes show. Find every pair that makes a red clue give each hidden color the same chance.

## figure [K-1]
box(0,20,7,2.8) + box(10,20,7,2.8)

## figure [2-3]
space(22,2)
