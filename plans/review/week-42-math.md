# Week 42 (fair results from a bag): math check

Scope:
- `lowell-math-circle-year-2/week-42/week-42-k-1.pdf` (5 pp., Problems 1–6), `week-42-grades-2-3.pdf` (4 pp., Problems 1–7), `week-42-grades-4-5.pdf` (4 pp., Problems 1–7) and `week-42-facilitator.pdf` (6 pp.).
- The bonus companion in the same folder: `week-42-bonus.pdf` (W42-BONUS-v1, 3 pp., Problems 1–3) and `week-42-bonus-facilitator.pdf` (3 pp.).
- I ignored the archive folders.

Sources read: `source/week-42/editable/src/write.py` and `common.py` (the generators of the three student TeX files), and `source/week-42-bonus/student/build.py`. The six delivered PDFs are byte-identical (MD5) to `source/week-42/editable/reference-pdfs/` and `source/week-42-bonus/reference-pdfs/`. I did not run or import `check.py`, `verify_math.py`, `facilitator-src/check_math.py` or the bonus `student/verify.py`. I rendered every page at 100 dpi and read each one. My scripts and their outputs are in [checks/week-42/](checks/week-42/). Checked October 5, 2026.

**Result: every answer, count and probability in the three bands, the bonus and both guides is correct, and every counter diagram matches its text. I found 5 minor problems. Two are student wordings that can change an answer: K-1 P1, where returning the counter is stated only for random draws, and K-1 P5, where the rule is not fixed. The bonus P3 wording leaves "whole pair fair" undefined. Base guide p. 1 has a sentence that drops a hypothesis. The guide's counter count falls one short for one Grades 4–5 P5 case.**

## How it was checked

- **`check_math.py`** (output `out_check_math.txt`, 114 checks, 0 failures):
  - It builds labelled counters for every bag and enumerates all 81 colour-only rules. For 3R/1B it finds exactly two fair rules (BR and RB to opposite shapes, RR and BB skipped). Both skip exactly 10 of 16. No fair rule gives a shape on every pair.
  - It recomputes every K-1, 2–3 and 4–5 answer: the P4 bags, the red-count sweep 0, 6, 8, 6, 0, all the P6 stories, the 4 × 4 grid, all cross-bag cases, the 49-outcome bags and the 12-outcome no-replacement case. It also checks the general rule for r red and b blue up to 8 + 8.
  - It checks the overview formulas exactly over rational grids: p(1−q) = (1−p)q iff p = q, output rate 2p(1−p), and the chance [p² + (1−p)²]^m of no output (by enumeration for m ≤ 3).
  - Bonus P1: it enumerates all 3⁶ assignments of the six mixed words. Exactly 36 (3!·3!) are fair for every p, and these are the ones that give each shape one one-R word and one two-R word. It checks the 64-, 8- and 27-history counts.
  - Bonus P2: it enumerates all 16 and all 256 four-draw histories, with and without recycling. It checks the per-block distributions and the expected output 4p(1−p) + 2p²(1−p)² exactly.
  - Bonus P3: it enumerates every ticket cup of up to 10 tickets.
  - It reads both guides with `pdftotext` and compares 47 printed numbers, row lists and the p. 4 grid table with the enumeration.
- **`check_diagrams.py`** (output `out_check_diagrams.txt`, 79 checks, 0 failures) reads the vector drawings and word positions of every student page with PyMuPDF. It recovers each counter, its fill colour, its label and the box that contains it, then compares them with the text:
  - every bag composition and caption;
  - the order of every pair;
  - the 16 K-1 pictures, which are exactly the ordered labelled pairs, row by row;
  - the 2–3 grid heads, and the highlighted cell at row R2, column B, which shows R2 then B;
  - the 18 K-1 story slots;
  - the eight bonus three-draw words, the sixteen bonus four-draw stories and the eight ticket boxes;
  - that every counter, square and circle is drawn with equal width and height.

  The bonus triangle symbol is isosceles (sides 24.0, 25.1, 25.1 pt). The page never calls it equilateral, so I do not count this as a problem.

## K-1 (pp. 1–5): checks out except for the wording in Problems 1 and 2 below

- **P1:** there are four colour pairs, RR, RB, BR and BB, and the page has four two-position boxes for them. With replacement BB is possible from one blue. Removing the blue leaves only RR, so RB, BR and BB disappear. See Problem 1 for the replacement wording.
- **P2/P3:** the 16 pictures fall into colour classes RR 9, RB 3, BR 3 and BB 1. Exactly two rules give each shape the same number of pictures and sometimes give each shape. The guide's completeness argument is valid: RR's 9 pictures outweigh the other 7. With RR skipped, giving BB a shape never balances (4 vs 3, 1 vs 3 or 6, 7 vs 0).
- **P4:** under the kept rule, RBBB gives 3 and 3 of 16, RRBB gives 4 and 4, and RRRR and BBBB give no shape.
- **P5:** red counts 0–4 give 0, 6, 8, 6 and 0 shapes in 16, so two red and two blue is best. The counter drawn first can always be drawn again, which gives a same-colour pair, so with the kept rule no bag gives a shape every time. See Problem 2.
- **P6:** all three targets can be reached, and the guide's stories are valid. Six RR pairs have chance (9/16)⁶ > 0.

