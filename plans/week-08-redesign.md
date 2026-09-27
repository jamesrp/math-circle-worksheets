# Week 8: Rook moves, Nim, and changing the losing set

Redesigned September 19, 2026; review revisions September 20, 2026. Prepared, not taught. Use Week 1’s standard of an approachable experiment leading to a theorem, obstruction, optimization, or controlled mathematical question. Three core entry levels plus **one optional grades 6–7 page**. Full launch prompts, hints, checked solutions, and the 60-minute operating plan are in the [four-page facilitator guide](../lowell-math-circle-year-2/week-08/week-08-facilitator.pdf) and its [editable source](../lowell-math-circle-year-2/source/week-08/week-08-facilitator.tex).

## What changed

The original middle activity now requires both halves of a universal winning-position argument. The upper king-variant task is replaced by three-pile Nim, a counterexample to naive matching and to even-total conjectures, then a constructive binary proof. The extra changes the move set again, leading to Wythoff pairs and the golden ratio.

## Entry points and mathematical work

Grade labels are approximate. Reading can always be supported by adult scribing/read-aloud; moving objects and giving an oral explanation count as mathematical work.

| ID suffix | Investigation | Student pages | Prerequisites: reading/arithmetic/reasoning | Main work |
| --- | --- | --- | --- | --- |
| K | Race to the star / Can you copy my move? | 2 | No independent reading; count to 2 or compare distances physically. Follow a turn rule, inspect every option from the center, and copy a move in the other direction. | Play on a 3-by-3 board; investigate center and top-left; translate matching to two piles of 2. |
| M | Map the traps / The board is two piles | 2 | Short instructions can be read aloud; count to 7. Reason about every opposing move versus one winning response. | Classify a 4-by-4 board, prove the equal-pile rule for arbitrary rectangles, then break a naive generalization with three piles. |
| U | Three piles break the mirror / Binary balance | 3 | Small subtraction and odd/even; binary representation is built from 1/2/4/8 bundles. Follow a two-direction strategy proof and a highest-bit argument. | Play (1,2,3) and (1,2,4); test (1,1,2) against even-total reasoning; find zero-XOR positions and prove how to reach them. |
| X | One new move, a new world | 1 | Organize a table and subtract. Floor and square-root notation are explained for the final comparison; the greedy part needs neither. | Classify Wythoff positions through 7, generate greedy pairs, distinguish no-edges-between from completeness, test the golden-ratio theorem. |

The complete IDs are **F08-K/M/U/X-v2**. There is no extra packet for the lower groups; offer the next entry level when appropriate.

## Materials, launch, and hour

About 60 counters, five paper plates or marked pile areas, pencils, and scraps labeled 1, 2, 4, 8. Reuse the counters between trials; no chess pieces are necessary. Print three K1 packets, three middle packets, and one upper packet: **15 core student sheets**, plus the single extra sheet if wanted. Print single-sided, US Letter; actual size is recommended but no physical fitting depends on calibration. Introduce one page at a time.

**Launch:** Can you leave me a square where every move helps you? Let children show all legal moves before asking for a pattern. Demonstrate a long rook move so the game is not mistaken for one-step movement.

**Proposed hour:** 0–10 explore tokens and piles; 10–15 brief common rule demonstration; 15–35 main investigation: play, classify, and challenge claims; 35–40 movement/reset; 40–55 continue at the group’s stopping point or choose an optional proof; 55–60 share one move with its reason and tidy.

One parent stays mainly with K,K,1; the organizer alternates between 3,3,3 and the fifth grader, aiming for a return within five minutes and leaving a concrete next attempt. Roles rotate within triplets, preserving two opposing sides for games. The fifth grader needs actual adult mathematical conversation. The exact timetable and staffing are this project’s proposal, not a documented arrangement from the books.

**Hints and pacing:** first ask a child to demonstrate the rule and show their current attempt; next ask for a smaller example or counterexample; only then offer the organizing representation on the next page. The facilitator gives specific hint ladders. A corrected conjecture is valuable. Do not fill time with copying or require finishing every task.

## Stopping points and optional proof continuations

| Group | Satisfying stopping point | Optional proof continuation |
| --- | --- | --- |
| K–1 | Show both moves from the center and their replies, then copy a move on equal two-pile starts. | Explain why matching still works from the top-left or any two equal piles. |
| 2–3 | Classify the 4-by-4 board and explain how to restore equality from an unequal pair. | Prove both directions for all two-pile starts and explain termination; then challenge a three-pile guess. |
| 4–5 | Refute the even-total rule and find a legal balancing move using bundles. | Prove that every move breaks balance, every unbalanced start can be repaired, and play terminates. |

Record the achieved claim separately from any theorem supplied by an adult; the full Nim proof is a continuation, not a completion requirement.

## Verified mathematical backbone

