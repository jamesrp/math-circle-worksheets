+++
id = "w39.c-to-f"
title = "Trips from C to F"
grades = ["K-1", "4-5"]
route = { "K-1" = "return", "4-5" = "first" }
page = "same"
kernel = 'Every trip from C to F, however long, shortens to C$\to$B$\to$D$\to$F, so no extra step survives and no two trips finish differently.'
+++

## prompt @190 [K-1]
Make a trip from C to F that uses every road. Can any such trip keep an extra road step after all immediate reversals are removed?

## prompt @225 [4-5]
Can two trips from C to F finish with different routes after every immediate reversal is removed? Explain using the roads.

## figure [K-1]
blank(16, 235, 180, 20)

## key [K-1]
CBABDEDBDF has nine steps, uses AB, BC, BD, DE, and DF, and ends at F. Delete B$\to$A$\to$B, D$\to$E$\to$D, and the later D$\to$B$\to$D excursion as they become adjacent to get CBDF. No such route can retain an extra step beyond C$\to$B$\to$D$\to$F once every immediate reversal is gone.

## key [4-5]
No. Every C-to-F journey reduces to CBDF. A reduced tree path cannot revisit a vertex, because the subjourney between repeated visits would be a nonempty closed reduced tree walk. It is thus simple, and a tree has only one simple path between the endpoints.
