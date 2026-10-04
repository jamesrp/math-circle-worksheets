# Revision notes: Week 7 take-away games

All edits are in `src/make.py`. I regenerated the three `.tex` files from it, compiled them with pdflatex, and copied the PDFs to `final/`. Page counts are the same as before: K-1 has 5 pages, grades 2-3 has 5, and grades 4-5 has 6. I re-solved every changed problem by brute force (`scratch/rev/check.py`). The intended answers are unchanged, and every diagram still matches its text.

## 1. Two-pile games: "the last counter" could mean emptying one pile (all three bands): FIXED

I confirmed the problem. With two piles, "whoever takes the last counter wins" can be heard as "whoever empties a pile wins", and that reading changes the answers. In each two-pile problem I now name the counter that wins:
- **K-1 P8:** added the sentence "Whoever takes the last counter on the table wins." after the move sentence. The rest of the text is unchanged.
- **Grades 2-3 P7:** added the same sentence after "On each turn, a player takes 1 or 2 counters from one of the piles."
- **Grades 4-5 P8:** changed "whoever takes the last counter wins" to "whoever takes the last counter on the table wins".
- K-1 P9 and 4-5 P9 refer back to P8, so they need no change.

Checked under the intended reading:
- K-1 P8: (1,1) 2nd, (1,2) 1st, (2,2) 2nd, (2,3) 1st, (3,3) 2nd, (1,4) 2nd.
- K-1 P9: (6,6) 2nd.
- 2-3 P7: (3,3) Second, (4,2) First, (4,1) Second, (5,3) First.
- 4-5 P8: the "second" squares are exactly those with a ≡ b (mod 3).
- 4-5 P9: the unequal pairs are {1,3}, {1,8}, {2,7}, {3,8}, {4,6}.

## 2. K-1 P10: the move rule was not restated after P7 changed it: FIXED

I confirmed the problem. P7 changed the moves to "1, 2, or 3", and P10 is the next one-pile problem. The traps differ by rule: 1, 4, 7, 10, 13, 16, 19 for {1, 2}, and 1, 5, 9, 13, 17 for {1, 2, 3}. I added one sentence, "Each player may take 1 or 2 counters on a turn.", worded like P7's own rule sentence. The original two sentences are unchanged. The intended traps are still 1, 4, 7, 10, 13, 16, 19.

## 3. K-1 P6: the number of blank rows suggested the wrong number of ways: FIXED

I confirmed the problem. A game with 4 counters can go 5 ways and a game with 5 counters can go 8 ways, but the page had 8 rows and 10 rows. A K-1 child takes the rows as the number of answers. The extra rows would send the child after ways that do not exist, or lead them to fill the spare rows with repeats. I changed `range(8)` to `range(5)` and `range(10)` to `range(8)`, so the page now shows 5 rows of 4 counters and 8 rows of 5 counters. I did not use the alternative of one spare row per column, because a K-1 child would still read 6 and 9 rows as 6 and 9 ways. The rest of page 3 is unchanged. P7 moves up a little and still fits on the page.

## 4. Grades 4-5 P8: the row 0 / column 0 square is not a playable position: FIXED

I confirmed the problem. Square (0,0) is two empty piles, so no counter is ever taken. The page's rule does not decide that square, and "first or second" has no answer there. I crossed the square out with a thin grey X in the `grid()` helper, which draws both the P8 and P9 grids. P9 says "the grid works the same way as in Problem 8", so the two grids stay alike.

I chose a cross instead of greying the square, because the task asks children to shade squares: a grey corner would look like a square already shaded as a "second" answer. I did not use the text alternative "Shade every other square". It adds words, and "every other" can be heard as "every second square". No text changed for this issue.
