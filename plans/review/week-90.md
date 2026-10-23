# Week 90: Sliding number arrays (jeu de taquin)

**Verdict: keep.** No must: every card, example and key checks, every problem has its board, cards and pieces, and the guide opens with the theorem and its limits. The fixes are a teaser line, a question that answers itself, an undefined B catalog, and guide gaps.

Reviewed October 23, 2026 by Claude, with math.md. Packets: week-90-students.pdf (W90-students-v1, Grades 2–5, 8 pp., P1–P9), week-90-materials.pdf (W90-materials-v1, 11 pp.). Adult guide: week-90-facilitator.pdf (W90-FAC-v1, 9 pp.). Companions noticed but not reviewed: the band-view menu. Status: unpiloted; handling, resets and timing unrehearsed (README, QA.md). No K–1 packet, by design. I agree with both math.md findings, rating item 1 should and item 2 could.

## The mathematics

A slide opens an inner corner of an increasing skew filling and moves the smaller right or lower neighbour into the hole until it exits. It keeps every number and the order, and ends (P9). Sliding until no gray square remains gives the same labelled array whichever corner starts each slide: the first fundamental theorem of jeu de taquin, tested on all 6 D and 16 B starts (P3, P5) but not provable by children. D2 and D5 both finish 13/2, so a finish need not reveal its start (P6); a saved exit undoes a slide (P7); the larger rule breaks every A start (P8). A mathematician would enjoy it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Order independence on complete finite families, with provable side facts (P2, P6–P9). |
| Problems | adequate | P4 (a start for each outline), P6, P8 and P9 are real thinking. P1 is three two-move slides. P3 and P5 ask one question over 12 and 32 runs, split among pairs. |
| Student pages | adequate | Spec header and footer, rules once, a non-task worked visual before each procedure (pp. 1, 3, 7), 14 mm references beside 30 mm boards. Fixes 1–3. |
| Concreteness | adequate | Tiles, ring, masks and unchanged reset cards hold every state; a whole-group launch on the 2×2 board (guide p. 2). Only the partner polices "smaller". |
| Correctness | strong | math.md replays every card, example, target and table: 0 failures. Two guide slips (fixes 6, 8). |
| Adult guide | adequate | Theorem-first, with assumptions, limits, finite-versus-general evidence and a band map; full keys, counts, proofs, kit counts. Fixes 4–7. |
| Age fit, K–1 | weak | No route: "A separate familiar activity is appropriate for the K–1 table" (guide p. 2). |
| Age fit, grades 2–3 | adequate | The adult reads; comparing 1–5 is the only arithmetic. Four kinds of square plus resets is a lot; the guide's one-hole gate fits (prediction). |
| Age fit, grades 4–5 | strong | P2's 3 + 2 count, P4's search, P6's lost information and P9's three proofs suit this table. |

## Keep

- p. 1's worked example ("1 slides up", "3 slides left; cover exit"), the launch's non-task 2×2, which p. 7 reverses back to the exact start.
- p. 3's four frames: unchosen gray squares kept, stopping at "Open next corner" without solving a D card.
- Gray, dark and ring as distinct states; printed outside cells; 30 mm cells, 26 mm pieces; complete A, D, B cards.
- P1's A3 and A5 (same outline, different labels); P3's "the finished outline or the position of any number".
- P4 before the B catalog; P6's D collisions against B's distinct finishes; P8; P9's three claims.
- Guide: "This supplies evidence for, not a proof of, the universal theorem"; the 3 + 2 and 5 + 6 + 5 counts; "Why larger?"; "adults should not operate every move".

## Fix

1. **should**, p. 1, top line in larger type: "Slide tiles to close a missing corner. Which finished shapes can you make?" A teaser, not a task (neg.md). Delete it.
2. **should**, p. 2, P2: "Could an increasing start be missing from this collection? Explain why your collection is complete." The second sentence answers the first. Replace it with "Explain how you know."
3. **should**, p. 6, P6: "Use the B catalog to decide." No page defines it, and P5 sorts by outline, so the start cards cannot answer. Write "Use your finished B arrangements from Problem 5". On guide p. 6, say the pooled record is each B finish, saved as made.
4. **should**, guide p. 2: the first visit is "25–35 minutes with supplied one-hole boards"; several gray squares are "A later launch". A has five starts, so the 4–5 trio may finish P1–P2 early (prediction). Name P3, then P4, as its same-visit continuation, launched at the table from the p. 3 frames.
5. **should**, K–1, guide pp. 1–2: no route; a should, as on the Week 83 and 87 cards, since the choice is deliberate. Fix: the launch, P1 on the A board, and P2's sort of the five A cards into two piles; the parent reads, children compare 1–4 and slide (prediction).
6. **should**, guide p. 7 hint, "stop at S even if another neighboring label exists", and p. 1, "Boundary markers carry essential information." No label ever lies above or left of S (math.md item 1, all 37,320 slides), so the backward slide stops there itself; only E is essential. Use math.md's wording; hold "Which marker do you need?" as a 4–5 prompt for P7.
7. **should**, guide p. 1: the overview never says what children should discover. Add one sentence: corner order never changes these finishes; two D starts can share a finish, two B starts never do; a saved exit undoes a slide; the larger rule breaks order.
8. **could**, guide p. 4: "descending diagonal" → "the diagonal from top right to bottom left"; column head "labels, top right to bottom left" (math.md item 2).
9. **could**, p. 3: "Use the unchanged D card to reset…" belongs in the launch; p. 7's "Use the S and E markers…" repeats its rule.
10. **could**, P5: "Can you account for every increasing start" → "Could an increasing start be missing from the sixteen cards?"
11. **could**, guide p. 4 hints: two orders that differ mean a slip; replay both with the partner pointing.
12. **could**, p. 6: two targets show a dark exit and two do not; draw all four alike.

October 23, 2026: fixes 1–12 made in the problem files and the guide; see `source/week-90/editable/review/card-fixes-2026-10-23.md`.

## Overlaps

Weeks 11 (chip firing), 39 (road detours) and 98 (growing from seeds) also end the same in every order, with elementary proofs. Week 54 shares Young diagrams; Week 1's extension X3 counts standard tableaux. None slides a skew shape. No merge.

## App fit

No themes.md row. Proposed B, size M:

| 90 | Sliding number arrays | Slide the smaller neighbour into the hole; design starts for target outlines; find every start of a finish | Every corner order gives one finished tableau; starts can share a finish | No | B | Tap tiles into the hole (only the smaller moves); place 1–n to reach a target | M |

The screen enforces "smaller", removing paper's main risk. The solve is design: place 1–n on a skew board so sliding reaches a target outline (P4) or an exact finish; find two starts with one finish (P6's D); collect every start of a finish, declared done. On one board every finish of an outline has the same number of starts (D: 2, 2, 1, 1; B: 1 each, a Littlewood–Richardson coefficient). Unreachable outlines have no child-checkable "can't", so set reachable targets. Pitfalls: auto-played slides and "will the other corner change it?" are predict-an-outcome; no "3 of 5" counter. Draw on P1, P4, P6, P7 and P8.

## Classroom evidence

None reported. The README, QA.md and the guide say unpiloted and physically unrehearsed; the production critic and age-fit reviews are predictions.
