# Review of the Week 1 draft (base/)

I checked every problem by hand and with a brute-force solver run on the source geometry (`scratch/chk/`). Everything below is mathematically correct:

- K–1 P1 yes/no pattern is yes, no, yes, no, yes, no. The 8-triangle trapezoid has 5 up and 3 down triangles.
- Fewest greens on triangles of side 2–5 are 2, 3, 4, 5 with blues, and 4, 5, 4, 5 with chevrons.
- K–1 P4 minima are 3, 3, 4.
- K–1 P5 strip games are wins for first, second, first, first, and the hexagon is a win for second.
- Covering counts: 2 and 3 (K–1 P3), 6 (the 1-2-2 board), 20 and 20 (4–5 P7, P8).
- 2–3 P7 rule: every up/down pair of greens works and no same-direction pair works.
- 4–5 P3 shortest flip routes are 3, 4, 8. The flip graph of the 1-2-2 board has diameter 4, reached by one pair only.
- The ribbon example really does read LRRLR.

All boards are actual size. Headers, footers and "Problem N:" labels are correct on every page, and there are no titles, encouragement or exclamation marks. The issues are below.

---

## K–1

**1. MUST. K–1, page 6, Problem 6.** Text: "Find all the ways to cover the big shape with blue blocks. Draw each way on a small shape." The eight recording copies are half size (small-triangle edge 0.5 in) with all grid lines printed.
- *What goes wrong:* Each covering has 8 rhombi. To record one, a kindergartner must copy a block layout from the actual-size board onto a half-size picture and darken exactly the right segments, while the grid line through the middle of each rhombus stays visible. Most K–1 children cannot do this. Without a record they cannot keep track of which ways they have already found, and keeping track is the whole task ("find all").
- *Smallest fix:* Drop the big shape and the half-size copies. Print eight actual-size copies of this board, four per page on this page and one more. Change the second sentence to "Put each way on a shape of its own." This is the same wording as Problem 3, so the children leave the blocks in place as their record.

---

## Grades 2–3

**2. SHOULD. Grades 2–3, pages 3–4, Problem 3.** Text: "Cover each big triangle with blue rhombuses and green triangles. … Then explain why nobody can cover the biggest triangle with fewer green triangles than you used." Page 3 shows the side-2, side-3 and side-4 triangles. The side-5 triangle and the writing lines are on page 4, which has no text at all.
- *What goes wrong:* On page 3 the biggest triangle in sight has side 4, so children explain the wrong triangle. A child who picks up page 4 by itself finds an unlabeled triangle with no task.
- *Smallest fix:* Change the first sentence to "Cover each of the four big triangles on this page and the next page with blue rhombuses and green triangles."

**3. SHOULD. Grades 2–3, page 5, Problem 4.** Text: "Imagine a triangle board with 10 small triangles along each side. … what is the fewest number of green triangles you need? What if the board has 100 small triangles along each side?"
- *What goes wrong:* The boxes in Problem 3 already read 2, 3, 4, 5. A quick third grader writes "10 and 100" in under a minute by continuing the pattern, without using the up/down idea or knowing that 10 can actually be reached. That is far short of the five minutes of thinking a numbered problem should give.
- *Smallest fix:* Add one sentence at the end: "Explain how you know." The explanation is the point here: why the count is best, and why that many greens is enough.

---

## Grades 4–5

**4. SHOULD. Grades 4–5, page 4, Problem 5.** Text: "Write the ribbon of each covering of the board from Problem 1. On the hexagon board each covering has two ribbons, because its top side has two short edges."
- *What goes wrong:* The board from Problem 1, named in the sentence just before, is also a six-sided hexagon, and its top side has only one short edge. Children look at that board and are confused about where the second ribbon is. The packet means the Problem 3 board here but does not say so.
- *Smallest fix:* "On the hexagon board from Problem 3, each covering has two ribbons, because its top side has two short edges."

**5. SHOULD. Grades 4–5, page 5, Problem 6.** Text: "Then explain why nobody can change covering E into covering F in Problem 3 with fewer flips than your answer."
- *What goes wrong:* The shortest route is 8 flips. A child whose box in Problem 3 says 10 or 12 is asked to explain something false, and will either get stuck or produce a wrong argument.
- *Smallest fix:* "Then find the fewest flips that change covering E into covering F in Problem 3, and explain why nobody can do it with fewer."

**6. SHOULD. Grades 4–5, pages 6–7, Problems 7 and 8 (order).**
- *Current order:* Problem 7 counts the coverings of the side-2 hexagon. Each covering has two ribbons that must not cross, and the page asks the child to draw all 20 coverings. Problem 8 counts the coverings of the 1-3-3 board, where each covering has one ribbon with three L's and three R's.
- *What goes wrong:* Problem 8 is the direct next step after Problems 1 and 5 (one ribbon with two L's and two R's gives 6 coverings). Problem 7 is the harder two-ribbon case, and drawing 20 coverings takes a long time. A child who stops partway through Problem 7 never reaches the clean ribbon count. This is backwards from "meet the idea in a simpler case, then use it".
- *Smallest fix:* Swap the two problems and renumber them: the 1-3-3 board becomes Problem 7 and the side-2 hexagon becomes Problem 8. Neither problem's text needs changing, because "the hexagon board from Problem 3" still refers to the right board.
