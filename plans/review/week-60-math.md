# Week 60 (take it or pass): math check

Scope: `lowell-math-circle-year-2/week-60/week-60-students.pdf` (W60-S-v2, 7 pp., Problems 1–9) and `week-60-facilitator.pdf` (W60-FAC-v1, 8 pp.). The student PDF is one combined packet. Pp. 1–3 and 6 (Problems 1–4 and 7) are headed Grades 3–5; pp. 4, 5 and 7 (Problems 5, 6, 8 and 9) are headed Grades 4–5. I also read the editable source in `lowell-math-circle-year-2/source/week-60/` (`student/students.tex`, `student/mathematics.md`, the READMEs). Checked October 5, 2026. My scripts and outputs are in [checks/week-60/](checks/week-60/).

**Result: every answer, total, average, table entry and theorem in the packet is correct. I found 4 minor problems, none of which changes an answer: an unstated counter count in the student rules (p. 1), a practice example that models the Problem 3 answer (p. 2), a wrong piece name in the guide's K–1 materials list (guide p. 2), and a false "only tie" remark in the guide (p. 8).**

## How it was checked

- `w60common.py` holds my own exact model of the game: a bag of equally likely tickets, draws with replacement, a fixed number of offers, take-and-stop or pass-forever, a compulsory last offer, and reward = the one taken score. It plays complete words, enumerates every deterministic history-dependent policy (a take/pass bit for every observed prefix), and computes the optimum over all history-dependent policies by evaluating the whole history tree. Nothing from the packet's `check_math.py`, `check_pdf.py` or `check_answers.py` is used.
- `check_math.py` (`out_check_math.txt`, 85 ok lines, 2 FAIL lines that are items 3 and 4 below) recomputes every answer:
  - V_m for every bag in the packet by the full history tree and by the recursion V_m = E[max(X, V_(m−1))], and confirms they agree (0/4/6 to n = 4, 0/5/6 to n = 5, 0/3/6, 1/2/5, 1/3/5).
  - All 8 two-offer first-offer rules for each of 0/4/6, 0/3/6, 0/5/6 and 1/3/5.
  - Plans A and B on all 27 words, word by word.
  - All 4,096 three-offer history policies for 0/4/6 and for 0/5/6, and the history-tree optimum for 0/5/6 at four offers (this covers all 2^39 four-offer history policies, since decisions at different nodes act on disjoint sets of words).
  - Problem 9 exhaustively on 558 bags (every bag of 1–3 tickets from −2..3, plus 300 random bags of 1–5 tickets from −5..9, with duplicates and negatives) at horizons up to 4 or 5.
  - Every printed position for ties (take value equal to the continuation value).
  - It reads the delivered guide PDF text and checks every A/B entry of the 27-word table, every group total, count, total and average in the guide against the computation, and the preparation arithmetic.
- `check_diagrams.py` (`out_check_diagrams.txt`, 38 ok lines, no FAIL; `extracted.json`) reads the delivered student PDF itself (PyMuPDF text spans and vector drawings), not the source:
  - Headers and bands on all 7 pages, the footer, and Problems 1–9 in order.
  - Every dashed card and the digits inside it: p. 2 is exactly the nine 0/4/6 pairs once each; p. 3 is exactly the 27 0/4/6 triples once each; p. 6 has the nine 0/3/6 pairs under "Bag: 0, 3, 6" and the nine 0/5/6 pairs under "Bag: 0, 5, 6".
  - Every card has one score line and one (pairs) or two (triples) dividers. All pair cards are 154.8 × 63.36 pt, all triple cards 154.8 × 50.4 pt, so cards of one length are interchangeable when sorted and pooled.
  - P5 position boxes: "2 offers left, including this one" with a current 4 and two counters; "3 offers left, including this one" with a current 4 and three counters. All five counters are true circles of equal diameter 17.28 pt.
  - The p. 1 practice boxes (offer 2, two counters → pass, one counter → must take 1 → score 1) and the p. 2 practice card (3 | 1 → take 3, later 1 unseen → score 3) read in order and are legal plays under the p. 1 rules.

## Grades 3–5 (pp. 1–3 and 6, Problems 1–4 and 7): correct; items 1 and 2 below

