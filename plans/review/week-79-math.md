# Week 79 (numbered-ball detectives): math check

Scope:
- `lowell-math-circle-year-2/week-79/week-79-students.pdf`: one selected-band packet, 5 pages.
  - pp. 1–2 (Grades 2–5): the opening rule and worked visual, then Problems 1–3.
  - p. 3 (Grades 4–5): Problem 4.
  - p. 4: a sheet of 24 cards. p. 5: an A/B mat.
- `week-79-facilitator.pdf`: 4 pages.

Sources read: `source/week-79/student/students.tex`, `guide/facilitator.tex`, `build.py`, `README.md` and `SOURCES.md`, plus the outline `worksheet-workflow/outlines/week-79-numbered-ball-detectives.md` for intent. I did not run or import the package's `check_math.py`. My scripts and their outputs are in this run folder, for `plans/review/checks/week-79/`. Checked October 16, 2026.

**Result: every printed fact, formula, answer and diagram is correct. I found 2 problems, both in the guide. (1) A hint headed "Problems 3–4" states two facts that hold only for the smallest-card rule, and both are false under Problem 3's rule. (2) The guide never answers Problem 4's finite-day question for the changed rule, and the student wording admits a defensible "yes" there.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures):
  - Replays both rules day by day with explicit sets for 1,500 days. The replay picks min(A) or the larger new card directly and does not use the closed forms. Closed forms are only compared against it.
  - Confirms the opening day-1 states.
  - Problem 1: confirms the end-of-day counts are n and n for every day under both rules. The day-6, day-10 and day-12 states match. Six days use cards 1–12 and twelve days use cards 1–24. In 12 days, A holds at most 13 cards at once (mid-day) and B at most 12.
  - Problem 2: confirms the entry day ⌈k/2⌉ and the move day k, including cards 3, 6, 10, 20 and 8.
  - Problem 3: confirms the changed-rule sets (odds ≤ 2n−1 in A, evens ≤ 2n in B). End-of-day and mid-day count histories match the smallest rule exactly, and the arrangements differ on every day ≥ 1. Card 1 is a one-card witness.
  - Problem 4: for labels 1–600, finds the last day each label changes bowl and checks that it stays put to day 1,500. It then tests both readings of "that arrangement" on finite days.
  - Tests the guide's p. 3 sentences under both rules, the p. 4 limit facts (pointwise limit, sums, sup over k, the least majorant), and the first-route timing (55 min).
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 0 failures):
  - Reads the delivered student PDF with pdfplumber. Checks headers, footers, band labels, and that the problems are numbered 1–4 consecutively.
  - Opening visual: the six bowl outlines are equal (130.4 × 42.5 pt). Each card square is mapped to the bowl that contains it and its label read. The result, Before {}/{}, then A {1,2}, then A {2}/B {1}, equals a day-1 replay.
  - Problem 2: four 17 × 17 mm cards labelled 3, 6, 10, 20, each with a "Day ___" blank under it.
  - Problem 4: four boards, titled with both rules, with nothing printed inside except the letters A and B.
  - Card sheet: 24 squares, each exactly 30.0 × 30.0 mm, labelled 1–24 in reading order, one centred label each.
  - Mat: A and B regions are each 180 × 96 mm. Each holds 18 flat 30 mm cards, against a peak need of 13.
  - Uses pdftotext to confirm the guide sentences quoted below.

The infinite statements are proved by hand, not only replayed:
- **Smallest rule.** Induction on n from A₀ = B₀ = ∅. From A_n = {n+1,…,2n}, adding 2n+1 and 2n+2 makes the minimum n+1, which moves. So B_n = {1,…,n}, label k moves on day k, and B never loses a card.
- **Changed rule.** It moves only the day's even card 2n. So label 2m−1 enters A on day m and is never moved, and label 2m is in B from day m on.
- **Counts.** The counts tie because each day adds 2 to A and moves 1 from A to B, whatever the rule.
- **Limits.** Under the smallest rule, for each fixed k, k ∉ A_n for all n ≥ k, so A settles empty and B settles to all labels. On every day N ≥ 1, label N+1 is in A. On day 0, B is empty.

## Student packet, Grades 2–5 pages (pp. 1–2, 4–5): checks out

- **Opening rule and visual (p. 1):** correct for day 1 of the smallest-card rule. Because A is always {n+1,…,2n}, "smallest" is also the oldest card, so no reading of "smallest" changes any answer.
- **P1:** no. At the end of day n both bowls hold n cards, under every rule that adds two and moves one. The six-day and twelve-day runs fit the cards supplied: 12 and 24 cards.
- **P2:** card k moves on day k: 3 → 3, 6 → 6, 10 → 10, 20 → 20. Card 20 would need cards 1–40, so it must be predicted, as the page intends. Every card eventually moves, so "any numbered card" has an answer.
- **P3:** no. Count histories are identical at every moment (end of day and mid-day). The cards always differ: after day 1, A = {2} under the smallest rule and A = {1} under the changed rule. Card 1 alone tells the rules apart from day 1 on.
- **Materials (pp. 4–5):** 24 distinct 30 mm cards cover the longest printed run, and each mat region holds the 13-card peak flat.

