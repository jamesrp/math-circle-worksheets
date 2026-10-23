+++
id = "w20.45-fractions"
title = "Whole numbers or fractions"
grades = ["4-5"]
route = "return"
kernel = "Whole-number squares can force fractions: a path from A to B with L steps is whole exactly when L divides B - A. The quarter cards fit no board."
+++

## prompt @9.86
Which boards can you fill with whole numbers? Fill the other boards using the fraction cards.

## figure
path(8.15,(0,1),1) + path(6.65,(0,3),2) + path(5.15,(0,2),1) + path(3.65,(0,1),2) + fraction_cards()
