+++
id = "w27.23-circle-and-join"
title = "Circle the pairings that stay, join a blocker"
grades = ["2-3"]
route = "first"
page = "new"
# Second card run's should 4, October 23, 2026: "join two letters that both want to change" invited
# the one-sided check (both circles want to change in AY / BX of the bottom case, which stays).
kernel = "Top: only AX / BY stays, and A with X blocks AY / BX. Bottom: both pairings stay, although in each some letters wish for a change: a blocker needs a circle and a square who both want each other."
+++

## prompt @1.87 size=14
Circle every pairing that can stay. On each other pairing, join a circle and a square that would both rather be together.

## figure
two_pair_case(2.72,'k_unique_shared')+two_pair_case(6.40,'k_two_stable')+ln(.6,6.02,7.9,6.02)