## Grades 2–3 (pp. 1–4): checks out

- **P1/P2:** the grid holds RR 9, RB 3, BR 3 and BB 1. The highlighted cell (R2, B) is RB, which matches "row R2, column B".
- **P3:** 2R/2B has 4 RB and 4 BR, and 1R/3B has 3 and 3. Both are fair.
- **P4:** the two-red bag gives a shape in 8 of 16 pairs and the three-red bag in 6 of 16. Even if the rule may change, the two-red bag still wins.
- **P5:** RRRB then RBBB gives RR 3, RB 9, BR 1 and BB 3. That is 9/10 against 1/10, which is unfair for both fair rules.
- **P6:** six RR pairs settle it.
- **P7:** no. RR has 9 of 16, which is more than half. This relies on p. 1's definition that a rule acts on colour pairs. A rule that used P2's marks could give a shape every time fairly (for example, first counter R1 or R2 gives a square, 8 to 8). The printed definition already excludes that rule, and the guide's "No color-only deterministic rule" matches it.

## Grades 4–5 (pp. 1–4): checks out

- **P1/P2:** each shape has 3/16, and the conditional chance of each is 1/2.
- **P3:** the 5R/2B bag (drawn as 5 red and 2 blue) gives 10 and 10 of 49, and the 3R/4B bag gives 12 and 12 of 49. In general a bag gives rb and rb of (r + b)², which is fair exactly when r, b > 0.
- **P4:** a fair rule cannot always give a shape, because 9 > 8. The minimum skip is 10, which is correct for colour-only rules.
- **P5:** 3R/1B then 1R/3B is unfair (9/16 against 1/16). 3R/1B then 6R/2B (drawn as RRRR/RRBB) is fair at 6/32 each. 2R/2B then 1R/1B is fair at 2/8 each.
- **P6:** without replacement there are 12 pairs: RR 6, RB 3, BR 3, BB 0. That is fair. RB = BR holds for every bag without replacement (checked up to 6 + 6).
- **P7:** neither claim follows. BR followed by five RR is a valid counterexample to the first claim.

## Base adult guide: correct throughout, apart from Problems 3 and 5

- **Overview:**
  - P(RB) = p(1−p) = P(BR).
  - The two fair rules for 3R/1B and the 10 forced skips are correct.
  - Output rate 2p(1−p), with 8 of 16 against 6 of 16, is correct.
  - p(1−q) = (1−p)q iff p = q is correct.
  - The no-output chance [p² + (1−p)²]^m and "no finite worst-case deadline" are correct.
- **Keys:** every K-1, 2–3 and 4–5 key matches my enumeration, including the p. 4 grid table and every printed fraction. The restriction in the 4–5 P4 key ("deterministic color-only rules") is stated correctly.
- **Route page (p. 6):** the problem numbers it cites match the packets.
- **Source:** I could not check the citation (Levin, Peres and Wilmer, Appendix B.2, printed p. 312) because the book is not in this checkout. The von Neumann fact it is cited for is standard, and I verified it independently above.

## Bonus companion and its guide: correct throughout, apart from Problem 4

- **P1:**
  - The lone-colour-position rule assigns the words exactly as the guide prints them.
  - Each shape has weight p(1−p), and the total is 3p(1−p).
  - 3R/1B gives 12, 12, 12 and 28 skipped of 64. A one-red, one-blue bag gives 2, 2, 2 and 2 of 8. 2R/1B gives 6, 6, 6 and 9 of 27.
  - There are 36 universal rules, all of the one-from-each-class form, as the guide says.
- **P2:**
  - The both-skipped words are RRRR, RRBB, BBRR and BBBB.
  - A balanced bag gives 8/8 → 9/9 outputs (16 → 18). The per-block counts are 4/8/4 → 2/10/4.
  - 3R/1B gives 96/96 → 105/105 (192 → 210 of 256).
  - The expected output is 4p(1−p) → 4p(1−p) + 2p²(1−p)².
- **P3:**
  - Exactly three four-ticket cups have fair positions: SS,SS,CC,CC and SC,SC,CS,CS, which give two pairs, and SS,SC,CS,CC, which gives all four.
  - The extension (no cup has three possible pairs) is correct for any number of tickets, not only four.
- **Materials arithmetic:** 5 kits use 40 tickets, 20 counters and 40 tokens of each shape. The strip is 4 × 40 = 160 mm. All of this is consistent.

## Problems found

### 1. K-1 p. 1, Problem 1 (minor): returning the counter is stated only for random draws, but BB needs it

- **Quoted text:** "For random draws, use the same bag. Every counter has the same chance each time; put it back and mix after each draw." Then: "Problem 1: Choose draws yourself to make every different color pair. Which pairs disappear if you take the blue counter out of the bag?"
  - Guide p. 3: "Replacement makes BB possible even with only one blue counter. Taking the blue counter out leaves only RR: RB, BR, and BB disappear."
