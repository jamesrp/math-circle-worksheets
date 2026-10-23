+++
id = "w46.k1-two-instructions"
title = "Two instructions: a match and a miss"
grades = ["K-1"]
route = "return"
page = "same"
kernel = "After 1->R and 3->B only the middle color survives, so two starts end matching exactly when their middle colors agree."
+++

## prompt @15
Use these two instructions. Make one starting pair that ends matching and another that ends different.

## figure
story(2,17.5,[(1,'R'),(3,'B')]) + board_pair(0,20,'','',1.3) + board_pair(10,20,'','',1.3)
