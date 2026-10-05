# Week 30 (two-pan weight kits): math check

Scope: everything current in `lowell-math-circle-year-2/week-30/`, archive folders excluded:

- `week-30-k-1.pdf` (F30-K-v2, 5 pp., P1–P5)
- `week-30-grades-2-3.pdf` (F30-23-v2, 5 pp., P1–P6)
- `week-30-grades-4-5.pdf` (F30-45-v2, 5 pp., P1–P7)
- `week-30-facilitator.pdf` (5 pp.: overview, keys for all three bands, extension and source on pp. 1–4, route note on p. 5)
- The bonus companion `week-30-bonus.pdf` (W30-BON-v1, 4 pp., P1–P7) and its guide `week-30-bonus-facilitator.pdf` (W30-BON-FAC-v1, 5 pp.)

Sources read: `source/week-30/editable/student-src/make_packets.py` and `draw.py` (card, board and strip geometry). I also read the base guide's `guide.json` and the bonus `guide-src/guide.json`, but only to find where the fixes go. The delivered PDFs are byte-identical to the reference copies in both source folders. I did not use the packet's own `check_math.py`, `checks.json`, `independent-check.py` or its review notes. Checked October 5, 2026.

**Result: every answer in every student band, the bonus included, is correct. Every "find all" count matches the page, and every printed board can be filled as the problem intends. The base adult guide is correct throughout. I found three minor problems: a dot that sits on the card border on one K–1 weight card, and two wording slips in the bonus guide. None of them changes an answer.**

Convention used throughout, from the shared rules: the target stays on the left pan, and each weight goes beside it, opposite it or off. Target t balances exactly when t = Σ cᵢwᵢ with cᵢ ∈ {−1, 0, +1}, where +1 means opposite the target.

## How it was checked

My scripts and their saved outputs are in this folder. Each script finds the repository from its own location: four folders up when it sits in `plans/review/checks/week-30/`, otherwise by walking up. Run `extract.py` first; `check_students.py` runs it itself if `extracted.json` is missing.

- `common.py`: enumeration of all 3^m placements of a kit, reachable targets, every way to balance a target, and run length.
- `extract.py` → `extracted.json`, `extract.out`: reads every diagram back out of the vector drawings in the three base student PDFs. For each weight card it records the printed number, the dot count and the dot's gap to the border. For each board it records the printed target, the weight disks drawn in each pan, both pans and the "=". It also records the target strips, the kit labels and the ruled lines, each assigned to its problem.
- `check_students.py` → `check_students.out`: solves every base problem from the extracted data. It checks that each card's dots match its number, that the launch board balances, and that every board target and strip range fits its problem. Searches: every third weight from 1 to 199 for 2–3 P2; every two-weight kit below 60 for 4–5 P1; every three-weight kit up to 60 (with and without repeated weights) for the 13-target bound; and a pruned search of all five-weight kits that reach 121.
- `check_guide.py` → `check_guide.out`: reads the guide text from the PDF. It parses the small-kit key, the K–1 P1 and P4 lists and the 13-row Grades 2–3 balance table, and checks every row. It checks the overview theorems (balanced ternary for m ≤ 7, and the counting bound by exhaustive search for m ≤ 4) and the "why powers of three" step for S = 1, 4, 13, 40. It also checks every proof inequality, the one-sided extension and the route-note references.
- `check_bonus.py` → `check_bonus.out`: reads the P1 table, card strips, search example, P6 kits and their tray counts from the bonus PDF. It checks robust kits over all triples (1–8, up to 60, and up to 60 with equal values allowed) and all pairs up to 200. It finds the fewest comparisons for every candidate set by a minimax search over all whole-number thresholds, and it enumerates every equal-team partition.

All four scripts end with 0 FAIL lines. `check_students.out` has one WARN line, which is problem 1 below. `scratch/` holds my page renders and text dumps; it is not a script output and need not be committed.

## Diagrams (all bands)

- **Weight cards:** all 25 cards have exactly as many dots as their number.
- **Boards:** every one of the 27 boards has two equal pans (223.9 × 87.9 pt), an "=" and a target label. The weight disks are true circles (45.4 × 45.4 pt).
- **Launch example (all three bands):** target 3 with disk 1 on the left and disk 4 on the right, so 3 + 1 = 4.
- **Strips and kit labels:** each matches its problem's range (1–5, 1–6, 5–13, 1–13, 1–15, and 1–6 three times).
- **One drawing fault:** the tenth dot on the K–1 "10" card (problem 1).

## K–1: checks out mathematically (one diagram item, problem 1)

