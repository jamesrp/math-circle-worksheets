# Revision notes: Week 7 / Take-away games

All edits are in `src/make.py`. It regenerates the three `.tex` files, which are compiled with pdflatex into `final/`. Page counts: K-1 is 5 pages, grades 2-3 is 5 pages, grades 4-5 is 6 pages (all unchanged from the draft).

## Issues

1. **Grades 2-3: too little work for the quick child.** Fixed. I added Problem 9 on page 5 under Problem 8, using the reviewer's wording with a 20-box `chart(20)`: "Now whoever takes the last counter loses. On each turn, a player takes 1, 3, or 4 counters. Shade the box of every starting pile from 1 to 20 where you would rather go second." Solved: the losing piles are 1, 3, 8, 10, 15, 17 (remainder 1 or 3 when divided by 7). The opening paragraph used to state the normal-play rule for "every game in this packet", which this problem now contradicts. I changed its last sentence to "Unless a problem says otherwise, whoever takes the last counter wins." This is the same wording the grades 4-5 packet already uses.

2. **K-1 Problems 2 and 8: "would rather go first or second".** Fixed. Problem 2 now reads "Circle 1st or 2nd to show which player can be sure to win with each pile." Problem 8 now reads "Circle 1st or 2nd to show which player can be sure to win." I left out "with each pile" in Problem 8 because each case there has two piles.

3. **Two-pile layout: 1st/2nd under each pile (K-1 Problem 8, grades 2-3 Problem 7).** Fixed. In `two_pile_panel`, the two choice words used to sit at 0.25 and 0.75 of the case width. They are now a close pair centered under the middle of the case, with gaps of 0.9 cm (K-1) and 0.7 cm (grades 2-3), and their baselines line up. The trays and frames did not change.

4. **K-1 Problem 6: padded rows, cramped counters, "different way" undefined.** Fixed, using the reviewer's alternative.
   - The rows stay at 8 and 10, so the page does not give away the counts of 5 and 8.
   - I added "Some rows may stay empty." This matches the organizer's own practice in the walking problem, where the number of blank grids does not match the answer. Printing exactly 5 and 8 rows would hand the child the count and turn "every way" into "fill the rows".
   - I added "Taking 1 then 2 is different from taking 2 then 1."
   - Counter spacing went from 1.15 cm to 1.5 cm sideways and from 1.3 cm to 1.8 cm between rows.
   - Problem 6 now fills page 3, and Problem 7 moves to page 4.

5. **K-1 Problem 10: allowed moves unclear.** Fixed. It now reads "Now there is one pile again. Each player takes 1 or 2 counters on a turn, and whoever takes the last counter loses." I added "on a turn" to match Problem 7's phrasing. Traps: 1, 4, 7, 10, 13, 16, 19.

6. **K-1 Problem 5: "always" and "circle".** Fixed. It now reads "Ben goes first and takes 2 counters. Put a check by each pile where Ben can still be sure to win." Answer: 5, 8, 11. The diagram did not change.

7. **K-1 Problems 1 and 3: "circle the counters you take".** Fixed. I added "now" in both: "Circle the counters you take now to be sure to win, ..."

8. **Grades 2-3 Problem 7: only equal pair is (3,3).** Fixed. (3,3) is now (4,4), drawn as two piles of 4. Solved: (4,4) and (4,1) are second-player wins, and (4,2) and (5,3) are first-player wins. A single pile of 4 is not a trap, so "both piles are traps" no longer explains the equal case.

9. **Grades 4-5 Problem 6: read as the single game {1, ..., 6}.** Fixed with the reviewer's wording: "Choose some of the numbers 1, 2, 3, 4, 5, 6 to be the allowed moves. Find every choice whose losing piles are exactly the multiples of 4. Explain why your list is complete." Solved: {1,2,3}, {1,2,3,5}, {1,2,3,6} and {1,2,3,5,6}.

10. **K-1 Problem 4: abstract definition of trap.** Fixed. It now reads "A pile is a trap if you cannot be sure to win when it is your turn, like the pile of 3." The example points back to the pile the children have just handled in Problem 1.

11. **Grades 2-3 Problem 2: claims already settled by the Problem 1 table.** Fixed. Lee now has 21 counters. Mo now has 20 counters and takes 1. Lee is still right (21 is a multiple of 3). Mo is still wrong: he leaves 19, the partner takes 1 to leave 18, and the correct first move is to take 2.

12. **Grades 2-3 and 4-5: what happens when no move is possible.** Fixed. I added "If you cannot take any counters, you lose." to the end of the opening rule paragraph in both packets. The 4-5 Problem 6 answer above was checked with this rule.

13. **Grades 4-5 Problem 4: "as many counters as the rule allows".** Fixed. It now reads "Dana's plan is to always take the biggest number of counters she is allowed to take from the pile." Solved: the plan fails at 4 for {1,2}, at 5 for {1,3,4} and at 8 for {1,4}, and always wins for {1,3,5}. The new wording is one line longer and pushed Problem 5 onto a new page (6 pages became 7). To keep the original page breaks, I cut the writing space after Problem 4's table from 5.0 cm to 4.5 cm.

14. **K-1 Problem 4 overlaps Problems 1-3.** Skipped. Starting the track at 13 would make the page worse for K-1:
    - Problem 4 is where the children gather the separate piles into a single 1-20 picture. Seeing the X's on 3, 6, 9, ... laid out together is how the "every third" pattern becomes visible.
    - Problems 7 and 10 use the same 1-20 track, so a child can compare the three rules box by box. A 13-20 track breaks that.
    - The cost was about 2 minutes for the quick child, who did not run out of work.
