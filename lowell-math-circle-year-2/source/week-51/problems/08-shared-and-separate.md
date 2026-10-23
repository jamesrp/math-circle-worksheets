+++
id = "w51.shared-and-separate"
title = "The same A twice, or A against a separate B"
grades = ["K-1", "2-3", "4-5"]
route = "return"          # after the gap page, which meets the cross pairing alone (card fix 3)
kernel = "(A+4)-(A+1) is exactly 3 because the same A cancels, while (A+4)-(B+1) with A and B separately in [4,6] spreads over [1,5]."
+++

## prompt [K-1]
Find how small and how big each end gap can be. Start at 0. Both A's in the top picture are the same length. Each try may use new lengths.

## prompt
Compare the gaps between the right ends of these joins, starting at 0. Repeated A means the same unchanged length; B may vary separately. Find the tightest range for each gap.

## figure
band(12,40,4,6,'A')+band(12,79,4,6,'B')

## text @12,113 size=10
The white pieces are exactly 4 and 1 units long.

## figure
comparison(126,True)+ruler(12,161)+comparison(188,False)+ruler(12,223)

## key
Top comparison: A+4 versus that same A+1. The end gap is always \textbf{3}; both smallest and largest gaps are 3, because the shared A cancels.\par
Bottom comparison: A+4 versus B+1, with A and B each separately allowed from 4 to 6. The tight gap is \textbf{[1,5]}. Minimum: A=4,B=6 gives 8-7=1. Maximum: A=6,B=4 gives 10-5=5. The two extremes use different values of A, since each try may use new lengths. Intermediate values are possible too. The diagram shows one setting, not a promise that the shaded pieces always retain their drawn lengths.
