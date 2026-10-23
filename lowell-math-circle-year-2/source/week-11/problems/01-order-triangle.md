+++
id = "w11.order-triangle"
title = "Two orders from each start on the triangle"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"
kernel = "On the triangle with a sink, every legal order from a start gives the same final piles and the same number of shares at each circle."
+++

## prompt @48 [K-1]
Try each starting pair and share until you must stop. Can choosing a different order leave different piles?

## prompt @56 [2-3]
Finish each start in two different orders, if possible. After stopping, count each letter in the sharing word. Can a different order change the final piles or these counts?

## prompt @46 [4-5]
Finish each start in two different orders, if possible. After stopping, count each letter in the sharing word. For the same start, can the final piles agree while the sharing counts differ?

## figure [K-1]
k1_order_triangle()

## figure [2-3]
order_triangle_23()

## figure [4-5]
order_triangle_45()

## key [K-1]
Triangle starts. Changing legal move order cannot change the finish. The answer rows are:
\begin{center}\begin{tabular}{llll}\toprule Start & Finish & Shares at each circle & One legal order\\\midrule
$(2,2)$ & $(1,1)$ & $(1,1)$ & AB\\
$(3,2)$ & $(1,0)$ & $(2,2)$ & ABAB\\
$(2,3)$ & $(0,1)$ & $(2,2)$ & ABBA\\
$(3,3)$ & $(1,1)$ & $(2,2)$ & ABAB\\
\bottomrule\end{tabular}\end{center}
The share-count column is adult support; children are only asked about final piles. These trials deliberately give three different finishes across different starts. Each start is printed on two rows, one for each order, so that children compare two runs of the same start rather than different starts.

## key [2-3]
Triangle finishes and sharing counts are both independent of legal order, for the same start.
\begin{center}\begin{tabular}{llll}\toprule Start & Finish & Shares at each circle & One legal order\\\midrule
$(2,2)$ & $(1,1)$ & $(1,1)$ & AB\\
$(4,0)$ & $(1,0)$ & $(2,1)$ & AAB\\
$(3,3)$ & $(1,1)$ & $(2,2)$ & ABAB\\
\bottomrule\end{tabular}\end{center}
Two examples of orders are AB and BA for $(2,2)$, and ABAB and BABA for $(3,3)$. The start $(4,0)$ has only one complete legal word, AAB; the printed ``if possible'' matters. A cannot skip a legal forced move by inventing a second order.

## key [4-5]
For one fixed start, final piles cannot agree while share counts differ. Here are all four records:
\begin{center}\begin{tabular}{llll}\toprule Start & Finish & Shares at each circle & Chips in sink\\\midrule
$(2,2)$ & $(1,1)$ & $(1,1)$ & 2\\
$(4,0)$ & $(1,0)$ & $(2,1)$ & 3\\
$(3,3)$ & $(1,1)$ & $(2,2)$ & 4\\
$(5,4)$ & $(1,0)$ & $(4,4)$ & 8\\
\bottomrule\end{tabular}\end{center}
Use AB/BA; AAB only; ABAB/BABA; and AABABBAB/BBAABAAB, respectively. Across \emph{different} starts, equal finishes with different share counts do occur: $(2,2)$ and $(3,3)$ are examples. Preserve the printed fixed-start qualification.

## hints [K-1]
If a child moves just one chip, touch both lines from the firing circle and send a chip along each. For an order comparison, restore the identical start first.

## hints [2-3]
Keep the table routine from page 4: one child moves chips and the other checks each line and records the firing word; then exchange roles. After stopping, count its letters to recover the sharing counts. A count at A means the number of times A shared, not chips remaining at A.
