+++
id = "w19.largest-8"
title = "The largest collections from eight cards"
grades = ["K-1", "2-3"]
route = "first"
kernel = "The maximum is three, reached only by A/B/C and AB/AC/BC."
+++

## prompt @0.98 [K-1]
Make the biggest collection you can from this deck. Make a different collection just as big.

## prompt @0.98 [2-3]
Find the largest collection you can from this deck. Find every collection of that size.

## figure [K-1]
deck(D8,1.98,cols=8,s=.69,gap=.20)+line(4.77)

## figure [2-3]
deck(D8,1.89,cols=8,s=.69,gap=.20)+line(5.05)
