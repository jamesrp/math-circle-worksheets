# Week 98: Growing from a few seeds

**Verdict: keep.** No must: every answer and diagram checks, the pages meet spec, and the 4–5 sequence reaches a sharp lower bound with its proof. The fixes are a thin 2–3 P3 and P4 record, order independence missing from 4–5, an unclear materials list, two guide slips and no K–1 route.

Reviewed October 23, 2026 by Claude, with math.md and card_appfit*.py. Packets: week-98-grades-2-3.pdf (W98-23-v1, 5 pp., P1–P5); week-98-grades-4-5.pdf (W98-45-v1, 6 pp., P1–P6). Adult guide: week-98-facilitator.pdf (W98-FAC-v1, 5 pp.). Companions noticed but not reviewed: none. Status: unpiloted and physically unrehearsed (QA.md); not yet reviewed by the organizer. I agree with both math.md findings (fix 6).

## The mathematics

An empty square fills when two side-neighbours are filled. Every complete run from the same seeds ends in the same set, the least closed set containing them (2–3 P4). An addition touching k filled squares changes the exposed sides by 4 − 2k ≤ 0, so s seeds (at most 4s sides) fill an n × n board (4n sides) only if s ≥ n, and the diagonal uses n (4–5 P2–P5). A start can need every seed without being smallest: four on 3 × 3 against the three-seed diagonal (2–3 P5, 4–5 P6). A mathematician would enjoy the one-line monovariant meeting its construction.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Three theorems with stated hypotheses; the bound is sharp for every n. |
| Problems | adequate | 4–5 P1–P6 carry the development: catalog, conjecture, monovariant, proof, indispensable against fewest. 2–3 P1, P2, P5 are substantial; P3 half repeats P1, P4's record hides what varies, and 4–5 never meets order (fixes 2–4). |
| Student pages | strong | Spec header and footer, rules once, a non-task 2 × 3 worked visual, no slop or hints, 30 mm boards for counters, 10 mm records. Coulds 7–9. |
| Concreteness | adequate | Counters hold the state; "Your partner points to two filled neighbors before each addition" is printed and launched on a separate 2 × 3 board (guide p. 2). Nothing physical stops a one-neighbour addition (prediction). Fix 5. |
| Correctness | strong | No student error (math.md: every start and order on 3 × 3 and 4 × 4, searches to 5 × 5). Fix 6. |
| Adult guide | strong | Theorem-first overview with limits and band map; full keys, a first visit, hints. Fixes 2, 5, 6. |
| Age fit, K–1 | weak | No route, by design: "Plan a separate established activity for the K–1 table" (guide p. 2). Fix 1. |
| Age fit, grades 2–3 | strong | Counting to 16; short tasks after a seven-sentence rule paragraph an adult reads; seed colour and reset sketch keep track. |
| Age fit, grades 4–5 | strong | Explanations where they are the point (P1, P4, P5); P3's 10 × 10 asks for the general pattern. |

## Keep

- Both bands: p. 1's pointing check and 2 × 3 worked visual, repeated in the launch; P2's open "smallest number" with one 30 mm working board and three records.
- 2–3 P5 and 4–5 P6: the start (1,1), (1,2), (2,3), (3,3), its four printed deletions (6, 3, 3, 6) and "Is four the fewest…?", which P1's diagonal answers; 4–5's "Find a different four-seed start…".
- 4–5: P1's "How many different final numbers…"; P3's 10 × 10; P4's pictures for k = 2, 3, 4 with Before/After blanks; P5's "for every possible start".
- Guide: the overview, both proofs, "ask the checker to touch the two supporting squares", the rectangle limit.

## Fix

