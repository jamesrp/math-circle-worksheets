+++
id = "w51.remove-same-a"
title = "Remove the very same A"
grades = ["4-5"]
route = "return"
page = "same"             # shares the fixed-total page
kernel = "(A+B)-A is exactly B, in [3,4]; subtracting the ranges [7,10] and [4,6] separately gives the valid but loose [1,6]."
+++

## prompt @185
Join A (4 to 6 units) to B (3 to 4 units), then remove that very same A. Someone uses the join's range and A's range separately to claim the remainder could be 1 to 6 units. Is that the tightest range? Explain with the pieces.

## key
The tight remainder range is \textbf{[3,4]}, exactly B's original range. Physically remove the same A that was joined: all that remains is B. The claimed [1,6] is a valid but unnecessarily wide enclosure obtained by treating the total and A as freely variable. Its extreme combinations cannot occur together: a total of 7 requires A=4,B=3, while a total of 10 requires A=6,B=4.
