+++
id = "w13.bottleneck"
title = "The interior bottleneck"
grades = ["2-3", "4-5"]
route = "first"
kernel = "Three arrows leave Start and three enter Finish, but every route must use one of the two arrows leaving D, so two routes and two closures certify each other."
+++

## prompt [2-3]
Find the largest collection of routes on this board. Close as few arrows as possible to stop every route. Explain how you know your collection cannot be larger.

## prompt [4-5]
Find a largest route collection and a smallest set of closing arrows. Explain why your closing arrows stop every route, and how you know your collection cannot be larger.

## figure [2-3]
bottleneck_23()

## figure [4-5]
bottleneck_45()

## key [2-3]
Maximum and minimum are both 2. Use s-A-D-E-G-H-t and s-C-D-F-G-J-t; close DE and DF (or EG and FG). Start has three outgoing arrows and Finish three incoming arrows, but every route must pass through one of the two arrows leaving D. Hence no collection of three fits. The board has 18 individual routes and 36 unordered maximum collections, but listing them is unnecessary. See the reference diagram on page 7.

## key [4-5]
Use the interior bottleneck solution on page 7: two routes and two closures, DE and DF. Every s-to-t route must leave the start-side set \{s,A,B,C,D\}, and these are its only outgoing arrows. The certificate argument on page 4 supplies both required inequalities.

## hints [2-3]
Hint: look in the middle, not only at the ends.

## hints [4-5]
Hint: explain why all routes cross the proposed barrier before claiming the count is optimal.
