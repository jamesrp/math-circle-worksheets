+++
id = "w51.gap-extremes"
title = "Biggest and smallest gap between two strips"
grades = ["K-1", "2-3", "4-5"]
route = "return"
kernel = "The gap long minus short is smallest at the shortest long strip and the longest short strip, and largest the other way round."
+++

## prompt [K-1]
Put both starts at 0. Make the biggest gap between the ends, then the smallest.

## prompt
Align both starts at 0. Find the tightest guaranteed range for the gap between the ends. Build lengths that show neither bound can be improved.

## figure [K-1]
band(12,52,7,9,'long strip')+band(12,108,5,6,'short strip')

## figure
band(12,52,13,15,'long strip')+band(12,108,10,12,'short strip')

## key [K-1]
The long strip is 7-9 and the short strip 5-6. Largest gap \textbf{4} occurs at 9-5; smallest gap \textbf{1} occurs at 7-6. Each end moves separately. Subtracting shortest from shortest would not give the smallest gap.

## key [2-3, 4-5]
Long strip [13,15] minus short strip [10,12] has tight gap \textbf{[1,5]}. Use 13-12=1 and 15-10=5 to show both bounds are attained. Every allowed long length is at least 13 and every short one at most 12, so the difference is positive.
