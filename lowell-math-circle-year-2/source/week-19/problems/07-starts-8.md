+++
id = "w19.starts-8"
title = "Keep the starting cards (eight-card deck)"
grades = ["K-1", "2-3"]
route = { "K-1" = "return", "2-3" = "first" }
page = "same"
kernel = "ABC and A/BC take no more cards, yet three is possible: being unable to add a card is not the same as largest."
+++

## prompt @5.04 [K-1]
Use the same deck. Keep each group of cards below and add as many cards as you can.

## prompt @5.33 [2-3]
Use the same deck. Keep each starting collection and add as many cards as you can. Does being unable to add a card mean a collection is as large as possible?

## figure [K-1]
deck([7],6.10,s=.78,x=.97)+deck([1],6.10,s=.78,x=4.7)+deck([3],8.05,s=.78,x=.97)+deck([1,6],8.05,s=.78,gap=.22,x=4.7)

## figure [2-3]
deck([7],6.40,s=.78,x=.97)+deck([1,6],7.65,s=.78,gap=.24,x=.97)+deck([3],8.90,s=.78,x=.97)