- **P1:** weights 1 and 3 balance 1 = 1, 2 + 1 = 3, 3 = 3 and 4 = 1 + 3. The boards for 2 and 4 can both be filled.
- **P2:** weights 1 and 2 balance exactly 1, 2 and 3. Boards 4 and 5 cannot be filled (the total is 3), which fits "Which targets … can you balance?".
- **P3:** the 1, 4 kit balances 1, 3, 4, 5 and the 1, 3 kit balances 1, 2, 3, 4: four each, so neither balances more. Board 2 works only with 1, 3; board 5 only with 1, 4.
- **P4:** of the six kits, only {1, 3} covers 1–4.
- **P5:** only 9 works. The 8-kit misses 13 and the 10-kit misses 5. Boards: 5 + 1 + 3 = 9 and 13 = 1 + 3 + 9.

## Grades 2–3: checks out completely

- **P1:** 1, 2 → 1, 2, 3; 1, 3 → 1–4; 1, 4 → 1, 3, 4, 5 (within 1–6).
- **P2:** 9 is the only third weight from 1 to 199 that covers 1–13. The boards are 5 + 1 + 3 = 9, 8 + 1 = 9 and 13 = 1 + 3 + 9.
- **P3:** the first targets missed are 13 (1, 3, 8), 14 (1, 3, 9) and 5 (1, 3, 10).
- **P4:** 4 balances in exactly two ways with 1, 3, 8 (4 = 1 + 3; 4 + 1 + 3 = 8) and one way with 1, 3, 9. The page prints 2 and 1 boards.
- **P5:** no kit works. Exhaustively, no three-weight kit with weights ≤ 40, repeats allowed, exceeds 13 positive targets.
- **P6:** 27 is the unique best fourth weight, giving the run 1–40. With 26 the run is 1–39; with 28 it is 1–13.

## Grades 4–5: checks out completely

- **P1:** among all pairs a < b < 60, only {1, 3} covers 1–4.
- **P2:** 9 is the unique best weight, with run 13. Smaller w gives a run of w + 4; w ≥ 10 gives 4.
- **P3:** 1, 3, 9 balances 1–13, each in exactly one way. Boards: 4 = 1 + 3 and 7 + 3 = 1 + 9.
- **P4/P5:** among different weights ≤ 60, the most distinct positive targets is 13, and 28,588 kits reach it (1, 3, 9; 1, 3, 10; …). No kit covers 1–14.
- **P6:** adding 27 gives 1–40, each in exactly one way. 27 is the only such weight.
- **P7:** the answer is 121. The kit 1, 3, 9, 27, 81 reaches it with every target in one way, and a search of all sorted five-weight kits finds it is the only kit that does.

## Bonus companion: checks out completely

- **P1:** all nine (removed, target) rows can be balanced. The table prints exactly those nine rows.
- **P2:** the only pairs (up to 200) covering 1–3 are {1,2}, {1,3}, {2,3}. So {1,2,3} is the only robust triple from 1–8, and also up to 60. "Can a different kit do this?" has the answer no.
- **P3:** the only pair covering 1–4 is {1,3}, so no triple survives every removal. This holds up to 60, and also with equal values allowed.
- **Search example:** candidates 8, 9, 10, compare with 9, heavier → 10. This is correct and is not a task instance.
- **P4/P5:** the fewest comparisons needed for 1..n are 0, 1, 1, 2, 2, 2, 2, 3, … The largest set solvable in k comparisons is 1, 3, 7, 15 = 2^(k+1) − 1. So 1–7 can be done in two comparisons, and the first threshold must be 4. 1–8 cannot be done in two.
- **P6:** the printed trays (2, 3, 2, 4) match the requested teams. Kits 1–4, 1–6 and 1–8 have exactly one partition each. {1,2,5} has none: its total is even, but 5 > 4.
- **P7:** exactly one split: {1,6}, {2,5}, {3,4}.

## Base adult guide: correct throughout

- **Overview:** balanced ternary with endpoints 4, 13, 40, 121 is correct. So is the (3^m − 1)/2 bound "even if gaps are allowed", which exhaustive search confirms for m ≤ 4 at bounded weights. The 2S + 1 step is correct for S = 1, 4, 13, 40: a heavier weight misses S + 1, and a lighter one falls short. The hypotheses (each weight once, target fixed, one exact balance) are stated.
- **Small-kit key:** all six rows and their reasons are correct, including "1…4 and 6…14" for 1, 3, 10.
- **Answer keys:**
  - K–1 P1–P5: correct, including all six P4 kits.
  - G2–3: the 13-row table is all valid placements with each weight used at most once, and P2–P6 are correct.
  - G4–5 P1–P7: correct. The proofs hold: the a, b, b − a, a + b argument, the largest-differing-weight cancellation (8 < 9, 2 < 3) and the interval proofs.
