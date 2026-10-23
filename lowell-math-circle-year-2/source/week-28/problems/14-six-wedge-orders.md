+++
id = "w28.six-wedge-orders"
title = "Orders of six wedges with alternating half-turns"
grades = ["2-3", "4-5"]
route = "return"
kernel = "With wedges 30, 30, 60, 60, 90 and 90 degrees, each alternating triple must be one of each size, which gives 36 rooted orders and 12 starting with 30 degrees."
+++

## prompt [2-3]
Use these six wedges once each to fill a disk. Find four different orders of A, B, and C in which the alternating wedges make two half-turns. Read clockwise from the top ray.

## prompt [4-5]
Use the angles $30^\circ,30^\circ,60^\circ,60^\circ,90^\circ,90^\circ$ once each, clockwise around one center. How many different orders start with $30^\circ$ and have alternating totals of $180^\circ$? Explain why your count is complete. Swapping equal angles does not make a new order.

## figure [2-3]
six_wedges_23()

## figure [4-5]
angle_orders_45()

## key [2-3]
Here A=30$^\circ$, B=60$^\circ$, C=90$^\circ$, and each letter appears twice. Four sample answers are \textbf{AABBCC, AABCCB, AACBBC, AACCBB}. Each word is read clockwise from the top ray; swapping the two physical copies of a letter makes no new order. There are 36 rooted letter orders in all, although only four are requested.

## key [4-5]
\textbf{Answer:} exactly twelve clockwise orders start with 30$^\circ$ and give two alternating sums of 180$^\circ$. The first sector lies immediately clockwise after the marked top ray. Equal copies are indistinguishable; reflections and rotations are not identified after this starting convention is fixed.

The first 30$^\circ$ fills one odd slot. The other odd slots 3 and 5 hold 60$^\circ$,90$^\circ$ in two possible orders. The even slots 2,4,6 hold 30$^\circ$,60$^\circ$,90$^\circ$ in 3$\times$2$\times$1=6 orders. The choices are independent, giving 2$\times$6=12.
