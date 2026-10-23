+++
id = "w11.order-square"
title = "Two orders from each start on the four-cycle"
grades = ["K-1", "2-3"]
route = "first"
kernel = "On the four-cycle, where B sends only to A and C, every legal order from a start still gives one finish and one count vector."
+++

## prompt [K-1]
Try each start and share until you must stop. Can choosing a different order leave different piles?

## prompt [2-3]
Finish each start in two different orders. After stopping, count each letter in the sharing word. Can a different order change the final piles or these counts?

## figure [K-1]
k1_order_square()

## figure [2-3]
order_square_23()

## key [K-1]
Four-cycle starts. All legal orders from a fixed start agree:
\begin{center}\begin{tabular}{llll}\toprule Start & Finish & Shares at each circle & One legal order\\\midrule
$(0,4,0)$ & $(1,0,1)$ & $(1,3,1)$ & BBACB\\
$(2,2,0)$ & $(1,1,1)$ & $(1,1,0)$ & AB\\
$(0,2,2)$ & $(1,1,1)$ & $(0,1,1)$ & BC\\
$(2,0,2)$ & $(1,0,1)$ & $(1,1,1)$ & ACB\\
\bottomrule\end{tabular}\end{center}

## key [2-3]
Four-cycle starts have these exact records:
\begin{center}\begin{tabular}{llll}\toprule Start & Finish & Shares at each circle & One legal order\\\midrule
$(0,4,0)$ & $(1,0,1)$ & $(1,3,1)$ & BBACB\\
$(2,1,2)$ & $(1,1,1)$ & $(1,1,1)$ & ABC\\
$(2,4,2)$ & $(1,0,1)$ & $(3,5,3)$ & ABBABCCBACB\\
\bottomrule\end{tabular}\end{center}
Other complete words are BBCAB, CBA, and CBBCBAABCAB, respectively. Every row duplicated on the student page should end with the same finish and count vector.

## hints [K-1]
B sends to A and C, not to the sink. On $(0,4,0)$, B may share twice before either neighbor shares. Ask where every chip went if the total appears to change.

## hints [2-3]
If records disagree, replay the two words slowly. Check for an illegal early firing or a missed chip along the B--C edge before discussing a counterexample.