- **Extension:** one-sided weights 1, 2, 4 cover 1–7 uniquely.
- **Cross-references:** "page 2", "next page", "(page 3)" and the route note's problem numbers are all right.

## Bonus adult guide: correct apart from problems 2 and 3

The P1 balances, the P2 case argument ("even without the 1-8 cap"), the P3 proof, the P4 plan and the "first threshold must be 4" claim are correct. So are the P5 branch bound, M(k) = 2M(k−1) + 1, the 15-candidate three-comparison plan, the P6 witnesses with the {1,2,5} impossibility, the P7 forcing argument, endpoint pairing and the claim that m | r gives m teams.

## Located problems

### 1. K–1 p. 5, Problem 5: the tenth dot on the "10" weight card sits on the card's bottom border (minor, diagram)

- **Diagram:** the "10" card (dots in rows of three: 3, 3, 3, 1).
- **Evidence:** `extract.out` puts the lowest dot 0.21 pt above the card's bottom edge. The dot is 3 pt across and the border stroke is 0.7 pt, so the dot overlaps the stroke. At 300 dpi it reads as a blob on the border rather than a tenth dot inside the card. Every other card's dots clear the border by at least 10.9 pt. The count is right, but for K–1 the dots are how a child reads the weight, and P5 turns on telling 8, 9 and 10 apart.
- **Cause:** `make_packets.py` `weights()` draws a 2.25 cm card with dot rows at 1.05 + 0.38k cm. The fourth row lands at 2.19 cm.
- **Smallest fix:** change the row step from `.38` to `.33` in `weights()`, which puts the fourth row at 2.04 cm, about 4 pt clear. Alternatively, draw 10 as two rows of five.

### 2. Bonus guide p. 2, P1–3 "Depth and further questions": the question assumes a change that does not happen (minor)

- **Quoted text:** "Ask how the conclusion changes if equal-valued cards are allowed; do not silently allow them in the printed task."
- **Evidence:** a pair of equal cards a, a balances only a and 2a, so it never covers 1–3. Every surviving pair must therefore still be {1,2}, {1,3} or {2,3} (for 1–4, {1,3}). With repeats allowed, {1,2,3} is still the only kit for P2 and P3 is still impossible. `check_bonus.py` confirms this over all multisets with weights ≤ 60. An adult reading "how the conclusion changes" would look for a duplicate-card kit that does not exist.
- **Smallest fix:** "Ask whether allowing equal-valued cards changes the conclusion. (It does not: two equal cards a, a balance only a and 2a, so the surviving pairs must still be {1,2}, {1,3}, {2,3}, or {1,3} for targets 1–4.) Do not silently allow them in the printed task."

### 3. Bonus guide p. 1, Mathematical overview: one sentence is false on its literal reading (minor, wording)

- **Quoted text:** "a two-weight kit covering those four targets must be {1,3}, and every surviving pair cannot be that kit."
- **Evidence:** read literally, "every surviving pair cannot be {1,3}" says that no pair can be {1,3}. That is false: {1,3,x} with x removed leaves {1,3}. The true statement, which the P3 solution on p. 2 gives correctly, is that the three surviving pairs cannot all be {1,3}, because three different weights give three different pairs. In the theorem-first overview, this is the one sentence an adult reads for the P3 destination.
- **Smallest fix:** "… must be {1,3}, and the three pairs left by the three possible removals cannot all be {1,3}."

## Observations that are not errors

- **Launch example:** the shared launch (target 3 with weights 1 and 4) is also one entry of K–1 P3 and 2–3 P1, so it gives away that entry. It does not reveal either problem's conclusion. This is a design point for the card.
- **Board counts:** Grades 2–3 P4 prints exactly as many boards as there are balances (2 for 1, 3, 8 and 1 for 1, 3, 9), so the page shows the counts. The "every possible way" argument (big weight off, opposite or beside) is still the child's work.
- **Impossible boards:** K–1 P2 prints boards for 4 and 5, which cannot be balanced. That fits the question, but adults should expect and welcome "cannot".
- **Guide's 10-kit reason:** the guide's reason in K–1 P5 covers only the case with 10 opposite the target. The other two cases (10 off: at most 4; 10 beside: impossible) are immediate, so the claim stands.
- **Cards for weights children choose:** the base materials list only cards 1, 2, 3, 4, 8, 9, 10, 27, 81. Children who choose 5, 6, 7 or 11 in 2–3 P2, 4–5 P1, P2 or P5 will have no card and must write the weight. The mathematics is unaffected.
- **P7 kit:** the five-weight kit reaching 121 is unique (the search found only 1, 3, 9, 27, 81). The page asks only for "a kit", so the guide need not mention this.
