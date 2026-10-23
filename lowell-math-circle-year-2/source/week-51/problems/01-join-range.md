+++
id = "w51.join-range"
title = "Shortest and longest join"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"             # shares page 1 with the rules
kernel = "A join of A in [4,6] and B in [3,4] can end anywhere in [7,10] and nowhere else: the extremes pair shortest with shortest and longest with longest."
+++

## prompt @119 [K-1]
Make the shortest and longest joins with these strips. Can you make a join ending exactly at 8?

## prompt @119
Find the tightest guaranteed range for the join. Someone claims it must end between 8 and 9; build allowed strips that defeat that claim.

## figure
band(12,164,4,6,'A')+band(12,204,3,4,'B')

## key
A is 4-6 and B is 3-4, so the tight join range is \textbf{[7,10]}. Extremes are 4+3=7 and 6+4=10. K-1 can make exactly 8 with 4+4 or 5+3. In the older task, either extreme defeats the claimed 8-9 guarantee. Every sum lies in [7,10], and both endpoints are allowed, so neither bound can improve.
