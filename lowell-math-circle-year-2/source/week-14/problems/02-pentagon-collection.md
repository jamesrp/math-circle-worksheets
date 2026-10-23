+++
id = "w14.pentagon-collection"
title = "Every filling of the pentagon"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = {"4-5" = "same"}
kernel = "A pentagon has exactly five fillings, the five fans: its two diagonals must share a corner, which then forces both."
+++

## prompt [K-1]
Find every way to fill this five-corner shape with triangles.

## prompt [2-3]
Find every filling of this five-corner polygon. How do you know none are missing?

## prompt @1.78 [4-5]
Find every filling of the five-corner polygon. Explain how your collection shows that none are missing.

## figure [K-1]
large_plus_copies(5)

## figure [2-3]
large_plus_copies(5,labels='letters')

## figure [4-5]
large_plus_copies(5,labels='letters',topcy=4.6,copyy=7.85)

## key [K-1]
There are five fillings, exactly the five fans on page 3 with letters replaced by numbers. Their diagonal sets are $\{13,14\}$, $\{24,25\}$, $\{13,35\}$, $\{14,24\}$, and $\{25,35\}$.

## key [2-3]
Exactly five pentagon fillings, displayed on page 3. The shared-corner argument there proves completeness.

## key [4-5]
The five pentagon fans on page 3 are the complete answer. The shared-corner proof or the root-edge classification proves no filling is missing.

## hints [K-1]
Let the child keep each discovery on a separate tracing. When ready to check completeness, ask whether the two lines meet at a corner and which corner it is.

## hints [2-3]
Sort a child's collection by the corner shared by its two diagonals. Keep corner names fixed so that all five fans remain distinct.
