# Revision notes: Week 1 tiling packet

R1, R2 and R3 are Report 1 (adversarial review), Report 2 (simulated session) and Report 3 (mathematical check). Where reports overlap, the issue appears once below. Item numbers are the reports' own numbers.

## Fixed

1. **Upscale blocks break the "fewest" problems (R1-1).** Fixed. I added "Use only the small blocks." to the packet rule at the top of page 1 in all three packets.

2. **4–5 Problem 4 is impossible from covering E or F, and F is the covering left on the board (R1-2, R2-8, R3-1).** Fixed. The first sentence now reads "Start with covering A from Problem 3." I checked that covering A has 6 valid 4-flip round trips and that E and F have none. gen.py now asserts the check for A.

3. **2–3 Problem 7 asks third graders to prove the "always works" direction (R1-3).** Fixed. "explain why your rule is right" now reads "explain why the other places can never work".

4. **K–1 Problem 6 asks for recording by drawing on half-size copies (R1-4, R2-2, and the Problem 6 part of R3-2).** Fixed.
   - I replaced the big board and the eight half-size copies with six actual-size copies, one for each of the 6 coverings.
   - The text is now "Find all the ways to cover this shape with blue blocks. Put each way on a shape of its own.", which is the wording of Problem 3.
   - To fit six copies on one page, the board is turned 60° (hexagon 2,2,1 in place of 1,2,2). This avoids an unlabelled continuation page. It is the same shape, and gen.py checks that it still has 6 coverings. Each copy measures 3.5 in across at a 1-inch triangle edge.

5. **K–1 Problem 1 layout gives the answers away (R1-5).** Fixed. I swapped the two shapes in the middle row. Each column now mixes coverable and impossible shapes.

6. **4–5 Problem 2 makes children recopy their coverings, and the 2×4 grid of boards makes the graph lines cross (R1-6, R2-7).** Fixed, in part.
   - The recopying is gone. The text now reads "Give each of your coverings from Problem 1 a number. Below, write the numbers and draw a line between two numbers whenever one flip changes one covering into the other." The eight small boards are replaced by blank space.
   - I used numbers instead of letters so they do not clash with the coverings A–F in Problem 3.
   - I kept the request to draw the flip connections. The outline names the flip graph as the thing to explore, so this is a task to do, not a hint about method.

7. **4–5 Problem 4 has no place to record a flip sequence (R1-7).** Fixed.
   - I added a row of five small side-2 hexagons, for the start and the covering after each of the 4 flips. The two writing lines are kept for the 5-flip and 7-flip questions.
   - The added row pushed Problem 5's writing lines onto a page of their own, so Problem 5 now starts a new page. Problems 6–8 already have a page each. The 4–5 packet goes from 7 to 8 pages.

8. **K–1 Problem 5 is too long for one hearing, and the answer choices are printed words (R1-9, R2-1).** Fixed.
   - The text is now: "Take turns with a partner putting one blue block on a board. Whoever puts down the last block wins. On each board, circle 1 if the first player can always win, or 2 if the second player can."
   - The words "first" and "second" next to each board are replaced by a large 1 and 2.
   - The answers are unchanged: 1, 2, 1, 1, 2.

9. **K–1 Problem 3 prints more copies than there are ways, and "each shape" is unclear (R1-10, R2-3, R3-2).** Fixed. The page now prints exactly 2 hexagons in one row and 3 long hexagons below them, one copy per way: the hexagon has 2 ways and the long hexagon has 3. The two shapes now sit in separate groups, so it is clear which copies belong together. The text is unchanged.

10. **2–3 Problem 3: the side-5 triangle on page 4 is lost (R1-11, R2-4).** Fixed. "Cover each big triangle" now reads "Cover each big triangle on this page and the next". "The biggest triangle" now clearly means the one on page 4.

11. **K–1 rule "sit on the thin lines" (R1-12).** Fixed. It now reads "line up with the thin lines".

12. **"the fewest number of" (R1-13).** Fixed. It now reads "the smallest number of" in 2–3 Problem 4 and 4–5 Problem 3.

13. **2–3 Problem 4 takes about 30 seconds (R1-14, R2-5).** Fixed by using R1's option of asking why the side-10 board cannot do better.
    - I added "Explain why nobody can use fewer." after the side-10 question, and the writing lines go from 3 to 5.
    - This keeps the general statement of kernel 1 (a side-n triangle needs n greens) in the 2–3 packet, and makes the problem the generalization step after the concrete cases in Problem 3.
    - I did not delete the problem, as R2 suggested, because that would remove the only general-n question from the band.
    - Answers: 10 and 100. The side-10 triangle has 55 up and 45 down triangles.

14. **4–5 Problem 7: drawing 20 coverings on 0.3-inch triangles takes most of the time (R1-15).** Fixed. The text now reads "Draw them on the small hexagons below or list them".

15. **4–5 Problem 6 does not name a board (R1-16).** Fixed. It now reads "whenever you make flips on the hexagon board and end at…".

16. **4–5 Problem 6 assumes the child's Problem 3 answer is the true minimum (R3-3).** Fixed. The second sentence is now "Then find the smallest number of flips that changes covering E into covering F in Problem 3, and explain why nobody can do it with fewer." The true minimum is 8.

17. **4–5 Problem 3: the target pictures A–F have no grid lines, so they are hard to copy (R2-10).** Fixed. I added faint triangle grid lines inside the six covering pictures (`draw_tiling(..., grid=True)` in gen.py). I checked that the rhombus fills and edges are identical to the draft, so the coverings and the distances 3, 4 and 8 are unchanged.

## Skipped

18. **4–5 Problems 2 and 5 name "flip" and "ribbon" before the child has used them (R1-8).** Skipped.
    - The move has to be defined before a child can do it, and the name "flip" is needed in Problems 2–6.
    - The ribbon paragraph already gives only the rule and the worked picture, and the child uses the name right away.
    - Moving or rewriting these would reorganize the packet without fixing anything a child would get wrong.

19. **2–3 explanation load (R1-17).** Skipped. The reviewer says every explanation is a legitimate "why impossible / why best" question and that this is not a violation. Removing writing lines would take away recording space.

20. **2–3 Problem 6: the natural route of growing the side-4 triangle cannot reach 6 greens (R2-6).** Skipped.
    - The 20-triangle / 6-green task can be done: R1 and R3 confirmed it with the comb, and two side-3 triangles joined by one down-triangle and one up-triangle also work.
    - It is the most uneven 20-triangle board possible, so it is a real extremal construction.
    - Seeing that the first idea cannot work and finding a new shape is the mathematics. Hints belong with the adult.
    - Changing it to 19 and 5 would make it a much smaller problem.

21. **4–5 Problem 1 prints ten small boards for six coverings (R2-9).** Skipped. The problem asks the child to find all the coverings and explain how they know they have them all. Printing exactly 6 boards would give away the answer to that question. Spare copies are deliberate here, as in Problem 7, which prints 25 hexagons for 20 coverings.

## Build

- I edited the sources in `src/`: k-1.tex, grades-2-3.tex, grades-4-5.tex and gen.py.
- Figures: I added `figs/k1_b221.tex`, regenerated `figs/g45_pair_A–F.tex`, and removed `figs/k1_b122.tex` and `figs/k1_b122_small.tex`, which are no longer used.
- All checks in gen.py pass, including the two new ones.
- I compiled with pdflatex. There are no overfull or underfull boxes.
- Final page counts: K–1 6, grades 2–3 7, grades 4–5 8. I looked at every page.
