# Week 17 (machine memory): math check

Scope:
- `lowell-math-circle-year-2/week-17/week-17-k-1.pdf` (W17-K-v2, 5 pp., Problems 1–6).
- `week-17-grades-2-3.pdf` (W17-23-v2, 5 pp., Problems 1–6).
- `week-17-grades-4-5.pdf` (W17-45-v2, 5 pp., Problems 1–6).
- `week-17-facilitator.pdf` (11 pp.: overview, launch, solutions, sources and the p. 11 route note).
- The return-visit companion in the same folder: `week-17-return-visit.pdf` (W17-RV-draft, 3 pp., Problems 1–3) and `week-17-return-visit-facilitator.pdf` (RV-17-FAC-v1, 5 pp.).

The archive folders were ignored, and I opened no use logs or session records. The four base PDFs are byte-identical (MD5) to `source/week-17/editable/reference-pdfs/`, and the two return-visit PDFs to `source/week-17-return-visit/reference-pdfs/`. I read `source/week-17/editable/src/*.tex`, `facilitator-src/build_guide.py` and `source/week-17-return-visit/student/return-visit.tex` for coordinates and data only. I did not run or import the packet's own `check_math.py`, `independent_checks.py`, `independent-checks.json`, `independent-check-results.json` or `verify.py`. My scripts and their outputs are in [checks/week-17/](checks/week-17/). Checked October 10, 2026.

**Result: every machine drawing matches its text, and every answer, list, count, witness, construction and minimum-state proof in the three base bands, the adult guide and the return visit is correct. I found 3 problems, all minor. One is a wording in return-visit Problem 1 that has a second reading, under which the guide marks a correct test answer wrong. One is the spare answer lines in Grades 2–3 and 4–5 Problem 1, which the guide does not mention. One is a K–1 hint that needs more red cards than the guide supplies.**

## How it was checked

- **`dfa17.py`** is this review's own model of a card machine: states, one start, one R and one B arrow per state, and a fixed YES/NO. It runs rows, decides language equality exactly (product search, not sample rows), minimises a machine (Moore refinement), finds the shortest common continuation that separates two histories, and enumerates every machine with k states (start fixed at state 0).
- **`pdfgeom17.py`** is a standard-library reader for the delivered PDFs. It handles pdfTeX object streams and ASCII85+Flate streams, interprets the content streams (q/Q/cm, paths, paint colours), and reads words with their boxes from `pdftotext -bbox`.
- **`extract_pdf.py`** (output `out_extract_pdf.txt`, data `pdf_data.json`) rebuilds every machine from the drawing itself. It reads the state circles and the words inside them, each stroked edge with the arrowhead at its end (the circle its tip touches), the start arrow, and the card label nearest the middle of each edge. It reads every card row from the coloured card shapes and the letter inside each one, and it counts the answer boxes and lines.
- **`check_math.py`** (output `out_check_math.txt`: 175 checks, 0 failures) covers the base packets and guide:
  - It checks every drawn machine for exactly one start and one R and one B arrow per circle, and proves which rule it recognises by exact equivalence.
  - It recomputes every printed row's answer, every "find every" list, every pair and continuation witness, and every minimum. Each minimum is checked three ways: minimisation, explicit pairwise-distinguishing histories, and a search of every smaller machine (66 machines for the three-state targets, 5,898 for groups of four, 1,054,474 for groups of five). The groups-of-six minimum rests on its six distinguishable histories.
  - It locates each guide claim verbatim in the guide text before comparing it, and it checks the guide's "Student page" references and the route note's problem numbers against the PDFs.
- **`check_return_visit.py`** (output `out_check_return_visit.txt`: 44 checks, 0 failures) does the same for the return visit. It also tests the equal-count impossibility argument on every machine with 1–3 states and on 3,000 random machines with 4–12 states.
- All four scripts were also run from a copy laid out as `plans/review/checks/week-17/` (repository files linked in, nothing written outside my run folder). They found the repository four folders up and reproduced byte-identical outputs.
- The two guide figures (pp. 3 and 7) were read at 150 dpi and against the drawing code in `build_guide.py`.

## K–1 (5 pp.): checks out

