+++
id = "w46.k1-two-instructions"
title = "Two instructions: a match and a miss"
grades = ["K-1"]
route = "first"
kernel = "After 1->R and 3->B only the middle color survives, so two different starts end matching exactly when their middle colors agree."
+++

## prompt @0
Use these two instructions. Make two different starts that end matching, and a pair that ends different.

## figure
story(2,2.3,[(1,'R'),(3,'B')]) + board_pair(0,4.6,'','',1.6) + board_pair(10,4.6,'','',1.6)
