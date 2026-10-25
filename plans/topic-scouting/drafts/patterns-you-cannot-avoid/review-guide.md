# Review: facilitator guide, "Patterns you cannot avoid" (draft/facilitator.pdf, 6 pp.)

Reviewer: adversarial guide critic. I did not edit the guide or the pages. What I did:

- Rendered all 6 guide pages, all 19 student pages (K–1 6, Grades 2–3 6, Grades 4–5 7) and the Week 98 model guide, and read each one.
- Read `draft/src/` and the page sources (`gen.py`) for sizes.
- Re-derived every printed answer with my own code: `review-guide-check/check.py`, output in `review-guide-check/check.out`. The script uses exhaustive enumeration, full game trees for the strip game and Sim, exact probabilities for random safe play, and forced-step checks of every hand chain.
- Rebuilt the guide from a copy of `draft/src` (`review-guide-check/rebuild/`). It built with no warnings, and its text is identical to `draft/facilitator.pdf`.

## Verdict

**There are no must-fix findings.**

- Every answer, count and hand chain is correct against the final pages.
- Every problem number, page number, picture description, board size and page count matches the final PDFs.
- The overview is theorem-first, gives real proofs, and labels the computer-only facts as such.

The should-fix items are about usability: the spacing-comb materials, a completeness argument that is asserted but not shown, the K–1 recording load in Problem 6, and one missing sentence in the overview about the general theorems.

## 1. Correctness: everything checks

Each claim was checked independently (`check.out`):

| Claim in the guide | Result |
|---|---|
| Good strips for n = 3…9 are 6, 10, 14, 20, 16, 6, 0. The six 8-strips are as listed. There are 16 equally spaced threes on 9 squares (7/5/3/1 by spacing). | correct |
| K–1 P1: 10, 20 and 16 good strips. RRBB, RRBBRR and RRBBRRB are good. RBRB is good. RBRBRB and RBRBRBR fail at 1, 3, 5. | correct |
| K–1 P2: each strip has exactly one answer (BRRBBRR, RRBBRRBB, RBRBBRBR, RBBRRBBR). The 7-strip chain 1B, 4B, 7R, 5B, 6R is forced. Strip 2 forces 3; with 4 red it gets stuck, with 4 blue the rest is forced. Strips 3 and 4 force 3, 6 and 2 respectively; with square 1 blue they get stuck (at 8 and at 7), with square 1 red the rest is forced. | correct |
| Reversals and swaps of the 8-strips. Every 8-strip dies at square 9 in both colours, at the stated threes. | correct |
| Overview proof for nine: both cases, every step forced. The reverse-and-swap reduction is valid. | correct |
| Strip game: a draw with perfect play on 3–8 squares; the second player wins on 9. | correct |
| Random safe play on 9 (exact): the first player loses 0.5617 of games (0.5599 of all games on move 9); the second player is stuck on move 8 in 0.438. On 8 the strip fills in 0.182 of games. | matches "a little over half…", "one in five" |
| Two colours, doubling counts: 1..4 only RBBR/BRRB; 1..5 impossible; the 4–5 P4 dead ends are exactly RBR/BRB. | correct |
| Three colours: 1..13 works with 18 colourings in exactly the three stated partitions, 7 free; 1..14 has none; the largest class has 5 numbers (so 6 green counters suffice). Greedy R, B, G colouring stops after 7. In-order dead ends with 1 red: 278 in all, 6 of them reaching 13. | correct |
| No doubling: 1..8 only RRBRBBBR or its swap; 1..9 impossible; all three case chains in 4–5 P9 consist of forced steps. | correct |
| Five dots: 12 of 1,024; by red outside lines 5/0/3/2 the counts are 1/1/5/5; both figure colourings are valid. | correct |
| Six dots: minimum 2 one-colour triangles, reached by 1,760 colourings; 3 is reachable (5,760); the two-triangle figure has exactly 2; no 8-red/7-blue board avoids a triangle. | correct |
| Sim: the first player loses with perfect play (my solver visited 112,096 positions). | correct |

## 2. Agreement with the pages: everything checks

All of these match the final PDFs:

- **Problem and page citations.** K–1 P1–P6 on pp. 1, 2, 3, 4, 4 and 5–6. Grades 2–3 P1–P8 on pp. 1, 2, 3, 4, 4, 5, 6, 6. Grades 4–5 P1–P10 on pp. 1, 2, 3, 3, 4, 5, 5, 6, 7, 7.
- **Page counts.** 6 landscape, 6 and 7 pages.
- **Square sizes.** K–1 squares are 25 mm. The rule picture is half size (RRBRBR with the comb at 2, 4, 6, and the blue counters at 3 and 5 hidden).
- **Strips in the upper packets.** 15/13/11 mm.
- **Recording space.** Eight strips for six answers in 2–3 P2 and 4–5 P2. Six strips across K–1 pp. 5–6. Sixteen five-dot boards at 3.9 cm.
- **Sim pages.** Grades 2–3 p. 6 and Grades 4–5 p. 5, each with two boards.
- **Launch strip.** No packet has a 5-square strip.
- **Older-band rule picture.** The comb is at 2, 5, 8.

