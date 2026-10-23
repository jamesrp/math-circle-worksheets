+++
id = "w43.k1-missing-ticket"
title = "A ticket goes missing"
grades = ["K-1"]
route = "return"
kernel = "Removing first ticket 1, 2 or 3 means A, B or C can never be first, so exactly two rows become impossible."
+++

## prompt @0
Remove one ticket from the first set, leaving the second set alone. Which rows become impossible for each missing ticket?

## figure
k1_missing_ticket_rows()

## key
Remove first ticket \textbf{1}: ABC and ACB become impossible. Remove \textbf{2}: BAC and BCA become impossible. Remove \textbf{3}: CAB and CBA become impossible. Each removal prevents one particular card from ever being first. The second set remains \{2,3\}.
