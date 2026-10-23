+++
id = "w12.pairings-to-paths"
title = "Paths for three six-dot pairings"
grades = ["2-3"]
route = "first"
page = "same"             # shares page 2 with the path code
kernel = "Reading a noncrossing pairing as U at each first end and D at each second end gives a path that never dips below its start: its height counts the strings still open."
+++

## prompt @120
Draw the path for each pairing, starting at the marked dot. How does the height of each path compare with its starting level?

## figure
pairings_to_paths()

## key
\emph{Print guide, p. 5.} Worked example: UDUUDDUD, from 12|36|45|78. For the three unanswered cases, top to bottom: UUUDDD, UUDDUD, UDUDUD. Their height sequences, including the start, are 0,1,2,3,2,1,0; 0,1,2,1,0,1,0; and 0,1,0,1,0,1,0. All stay at or above the starting level and end there. Height counts opened pairs that have not yet closed; that number cannot be negative.
