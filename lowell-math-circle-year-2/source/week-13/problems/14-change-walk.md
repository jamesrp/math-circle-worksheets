+++
id = "w13.change-walk"
title = "A change-walk that adds a route"
grades = ["4-5"]
route = "return"
kernel = "A change-walk may follow unused arrows forward and reserved arrows backward; toggling its arrows turns two stuck routes into three."
+++

## text
A change-walk follows an unused arrow forward or a reserved arrow backward. A forward step reserves its arrow; a backward step cancels its reservation. A change-walk visits each dot at most once. Final routes follow the printed arrows.

## figure
cancellation_example()

## prompt
Find a change-walk from Start to Finish that increases the number of routes by one, on this board and on both boards of Problem 1. Draw each resulting route collection.

## figure
staircase_boards()

## key
The reserved routes are s-B-D-t and s-C-E-t. Use the change-walk s-A-D-B-E-C-F-t. The steps D to B and E to C cancel the original BD and CE. Other steps reserve sA, AD, BE, CF, Ft. The resulting three forward routes are s-A-D-t, s-B-E-t and s-C-F-t. All arrows are present in the printed board. The three arrows leaving Start bound every collection by 3, so this improvement is optimal. The problem also asks for the two Problem 1 boards: their change-walks are s-B-A-t and s-B-A-C-E-D-t (page 7).

The change-walk is forced here: only sA is initially available from Start; after AD, the used Dt is unavailable forward, so go backward along BD; continue analogously through E. This is a different interaction from the revised bowtie case.

## hints
Hint: redraw only the currently available forward steps and allowed cancellation steps, keeping their meanings distinct.