- **P1:** open; any legal rule works. The practice round on p. 1 is legal (and, incidentally, passing 2 is optimal for 1/2/5 because the one-offer continuation is 8/3 > 2; the target bag is untouched).
- **P2:** yes. Every one of the 8 two-offer and 4,096 three-offer history policies scores 6 on (6,6)/(6,6,6) and 0 on (0,0)/(0,0,0), so six constant words give 36 versus 0 and reversing them gives 0 versus 36, whatever the children invented. Each constructed match has probability 3^−30 > 0. Neither match settles the expected ranking. This holds under either reading of "winners" (two-offer rule versus three-offer rule, or child versus partner).
- **P3:** the unique best first-offer choice is pass 0, take 4, take 6: total 40 (average 40/9). The other seven choice sets total 38, 32, 30, 30, 28, 22, 20. Group take/pass totals are 0/10, 12/10, 18/10. Scores: one 0, four 4s, four 6s.
- **P4:** A totals 130, B totals 134, so B. A scores one 0, thirteen 4s, thirteen 6s; B two 0s, eight 4s, seventeen 6s. The plans differ only on (4,0,0) (A +4) and on (4,0,6), (4,6,0), (4,6,4), (4,6,6) (B +2 each). Group totals by first offer: 40/40, 36/40, 54/54.
- **P7:** 0/3/6: best total 36 (average 4), reached by exactly two choice sets, pass 0 and take 6 with 3 either taken or passed (group totals 0/9, 9/9, 18/9). 0/5/6: unique best pass 0, take 5, take 6, total 44, average 44/9 (group totals 0/11, 15/11, 18/11). "Find all" is right for both bags, and the single "Total" blank works because both 0/3/6 optima total 36.

## Grades 4–5 (pp. 4, 5 and 7, Problems 5, 6, 8, 9): checks out completely

- **P5:** with two offers left including the current 4, passing leaves the forced next offer, average 10/3 < 4: take. With three left, passing leaves the best two-offer play, average 40/9 > 4: pass. No ties. The diagrams' counters equal the offers left including the current one, matching the p. 1 counter rule.
- **P6:** the maximum over all 4,096 history-dependent policies is 134 (average 134/27). All 8 optimal tables differ only at unreachable nodes (after a taken first 6), so the plan is unique: take only 6 first; on the second offer take 4 or 6 and pass 0; take the last. It is Plan B. After any passed first offer the best nine-word total is 40, so remembering passed offers cannot help.
- **P8:** bag 0/5/6: V1..V4 = 11/3, 44/9, 143/27, 448/81. Three offers: take 5 or 6 at either nonfinal offer (5 > 44/9 and 5 > 11/3), total 143 on 27 words (one 0, thirteen 5s, thirteen 6s). Four offers: first take only 6 (143/27 > 5), then the three-offer plan, total 448 on 81 words (two 0s, 26 5s, 53 6s). The first 5 is taken with three offers and passed with four. No ties anywhere, so both plans are unique.
- **P9:** an extra offer never lowers the optimum, and it leaves it unchanged exactly when every ticket has the same score; otherwise it strictly raises it. Confirmed on all 558 bags at every tested horizon, including duplicate and negative scores.

## Adult guide

Every answer, table entry and proof is correct. I checked:
- the overview: V1 = 10/3, V2 = 40/9, V3 = 134/27; the threshold rule (take above V_(m−1), pass below, either at equality); the claim that backward induction bounds history-dependent and randomized plans; "more offers never lower the optimum; strictly raise it for any nonconstant finite bag; equality for a constant bag"; and the 0/3/6 tie with both optima totalling 36;
- the P2 construction table and its "whatever the children invented" claim;
- the P3 key and group comparison;
- all 27 A/B entries of the P4 table, the group totals 40/40, 36/40, 54/54, the score counts and the "net advantage 4" breakdown;
- the P7 take/pass totals and both score keys;
- the readiness example (1, 3, 5 → nine cubes, 3 each);
- the P5 table and its equal-batch comparisons (12 vs 10, 36 vs 40);
- the P6 object-based bound (second-offer totals 0/10, 12/10, 18/10 → 40 after every passed first offer; first-offer group bounds 40, 40, 54 → 134);
- the P8 table, both V computations, the score counts and the 143 + 143 + 162 decomposition;
- the P9 proof (pass the new first offer; constant-bag equality; V_n < M from the all-minimum word; V_(n+1) − V_n = E[(X − V_n)+] > 0);
- the p. 8 recurrence proof, the randomization remark and the complete-words weighting (each length-n word has probability k^−n; an accepted first offer stands for k^(n−1) words);
- the preparation arithmetic (9 tickets, 12 counters, 6 action places; 18 replacement tickets; prints 8, 12, 12, 6, 3; 54 cards per table, 108 cut; KK11 blocks 30/60/15 = 5 × the Week 1 K–1 kit of 6 blues, 12 greens and 3 purples, plus ten each of the reds and yellows that Week 1 leaves as "a few").

The guide's problems are items 3 and 4 below.

## Located problems (4, all minor; no incorrect answers)

