# Week 11 (chip firing with a sink): math check

Scope: `lowell-math-circle-year-2/week-11/week-11-k-1.pdf` (F11-K-v3, 6 pp., Problems 1–6), `week-11-grades-2-3.pdf` (F11-23-v3, 6 pp., Problems 1–6), `week-11-grades-4-5.pdf` (F11-45-v3, 6 pp., Problems 1–6) and `week-11-facilitator.pdf` (12 pp.). I also checked the return-visit companion in the same folder: `week-11-return-visit.pdf` (F11-RV-v1, 3 pp., Problems 1–3) and `week-11-return-visit-facilitator.pdf` (RV-11-FAC-v1, 5 pp.). Sources: `source/week-11/editable/src/build_packets.py` (which writes the three student `.tex` files), `facilitator-src/`, and `source/week-11-return-visit/`. I did not use the packet's own checkers (`build_packets.py`'s asserts, `checks.json`, `verify.py`, `independent_checks.py`). Archive folders were ignored, and I opened no use logs or session records. My scripts and their outputs are in this folder, for `checks/week-11/`. Checked October 10, 2026.

**Result: every answer, word, count and claim in all three bands, the return visit and both adult guides is correct, and every problem can be done as stated. Every printed board matches its text. I found 3 minor problems, none of which changes a stated answer: two K–1 wordings where a natural reading changes the count or the answer (items 1 and 2), and one optional argument in the base guide that skips a step (item 3).**

## How it was checked

- `chipfire.py` is my own solver. It fires chips on any undirected board, with or without a sink, and finds every complete legal firing word, or the set of (finish, firing counts, sink chips) over all legal orders by a memoised search over states. It also handles interleaved single-chip additions with firing at any time, and explores every state reachable on a sink-free board, with cycle detection.
- `extract_pdf.py` (outputs `extract_pdf.out`, `pdf_geometry.json`) reads the delivered PDFs with pdfplumber's drawing objects:
  - **Boards.** It finds every circle and sink, gives each circle the letter printed beside it, and turns each line into an edge by attaching its ends to the shapes they touch. All 18 base boards, the 3 return-visit working boards, the 3 return-visit example panels and the 3 guide thumbnails on p. 5 give exactly the intended graphs: triangle A–B, A–S, B–S; four-cycle S–A–B–C–S; extra line, which adds A–C; and the closed triangle A–B–C. Every base circle is 44.0 × 44.0 mm and every base sink a 60.0 × 60.0 mm square. Return-visit circles are 42.0 mm and sinks 55.0 mm circles, as both guides say. The closed triangle on return-visit p. 1 is equilateral to 0.05%. There are no regular polygons beyond that triangle.
  - **Tables.** Every ruled table, with cell text and the number of chip dots drawn in each cell. The K–1 starts are dots, and the script counts them.
  - **Worked example.** The return visit's three-panel example has 2 chips at A before, arrows A→B and A→C, and chips at B and C after.
- `check_answers.py` (output `check_answers.out`) reads every start from `pdf_geometry.json` and checks it against my own transcription. It then solves every problem and runs 259 checks of the pages and both guides: finishes, firing counts, sink chips, every quoted word, the alternative orders, every all-starts table and every repeated-addition table. It also checks the general claims in the overview over all starts in a box: termination scores, the least-action characterisation, the triangle formula, staged additions and the monoid. It found 0 mismatches. Its 3 NOTE lines are items 1–3 below. The script ends by confirming that each guide sentence I compared is present in the PDF text.
- `source_vs_pdf.py` (output `source_vs_pdf.out`) confirms the delivered PDFs are byte-identical (MD5) to `source/week-11/editable/reference-pdfs/` and `source/week-11-return-visit/reference-pdfs/`. It also confirms all 21 problem statements and the three sets of shared rules from the sources appear in the PDFs. pdfLaTeX is not installed here, so I could not test a clean rebuild.

Order independence holds on these boards: over all legal orders, every start gives one finish and one count vector. That was checked for every start below 13 per circle on the triangle, 9 on the four-cycle and 8 on the extra line. The number of complete legal words ranges from 1 for (4,0) to 109,584 for (0,12,0).

## K–1: all answers correct; two wordings with a second reading (items 1, 2)

