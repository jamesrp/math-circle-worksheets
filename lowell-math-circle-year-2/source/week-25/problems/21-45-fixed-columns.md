+++
id = "w25.45-fixed-columns"
title = "Fixed columns and four free columns"
grades = ["4-5"]
route = ["first", "return"]
kernel = "A full and an empty column are forced, so only four free columns choose: 6 pictures, greatest shortest distance 2."
+++

## prompt @27
Find the fewest switches from the upper picture to the lower picture. How many different pictures share these counts? What is the largest number of switches ever needed between two of them?

## figure
h_fixed_columns()

## key
\emph{Print guide, p. 14.} \textbf{Answers:} the printed endpoints are 2 switches apart; there are 6 pictures with these counts; the greatest shortest distance is 2. Column 1 is full and column 3 is empty in every solution. The only choices are columns 2, 4, 5, 6; exactly two must have their counter in row A.

Start with free top pair \{2,4\}. Switch columns 2,5 to obtain \{4,5\}, then columns 4,6 to obtain \{5,6\}. The two unwanted top columns, 2 and 4, each have to be removed; a single switch removes at most one. Therefore two is both necessary and sufficient.
