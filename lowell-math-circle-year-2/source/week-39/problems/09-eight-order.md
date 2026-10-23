+++
id = "w39.eight-order"
title = "Two rings in either order"
grades = ["2-3", "4-5"]
route = "return"
kernel = "On two rings joined at H, left then right and right then left shorten to different trips, and left, right, left backward, right backward cannot disappear: order survives."
+++

## prompt @27 [2-3]
From H, go around the left ring through A, then the right ring through C. Trade only the order of the two full ring trips. Do the two journeys become the same after removing every immediate reversal?

## prompt @27 [4-5]
From H, go around the left ring through A, then the right ring through C, then the left ring backward, then the right ring backward. Can the whole trip disappear by removing immediate reversals?

## figure [2-3]
graph(25, 87, 41, EIGHT, EEDGES)

## figure [4-5]
graph(25, 84, 41, EIGHT, EEDGES)

## key [2-3]
Left then right is HABHCDH; right then left is HCDHABH. Neither contains any adjacent reversal, and the sequences are different. Therefore they remain different after all deletions. The common endpoint H and use of the same roads do not permit swapping their order.

## key [4-5]
The requested journey is HABHCDHBAHDCH, or ab a$^{-1}$ b$^{-1}$. No consecutive pair is an edge followed immediately by that same edge backward, including at H between circuits. Nothing can be removed, so the trip cannot disappear. H is the based endpoint and interior junction; it is not permission to split off or reorder a circuit.
