+++
id = "w18.four-pictures-five"
title = "A five-counter key for four pictures"
grades = ["2-3", "4-5"]
route = { "2-3" = "return", "4-5" = "first" }
kernel = "Four rows of length five can differ pairwise in at least three places, for example 01001, 01110, 10000, 10111."
+++

## prompt [2-3]
Make a key for all four pictures, with five counters in each row, that always lets the receiver know the picture. Explain how you know your key works.

## prompt [4-5]
Make a key for all four pictures, with five entries in each row, that always lets the receiver recover the picture. Explain why your key works.

## figure [2-3]
''.join(keyed(1.4,y,s,'-----',2,small=True) for y,s in zip([3.8,7,10.2,13.4],['triangle','square','star','diamond']))

## figure [4-5]
''.join(keyed(1.5,y,s,'-----',1.2,1.1,'number') for y,s in zip([3.4,5.65,7.9,10.15],['triangle','square','star','diamond']))
