+++
id = "w41.change-trip"
title = "Change RRRUUU into UUURRR"
grades = ["4-5"]
route = "return"
page = "new"
kernel = "Nine square slides, one per square between the trips, change RRRUUU into UUURRR."
+++

## prompt @27
Change the first trip into the second using the allowed moves. Keep the same starting copy.

## figure
arrtrip(19,45,81,'RRRUUU',13)+arrtrip(116,45,81,'UUURRR',13)+ruled(68,248,12)

## key
One full nine-slide sequence is: RRRUUU $\to$ RRURUU $\to$ RURRUU $\to$ URRRUU $\to$ URRURU $\to$ URURRU $\to$ UURRRU $\to$ UURRUR $\to$ UURURR $\to$ UUURRR.

Each step swaps one adjacent R,U to U,R through one square of cell centers; its two subpath endpoints stay fixed. The whole route starts in the same copy throughout.
