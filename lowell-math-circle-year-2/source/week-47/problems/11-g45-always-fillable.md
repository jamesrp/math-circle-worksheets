+++
id = "w47.g45-always-fillable"
title = "Must pairwise-consistent clues be fillable?"
grades = ["4-5"]
route = "return"
kernel = 'Yes: if every pair of clues differs by at most their distance, the lower envelope $L(i) = \max(0, \max_c(a_c - |i - c|))$ is a landscape through every clue (discrete McShane extension).'
+++

## prompt
A row has at least one clue. Suppose every pair of clues differs by no more than the steps between them. Must the whole row be fillable? Give a construction that always works, or a set of clues that defeats the claim.

## figure
board(25,40,7,5)
