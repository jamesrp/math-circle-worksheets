+++
id = "w13.reachable"
title = "Every dot a change-walk can reach"
grades = ["4-5"]
route = "return"
kernel = "With two routes reserved on the bottleneck board, change-walk steps reach exactly s, A, B, C, D, and the arrows leaving that set are a closing set as large as the collection."
+++

## prompt
The thick arrows form two reserved routes. Find every dot you can reach from Start by change-walk steps. Find a smallest set of closing arrows, and explain why it matches the route collection.

## figure
reachable_board()

## key
The printed reservations on the bottleneck board are s-A-D-E-G-H-t and s-C-D-F-G-J-t. Exactly s,A,B,C,D are reachable by change-walk steps. A search witness: s-B-D reaches B and D; backward steps D-A and D-C then reach A and C. No change-step leaves that set because DE and DF are reserved and point outward; their backward directions start outside the set.

Thus \{DE,DF\} is a two-arrow closure matching the two reserved routes. No other dot is reachable: E,F,G,H,I,J,t all lie beyond those saturated arrows, and there is no unused outgoing crossing.

## hints
Hint: mark reached dots, examine every allowable step leaving one, and continue until no new dot can be marked. Do not stop after one failed branch.
