+++
id = "w41.change-trip"
title = "Change RRRUUU into UUURRR"
grades = ["4-5"]
route = "return"
page = "same"
kernel = "Nine square slides, one per square between the trips, change RRRUUU into UUURRR."
+++

## prompt @217
Change the first trip into the second using the allowed moves. Keep the same starting copy.

## figure
arrtrip(19,245,81,'RRRUUU',13)+arrtrip(116,245,81,'UUURRR',13)

## key
One full nine-slide sequence is: RRRUUU $\to$ RRURUU $\to$ RURRUU $\to$ URRRUU $\to$ URRURU $\to$ URURRU $\to$ UURRRU $\to$ UURRUR $\to$ UURURR $\to$ UUURRR.

Each step swaps one adjacent R,U to U,R through one square of cell centers; its two subpath endpoints stay fixed. The whole route starts in the same copy throughout.