- **P1:** (2,2) → (1,1); (3,2) → (1,0); (2,3) → (0,1); (3,3) → (1,1). Each start has at least two complete orders, so the order question can be tested, and order never changes the piles. The guide's share counts and orders (AB, ABAB, ABBA, ABAB) are right.
- **P2:** with 4 chips, (0,4) → (0,1), (1,3) → (1,0), (2,2) → (1,1), (3,1) → (0,1), (4,0) → (1,0). With 5 chips, (0,5) → (1,0), (1,4) → (1,1), (2,3) → (0,1), (3,2) → (1,0), (4,1) → (1,1), (5,0) → (0,1). Each total has exactly the three finishes (1,0), (0,1) and (1,1). The answer is the same whether or not one-sided starts count.
- **P3:**
  - (0,4,0) → (1,0,1). The only words are BBACB and BBCAB.
  - (2,2,0) → (1,1,1).
  - (0,2,2) → (1,1,1).
  - (2,0,2) → (1,0,1).

  All of these are as in the guide.
- **P4:** the 8 stable placements are the 0/1 triples, and the capacity is 3, so no placement uses 4 chips. The table has 8 rows; see item 1.
- **P5:** I tried every interleaving of single-chip additions with legal sharing. (3,3) always finishes (1,1) and (2,4) always (1,0). The guide's intermediate batch states are all right.
- **P6:** (1,0), (0,1), (1,1), repeating. (0,0) has no incoming arrow, so it never returns; see item 2. The guide's state diagram on p. 7 matches the computed map arrow for arrow. Adding at B runs the same cycle backwards, as the extension says.

## Grades 2–3: checks out completely

- **P1:** (2,2) → (1,1) with counts (1,1); (4,0) → (1,0) with (2,1); (3,3) → (1,1) with (2,2). (4,0) has the single word AAB, so "if possible" is needed and is printed.
- **P2:** (0,4,0) → (1,0,1) with counts (1,3,1); (2,1,2) → (1,1,1) with (1,1,1); (2,4,2) → (1,0,1) with (3,5,3), from 180 complete words. Every start has at least two orders, as the unhedged wording needs. All six guide words are legal and complete.
- **P3:** of the seven six-chip starts, (0,6), (3,3) and (6,0) finish at (1,1). The table has one row per start.
- **P4 (extra line):**
  - (3,0,3) → (2,0,2) with counts (1,1,1).
  - (0,6,0) → (2,0,2) with (1,4,1).
  - (2,2,2) → (2,0,2) with (1,2,1).
  - (4,1,2) → (2,1,0) with (2,2,2).

  Every start has a choice of order. All eight guide words are legal, and the added line does change some finishes.
- **P5:** all three timings, and every interleaving, finish at (1,1,1) with total counts (2,3,1). The intermediate states are (0,1,0) and (1,0,1).
- **P6:** the A column is (1,0), (0,1), (1,1), … and the B column is (0,1), (1,0), (1,1), …. Each rule reaches exactly those three pairs.

## Grades 4–5: checks out completely

- **P1:** (2,2), (4,0), (3,3) and (5,4) give finishes (1,1), (1,0), (1,1), (1,0); counts (1,1), (2,1), (2,2), (4,4); sink chips 2, 3, 4, 8. AABABBAB and BBAABAAB are legal and complete. For a fixed start the counts never differ: on a sink board L is invertible, and I also checked every start up to 14 + 14.
- **P2:** 4 at B with 2 at A gives (1,1,1) for all three timings; 3 at A with 3 at C gives (1,0,1) for all three.
- **P3:** the four rows are as in the guide. (1,0), (0,1) and (1,1) return at After 3. (0,0) and (1,1) both go to (1,0) after one addition.
- **P4:** the same extra-line results as Grades 2–3 P4. Every start has at least two orders.
- **P5:** (0,12,0), (6,0,6) and (4,4,4) all finish (1,0,1), with counts (5,11,5), (5,5,5), (5,7,5) and 10 chips in the sink. W = 3A + 4B + 3C drops by exactly 2 at every legal firing on the four-cycle and on the extra line, for every state up to 8 per circle. That gives the scores 48, 36, 40 → 6, so 21, 15 and 17 moves.
- **P6:** (0,8,0) → (1,0,1), counts (3,7,3), 6 in the sink, 180 complete words. Both guide words are legal 13-move runs and are A↔C swaps of each other. The quota argument is a correct least-action proof.

## Adult guide (base)

All 18 keys, every hint and every extension are correct. So are the overview's facts:

- **Stable states and capacity:** 4, 8 and 18 stable states, with capacities 2, 3 and 5.
- **Termination:** the theorem and proof under the sink hypothesis, and the score certificates. A + B drops by 1 per firing on the triangle.
- **Least action:**
  - the odometer is the componentwise least f with c − Lf < d, and the unique minimiser of Σf over 0 ≤ c − Lf < d. I checked this by brute force over f.
  - the (2,2) spurious balance solution (0,0) does not select the finish.