### 1. Student p. 1, shared rules: the number of turn counters is never stated
- **Quoted text:** "Set the number of offers before a round. Your partner shows each offer. Take it to end the round, or pass it forever. With one counter left, you must take the offer, even if it is 0. Remove one turn counter after deciding on each offer."
- **Evidence:** the deadline rule fires at "one counter left", so it makes the last offer compulsory only if a round starts with one counter per offer. The page never says so. The practice figure shows "offer 2 / two counters" without saying it is a two-offer round, and the convention is first spelled out on p. 4 ("2 offers left, including this one" with two counters), which is a Grades 4–5 page. Each kit holds four counters (guide p. 2). A pair that puts all four out for a three-offer round reaches the third offer with two counters left, so nothing forces it to be taken; if it is passed, the round ends with no score and the rules cannot be carried out. The guide's launch ("Show the separate 1, 2, 5 practice bag and two counters. Say: 'We set two offers.'") covers it in the room, so the risk is small.
- **Smallest fix:** "Set the number of offers before a round, and put out one turn counter for each offer."

### 2. Student p. 2, practice example: the demonstrated rule is an optimal rule with the same shape as the Problem 3 answer
- **Quoted text:** "With practice tickets 1, 3, 5, this rule takes 3 or 5 and passes 1:" followed by the card 3 | 1 → "take the first offer: 3 / the later 1 is unseen" → "score 3".
- **Evidence:** for the 1/3/5 bag at two offers, the best total on the nine cards is 33, reached by exactly two rules: take 3 or 5 (the printed rule) and take only 5 (`check_math.py`, p. 2 section). So the example shows an optimal rule, and its shape, "pass the smallest ticket, take the other two", is exactly the unique answer to Problem 3 on the same page (pass 0, take 4, take 6) and to the 0/5/6 half of Problem 7. A child can copy the pattern instead of comparing group totals; they would still have to total the nine cards. The source README intends "Neither gives an optimal target rule", which is true only because the bag differs. Nothing printed is false.
- **Smallest fix:** "With practice tickets 1, 3, 5, this rule takes any first offer:" The figure stays as it is (3 | 1 → take 3, later 1 unseen → score 3), and the rule is no longer optimal (total 27 < 33).

### 3. Guide p. 2, KK11 materials: "purple trapezoids" should be purple chevrons
- **Quoted text:** "For four child kits plus one spare, plan 30 small blue rhombi, 60 green triangles, 15 purple trapezoids, ten red trapezoids and ten yellow hexagons".
- **Evidence:** the counts are 5 × the Week 1 K–1 kit ("For each K–1 child: 6 blues, 12 greens, 3 purples, and a few reds/yellows", Week 1 guide p. 1). Week 1 calls its purple pieces "purple chevrons" throughout ("Every purple occupies four triangle spaces and splits into two blues") and never trapezoids. The trapezoid in this kit is the red piece, which the same sentence lists separately. An adult could look for a purple trapezoid that does not exist in the kit. (Pages 1–2 of the K–1 packet, the ones the guide resumes, allow "any small pieces", so the purples are optional there.)
- **Smallest fix:** "15 purple chevrons".

### 4. Guide p. 8, proof section: "only the two-offer 0, 3, 6 middle choice is tied" is false
- **Quoted text:** "On this week's distinct three-ticket bags, only the two-offer 0, 3, 6 middle choice is tied among the student positions."
- **Evidence:** the p. 2 practice card is a printed student position in a three-ticket bag: bag 1, 3, 5, two offers, first offer 3. Taking gives 3; passing gives the mean (1 + 3 + 5)/3 = 3. It is a tie, and the printed rule there is one of the two optimal rules (item 2). The scan of every printed position finds exactly these two ties and no others (`check_math.py`, "Ties among the positions printed on student pages"). No answer depends on the remark, but an adult reading it would believe the practice rule's "takes 3" is a strict choice.
- **Smallest fix:** "Among Problems 1–9, only the two-offer 0, 3, 6 middle choice is tied; the page-2 practice bag 1, 3, 5 also ties at a first 3."

## Not checked

- The Ferguson page and section references (pp. 2.1, 2.2, 2.7–2.8, equation (6)). The reference PDF is not in this checkout (only `external-resources/new-themes-52-63/week60-61/README.md` and its manifest), and downloading it was refused by the network proxy. The mathematics they are cited for is standard, and I verified it independently above.
- Physical handling: blind drawing, mixing, display versus bag ticket, counter timing and score-line erasing. The guide already marks these unrehearsed.
- The packet's own `check_math.py`, `check_pdf.py` and `check_answers.py`, which I did not run, by design.