## 3. The overview

It meets the rule. It states each threshold with its assumptions: d ≥ 1 including neighbours, x = y allowed (and what changes when it is not), and a crossing is not a dot. It gives followable proofs for 9 squares, 5 numbers, R(3,3), the 12 five-dot colourings and Goodman's "at least two". It marks the 13/14, strip-game and Sim results as computer facts. It has a separate paragraph on experiments, conjectures and explanations, and a band map with prerequisites. All of this comes before any solution.

## Should-fix

**S1. Overview, p. 1: add the general theorems and their limits.**
The title promises "past a size, the pattern cannot be avoided", but the overview only states three instances. An adult leading the 4–5 "how the threshold moves" conversation needs to know that a threshold always exists, and where knowledge stops.

Fix: add two sentences. "Each threshold is the first case of a general theorem. For any number of colours and any length of pattern, a long enough strip, run of numbers or set of dots must contain it (van der Waerden 1927, Schur 1916, Ramsey 1930). The thresholds grow fast and are known only for small cases: three colours need 27 squares for a three, four colours need 45 numbers for sums (1..44 can be coloured), and four dots of one colour need 18 dots. Children meet three instances; the general theorem is adult background."

**S2. K–1 P6 (p. 4) and Grades 2–3 P2 (p. 4): show why each start gives exactly one 8-strip.**
"Each start allows exactly one good 8-strip" is the whole completeness argument, and it is only asserted. A parent volunteer cannot check a child's "we found them all" from it. I checked that each start needs at most one try:

- **RR:** 3 must be blue. If 4 is red, then 6 and 7 are blue (2,4,6; 1,4,7), 5 is red (5,6,7), and 8 can be neither (2,5,8; 6,7,8). So 4 is blue, and the rest is forced: RRBBRRBB.
- **RBR:** 5 must be blue (1,3,5) and 8 red (2,5,8). If 4 is red, 6 is blue (4,6,8), and 7 can be neither (1,4,7; 5,6,7). So 4 is blue: RBRBBRBR.
- **RBB:** everything is forced. 4 is red (2,3,4), 7 blue (1,4,7), 5 red (3,5,7), 6 blue (4,5,6), 8 red (6,7,8): RBBRRBBR.

Fix: print these three lines once (under K–1 P6) and point to them from 2–3 P2 and 4–5 P2.

**S3. Spacing combs, p. 2: the dimensions do not suit the K–1 pages.**

- *The problem.* A 5 cm card with notches 3 cm deep leaves a 2 cm spine. That spine extends from 0.5 to 2.5 cm beyond the strip being checked. The K–1 page strips are only 1.1 cm apart (P1), 1.3 cm (P2) and 1.6 cm (P6). So on every middle strip, the comb lies across the neighbouring strip's counters.
- *Tolerance.* Notches exactly 25 mm wide also leave only about ±1.5 mm before a neighbour's counter shows.
- *Fix.* Specify card 3.5 cm tall with notches 2.7 cm deep, which leaves a 0.8 cm spine that ends within the 1.1 cm gap. Optionally make the notches 23 mm wide, centred on the squares (starting 6 mm from the end). Alternatively, tell children to clear or colour a finished strip before checking the next one. Either way, add "comb over a middle strip" to the Status list of untested items.

**S4. Combs, p. 2: print a template and re-estimate preparation.**
"No template is printed". Twenty combs have to be measured and cut by ruler, with up to three notches each, and the guide budgets 25 minutes for that. The outline assumed print-and-cut ("about 15 minutes for five sets"), and the model weeks forecast 20–35 minutes for all preparation.

Fix: add a final guide page with the four combs drawn at 100% (one set per landscape Letter sheet of card, cut lines and spacing labels shown), and tell the volunteer to print five on card. Then re-estimate the time, or keep "about an hour" and say that the combs take most of it.

**S5. K–1 P6 recording and materials (pp. 2 and 4).**

- *The problem.* Ten counters of each colour let a pair keep only two 8-strips built at once, since each needs 4 red and 4 blue. Problem 6 does not say to colour. So children must either remember strips or rebuild them, which is the bookkeeping the page review flagged (review.md §3.7).
- *A related gap.* The K–1 key says "a crayon dot in each square", but the per-pair list has only coloured pencils.
- *Fix.* Under K–1 P6, say: "When a strip passes every comb, dot each square in crayon, then move the counters to the next strip." Add red and blue crayons to the K–1 materials. Or offer 24 of each colour per K–1 pair, so that all six strips can stay built and be compared for swaps and reversals.

## Minor

These are listed in page order.