- **Triangle formula:** the residue formula for S(a,b), with S(0,0) = (0,0), and the u_A and u_B formulas, for all a, b ≤ 40.
- **Staged additions:** S(S(x)+y) = S(x+y), 3,000 random pairs per board.
- **The operation on stable states:** ⊕ is commutative, associative and has identity 0, but is not a group, on all three boards.
- **Finishing empty:** only the empty start finishes empty on the printed boards, while a lone circle joined only to the sink can.
- **Sink-free triangle:** the cycle (2,1,0) → (0,2,1) → (1,0,2) → (2,1,0).
- **Materials:** the largest prescribed total is 12, and 264 = 24 × 11.

Page cross-references (pp. 2, 3, 7 and 9) point to the right pages. I did not check the page and lemma numbers cited from Holroyd et al. or Levine–Propp. Item 3 is the one gap.

## Return visit: checks out completely

- **P1 (closed triangle):** (3,0,0) can only fire A and stops at (1,1,1). From (2,1,0) every run is the forced cycle A, B, C. From (4,0,0) no stable state is reachable (5 reachable states) and every run repeats. AABC reaches (2,1,1) again. Up to symmetry the three-chip types stop, cycle or are already stable, exactly as the guide says.
- **P2 (four-cycle):** over all 24 trials (8 stable starts × 3 sites), the maximum is 4 firings. Only (1,1,1) + B reaches it, with exactly the words BACB and BCAB, counts (1,2,1), finish (1,0,1) and 2 chips in the sink. (1,1,1) + A gives only ABC → (1,1,0), and (1,1,1) + C only CBA → (0,1,1). Every other start gives at most 2 firings, an addition to an empty circle gives none, and B fires twice only in the maximal trial.
- **P3:** the legal four-letter words are exactly BBAB, BBBA; ABAB, ABBA, BAAB, BABA; and AAAB, AABA. All end at (1,1) with 4 in the sink. The inverse continuation is right too: only (0,6), (3,3) and (6,0) finish (1,1) after four firings, and four reverse moves from (1,1) give exactly these eight histories.

## Problems found

### 1. K–1 Problem 4: the eighth row is the empty board, which the task need not count (p. 4; guide p. 7)

- **Quoted text:** "Problem 4: Find every way to put chips on A, B, and C so that no circle can share. Can any of these ways use 4 chips?" The page has an A | B | C answer table with 8 blank rows. The guide answers "The complete set of eight is (0, 0, 0), (0, 0, 1), …", and its hint is "Once the child has examples, sort them by whether A is empty; each half has the four B/C choices."
- **Evidence:** the four-cycle has 8 stable placements, but only 7 use any chips (`check_answers.out`, NOTE line). A K–1 child can reasonably decide that putting no chips is not "a way to put chips", find all seven, and then search for an eighth that only exists under the other reading. The guide never says the eighth is the empty board. It does say this for the analogous Grades 2–3 Problem 3: "ask whether an empty circle is permitted at the start".
- **Smallest fix:** add to the guide's P4 hint: "If a child stops at seven, ask whether a board with no chips counts; the eighth way is (0, 0, 0)."

### 2. K–1 Problem 6: "empty circles" also reads as "an empty circle", which flips the answer (p. 6)

- **Quoted text:** "Problem 6: Start with empty circles, then add one chip to A at a time, finishing all the sharing after each chip. Can you ever get empty circles again?" The guide (p. 7) says "No later stable finish is empty."
- **Evidence:** after 1, 2, 4, 5, 7, 8, 10 and 11 chips the finish is (1,0) or (0,1), so one circle is empty in 8 of the 11 rows (`check_answers.out`, NOTE line). A child who reads "empty circles" as "a circle with nothing in it" will answer "yes" and be right. The intended answer, both circles empty, is "no".
- **Smallest fix:** "Can both circles ever be empty again?"

### 3. Guide p. 8, Grades 2–3 Problem 3 optional invariant: the remainder alone does not rule out (0,0)

- **Quoted text:** "Optional invariant for a ready child. On the triangle, the remainder of A − B upon division by 3 never changes: an A move changes it by −3, a B move by +3. The three nonempty stable pairs have different remainders. This explains the repeating pattern here."
- **Evidence:** (0,0) and (1,1) both have A − B ≡ 0 (mod 3) (`check_answers.out`, NOTE line). So for exactly the three answers to the problem, (0,6), (3,3) and (6,0), the remainder cannot tell the finish (1,1) from (0,0). The step "a start with chips never finishes empty" is used but not given here; it appears only on p. 3. An adult using this paragraph alone cannot answer a child who asks "why not (0, 0)?"
- **Smallest fix:** before "The three nonempty stable pairs…", insert: "A start with chips never finishes empty, because the last share always leaves a chip on the other circle."
