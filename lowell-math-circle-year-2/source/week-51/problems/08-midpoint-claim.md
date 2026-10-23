+++
id = "w51.midpoint-claim"
title = "The middle values do not give one exact gap"
grades = ["2-3", "4-5"]
route = "return"
page = "same"             # shares the gap page
kernel = "14-11=3 is one possible gap, not a guaranteed one: the settings at the two bounds give 1 and 5."
+++

## prompt @167
Someone subtracts the two middle values and announces one exact gap. Can you choose allowed strips that show why this is unsafe?

## figure
ruler(12,216)

## key
Subtracting middle values gives 14-11=3, which is possible but not guaranteed. Either 13 and 12 (gap 1) or 15 and 10 (gap 5) defeats the assertion of one exact gap. No probabilistic claim makes the midpoint more authoritative.
