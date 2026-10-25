# Review: Week 63 return visit (Cards away from home), draft v1

This is the review stage. I did not edit the draft.

## What I checked

- I rendered all 20 pages (K–1 5, Grades 2–3 6, Grades 4–5 9) at 80 dpi and looked at each one. I re-rendered the arrow, grid and forbidden-board pages at 200 dpi.
- At 254 dpi I measured the actual-size boards. The K–1 Problem 6 board is 105.2 × 45 mm (three 35 × 45 homes). The Grades 4–5 Problem 10 board is 175.2 × 45 mm and sits 18.8 mm from the left edge of the page, so it fits US Letter at 100% with about 22 mm to spare on the right. I compared the home label (letter and small picture in the top band) and the card pictures (A circle, B triangle, C square, D diamond, E star) with `lowell-math-circle-year-2/week-63/week-63-materials.pdf` (W63-M-v3). They match the kit.
- I rebuilt the draft from `draft/src/build.py` and `tikzlib.py` in a scratch copy. Every page is pixel-identical to `draft/*.pdf`, so the sources match the PDFs. The LaTeX logs show no overfull or underfull boxes, and nothing on any page overflows or overlaps.
- I read every board, grid and row from the rendered pages and the generated `.tex`, and solved them with my own script (not the author's `check.py`/`check3.py`): breadth-first search for fewest swaps, exact-m reachability, match totals, pairs and piles through five cards, every forbidden-spot board by enumeration, and all 1820 ways to cross out four cards on a four-home board (for 2–3 Problem 9).

**Verdict.** The mathematics is correct on every page. Every row, board and grid has the answer the brief implies, and the arrow and grid examples are drawn the right way round (W → U for "W sits in home U"; the dot for card V is in line V, column U). The packet follows the organizer's format closely: correct header and footer with page numbers, no titles, no encouragement, no hints, no lettered sub-steps. Each band covers its emphasis from the brief, and in each band the work moves from concrete to explanation. All three bands meet the physical rules: "any two cards, near or far" with a U–X swap of non-neighbouring cards shown before and after; refused pictures above the cell; 35 × 45 homes wherever real cards go on the page; a light record (a running swap word plus the final row); no tallies; and worked non-task visuals before the first arrows and the first grid.

What needs fixing:

- **2–3 Problem 9 is half answered before it starts.** Problem 8's fourth board already gives the minimum (0), and its first board already gives the maximum (9).
- **K–1 never says how to write a swap.** The 2–3 and 4–5 rules state the recording convention. K–1 has the "swaps" lines but not the sentence that says what goes on them.
- **2–3 Problem 3 is mostly answered by Problem 2 and can be read as having no answer.**
- **4–5 Problem 12 gives the new grid no concrete use before the hardest count in the packet,** and it mixes the five-card grids in with the four-card ones.
- **K–1 Problem 5's wording** and **crowded crossed-out cards on K–1 Problem 8** are smaller problems. Section B lists the minor points.

---

## A. Problems that should be fixed

### A1. 2–3 Problem 9 is answered by Problem 8

Problem 9 says: "Cross out four cards … so that as many of the 24 outcome cards as possible obey the board. Then cross out four cards on another board so that as few as possible obey it."

- **The minimum is on the page above.** Problem 8's fourth board (card A crossed out above every home) gives 0. A child has just counted it, and nothing can be fewer than zero. That half of the problem is empty.
- **The maximum is also on the page above.** Problem 8's first board (own homes) gives 9, and 9 is the largest possible. Of the 1820 boards with four crosses, exactly 24 reach 9, and those are the boards with one cross in each card and each home. So the first half becomes "can you beat 9?" That is a real question but a thin one for five minutes, and the proof that 9 is best is beyond grade 3.

**Data for a redesign.** With four crossed-out cards on four homes, the possible counts are 0, 4, 6, 7, 8 and 9 (the number of boards giving each is 8, 324, 384, 576, 504 and 24). Counts of 1, 2, 3 and 5 cannot happen. Problem 8 already shows 0, 4, 7 and 9, so only 6 and 8 are new:
- 8 obey: home A refuses A and B; home B refuses C and D.
- 6 obey: home A refuses A, B and C; home B refuses D.

**Suggested fix.** Keep "as many as possible." Replace the "as few as possible" sentence with targets that Problem 8 has not shown, for example: "Then cross out four cards so that exactly 8 obey, and four so that exactly 6 obey." The impossible 5 could go in the guide as a late puzzle. Another option is to make the whole problem "Which numbers of obeying outcome cards can four crossed-out cards make?", which uses all four printed boards. Either version keeps checking with the outcome cards as the activity and gives children a real search.

### A2. K–1 has no rule for writing a swap

The 2–3 and 4–5 rules end with "Write each swap as the letters of the two cards it trades." The K–1 rules leave this out. K–1 Problems 1–4 still have "swaps ____" lines, and the demo prints "VX" over the arrow without saying what it means. The K–1 adult is the parent volunteer, who is not a mathematician. That adult may write the number of swaps, or nothing at all, and then the running word is lost. The brief asks for a running word plus the final row, with swaps counted afterwards; without the word there is nothing to count from or to replay.

**Fix:** add the same sentence to the K–1 rules, where the adult reads it once: "Write each swap as the two letters of the cards it trades." Consider adding "The homes stay in place" too, which the other two bands have.

### A3. 2–3 Problem 3 is mostly answered by Problem 2, and its wording can be read as having no answer

- Problem 2 already includes BCDA and CDBA, and both need 3 swaps. So "Find a row … that takes as many swaps as possible" is done before the child starts, and only "Could any row need 4 swaps? Explain" is left.
- "Takes as many swaps as possible" can be read as "how many swaps can I use?" Wasted swaps (AB, AB, …) make that number unlimited. A playful third grader will notice. Problem 4 of the 4–5 packet says "need the most swaps", which is better.

**Suggested fix:** "Find every row of A, B, C and D that needs the most swaps to come home. Could any row need 4 swaps? Explain." The six answers are BCDA, BDAC, CADB, CDBA, DABC and DCAB (the single loops through all four cards). Give six small record rows instead of the one blank row now printed. This turns Problem 3 into a real find-every search, and it ties to the 4–5 count of hardest rows, (n − 1)!.

### A4. 4–5 Problem 12: the new grid gets no concrete use, and four-card and five-card grids are mixed

- The grid convention is introduced and then immediately used for "Count the rows that obey each grid below without listing them." That is the hardest computation in the packet: for the five-card strip, the count needs the numbers of non-clashing choices 9, 28, 35, 15 and 1; for the five-card ring, 10, 35, 50, 25 and 2. AGENTS.md asks that a new representation get its own concrete work before it carries an argument. Here the only use is the worked example.
- Children who try overlap counting need somewhere to mark which shaded squares they chose. The page has no blank copies of the grids, so they would redraw grids by hand. That makes transcription the demand, which AGENTS.md says to avoid.
- The order is Problem 10 four cards, Problem 10 five cards, Problem 11 four cards, Problem 11 five cards. A child who can manage four cards hits a five-card grid second.
- "Check that your counts match your lists from Problems 10 and 11" repeats what the captions already say. It reads like an automatic follow-up.

**Suggested fix:** put the two four-card grids first, or split them into their own problem with the five-card grids as the next problem, so stopping after four cards is natural. Add a row of small blank copies of the four-card strip grid, labelled as extra workspace, for marking chosen squares. Drop the "Check that…" sentence, since the captions already tie each grid to its list. Any scaffold that connects the grid to the base week's group repair (24 − 6 − 6 + 2) belongs in the guide, not on the page.

### A5. K–1 Problem 5 wording

"Put a counter on every card at home on the six A–C outcome cards. Are there more counters or more outcome cards? Which letter has the most counters?"

- "Card" means two different things in one sentence: the lettered pictures on an outcome card, and the outcome cards themselves. The 2–3 and 4–5 pages say "every letter that sits in its own home", which is clearer.
- "Which letter has the most counters?" assumes there is a winner. The answer is that all three tie at 2. A tie can be a nice surprise, but a question built on a false premise, read once to a kindergartner, is more likely to bring a guess. "How many counters does each letter get?" asks the same thing and matches the three answer boxes.
- The problem has three sentences. The standard for K–1 is one or two.

**Suggested wording:** "Put a counter on every letter at home on the six A–C outcome cards. Are there more counters or more outcome cards, and how many counters does each letter get?" A guide note: counters no wider than 12 mm are not in the base kit list (lettered sticky dots are). The brief's other route is pencil circles on an uncut copy of materials p. 2.

### A6. Crowded crossed-out cards on K–1 Problem 8 (and small ones on 2–3 Problem 8)

On K–1 Problem 8, homes B and C each have three crossed-out cards 9 mm wide. Inside a group the cards are 1.8 mm apart, but the gap between the B group and the C group is only 4.4 mm. A pre-reader matching pictures, or a parent glancing at the board, can easily assign a crossed card to the wrong home, and that changes the answer. The other K–1 boards and the 4–5 boards have gaps of 9.8 mm or more and are fine.

**Fix:** use narrower cards or a smaller gap inside each group so that groups are clearly separated (about 8 mm cards with 1 mm gaps leave about 9 mm between groups), or add a short tick from each group down to its home. The crossed cards on 2–3 Problem 8 are 7.5 × 9.5 mm with 8 pt letters, and the X runs close to the letter. They are readable on screen but tight on paper. Making them about 9 × 11 mm, like K–1, would help, and there is room.

---

## B. Smaller points

1. **4–5 has many "explain" requests.** Problems 1, 3, 5, 6, 7, 8 and 9 all end with explain or why, and 6–8 are three "without listing … explain" problems in a row. Each is defensible, but together they come close to the "not after every task" warning. Consider dropping "Explain" from Problem 7 (the pairs), where the prediction itself is the work, and leaving the why to the adult.
2. **4–5 Problem 1's record rows are all five-card,** but the problem asks about three, four and five cards. Group them as 2–3 Problem 1 does (a few four-card rows, a few five-card rows), or label which attempts are for which number of cards.
3. **4–5 Problem 1: "Explain why five cards cannot be done in fewer swaps"** assumes the child's answer is already the minimum. Something like "Explain why five cards need at least that many" has the same problem. Better: "…and explain why no fewer swaps will do."
4. **2–3 Problem 1: "in that fewest number of swaps"** is awkward. Write "in that many swaps."
5. **2–3 Problem 6's A–E part** (120 circles) goes past the 2–3 arithmetic in the brief ("counting to 24") and is listed as a 4–5 emphasis. It is fine as a late problem, since 5 × 24 ties nicely to the deck the children hold, but the guide should mark it optional.
6. **The label "outcome cards"** next to the small pile boxes in 2–3 Problem 7 (and "A–D" in 4–5 Problem 8) could read as a place to put cards. The boxes are too small for that, so the risk is low. "how many" would be clearer.
7. **Material sharing at the 2–3 table (guide note).** Two pairs share one cut A–D deck and one uncut sheet, so Problem 5 (uncut sheet) and Problems 7–9 (cut deck) cannot run at the same time for both pairs. The guide should suggest staggering.
8. **2–3 Problem 9's light grey menu cards** (gray!55, 7 pt) may print faintly on a weak home printer. Use a slightly darker grey.
9. **`draft/src/` includes build leftovers** (`__pycache__`, `.aux`, `.log`) and the author's scratch checks. If this moves to `lowell-math-circle-year-2/source/`, keep `build.py`, `tikzlib.py` and a tidy verification script, and drop the rest.

---

## Answer check, every problem

Rows are written as the cards in homes A, B, C, … in order.

| Band / problem | Verified answer |
|---|---|
| K–1 P1 | Fewest 2, ending BCA or CAB |
| K–1 P2 | Fewest 2; end rows BADC, CDAB, DCBA |
| K–1 P3 | Two swaps cannot (they touch at most four cards); three can, e.g. AB, CD, AE → BEDCA |
| K–1 P4 | CBA 1, BCA 2, BADC 2, BCDA 3 |
| K–1 P5 | 6 counters, 6 outcome cards, 2 per letter |
| K–1 P6 | Strip rule, three cards: BCA only |
| K–1 P7 | Strip rule, four cards: BCDA, CDAB, DCAB |
| K–1 P8 | Own or either neighbouring home: CDAB only |
| 2–3 P1 | Four cards 2 (BADC, CDAB, DCBA); five cards 3 |
| 2–3 P2 | CBAD 1, BCAD 2, DCBA 2, ACDB 2, BCDA 3, CDBA 3 |
| 2–3 P3 | Most is 3 (six rows, listed in A3); never 4 |
| 2–3 P4 | Yes: CDAB, DBCA. No: BCDA, BCAD, DACB |
| 2–3 P5 | 24 circles, 6 per letter |
| 2–3 P6 | 6; 120 |
| 2–3 P7 | Piles 9, 8, 6, 0, 1 (8 = 4 × 2, 6 = one per pair) |
| 2–3 P8 | 9, 7, 4, 0 |
| 2–3 P9 | Max 9 (one cross per card and per home); min 0 (see A1) |
| 4–5 P1 | 2, 2, 3 |
| 4–5 P2 | EBCDA 1, BCADE 2, BADEC 3, BCAED 3, BCDEA 4, DEABC 4 |
| 4–5 P3 | Fewest swaps = 5 − loops (loops of one count) |
| 4–5 P4 | Single loops through all five; 24 of them; 20 of the 44 home-free rows need fewer (3) |
| 4–5 P5 | BACDE: 1, 3, 5 yes, 2 and 4 no. BCADE: 2 and 4 yes, 3 and 5 no |
| 4–5 P6 | 24, 6 per letter; 120 |
| 4–5 P7 | 12; 60 |
| 4–5 P8 | 9, 8, 6, 0, 1; predicted 44, 45, 20, 10, 0, 1 |
| 4–5 P9 | 9 vs 8, 44 vs 45: the difference alternates +1, −1 |
| 4–5 P10 | BCA; BCDA, CDAB, DCAB; 16 rows (BCDEA BDAEC BDEAC BEDAC CDAEB CDEAB CDEBA CEDAB CEDBA DCAEB DCEAB DCEBA DEABC ECDAB ECDBA EDABC) |
| 4–5 P11 | BCDA, CDAB; 13 rows (the 16 above less ECDAB, ECDBA, EDABC) |
| 4–5 P12 | 3, 16, 2, 13 by the alternating sums in the brief; grids match the P10/P11 boards square for square |

Record space never gives away a count. Each list has more boxes than answers: K–1 P6 3 for 1, P7 5 for 3, P8 3 for 1; 4–5 P10 2/4/18 for 1/3/16, P11 4/15 for 2/13.

## Brief and constraint coverage (checked, no change needed)

- Every band's emphasis from the brief is covered, in its order. K–1 goes from home to home-free (2 and 2), brings mixed rows home, compares counters with cards, and hunts on actual-size boards. 2–3 covers kernel 1 with four cards, marks and piles on the 24 cards, and the optional question of whether the number of forbidden spots decides the count. 4–5 covers the loop explanation, hardest rows, parity, predictions without listing, the 44-and-45 alternation, and strip and ring rules last.
- Nothing repeats the base week. No page asks again for the home-free catalogs, the home-group overlap repairs or the recursive constructions. The plain own-homes board in 2–3 P8 is there for contrast and matches P7's 0-pile.
- The swap demo uses U–X, swaps the non-neighbouring cards V and X, and shows before and after with matching labels in all three bands.
- The arrow worked visual (4–5 P3) shows the input row, one arrow with "W sits in home U", and all arrows with loops of one. It does not reveal the swap count. The task pentagons use the same layout, and every chord avoids the other nodes.
- The grid worked visual (4–5 P12) shows the input row, one dot, and the full set of dots, with "cards" and "homes" labelled, and it uses a non-task shading.
- Forbidden rules are always visible as crossed-out pictures above the cell, never inside the 5 mm label band.
- Nothing asks for two reference rows at once, no six-card fact appears, no outcome cards go in a printed box, and no tally is kept during moves.
- Problems are numbered consecutively in each packet (K–1 1–8, 2–3 1–9, 4–5 1–12). Page counts of 5, 6 and 9 give quick children more than enough.
