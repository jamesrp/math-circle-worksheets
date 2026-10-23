# Week 99 (Moving piles): math check

Scope:
- `lowell-math-circle-year-2/week-99/week-99-grades-2-3.pdf`: 6 pages.
  - p. 1: the shared rules and the start/middle/target rule picture, then Problem 1: two pairs, 00 → 24 and 03 → 12.
  - p. 2: Problem 2: three pairs, 0005 → 1234, 1144 → 0225 and 2222 → 0134.
  - p. 3: Problem 3, the shortest-delivery rule, on 03 → 25 and 04 → 25.
  - p. 4: Problem 4: a fixed target of four counters at bin 2, with five blank start rows for least work 4 and 7.
  - p. 5: Problem 5: three-leaf star roads. Two pairs, then a blank pair for a three-counter invention with work 6.
  - p. 6: Problem 6, the work-5 partner game (landscape).
- `week-99-grades-4-5.pdf`: 6 pages.
  - p. 1: the same rules, then Problem 1, which repeats 2–3 Problem 2's first two pairs.
  - p. 2: Problem 2: 0055 → 2233, 1114 → 0235 and 0235 → 1144, each with "explain why no plan can use less".
  - p. 3: Problem 3: greedy on 03 → 25 and 04 → 35, including the tie question.
  - p. 4: the position-total example, then Problem 4: eight cards with total 8 on bins 0–4.
  - p. 5: Problem 5: stars, with a formula for every start and target.
  - p. 6: Problem 6, the triangle question, on three blank boards (landscape).
- `week-99-facilitator.pdf` (6 pp.), built from `guide/facilitator.tex` and `guide/solutions.tex`.

There is no K–1 packet. All three delivered PDFs are byte-identical to `source/week-99/reference-pdfs/`. Sources read: every `student/*.tex`, both guide `.tex` files, `README.md`, `QA.md`, `SOURCES.md` and `build.py`. I did not run or import the package's `check_math.py`. My scripts and their outputs are in this run folder, for `plans/review/checks/week-99/`. Checked October 23, 2026.

**Result: every printed pile, every least-work value, the greedy runs, the counts, the card catalogue, the star formula and the guide's theorems are correct in both bands. I found 2 problems, both minor. One is a garbled guide sentence about "different matchings" that never applies to a printed pair. The other is the rule picture's "target" panel, which shows a filled counter where every other target uses open circles.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures). It is written from scratch, with the printed data typed in from the pages; `check_diagrams.py` confirms that data against the PDFs.
  - **Least work.** Every value is a breadth-first search over pile states: one move takes one counter across one road, and counters are interchangeable. Three methods are computed separately and compared with it: the gap sum Σ|S_i|, the sorted matching, and a brute-force best assignment over all permutations.
  - **Problem 1 records.** The number of shortest move records (state sequences) for each pair, and the number of distinct optimal matchings once identical counters are identified.
  - **Problem 3.** Every outcome of "make the shortest remaining delivery" under every tie-break.
  - **2–3 Problem 4.** The least work to the 2222 target for all 126 four-counter starts.
  - **Stars.** Least work on the A–O–B–C star by BFS. The leaf-imbalance formula against BFS for all 4,877 equal-total pairs with 1–5 counters. Every three-counter pair, to find the maximum work and all work-6 pairs.
  - **2–3 Problem 6.** For each of the 126 targets, every start, plus a simulation of the guide's five one-direction steps.
  - **4–5 Problem 4.** All four-counter arrangements on bins 0–4 with total 8; the full 8 × 8 distance matrix on 5 bins and on 6 bins; and a prefix-count bound.
  - **4–5 Problem 6.** All 126³ = 2,000,376 ordered triples of four-counter arrangements on bins 0–5.
  - **Overview theorems.** BFS = Σ|S_i| = sorted matching for all 82,993 equal-mass pairs with 1–5 counters on 6 bins. The edge-cut sum against BFS on four trees: the star, a 2-2-1 spider, a caterpillar and a four-leaf star, each for 1–3 counters. The four-bin ring example.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 0 failures). It reads the delivered PDFs' vectors and words with PyMuPDF.
  - **Counters.** Each counter is assigned to the bin or node that contains it, as filled (start) or open (target place). Every counter's coordinates also match a `\draw … circle` in the TeX source for that page.
  - **Line boards.** The bin numbers printed under each bin read 0–5, or 0–4 on the cards. Bins are equal in size and evenly spaced, and every adjacent pair is joined by a connector.
  - **Rows and pairs.** Each row's label (start / target picture / A / B / C) is read, and the start-target pairs are rebuilt and compared with the typed data.
  - **Stars.** Each star has nodes A, O, B, C of equal radius, with roads O–A, O–B and O–C and no road between leaves.
  - **Rule picture.** The counter sits in bin 0, then 1, then 2.