- **M1. Launch, p. 2: the first try gives away a discovery.** Starting from RBRBR shows children that taking turns fails at spacing 2. That is the main obstacle K–1 P1 would otherwise let them discover, and the page 1 rule picture already shows a spacing-2 catch. Consider dropping "(taking turns with colours is a natural first try)" and letting children propose the first try. If they alternate, use it.
- **M2. Launch figure, p. 2: the spacing-1 comb is drawn wrongly.** The figure draws it with three windows, but the text says one 75 mm notch. Draw a single window.
- **M3. Launch, p. 2: the strip is too small for the whole group.** Eleven children cannot all see a 12.5 cm strip. Make the board version the default, and spell out the paper comb: "cover squares 2 and 4 with two sheets of paper to make the spacing-2 comb".
- **M4. K–1 P3, p. 3: an untested prediction.** "Children will conclude this from many tries" predicts what children will do in an unpiloted session. Write "may".
- **M5. K–1 P4, p. 4: "Play honestly" is ambiguous.** Say instead "make real safe moves; do not throw games", since no simple perfect strategy is known.
- **M6. Grades 2–3 P3, p. 4: ambiguous wording.** "Your list of eight" can be read as eight items. Say "your list of good 8-strips".
- **M7. Grades 4–5 P3, p. 5: give the mirrored chain.** For an adult following a child who does both cases by hand: with 4 red, 5 blue and 6 blue, 7 is red (5,6,7), 1 blue (1,4,7), 3 red (1,3,5), 2 blue (2,3,4) and 9 red (1,5,9). Then 8 can be neither colour (7,8,9 would be all red; 2,5,8 all blue).
- **M8. Grades 4–5 P5, p. 5: say which counts to accept.** "Find every way" has three defensible answers: 12 on labelled dots, 4 if turning counts as the same, and 2 if swapping colours also counts. Ask the child what they count as different.
- **M9. Grades 4–5 P8, p. 6: give the referee a counting routine.** Counting one-colour triangles means checking 20 triples per board. Suggest: "at each dot, for each pair of same-colour lines, check the third line; each one-colour triangle is found once at each of its three corners".
- **M10. Grades 4–5 P9, p. 6: an unneeded step.** The second case lists "7 blue", which the argument does not need. End with "8 red (3+5), 9 red (3+6), and 1+8=9 is all red".
- **M11. Pacing, p. 3: P5 belongs with P4.** K–1 P5's question "would you rather go first or second on 9?" is the payoff of the P4 game, and the guide calls it "the prize". Yet the first route stops at P4 and leaves P5 for the return visit. Suggest asking that question aloud at the end of the first visit's games.
- **M12. Return visit, p. 3: K–1 Sim needs a caveat.** It is not on the K–1 pages, and the parent has to spot triangles. Mark it as optional and untested, and point to the "three fingers on three dots" check.
- **M13. Script references, pp. 1 and 6.** `check_guide.py` is process detail, and the script will not travel with the guide. Write "computer-checked" instead, and keep the script name in the source package.
- **M14. Brevity.** The fifteenth-line Sim argument appears three times (overview, 2–3 P7, 4–5 P6). The five-dot completeness argument appears twice (overview, 4–5 P5). Keep one full version of each and point to it.
- **M15. Sources, p. 6: two related references are not named.** The resource manifest also lists JRMF "Color Triangles" and Early Family Math "K–3 Sim Triangle". Neither is in this checkout. Name them as related references that were not consulted.

## What works and should be kept

- **Correctness.** Every printed answer is correct and complete. The "find every" answers give the full lists, the impossibility claims have checked forced chains, and the computer-only results are labelled.
- **Agreement with the pages.** The guide is keyed exactly to the final pages, including recording-space counts that tell adults when a child is done.
- **The overview.** It is genuinely theorem-first:
  - It gives the mixed-corner proof of "at least two triangles" and the 12-loop count.
  - It explains that the convention changes the answer (8 without doubling).
  - Its experiment, conjecture and explanation paragraph is clear ("a list is complete when its cases are organized, not when ideas run out").
- **The launch.** It uses a non-task 5-strip with an input, one step and an output, says "nothing about longer strips", and gives later one-minute demonstrations of sums and triangles on non-task instances.
- **Practical adult knowledge.**
  - Check only the threes through the newest counter.
  - Either player may use either colour.
  - The random-play statistics explain why children may first answer "no" on 8 squares and why "second on 9" is not obvious.
  - In 4–5 P4, the guide separates a dead end from the limit.
  - The ninth-square extension argument, with the warning "the argument is only as good as the list".
- **Staffing.** It contains the line "choosing colours for a child means the task is too big". The status is honest about what has not been tested, the watch-for list is labelled as hypotheses, and the sources section is honest that nothing was read.

## Summary

There are no must-fix findings. My own code confirms every answer, and every reference matches the final PDFs. The overview meets the theorem-first rule.

Fix five things before approval:

1. Add one sentence on the general theorems (S1).
2. Show the one-try trees that prove the six 8-strips are complete (S2).
3. Resize the combs to fit the 1.1–1.6 cm gaps between K–1 strips (S3).
4. Print a comb template and adjust the preparation estimate (S4).
5. Settle how K–1 records Problem 6 with ten counters of each colour (S5).
