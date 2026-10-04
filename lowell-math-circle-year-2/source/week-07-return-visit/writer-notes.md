# Week 7 writer-stage record

Prepared draft, unpiloted. One shared student PDF with three distinct investigations:

| Page | Problem | Suitable band on page | Exact task starts |
|---|---|---|---|
| 1 | 1, one shared PASS | Grades 2–5 | Piles 1–12, PASS available and already used |
| 2 | 2, remembered LAST | Grades 4–5 | Piles 1–8, no previous move / LAST 1 / LAST 2 / LAST 3 |
| 3 | 3, fixed-gap pairs | Grades K–5 | A: one row 4; B: two rows 2+2; C: one row 5; D: one row 3; E: one row 6; F: one row 9 |

The page-level bands describe the genuine entry points. The PASS and LAST pages are not offered as K–1 memory tasks. Problem 3 provides six concrete boards whose legal moves a partner can check; its guarantee question can continue at greater readiness. Problem 2's prediction for larger piles is a continuation after concrete state experiments. This stage contains student pages and a writer record only, with no facilitator guide.

## Exact answers

“Winning” always means the player about to move can force a win against any legal play. Experimental wins against a partner alone do not establish that fact. Empty piles are terminal; the previous player has already won. A pass from an empty pile is not legal.

### Problem 1

| Starting pile | Winning first moves, PASS available | Winning first moves, PASS used |
|---|---|---|
| 1 | Take 1 | Take 1 |
| 2 | Take 2 | Take 2 |
| 3 | PASS | None |
| 4 | None | Take 1 |
| 5 | Take 1 | Take 2 |
| 6 | Take 2 or PASS | None |
| 7 | None | Take 1 |
| 8 | Take 1 | Take 2 |
| 9 | Take 2 or PASS | None |
| 10 | None | Take 1 |
| 11 | Take 1 | Take 2 |
| 12 | Take 2 or PASS | None |

Circle 1, 2, 3, 5, 6, 8, 9, 11, 12 in the available list; circle 1, 2, 4, 5, 7, 8, 10, 11 in the used list. PASS changes the forced winner at 3, 4, 6, 7, 9, 10, 12.

For positive piles without PASS, exactly the multiples of 3 lose. With PASS available, exactly 4, 7, 10, … lose. The pile of 1 is an important exception to an unqualified “1 modulo 3” description. Piles 1 and 2 end immediately with the winning take. Pile 3 wins by spending PASS. For larger available piles: a pile congruent to 1 modulo 3 can only take to available winning states or pass to an ordinary winning state; every other positive residue can take to an available losing state or pass to an ordinary losing state. This supplies the induction, with the small boundaries checked directly.

The procedural example uses a non-task pile of 14 and shows that spending PASS leaves all 14 counters while changing the physical card state. It reveals no winning strategy.

### Problem 2

Entries give every winning first take; a dash is a losing state.

| Pile | No previous move | LAST 1 | LAST 2 | LAST 3 |
|---|---|---|---|---|
| 1 | 1 | — | 1 | 1 |
| 2 | 1, 2 | 2 | 1 | 1, 2 |
| 3 | 3 | 3 | 3 | — |
| 4 | — | — | — | — |
| 5 | 1 | — | 1 | 1 |
| 6 | 1, 2, 3 | 2, 3 | 1, 3 | 1, 2 |
| 7 | 3 | 3 | 3 | — |
| 8 | — | — | — | — |

Thus circles by column are: no previous move, 1, 2, 3, 5, 6, 7; LAST 1, 2, 3, 6, 7; LAST 2, 1, 2, 3, 5, 6, 7; LAST 3, 1, 2, 5, 6. Pile 1 with LAST 1 loses because no move is legal, even though a counter remains.

For all positive n, losing residues modulo 4 are:

| Initial LAST state | Losing residues |
|---|---|
| No previous move | 0 |
| 1 | 0, 1 |
| 2 | 0 |
| 3 | 0, 3 |