- **Evidence:** the bag holds one blue. A child who chooses draws and keeps the first counter in hand, because returning was stated "for random draws", can make only RR, RB and BR. That child answers three pairs, and RB and BR disappear. With returning, there are four pairs (`out_check_math.txt`, K-1 P1). The four printed record boxes hint at the intended answer, but the rule that produces BB is not stated for this task.
- **Smallest fix:** make returning unconditional on p. 1: "Use the same bag. Put each counter back after every draw; for random draws, mix and draw without looking."

### 2. K-1 p. 4, Problem 5 (minor): the rule is not fixed, and with a new rule the answer to the second question is yes

- **Quoted text:** "Problem 5: Choose a four-counter bag that makes shapes come out as often as possible. Could any four-counter bag give a shape on every pair?" Only P4 says "Keep your rule for these bags."
  - Guide p. 3: "No four-counter bag gives a shape on every pair under this rule".
- **Evidence:** in the 2R/2B bag every colour class has 4 of 16 labelled pairs. So six colour-only rules give a shape on every pair and are fair. One is "first counter red → square, blue → circle", which a child can find by noticing that half the bag is red (`out_check_math.txt`, "P5 other reading"). No other four-counter bag admits such a rule. The key's "No" is right only if the rule is kept.
- **Smallest fix:**
  - Print "Keep your rule. Choose a four-counter bag … Could any four-counter bag give a shape on every pair with your rule?"
  - Optionally add one guide sentence: with two red and two blue, a new rule (the first colour decides) gives a fair shape on every pair. The kept rule cannot, because it skips same-colour pairs.

### 3. Base guide p. 1, Assumptions and limits (minor): "Independence is sufficient" drops the same-bag hypothesis

- **Quoted text:** "If the first and second draws have red probabilities p and q and are independent, the kept weights are p(1-q) and (1-p)q: they agree exactly when p = q … Independence is sufficient, not necessary: the no-replacement variation is fair because reversing distinct-counter pairs preserves their chances."
- **Evidence:** the preceding sentence shows that independent draws with p ≠ q are unfair. For example, RRRB then RBBB is independent and gives circle 9 against square 1 (`out_check_math.txt`). So independence alone is not sufficient. What suffices is independent draws from the same bag (identically distributed). What the rule actually needs is P(RB) = P(BR), which is why the dependent, exchangeable no-replacement draws also work.
- **Smallest fix:** "Independent draws from the same bag are sufficient but not necessary: what the rule needs is P(RB) = P(BR). The no-replacement variation is fair because reversing distinct-counter pairs preserves their chances."

### 4. Bonus p. 3, Problem 3 (minor): "whole pair fair" is undefined, and under one natural reading every four-ticket cup is fair

- **Quoted text:** "Does fairness at each position make the whole pair fair?"
  - Bonus guide p. 2: "Cup 1's mixed pairs are impossible; Cup 2 has one ticket for each pair. Therefore marginal fairness does not imply whole-pair fairness."
- **Evidence:** only three four-ticket cups have fair positions: SS,SS,CC,CC, SC,SC,CS,CS and SS,SC,CS,CC. Each gives equal chances to every pair it can give (½, ½ or ¼ each; `out_check_math.txt`, Bonus Problem 3).
  - The base packet defines fairness as equal chances among outputs that come out, plus "sometimes gives each". A child who applies only the equal-chance half concludes that Cup 1 is fair, because SS and CC are equally likely, and answers "yes".
  - The intended "no" holds only because Cup 1 never gives SC or CS. With four tickets the failure is always missing pairs, never unequal chances.
  - The smallest cup with fair positions and unequal possible-pair chances has six tickets: SS,SS,SC,CS,CC,CC.
- **Smallest fix:**
  - Print "Does fairness at each position make all four pairs equally likely?"
  - Optionally add to the bonus guide: with four tickets, fair positions always give equal chances to the possible pairs, so the counterexample is a missing pair. Unequal chances need at least six tickets (SS,SS,SC,CS,CC,CC).

### 5. Base guide p. 2, Materials (minor): the counter count is one red short for Grades 4–5 P5's second case

- **Quoted text:** "prepare five opaque bags or cups; about eight red and eight blue same-size, same-feel counters per pair".
- **Evidence:**
  - Grades 4–5 p. 3, P5, second case, draws first from RRRB and then from RRRRRRBB, so a pair needs 9 red and 3 blue at once. The other bag sets fit within 8 + 8: 8R/6B for 4–5 P3, and 4R/4B and 3R/3B for the other P5 cases.
  - P5 in both upper bands also needs two containers per pair at once, while the guide gives one bag per pair.
- **Smallest fix:** "about ten red and eight blue counters and two opaque bags or cups per pair". Alternatively, note that a pair can use one bag for that case: draw from RRRB, return the counter, add three red and one blue for the second draw, then take them out again. That needs only 6 red and 2 blue.
