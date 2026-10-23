+++
id = "w14.pentagon-loop"
title = "A loop through the pentagon fillings"
grades = ["K-1", "2-3"]
route = "return"
kernel = "Following the pentagon's five-cycle visits every filling once and returns in five flips, an odd number."
+++

## prompt [K-1]
Start with this filling and change one inside line at a time. Can you visit every other filling once and then return?

## prompt [2-3]
Start with this filling and return to it after an odd number of flips. Show every filling along your route.

## figure [K-1]
large_plus_copies(5,fan(5,0))

## figure [2-3]
large_plus_copies(5,fan(5,0),'letters')

## key [K-1]
Yes. Name a pentagon filling by the corner where its two diagonals meet. The route $1,3,5,2,4,1$ visits every other filling once and returns in five changes. The route in the opposite direction works too. Its complete diagonal sets are
\[
\{13,14\}\to\{13,35\}\to\{25,35\}\to
\{24,25\}\to\{14,24\}\to\{13,14\}.
\]
Each arrow replaces exactly one line. The pentagon map on page 6 shows why all five fillings have been visited. Useful stopping point. Children who build and explain this five-step loop have encountered a genuine odd cycle. They do not need the word ``parity'' or the older packet's distance formula.

## key [2-3]
An odd return route is $F_A,F_C,F_E,F_B,F_D,F_A$, with five flips. The complete sets are the K--1 P6 route with letters replacing numbers. No shorter odd return is possible: this graph has no loops or triangles. An immediate out-and-back takes two flips and does not meet the odd condition.

## hints [K-1]
Lay the five earlier tracings around the table. Ask which ones can follow the current picture after one change. Keep the used tracings separate until it is time to return.

## hints [2-3]
Ask children to trace the joins with a finger and count \emph{moves}, not pictures. Six listed pictures represent five flips when the first is repeated at the end.
