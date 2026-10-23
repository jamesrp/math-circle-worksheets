+++
id = "w34.five-ring"
title = "The five-ring"
grades = ["K-1", "2-3", "4-5"]
route = { "K-1" = "return", "2-3" = "first", "4-5" = "first" }
kernel = "On five spots two kinds still fail, because some flip axis always matches a two-kind pattern; three kinds work."
+++

## prompt [K-1]
Can two kinds of counter stop every turn and flip on this ring? Try three kinds too.

## prompt [2-3]
Find how few kinds of counter can stop every turn and flip on this ring. Can you explain why fewer kinds would fail?

## prompt [4-5]
Find the fewest kinds of counter that stop every turn and flip on the five-ring. Find an explanation that also works for the three-ring and four-ring.

## figure [K-1]
ring(9.2,13,5)

## figure
ring(9.2,13,5)+line(23)+line(24.1)