The general facts I checked by hand, besides the code:
- **Gap bound.** The surplus left of gap i must leave across it, net.
- **Sorted pairing has no opposite traffic.** x ≤ i < x′ with y > i ≥ y′ reverses the order.
- **Star and tree cut formula.** Proved by decomposing the forced edge flows into surplus-to-deficit paths.
- **2–3 Problem 6 construction.** With one-direction steps, every S_i has one sign and ΣS_i equals the change in position total, 5.
- **2–3 Problem 5 work 6.** Each of 3 counters can cross at most two roads. So 6 is the maximum, reached exactly when the start and target have nobody at O and use different leaves (18 ordered pairs).

## Grades 2–3 (pp. 1–6): correct except item 2 (p. 1 rule picture)

- **P1.**
  - 00 → 24: least work 6, gaps (2, 2, 1, 1, 0), 9 shortest records.
  - 03 → 12: least work 2. There are exactly 2 shortest records, the two orders of 0→1 and 3→2. "Find two best move records… Changing the order of moves counts as different" is therefore just achievable, as intended.
- **P2.** Least work 7, 5 and 6. The sorted matching, the gap sum and BFS agree on each.
- **P3.**
  - 03 → 25: the rule makes 3→2 first (unique shortest, 1) and then 0→5, for 6; the optimum is 4, so another plan uses less.
  - 04 → 25: the rule makes 4→5 and then 0→2, for 3, which is optimal.
  - There are no ties in either pair, so "If deliveries tie, choose either" is harmless.
- **P4.** Least work to 2222 is the sum of distances to bin 2. There are 16 starts with work 4 and 19 with work 7, so five rows are easily filled.
- **P5.**
  - Pair 1: A2 C1 → O1 B2 needs 5, with leaf imbalances 2, 2, 1.
  - Pair 2: A2 B1 → A1 C2 needs 4, with imbalances 1, 1, 2.
  - A three-counter pair with work 6 exists; it is the maximum.
- **P6.** No target defeats work 5. Every one of the 126 targets has between 6 and 28 starts at exactly 5 (6 for 0000).

## Grades 4–5 (pp. 1–6): correct except item 2 (p. 1 rule picture)

- **P1.** The same pairs as 2–3 P2, with work 7 and 5: 112 and 60 shortest records, so two best records are easy to find.
- **P2.**
  - 0055 → 2233: work 8, gaps (2, 2, 0, −2, −2).
  - 1114 → 0235: work 5, gaps (−1, 2, 1, 0, 1).
  - 0235 → 1144: work 4, gaps (1, −1, 0, 1, −1).
  - The gap counts give the "no plan can use less" certificate for each.
- **P3.**
  - Pair 1 gives 6 against an optimum of 4, so the rule does not always give the least work.
  - Pair 2 (04 → 35) has a tie between 4→3 and 4→5 at cost 1. They lead to 6 and 4, so tied choices can change the result.
- **P4.**
  - The eight cards read 0044, 0134, 0224, 0233, 1124, 1133, 1223 and 2222. Each totals 8. They are exactly the eight such arrangements on bins 0–4, so none is missing.
  - The maximum distance is 8, reached only by 0044 and 2222.
  - The distances are the same on the six-bin mat.
- **P5.**
  - Pair 1 needs 5.
  - Pair 2, A3 B1 → A1 O1 C2, needs 5, with imbalances 2, 1, 2.
  - The sum of the leaf imbalances equals the least work for every equal-total start and target, as the last question intends.
- **P6.** No triple violates the triangle inequality. Of the 2,000,376 ordered triples, 323,724 give equality, 292,098 of them with three different arrangements, and the rest are strictly greater.

## Facilitator guide (6 pp.): correct except item 1

- **Overview (p. 1).** All correct, with their hypotheses stated: equal totals, unlimited capacity, unit gaps.
  - The model, and S_i as right crossings minus left.
  - The bound Σ_{i<m}|S_i|, and the proof that sorted matching attains it.
  - "Optimality, not uniqueness".
  - The 0,3 → 2,5 nearest-first example: 6 against 4.
  - Metric axioms, and the 0044/2222 equal-centre example at distance 8.
  - W1 = work/N.
  - The tree extension, and the remark that cycles need a different argument.
