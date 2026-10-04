# Revision notes: Week 1 Tiling packet

Final PDFs: final/k-1.pdf (6 pages), final/grades-2-3.pdf (9 pages), final/grades-4-5.pdf (9 pages).
Where the three reports describe the same problem, it is listed once with its sources (R1 = adversarial review, R2 = classroom simulation, R3 = mathematical check).

## Fixed

1. **Grades 4–5: explanations asked for before the chain tool exists (R1 major 1, R2 #8, also R1 minor 6).**
   - I deleted "For the first pair, explain why it cannot be done in fewer moves" from Problem 3.
   - In Problem 4, "For each number, draw the coverings you pass through, or explain why it cannot be done" now reads "For each number that works, draw the coverings you pass through."
   - I added a new Problem 8 on its own page after Problem 7 (chains), with the page as writing space: "Could the first pair in Problem 3 be done in fewer moves than you used? Could a round trip in Problem 4 take exactly 5 moves, or exactly 7 moves? Explain."
   - I worded it as a question so that it does not give away the answers 8 and "no" to a child reading ahead. This is the same reasoning as item 4.
   - Old Problems 8 and 9 are now Problems 9 and 10. Checked again: pair 1 takes 8 moves (each chain LLRR to RRLL needs 4 swaps), and round trips exist for 4 and 6 moves but not for 5 or 7.

2. **K–1: the packet rule did not say "along the lines", which changes the Problem 6 game (R1 major 2, R2 #3, R3 #1).**
   - The rule now reads "In every problem, blocks go on the lines of the shape. They must stay inside it and must not overlap."
   - On the grid, the outcomes are: hexagon, second player wins; both strips, first player wins.

3. **Hints that do the noticing (R1 moderate 3).**
   - Grades 2–3, Problem 5: I removed "Each side of triangle C is 4 inches long." The sizes now read "with 10 small triangle edges along each side" and "with 100 small triangle edges along each side". The answers are still 10 and 100.
   - Grades 4–5, old Problem 8 (now 9): I deleted "This board has only one small edge on its bottom side." and changed "it" to "this board".

4. **Grades 2–3, Problem 4 gave away the answer to Problem 2C (R1 moderate 4).** It now reads "Could triangle C in Problem 2 be covered with blue blocks and fewer green triangles than you used? Explain."

5. **Grades 4–5: not enough recording space (R1 moderate 5, R2 #9, R3 #4).**
   - Problem 4: I added a third row of four copies, so there are 12. The 4-move and 6-move round trips need 10 drawings.
   - Old Problem 8 (now 9), the 1-3-3 board: I added a row of four 0.4-scale copies below the actual-size board, plus the packet's existing sentence "If you run out of copies, you can draw more on the back." With 20 coverings, the four copies do not suggest a count.

6. **K–1 sentences too long for one hearing, and Problem 6 never said to circle (R1 moderate 6, R2 #2).**
   - Problem 6 now reads: "Take turns with a partner putting one green block or one blue block on the shape. The player who puts down the last block wins. For each shape, circle the player who can always win: first or second."
   - This also stops children from answering a "would you rather" question before they have played.
   - Problem 5's first sentence is split in two: "Build the left picture with blue blocks. Change it into the right picture in as few moves as you can."

7. **Grades 2–3: page breaks mixed the board labels of Problems 1 and 2 (R1 moderate 7).**
   - Problem 2 now starts on a fresh page. Page 2 holds only boards E and F of Problem 1, the same way Problem 3 continues onto a second page.
   - I tried moving E and F onto page 1, but all six boards do not fit at actual size with reasonable spacing.
   - The packet is now 9 pages.

8. **K–1, Problem 4: extra copies (3 hexagons for 2 ways, 4 long shapes for 3 ways) sent children hunting for ways that do not exist (R2 #1, R3 #3).**
   - I added "Some copies may stay empty." This is R3's preferred fix.
   - I kept the copy counts, so that deciding when every way has been found stays with the child. Printing exactly 2 and 3 copies would give the count away.

9. **Grades 4–5, Problem 1: eight lettered copies for 6 coverings (R2 #7, R3 #2, copy-count part).**
   - I added "Some copies may stay empty." I chose this for the same reason as item 8: six copies would print the answer next to "Explain how you know that you have found them all."

10. **K–1, Problem 5: the targets were printed at 62% size, and children tried to build on them (R2 #4).**
    - Both targets are now printed at actual size (1-inch edges), beside their actual-size starting boards. The tiling figures are unchanged.
    - So that both puzzles still fit on one page, the arrow sits in the gap between the slanted boards and "moves:" sits under it. The blank is shortened so it does not touch the boards. The page count is unchanged.
    - The fewest moves are still 2 and 4.

11. **K–1, Problem 3: "how many green blocks this big triangle needs" was heard as "how many greens fill it" (R2 #5).** It now reads "Guess the fewest green blocks you will need for this big triangle."

12. **Grades 2–3, Problem 7 was misread as "a board I can cover with 4 greens" (R2 #6).** It now reads "...so that it cannot be covered with blue blocks and fewer than 4 green triangles." The task is still possible, for example with a 12-triangle shape of 8 up and 4 down triangles.

13. **Grades 2–3, Problem 6 wording (R1 minor 1).** I dropped "Now", and changed "Is there a board where" to "Is there a triangle where".

14. **Grades 4–5 packet rule (R1 minor 2).** It now reads "The blank small drawings of boards are for recording." The filled-in pictures in Problems 3 and 5 are not for recording.

15. **Faint grids on small copies (R1 minor 7).** On the blank small copies (h221_s50, h222_s40, h222_s45 and the new h133_s40), the grid lines went from 0.35 pt at 22% gray to 0.45 pt at 30% gray. Nothing else changed in gen_figs.py.

## Skipped

- **Grades 4–5, Problem 5 introduces the word "chain", the notation and an example together (R1 moderate 8).** The reviewer calls this a judgment call. The notation is needed for Problems 5–10, and children use it on four concrete coverings in Problem 5 before Problems 6–8 ask them to generalize. The proposed fix would add a new tracing step and reorganize the section.
- **Grades 4–5, Problem 1: "different" is not defined (R3 #2, second part).** The task is to cover this board, so placements on the fixed board are the natural reading. The adult can settle the question at the table, and the simulation did not run into it.
- **Grades 4–5, Problem 9 (now 10): 16 copies for 20 coverings (R1 moderate 5, third part).** The problem already says "If you run out of copies, you can draw more on the back." This matches the organizer's own walking problem (16 copies for 20 ways). Printing 20 copies would give the count away, and 24 would send children hunting for coverings that do not exist, as in items 8 and 9.
- **K–1, Problems 2 and 4 are a little long (R1 moderate 6).** The reviewer calls them tolerable, and the simulation showed no trouble with them.
- **K–1, Problem 6 is outside the two kernels (R1 minor 3).** No change was requested. The brief names "work out how to win a game" as K–1 mathematics.
- **Grades 2–3: no balanced board that still cannot be covered (R1 minor 4).** The reviewer marks it optional. It would add a new board, and the band already holds more work than the hour.
- **Grades 2–3, Problem 3: no marked space for explanations (R1 minor 5).** The simulation found the blank space beside each board was enough, and marking it would mean adding labels.
- **Footer 0.35 inch from the bottom edge (R1 minor 8).** The reviewer says it is fine on most printers.
