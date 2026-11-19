+++
id = "w36.split"
title = "Split the nine tiles into three allowed threes"
grades = ["K-1", "2-3", "2-5"]
route = "first"
kernel = "The nine tiles split into three disjoint allowed threes in exactly four ways, the four parallel classes of the plane."
+++

## prompt [K-1]
Put all nine tiles into three allowed threes, one three in each row of the mat. Find different ways; the same three groups in other rows are not a new way.

## prompt [2-3, 2-5]
Split all nine tiles into three allowed threes. Colour each split on a board, one colour for each three. Find different splits; the same three groups in another order are not a new split.

## figure [2-3, 2-5]
boards((1.8,3.1),(11,3.1),(1.8,10.4),(11,10.4),(1.8,17.7),(11,17.7))

## figure
mat()
