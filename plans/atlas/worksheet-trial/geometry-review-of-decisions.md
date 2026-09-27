# Independent design review: the four decision worksheets

Reviewer: geometry author, 25 September 2026. Scope: AP-23, AP-21, AP-01, AP-29; all twelve student pages and all thirty-six numbered prompts. I first read the student rules/prompts and independently solved the finite instances, then compared the solutions and figure data. I also inspected and ran `decisions-checks.py`; all assertions pass. This is a mathematical/design review, not a PDF layout review or classroom pilot.

**Result:** no incorrect mathematical answer found. One material rule clarification is required before release: AP-01 page 1 must specify a fair independent coin and restrict the chosen starts/guaranteed-win question to the interior positions 1, 2 and 3. As written at review time, “chosen start on 0–1–2–3–4” also permits 4, which immediately guarantees the prize; the key correctly discusses interior starts only. This was sent directly to the author for correction. No other design blocker found.

**Closure:** the author repaired the AP-01 launch and question in data, Markdown and renderer. I reread the revised JSON: it explicitly says a fair independent coin, starts 1/2/3, and “Can any of those starts guarantee a win?” This finding is closed. PDF layout remains separately reviewed.

## AP-23 — all prompts 23.1–23.9

Independently derived totals by QUICK crowd 0, 1, 2, 3 as 12, 9, 10, 15. The only strict-improvement crowd arrows are 0→1, 1→2, 3→2; crowd 2 alone is stable. For the explicit move, R changes 1→3, G changes 4→3, B stays 4: group total rises from 9 to 10 although G benefits. The reverse move from a stable state lowers the total but hurts its mover. Thus the requested distinction is real and not an artifact of a tie.

With STEADY changed to 3, both crowds 1 and 2 are strict-stable. The six named states have precisely the inclusion-cycle edges R↔RG↔G↔GB↔B↔RB↔R for equal-cost single-person moves. Totals alternate 7 and 9. The all-empty/all-full named states are excluded from the six-state display because their relevant moves are strict improvements, not ties. All figure rules and solutions agree.

This is a strong worksheet design: meaningful counter placement, a state compression children can explain, external cost, and a changed rule producing a genuine dynamics question. The supplied hexagonal vertex order makes the final tour easier but does not reveal which edges are legal; that is a defensible scaffold, not a supplied solution. Do not let the first page's tables crowd out the route mat.

## AP-21 — all prompts 21.1–21.9

Independently enumerated feasible choices in reasoning and checked them against the exact script. The unique best original plan is days 2, 4, 5: cost 5, reward 18. Chronological greedy gives days 1, 2, 4 and 15 points; reward-first gives days 3, 5 and 17. Histories X and Y have the same 3 remaining battery and best future reward 12, but final totals 17 and 18. This correctly distinguishes sufficient future state from total earned score.

The day-4 values for batteries 0–5 are 0, 4, 8, 12, 12, 12. The selected day-3 values at batteries 1, 3, 5 are 4, 12, 17. The day-2 values at 3 and 5 are 12 and 18, forcing day-1 value 18. The take/skip recurrences use the correct successor battery, so their upper-bound certificate is valid. With the last reward lowered to 3, exactly days 2, 3 and days 1, 2, 4 tie at 15. The three-case proof exhausts the possibilities; the changed day-4 row 0, 4, 4, 7, 7, 7 is correct.

Strongest aspect: equal future states arise before the backward method is introduced. This supports understanding instead of asking children to execute a table algorithm. Main risk is page 3 density: three earlier-state cards, two day-2 comparisons, one day-1 comparison, a path trace and a new optimization could consume too much physical worksheet space. The final changed-reward problem should be moved to a separate optional follow-up or facilitator prompt if necessary; preserve generous branch-record boxes and body type.

## AP-01 — all prompts 01.1–01.9

The independent first-step equations give prices 0, 1, 2, 3, 4 and probabilities 0, 1/4, 1/2, 3/4, 1. Equal adjacent gaps prove uniqueness; changing one height alone is appropriately not treated as a proof that coordinated changes are impossible. The reflected-path argument at start 2 preserves probability; the key correctly separates it from guaranteed winning and includes eventual absorption.

The ferry at 2 directly yields price 2, then prices 1 and 3 follow. All endpoint chances are unchanged. Ferry durations are at most two tosses, with expected counts (3/2, 1, 3/2), compared with (3, 4, 3) originally. The child-facing explanation uses only the first-toss values and does not need expected-duration theory. For the 0–6 design, the changed destinations must satisfy a+b=2i. New unordered choices are 2→{0,4}, 3→{0,6} or {1,5}, 4→{2,6}; no new longer pair exists at 1 or 5. The single-site modified chains still absorb, so the harmonic certificate has its intended interpretation.

The design is richer than simply simulating a random walk: price/height is a new representation, uniqueness supplies a certificate, and the ferry gives an unexpected preserved answer. Fractions and expectation reasoning are genuine gates, correctly stated. Fix the page-1 coin/interior-start rule as noted above. The first page intentionally introduces only a few trials; do not extend it into repetitive data collection.

## AP-29 — all prompts 29.1–29.9

Independently concatenated the baseline encoding to `0001001000011100` (16 bits), and the short code to `01001100101110` (14 bits). The bad proposed code genuinely has 010 = 0|10 = AC and 01|0 = BA. This is a real ambiguity in the complete supplied code, not the false generalization that every non-prefix code is ambiguous.

Suppressing unary nodes preserves the leaf/prefix property and strictly lowers total length for positive weights. Full four-leaf shapes have depths (2,2,2,2) or (1,2,3,3), since the root splits 2+2 or 1+3. The exchange argument then gives totals 16 and 14. With all counts 2 the totals are 16 and 18. A six-picture tie requires multiset (2,2,1,1), giving 12 for both shapes; the only alternative positive multiset (3,1,1,1) gives 11 versus 12. The example ABACBD has the intended counts. Unique greedy leaf decoding is valid for every concatenation.

This is a strong worksheet: communication failure motivates the tree constraint, children choose a code before seeing the optimal shape, and both optimality and a frequency reversal/tie extend the investigation. Root-only/tree-frame scaffolds leave the meaningful construction to the child. The four-leaf proof is satisfying without importing Huffman's algorithm or logarithms.

## Checks that remain at the PDF stage

- All twelve pages need actual visual inspection at readable size; no quality claim follows from JSON alone.
- Preserve usable route mats, branching boxes, tree drawing regions and empty skyline grids. Delayed hints must stay out of initial student pages.
- Keep vector picture symbols plus letter labels. Distinguish total costs from individual costs, and past score from future reward in every caption.
- Correct missing prose spaces during typesetting, without applying a global spacing regex to source URLs or mathematical identifiers.
- None of these designs has classroom pilot evidence. Their mathematical correctness is stronger evidence than the still-provisional claims about engagement and pacing.