The rook state is the pair of remaining horizontal/vertical distances. A move reduces exactly one coordinate. Equal pairs are losing: every move breaks equality and every unequal pair can restore equality by reducing its larger coordinate. The total strictly decreases. This establishes both directions and termination.

Three piles change the question. (1,1,1) is winning by removing a pile; (1,1,2), despite even total, is winning by removing the 2-pile. For (1,2,3), each of its six first moves has a response leaving two equal piles and one empty pile; the facilitator prints all six.

For any number of piles, write binary digits and add each column modulo 2. A legal single-pile move changes at least one column, so zero XOR cannot remain zero. If XOR s is nonzero, choose a pile x with a 1 in the highest 1-bit of s, and replace it by x XOR s. All higher bits stay fixed, the highest changed bit drops, and lower bits total less than its value; therefore the pile strictly shrinks. New XOR is zero. This is both a proof and a winning-move algorithm.

Checked upper starts: (2,4,6) and (3,5,6) are balanced; moves (3,4,5)→(1,4,5), (1,5,7)→(1,5,4), (7,10,12)→(6,10,12) restore balance. For any first two piles, the unique balancing third is their XOR.

The extra's sorted losing pairs through 7 are (0,0),(1,2),(3,5),(4,7); greedy rows n=4,5 give (6,10),(8,13). Distinct pairs have disjoint coordinates and distinct differences, so no legal move joins them. That argument alone does **not** prove every outside position reaches the list. The golden-ratio formula is supplied as a known theorem, not inferred from a short table. Extra examples move (2,4)→(2,1), (5,8)→(4,7), (8,12)→(6,10).

## Sources and boundary between class and research

- JRMF, *Rook’s Move Activity Guide*, local PDF pp. 3–6: exact rook rule, losing-position strategy, and Wythoff link. The three-pile sequence is our adaptation.
- Charles L. Bouton, *Nim, a Game with a Complete Mathematical Theory*, *Annals of Mathematics* 3 (1901–02), pp. 35–39. [Primary historical paper hosted at Caltech](https://paradise.caltech.edu/ist4/lectures/Bouton1901.pdf). The paper’s historical binary analysis motivates the connection; the normal-play proof used here is provided independently in the guide.
- Aviezri S. Fraenkel and Udi Peled, *Harnessing the unwieldy MEX function*, *Games of No Chance 4*, MSRI Publications 63 (2015), pp. 77–94. [Primary research chapter](https://library.slmath.org/books/Book63/files/131104-Fraenkel-2.pdf), §1 pp. 77–78 for Wythoff rules, greedy pairs, and the floor formulas; §5 for algorithms for generalized sequences. The activity reaches complementary sequences and computational questions; it does not reproduce that algorithm.

Undergraduate homes: impartial combinatorial games, induction on a decreasing state measure, invariants, binary arithmetic, addition over the two-element field. Historical research is solved mathematics; no claim is made that this classroom problem is currently open.

For pedagogy, re-read *Math Circle by the Bay*, preface printed pp. viii–x (PDF 9–11): common themes with varying depth, manipulatives, explanations, and reserve challenges. Also re-read Rozhkovskaya, Lesson 3 “At the lesson” (`part0013.xhtml`) for attempts before an organizing display; Lesson 7 (`part0017.xhtml`) for verifying legal-move understanding; and Lesson 8 (`part0018.xhtml`) for unequal copying pace. Our preprinted material, adult rotations, and particular task sequence are adaptations, not arrangements reported by those sources. See [lesson-format-source-notes.md](lesson-format-source-notes.md).

## Returning children and future branches

Lowell Handout 2 problem 2.3 and Handout 3 problems 3.1–3.3 (moves 1–3 and 1–5), and Week 7 are related through winning/losing positions. Here arbitrary removal from one pile, simultaneous multiple piles, and XOR are the new representation and argument. The old upper king variant remains an available reserve, and Wythoff moves from an old long-term reserve onto the optional extra. Record exact starts and whether Wythoff was actually attempted. Update the [use log](fall-k-5-year-a-use-log.md) after teaching, recording exactly which packet pages and instances each child encountered; prepared reserves stay untaught. Preserve an oral explanation as a brief adult note when writing is a barrier.

## Verification and outputs

Backward recursion, independent of XOR, checks 2,197 three-pile positions (each heap 0–12), 169 two-pile positions, and 961 Wythoff positions (0–30); sample moves are checked. Finite checks do not replace the general proofs.

Run `python3 lowell-math-circle-year-2/source/week-08/verify.py`, then `sh lowell-math-circle-year-2/source/week-08/build.sh`. Builds write five PDFs in `lowell-math-circle-year-2/combined/`; LaTeX is editable in the week folder. The [print index](../lowell-math-circle-year-2/source/week-08/README.md) and [review record](../lowell-math-circle-year-2/source/week-08/REVIEW.md) describe the delivered files and visual checks.
