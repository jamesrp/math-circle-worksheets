# Week 07 return visit: critic review

Reviewed `draft/return-visit.pdf` (three US Letter pages), its LaTeX source, builder, game-check source, and writer notes. Read `PROMPT.md` and `CRITIC.md`. The outline's explicit scope overrides the generic harness: one shared PDF, three consecutively numbered investigations, genuine page-level bands. I independently rendered and visually inspected **all three pages** at 108 dpi; the review renders are in `critic-renders/`.

## Verdict and revision priorities

This is a strong, compact draft. All three kernels have substantial investigations, the materials carry the game state, the procedural examples precede first use, and the page format is clean. I found no mathematical error in any displayed starting position and no clipping or overlap. Do not expand it into three packets or a full-hour sequence.

**One small essential-rule correction is recommended before release:** make the PASS card's one-use condition explicit in the page 1 rules. The current rule says either player may use the shared card and must turn it face down afterward, but never directly says that a face-down card cannot be used again. The intended restriction is inferable from “used,” yet it is precisely the rule the partner referee must enforce. This matters mathematically: unlimited passes would permit endless play and destroy the finite-game classification. A short replacement such as “Either player may turn the face-up PASS card face down instead of taking counters” specifies both availability and the physical action without adding a sentence. Retain the immediate last-counter win.

Two optional clarity improvements, with no redesign required:

- On page 2, “No face-up LAST card means there is no previous move” would match the actual three-card setup more precisely than “No LAST card.” The present wording is understandable if the unused cards are put aside; this is a small setup ambiguity, not an incorrect game.
- Problems 1 and 2 immediately ask for classification, while Problem 3 explicitly asks children to play. Consider putting the verb “play” into the former tasks so the first action is as concrete as the third page. The diagrams and supplied materials already make the intended play recoverable, so this is not a blocker. Avoid adding a sequence of tests or a prescribed classification method.

## Page-by-page review

| Page / problem | Substance and independent choices | Rules, worked example, and diagram use | Result |
|---|---|---|---|
| 1 / Problem 1 / Grades 2–5 | Twenty-four contrasting starting states: piles 1–12 with PASS available and used. The question targets a change in the winner rather than merely a list of game results. Children choose first moves, replies, trial order, and how to make a guarantee; no strategy is printed. The pile 1 exception and changes at neighboring sizes are present naturally. | The non-task 14-counter example shows input, the act of turning the card, and output with the same 14 counters. Labels and arrows have clear roles. The two large, readable lists provide one light record rather than concurrent move tallies. Clarify one-use availability as above. | Substantial and suitable for the indicated band. Revise one rule phrase. |
| 2 / Problem 2 / Grades 4–5 | Thirty-two states distinguish pile size from previous move. The columns include the important 1-counter/LAST 1 state, where inability to move loses with a counter still present. Eight pile sizes give two full blocks of four for conjecturing a pattern. Asking for a larger-pile rule adds a real continuation without printing modular arithmetic or recurrence instructions. | Input: 13 counters/LAST 1. Intermediate: two visibly crossed-out counters while the old card is still shown. Output: 11 counters/LAST 2. Both state changes are explicit, and 13 is outside the task range. The table is an intelligible state chart; circles are the only required record, with two lines below for a rule. | Clear, mathematically substantial, and appropriately placed at the older readiness level. |
| 3 / Problem 3 / Grades K–5 | Six starts support partner play, counterexamples, and guaranteed strategies. A (one row of 4) versus B (two rows of 2) changes the winner with the same total count. Rows 3, 5, 6, and 9 supply varied short and longer games. Children retain the choice of pair and strategy; the central-pair or mirror response is not supplied. | The non-task seven-square example removes squares 2 and 3 and leaves the gap in place, explicitly bridging the physical move to the resulting split position. All six active boards are large enough for the stated counters. B's bracket visibly groups both rows into one start; its separate rows cannot be mistaken for neighboring squares. A–F labels are close and unambiguous. | A genuine concrete young-child entry with deeper work available to older children. |

Problem 3's “make sure” classification is more demanding than playing a few rounds. That is appropriate mathematical depth, and the stated adult can read and discuss it. Whether younger children can distinguish an observed win from a guarantee is an **unpiloted classroom hypothesis**, not evidence that the page needs an easier task. Likewise, F is an appropriate later continuation; completing every start is not a prerequisite for successful use.

## Mathematical verification

I independently checked the games with a separate bottom-up state calculation for PASS/LAST and exhaustive recursion on surviving run tuples for adjacent pairs. This agrees with the writer's computed answers:

- **PASS available, winning piles 1–12:** 1, 2, 3, 5, 6, 8, 9, 11, 12. **PASS used:** 1, 2, 4, 5, 7, 8, 10, 11. The changed winner occurs at 3, 4, 6, 7, 9, 10, 12. A terminal empty pile was not allowed to pass. The indicated losing-state formulas also agree through 30; that finite check is supporting evidence, not a proof of the infinite formula.
- **LAST, winning piles 1–8:** no previous move = 1, 2, 3, 5, 6, 7; LAST 1 = 2, 3, 6, 7; LAST 2 = 1, 2, 3, 5, 6, 7; LAST 3 = 1, 2, 5, 6. Legal takes obey both the pile bound and the LAST exclusion. The residue formulas agree through 30. The student's larger-pile rule remains a conjecture until explained; the page does not overclaim a theorem from experiments.
- **Adjacent pairs:** A, D, E win; B, C, F lose. Every legal adjacent removal was included, and the successors preserve all surviving runs. Single rows 1–12 lose exactly at 1, 5, 9, consistent with the outline. The page does not assert a general period or introduce a false analogy with unrestricted Nim.

The three investigations are distinct from ordinary subtraction: shared resource availability, remembered move, and split geometry. No binary Nim prerequisite is introduced. The single physical card or visible gap supplies the memory that caused trouble in the reported lamp session.

## Print and format inspection

- Correct single-line week/topic/band headers, consistent footer ID `F07-RV-v1`, and pages 1–3. Problems are numbered 1, 2, 3. No Name/Date fields, duplicate titles, bonus labels, encouragement, facilitator hints, or automatic explanation prompts.
- Rules occur once for each distinct game. The two classification lists and the LAST-card table use necessary diagram labels, not extraneous section headings.
- All three procedural examples have a non-task input, meaningful intermediate action, and output with matching visual objects. They illustrate legal mechanics without revealing a winning move for a task start.
- PDF vector measurements confirm **31 active squares**, each approximately **57.601 × 57.601 points = 0.80 × 0.80 inches**, with equal axis scaling. Their horizontal span is 39.600–565.209 points on a 612-point page. The lowest active board ends at 705.608 points, above the footer. No extracted text block falls outside the page.
- The example's 0.20-inch squares are clearly small procedure diagrams; the active mats are 0.80-inch squares. The latter have the required nominal 0.05-inch clearance for counters at most 0.75 inches in diameter. Physical printing and counter fit have **not** been rehearsed by this review.
- All pages are legible and uncrowded. Page 1 has generous unused lower space, which is harmless in this three-page companion. The return-visit scope explicitly overrides the harness's generic four-pages-per-band advice.

No draft files were edited. This is a student-page critique only; it does not assess a facilitator guide or supply evidence of classroom piloting.