The exact recurrence uses both pile and last move: W(n,last) is true precisely when some legal k in {1,2,3}, k ≤ n and k ≠ last, leads to false W(n−k,k). No previous move is coded 0. W(0,last) is false as a terminal next-player state. For the general statement, check n=1,2,3 directly, then apply the residue table inductively. At residue 0 all possible moves lead to winners. At residue 1, take 1 leads to a loser unless forbidden by LAST 1; the other legal moves then lead to winners. At residue 2, take 2 leads to a loser when legal, and take 1 does so when LAST 2 forbids taking 2. At residue 3, take 3 leads to a loser unless forbidden by LAST 3; the other moves then lead to winners.

The worked non-task visual has input 13 counters, LAST 1; intermediate removal of 2 while the old LAST remains visible; output 11 counters, LAST 2. It shows both updates without assigning a winner.

### Problem 3

Circle A, D, E. These are all first-player winning starts:

- A, row 4: remove squares 2 and 3. The two isolated survivors have no legal pair.
- B, rows 2+2: loses. The second player removes the remaining row after the first removes one row.
- C, row 5: loses. An end pair leaves a row of 3; an interior pair leaves one isolated counter and a row of 2. Either successor wins immediately.
- D, row 3: remove either pair; the single survivor has no legal pair.
- E, row 6: remove squares 3 and 4, leaving two equal rows of 2. The second player in the original game must take one row, and the first takes the other.
- F, row 9: loses. Up to reflection, its possible first-removal successors have run lengths (7), (1,6), (2,5), (3,4). The checked recursion classifies every one as winning for the next player. All eight pair positions were examined, not just these representatives.

Single rows of lengths 1–12 lose exactly at 1,5,9; 0 is terminal. This finite check does not assert a continuing period. Every even single row is winning by removing its central pair and then mirroring replies across the two equal halves. Equal duplicate rows lose by the corresponding-row reply; gaps remain fixed on each row throughout. The equal-row strategy does not require Nim terminology.

The procedural visual uses a non-task row of 7, removes squares 2 and 3, and leaves the empty squares in their original locations between a survivor of length 1 and a survivor run of length 4.

## Physical and drawing dimensions

- US Letter, 8.5 × 11 inches; page origin 0.55 inches from the top and left, content width 7.40 inches. Print at 100% scale.
- Every active Problem 3 square is exactly 0.80 × 0.80 inches (57.60 × 57.60 PDF points), with equal axis scaling. Counters at most 0.75 inches diameter leave 0.05 inches of nominal clearance. The nine-square board is 7.20 inches long and stays inside the 7.40-inch content width.
- B is one start with two separate, fixed two-square rows. Its two row centres are 0.90 inches apart, with 0.10 inches between printed row boundaries. A bracket groups the rows. Each board can be rebuilt between games; gaps made during play stay empty.
- The 0.20-inch squares in the tiny worked example illustrate the procedure and are not active counter mats. The active boards are the six large labelled starts below Problem 3.
- PASS procedural cards are 0.76 × 0.46 inches and LAST illustrations 0.78 × 0.56 inches. These are reference icons, not cutouts or fitted holders. Use the supplied shared PASS and three LAST cards beside the playing counters.
- Rule wording specifies “neighbouring squares,” because counters smaller than the square pitch need not physically touch.
- Children build one chosen start at a time, requiring at most 9 counters for a row game, 12 for the PASS tasks, or 8 for the LAST table. LAST's rule explicitly replaces the previous face-up card so only one previous move is visible.

## Verification and reproducibility

`src/check_games.py` checks all displayed states and emits `math-checks.json`. It also checks the PASS and LAST residue formulas through n=100, the single-row classifications through 12, duplicate rows through length 12, and even single rows through length 12. The general arguments above distinguish the proved state formulas and symmetry arguments from the finite row check. The pair recursion splits at every legal removed pair, keeps all resulting run lengths, and omits isolated counters only from its canonical mathematical key because they can never move; they remain physically on the board.

`sh src/build.sh` builds `return-visit.pdf` using portable LaTeX/TikZ; `PDFLATEX` can select another TeX engine path. The source package needs no repository files, fonts beyond a normal TeX distribution, or downloaded images. The build intermediates stay in `draft/build/`. Final PDF pages were rendered to `draft/renders/` and all inspected; no clipping, overlap, or TeX warnings found. A clean build from the extracted `return-visit-source.zip` matches all three pages' text and rendered pixels. Vector geometry checks confirm all 31 active square boundaries are 57.60 × 57.60 points. Physical printing, materials rehearsal, and classroom use have not been tested.
