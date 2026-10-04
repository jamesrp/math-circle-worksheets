# Week 9 return visits: adversarial student-page review

**Verdict: PASS. No essential mathematical or layout correction found. Prepared, unpiloted.**

Reviewed the actual seven-page `draft/return-visit.pdf`, rendered every page with PyMuPDF, and inspected all seven images. Read `PROMPT.md`, the TeX source and checks, then the writer's notes. This review is for the shared companion specified in the outline: three investigations with additional workspace, suitable page bands, no forced K–1 equivalent, and no expectation of finishing in an hour. The generic three-band harness text does not govern that scope.

## Page coverage

| Actual PDF page | Review result |
|---|---|
| 1, Grades 2–5 | Problem 1 gives the concrete start and two distinct finishes, asks for every ordered two-bounce wall word, permits repeated names as candidates, and requires a ruler-drawn path. Shared rules enforce straight segments, equal angles and stopping at corners. S and F are visibly distinct from the L/R/B/T wall labels. The non-task one-bounce visual supplies incoming ray → equal-angle turn → completed path and word R before word use. The four boards are legible and have 12.5 mm square cells. |
| 2, Grades 2–5 | Extra workspace remains part of Problem 1. Six further boards and the two finish-word lines provide a light, recoverable catalog. Board copies match page 1. No duplicate problem number or additional investigation is introduced. |
| 3, Grades 2–5 | Six further matching boards bring the supply to eight per finish. That accommodates all eight successful A paths and all six successful B paths separately, with two spare B boards. Attempts can be erased or use other paper; the page need not supply one permanent board for every rejected word. |
| 4, Grades 4–5 | Problem 2 supplies all 15 interior dots on a 6-by-4 board, the NE initial state, C/L recording convention, and a stopping condition involving both position and direction. The three-frame non-task example correctly shows NE at the start, NW after a right-wall contact, and SW after the next top-wall contact. Direction is externalized in the counter arrow. The 22 mm cells are large enough for a small counter. Classification and first-return length are substantial questions rather than a sequence of tiny instructions. |
| 5, Grades 4–5 | Two 18 mm-cell boards provide real drawing room and simple start/step-count records for Problem 2. These are clearly extra workspace. |
| 6, Grades 2–5 | Problem 3 defines crossings as distinct interior X locations and excludes wall contacts and corners. First pass → later pass → circled location is a clear worked recording convention. The four contrasting boards support tracing, counting and a scaling comparison; the exact-ten task remains open. All four boards have square 12.5 mm cells, adequate space around their labels, and a visible NE launch at S. |
| 7, Grades 2–5 | A 12-by-12 workspace at 12.5 mm per square fits both a 5-by-6 ten-crossing rectangle and its 10-by-12 scaled version. The instruction to outline the rectangle and the dimension/count blanks make the next action clear. |

All seven pages have the required header/footer and consecutive page numbers. Text, labels and diagrams do not overlap or spill beyond the page. The rectangular boards use equal horizontal and vertical scales. Extra-workspace wording is compatible with the organizer's specific allowance for additional blank boards; it is not a second page title above a new numbered problem. There are no Name/Date fields, encouragement, printed hints or answer formulas.

## Mathematical checks

I ran the supplied exact checks successfully and also enumerated reflected rectangle tiles independently, counting the ordered crossings of their boundary lines. This independently gives:

- Finish A, S=(1,1), F=(2,3): BL, BR, BT, LR, LT, RL, RT, TB.
- Finish B, S=(1,1), F=(3,3): BR, BT, LR, LT, RL, TB.

Repeated-wall words are impossible. Simultaneous boundary crossings are corners and are rejected; the B cases LB/BL and RT/TR therefore supply meaningful obstructions. The enumeration is about realizable wall words and actual crossing order, not shortest paths. It is distinct from the existing Week 21 optimization of two contacts on parallel walls, while sharing repeated reflection as an ancestor. Nothing in the student PDF claims that reflection itself is new.

For Problem 2, unfolded motion reaches a corner when a step number satisfies n=-x modulo 6 and n=-y modulo 4. These simultaneous conditions are compatible exactly when x-y is even. Thus A, C, E, G, I, K, M and O reach a corner; B, D, F, H, J, L and N loop. A full return with the original NE direction requires a displacement divisible by both 12 and 8, so its first positive time is 24 steps. In particular H returns to its dot at step 12 with SE direction; the printed full-state condition correctly prevents premature stopping.

Independent reduced-grid parity counts confirm the four crossing totals 1, 3, 6 and 1. For reduced coprime dimensions u,v the count is (u-1)(v-1)/2, giving ten for 5-by-6 and 10-by-12. The formula is appropriately absent from the student pages.

## Operational review and limited recommendations

The elementary entries are operational rather than dependent on lcm, fractions or square roots: ruler handling and bounce-angle recognition for Problem 1; short-label reading, a diagonal counter move and direction tracking for Problem 2; following a diagonal pencil path and recognizing an X for Problem 3. Ordinary adult reading and a brief legal-attempt demonstration remain appropriate. These are genuine prerequisites, so omitting an independent K–1 equivalent is justified. The packet is a menu for return visits, not a seven-page completion assignment.

Two small facilitation/portability concerns are **hypotheses, not blocking defects**:

1. The explicit one-square-across/one-square-up-or-down definition appears on page 4, which carries a Grades 4–5 header; pages 6–7 carry Grades 2–5. Returning children have already used diagonal billiards, and page 6 supplies NE arrows and the common equal-angle rule, so they can start. If pages 6–7 will be distributed independently, carry the diagonal-rule strip into that print selection or make the one-sentence diagonal definition available there. A new lengthy worked example is unnecessary.
2. Counting all seven 24-step loops with a counter can become a memory demand if a child simultaneously tracks moves and counts. The supplied workspace permits tracing each edge and counting afterward; the adult guide should offer that recoverable record if needed. The mathematics does not require seven concurrent tallies or an additional student scaffold.

No classroom pacing, physical counter handling or ruler/tracing-paper reflection rehearsal was tested in this critic stage. The mathematical and rendered-PDF checks support a reviewable draft, not a claim of classroom readiness or piloting. No draft, base worksheet, guide, AGENTS file or global index was edited.
