# Week 99: Moving piles

**Verdict: keep.** No must. Every answer checks, the pages follow spec, and the gap certificate, greedy failure, star rule and triangle rule reach children through tasks. The shoulds are an unprinted mat, copying in P1, a garbled guide paragraph, one page sentence and no K–1 route.

Reviewed October 23, 2026 by Claude, with math.md and card_checks.py. Packets: week-99-grades-2-3.pdf (W99-23-v1, 6 pp., P1–P6) and week-99-grades-4-5.pdf (W99-45-v1, 6 pp., P1–P6). Adult guide: week-99-facilitator.pdf (W99-FAC-v1, 6 pp.). Companions noticed but not reviewed: none. Status: unpiloted and physically unrehearsed (QA.md); the organizer approved the topic on October 17, not the worksheets. I agree with both math.md findings, as a should and a could.

## The mathematics

A move carries one counter across one gap between bins. Each gap's net traffic is forced, so the gap counts bound every plan, and matching counters in order attains the bound (P1–P2). Nearest-first can fail, and ties matter (P3). Least work is a distance: equal position totals can be 8 apart (4–5 P4), and it obeys the triangle rule (4–5 P6). On a star each road's imbalance must cross it (P5). A mathematician would enjoy it: optimal transport, with a lower bound met by a plan.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A real theorem with certificates on both sides, plus metric and tree extensions. |
| Problems | adequate | Most give five minutes and the order carries the development; 2–3 P4 and P6 invert the question. P1's second record is copying (fix 2); 4–5 P3 is two quick cases. |
| Student pages | adequate | Spec header and footer, rules once with a cost picture, no slop. Fixes 2, 4, 6. |
| Concreteness | adequate | Every physical move is legal, so only the count can go wrong, and the record and a checking partner catch it. Printed targets stay fixed. Whole-group launch, guide p. 2. No printed mat (fix 1). |
| Correctness | strong | Every pile, least work, greedy run, count, card and formula checks (math.md). |
| Adult guide | adequate | Theorem-first overview with hypotheses, a non-task launch, keys with gap rows, proofs. Fixes 1, 3, 5. |
| Age fit, K–1 | weak | No route, by design: "Use an established separate K–1 activity" (guide p. 2). |
| Age fit, grades 2–3 | strong | Small sums, an adult reads P3, one record, and P6's "Can a target make this impossible?" comes last. |
| Age fit, grades 4–5 | strong | Certificates, cards, a star rule, the triangle question; pooling keeps P4's 28 pairs light. |

## Keep

- p. 1 rules and cost picture; open-circle target rows apart from the start row.
- 2–3 P2's three contrasting pairs; 4–5 P2's "Explain why no plan can use less."
- P3's 03 → 25 (6 against 4), with 2–3's 04 → 25 success and 4–5's 04 → 35 tie.
- 2–3 P4's fixed 2222 target (16 starts at work 4, 19 at 7) and the exactly-5 game.
- P5 stars, 2–3's work-6 invention (the maximum) and 4–5's "Does it work for every start and target".
- 4–5 P4's eight cut cards, exactly the complete set, with the position-total example above.
- Guide: the overview, the A–D launch, the p. 3 table, the s / 20 − s argument, the star proof.

## Fix

1. **should**, both bands, guide p. 2: "A six-bin line mat with bins about 35 mm apart … a fixed target/reset card and one move-record strip" and "Provide a three-leaf star board". Nothing prints either, though QA.md says "The guide supplies a full-size reusable mat". Other line bins are 20.8 × 14.5 mm or smaller, star circles 15.7 mm; only p. 6 spaces bins 35 mm apart. Both P6s ("Check it, then swap"; equal and different triples) have one set of rows. Fix: print two extra copies of p. 6 per pair, as mat and later rounds, printed target rows as target cards, 2 cm counters stacked; add a star page with 35 mm circles; correct QA.md.
2. **should**, both bands, P1: "Find two best move records for each pair. Changing the order of moves counts as different." Every printed best matching is unique (math.md), so the second record is the first reordered: copying. Fix: delete both sentences and each pair's second record line.
3. **should**, guide p. 3: "The requested “more than one” plan does not mean the optimum is unique…" says the reverse of its intent (math.md item 1). Fix: "Different orders of the same moves give the same work. In every printed pair the best matching is unique once identical counters are ignored." Drop the paragraph's two-record sentences if fix 2 is made.
4. **should**, 4–5 P5: "Make a start and target with four counters each to test your way." It says what the blank boards are for and suggests a method (neg.md). Fix: delete it.
5. **should**, K–1, guide p. 2. Fix: a route on the p. 6 mat with two or three counters: 2–3 P1's pairs ("Make it match. Can you use fewer moves?"), two counters gathered at bin 2, and the game at work 3. That K–1 manages it is a prediction.
6. **could**, p. 1 picture: the panel labelled "target" holds a filled counter (math.md item 2); relabel it "end".
7. **could**, p. 1: "Keep one record of your moves at a time" reads oddly; "Write each move as you make it."
8. **could**, P3: "takes one counter that has not yet been delivered all the way to one target place" garden-paths; "carries one counter straight to an unfilled target place".
9. **could**, 2–3 P3: "If deliveries tie, choose either." Neither pair ties.
10. **could**, guide p. 2: the launch record "AB, CD" uses letters; the pages number bins.
11. **could**, guide p. 5: add math.md's prefix-count reason that no 4–5 P4 pair exceeds 8.
12. **could**, 4–5 P2: end "Find a way to know the least work before moving", as P5 does.
13. **could**, 4–5 P3: ask for a pair where the rule wastes the most; 0,2,4 → 1,3,5 wastes 4 with unlucky ties (card_checks.py).
14. **could**, guide p. 2: name each band's first-visit problems.

Fixed October 23, 2026: shoulds 1–5 and coulds 6–11 and 14, in the problem files, the guide and a new week-99-materials.pdf (W99-23-v2, W99-45-v2, W99-FAC-v2, W99-MAT-v1); coulds 12 and 13 deferred.

## Overlaps

Week 2's return visit (exchanges on a line) is a capacity-one relative. Week 13 shares the two-sided certificate, Week 53 the cut, Week 47 the dual (landscapes), Week 89 the prefix sums, Week 100 the triangle rule. No merge.

## App fit

Not in themes.md. I propose Fit A, size S: | 99 | Moving piles | Move counters one bin at a time to a fixed target; least work; design starts; stars | Forced gap traffic, met by matching in order; nearest-first fails; tree roads carry their imbalance | No | A | Tap a pile, then a neighbour; meet the budget; design a start at exactly k; rings for Hard | S |

Use the shared graph board. Solves: reach the target within the least-work budget; design a start at exactly k (2–3 P4, P6); build two total-8 arrangements on bins 0–4 as far apart as possible (Best is 8, only 0044 against 2222). After a solve, each road's forced count shows why it is best. Hard: a six-bin ring, where 0000 → 1245 costs 6, not the line's 12, and one cut per road no longer decides it (card_checks.py).

Pitfalls: a drag costs its length; no counter labels, live gap counts or predict-the-work puzzles. Once matching in order is found, line puzzles repeat; keep them few. Draw on P2, P3, 2–3 P4, P5 and 2–3 P6. 4–5 P6 and "Can a target make this impossible?" are claims about every case and stay on paper.

## Classroom evidence

None reported. Source README: "Unpiloted; printing, preparation, material handling, adult procedures and timing have not been physically rehearsed."
