+++
id = "w38.predict-cut"
title = "Predict, then cut along the middle line"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "Cutting A along its middle makes two annuli; cutting B makes one piece, an annulus with two edges."
+++

## prompt @27 [K-1]
Guess how many pieces each band will make when an adult cuts its middle line. Ask the adult to cut A and B, and draw what you get.

## prompt @27 [2-3]
Predict how many connected pieces a middle-line cut will make in A and B. Ask an adult to make both cuts and record what happened.

## prompt @27 [4-5]
Predict the number of connected pieces after a middle-line cut in A and B. Have an adult cut both bands, then count the pieces and the boundary components of each piece.

## figure
strip(25,78,73,28,False,True,'A')+strip(124,78,73,28,True,True,'B')+lab(58,125,'I predict: ______',12)+lab(158,125,'I predict: ______',12)+blank(16,141,84,94)+blank(112,141,84,94)+lab(58,244,'after cutting A',11)+lab(154,244,'after cutting B',11)
