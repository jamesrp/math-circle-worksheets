+++
id = "w50.finite-pieces"
title = "Could more, smaller pieces reach 200 mm?"
grades = ["4-5"]
route = "return"
page = "same"             # printed under the left-once path
kernel = "The diagonal is a limit of staircases in position, not in length."
+++

## prompt @184
A staircase may use more and smaller right-and-up pieces. Could any finite number of pieces give the same length as the 200 mm diagonal? Explain which distances can shrink and which length stays the same.

## key
No finite right/up staircase can have length 200 mm. Its total horizontal and vertical distances remain 160 and 120. With $n$ equal right-then-up steps, the largest vertical gap is $120/n$ mm, which can be made smaller than any specified positive tolerance by taking a sufficiently large finite $n$. The length remains 280 mm. The diagonal is a separate limiting curve with length 200 mm, not a last member of the staircase sequence.
