+++
id = "w13.add-arrow"
title = "Add one arrow so that three routes fit"
grades = ["2-3"]
route = "return"
kernel = "A new inside arrow helps only if it jumps past both two-arrow bottlenecks; on the board with two Start arrows no inside arrow can help."
+++

## prompt
On each board, add one new arrow between two inside dots so that three routes fit. The new arrow cannot touch Start or Finish. Crossings without a dot are not meeting points. If it is impossible, explain why.

## figure
add_arrow()

## key
Upper board: add D to G. Three routes are s-A-D-E-G-H-t, s-B-D-G-I-t, and s-C-D-F-G-J-t. They meet at D and G but share no arrows. Lower board: impossible. Start has only two outgoing arrows, and the allowed new arrow cannot touch Start. Every collection is therefore bounded by 2.

## hints
Hint: before searching, ask whether there is a bottleneck the allowed move cannot change.
