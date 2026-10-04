# Revision notes: Week 1 Tiling

I checked each issue against the base draft and, where the mathematics mattered, ran the author's solver (`src/tri.py`) on a scratch copy.

1. **K–1, Problem 5: the game question can't be read. FIXED.**
   I checked the random-play claims. The first player wins 1/3 of random games on the 4-strip, where 1st is correct, and 2/3 on the hexagon, where 2nd is correct. I replaced the printed words "first" and "second" beside each board with a large "1" and "2" (32 pt). The second sentence, "On each board, circle whether you should go first or second to be sure to win.", now reads "Who can always win on each board, the 1st player or the 2nd player? Circle 1 or 2." The review suggested "on this board". I kept "each board" because the parent reads the question once for all five boards. The game outcomes are unchanged.

2. **K–1, Problem 6: drawing at half size. FIXED.**
   I removed the big shape and the eight half-size copies and put in six actual-size copies of the same shape: four on page 6 and two on a new page 7. There are 6 coverings, which I checked again. The text is now "Find all the ways to cover each shape on this page and the next with blue blocks. Make every shape a different way." This follows the new Problem 3 wording (see 3). I added "on this page and the next" so the unlabeled second page isn't missed, which is the failure reported in issue 4. The K–1 packet is now 7 pages.

3. **K–1, Problem 3: more shapes than ways. FIXED.**
   There are now 2 hexagons and 3 long shapes, matching the 2 and 3 ways the solver finds. The review proposed adding "Make every shape a different way." as a third sentence. That would break the two-sentence limit for K–1 problems, so I used it to replace "Put each way on a shape of its own." With exactly as many shapes as ways, the new sentence also says that each way goes on its own shape. I widened the gap between the two hexagons from 0.45 in to 0.7 in to match the long shapes below them.

4. **Grades 2–3, Problem 3: the fourth triangle gets lost. FIXED, with a smaller change than proposed.**
   "Cover each big triangle with…" now reads "Cover each big triangle on this page and the next with…". Once the reader knows there are four triangles, "the biggest triangle" can only mean the side-5 triangle on the next page. So I left the explanation sentence alone and did not add the proposed extra sentence. Problem 4 (formerly 5) refers to "the four triangles in Problem 3", which is now consistent.

5. **Grades 2–3, Problem 4: a 30-second problem. FIXED.**
   I deleted Problem 4 (side 10 / side 100), and the problems after it moved up one number. No other problem refers to them by number; the chevron problem's reference to "Problem 3" still holds. I did not add the large cases to Problem 3, which the review left optional.

6. **Grades 2–3, Problem 6 (now 5): the natural first idea can't work. FIXED.**
   I confirmed the claim. All 2,511 one-piece boards made from the side-4 triangle plus 4 triangles need at most 4 greens. The text "exactly 20 small triangles that needs at least 6 green triangles" now reads "exactly 19 small triangles that needs at least 5 green triangles". I solved it again: 12 of the 517 boards made from the side-4 triangle plus 3 triangles need exactly 5 greens, for example the triangle with a trapezoid along one side (12 up-triangles, 7 down-triangles). In `gen.py`, the 20/6 check is replaced by this 19/5 example.

7. **Grades 4–5, Problem 2: copying the coverings again. FIXED.**
   The first two sentences after the flip picture now read "Give each of your coverings in Problem 1 a letter. Below, write the letters and draw a line between two letters whenever one flip changes one covering into the other." The question about the two coverings that need the most flips is unchanged. The eight small boards are replaced by blank space (4.3 in) for the graph, and the two answer lines stay.

8. **Grades 4–5, Problem 4: the natural starting covering can't work. FIXED.**
   I confirmed it: E and F each allow only one flip and are the only coverings on no 4-flip cycle. Covering A is on six. "Start with any covering of the hexagon board from Problem 3." now reads "Start with covering A from Problem 3." `gen.py` now checks for a 4-flip cycle through A specifically.

9. **Grades 4–5, Problem 1: more boards than coverings. SKIPPED.**
   Printing exactly 6 boards tells the child the answer to the problem's real question, "Explain how you know you have found them all." The search would stop at the sixth board, so there would be nothing left to convince anyone of. When the hunt for more coverings goes nowhere, that is what makes the completeness argument necessary, and a mathematician sits with this group to push for it. The organizer's own walking problem does the same: it prints sixteen blank grids for twenty routes, so he doesn't match the number of slots to the answer. Duplicate or wrong drawings can happen with any number of boards.

10. **Grades 4–5, Problem 3: the target pictures are hard to copy. FIXED.**
   The six covering pictures A–F now have faint grid lines (black!25, 0.35 pt, the same style as the small boards), drawn over the blue fill and under the rhombus outlines. I did this in `gen.py` by giving `draw_tiling` a `grid` option and using it only for the A–F pictures. The coverings themselves are unchanged, and the flip distances 3, 4 and 8 still check.

## Build
I rebuilt all figures with `src/gen.py`; every check passes. Apart from the A–F pictures, the figures differ from the old ones only in drawing order. I compiled with pdflatex and copied the PDFs to `final/`: k-1.pdf (7 pages), grades-2-3.pdf (7 pages), grades-4-5.pdf (7 pages). I rendered every page and checked it.
