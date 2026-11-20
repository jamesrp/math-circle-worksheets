+++
id = "w04.u-pieces-without-drawing"
title = "Pieces without drawing"
grades = ["4-5", "2-5"]
route = "first"
page = "new"
+++

## prompt
Find how many pieces each of these drawings has, without drawing it. Then draw the first two on the rings to check.

## prompt [2-5]
Find how many times you will start for each of these, without drawing it. Then draw the first two on the rings to check.

## figure [2-5]
predict_pieces([(20, 8), (24, 10), (30, 12), (36, 27), (17, 5), (100, 35), (60, 45)], drawn=2, label="starts", Rc=1.72, gap=4.05, h=7.95)

## figure
predict_pieces([(20, 8), (24, 10), (30, 12), (36, 27), (17, 5), (100, 35), (60, 45)], drawn=2)
