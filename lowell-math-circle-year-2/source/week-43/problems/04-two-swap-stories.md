+++
id = "w43.two-swap-stories"
title = "The six two-ticket stories"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"
kernel = "Left-to-right Fisher-Yates: the six equally likely ticket stories give six different rows, one per order."
+++

## prompt @7.3 [K-1]
Start with A B C and choose tickets to make every row. Can any row be made by two different ticket stories?

## prompt @7.3 [2-3]
Start with A B C. Match each two-ticket story to the final row it makes. Does this give each row the same chance?

## prompt @7.3 [4-5]
Does this two-swap rule give every order the same chance? Find all its choice stories and their final orders.

## figure [K-1]
k1_ticket_records()

## figure [2-3]
printed_stories()

## figure [4-5]
answer_box(10, 4.5)

## key [K-1]
Write a ticket story as (first ticket, second ticket), not as card names. The complete correspondence from ABC is:\par
\begin{tabular}{llll}\toprule Ticket story & Final row & Ticket story & Final row\\\midrule
(1,2) & ABC & (1,3) & ACB\\
(2,2) & BAC & (2,3) & BCA\\
(3,2) & CBA & (3,3) & CAB\\\bottomrule\end{tabular}\par
No final row comes from two different stories. First ticket 1, 2, or 3 puts A, B, or C first, and the second ticket chooses between the two remaining orders.

## key [2-3]
In the printed order, the mappings are (1,2) $\to$ ABC; (2,2) $\to$ BAC; (3,2) $\to$ CBA; (1,3) $\to$ ACB; (2,3) $\to$ BCA; (3,3) $\to$ CAB. The six stories are equally likely, and every row appears once, so this rule is fair.

## key [4-5]
For the two-swap rule from ABC, the complete list is (1,2) $\to$ ABC, (1,3) $\to$ ACB, (2,2) $\to$ BAC, (2,3) $\to$ BCA, (3,2) $\to$ CBA, (3,3) $\to$ CAB. Again each equally likely story has a different output, proving uniformity.