- **Launch (p. 2).** The A–D table, 1010 → 0101: work 2, record AB, CD. "A to C costs two even in one hand motion" is right.
- **Solutions table (p. 3).** All eight rows (start, target, signed gap row, work) match BFS and my gap rows, as does "Reading one proof", 3+2+1+0+1 = 7.
  - "Why the sorted plan attains all bounds" is right.
- **P3, P4 and the 2–3 P6 entries (p. 4).**
  - P3: greedy totals 6 vs 4; 3, optimal; and the tie giving 6 or 4. The other pairings, 4 and 7.
  - P4: the examples 0022, 1111, 0224 (work 4) and 0003, 0014, 0115 (work 7), and the counts 16 and 19.
  - 2–3 P6: the s / 20 − s argument and the one-direction construction.
- **4–5 P6 entry (p. 4).** The examples 4 + 4 = 8 and 20 + 16 > 4 are right.
- **4–5 P4 (p. 5).** The card labels A–H, the full distance matrix, "maximum 8, attained only by A and H", the 28 pairs, and the case proof that no card is missing are all right. So is the remark that gathering at 2 gives only 16.
- **Stars (p. 6).**
  - Work 5 with 2,2,1; work 4 with 1,1,2; the A3 → B3 invention with work 6; work 5 with 2,1,2.
  - The general star proof and the ring example: one road against three.

## Problems found

1. **Guide p. 3, "Different plans": a garbled sentence, and a claim that never applies to a printed pair.** Minor; guide only.
   - **Quoted:** "Some different matchings also tie. The requested “more than one” plan does not mean the optimum is unique after ignoring interchangeable-counter identities."
   - **Evidence** (`check_math.py`, "distinct optimal matchings"):
     - In every printed line pair of P1 and P2 in both bands, the optimal matching is unique once identical counters are identified. That is 00→24, 03→12, 0005→1234, 1144→0225, 2222→0134, 0055→2233, 1114→0235 and 0235→1144.
     - So "Some different matchings also tie" is true in general (e.g. 01 → 12 by 0→1, 1→2 or by 0→2 with the counter at 1 staying), but never on these pages.
     - The next sentence says the opposite of what the paragraph means. Asking for more than one plan would suggest non-uniqueness, and the paragraph goes on to say "Different assignments are not required". The point it needs is that the optimum need *not* be non-unique.
     - "more than one" is also not the printed wording; both packets say "two best move records".
   - **Consequence:** an adult may send a child looking for a second optimal assignment, which does not exist for any printed pair. The paragraph's last sentences ("Different legal orders suffice… Different assignments are not required") give the right instruction, so the risk is small.
   - **Smallest fix:** replace the two quoted sentences with:

     > "Asking for two best records does not mean there are two different matchings: in every printed pair the best matching is unique once identical counters are ignored, so the two records differ in move order. (Different matchings can tie elsewhere, e.g. 0,1 → 1,2.)"

2. **Both bands, p. 1, the rule picture: the panel labelled "target" holds a filled counter, while every target on the pages is drawn with open circles.** Minor; diagram label.
   - **Diagram:** three small three-bin boards, "start" (filled counter in the left bin) → "cost 1" → "middle" (filled counter in the middle bin) → "cost 1" → "target" (filled counter in the right bin).
   - **Evidence** (`check_diagrams.py`, "Rule diagram" and every row):
     - All 15 printed line-board target rows (8 in Grades 2–3, 7 in Grades 4–5) and all four printed star "target picture" boards mark target places with open circles. Start counters are always filled.
     - The rules never state this convention. The only picture before Problem 1 labels a filled counter "target", so the first example of the open-circle convention is Problem 1 itself.
     - The arithmetic of the picture is right: two crossings, cost 2.
   - **Smallest fix:** relabel the third panel "end" (or "done"). Or draw an open target circle in the right bin of the "start" panel, so the picture shows a counter arriving at an open target place.

## Notes (not errors)

- **4–5 P4, "Explain why no pair needs more".** The guide offers only the 28-pair comparison and calls the full maximum later depth. The week's own gap certificate gives a short explanation that children can check.
  - On these cards the number of counters in bins ≤ 0 and ≤ 1 is always 0–2, and in bins ≤ 2 and ≤ 3 always 2–4 (`check_math.py`, "prefix counts").
  - So at most 2 counters can need to cross any of the four gaps, and no pair needs more than 4 × 2 = 8.
  - The guide could add this as the hint for that question.
- The star roads are drawn with unequal lengths on paper: O–A and O–B are 0.97 in, O–C 0.78 in. The page's "One counter crossing one road costs 1" and the guide's "road length on paper is irrelevant" cover it.
