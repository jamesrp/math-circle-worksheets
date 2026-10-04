# Week 24 independent mathematics review

Reviewed October 4, 2026. No located mathematical defects. All three bands check out completely within the printed fair, independent, replacement-draw model. This report does not make a classroom-readiness claim.

## Independent evidence

The reviewer independently enumerated card pairs and deck partitions, without running or importing the author's checker. Results are saved in `critic-render/math-checks.json`. The actual generated K–1 TeX was parsed for its numeric card nodes: its first six values on each revised page give the original two decks, and its remaining eighteen values give each Cartesian-product pair once. Thus the pooled record is a complete nine-outcome result for each of A–B, B–C and C–A.

No cross-deck ties occur in K–1's printed cases. The unchanged older packets expressly prohibit a shared number between compared decks. Repeated cards are separate equally likely physical outcomes, so multiplicities remain in the denominators.

## K–1 verification coverage

Each problem occupies the same-numbered page.

| Problem | Asked outcome and independent check |
|---|---|
| 1 | Split and pool A–B comparisons; A wins 5 of 9, B wins 4. All nine printed pairs are present exactly once. |
| 2 | Split and pool B–C comparisons; B wins 5 of 9, C wins 4. All nine printed pairs are present exactly once. |
| 3 | Split and pool C–A comparisons and decide whether one deck beats both others; C wins 5 of 9, A wins 4. No strongest deck exists. All nine printed pairs are present exactly once. |
| 4 | Choose a deck with pairwise advantage against each fixed choice, then play six rounds. Choose C against A, A against B, B against C. None is guaranteed to win more actual rounds: every round still has positive losing probability. |
| 5 | Test replacements 3, 5, 7, 9 in (2,4,blank) against B. Directed wins are 3, 3, 4, 5 respectively; only 9 succeeds. |
| 6 | Find every single A–B swap reversing advantage. The five swaps are (A2,B1), (A4,B1), (A9,B1), (A9,B6), (A9,B8); B's new win counts are 5, 6, 9, 6, 5. All nine candidate swaps were enumerated. |
| 7 | Split six distinct cards into equal three-card decks with equal wins. Impossible: all nine comparisons are decisive and an odd total cannot divide equally. |
| 8 | Split cards 1–6 into three two-card decks with cyclic majority advantage. Impossible; all 90 labeled partitions were checked, and the general coordinatewise argument below applies. |

K–1 Problems 4–8 and all diagrams associated with them are unchanged in source. Rendered numeral/dot counts agree with the intended values.

## Grades 2–3 verification coverage

Each problem occupies the same-numbered page.

| Problem | Asked outcome and independent check |
|---|---|
| 1 | Compare the three original decks. A beats B, B beats C, C beats A, each 5:4; no strongest deck. |
| 2 | Infer certainty from a finite winner-only sequence. Impossible: either ordering of either original pair gives both winners positive probability, so every finite binary result string has positive probability under both orderings. |
| 3 | Keep maxima 9/8/7, distribute 1–6, and find two cycles different from Problem 1. Exhaustive checking finds exactly three arrangements: A=(1,5,9), B=(3,4,8), C=(2,6,7); A=(2,3,9), B=(1,6,8), C=(4,5,7); and the original. The first two are the required alternatives. |
| 4 | Test all five offered replacements in A=(2,blank,9). Directed A–B/B–C/C–A wins are 0→(4,5,6), 2→(5,5,6), 4→(5,5,5), 9→(7,5,3), 10→(7,5,3). Exactly 2 and 4 give the cycle. |
| 5 | Compare doubled six-card decks. Directed wins are 20/36 against 16/36 for the reverse relation. Winners do not change. |
| 6 | Build a distinct-card cycle with sums 15,18,21 using values 1–12. Independent search finds A=(3,5,7), B=(2,4,12), C=(1,9,11), with directed counts (5,5,6); all nine values are distinct and sums correct. |
| 7 | Build a two-card cycle using 1–6. None exists; the exact 90-partition search and general proof agree. |

## Grades 4–5 verification coverage

Each problem occupies the same-numbered page.

| Problem | Asked outcome and independent check |
|---|---|
| 1 | Count pairs and compare equal deck totals. Counts are (5,5,5), totals are all 15; equal totals do not settle the pairwise relation. |
| 2 | Find every cycle with maxima locked at 9/8/7. All 90 assignments of lower pairs were tested; precisely the three arrangements listed above succeed. Internal card order does not add arrangements. |
| 3 | Use numbers 1–6 with repeats allowed only within a deck. A=(1,4,4), B=(3,3,3), C=(2,2,5) is valid, with directed wins (6,6,5). Independent multiset enumeration found 30 labeled solutions; the task asks for one. |
| 4 | Compare six-card and four-card copies. Six-card directed probabilities are 20/36=5/9 throughout. Four-card A–B, B–C, C–A counts are 10/16, 7/16, 10/16 respectively; in particular the B–C winner reverses. Reverse probabilities complement these because there are no ties. |
| 5 | Compare the four displayed two-card pairs and formulate a rule. First-listed deck counts are 2,3,4,1 out of 4, giving A/B=2:2, C/D=3:1, E/F=4:0, G/H=1:3. A sorted two-card deck wins a strict majority exactly when both its sorted coordinates exceed the other's. |
| 6 | Decide whether one- and two-card cycles exist and find the smallest equal deck size. One-card comparison is transitive; the two-card rule is also transitive. Neither size permits a cycle. The original three-card example shows that three suffice. |
| 7 | Use 1–9 once each with every directed edge winning at least 6/9. Independent enumeration of all 1,680 labeled three-deck partitions finds no solution. Majority cycles occur, but at least one directed edge has only five wins. |

## General arguments and diagram checks

For sorted two-card decks a1≤a2 and b1≤b2 without cross-deck ties: if a1<b1, the smaller A card loses to both B cards, so A has at most two wins. If a2<b2, both A cards lose to B's larger card, with the same consequence. Conversely, a1>b1 and a2>b2 force the three wins (a1,b1), (a2,b1), (a2,b2). Coordinatewise strict inequalities are transitive, excluding a cycle for any allowed numbers, including repeated values within a deck.

There is also a short certificate for grades 4–5 Problem 7. Rotate the names around the proposed cycle so A contains the global largest card 9, and let a<b be A's other cards. If C beats A at least six times, no C card can beat 9, so every C card must beat both a and b. If A beats B at least six times, its lower two cards must contribute at least three wins beyond 9's three wins; consequently some B card is below a. That B card loses to every C card. If B beats C at least six times, the other two B cards must both exceed every C card, hence both exceed b. Then A's lower two cards beat only B's small card, contributing just two wins, and A beats B only five times. This contradicts the proposed six wins. It agrees with the independent full enumeration.

All delivered pages were rendered and inspected. Printed card values, multiplicities, labels and blank-card counts agree with the tasks. No diagram changes the computed model. The full-size original K–1 deck pictures remain unchanged; the newly supplied pairs are smaller recording illustrations rather than physical card templates.