- **P1:** the drawing is start 1 (✓) and 2 (×), with B loops and R arrows both ways, so it says ✓ exactly for an even number of reds. The printed rows (no cards), B, RBR, RRR, RRRR, BBBRB give ✓, ✓, ✓, ×, ✓, ×. The example "B R: start 1 → 1 → 2; stop at ×" matches the drawing. There are 32 six-card ✓ rows, and three are asked for.
- **P2:** the machine says ✓ exactly when the last card is R. There are 8 four-card ✓ rows, which are the 2³ choices before a final R. The page prints 12 four-box slots, and the guide explains them.
- **P3:** the two machines are P1's and P2's. Exactly 32 six-card rows give different answers. The guide's criterion is exact: ends B with an even red count, or ends R with an odd one.
- **P4:** the start circle must say ×, and the drawn start is on the left circle. Exactly one two-circle machine works: start ×, other ✓, with R going to start and B to the other circle from both circles. One circle cannot work.
- **P5:** the minimum is 2. All 2 one-circle machines fail.
- **P6:** the drawing is a three-circle red cycle (✓, ×, ×) with B loops, so ✓ means a red count divisible by 3. The printed pairs are (no cards)/R, R/RR, RR/RBR and B/RRR. The first two can be separated, by nothing and by R respectively. The last two end on the same circle (remainders 2 and 0), so no common addition separates them.
- **Diagrams:** every circle is round, and every edge label sits within 15 pt of the middle of its own edge, and the next label is at least 25 pt farther (all bands and the return visit).

## Grades 2–3 (5 pp.): checks out (see Problem 2 for the P1 lines)

- **P1:** the machines are "even reds" and "last card R". Exactly 8 four-card rows make exactly one say YES: RRBR, RRBB, RBRR, RBRB, BRRR, BRRB, BBBR, BBBB. The example "B R: 1 → 1 → 2; NO" matches the drawing.
- **P2 / P3:** "at least one red" and "last card blue, NO for no cards" each need exactly 2 circles.
- **P4:** the printed pairs are (no cards)/R, R/RR, RR/RRR, RBR/RR, B/RRR and RB/BR. The first three separate: by nothing, by R and by nothing. The last three cannot be separated, because their red remainders are equal (2, 0 and 1).
- **P5:** the minimum is 3. Empty, R and RR are pairwise separated (by stopping, by stopping, and by R), and none of the 66 smaller machines works.
- **P6:** the minimum is 3. The guide's machine is N (no useful ending), R (last card R) and RB (last two cards RB), and it is correct for every row. Empty/R are separated by B, and RB is separated from both by stopping. None of the 66 smaller machines works.

## Grades 4–5 (5 pp.): checks out (see Problem 2 for the P1 lines)

- **P1:** the drawing is the red cycle 1 (YES) → 2 → 3 → 1 with B loops, so YES means a red count divisible by 3. Exactly 11 five-card rows are YES: BBBBB and the ten rows with three reds. The example "R B: 1 → 2 → 2; NO" matches the drawing.
- **P2:** the pairs are (no cards)/R, R/RR, RR/BRR and BBB/RRR. Stopping separates the first and R the second. The last two share a circle.
- **P3:** "no" is right. In every machine with at most 3 states, two rows of up to 3 cards that end on one circle are never separated by a common continuation of up to 3 cards. This is a direct check of the determinism argument.
- **P4:** the minimum is 4, and none of the 5,898 machines with at most 3 states works. The guide's witness (append 4 − i reds, or none if i = 0) separates every pair i < j.
- **P5:** the minimum is 3, as in Grades 2–3 P6.
- **P6:** the m-state cycle is correct and minimal for m = 1 to 10. The guide's witness (0 if i = 0, else m − i reds) separates every pair i < j < m. For groups of five, none of the 1,054,474 machines with at most 4 states works. For m = 1, one YES state with both loops works.

## Adult guide (11 pp.): mathematics checks out; see Problems 2 and 3

- **Overview (p. 1) and central argument (p. 3):** the model, the shared-circle lemma and the k-distinguishable-histories lower bound are stated with the right hypotheses. The facts all hold: m states for divisibility by m (any m ≥ 1), 3 for the suffix RB, and 2 for last-card and seen-red. Every solution entry matches the recomputation above. That includes the P3 left/right example directions, the "RBB" trap for an "RB has appeared" machine, and the "exactly two reds" extension (4 states, minimal).
- **Figures:** the p. 3 figure is 0 → 1 → 2 → 0 on R, with B loops and only 0 saying YES. The p. 7 figure is N → R and RB → R on R, R → RB on B, RB → N on B, and loops B at N and R at R. Both are the machines the text describes.
- **Counts (p. 10):** 66 = 2 + 64 machines with 1–2 states and 5,898 = 66 + 5,832 with 1–3 states, both with the start fixed. The row counts 8, 11 and 32 are right.
- **References:** every "Student page N" reference matches the PDFs, and so does the route note's problem numbering (p. 11).

## Return visit (3 pp. + 5 pp. guide): mathematics checks out; see Problem 1

