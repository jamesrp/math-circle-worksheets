# Week 24: Nontransitive dice and decks

**Verdict: keep.** No must. Every band reaches the 5/9 cycle and then an impossibility it can show with cards, and every student answer checks. Fix 1, a guide sentence false for half of 4–5 Problem 4, is a should because no correct answer or complete argument would be marked wrong.

Reviewed October 5, 2026 by Claude in two independent reviews, reconciled, with the math check in [week-24-math.md](week-24-math.md). The reviews differed on three severities (fixes 4, 6 and 7). Count checks: `card_checks.py`, `best_cycle.py` and `reconcile_checks.py`. Packets: week-24-k-1.pdf (F24-K-v2, 8 pp., P1–8), week-24-grades-2-3.pdf (F24-23-v2, 7 pp., P1–7), week-24-grades-4-5.pdf (F24-45-v2, 7 pp., P1–7). Adult guide: week-24-facilitator.pdf (15 pp.: an unnumbered overview, printed pp. 1–13, a route page numbered 15). Companions noticed but not reviewed: week-24-bonus.pdf (W24-BON-v1, 4 pp.) and its guide (W24-BON-FAC-v1, 5 pp.), both correct per the math check. Status: unpiloted (source README; guide footers). The approved October 4 revision replaced K–1 P1–3's "Record every different pair" with printed pairs to share; the organizer approved its scope, not classroom use.

## The mathematics

