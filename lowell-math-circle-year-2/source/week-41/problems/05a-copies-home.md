+++
id = "w41.copies-home"
title = "Four trips home that finish in different copies"
grades = ["4-5"]
route = "first"
kernel = "A trip returns to H exactly when both net step counts are multiples of 3; different multiples give different copies of H."
+++

## prompt @27
Make four different trips from H back to H. Choose trips whose replays finish in different copies of H on the repeated map.

## figure
tile(18,71,180,True,True,True,15)

## key
Four examples returning to H in different copies: RRR$\to$(1,0), LLL$\to$($-$1,0), UUU$\to$(0,1), DDD$\to$(0,$-$1). Many other choices are valid; the copy pair must differ for each of the four.

A follow-up to ask aloud: which copies can a trip home of exactly 4, 5 or 6 steps reach? Four steps: only (0,0). Five steps: the four neighbouring copies ($\pm$1,0) and (0,$\pm$1). Six steps: (0,0), the four diagonal copies ($\pm$1,$\pm$1), and ($\pm$2,0) and (0,$\pm$2).
