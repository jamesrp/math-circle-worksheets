+++
id = "w43.no-self-swaps"
title = "Forbid swapping a slot with itself"
grades = ["4-5"]
route = "return"
page = "same"
kernel = "Without self-swaps only BCA and CAB occur: two orders at 1/2 each, not a fair shuffle of six."
+++

## prompt @15
Another rule forbids swapping a slot with itself. Swap slot 1 with slot 2 or 3, then swap slots 2 and 3. Find every possible final order. Is this a fair shuffle of all six orders?

## figure
start_row_and_lines('ABC', 19, 2)

## key
First swap 1 with 2: ABC $\to$ BAC $\to$ BCA after swapping 2 with 3. First swap 1 with 3: ABC $\to$ CBA $\to$ CAB. Thus only BCA and CAB occur. If the initial two choices are equally likely, these have probability 1/2 each, but four orders have probability zero. It is not a fair shuffle of all six orders.