A=(2,4,9), B=(1,6,8) and C=(3,5,7) each beat the next on 5 of 9 equally likely pairs, so "beats" goes in a circle though every deck totals 15. Copying every card equally keeps the chances; copying only the smallest values changes every one (4–5 P4). For equal decks with no shared values a cycle needs three cards: with two, a deck wins a majority exactly when each of its sorted cards beats the matching one, which is transitive. With 1–9, no cycle reaches 6/9 on all three arrows. A mathematician would enjoy it: nontransitive dice at their smallest size, with sharp bounds a child proves by pointing at cards. Every P1 carries the cycle; K–1 P7–8, 2–3 P7 and 4–5 P5–7 give the limits.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A paradox, its minimum size and a sharp bound, with honest hypotheses (no cross-deck ties, equally likely cards, equal sizes). |
| Problems | strong | The order builds from cycle to impossibility. Contrasts: 2–3 P4's five values; 4–5 P4's six- against four-card decks; 4–5 P5's 2–2, 3–1, 4–0, 1–3. 2–3 P3 asks for two arrangements; exactly two exist. K–1 P1–3 are short but form one pooled investigation. |
| Student pages | adequate | Header, footer, numbering right; no slop. Older bands at the catalog bar. K–1 P1 prints table management (fix 2); K–1 P4 is ambiguous (fix 3). |
| Concreteness | strong | The larger card wins by itself; constructions use single cards 1–9, so no value sits in two decks. Guide p. 1's launch handles cards, returns one draw, records one pair. Cards are not supplied (fix 4) but need no design. |
| Correctness | strong | No student error (math check; both reviews' enumerations agree). One false guide sentence (fix 1). |
| Adult guide | strong | Theorem-first overview with hypotheses and band map; keys with proofs; certificate (p. 9); held hints, routes. Fixes 1, 4–6, 8–10. |
| Age fit, K–1 | adequate | Adult reads; dot cards to 9; every pair pictured. P7 (nine is odd) and P8 (follow the deck holding 1) are object proofs. P4 will need re-explaining (prediction); P6 is late, with adult recording (guide p. 4). |
| Age fit, grades 2–3 | strong | Numbers to 12, sums to 21; cards hold the state. P2 is abstract but short. P6 has one solution among 119 assignments with those totals; few will finish (prediction), fine late. |
| Age fit, grades 4–5 | strong | A complete search (P2), exact chances with duplicates (P4), a two-way proof (P5), a minimum (P6), a bound (P7), all checkable with cards. |

## Keep

- The three equal-total decks, and 4–5 P1's "Do the three deck totals settle this question?"
- K–1: numeral-and-dot cards; the nine pictured pairs per comparison (P1–3), which enforce completeness; P5; P6's "Find every swap"; P7–8 with "or show why it cannot be done".
- 2–3: P2's "Could any fixed number of these results make you sure?"; P3's pinned 9, 8, 7; P4's menu 0, 2, 4, 9, 10 (every value from 0 to 10 not in B or C); P5; P6's totals rising against two arrows; P7.
- 4–5: P2's "explain why none are missing"; P4; the run P5, P6, P7.
- Guide: overview, launch, and the tables and proofs on pp. 3, 4, 9, 10 and 12.

## Fix

1. **should**, guide p. 10, 4–5 P4 gate: "Counting distinct printed number-pairs as equally likely gives the wrong answer." False for the six-card decks: each distinct pair has four physical copies, so nine pairs give 5/9 (math check finding 1). Not a must like Week 25's hint, which rejected a complete proof: the inference it warns against does fail on P4 (by distinct pairs every four-card chance stays 5/9, not 10/16, 7/16, 10/16), and the same page prints 20/36 = 5/9 and "Each original outcome has four physical versions". Use the math check's sentence: "…gives the wrong answer for the four-card decks (B over C would look like 5/9 instead of 7/16). It works for the six-card decks only because every card is copied equally."
2. **should**, K–1 p. 1, P1: "For each of Problems 1–3, split the pairs among you and circle all nine winners on one shared page." Dividing the work is the adult's job (guide pp. 2, 3, 15), and P2–P3 get their action only from this sentence. Begin P1, P2 and P3 with "Circle the winner in each pair." and cut P1's first sentence.
3. **should**, K–1 p. 4, P4: "For each of A, B, and C, choose a deck that wins more card pairs and play six rounds." It does not say what the deck must beat; after P3 it reads as one that beats everything. Use: "Your partner takes A. Choose a deck that wins more card pairs against it and play six rounds. Do the same for B and C. Must your chosen deck win more rounds?" The guide should say the eighteen counters record rounds.
4. **should**, guide p. 1: cards "indistinguishable by touch", the printed ones "not 4 x 6 cm cutting templates", yet "Before the session, 10-15 minutes" omits making 57 cards (27 originals, 27 spares, 10–12), dotted for K–1. Add a print-and-cut sheet or name index cards and paper bags, and restate the time. The first review rated this a could; it is a should because the omitted work falls on a parent volunteer, and not a must like Week 23's mat because numbered cards need no design.
5. **should**, K–1 footer; guide pp. 1 and 13. The current K–1 and the archived pre-revision one are both footed F24-K-v2; the guide says F24-K-v3. Set F24-K-v3 in `src/build_packets.py` (line 121), rebuild, refresh the reference PDF and source ZIP.
6. **could**, guide p. 7 ("the older review's 14,15,16 or 18,16,15 examples do not answer it") and p. 13 ("Final authority: final/k-1.pdf"; "PROMPT.md, review.md"): cut. The second review rated this a should; Week 23's card made the same residue a could, since it costs an adult a sentence.
7. **could**, 2–3 P2: the guide (p. 2) says it "uses short runs of draws" but not who hides the bags; add that an adult fills two bags secretly and announces only which bag won. The second review rated this a should; it is a could because P2 is answerable as printed from P1's losing pairs.
8. **could**, guide p. 3: K–1 P1's hint "later ask whether it has met all three B cards" predates the printed pairs.
9. **could**, guide: one title instead of three ("Nontransitive dice and fair decks", "Three random decks", "Nontransitive random decks"); number the route page 14.
10. **could**, guide p. 2: the plan runs 0–60 minutes; context.md allows 35–40 at tables.
11. **could**, 4–5 p. 1: the label A touches "question?".
12. **could**, K–1 P6: only the guide says to reset the decks after each swap.

## Overlaps

Week 42 lists the same ordered draw pairs but proves von Neumann's unbiasing; themes.md also puts Weeks 43–45, 60 and 63 on the shared case engine. None has nontransitivity, so no merge. The bonus's label bags (P4–5) are mixed strategies, near atlas AP-22.

## App fit

B, size M, confirmed (themes.md: "Deal 1–9 into three decks with a live win grid; goal a cycle, or the best cycle"). A child moves nine number cards among three decks; two-tap swaps, as `wireCups` does for cups, keep every state a legal deal. Each pair of decks gets a 3×3 win grid (`catalogHTML`, as cases.md proposes) and an arrow that lights at 5 of 9. Solves:

- **Make a cycle** from 1–9: 15 of 1,680 labelled deals (5 up to rotation). With 9, 8, 7 pinned, **find all three** with That's all (certificate: guide p. 9).
- **Find every**: K–1 P6's five swaps; 2–3 P4's values (2 and 4). K–1 P5's third card (only 9) is a warm-up.
- **Hard**: totals 15, 18, 21 (2–3 P6, one solution); repeated values (4–5 P3).
- **Strongest cycle.** All 15 cycles have weakest arrow exactly 5, so "best cycle" by weakest arrow is no goal. Two arrows at 6 is a real goal: (2,3,9), (1,7,8), (4,5,6) gives 5, 6, 6, unique up to rotation; three is impossible (4–5 P7).
- **Can't**: two-card decks from 1–6 (K–1 P8, 2–3 P7), certified by the deck holding 1 and its two lost pairs; an equal split (K–1 P7), since nine decisive pairs cannot split evenly. Mix possible and impossible sets so "can't" is no free guess.

Pitfalls: no "x of n" counters. The live grid counts, so random dragging can light three arrows; lean on pins, totals and find-every, or have K–1 tap each pair's winner first. K–1 P4, 2–3 P2 and the six-round game are predict-an-outcome: a no-goal draw playground at most. Draw on K–1 P1–3 and P5–8, 2–3 P3, P4, P6–7, and 4–5 P2, P3, P5–7.

## Classroom evidence

None reported; the theme is unpiloted. The source README says "The theme remains unpiloted and can span several meetings"; guide p. 13 says "This remains an unscheduled library slot until deliberately selected." Card making, bag draws and timing are unrehearsed.
