# Week 53: Cheapest connected networks

**Verdict: revise.** The mathematics and the problems are right. Two things need the reviser: two price labels on page 8 that sit on the wrong link, and a K–1 route that is one page long.

Reviewed October 5, 2026 by Claude. Packets: week-53-students.pdf, W53-networks-v1, 9 pages (pp. 1–4 Grades 2–5, Problems 1–4; pp. 5–9 Grades 4–5, Problems 5–9). Adult guide: week-53-facilitator.pdf, W53-guide-v1, 8 pages. Companions noticed but not reviewed: none exist. Status: unpiloted. Written October 4 under the 52–63 routing, which allowed shallow younger entries.

## The mathematics

Children pay counters for links until every place is connected, seeking the cheapest network. With positive prices, a cheapest network has no loop. A link uniquely cheapest across a split of the places is in every optimum, and a link uniquely dearest on a loop is in none. A loop-free network is cheapest exactly when no one-link swap improves it. Distinct prices give one optimum. This is minimum-spanning-tree theory, and a mathematician would enjoy it. P3 (the greedy trap), P5 and P8 (swaps), P6 (certificates), P7 (inverse design) and P9 (uniqueness) carry it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Real theorems, with positivity and ties built into the tasks: P6 has repeated prices and one optimum. |
| Problems | strong | The order carries the development: connect, cheapest, every optimum, trap, swaps, every/none, design, local-to-global, uniqueness. P2–P7 each give real work. P1 is short except for K–1. P4 repeats P2's answer shape. |
| Student pages | adequate | Header, footer and numbering are right. There is no slop and no method. The non-task visuals before P1 and P5 meet AGENTS.md. Faults: the p. 8 labels, record counts that give away P2 and P4, and the P6 heading. |
| Concreteness | strong | Counters pay and refund in an off-map tray, and a pawn tests reach. Guide p. 2 gives a short launch on a non-task map. Connection is checked by eye, which works on maps this small. |
| Correctness | adequate | Every answer checks ([week-53-math.md](week-53-math.md), and my own enumeration of P1–P6, P9 and both swap lists). I agree with all three math.md findings. The p. 8 diagram misprices CD and DE. |
| Adult guide | strong | Theorem-first overview with assumptions, limits and a band map. Experiments are kept apart from proofs. Complete keys with lower bounds in counters, proofs, kit counts, a pretest list. |
| Age fit, K–1 | weak | K–1 gets p. 1, "possibly p. 2". Guide p. 2 otherwise sends the parent to "an accepted prior concrete activity". P3–P4 show prices as numerals only. |
| Age fit, grades 2–3 | strong | Short prompts. Dots give way to numerals, and the cheapest totals are 3 to 7. The state is the marks on the map plus one pile. P3 and the P2/P4 catalogs are real optimization. |
| Age fit, grades 4–5 | strong | P5–P7 are concrete and checkable. P6 asks for reasons, and P8–P9 for general arguments, late where they belong. P8 asks three questions in about 60 words. |

## Keep

- p. 1: the rules, the dot-to-numeral bridge and the non-optimal X/Y/Z visual. P1: one optimum against two.
- P3: AB=1, BC=2, AC=3, CD=4, AD=5. The three cheapest links make a loop and leave D out.
- P2 and P4: complete tied catalogs, with "every" as the task.
- P5: the U/V/W demo. The left input has three cheaper swaps plus a cheaper-looking one (return AD, buy BC) that isolates D. The right input has none.
- P6: CD is forced by price although it is not a bridge. P7: open design with prices 1–4.
- P8: the stuck cost-8 tree beside the cost-14 tree, which has four legal improving swaps and five that disconnect.
- Guide: the overview, the lower-bound keys and the proof enactments.

## Fix

1. **must**, 4–5, p. 8, Problem 8 (the same map is on p. 6). CD's "2" and DE's "1" are printed on link CE, and their white boxes break the CE line. CE reads as 6, 2, 1, and the thick CD and DE carry no price. The costs (8, 14) and every swap depend on these two prices. On p. 6 it is recoverable, since CE has its 6. Fix in diagrams.py/networks.json and rebuild both pages. Move DE's label to the F side. Centre CD's label on CD, or move it toward D (fraction about 0.75, offset 0.2 cm). Put BD's "5" below BD, which clears circle C on p. 8 ([week-53-math.md](week-53-math.md) items 1–2).
2. **must**, K–1, guide p. 2 and student pp. 3–4. "Young pairs can stay with p. 1 … offer p. 2 orally only if they retain the choices." The K–1 table gets one page, a do-not-list item, though the action suits K–1 well. That they run out in 10–15 minutes is a prediction. Fix: put dots beside the numerals on P3 and P4 (six at most), head pp. 1–4 "Grades K–5", and route K–1 through pp. 1–4 in the guide. Children choose links; the adult reads and pays.
3. **should**, 2–5, pp. 2 and 4, Problems 2 and 4. Each prints exactly three record maps, and each has exactly three optima. A child stops at the third box, so the boxes give away that the list is complete (themes.md: "A visible '3 of 5' removes it"). Print four or five.
4. **should**, 4–5, p. 6, Problem 6. The question asks about links "in no cheapest purchase", but the answer area is headed "Cannot be bought:". Every link can be bought, and P8's lower tree has BD bought. Head the areas "In every cheapest purchase:" and "In no cheapest purchase:".
5. **could**, 2–5, P4: CE=2 makes the catalog 3 × 3 = 9 rather than repeating P2's three.
6. **could**, 4–5, P8: give the final general question its own problem.
7. **could**, guide pp. 2 and 8: move the spacing figures and the authorship and verification paragraphs to the source notes.
8. **could**, materials: name the bought-link marker object, or use only the sleeve trace.

## Overlaps

Week 52 (bracing) also reaches "a minimum connected set is a tree with n − 1 links", without prices. Week 13 uses cuts for max-flow; Weeks 21 and 50 minimize one trip. None has prices, ties, exchanges or cut/cycle certificates. Keep 52 and 53 separate; they can share the app's graph editor.

## App fit

Fit A, confirmed. Size S for buy-and-check, M with swaps and certificates. The child taps links to buy; the app keeps the pile and lights reached places. The solve: declare "cheapest"; the app answers a wrong claim with a cheaper network or an improving swap. Collect-every (P2, P4) needs a "done" declaration with no visible count. In swap mode (P5, P8), tapping an unused link shows its loop, and the child returns a loop link. Goals: fewest swaps to the optimum, or every improving swap. Certificates (P6): tap a split of the places to force a link, or a loop to exclude one. In design (P7), "exactly one cheapest" holds for 1956 of the 4096 price choices, so guessing wins. Use rarer targets, such as exactly 4 optima (144 of 4096), or a fixed multiset of prices. Pitfalls: a visible target price invites trial on maps with 8–55 trees, and plain "find the cheapest" is routine once Kruskal is known. Put the difficulty in ties, swaps, certificates and design, and never let drawn length hint at price. Draw on P2–P8. Leave P9's proof on paper.

## Classroom evidence

None reported. The packet is unpiloted, and themes.md lists only Weeks 1, 2 and 15 as taught.
