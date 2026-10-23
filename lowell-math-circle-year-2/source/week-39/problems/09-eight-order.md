+++
id = "w39.eight-order"
title = "Two rings in either order"
grades = ["2-3", "4-5"]
route = "return"
kernel = "On two rings joined at H, the order of whole ring trips matters: the same ring trips in another order can shorten to a different trip, and left, right, left backward, right backward cannot disappear."
+++

## prompt @27 [2-3]
Left forward (LF) is H to A to B and back to H, left backward (LB) is H to B to A and back to H, and right forward (RF) is H to C to D and back to H. Join these three ring trips in each of the six possible orders and shorten each journey. Which orders shorten to the same trip?

## prompt @27 [4-5]
Left forward is H to A to B and back to H, and right forward is H to C to D and back to H. From H, go left forward, right forward, left backward, then right backward. Can the whole trip disappear by removing out-and-back pairs?

## figure [2-3]
graph(56, 65, 24, EIGHT, EEDGES) + blank(16, 121, 180, 69)

## figure [4-5]
graph(40, 62, 34, EIGHT, EEDGES)

## key [2-3]
Write a for left forward (HABH), a$^{-1}$ for left backward (HBAH) and b for right forward (HCDH). Four orders shorten to HCDH: a a$^{-1}$ b, a$^{-1}$ a b, b a a$^{-1}$ and b a$^{-1}$ a, because a ring trip next to its backward trip cancels. The other two, a b a$^{-1}$ = HABHCDHBAH and a$^{-1}$ b a = HBAHCDHABH, contain no out-and-back pair, so they stay as they are and differ. The same three ring trips in a different order can give a different result.

## key [4-5]
The requested journey is HABHCDHBAHDCH, or ab a$^{-1}$ b$^{-1}$. No consecutive pair is an edge followed immediately by that same edge backward, including at H between circuits. Nothing can be removed, so the trip cannot disappear. H is the based endpoint and interior junction; it is not permission to split off or reorder a circuit.
