+++
id = "w12.k1-six-dot-pairings"
title = "Every pairing of six dots on a circle"
grades = ["K-1"]
route = "first"
page = "same"             # shares page 1 with the rules
kernel = "Six fixed dots on a circle have exactly five noncrossing pairings: dot 1 can meet only 2, 4 or 6, which leave 2, 1 and 2 ways to finish."
+++

## prompt @119
Find every way to pair six dots.

## figure
k1_six_dot_mat_and_records()

## key
\emph{Print guide, p. 3.} The printed four-dot examples are 12|34 and 14|23; 13|24 crosses. The task is to find all five six-dot pairings in the gallery on page 6. Here 12 means the pair \{1,2\}; a vertical bar separates pairs. Do not count a rotated drawing as the same unless every numbered dot still has the same partner.
