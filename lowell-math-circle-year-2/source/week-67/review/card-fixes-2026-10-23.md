# Week 67 card fixes, October 23, 2026

The review card is `plans/review/week-67.md` (verdict keep). This pass made its three shoulds and seven coulds. The student pages were converted to problem files first, with no wording change (a separate commit), and edited there afterwards. The packet is now GGT67-S-v2 (five pages, Problems 1–5) and the guide GGT67-FAC-v2 (three pages).

| Card item | Change |
|---|---|
| should 1 | Problem 5 has its own page 5 with two blank cube maps above its answer lines, so new homes need not go on Problem 4's coloured cubes. |
| should 2 | Guide "K–1 tables": an adult-led route on the existing pages (the launch example, Problem 1's left board with A and B only and then with C, Problem 3's tree), the adult reading, scribing and drawing, with a key in plain words. No K–1 pages. A prediction, unpiloted. |
| should 3 | Problem 4's right-hand homes are 000, 001 and 111 (distances 1, 3, 2); key 001, the home itself, which is not next to 111. Both old triples were the three neighbours of their meeting label. |
| could 4 | p. 4 no longer says "Each dot on these maps has a three-digit label." |
| could 5 | The P–M–Q example on p. 1 is drawn at the boards' 1.6 cm spacing. |
| could 6 | "Keep a drawing of your attempts." moved from Problem 2 to the guide's Problem 2 notes. |
| could 7 | Guide, after the Problem 3 key: two maps for a ready pair, two crossroads joined to A, B and C (two dots work) and a six-dot ring with alternate homes (none). |
| could 8 | Guide overview: the majority of three digits is their middle value, so the cube rule is the grid rule on a 2 × 2 × 2 grid; median graphs named. |
| could 9 | Guide launch: all six dots work for P and Q; two homes have many meeting dots, three on a full grid have one. |
| could 10 | Guide materials: counters about 1.2 cm across or smaller for the 1.6 cm (1.55 cm) dot spacing. |

Also: the guide's materials say five pages, its first route calls pages 4–5 the cube continuation, its headings no longer end a page, and the week's own checkers (`checks/independent_check.py`, `student/check_math.py`, `guide/check_math.py`, `checks/results.json`) use Problem 4's new homes.

Checks: `review/verify_card_fixes_2026_10_23.py` checks Problem 4's keys and routes, the majority rule on all 56 cube triples, the launch's six dots, the K–1 key, the two extra maps, the dot spacings, and the printed wording, numbering and footers (and the PDFs' page counts when given them). Page 3 of the packet changed only in its footer.

Nothing was physically rehearsed; the packet remains unpiloted.

## Critic follow-up, later on October 23, 2026 (guide v3)

An independent critic's could 13, made in the guide only: "Put a counter on every dot where the walk can stop and still be shortest" needs about ten counters, more than the three home counters and one meeting counter per pair, so the materials now say "a smaller meeting counter (about ten for a K–1 pair)"; and the K–1 key says "the junction two roads below C", because a plain dot sits between C and the junction (`verify_card_fixes_2026_10_23.py`: C is next to t, t next to the meeting vertex v). Guide GGT67-FAC-v3, still three pages; the student pages are unchanged. Checked by `plans/review/checks/week-67/check_critic_fixes.py` in the repository.