1. **should**, K–1, guide p. 2: "Plan a separate established activity for the K–1 table." Placing counters and checking two neighbours needs no reading. A should, as on the Week 54 and 60 cards: no K–1 packet is claimed. Fix: a K–1 paragraph: the launch; 2–3 P1, the parent reading the rule as one sentence; P2 with counters, the parent recording; P5's deletions, one per child. That K–1 sustains this is a prediction.
2. **should**, 4–5, guide pp. 3–4. The overview's first theorem, "Every completed order has the same finish", is never asked in 4–5, though P1's "final numbers" presumes it, and p. 3 gives 2–3 adults only the closed-set proof. Fix: on p. 4, have the 4–5 adult ask 2–3 P4's question with diagonal seeds before P1. On p. 3 add: "Every square one run adds has two filled neighbours from earlier in that run. Another run that has them all cannot stop until it adds that square too."
3. **should**, 2–3 p. 4, P4: First/Second finish boards record only finishes, so a child draws one picture twice and the orders leave no trace. Fix: add "Number the added squares in the order you add them."
4. **should**, 2–3 p. 3, P3: the 9 and a stuck finish repeat P1, and the task ends at hitting targets. Fix: append "Can three seeds finish with any other number of filled squares?" (no: only 3, 4, 6 and 9 occur, math.md); key it on guide p. 3.
5. **should**, guide p. 2, "Per pair": "a reusable 4 × 4 board with approximately 30 mm cells, and a removable 3 × 3 mask", 15–20 minutes to prepare. The packets already print 30 mm boards (2–3 pp. 1–4; 4–5 pp. 1, 2, 6), and nothing explains the mask, so a volunteer cannot tell what to make. Fix: name the printed boards as workboards, drop the mask, ask for two counter colours, re-estimate preparation; update catalog/weeks/week-98.toml's materials.
6. **should**, guide pp. 1, 4 (math.md items 1–2): p. 1 defines closed by "no outside cell" right after "there are no outside cells", and its "therefore" gives the wrong reason; p. 4's "A third seed on that line gives 3" cannot occur. Fix: math.md's wording; state the (row, column) convention on p. 1.
7. **could**, both bands p. 1: cut "Opposite edges do not meet;", which a child cannot act on.
8. **could**, 2–3 p. 5: the start board (18 mm cells) is smaller than its deletion boards (20 mm); print it at 30 mm, as 4–5 P6 does.
9. **could**, 4–5 P1: two boards for four finishes; add two.
10. **could**, guide p. 2: "Introduce perimeter sticks then, rather than prescribing a proof" contradicts 4–5 P4; say it is for 2–3.
11. **could**, 4–5 P3: one 7 mm 10 × 10 board, so a failed pencil try must be erased; add a spare.
12. **could**, guide p. 5: cut release residue ("The paper's historical open questions are not represented as current.").

## Overlaps

Week 26 counts exposed sides of tile shapes; here they certify a process. Week 11's chip firing has an order-independent finish. Week 19 separates "no card can be added" from "largest", as "no seed can be removed" differs from "fewest" here. None has threshold growth or the seed bound. No merge.

## App fit

Not in themes.md. I propose Fit B, size M: a family on the shared square grid (sq-grid.md), beside Garden fences, whose rails can show the certificate. The child plants seeds from a tray, then taps squares to grow; the app accepts only a square with two filled side-neighbours and lights them. Solves:

- Fill the plot within a seed budget: n × n, then rectangles, rocks and L-shapes, with minima from the validator's search (math.md checked ⌈(a + b)/2⌉ only to 4 × 5). A wrong "Fewest" gets "Fewer seeds can do it." The "can't" certificate is a live fence count that growth never raises: s seeds give at most 4s; a full n × n needs 4n.
- Every seed needed: a filling start whose one-seed deletions all fail, which the app runs. Hard: the most such seeds, 4 on 3 × 3, 5 on 4 × 4 (none larger) and at least 7 on 5 × 5 (none with 8) (card_appfit outputs).
- Every finish: three seeds on 3 × 3 make 3, 4, 6 and 9, then "That's all".

Pitfalls: 14 of 84 three-seed starts fill 3 × 3, so random taps work there (130 of 1,820 on 4 × 4). After the diagonal every square board is alike, so vary plots. No predict-the-finish; order independence is a playground. No answer slots. Draw on 2–3 P1, P2, P5 and 4–5 P1, P3, P6.

## Classroom evidence

None reported. Source README and QA.md: unpiloted; the catalog record lists no uses.
