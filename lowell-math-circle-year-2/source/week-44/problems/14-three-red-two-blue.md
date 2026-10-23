+++
id = "w44.three-red-two-blue"
title = "Stories to three red and two blue"
grades = ["2-3"]
route = "return"
page = "same"
kernel = "RRB, RBR and BRR each have chance $1/12$: reordering a color story does not change its chance."
+++

## prompt @17
A copying bag ends with three red and two blue. Find all possible three-draw color stories. Could they have different chances?

## figure
lines(21,3)

## key
The stories are RRB, RBR, BRR. Each has chance 1/12: RRB gives (1/2)(2/3)(1/4); RBR gives (1/2)(1/3)(2/4); BRR gives (1/2)(1/3)(2/4). Each represents two of the 24 marked histories. The intermediate bags differ, but these three ordered stories have equal probabilities.