## Student packet, Grades 4–5 page (p. 3): one problem, item 2 below

The settled arrangements are correct:
- Smallest rule: every label settles in B and A settles empty.
- Changed rule: odd labels settle in A and even labels in B.

The answer "no finite day" is correct for both under the whole-arrangement reading. The changed-rule half of the question has a second reading; see item 2.

## Adult guide: correct except items 1 and 2

The overview's formulas, entry and finishing days, eventual-membership limits and changed-rule sets are true with the hypotheses stated. So are the claim that count histories do not determine limiting membership and the p. 4 analysis:
- the pointwise limit is 0 while Σ_k a_n(k) = n;
- sup_k a_n(k) = 1 for n ≥ 1 and 0 at day 0;
- no summable majorant exists, because sup_n a_n(k) = 1 for every k ≥ 2;
- B is monotone.

The remark that non-uniformity alone does not explain a failed interchange is also right: 1/n on k ≤ n converges uniformly to 0 yet sums to 1. The induction step, every P1/P2 answer (days 6 and 10; cards 3, 6, 10, 20, 8), the day-0 caveat and the changed-rule mechanism are correct.

### 1. Guide p. 3, hint headed "Problems 3–4" (moderate): two sentences are false under Problem 3's rule

- **Quoted text:** "Problems 3–4: inspect a named finite list of labels, leaving every A/B card where it is. Inspect labels 1–6, then 1–12, regardless of location. Any fixed finite list eventually has all its labels in B. At every positive finite day N, label N + 1 is still in A."
- **Evidence:** Problem 3 uses only the changed rule (move the larger new card), and Problem 4 asks about both rules. Under the changed rule:
  - Labels 1, 3 and 5 of the list 1–6 are never in B. They are in A at the end of every day through day 1,500, and by the proof above, forever.
  - "Label N + 1 is still in A" fails on every odd N. For N = 1, label 2 is in B and A = {1}. The failures continue at N = 3, 5, 7, 9, 11 (`check_math.py.out`, "Guide p. 3" block).

  Both sentences are true for the smallest-card rule. Only the next paragraph's "For the changed rule…" signals that the hint meant that rule. An adult helping with Problem 3 who follows the heading would tell children that labels 1–6 all end up in B, which is the opposite of what the changed rule shows.
- **Smallest fix:** change "Problems 3–4:" to "Problem 4, smallest-card rule:". Optionally add a Problem 3 hint: "Problem 3: after day 1, card 1 is in B under the smallest-card rule and in A under the changed rule."

### 2. Guide p. 3 and student p. 3, Problem 4, changed rule (minor): the finite-day question has no answer in the guide, and it admits a correct "yes"

- **Quoted text:** "For each rule, decide where all the labels settle. Can that arrangement happen on a finite day?" (student p. 3). For the changed rule, the guide says only "the larger new card is 2n, so it moves immediately to B. The smaller 2n − 1 never moves." The settled arrangement (odds in A, evens in B) is only implied, by this sentence and by the overview's finite-day sets. The guide never answers the finite-day question for that rule. Its finite-day argument ("At every positive finite day N, label N + 1 is still in A … Hence no finite day finishes every label") is the smallest-rule argument and does not transfer.
- **Evidence:** under the changed rule, on every day N each card present is already in the bowl where it settles (A = odds ≤ 2N−1, B = evens ≤ 2N). This holds for all 300 days tested and by the proof above. By contrast, under the smallest rule no day N ≥ 1 has this property, because cards N+1 to 2N sit in A, the bowl they will leave (`check_math.py.out`, Problem 4 block). So "Can that arrangement happen on a finite day?" has two answers for the changed rule:
  - Read as "odds in A, evens in B", a child can truthfully say yes, it looks like that every day.
  - Read as the whole arrangement, the answer is no, but only because labels above 2N have not arrived. That is a weaker reason than the smallest rule's, where A is never empty.

  An adult has nothing in the guide to tell these apart and may treat the first answer as wrong.
- **Smallest fix:** in the guide, after "The smaller 2n − 1 never moves.", add: "So in Problem 4 the odd labels settle in A and the even labels in B. On every finite day each card present is already in its settled bowl, so 'it already looks like that' is right about the cards present. The whole arrangement never occurs, because labels above 2N have not arrived by day N. Contrast the smallest-card rule, where cards N+1 to 2N sit in A, the bowl they will leave."

**Not counted (outside the math scope or correct as printed):**
- The guide's Problem 1 checkpoint is day 10 (A = {11,…,20}). The page's optional continuation is twelve days (A = {13,…,24}, B = {1,…,12}). Both are correct.
- The overview's band map gives "changed-rule comparison" to Grades 4–5, but Problem 3 is printed on a Grades 2–5 page and is in the first route.
- "If the table says A is always equally full" presumably means "A and B are always equally full".
- The two Problem 4 board pairs differ slightly in height (63 mm and 60 mm).
