+++
id = "w22.placing-game"
title = "The placing game: can four dots always be split?"
grades = ["K-1", "2-3", "4-5"]
route = { "K-1" = "return", "2-3" = "return", "4-5" = "first" }
page = "new"
kernel = "No arrangement of four dots defeats the splitter (Radon's theorem in the plane): one dot in the triangle of the others, two crossing segments, or a degenerate case always gives a meeting split."
+++

## prompt [K-1]
Take turns placing A, B, C, and D in the box. Can the other player always make two regions that meet?

## prompt [2-3]
Take turns placing A, B, C, and D in the box. Try to make an arrangement that the other player cannot split successfully. Can four dots always be split so their regions meet?

## prompt [4-5]
Take turns placing A, B, C, and D in the box. Try to make an arrangement with no successful split. Decide whether your opponent must always be able to find one.

## figure
board()

## text [2-3, 4-5]
\recordlines{2}
