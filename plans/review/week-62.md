# Week 62: Conflict networks and scheduling

**Verdict: keep.** No must. Real colouring mathematics for Grades 2–5, every answer checks, and the guide is at the bar. The missing K–1 band is a should, because STAGE-ROUTING.md allows it.

Reviewed October 5, 2026 by Claude, reconciled from two independent card runs, with the math check in [week-62-math.md](week-62-math.md). Packets: week-62-students.pdf (W62-S-v1, 9 pp.; Problems 1–3 for Grades 2–5, Problems 4–9 for Grades 4–5). Adult guide: week-62-facilitator.pdf (W62-FAC-v1, 10 pp.). Companions noticed but not reviewed: none. Status: unpiloted.

## The mathematics

A schedule is a proper colouring of the conflict network. A group where every pair conflicts needs that many slots, but P3's five-cycle with a leaf has no such group above two and needs three. Two slots work exactly when there is no odd cycle (P4–P6, proved in the guide). First-fit is legal and uses at most one more slot than the most conflicts any card has, but a bad order wastes slots: three on P7's path, four on P8's tree, the smallest trees that can do it. P9 counts schedules with named slots. A mathematician would enjoy it, especially P6 and P8.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | The clique bound and its gap, the odd-cycle theorem with proof, first-fit against the optimum, colouring counts. |
| Problems | strong | Contrasts carry the ideas: K4 against K2,3 (six lines each, needing 4 and 2); a five-ring against a six-ring (P3); chord AD making an odd cycle in one network only (P4); a tree against an empty board (P6). |
| Student pages | adequate | Spec header and footer, no slop, 20 mm sites, a worked visual before each new convention. But the p. 9 visual prints a method (fix 2). |
| Concreteness | adequate | A wrong placement stays visible; the guide's checker traces every line, and its launch (p. 3) is right. But the lines are on the mat, the cards on the table, and the counters have no role (fix 1). |
| Correctness | strong | week-62-math.md finds no wrong answer in 18 networks; its scripts rerun unchanged, and both card runs' spot checks agree. |
| Adult guide | strong | Theorems first on p. 1, with hypotheses and a band map. Answers carry certificates, hints are held, and p. 6 separates experiment, conjecture and proof. |
| Age fit, K–1 | weak | No K–1 pages, by design. The guide offers p. 1 as an optional trial, with pattern-block mats as the fallback (fix 3). |
| Age fit, grades 2–3 | adequate | An adult reads; children match letters, count to eight and check pairs. On p. 2, "Show why fewer slots cannot work" needs only a line, a triangle or four linked cards. Only pp. 1–3 are printed (fix 4). |
| Age fit, grades 4–5 | strong | P4 and P7 are concrete starts, and P6 is concrete too. P5's converse, P8 and P9 come late, as continuations or return visits. |

## Keep

- The p. 1 visual and the guide's matching A–B–H launch with scheduler and checker.
- P2's K4 against A and B each joined to C, D and E; P3's two rings and its closing question; P4's chorded rings, after a cycle visual on an even square that gives away no parity.
- P6: six one-line answers on the tree, a triangle on the empty board, and added lines that clear other circles by at least 3 mm.
- P8, where a four-slot order must be planned backwards (D or H comes last), and "Could any order use five?"
- The guide's p. 1 overview and its P6 and P8 tables.

## Fix

1. **should**, guide pp. 2–3. The kit lists "Counters: 8 of each of 4 colors" for "the printed 20 mm sites", but no colour means a slot, and the launch only lets children handle them. Give headers 1–4 one colour each, let a counter of that colour mark a card's slot on its site, and show it in the launch; or drop the counters. Then a checker sees both ends of a line at once (prediction).
2. **should**, Grades 4–5, p. 9 visual: "place X in slot 1 → X 1, Y _ → two different schedules: X 1, Y 2 / X 1, Y 3". Fixing one card and branching is P9's method, which the guide holds back as hint 1. The visual never shows the swap the sentence above describes, and its "two" holds only for slots 1–3 (math check item 2 asks only for that caption). Show three schedules captioned "slots 1, 2, 3": X 1, Y 2; X 2, Y 1; X 1, Y 3. Rewrite the guide's p. 9 note to match.
3. **should**, K–1: no pages. [STAGE-ROUTING.md](../new-themes-52-63/STAGE-ROUTING.md) allows Grade 3–5-only themes, and the guide offers p. 1 as "a shallow trial entry", so this is not a must. But the mathematics has a genuine entry without reading, and otherwise the K–1 table spends the hour elsewhere. At minimum, extend its route to the p. 2 diamond and K4; better, add pages asking for the fewest colours on a path, a star, and rings of three, four and five.
4. **should**, Grades 2–3, guide pp. 2–3: "Core pp. 1–2; p. 3 if ready", and only pp. 1–3 are printed. A quick pair may finish with nothing next (prediction). Print pp. 6–7 for each third-grade pair and name the p. 6 tree and P7 as continuations.
5. **should**, guide p. 2. Making 56 cards with "a large fixed letter and a distinct simple picture" and 28 headers in "roughly 15–20 minutes" is optimistic (prediction). Supply a printable sheet of A–H cards and 1–4 headers, without pictures. Pencils won't mark the sleeves: add dry-erase markers.
6. **could**, p. 1: "Put every card in one slot" → "Put each card in exactly one slot" (math check item 1).
7. **could**, guide p. 1: "Swapping slot numbers gives a different assignment" fails for two empty slots, as guide p. 9 says; add "when a used slot is involved" (math check item 3).
8. **could**, P7 says "the rule" and P8 "the first-slot rule". Use one name.
9. **could**, P3: add "Largest group:" beside each "Fewest slots:", and room for the yes-or-no answer.

## Overlaps

The Week 33 bonus (P2–P3) and Week 35 bonus (P3) colour rings; the Week 14 return visit (P2) three-colours triangulation corners. Week 62 adds arbitrary networks, the clique gap, first-fit and added lines. Weeks 16 and 40 use other colouring rules. No merge.

## App fit

Fit A, size S, confirmed: two groups in Neighbor Lanterns. themes.md's "largely repeats" fits plain colouring only; first-fit orders and proofs that fewer can't work are new.

- **First-fit (P7, P8).** The child taps lanterns in turn and each drops into its first free colour, so the app enforces the rule and the child plans. Targets: exactly 3 on the path (a tutorial); exactly 4 on P8's tree, where only 630 of 40,320 orders work. For Hard, an eight-lantern crown graph (two rows of four, each joined to the other row except its partner) can take 4 where 2 suffice. "Could any order use five?" has a checkable reason: no lantern has four links.
- **Fewest colours with proof (P2–P4).** The child colours with the fewest colours, then taps mutually linked lanterns or an odd ring to show fewer can't work. Use K4, the diamond, K2,3 and P3's five-ring with a tail, which has no triangle; every minimum needs a tappable proof.
- **Later, in the graph editor:** P6, adding the fewest links so two colours fail.

Pitfalls: entering a whole order to run, or asking where a lantern will land, is prediction. A "fewest" first-fit target repeats plain colouring. Show no count of orders. Leave P9 on paper.

## Classroom evidence

None reported. The source README says "These adaptations are unpiloted"; the physical pretest on guide p. 2 hasn't been run.
