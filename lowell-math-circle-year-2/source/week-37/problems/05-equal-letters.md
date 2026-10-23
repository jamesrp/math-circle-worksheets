+++
id = "w37.equal-letters"
title = "Make two letters equal"
grades = ["K-1", "2-3", "4-5"]
route = { "K-1" = "first", "2-3" = "return", "4-5" = "return" }
kernel = "Making any two of the four labels equal lets the mirror pair match, because the reflection that swaps the two equal corners combines with the mirror to give a turn."
+++

## prompt [K-1]
Change D to C on both models from Problem 2. Can you turn them to match now?

## prompt [2-3]
Change D to C on both models from Problem 2 and test for a match. Try other choices of two letters to make equal; start each trial with the original A, B, C, D mirror pair. Which choices allow a match by turning?

## prompt [4-5]
Choose two letters in the mirror pair and make them equal on both models. Start each trial with the original A, B, C, D mirror pair. Which choices allow a match by turning? Explain why your conclusion covers every choice.

## figure [4-5]
equal_letter_pair(ruled=[17,19,21,23])

## figure
equal_letter_pair()

## key [K-1]
Yes. After D becomes C, the pair is A B C C versus A C B C in the same positional order. A one-third turn around the A axis sends the first model's front-left B to the second's front-right B, while the two Cs occupy the two C positions. Choose the turning direction that aligns B; the other labels then agree.

## key [2-3]
D becoming C allows a match, as above. Every other pairwise merge also allows a match: AB, AC, AD, BC, BD and CD. Start each test from the original A B C D / A C B D mirror pair; successive cumulative merges test a different question. The name kept for the merged pair does not change the result.

## key [4-5]
All six unordered choices of two labels allow a rotational match after merging, with the original mirror pair restored each time. One proof uses the reflection swapping the two equal vertices, then composes it with the mirror comparison to obtain an orientation-preserving symmetry. Details follow on page 5.
