+++
id = "w14.pentagon-loop"
title = "A loop through the pentagon fillings"
grades = ["K-1", "2-3"]
route = "return"
kernel = "Following the pentagon's five-cycle visits every filling once and returns in five flips, an odd number."
+++

## prompt [K-1]
Follow the arrows, changing one inside line each time. Can you fill every shape differently and come back to the top filling with one last change?

## prompt [2-3]
Start with this filling. Change one inside line at a time, keeping the polygon filled with triangles, and get back to this filling after an odd number of changes. Show every filling along your route.

## figure [K-1]
k1_ring()

## figure [2-3]
large_plus_copies(5,fan(5,0),'letters')

## key [K-1]
Yes. Name a pentagon filling by the corner where its two diagonals meet. The route $1,3,5,2,4,1$ visits every other filling once and returns in five changes. The route in the opposite direction works too. Its complete diagonal sets are
\[
\{13,14\}\to\{13,35\}\to\{25,35\}\to
\{24,25\}\to\{14,24\}\to\{13,14\}.
\]
Each arrow replaces exactly one line. The pentagon map on page 6 shows why all five fillings have been visited. The ring's top board is the fan at 1; four blank boards take four changes, and the last arrow home is the fifth. Only the first change is a choice; each later one is forced, since the other change goes back. Useful stopping point. Children who build and explain this five-step loop have encountered a genuine odd cycle. They do not need the word ``parity'' or the older packet's distance formula.

## key [2-3]
An odd return route is $F_A,F_C,F_E,F_B,F_D,F_A$, with five flips. The complete sets are the K--1 P6 route with letters replacing numbers. No shorter odd return is possible: the pentagon's flip map (Problem 5) has no loops or triangles. An immediate out-and-back takes two flips and does not meet the odd condition. Children find this route before drawing the map; Problem 5 then shows it as the map's cycle.

## hints [K-1]
Lay the five Problem 2 boards beside the ring. Ask which of them can follow the current picture after one change. A child who reaches a filling already on the ring has gone back; look for the other change.

## hints [2-3]
Ask children to count \emph{moves}, not pictures, along their route. Six listed pictures represent five flips when the first is repeated at the end.