- **Page 1 example:** X (NO, start) and Y (YES), with R to X and B to Y from both circles, says YES exactly when the last card is blue. The trace X → X → Y → Y on RBB is right.
- **P1 (RR anywhere):** the guide's N/P/F table is correct and minimal (3), and none of the 66 smaller machines works. The test rows RRBB, RBR and BRRB give YES, NO, YES under the intended reading.
  - The return question (RBR anywhere) has 4 states, and the guide's transitions are correct and minimal. Its witnesses (BR or R, and stopping) work.
- **P2 (both counts even):** the four-corner machine is correct and minimal, and none of the 5,898 machines with at most 3 states works. The table rows (no cards), R, RB, RRBB, BBR and BRBR give YES, NO, NO, YES, NO, YES.
  - The extension "even reds and last card blue" has 3 states, and the guide's E/F/O machine is correct. The two odd-red cells of the 2×2 grid do have identical futures.
- **P3 (equal counts):** RRBB, RBRB and BRR give YES, YES, NO. Every machine with 1–3 states is wrong on some row of length at most 2m. The guide's argument always finds the error: run R⁰…Rᵐ, find a collision i < j, append i blues. That held for all of them and for 3,000 random machines with 4–12 states.
  - The stated limits (bounded length, extra counters) are correct. Twelve cards per colour suffice for collision trials up to 8 states when each row is run on its own: at most 8 reds and 7 appended blues.

## Problems

### 1. Return visit, page 1, Problem 1: "in a row" has a second reading that the guide marks wrong (minor)

- **Text:** "Build a machine that says YES exactly when two red cards in a row have appeared anywhere. It must still say YES after more cards arrive. How few states can it use?" Test rows printed: RRBB, RBR, BRRB.
- **Evidence:**
  - On these pages "row" is the word for a card sequence: "Start fresh for each new row" (p. 1), "the row has an even number of red cards" (p. 2), and "a card row", "rows of every length" (p. 3).
  - Read as "two red cards have appeared anywhere in the row", the target is "at least two reds". That target also needs exactly three states (0, 1, 2+ reds; `out_check_return_visit.txt`), so a child gets a sound three-state machine.
  - On the printed rows that reading gives YES, YES, YES. The guide (p. 3) says "The printed test rows RRBB, RBR and BRRB should say YES, NO, YES respectively". RBR is the one row where the two readings differ, so an adult with the guide would mark RBR wrong.
  - The minimum, 3, is the same under both readings, and most readers will take the idiom as "consecutive".
- **Smallest fix:** say "two red cards next to each other", for example "…exactly when two red cards next to each other have appeared anywhere." Alternatively, add one guide sentence: if a child counts any two reds, accept the three-state counter and use RBR to show the two rules differ.

### 2. Grades 2–3 p. 1 and Grades 4–5 p. 1, Problem 1: spare answer lines with no guide note (minor)

- **Text:** "Find every four-card row that makes exactly one of these machines say YES" (2–3), printed with 12 answer lines. "Find every five-card row this machine sends to YES" (4–5), printed with 15 short answer lines and 3 long ones.
- **Evidence:** exactly 8 rows answer the first and 11 the second (`out_check_math.txt`), so 4 lines stay empty in each.
  - The spare lines are deliberate: the packet's own `review/student-draft-review.md` says the slots "do not disclose the count".
  - K–1 P2 has the same feature, and its guide entry deals with it: "Provide blank paper rather than treating the twelve printed slots as an answer count."
  - The guide's 2–3 P1 and 4–5 P1 entries say nothing about the spare lines. Their texts ("This accounts for all possibilities"; "precisely the choices of two B positions") do tell the adult that the list is complete. The remaining risk is a child who stops at 8 or 11 and thinks the list unfinished, or keeps hunting for 12 or 15.
- **Smallest fix:** add one sentence to each guide entry, as in K–1 P2: "Four printed lines stay empty; the lines are not an answer count. Ask how the child knows the list is complete."

### 3. Adult guide p. 4, K–1 Problem 2 hint: more red cards than the guide supplies (minor)

- **Text:** "If the list has repetitions, sort the physical rows by first card, then second." The materials on p. 2 are "For each of three tables: … 12 R cards and 12 B cards".
- **Evidence:** the eight answer rows (RRRR, RRBR, RBRR, RBBR, BRRR, BRBR, BBRR, BBBR) use 20 R and 12 B cards (`out_check_math.txt`). Sorting all the physical rows needs at least 20 red cards even for one child, and more if the list has the repetitions the hint is about. A K–1 table of up to four children has 12.
- **Smallest fix:** "sort the rows recorded on the page by first card, then second". Alternatively, supply 20 R cards to a child sorting P2 physically.
