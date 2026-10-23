+++
id = "w18.balanced-keys"
title = "Four-counter keys with two filled circles in each row"
grades = ["2-3"]
route = "return"
kernel = "Two rows with two filled circles each differ in an even number of places, so only opposite rows (four differences) work: six ordered keys."
+++

## prompt
Make four-counter keys for the two pictures with exactly two filled circles in each row. Find every key that always works. Swapping the pictures counts as a different key. Use more paper if needed.

## figure
''.join(keyed(0,y,'triangle','----',2,small=True)+keyed(9.5,y,'square','----',2,small=True) for y in [4,8.6,13.2,17.8])
